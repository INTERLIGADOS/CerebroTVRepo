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

import logging
import re
import requests
import urlparse
import os
import math
from time import time


class M3U8(object):

	def __init__(self, url=None, cookies=None, headers=None):
		self.url = url
		self._cookies = cookies
		self._headers = headers

		self._programs = []			# main list of programs & bandwidth
		self._files = {} 			# the current program playlist
		self._first_sequence = 0	# the first sequence to start fetching
		self._last_sequence = 0		# the last sequence, to compute reload delay
		self._reload_delay = 5		# the initial reload delay
		self._update_tries = None	# the number consecutive reload tries
		self._last_content = None
		self._endlist = False		# wether the list ended and should not be refreshed
		self.target_duration = None
		self._encryption_method = None
		self._key_url = None
		self._key = None
		self._iv = None
		self._end_sequence = None
		self.load_time = 0
		self.version = 1
		self._last_f = None

	def endlist(self):
		return self._endlist

	def has_programs(self):
		return len(self._programs) != 0

	def get_target_dura(self):
		return self.target_duration

	def get_program_playlist(self, program_id=None, bitrate=None):
		# return the (uri, dict) of the best matching playlist
		if not self.has_programs():
			printl("PL has not programs!",self,'E')
			raise Exception('PL has not programs!')

		_, best = min((abs(int(x['BANDWIDTH']) - bitrate), x)
				for x in self._programs)
		return best['uri'], best

	def reload_delay(self):
		# return the time between request updates, in seconds
		if self._endlist or not self._last_sequence:
			raise Exception('ELST or nor LSEQ')

		if self._update_tries == 0:
			ld = self._files[self._last_sequence]['duration']
			self._reload_delay = min(self.target_duration * 3, ld)
			d = max(0, self._reload_delay - self.load_time)
		elif self._update_tries == 1:
			d = self._reload_delay * 0.5
		elif self._update_tries == 2:
			d = self._reload_delay * 1.5
		else:
			d = self._reload_delay * 3.0

		return d

	def has_files(self):
		return len(self._files) != 0

	def iter_files(self):
		# return an iter on the playlist media files
		if not self.has_files():
			return

		if not self._endlist:
			current = max(self._first_sequence, self._last_sequence - 2)
		else:
			# treat differently on-demand playlists?
			current = self._first_sequence

		while True:
			try:
				if not self._files.has_key(current):
					current = max(self._first_sequence, current)
				f = self._files[current]
				current += 1
				yield f
				if (f.has_key('endlist')):
					break
			except GeneratorExit:
				break
			except StopIteration:
				yield None
			except KeyError:
				yield None
			except:
				break

	def update(self, content):
		# update this "constructed" playlist,
		# return wether it has actually been updated
		if self._last_content and content == self._last_content:
			self._update_tries += 1
			return False

		start_time = time()
		self._update_tries = 0
		self._last_content = content

		def get_lines_iter(c):
			c = c.decode("utf-8-sig")
			for l in c.splitlines():
				if l.startswith('#EXT'):
					yield l
				elif l.startswith('#'):
					pass
				else:
					yield l

		def getKey(l):
			#print l
			self._key = None
			a = l[18:].find(',')
			if a > 0:
				self._encryption_method = l[18:18+a].strip()
				if self._encryption_method == 'AES-128':
					a=l.find('URI="')
					if a > 0:
						j=l[a+5:].find('"')
						self._key_url = l[a+5:j+a+5]
						j += a+5
						a=l[j:].find('IV=')
						if a > 0:
							self._iv = l[j+a+5:].strip().decode("hex")
						url = urlparse.urljoin(self.url, self._key_url)
						opener = requests.session()
						response = opener.get(url, cookies=self._cookies, headers=self._headers)
						self._key = response.content
					else:
						printl("No Encryption Key-URI found",self,'E')
				else:
					printl("No valid Encryption Method found",self,'E')
			else:
				self._encryption_method = l[18:].strip()
			if not self._encryption_method:
				printl("No Encryption method found",self,'E')

		extinf_start = content.find('#EXTINF')
		if extinf_start < 0: content += '\n'
		self._lines = get_lines_iter(content[:extinf_start])
		try:
			first_line = self._lines.next()
		except:
			return False
		if not first_line.startswith('#EXTM3U'):
			printl('Invalid first line:\n%r' % content,self,'E')
			raise Exception('Invalid first line: %r' % first_line)

		self.target_duration = None
		i = 0
		last_bw = '-1'
		extinf_list = []
		for l in self._lines:
			if l.startswith('#EXT-X-STREAM-INF'):
				def to_dict(l):
					i = re.findall('(?:[\w-]*="[\w\.\,]*")|(?:[\w-]*=[\w]*)', l)
					d = {v.split('=')[0]: v.split('=')[1].replace('"','') for v in i}
					return d
				d = to_dict(l[18:])
				uri = self._lines.next()
				if 'googlevideo.com' in uri:
					a = uri.find('/itag/')
					if a > 0:
						b = uri.find('/',a+6,a+10)
						itag = int(uri[a+6:b]) if b > 0 else 0
						if itag not in (91,92,93,94,95,96,132,151,300): continue
				if d['BANDWIDTH'] != last_bw:
					last_bw = d['BANDWIDTH']
					uri = urlparse.urljoin(self.url, uri)
					d['uri'] = uri
					self._add_playlist(d)
			elif l.startswith('#EXT-X-TARGETDURATION'):
				self.target_duration = int(l[22:])
			elif l.startswith('#EXT-X-MEDIA-SEQUENCE'):
				i = self.media_sequence = int(l[22:])
				if self._last_f != None:
					y = content.rfind(self._last_f, extinf_start)
					if y > 0:
						y = content.find('#EXTINF', y)
						if y > 0:
							extinf_start = y
							i = self._last_sequence
						else:
							extinf_start = 0
					else:
						self._first_sequence = 0
			elif l.startswith('#EXT-X-VERSION'):
				self.version = int(l[15:])
			elif l.startswith('#EXT-X-PROGRAM-DATE-TIME'):
				#print l
				pass
			elif l.startswith('#EXT-X-BYTE-SIZE'):
				#print l
				pass
			elif l.startswith('#EXT-X-BYTERANGE'):
				#print l
				pass
			elif l.startswith('#EXT-X-DATERANGE'):
				#print l
				pass
			elif l.startswith('#EXT-X-CUEPOINT'):
				#print l
				pass
			elif l.startswith('#EXT-X-PROGRAM-DATE-TIME'):
				#print l
				pass
			elif l.startswith('#EXT-X-INDEPENDENT-SEGMENTS'):
				#print l
				pass
			elif l.startswith('#EXT-X-PLAYLIST-TYPE'):
				#print l
				pass
			elif l.startswith('#EXT-X-ALLOW-CACHE'):
				pass
			elif l.startswith('#EXT-X-KEY'):
				getKey(l)
			elif len(l.strip()) != 0:
				print l

		if extinf_start > 0:

			def proc_extinf_list(extinf_list):
				_len = len(extinf_list)
				a = _len - 5 if not self._endlist and _len >= 5 else 0
				for item in extinf_list[a:]:
					_i, _l, _f = item
					if _f == None:
						self._files[_i]['endlist'] = True
					else:
						if _f.startswith('./'): _f = _f[2:]
						v = _l[8:].split(',')
						d = dict(file=_f,
								title=v[1].strip(),
								duration=math.trunc(float(v[0])) if self.version < 3 else float(v[0]),
								sequence=_i)
						_i += 1
						self._set_file(_i, d)
				if _i > self._last_sequence:
					self._last_f = _f
					self._last_sequence = _i
				else: self._last_f = None

				if self._endlist:
					self._end_sequence = self._last_sequence - 1

			self._lines = get_lines_iter(content[extinf_start:])
			for l in self._lines:
				if l.startswith('#EXTINF'):
					while True:
						f = self._lines.next().strip()
						if not f.startswith('#'):
							break
					extinf_list.append((i,l,f))
					i += 1
				elif l.startswith('#EXT-X-DISCONTINUITY'):
					#print l
					pass
				elif l.startswith('#EXT-X-ENDLIST'):
					self._endlist = True
					extinf_list.append((i,None,None))
					#print l
				elif len(l.strip()) != 0:
					print l

			proc_extinf_list(extinf_list)
			del extinf_list[:]
			result = True
		elif extinf_start == 0:
			result = False
			self._update_tries += 1
		else: result = True

		if not self.has_programs() and not self.target_duration:
			printl("Invalid HLS stream: no programs & no duration",self,'E')
			raise Exception("Invalid HLS stream: no programs & no duration")

		del content
		self.load_time = time() - start_time
		return result

	def _add_playlist(self, d):
		self._programs.append(d)

	def _set_file(self, sequence, d):
		if not self._first_sequence:
			self._first_sequence = sequence
		elif sequence < self._first_sequence:
			self._first_sequence = sequence
		self._files[sequence] = d

	def __repr__(self):
		return "M3U8 %r %r" % (self._programs, self._files)