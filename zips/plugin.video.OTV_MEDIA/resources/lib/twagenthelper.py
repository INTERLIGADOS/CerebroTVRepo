# -*- coding: utf-8 -*-

import re
import base64
from time import time
from io import BytesIO
import os

import tw_util
from tw_util import *
__TW_VER__ = tw_util.__TW_VER__

MDEBUG = False
MDEBUG_TIMESTAMP = False

class TwRedirectAgent(BrowserLikeRedirectAgent):
	def _handleRedirect(self, response, method, uri, headers, redirectCount):
		locationHeaders = response.headers.getRawHeaders('location', [])
		if locationHeaders:
			location = self._resolveLocation(uri, locationHeaders[0])
			headers.addRawHeader('tw_location', location)
			d_print('tw_location:',location)
		return BrowserLikeRedirectAgent._handleRedirect(self, response, method, uri, headers, redirectCount)

class TunnelError(Exception):
	"""An HTTP CONNECT tunnel could not be established by the proxy."""

class TunnelingTCP4ClientEndpoint(TCP4ClientEndpoint):
	"""An endpoint that tunnels through proxies to allow HTTPS downloads. To
	accomplish that, this endpoint sends an HTTP CONNECT to the proxy.
	The HTTP CONNECT is always sent when using this endpoint, I think this could
	be improved as the CONNECT will be redundant if the connection associated
	with this endpoint comes from the pool and a CONNECT has already been issued
	for it.
	"""

	_responseMatcher = re.compile('HTTP/1\.. 200')

	def __init__(self, reactor, host, port, proxyConf, contextFactory,
				timeout=30, bindAddress=None, scheme=b'https'):
		proxyHost, proxyPort, self._proxyAuthHeader = proxyConf
		super(TunnelingTCP4ClientEndpoint, self).__init__(reactor, proxyHost,
			proxyPort, timeout, bindAddress)
		self._tunnelReadyDeferred = Deferred()
		self._tunneledHost = host
		self._tunneledPort = port
		self._scheme = scheme
		self._contextFactory = contextFactory

	def requestTunnel(self, protocol):
		"""Asks the proxy to open a tunnel."""
		tunnelReq = 'CONNECT %s:%s HTTP/1.1\r\n' % (self._tunneledHost,
												self._tunneledPort)
		if self._proxyAuthHeader:
			tunnelReq += 'Proxy-Authorization: %s\r\n' % self._proxyAuthHeader
		tunnelReq += '\r\n'
		protocol.transport.write(tunnelReq)
		self._protocolDataReceived = protocol.dataReceived
		protocol.dataReceived = self.processProxyResponse
		self._protocol = protocol
		return protocol

	def processProxyResponse(self, bytes):
		"""Processes the response from the proxy. If the tunnel is successfully
		created, notifies the client that we are ready to send requests. If not
		raises a TunnelError.
		"""
		self._protocol.dataReceived = self._protocolDataReceived
		if  TunnelingTCP4ClientEndpoint._responseMatcher.match(bytes):
			if self._scheme == b'https':
				self._protocol.transport.startTLS(self._contextFactory, self._protocolFactory)
			self._tunnelReadyDeferred.callback(self._protocol)
		else:
			self._tunnelReadyDeferred.errback(
				TunnelError('Could not open CONNECT tunnel.'))

	def connectFailed(self, reason):
		"""Propagates the errback to the appropriate deferred."""
		self._tunnelReadyDeferred.errback(reason)

	def connect(self, protocolFactory):
		self._protocolFactory = protocolFactory
		connectDeferred = super(TunnelingTCP4ClientEndpoint,
								self).connect(protocolFactory)
		connectDeferred.addCallback(self.requestTunnel)
		connectDeferred.addErrback(self.connectFailed)
		return self._tunnelReadyDeferred

class TunnelingAgent(Agent):
	"""An agent that uses a L{TunnelingTCP4ClientEndpoint} to make HTTPS
	downloads. It may look strange that we have chosen to subclass Agent and not
	ProxyAgent but consider that after the tunnel is opened the proxy is
	transparent to the client; thus the agent should behave like there is no
	proxy involved.
	"""

	def __init__(self, reactor, proxyConf, contextFactory=None,
				connectTimeout=None, bindAddress=None, pool=None):
		super(TunnelingAgent, self).__init__(reactor, contextFactory, connectTimeout, bindAddress, pool)
		self._proxyConf = proxyConf
		self._contextFactory = contextFactory

	if __TW_VER__ >= [15, 0, 0]:
		def _getEndpoint(self, uri):
			return TunnelingTCP4ClientEndpoint(
				self._reactor, uri.host, uri.port, self._proxyConf,
				self._contextFactory, self._endpointFactory._connectTimeout,
				self._endpointFactory._bindAddress, uri.scheme)
	else:
		def _getEndpoint(self, scheme, host, port):
			return TunnelingTCP4ClientEndpoint(
				self._reactor, host, port, self._proxyConf,
				self._contextFactory, self._connectTimeout,
				self._bindAddress, scheme)

class Request(object):

	def __init__(self, url, callback=None, method='GET', headers=None, body=None,
				cookies=None, meta=None, encoding='utf-8', errback=None):

		self._encoding = encoding
		self.method = str(method).upper()
		self._set_url(url)
		self._set_body(body)

		assert callback or not errback, "Cannot use errback without a callback"
		self.callback = callback
		self.errback = errback

		self.cookies = cookies or {}
		self.headers = Headers()
		if headers:
			for n, v in headers.iteritems():
				self.headers.addRawHeader(n, v)

		self._meta = dict(meta) if meta else None

	@property
	def meta(self):
		if self._meta is None:
			self._meta = {}
		return self._meta

	def _get_url(self):
		return self._url

	def _set_url(self, url):
		self._url = url

		if ':' not in self._url:
			raise ValueError('Missing scheme in request url: %s' % self._url)

	url = property(_get_url, _set_url)

	def _get_body(self):
		return self._body

	def _set_body(self, body):
		if body is None:
			self._body = b''
		else:
			self._body = tw_util.to_bytes(body, self.encoding)

	body = property(_get_body, _set_body)

	@property
	def encoding(self):
		return self._encoding

	def __str__(self):
		return "<%s %s>" % (self.method, self.url)

	__repr__ = __str__

	def copy(self):
		"""Return a copy of this Request"""
		return self.replace()

class _ResponseReader(Protocol):

	def __init__(self, finished, txresponse, request):
		self._finished = finished
		self._txresponse = txresponse
		self._request = request
		self.currentbytes = 0.0
		self.totalbytes = txresponse.length
		if not request.meta.get('file'):
			self._bodybuf = BytesIO()
			self.th_cb_deferred = self.progress_callback = None
		else:
			if txresponse.headers.getRawHeaders("accept-ranges", [None])[0] == 'bytes':
				r = txresponse.headers.getRawHeaders("Content-Range", [None])[0]
				if r:
					d_print('[_ResponseReader] Partial:',r)
					if r:
						self.currentbytes = float(r[6:].split('-',1)[0])
						if r[6:].rfind('/') > 0:
							self.totalbytes = float(r[6:].split('/',1)[-1])
						else:
							self.totalbytes += self.currentbytes
					d_print('currentbytes:',self.currentbytes)
					d_print('totalbytes:',self.totalbytes)

			self._bodybuf = request.meta.get('file')
			self.progress_callback = request.meta.get('progress_callback')
			self.th_cb_deferred = request.meta.get('th_cb_deferred')

	def dataReceived(self, bodyBytes):
		if not self._bodybuf:
			return
		try:
			self._bodybuf.write(bodyBytes)
		except IOError,e:
			d_print('[Tw dataReceived] err:',e,self._request.meta.get('outputfile')+':','bytes written:',self.currentbytes,'of:',self.totalbytes)
			self._bodybuf = None
			self._finished.errback(failure.Failure())
		else:
			self.currentbytes += len(bodyBytes)
			if self.totalbytes and self.progress_callback:
				self.progress_callback(self.currentbytes, self.totalbytes)
			if self._request.meta.get('file'):
				if self.th_cb_deferred and not self.th_cb_deferred.called:
					if self.currentbytes >= self._request.meta.get('threshold'):
						body = self._request.meta.get('outputfile')
						self.th_cb_deferred.callback(body)

	def connectionLost(self, reason):
		if self.th_cb_deferred and not self.th_cb_deferred.called:
			d_print('connectionLost: th_cb_deferred canceled')
			self.th_cb_deferred.cancel()

		if self._finished.called:
			return

		if not self._request.meta.get('file'):
			body = self._bodybuf.getvalue()
		else:
			self._bodybuf.close()
			body = self._request.meta.get('outputfile')

		if reason.check(ResponseDone):
			self._finished.callback((self._txresponse, body, None))
		elif reason.check(PotentialDataLoss):
			self._finished.callback((self._txresponse, body, ['partial']))
		else:
			self._finished.errback(reason)

class TwAgent(object):

	_Agent = Agent
	_ProxyAgent = ProxyAgent
	_TunnelingAgent = TunnelingAgent
	_RedirectAgent = TwRedirectAgent
	_CookieAgent = CookieAgent
	_ContentDecoderAgent = ContentDecoderAgent

	def __init__(self, contextFactory=None, timeout=10, bindAddress=None, pool=None, followRedirect=False, redirectLimit=None, gzip_decoding=False, cookies=None):
		self._contextFactory = contextFactory
		self._timeout = timeout if type(timeout) == tuple else (timeout, timeout)
		self._bindAddress = bindAddress
		self._pool = pool
		self._cookies = cookies
		self._followRedirect = followRedirect
		self._redirectLimit = redirectLimit
		self._gzip_decoding = gzip_decoding

	def _get_agent(self, request):
		bindaddress = request.meta.get('bindaddress') or self._bindAddress
		proxy = request.meta.get('proxy')
		if proxy:
			_, _, proxyHost, proxyPort, proxyParams = tw_util._parse(proxy)
			scheme = tw_util._parse(request.url)[0]
			omitConnectTunnel = proxyParams.find('noconnect') >= 0
			if not omitConnectTunnel:
				proxyConf = (proxyHost, proxyPort, request.headers.getRawHeaders("Proxy-Authorization", [None])[0])
				return self._TunnelingAgent(reactor, proxyConf,
					contextFactory=self._contextFactory, connectTimeout=self._timeout[0],
					bindAddress=bindaddress, pool=self._pool)
			else:
				endpoint = TCP4ClientEndpoint(reactor, proxyHost, proxyPort, timeout=self._timeout[0], bindAddress=bindaddress)
				return self._ProxyAgent(endpoint)

		return self._Agent(reactor, contextFactory=self._contextFactory,
			connectTimeout=self._timeout[0], bindAddress=bindaddress, pool=self._pool)

	def download_request(self, request):
		agent = self._get_agent(request)

		# gzip Agent
		if self._gzip_decoding:
			agent = self._ContentDecoderAgent(agent, [('gzip', GzipDecoder)])

		if self._cookies != None:
			agent = self._CookieAgent(agent, self._cookies)

		#_agent = agent
		if self._followRedirect and not request.meta.get('getlocation'):
			agent = self._RedirectAgent(agent, redirectLimit=self._redirectLimit)

		# request details
		url = urldefrag(request.url)[0]
		method = request.method
		if isinstance(agent, self._TunnelingAgent):
			request.headers.removeHeader('Proxy-Authorization')
		bodyproducer = StringProducer(request._body) if request._body else None

		d_print("req url:'%s',%s" % (method,url))
		d_print('postdata:',request.body)
		d_print('req. headers:',request.headers)
		start_time = time()
		d = agent.request(method, url, headers=request.headers, bodyProducer=bodyproducer)
		# set download latency
		d.addCallback(self._cb_latency, request, start_time)
		# response body is ready to be consumed
		d.addCallback(self._cb_bodyready, request)
		d.addCallback(self._cb_bodydone, request, url)

		# check download timeout
		if self._timeout[1]:
			self._timeout_cl = reactor.callLater(self._timeout[1], d.cancel)
			d.addBoth(self._cb_timeout, request, url, self._timeout[1])
		return d

	def _cb_timeout(self, result, request, url, timeout):
		if self._timeout_cl.active():
			self._timeout_cl.cancel()
			return result
		raise TimeoutError("Getting %s took longer than %s seconds." % (url, timeout))

	def _cb_latency(self, result, request, start_time):
		request.meta['download_latency'] = time() - start_time
		return result

	def _cb_bodyready(self, txresponse, request):
		# deliverBody hangs for responses without body
		if txresponse.length == 0:
			return txresponse, '', None

		def _cancel(_):
			d_print('_cancel()')
			#txresponse._transport._producer.loseConnection()
			if __TW_VER__ >= [11, 1, 0]:
				txresponse._transport._producer.abortConnection()
			else:
				txresponse._transport._producer.loseConnection()

		d = Deferred(_cancel)
		txresponse.deliverBody(_ResponseReader(d, txresponse, request))

		return d

	def _cb_bodydone(self, result, request, url):
		txresponse, body, flags = result
		status = int(txresponse.code)

		if request.meta.get('addlocation'):
			location = request.headers.getRawHeaders("tw_location", [url])[-1]
			d_print('addlocation:',location)
			return body, location
		elif request.meta.get('getlocation'):
			if 'Forbidden' in txresponse.phrase:
				return txresponse.phrase
			else:
				location = txresponse.headers.getRawHeaders("location", [url])[0]
				d_print('getlocation:',location)
				return location

		return result[1]

class StringProducer:
	implements(IBodyProducer)

	def __init__(self, body):
		self.body = body
		self.length = len(body)

	def startProducing(self, consumer):
		consumer.write(self.body)
		return succeed(None)

	def pauseProducing(self):
		pass

	def stopProducing(self):
		pass

class TwHTTP11PoolHelper(object):

	def __init__(self, maxPersistentPerHost=2, retryAutomatically=True):
		self._pool = HTTPConnectionPool(reactor, persistent=False)
		self._pool.maxPersistentPerHost = maxPersistentPerHost
		self._pool.retryAutomatically = retryAutomatically
		self._pool._factory.noisy = False
		self._disconnect_timeout = 1

	def close(self):
		d = self._pool.closeCachedConnections()
		# closeCachedConnections will hang on network or server issues, so
		# we'll manually timeout the deferred.
		#
		# Twisted issue addressing this problem can be found here:
		# https://twistedmatrix.com/trac/ticket/7738.
		#
		# closeCachedConnections doesn't handle external errbacks, so we'll
		# issue a callback after `_disconnect_timeout` seconds.
		delayed_call = reactor.callLater(self._disconnect_timeout, d.callback, [])

		def cancel_delayed_call(result):
			if delayed_call.active():
				delayed_call.cancel()
			return result

		d.addBoth(cancel_delayed_call)
		return d

class TwAgentHelper(object):

	DEBUG_HEADER = False
	_Agent = TwAgent

	def __init__(self, p_user=None, p_pass=None, proxy_url=None,  gzip_decoding=True, followRedirect=True, use_tls=False, cookieJar=None, redirectLimit=20, headers=None, timeout=10, pool=None):
		d_print( "Twisted Agent in use", __TW_VER__)
		self.headers = headers.copy() if headers else {}
		self.proxy_url = proxy_url
		self.useProxy = self.proxy_url != None
		self.body = None
		if self.useProxy:
			if p_user and p_pass:
				auth = 'Basic ' + base64.b64encode("%s:%s" % (p_user, p_pass)).strip()
				self.headers['Proxy-Authorization'] = auth
		self.agent = self._Agent(contextFactory=TwClientContextFactory(), followRedirect=followRedirect, redirectLimit=redirectLimit, gzip_decoding=gzip_decoding, cookies=cookieJar, timeout=timeout, pool=pool)

	def getRedirectedUrl(self, url, redir=True):
		d_print( "getRedirectedUrl: ", url)
		request = Request(url, method='HEAD', headers=self.headers)
		request.meta['getlocation'] = True
		return self.agent.download_request(request)

	def getWebPage(self, url, method='GET', postdata=None, addlocation=False):
		d_print( "getWebPage:",url)
		request = Request(url, method=method, body=postdata, headers=self.headers)
		request.meta['proxy'] = self.proxy_url
		request.meta['addlocation'] = addlocation
		d_print( 'agent type',self.agent)
		return self.agent.download_request(request)

def twAgentGetPage(url, method='GET', postdata=None, agent="Twisted PageGetter", addlocation=False, **kwargs):
	twAgent = TwAgentHelper(**kwargs)
	if agent:
		twAgent.headers['User-Agent'] = agent
	request = Request(url, method=method, body=postdata, headers=twAgent.headers)
	request.meta['addlocation'] = addlocation
	request.meta['proxy'] = twAgent.proxy_url
	return twAgent.agent.download_request(request)

class TwDownloader(object):
	def __init__(self, url, outputfile, method='GET', postdata=None, agent="MP HTTP Downloader", use_pipe=False, supportPartial=False, **kwargs):
		self.twAgent = TwAgentHelper(**kwargs)
		if agent:
			self.twAgent.headers['User-Agent'] = agent
		self.request = Request(url, method=method, body=postdata, headers=self.twAgent.headers)
		self.request.meta['proxy'] = self.twAgent.proxy_url
		self.request.meta['outputfile'] = outputfile
		self.request.meta['use_pipe'] = use_pipe
		self.request.meta['supportPartial'] = supportPartial
		self.requestedPartial = 0

	def start(self, resume=False):
		d_print('start:')
		self.requestedPartial = self.setRangeHeader()
		try:
			self.openFile(partialContent=self.requestedPartial)
		except IOError:
			return fail(failure.Failure())
		else:
			self._deferred = self.twAgent.agent.download_request(self.request)
			self._deferred.addErrback(self.errorHandler)
			return self._deferred

	def setRangeHeader(self):
		return setMetaRangeHeader(self.request.meta, self.request.headers)

	def stop(self):
		if self._deferred != None and not self._deferred.called:
			self._deferred.cancel()

	def openFile(self, partialContent=0):
		openMetaFile(self.request.meta, partialContent)

	def errorHandler(self, failure):
		d_print('errorHandler:',str(failure))
		if 'file' in self.request.meta:
			self.request.meta['file'].close()
		failure.trap(twisted.internet.defer.CancelledError)
		return 'cancelled'

def twDownloadPage(url, outputfile, method='GET', postdata=None, agent="MP HTTP Downloader", **kwargs):
	return TwDownloader(url, outputfile, method=method, postdata=postdata, agent=agent, **kwargs).start()

class TwDownloadWithProgress(TwDownloader):
	def __init__(self, url, outputfile, method='GET', postdata=None, agent="MP HTTP Downloader", use_pipe=False, supportPartial=False, **kwargs):
		TwDownloader.__init__(self, url, outputfile, method=method, postdata=postdata, agent=agent, use_pipe=use_pipe, supportPartial=supportPartial, **kwargs)
		self._deferred = None

	def addProgress(self, progress_callback):
		self.request.meta['progress_callback'] = progress_callback

	def addThreshold(self, threshold='all'):
		def errorHandler(failure):
			d_print('errorHandler:',str(failure))
			failure.trap(twisted.internet.defer.CancelledError)
			return 'cancelled'

		return addMetaThreshold(self.request.meta, threshold).addErrback(errorHandler)

def setMetaRangeHeader(meta, headers):
	requestedPartial = 0
	if meta['supportPartial']:
		d_print('setRangeHeader:')
		if os.path.exists(meta['outputfile']):
			requestedPartial = os.path.getsize(meta['outputfile'])
		headers.setRawHeaders('Range',["bytes=%d-" % requestedPartial])
	return requestedPartial

def openMetaFile(meta, partialContent):
	if meta['use_pipe']:
		if os.access(meta['outputfile'], os.W_OK):
			os.remove(meta['outputfile'])
		os.mkfifo(meta['outputfile'])

	if partialContent:
		file = open(meta['outputfile'], 'rb+')
		file.seek(0, 2)
	else:
		file = open(meta['outputfile'], 'wb')
	meta['file'] = file

def addMetaThreshold(meta, threshold):
	if 'all' == threshold:
		meta['threshold'] = 2000000000
	else:
		meta['threshold'] = int(threshold)*1024*1024
	d = Deferred()
	meta['th_cb_deferred'] = d
	return d

def d_print(*args):
	import time
	if MDEBUG:
		if MDEBUG_TIMESTAMP:
			s = '%s - ' % time.strftime('%H:%M:%S',time.localtime())
		else:
			s = ''
		for arg in args:
			s += str(arg)
		print s

__all__ = ["__TW_VER__", "TwAgentHelper", "twAgentGetPage", "TwDownloader", "TwDownloadWithProgress", "twDownloadPage"]