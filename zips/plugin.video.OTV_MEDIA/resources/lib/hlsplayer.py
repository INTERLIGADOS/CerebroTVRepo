#-*- coding: utf-8 -*-
#from os import path as os_path, mkdir, rmdir, system, walk, stat as os_stat, listdir, access, F_OK, R_OK, W_OK
import base64
import re
import time
import urllib
import urllib2
import sys
import traceback
import socket
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from urllib import *
import urlparse

#import xbmc
import thread
import zlib
from StringIO import StringIO
import hmac
import hashlib
import base64
import threading 
import xbmcgui,xbmcplugin
import xbmc 
import hashlib
g_stopEvent=None
g_downloader=None
g_currentprocessor=None
proxy = None
use_proxy_for_chunks = False
maxbitrate = 0
simpleDownloader = False
auth = None
streamtype = 'HLSRETRY'
setResolved = False
swf = None
callbackpath = ''
callbackparam = ''
iconImage = 'DefaultVideo.png'

class Server(HTTPServer):
    """HTTPServer class with timeout."""

    def get_request(self):
        """Get the request and client address from the socket."""
        self.socket.settimeout(5.0)
        result = None
        while result is None:
            try:
                result = self.socket.accept()
            except socket.timeout:
                pass

        result[0].settimeout(1000)
        return result


class ThreadedHTTPServer(ThreadingMixIn, Server):
    """Handle requests in a separate thread."""
    pass


HOST_NAME = '127.0.0.1'
PORT_NUMBER = 55333

class hlsproxy:

    def start(self, stopEvent, port = PORT_NUMBER):
        global g_stopEvent
        global HOST_NAME
        print 'port', port, 'HOST_NAME', HOST_NAME
        g_stopEvent = stopEvent
        socket.setdefaulttimeout(10)
        server_class = ThreadedHTTPServer
        MyHandler.protocol_version = 'HTTP/1.1'
        httpd = server_class((HOST_NAME, port), MyHandler)
        print 'XBMCLocalProxy Starts - %s:%s' % (HOST_NAME, port)
        while True and not stopEvent.isSet():
            httpd.handle_request()

        httpd.server_close()
        print 'XBMCLocalProxy Stops %s:%s' % (HOST_NAME, port)

    def prepare_url(self, url, proxy = None, use_proxy_for_chunks = True, port = PORT_NUMBER, maxbitrate = 0, simpleDownloader = False, auth = None, streamtype = 'HDS', swf = None, callbackpath = '', callbackparam = ''):
        newurl = urllib.urlencode({'url': url,
         'proxy': proxy,
         'use_proxy_for_chunks': use_proxy_for_chunks,
         'maxbitrate': maxbitrate,
         'simpledownloader': simpleDownloader,
         'auth': auth,
         'streamtype': streamtype,
         'swf': swf,
         'callbackpath': callbackpath,
         'callbackparam': callbackparam})
        link = 'http://' + HOST_NAME + ':%s/' % str(port) + newurl
        return link


class MyHandler(BaseHTTPRequestHandler):
    """
    Serves a HEAD request
    """

    def do_HEAD(self):
        print 'XBMCLocalProxy: Serving HEAD request...'
        self.send_response(200)
        rtype = 'flv-application/octet-stream'
        self.send_header('Content-Type', rtype)
        self.end_headers()

    def do_GET(s):
        print 'XBMCLocalProxy: Serving GET request...'
        s.answer_request(True)

    def answer_request(self, sendData):
        global g_currentprocessor
        global g_downloader
        try:
            request_path = self.path[1:]
            querystring = request_path
            request_path = re.sub('\\?.*', '', request_path)
            if request_path.lower() == 'stop':
                sys.exit()
                return
            if request_path.lower() == 'favicon.ico':
                print 'dont have no icone here, may be in future'
                self.wfile.close()
                return
            if request_path.lower() == 'sendvideopart':
                print 'dont have no icone here, may be in future'
                self.send_response(200)
                rtype = 'video/mp2t'
                self.send_header('Content-Type', rtype)
                self.end_headers()
                initDone = True
                videourl = self.decode_videoparturl(querystring.split('?')[1])
                g_currentprocessor.sendVideoPart(videourl, self.wfile)
                return
            initDone = False
            url, proxy, use_proxy_for_chunks, maxbitrate, simpledownloader, auth, streamtype, swf, callbackpath, callbackparam = self.decode_url(request_path)
            print 'simpledownloaderxxxxxxxxxxxxxxx', simpledownloader
            if streamtype == '' or streamtype == None or streamtype == 'none':
                streamtype = 'HDS'
            if streamtype == 'HDS':
                print 'Url received at proxy', url, proxy, use_proxy_for_chunks, maxbitrate
                downloader = None
                if not downloader or downloader.live == True or not (downloader.init_done and downloader.init_url == url):
                    from f4mProxy.f4mDownloader import F4MDownloader
                    downloader = F4MDownloader()
                    if not downloader.init(self.wfile, url, proxy, use_proxy_for_chunks, g_stopEvent, maxbitrate, auth, swf):
                        print 'cannot init'
                        raise Exception('HDS.url failed to play\nServer down? check Url.')
                    g_downloader = downloader
                    print 'init...'
                enableSeek = False
                requested_range = self.headers.getheader('Range')
                if requested_range == None:
                    requested_range = ''
                srange, erange = (None, None)
                if downloader.live == False and len(requested_range) > 0 and not requested_range == 'bytes=0-0':
                    enableSeek = True
                    srange, erange = self.get_range_request(requested_range, downloader.total_frags)
                print 'PROXY DATA', downloader.live, enableSeek, requested_range, downloader.total_frags, srange, erange
                enableSeek = False
                framgementToSend = 0
                inflate = 1815002
                if enableSeek:
                    self.send_response(206)
                    rtype = 'flv-application/octet-stream'
                    self.send_header('Content-Type', rtype)
                    self.send_header('Accept-Ranges', 'bytes')
                    print 'not LIVE,enable seek', downloader.total_frags
                    totalsize = downloader.total_frags * inflate
                    framgementToSend = 1
                    erange = srange + framgementToSend * inflate
                    if erange >= totalsize:
                        erange = totalsize - 1
                    crange = 'bytes ' + str(srange) + '-' + str(int(erange)) + '/*'
                    print srange / inflate, erange / inflate, totalsize / inflate
                    self.send_header('Content-Length', str(totalsize))
                    self.send_header('Content-Range', crange)
                    etag = self.generate_ETag(url)
                    self.send_header('ETag', etag)
                    print crange
                    self.send_header('Last-Modified', 'Wed, 21 Feb 2000 08:43:39 GMT')
                    self.send_header('Cache-Control', 'public, must-revalidate')
                    self.send_header('Cache-Control', 'no-cache')
                    self.send_header('Pragma', 'no-cache')
                    self.send_header('features', 'seekable,stridable')
                    self.send_header('client-id', '12345')
                    self.send_header('Connection', 'close')
                else:
                    self.send_response(200)
                    rtype = 'flv-application/octet-stream'
                    self.send_header('Content-Type', rtype)
                    srange = None
            elif streamtype == 'SIMPLE' or simpledownloader:
                from f4mProxy.interalSimpleDownloader import interalSimpleDownloader
                downloader = interalSimpleDownloader()
                if not downloader.init(self.wfile, url, proxy, g_stopEvent, maxbitrate):
                    print 'init throw error because init'
                    raise Exception('SIMPLE.url failed to play\nServer down? check Url.')
                srange, framgementToSend = (None, None)
                self.send_response(200)
                rtype = 'flv-application/octet-stream'
                self.send_header('Content-Type', rtype)
                srange = None
            elif streamtype == 'TSDOWNLOADER':
                from f4mProxy.TSDownloader import TSDownloader
                downloader = TSDownloader()
                if not downloader.init(self.wfile, url, proxy, g_stopEvent, maxbitrate):
                    print 'cannot init but will continue to play'
                    raise Exception('TS.url failed to play\nServer down? check Url.')
                srange, framgementToSend = (None, None)
                self.send_response(200)
                rtype = 'video/mp2t'
                self.send_header('Content-Type', rtype)
                srange = None
            elif streamtype == 'HLS':
                from f4mProxy.hlsDownloader import HLSDownloader
                downloader = HLSDownloader()
                if not downloader.init(self.wfile, url, proxy, use_proxy_for_chunks, g_stopEvent, maxbitrate, auth):
                    print 'cannot init'
                    raise Exception('HLS.url failed to play\nServer down? check Url.')
                srange, framgementToSend = (None, None)
                self.send_response(200)
                rtype = 'flv-application/octet-stream'
                self.send_header('Content-Type', rtype)
                srange = None
            elif streamtype == 'HLSRETRY':
                from f4mProxy.HLSDownloaderRetry import HLSDownloaderRetry
                downloader = HLSDownloaderRetry()
                if not downloader.init(self.wfile, url, proxy, use_proxy_for_chunks, g_stopEvent, maxbitrate, auth, callbackpath, callbackparam):
                    print 'cannot init'
                    raise Exception('HLSR.url failed to play\nServer down? check Url.')
                srange, framgementToSend = (None, None)
                self.send_response(200)
                rtype = 'flv-application/octet-stream'
                self.send_header('Content-Type', rtype)
                srange = None
            elif streamtype == 'HLSREDIR':
                from f4mProxy.HLSRedirector import HLSRedirector
                downloader = HLSRedirector()
                g_currentprocessor = downloader
                if not downloader.init(self.wfile, url, proxy, use_proxy_for_chunks, g_stopEvent, maxbitrate, auth, callbackpath, callbackparam):
                    print 'cannot init'
                    raise Exception('HLSR.url failed to play\nServer down? check Url.')
                srange, framgementToSend = (None, None)
                self.send_response(200)
                rtype = 'application/vnd.apple.mpegurl'
                self.send_header('Content-Type', rtype)
                srange = None
            self.end_headers()
            if not srange == None:
                srange = srange / inflate
            initDone = True
            if sendData:
                downloader.keep_sending_video(self.wfile, srange, framgementToSend)
                print 'srange,framgementToSend', srange, framgementToSend
        except Exception as inst:
            traceback.print_exc()
            if not initDone:
                xbmc.executebuiltin("XBMC.Notification(F4mProxy,%s,4000,'')" % inst.message)
                self.send_error(404)
            print 'closed'

        self.finish()
        return

    def generate_ETag(self, url):
        md = hashlib.md5()
        md.update(url)
        return md.hexdigest()

    def get_range_request(self, hrange, file_size):
        if hrange == None:
            srange = 0
            erange = None
        else:
            try:
                hrange = str(hrange)
                splitRange = hrange.split('=')[1].split('-')
                srange = int(splitRange[0])
                erange = splitRange[1]
                if erange == '':
                    erange = int(file_size) - 1
            except:
                srange = 0
                erange = int(file_size - 1)

        return (srange, erange)

    def decode_videoparturl(self, url):
        print 'in params', url
        params = urlparse.parse_qs(url)
        received_url = params['url'][0].replace('\r', '')
        return received_url

    def decode_url(self, url):
        print 'in params', url
        params = urlparse.parse_qs(url)
        print 'params', params
        received_url = params['url'][0].replace('\r', '')
        print 'received_url', received_url
        use_proxy_for_chunks = False
        proxy = None
        try:
            proxy = params['proxy'][0]
            use_proxy_for_chunks = params['use_proxy_for_chunks'][0]
        except:
            pass

        maxbitrate = 0
        try:
            maxbitrate = int(params['maxbitrate'][0])
        except:
            pass

        auth = None
        try:
            auth = params['auth'][0]
        except:
            pass

        if auth == 'None' and auth == '':
            auth = None
        if proxy == 'None' or proxy == '':
            proxy = None
        if use_proxy_for_chunks == 'False':
            use_proxy_for_chunks = False
        simpledownloader = False
        try:
            simpledownloader = params['simpledownloader'][0]
            if simpledownloader.lower() == 'true':
                print 'params[simpledownloader][0]', params['simpledownloader'][0]
                simpledownloader = True
            else:
                simpledownloader = False
        except:
            pass

        streamtype = 'HDS'
        try:
            streamtype = params['streamtype'][0]
        except:
            pass

        if streamtype == 'None' and streamtype == '':
            streamtype = 'HDS'
        swf = None
        try:
            swf = params['swf'][0]
        except:
            pass

        callbackpath = ''
        try:
            callbackpath = params['callbackpath'][0]
        except:
            pass

        callbackparam = None
        try:
            callbackparam = params['callbackparam'][0]
        except:
            pass

        return (received_url,
         proxy,
         use_proxy_for_chunks,
         maxbitrate,
         simpledownloader,
         auth,
         streamtype,
         swf,
         callbackpath,
         callbackparam)


global PORT_NUMBER ## Warning: Unused global