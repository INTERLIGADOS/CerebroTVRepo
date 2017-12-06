# -*- coding: utf-8 -*-
#
#    Copyright (c) 2015 Billy2011, MediaPortal Team
#
# Copyright (C) 2009-2010 Fluendo, S.L. (www.fluendo.com).
# Copyright (C) 2009-2010 Marc-Andre Lureau <marcandre.lureau@gmail.com>

# This file may be distributed and/or modified under the terms of
# the GNU General Public License version 2 as published by
# the Free Software Foundation.
# This file is distributed without any warranty; without even the implied
# warranty of merchantability or fitness for a particular purpose.
# See "LICENSE" in the source distribution for more information.

from itertools import ifilter
import logging
import os, os.path
import tempfile
import urlparse
from Crypto.Cipher import AES
import struct
from cookielib import CookieJar
import urllib
from time import time
import math

from twisted.python import log
from twisted.internet import defer, reactor, task
from twisted.internet.task import deferLater
from twagenthelper import twAgentGetPage, TwHTTP11PoolHelper
import re, httplib, urllib, urllib2, os, cookielib, socket, sha, shutil, datetime, math, hashlib, random, json, md5, string, xml.etree.cElementTree, StringIO, Queue, threading, sys


from m3u8 import M3U8


from make_url import make_url

def getUserAgent():
	userAgents = [
		"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
		"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20120101 Firefox/35.0",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0",
		"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
		"Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
	]
	return random.choice(userAgents)

class HLSFetcher(object):

	def __init__(self, url, **options):

		self.program = options.get('program',1)
		self.hls_headers = options.get('headers',{})
		self.path = options.get('path',None)
		self.bitrate = options.get('bitrate',200000)
		self.nbuffer = options.get('buffer',5)
		self.n_segments_keep = options.get('keep',self.nbuffer+1)
		url = urllib.unquote(url)
		self.puser = options.get('puser')
		self.ppass = options.get('ppass')
		self.purl = options.get('purl')

		us = url.split('|')
		if len(us) > 1:
			self.url = us[0]
			for hd in us[1:]:
				self.hls_headers.update(dict(urlparse.parse_qsl(hd.strip())))
		else:
			self.url = url

		self.agent = self.hls_headers.pop('User-Agent', getUserAgent())
		if not self.path:
			self.path = tempfile.mkdtemp()

		self._program_playlist = None
		self._file_playlist = None
		self._cookies = CookieJar()
		self._cached_files = {} 	# sequence n -> path
		self._run = True
		self._poolHelper = TwHTTP11PoolHelper(retryAutomatically=True)

		self._files = None 			# the iter of the playlist files download
		self._next_download = None 	# the delayed download defer, if any
		self._file_playlisted = None # the defer to wait until new files are added to playlist
		self._new_filed = None
		self._seg_task = None

	def _get_page(self, url):
		url = url.encode("utf-8")
		if 'HLS_RESET_COOKIES' in os.environ.keys():
			self._cookies.clear()

		timeout = 10
		return twAgentGetPage(url, agent=self.agent, cookieJar=self._cookies, headers=self.hls_headers, timeout=timeout, pool=self._poolHelper._pool, proxy_url=self.purl, p_user=self.puser, p_pass=self.ppass)

	def _download_page(self, url, path, file):
		def _decrypt(data):
			def num_to_iv(n):
				iv = struct.pack(">8xq", n)
				return b"\x00" * (16 - len(iv)) + iv

			if not self._file_playlist._iv:
				iv = num_to_iv(file['sequence'])
				aes = AES.new(self._file_playlist._key, AES.MODE_CBC, iv)
			else:
				aes = AES.new(self._file_playlist._key, AES.MODE_CBC, self._file_playlist._iv)
			return aes.decrypt(data)

		d = self._get_page(url)
		if self._file_playlist._key:
			d.addCallback(_decrypt)
		return d

	def _download_segment(self, f):
		url = make_url(self._file_playlist.url, f['file'])
		name = 'seg_' + next(tempfile._get_candidate_names())
		path = os.path.join(self.path, name)
		d = self._download_page(url, path, f)
		if self.n_segments_keep != 0:
			file = open(path, 'wb')
			d.addCallback(lambda x: file.write(x))
			d.addBoth(lambda _: file.close())
			d.addCallback(lambda _: path)
			d.addErrback(self._got_file_failed)
			d.addCallback(self._got_file, url, f)
		else:
			d.addCallback(lambda _: (None, path, f))
		return d

	def delete_cache(self, f):
		bgFileEraser = eBackgroundFileEraser.getInstance()
		keys = self._cached_files.keys()
		for i in ifilter(f, keys):
			filename = self._cached_files[i]
			bgFileEraser.erase(str(filename))
			del self._cached_files[i]

	def delete_all_cache(self):
		bgFileEraser = eBackgroundFileEraser.getInstance()
		for path in self._cached_files.itervalues():
			bgFileEraser.erase(str(path))
		self._cached_files.clear()

	def _got_file_failed(self, e):
		if self._new_filed:
			self._new_filed.errback(e)
			self._new_filed = None

	def _got_file(self, path, url, f):
		self._cached_files[f['sequence']] = path
		if self.n_segments_keep != -1:
			self.delete_cache(lambda x: x <= f['sequence'] - self.n_segments_keep)
		if self._new_filed:
			self._new_filed.callback((path, url, f))
			self._new_filed = None
		return (path, url, f)

	def _get_next_file(self):
		next = self._files.next()
		if next:
			return self._download_segment(next)
		elif not self._file_playlist.endlist():
			self._seg_task.stop()
			self._file_playlisted = defer.Deferred()
			self._file_playlisted.addCallback(lambda x: self._get_next_file())
			self._file_playlisted.addCallback(self._next_file_delay)
			self._file_playlisted.addCallback(self._seg_task.start)
			return self._file_playlisted

	def _handle_end(self, failure):
		failure.trap(StopIteration)
		print "End of media"

	def _next_file_delay(self, f):
		if f == None: return 0
		delay = f[2]["duration"]
		if self.nbuffer > 0:
			for i in range(0,self.nbuffer):
				if self._cached_files.has_key(f[2]['sequence'] - i):
					return delay
			delay = 0
		elif self._file_playlist.endlist():
			delay = 1
		return delay

	def _get_files_loop(self, res=None):
		if not self._seg_task:
			self._seg_task = task.LoopingCall(self._get_next_file)
		d = self._get_next_file()
		if d != None:
			self._seg_task.stop()
			d.addCallback(self._next_file_delay)
			d.addCallback(self._seg_task.start)
			d.addErrback(self._handle_end)

	def _playlist_updated(self, pl):
		if pl and pl.has_programs():
			# if we got a program playlist, save it and start a program
			self._program_playlist = pl
			(program_url, _) = pl.get_program_playlist(self.program, self.bitrate)
			return self._reload_playlist(M3U8(program_url, self._cookies, self.hls_headers))
		elif pl and pl.has_files():
			# we got sequence playlist, start reloading it regularly, and get files
			self._file_playlist = pl
			if not self._files:
				self._files = pl.iter_files()
			if not pl.endlist():
				reactor.callLater(pl.reload_delay(), self._reload_playlist, pl)
			if self._file_playlisted:
				self._file_playlisted.callback(pl)
				self._file_playlisted = None
		else:
			raise Exception('Playlist has no valid content.')
		return pl

	def _got_playlist_content(self, content, pl):
		if not pl.update(content) and self._run:
			# if the playlist cannot be loaded, start a reload timer
			d = deferLater(reactor, pl.reload_delay(), self._fetch_playlist, pl)
			d.addCallback(self._got_playlist_content, pl)
			return d
		return pl

	def _fetch_playlist(self, pl):
		d = self._get_page(pl.url)
		return d

	def _reload_playlist(self, pl):
		if self._run:
			d = self._fetch_playlist(pl)
			d.addCallback(self._got_playlist_content, pl)
			d.addCallback(self._playlist_updated)
			return d
		else:
			return None

	def get_file(self, sequence):
		d = defer.Deferred()
		keys = self._cached_files.keys()
		try:
			endlist = sequence == self._file_playlist._end_sequence
			sequence = ifilter(lambda x: x >= sequence, keys).next()
			filename = self._cached_files[sequence]
			d.callback((filename, endlist))
		except:
			d.addCallback(lambda x: self.get_file(sequence))
			self._new_filed = d
			keys.sort()
		return d

	def _start_get_files(self, x):
		self._new_filed = defer.Deferred()
		self._get_files_loop()
		return self._new_filed

	def start(self):
		if self._run:
			self._files = None
			d = self._reload_playlist(M3U8(self.url, self._cookies, self.hls_headers))
			d.addCallback(self._start_get_files)
			return d

	def stop(self):
		self._run = False
		self._poolHelper.close()
		if self._seg_task != None:
			self._seg_task.stop()
		if self._new_filed != None:
			self._new_filed.cancel()
		reactor.callLater(1, self.delete_all_cache)