# -*- coding: utf-8 -*-
#    HTTP-Player for MediaPortal
#
#    Copyright (c) 2015 Billy2011, MediaPortal Team
#
# This file may be distributed and/or modified under the terms of
# the GNU General Public License version 2 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE" in the source distribution for more information.

import os
import Queue
from twisted.web.server import NOT_DONE_YET
from functools import partial


CHUNK_SZ = 4096

class GSTPlayer:

	def __init__(self, request, keep=3):
		self._playing = False
		self._cb = None
		self._pcb = None
		self._request = request
		self._streamqueue = Queue.Queue()
		self.playerReady = True
		self._proxy_infos = None
		self._seeking = False
		self._clean_seek_headers = False
		self.set_seek_headers = False
		self.bytes_sent = 0L
		self.content_size = '*'

	def initProxyInfos(self, infos):
		self._proxy_infos = infos
		self.bytes_sent = 0L

	def doSeek(self, request):
		self._seeking = True
		self._request = request
		if request.requestHeaders.hasHeader('range'):
			r_range = request.requestHeaders.getRawHeaders('range')[0].split('bytes=')[-1].split('-')[0]
			r_range = long(r_range)
			if r_range >= self.bytes_sent:
				self.bytes_sent = r_range
				request.setResponseCode(206)
				if not self._streamqueue.empty():
					self.set_seek_headers
					return self.sendSegm()
				else:
					self._request.setHeader('Content-Range', 'bytes=%d-%d/%s' % (r_range, r_range-1, self.content_size))
					self._request.write(b"")
					if self.content_size == '*':
						return self.play()
					else:
						self._seeking = False
						return

			for item in self._proxy_infos['seek_cache']:
				c_range = range(item['bytes_range'], item['bytes_range'] + item['bytes_size'])
				if r_range in c_range:
					request.setResponseCode(206)
					self.set_seek_headers = True
					return self.sendSegm(item, item['bytes_range'])

			self._seeking = False
		else:
			self._seeking = False

	def play(self):
		print 'Play'
		if self._seeking:
			self._seeking = False
		self._playing = True
		self._on_about_to_play

	def stop(self):
		self._playing = False
		self._request = None
		print 'Stop'

	def set_uri(self, fpath):
		if fpath[0]:
			self._streamqueue.put(fpath)
		else:
			return

		if self.playerReady:
			self.sendSegm()

	def sendSegm(self, s_cache_item=None, r_range=None):
		self.playerReady = endlist = False
		while True:
			if s_cache_item != None:
				filepath = s_cache_item['filepath']
			else: filepath = ""

			if not self._request or (self._streamqueue.empty() and not s_cache_item):
				break
			if not filepath:
				filepath, endlist = self._streamqueue.get()
				if endlist:
					self._request.setResponseCode(200)
					self.set_seek_headers = True
			else:
				endlist = False
			try:
				size = os.path.getsize(filepath)
			except IOError, e:
				printl('File i/o error:'+str(e),self,'E')
				raise Exception(e)
				break
			else:
				with open(filepath, 'rb') as f:
					count = 0
					if self.set_seek_headers:
						if r_range == None:
							bytes_range = self.bytes_sent
						else: bytes_range = r_range
						self._request.setHeader('Content-Range', 'bytes=%d-%d/*' % (bytes_range, bytes_range+size-1))
						if endlist:
							self.content_size = str(bytes_range+size)
						self._clean_seek_headers = True
					elif self._clean_seek_headers:
						self._request.removeHeader('Content-Range')
						self._request.setResponseCode(200)
						self._clean_seek_headers = False

					self._request.write(f.read())
					count = size

				if s_cache_item == None:
					self._proxy_infos['seek_cache'].append({})
					self._proxy_infos['seek_cache'][-1]['bytes_range'] = self.bytes_sent
					if len(self._proxy_infos['seek_cache']) > 2:
						del self._proxy_infos['seek_cache'][0]
					self.bytes_sent += size
					self._proxy_infos['seek_cache'][-1]['bytes_size'] = size
					self._proxy_infos['seek_cache'][-1]['filepath'] = filepath
					self._on_about_to_finish()
				else:
					s_cache_item = None

				if self._seeking and not endlist:
					self.play()
		if endlist:
			self._request.finish()
			return NOT_DONE_YET
		else:
			self.playerReady = True

	def _on_about_to_finish(self, p=None):
		if self._cb:
			self._cb()

	def connect_about_to_finish(self, cb):
		self._cb = cb

	def connect_about_to_play(self, cb):
		self._pcb = cb

	def _on_about_to_play(self, p=None):
		if self._pcb:
			self._pcb()

	def finishPlayer(self,request):
		print 'HLS-Player finished.'
		self.stop()
		self._seeking = False
		if request and not request._disconnected:
			request.finish()
			return NOT_DONE_YET