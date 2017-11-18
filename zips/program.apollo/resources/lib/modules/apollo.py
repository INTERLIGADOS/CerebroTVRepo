# -*- coding: utf-8 -*-

'''
	Exodus Add-on
	Copyright (C) 2016 Exodus

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from requests import get
from shutil import rmtree

import re,sys,json,time,xbmc,urllib,xbmcgui, platform
import hashlib,urllib,os,zlib,base64,codecs,xmlrpclib

try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

from resources.lib.modules import control
from resources.lib.modules import cleantitle
from resources.lib.modules import playcount

from socket import create_connection,gethostbyname
try:
	host = gethostbyname("www.google.com")
	s = create_connection((host, 80), 2)
except:
	xbmcgui.Dialog().ok("Apollo Group","Unable to connect to server. Check your internet connection. (E07)")
	sys.exit()
	pass

from re import compile, I
def CheckMac(Am):
	regex = compile("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", I)
	return bool(regex.match(Am))
	
def GetMacAddress():
	if xbmc.getCondVisibility('system.platform.android'):
		try:
			Am = os.popen("cat /sys/class/net/eth0/address").read().strip()
			if CheckMac(Am) and not Am[:11]=="00:00:00:00":
				return Am.strip().replace(":","")
		except:	pass
		try:
			Am = os.popen("netcfg | grep 'eth0' | grep -o '[^ ]*.$'").read().strip()
			if CheckMac(Am) and not Am[:11]=="00:00:00:00":
				return Am.strip().replace(":","")
		except:	pass
	return 0
		
class apollo(xbmc.Player):
	def __init__ (self):
		xbmc.Player.__init__(self)
	
	def setAdvanceBuffer(self):
		AdvFile = xbmc.translatePath(os.path.join('special://profile', 'advancedsettings.xml'))
		if os.path.exists(AdvFile):
			i = xbmcgui.Dialog().yesno("Apollo Group","Setting advance buffer setting","will remove current advancedsettings.xml. Continue?")
		else:
			i = 1
		if not i == 0:
			try:
				KodiVer = int(xbmc.getInfoLabel("System.BuildVersion")[:2])
				xml = []
				xml.append("<advancedsettings>\n")
				if KodiVer > 16:
					xml.append('\t<cache>\n')
					xml.append('\t\t<buffermode>1</buffermode>\n')
					xml.append('\t\t<memorysize>139460608</memorysize>\n')
					xml.append('\t\t<readfactor>20</readfactor>\n')
					xml.append('\t</cache>\n')
					xml.append('\t<network>\n')
					xml.append('\t\t<curlclienttimeout>30</curlclienttimeout>\n')
					xml.append('\t\t<curllowspeedtime>30</curllowspeedtime> \n')
					xml.append('\t\t<curlretries>2</curlretries>\n')
					xml.append('\t</network>\n')
				else:
					xml.append('\t<network>\n')
					xml.append('\t\t<buffermode>1</buffermode>\n')
					xml.append('\t\t<cachemembuffersize>139460608</cachemembuffersize>\n')
					xml.append('\t\t<readbufferfactor>20</readbufferfactor>\n')
					xml.append('\t\t<curlclienttimeout>30</curlclienttimeout>\n')
					xml.append('\t\t<curllowspeedtime>30</curllowspeedtime>\n')
					xml.append('\t\t<curlretries>2</curlretries>\n')
					xml.append('\t</network>\n')
				xml.append("</advancedsettings>")
				outF = open(AdvFile, 'wb')
				outF.write("".join(xml))
				outF.close()
				
				xbmcgui.Dialog().ok("Apollo Group", "Buffer advacne setting approve","Reset kodi to take change take effect")
			except: pass

	def cleanCache(self):
		i = xbmcgui.Dialog().yesno("Apollo Group","Are you sure you want to delete","all your 'Apollo Group Addon' setting ?")
		if not i == 0:
			try:
				rmtree(control.dataPath)
				xbmcgui.Dialog().ok("Apollo Group", "Apollo Setting deleted")
			except: pass
	
	def tvguide(self):
		json.loads(unicode(xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method":"GUI.ActivateWindow","params":{"window":"tvguide"}, "id": 1}'), 'utf-8', errors='ignore'))

	def logout(self):
		response = get(control.apollo_link+'logout/?token='+control.addon().getSetting('apollo.token'))
		control.addon().setSetting('apollo.account', "Free Account")
		control.addon().setSetting('apollo.paid', "false")
		control.addon().setSetting('device.streams', "0")
		control.addon().setSetting('device.networks', "0")
		control.addon().setSetting('apollo.token',"0")
		control.addon().openSettings()

	def GetMedia(self,imdb,season,episode):
		try:
			self.playlogin()
			play_link = control.apollo_link+'play/?'
			mac = GetMacAddress()
			
			if mac:
				play_link = play_link+'&mac='+mac
			if imdb=="9999":
				play_link = play_link+'&token=%s&channel=%s'%(control.addon().getSetting('apollo.token'),season)
			else:
				play_link = play_link+'&token=%s&imdb=%s&season=%s&episode=%s'%(control.addon().getSetting('apollo.token'),imdb,season,episode)
			response = get(play_link)
			data = json.loads(response.text)
		except:
			control.infoDialog("Our Servers are down for maintenance, for more info visit FB @ApolloGroupTV", icon='WARNING',time=20000)
			return 0
			pass
			
		if 'error' in data:
			control.infoDialog(data['error'], icon='WARNING',time=20000)
			print "**** Apollo ERROR: {0}".format(data['error'])
			if not 'link' in data:
				return 0
		if 'msg' in data:
			xbmcgui.Dialog().ok("Apollo Group MSG", data["msg"])
			xbmc.sleep(5000)
		if 'link' in data:
			url = data["link"]+'|'+urllib.urlencode({'Keep-Alive':'True','Connection':'keep-alive'})
			return url
		return 0
	
	def playlogin(self):
		if len(control.addon().getSetting('apollo.token'))>10:
			response = get(control.apollo_link+'token/?token='+control.addon().getSetting('apollo.token'))
			data = json.loads(response.text)
			if not "error" in data:
				return #REFRESH

		mac = GetMacAddress()
		login_link = control.apollo_link+'login/?'
		if mac:
			login_link += '&mac='+mac			
		response = get(login_link+'&email='+control.addon().getSetting('apollo.email')+'&password='+control.addon().getSetting('apollo.password'))
		data = json.loads(response.text)
		if not "error" in data and "token" in data:
			control.addon().setSetting('apollo.token', data["token"])
			return 

		free_link = control.apollo_link+'free/?'
		if mac:
			free_link += '&mac='+mac			
		response = get(free_link)
		data = json.loads(response.text)
		control.addon().setSetting('apollo.token', data["token"])

	def login(self):
		xbmc.executebuiltin('Notification(Apollo Group,"Please wait, checking account info.", {0}, {1})'.format(2500,os.path.join( control.addonPath ,"icon.png")))
		login_link = control.apollo_link+'login/?'
		mac = GetMacAddress()
		if mac:
			login_link += '&mac='+mac			
		response = get(login_link+'&email='+control.addon().getSetting('apollo.email')+'&password='+control.addon().getSetting('apollo.password'))
		data = json.loads(response.text)
		if "error" in data:
			xbmcgui.Dialog().ok("Apollo Group Error", data["error"])
			return
		if "token" in data:
			control.addon().setSetting('apollo.token', data["token"])

		response = get(control.apollo_link+'account/?&token='+control.addon().getSetting('apollo.token'))
		data = json.loads(response.text)
		if "account" in data:
			if control.addon().getSetting('apollo.account')<>data["account"]:
				control.addon().setSetting('apollo.account', data["account"])
		if "stream" in data:
			if control.addon().getSetting('device.streams')<>data["stream"]:
				control.addon().setSetting('device.streams', data["stream"])
		if "network" in data:
			if control.addon().getSetting('device.networks')<>data["network"]:
				control.addon().setSetting('device.networks', data["network"])

		if control.addon().getSetting('apollo.account')<>"Free Account":
			control.addon().setSetting('apollo.paid', "true")
		control.addon().openSettings()

	def run(self, title, year, season, episode, imdb, tvdb, url, meta):
		try:
			if control.addon().getSetting('apollo.account')<>"Free Account":
				control.addon().setSetting('apollo.paid', "true")
			xbmc.executebuiltin('Notification(CerebroTV,"Please wait, connecting...", {0}, {1})'.format(3000,os.path.join( control.addonPath ,"icon.png")))

			if imdb=="9999": # Play Channel
				url = self.GetMedia(imdb,season,episode)
				if not url:
					return
				print "**** Apollo Play: {0}".format('live/{0}'.format(season))
				poster = 'https://github.com/Apollo2000/Repo/raw/master/TVLogos/'+str(season)+'.png'
				item = control.item(path=url,label=title)
				item.setInfo(type='Video', infoLabels = "")
				try: item.setArt({'poster': poster})
				except: pass
				item.setProperty('Video', 'true')
				item.setProperty('IsPlayable', 'true')
				control.player.play(url, item)
				control.resolve(int(sys.argv[1]), True, item)
			else:
				control.sleep(200)

				self.totalTime = 0 ; self.currentTime = 0

				self.content = 'movie' if season == None or episode == None else 'episode'

				self.title = title ; self.year = year
				self.name = urllib.quote_plus(title) + urllib.quote_plus(' (%s)' % year) if self.content == 'movie' else urllib.quote_plus(title) + urllib.quote_plus(' S%02dE%02d' % (int(season), int(episode)))
				self.name = urllib.unquote_plus(self.name)
				self.season = '%01d' % int(season) if self.content == 'episode' else 0
				self.episode = '%01d' % int(episode) if self.content == 'episode' else 0

				self.DBID = None
				self.imdb = imdb if not imdb == None else '0'
				self.tvdb = tvdb if not tvdb == None else '0'
				self.ids = {'imdb': self.imdb, 'tvdb': self.tvdb}
				self.ids = dict((k,v) for k, v in self.ids.iteritems() if not v == '0')

				self.offset = bookmarks().get(self.name, self.year)

				poster, thumb, meta = self.getMeta(meta)

				url = self.GetMedia(self.imdb,self.season,self.episode)

				if not url:
					return
				item = control.item(path=url)
				item.setArt({'icon': thumb, 'thumb': thumb, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster})
				item.setInfo(type='Video', infoLabels = meta)
				item.setProperty('IMDBNumber', imdb)
				
				if 'plugin' in control.infoLabel('Container.PluginName'):
					control.player.play(url, item)

				control.resolve(int(sys.argv[1]), True, item)

				control.window.setProperty('script.trakt.ids', json.dumps(self.ids))

				self.keepPlaybackAlive()

				control.window.clearProperty('script.trakt.ids')
		except:
			return


	def getMeta(self, meta):
		try:
			meta = json.loads(meta)
			poster = meta['poster'] if 'poster' in meta else '0'
			thumb = meta['thumb'] if 'thumb' in meta else poster

			if poster == '0': poster = control.addonPoster()

			return (poster, thumb, meta)
		except:
			pass

		try:
			if not self.content == 'movie': raise Exception()

			meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties" : ["title", "originaltitle", "year", "genre", "studio", "country", "runtime", "rating", "votes", "mpaa", "director", "writer", "plot", "plotoutline", "tagline", "thumbnail", "file"]}, "id": 1}' % (self.year, str(int(self.year)+1), str(int(self.year)-1)))
			meta = unicode(meta, 'utf-8', errors='ignore')
			meta = json.loads(meta)['result']['movies']

			t = cleantitle.get(self.title)
			meta = [i for i in meta if self.year == str(i['year']) and (t == cleantitle.get(i['title']) or t == cleantitle.get(i['originaltitle']))][0]

			for k, v in meta.iteritems():
				if type(v) == list:
					try: meta[k] = str(' / '.join([i.encode('utf-8') for i in v]))
					except: meta[k] = ''
				else:
					try: meta[k] = str(v.encode('utf-8'))
					except: meta[k] = str(v)

			if not 'plugin' in control.infoLabel('Container.PluginName'):
				self.DBID = meta['movieid']

			poster = thumb = meta['thumbnail']

			return (poster, thumb, meta)
		except:
			pass

		try:
			if not self.content == 'episode': raise Exception()

			meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties" : ["title", "year", "thumbnail", "file"]}, "id": 1}' % (self.year, str(int(self.year)+1), str(int(self.year)-1)))
			meta = unicode(meta, 'utf-8', errors='ignore')
			meta = json.loads(meta)['result']['tvshows']

			t = cleantitle.get(self.title)
			meta = [i for i in meta if self.year == str(i['year']) and t == cleantitle.get(i['title'])][0]

			tvshowid = meta['tvshowid'] ; poster = meta['thumbnail']

			meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodes", "params":{ "tvshowid": %d, "filter":{"and": [{"field": "season", "operator": "is", "value": "%s"}, {"field": "episode", "operator": "is", "value": "%s"}]}, "properties": ["title", "season", "episode", "showtitle", "firstaired", "runtime", "rating", "director", "writer", "plot", "thumbnail", "file"]}, "id": 1}' % (tvshowid, self.season, self.episode))
			meta = unicode(meta, 'utf-8', errors='ignore')
			meta = json.loads(meta)['result']['episodes'][0]

			for k, v in meta.iteritems():
				if type(v) == list:
					try: meta[k] = str(' / '.join([i.encode('utf-8') for i in v]))
					except: meta[k] = ''
				else:
					try: meta[k] = str(v.encode('utf-8'))
					except: meta[k] = str(v)

			if not 'plugin' in control.infoLabel('Container.PluginName'):
				self.DBID = meta['episodeid']

			thumb = meta['thumbnail']

			return (poster, thumb, meta)
		except:
			pass


		poster, thumb, meta = '', '', {'title': self.name}
		return (poster, thumb, meta)


	def keepPlaybackAlive(self):
		pname = '%s.player.overlay' % control.addonInfo('id')
		control.window.clearProperty(pname)


		if self.content == 'movie':
			overlay = playcount.getMovieOverlay(playcount.getMovieIndicators(), self.imdb)

		elif self.content == 'episode':
			overlay = playcount.getEpisodeOverlay(playcount.getTVShowIndicators(), self.imdb, self.tvdb, self.season, self.episode)

		else:
			overlay = '6'


		for i in range(0, 240):
			if self.isPlayingVideo(): break
			xbmc.sleep(1000)


		if overlay == '7':

			while self.isPlayingVideo():
				try:
					self.totalTime = self.getTotalTime()
					self.currentTime = self.getTime()
				except:
					pass
				xbmc.sleep(2000)


		elif self.content == 'movie':

			while self.isPlayingVideo():
				try:
					self.totalTime = self.getTotalTime()
					self.currentTime = self.getTime()

					watcher = (self.currentTime / self.totalTime >= .9)
					property = control.window.getProperty(pname)

					if watcher == True and not property == '7':
						control.window.setProperty(pname, '7')
						playcount.markMovieDuringPlayback(self.imdb, '7')

					elif watcher == False and not property == '6':
						control.window.setProperty(pname, '6')
						playcount.markMovieDuringPlayback(self.imdb, '6')
				except:
					pass
				xbmc.sleep(2000)


		elif self.content == 'episode':

			while self.isPlayingVideo():
				try:
					self.totalTime = self.getTotalTime()
					self.currentTime = self.getTime()

					watcher = (self.currentTime / self.totalTime >= .9)
					property = control.window.getProperty(pname)

					if watcher == True and not property == '7':
						control.window.setProperty(pname, '7')
						playcount.markEpisodeDuringPlayback(self.imdb, self.tvdb, self.season, self.episode, '7')

					elif watcher == False and not property == '6':
						control.window.setProperty(pname, '6')
						playcount.markEpisodeDuringPlayback(self.imdb, self.tvdb, self.season, self.episode, '6')
				except:
					pass
				xbmc.sleep(2000)


		control.window.clearProperty(pname)


	def libForPlayback(self):
		try:
			if self.DBID == None: raise Exception()

			if self.content == 'movie':
				rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)
			elif self.content == 'episode':
				rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetEpisodeDetails", "params": {"episodeid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)

			control.jsonrpc(rpc) ; control.refresh()
		except:
			pass


	def idleForPlayback(self):
		for i in range(0, 200):
			if control.condVisibility('Window.IsActive(busydialog)') == 1: control.idle()
			else: break
			control.sleep(100)


	def onPlayBackStarted(self):
		control.execute('Dialog.Close(all,true)')
		if not self.offset == '0': self.seekTime(float(self.offset))
		subtitles().get(self.name, self.imdb, self.season, self.episode)
		self.idleForPlayback()


	def onPlayBackStopped(self):
		bookmarks().reset(self.currentTime, self.totalTime, self.name, self.year)


	def onPlayBackEnded(self):
		self.libForPlayback()
		self.onPlayBackStopped()


class subtitles:
	def get(self, name, imdb, season, episode):
		try:
			if not control.setting('subtitles') == 'true': raise Exception()


			langDict = {'Afrikaans': 'afr', 'Albanian': 'alb', 'Arabic': 'ara', 'Armenian': 'arm', 'Basque': 'baq', 'Bengali': 'ben', 'Bosnian': 'bos', 'Breton': 'bre', 'Bulgarian': 'bul', 'Burmese': 'bur', 'Catalan': 'cat', 'Chinese': 'chi', 'Croatian': 'hrv', 'Czech': 'cze', 'Danish': 'dan', 'Dutch': 'dut', 'English': 'eng', 'Esperanto': 'epo', 'Estonian': 'est', 'Finnish': 'fin', 'French': 'fre', 'Galician': 'glg', 'Georgian': 'geo', 'German': 'ger', 'Greek': 'ell', 'Hebrew': 'heb', 'Hindi': 'hin', 'Hungarian': 'hun', 'Icelandic': 'ice', 'Indonesian': 'ind', 'Italian': 'ita', 'Japanese': 'jpn', 'Kazakh': 'kaz', 'Khmer': 'khm', 'Korean': 'kor', 'Latvian': 'lav', 'Lithuanian': 'lit', 'Luxembourgish': 'ltz', 'Macedonian': 'mac', 'Malay': 'may', 'Malayalam': 'mal', 'Manipuri': 'mni', 'Mongolian': 'mon', 'Montenegrin': 'mne', 'Norwegian': 'nor', 'Occitan': 'oci', 'Persian': 'per', 'Polish': 'pol', 'Portuguese': 'por,pob', 'Portuguese(Brazil)': 'pob,por', 'Romanian': 'rum', 'Russian': 'rus', 'Serbian': 'scc', 'Sinhalese': 'sin', 'Slovak': 'slo', 'Slovenian': 'slv', 'Spanish': 'spa', 'Swahili': 'swa', 'Swedish': 'swe', 'Syriac': 'syr', 'Tagalog': 'tgl', 'Tamil': 'tam', 'Telugu': 'tel', 'Thai': 'tha', 'Turkish': 'tur', 'Ukrainian': 'ukr', 'Urdu': 'urd'}

			codePageDict = {'ara': 'cp1256', 'ar': 'cp1256', 'ell': 'cp1253', 'el': 'cp1253', 'heb': 'cp1255', 'he': 'cp1255', 'tur': 'cp1254', 'tr': 'cp1254', 'rus': 'cp1251', 'ru': 'cp1251'}

			quality = ['bluray', 'hdrip', 'brrip', 'bdrip', 'dvdrip', 'webrip', 'hdtv']


			langs = []
			try:
				try: langs = langDict[control.setting('subtitles.lang.1')].split(',')
				except: langs.append(langDict[control.setting('subtitles.lang.1')])
			except: pass
			try:
				try: langs = langs + langDict[control.setting('subtitles.lang.2')].split(',')
				except: langs.append(langDict[control.setting('subtitles.lang.2')])
			except: pass

			try: subLang = xbmc.Player().getSubtitles()
			except: subLang = ''
			if subLang == langs[0]: raise Exception()

			server = xmlrpclib.Server('http://api.opensubtitles.org/xml-rpc', verbose=0)
			token = server.LogIn('', '', 'en', 'XBMC_Subtitles_v1')['token']

			sublanguageid = ','.join(langs) ; imdbid = re.sub('[^0-9]', '', imdb)

			if not (season == None or episode == None):
				result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid, 'season': season, 'episode': episode}])['data']
				fmt = ['hdtv']
			else:
				result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid}])['data']
				try: vidPath = xbmc.Player().getPlayingFile()
				except: vidPath = ''
				fmt = re.split('\.|\(|\)|\[|\]|\s|\-', vidPath)
				fmt = [i.lower() for i in fmt]
				fmt = [i for i in fmt if i in quality]

			filter = []
			result = [i for i in result if i['SubSumCD'] == '1']

			for lang in langs:
				filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in fmt)]
				filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in quality)]
				filter += [i for i in result if i['SubLanguageID'] == lang]

			try: lang = xbmc.convertLanguage(filter[0]['SubLanguageID'], xbmc.ISO_639_1)
			except: lang = filter[0]['SubLanguageID']

			content = [filter[0]['IDSubtitleFile'],]
			content = server.DownloadSubtitles(token, content)
			content = base64.b64decode(content['data'][0]['data'])
			content = str(zlib.decompressobj(16+zlib.MAX_WBITS).decompress(content))

			subtitle = xbmc.translatePath('special://temp/')
			subtitle = os.path.join(subtitle, 'TemporarySubs.%s.srt' % lang)

			codepage = codePageDict.get(lang, '')
			if codepage and control.setting('subtitles.utf') == 'true':
				try:
					content_encoded = codecs.decode(content, codepage)
					content = codecs.encode(content_encoded, 'utf-8')
				except:
					pass

			file = control.openFile(subtitle, 'w')
			file.write(str(content))
			file.close()

			xbmc.sleep(1000)
			xbmc.Player().setSubtitles(subtitle)
		except:
			pass


class bookmarks:
	def get(self, name, year='0'):
		try:
			offset = '0'

			if not control.setting('bookmarks') == 'true': raise Exception()

			idFile = hashlib.md5()
			for i in name: idFile.update(str(i))
			for i in year: idFile.update(str(i))
			idFile = str(idFile.hexdigest())

			dbcon = database.connect(control.bookmarksFile)
			dbcur = dbcon.cursor()
			dbcur.execute("SELECT * FROM bookmark WHERE idFile = '%s'" % idFile)
			match = dbcur.fetchone()
			self.offset = str(match[1])
			dbcon.commit()

			if self.offset == '0': raise Exception()

			minutes, seconds = divmod(float(self.offset), 60) ; hours, minutes = divmod(minutes, 60)
			label = '%02d:%02d:%02d' % (hours, minutes, seconds)
			label = (control.lang(32502) % label).encode('utf-8')

			try: yes = control.dialog.contextmenu([label, control.lang(32501).encode('utf-8'), ])
			except: yes = control.yesnoDialog(label, '', '', str(name), control.lang(32503).encode('utf-8'), control.lang(32501).encode('utf-8'))

			if yes: self.offset = '0'

			return self.offset
		except:
			return offset


	def reset(self, currentTime, totalTime, name, year='0'):
		try:
			if not control.setting('bookmarks') == 'true': raise Exception()

			timeInSeconds = str(currentTime)
			ok = int(currentTime) > 180 and (currentTime / totalTime) <= .92

			idFile = hashlib.md5()
			for i in name: idFile.update(str(i))
			for i in year: idFile.update(str(i))
			idFile = str(idFile.hexdigest())

			control.makeFile(control.dataPath)
			dbcon = database.connect(control.bookmarksFile)
			dbcur = dbcon.cursor()
			dbcur.execute("CREATE TABLE IF NOT EXISTS bookmark (""idFile TEXT, ""timeInSeconds TEXT, ""UNIQUE(idFile)"");")
			dbcur.execute("DELETE FROM bookmark WHERE idFile = '%s'" % idFile)
			if ok: dbcur.execute("INSERT INTO bookmark Values (?, ?)", (idFile, timeInSeconds))
			dbcon.commit()
		except:
			pass


