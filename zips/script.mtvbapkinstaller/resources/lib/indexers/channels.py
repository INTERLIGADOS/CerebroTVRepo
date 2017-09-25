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


from resources.lib.modules import cleangenre
from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import workers

import sys,re,json,urllib,urlparse,datetime,xbmc

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

control.moderator()

def getPassword():
	prefilledinput=''
	kb = xbmc.Keyboard(prefilledinput, 'Adults Section. Please enter password:')
	kb.setHiddenInput(True)
	kb.doModal()
	if (kb.isConfirmed()):
		password = kb.getText()
		return password
	else:
		return None

class channels:
	def __init__(self):
		self.list = [] ; self.items = []

		self.uk_datetime = self.uk_datetime()
		self.systime = (self.uk_datetime).strftime('%Y%m%d%H%M%S%f')
		self.imdb_by_query = 'http://www.omdbapi.com/?t=%s&y=%s'

		self.sky_now_link = 'http://epgservices.sky.com/5.1.1/api/2.0/channel/json/%s/now/nn/0'
		self.sky_programme_link = 'http://tv.sky.com/programme/channel/%s/%s/%s.json'


	def get(self,name): 
		if name==None:
			url = control.apollo_link+'?type=live&action=list&uuid=%s'%(control.addon().getSetting('uuid'))
			raw = urllib.urlopen(url)
			json_object = json.load(raw)
			for data in json_object:
				try: 
					if str(data['url'])=="0":
						url = str(data['id'])
					else:
						url = str(data['url'])
					self.list.append({'id': str(data['id']),'name': str(data['name']),'url':url})
				except: 
					print "####### ERROR Getting List from Server: %s"%str(data['id'])
					pass
		elif name>0:
			url = control.apollo_link+'?type=live&action=list&id=%s&uuid=%s'%(name,control.addon().getSetting('uuid'))
			if name==str(16): #Adults password
				password = getPassword()
				url += "&password="+password

			raw = urllib.urlopen(url)
			json_object = json.load(raw)
			
			for data in json_object:
				try: 
					self.list.append({'id': str(data['id']),'name': str(data['name'].encode('utf-8')),'title':str(data['title'].encode('utf-8')),'hd': str(data['hd']), 'url': str(data['url'].encode('utf-8')),'poster': control.apollo_static_link+"tvlogos/"+str(data['id'])+".png"})
				except:
					if str(data['id'])==str(999999):
						import xbmcgui
						dialog = xbmcgui.Dialog()
						dialog.ok("Adults Section","Bad password!")
					print "####### ERROR Getting List from Server: %s %s"%(str(data['id']),data)
					pass
		
			try: self.list = sorted(self.list, key=lambda k: k['name'])
			except: pass

		self.channelDirectory(self.list,name)
		return self.list

	def search(self, query=None):
		if control.infoLabel('Container.PluginName') == '':
			return control.dialog.ok('Exodus', control.lang(30518).encode('utf-8'), '', '')

		if not control.infoLabel('ListItem.Title') == '':
			self.query = control.window.getProperty('%s.channel.search' % control.addonInfo('id'))

		elif query == None:
			t = control.lang(30201).encode('utf-8')
			k = control.keyboard('', t) ; k.doModal()
			self.query = k.getText() if k.isConfirmed() else None

		else:
			self.query = query

		if (self.query == None or self.query == ''): return

		control.window.setProperty('%s.channel.search' % control.addonInfo('id'), self.query)

		search_link = control.apollo_link+'?action=search&type=live&search=%s' % urllib.quote_plus(self.query)
		raw = urllib.urlopen(search_link)
		json_object = json.load(raw)
		for data in json_object:
			try: 
				self.list.append({'id': str(data['id']),'name': str(data['name'].encode('utf-8')),'title':str(data['title']),'hd': str(data['hd']), 'url': str(data['url']),'poster': control.apollo_static_link+"tvlogos/"+str(data['id'])+".png"})
			except: 
				print "####### ERROR Getting List from Server: %s"%str(data['id'])
				pass
	
		try: self.list = sorted(self.list, key=lambda k: k['name'])
		except: pass

		self.channelDirectory(self.list,99)
		return self.list

	def sky_list(self, num, channel, id):
		try:
			url = self.sky_now_link % id
			result = client.request(url, timeout='10')
			result = json.loads(result)
			match = result['listings'][id][0]['url']

			dt1 = (self.uk_datetime).strftime('%Y-%m-%d')
			dt2 = int((self.uk_datetime).strftime('%H'))
			if (dt2 < 6): dt2 = 0
			elif (dt2 >= 6 and dt2 < 12): dt2 = 1
			elif (dt2 >= 12 and dt2 < 18): dt2 = 2
			elif (dt2 >= 18): dt2 = 3

			url = self.sky_programme_link % (id, str(dt1), str(dt2))
			result = client.request(url, timeout='10')
			result = json.loads(result)
			result = result['listings'][id]
			result = [i for i in result if i['url'] == match][0]

			year = result['d']
			year = re.findall('[(](\d{4})[)]', year)[0].strip()
			year = year.encode('utf-8')

			title = result['t']
			title = title.replace('(%s)' % year, '').strip()
			title = client.replaceHTMLCodes(title)
			title = title.encode('utf-8')

			self.items.append((title, year, channel, num))
		except:
			pass


	def items_list(self, i):
		try:
			url = self.imdb_by_query % (urllib.quote_plus(i[0]), i[1])
			item = client.request(url, timeout='10')
			item = json.loads(item)

			title = item['Title']
			title = client.replaceHTMLCodes(title)
			title = title.encode('utf-8')

			year = item['Year']
			year = re.sub('[^0-9]', '', str(year))
			year = year.encode('utf-8')

			imdb = item['imdbID']
			if imdb == None or imdb == '' or imdb == 'N/A': raise Exception()
			imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))
			imdb = imdb.encode('utf-8')

			poster = item['Poster']
			if poster == None or poster == '' or poster == 'N/A': poster = '0'
			if not ('_SX' in poster or '_SY' in poster): poster = '0'
			poster = re.sub('_SX\d*|_SY\d*|_CR\d+?,\d+?,\d+?,\d*','_SX500', poster)
			poster = poster.encode('utf-8')

			genre = item['Genre']
			if genre == None or genre == '' or genre == 'N/A': genre = '0'
			genre = genre.replace(', ', ' / ')
			genre = genre.encode('utf-8')

			duration = item['Runtime']
			if duration == None or duration == '' or duration == 'N/A': duration = '0'
			duration = re.sub('[^0-9]', '', str(duration))
			duration = duration.encode('utf-8')

			rating = item['imdbRating']
			if rating == None or rating == '' or rating == 'N/A' or rating == '0.0': rating = '0'
			rating = rating.encode('utf-8')

			votes = item['imdbVotes']
			try: votes = str(format(int(votes),',d'))
			except: pass
			if votes == None or votes == '' or votes == 'N/A': votes = '0'
			votes = votes.encode('utf-8')

			mpaa = item['Rated']
			if mpaa == None or mpaa == '' or mpaa == 'N/A': mpaa = '0'
			mpaa = mpaa.encode('utf-8')

			director = item['Director']
			if director == None or director == '' or director == 'N/A': director = '0'
			director = director.replace(', ', ' / ')
			director = re.sub(r'\(.*?\)', '', director)
			director = ' '.join(director.split())
			director = director.encode('utf-8')

			writer = item['Writer']
			if writer == None or writer == '' or writer == 'N/A': writer = '0'
			writer = writer.replace(', ', ' / ')
			writer = re.sub(r'\(.*?\)', '', writer)
			writer = ' '.join(writer.split())
			writer = writer.encode('utf-8')

			cast = item['Actors']
			if cast == None or cast == '' or cast == 'N/A': cast = '0'
			cast = [x.strip() for x in cast.split(',') if not x == '']
			try: cast = [(x.encode('utf-8'), '') for x in cast]
			except: cast = []
			if cast == []: cast = '0'

			plot = item['Plot']
			if plot == None or plot == '' or plot == 'N/A': plot = '0'
			plot = client.replaceHTMLCodes(plot)
			plot = plot.encode('utf-8')

			self.list.append({'title': title, 'originaltitle': title, 'year': year, 'genre': genre, 'duration': '0', 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot, 'code': imdb, 'imdb': imdb, 'tmdb': '0', 'poster': poster, 'channel': i[2], 'num': i[3]})
		except:
			pass


	def uk_datetime(self):
		dt = datetime.datetime.utcnow() + datetime.timedelta(hours = 0)
		d = datetime.datetime(dt.year, 4, 1)
		dston = d - datetime.timedelta(days=d.weekday() + 1)
		d = datetime.datetime(dt.year, 11, 1)
		dstoff = d - datetime.timedelta(days=d.weekday() + 1)
		if dston <=  dt < dstoff:
			return dt + datetime.timedelta(hours = 1)
		else:
			return dt


	def channelDirectory(self, items,name):
		if items == None or len(items) == 0: control.idle() ; sys.exit()

		sysaddon = sys.argv[0]

		syshandle = int(sys.argv[1])

		addonPoster, addonBanner = control.addonPoster(), control.addonBanner()

		addonFanart = control.addonFanart()

		try: isOld = False ; control.item().getArt('type')
		except: isOld = True

		isPlayable = 'true' if not 'plugin' in control.infoLabel('Container.PluginName') else 'false'

		#playbackMenu = control.lang(32063).encode('utf-8') if control.setting('hosts.mode') == '2' else control.lang(32064).encode('utf-8')

		#queueMenu = control.lang(32065).encode('utf-8')

		#refreshMenu = control.lang(32072).encode('utf-8')

		if name==None:
			for i in items:
				try:
					item = control.item(label=i['name'])
					item.setInfo(type='Video', infoLabels = "")
					item.addStreamInfo('video', { 'width':1920 ,'height' : 1080 })
					item.setProperty('Video', 'true')
					control.addItem(handle=int(sys.argv[1]), url="plugin://program.apollo/?action=channels&name="+i['url'], listitem=item, isFolder=True)
				except:	pass
		else:
			for i in items:
				try:
					label = '[B]%s[/B] (%s) %s' % (i['name'].upper(), i['id'],i['title'])
					sysname = urllib.quote_plus('%s (%s)' % (i['name'], i['id']))
					systitle = urllib.quote_plus(i['name'])
					poster = i['poster']
					banner = '0'
					url = i['url']
					sysurl = urllib.quote_plus(url)

					cm = []

					#cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

					#cm.append((refreshMenu, 'RunPlugin(%s?action=refresh)' % sysaddon))

					#cm.append((playbackMenu, 'RunPlugin(%s?action=alterSources&url=%s&meta=%s)' % (sysaddon, sysurl, sysmeta)))

					if isOld == True:
						cm.append((control.lang2(19033).encode('utf-8'), 'Action(Info)'))


					item = control.item(label=label)
					if (str(i['hd'])=="1"):
						item.addStreamInfo('video', { 'width':1280 ,'height' : 720 })
					elif (str(i['hd'])=="2"):
						item.addStreamInfo('video', { 'width':1920 ,'height' : 1080 })
					else:
						item.addStreamInfo('video', { 'width':600 ,'height' : 320 })

					item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'banner': banner})

					if not addonFanart == None:
						item.setProperty('Fanart_Image', addonFanart)

					item.addContextMenuItems(cm)
					item.setProperty('IsPlayable', isPlayable)
					item.setInfo(type='Video', infoLabels = "")

					control.addItem(handle=syshandle, url=url, listitem=item, isFolder=False)
				except:
					pass

		control.content(syshandle, 'movies')
		#control.do_block_check(False)
		control.directory(syshandle, cacheToDisc=True)


