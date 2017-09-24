import urllib, urllib2
import sys, re, os, json, random, string, base64, hashlib, pyaes
import xbmcplugin, xbmcgui, xbmcaddon, xbmc
import net
from urlparse import parse_qsl
import xml.etree.ElementTree as ET
import traceback
import requests

addonID = "plugin.video.streamztv"
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addonID, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addonID, 'icon.png'))
artpath = 'fanart.jpg'
xbmc.translatePath(os.path.join('special://home/addons/' + addonID + '/resources/art/'))

addonPath = xbmcaddon.Addon(id=addonID).getAddonInfo("path")
dialog = xbmcgui.Dialog()
selfAddon = xbmcaddon.Addon(id=addonID)
net = net.Net()

#This list will indicate the channel catagories to check based on their url
checkDirs = {'12':False,   # APK Install Info
			  '0':False,   # All Channels inc U.S.A.
			  '1':False,   # Entertainment
			  '2':False,   # Movies
			  '5':False,   # Sports
			  '3':False,   # Music
			  '4':False,   # News
			  '6':False,   # Documentary
			  '7':False,   # Kids Corner
			  '8':False,   # Food
			  '9':False,   # Religious
			  '11':False}   # Others



DIALOG_URL = "https://gist.githubusercontent.com/juTTeruk/f85cfaf36b178772d8bdb9ed5cd0d4ae/raw/"
ERROR_DIALOG_URL = "https://gist.githubusercontent.com/juTTeruk/9179dd9f658e8d3085ffd2505d7b655a/raw/"
username = '-1'
version = 155

def getVersion():
	# VERSION URL
	req = requests.get("https://gist.githubusercontent.com/juTTeruk/676e6bdab1c2b88d59353ca9f9c92319/raw/")
	if req.status_code != 200:
		return 0
	else:
		return int(req.text)
def isUpdaterInstalled():
	return xbmc.getCondVisibility('System.HasAddon(script.service.pysz)') == 1
	
	
	
def shouldUpdate():
	return getVersion() > version

xml_url = "http://pastebin.com/raw/Xf4CnFp"

def getXml(url):
	req = requests.get(url)
	return req.content

def parseXml(xml):
	xml = xml.replace("&", "XML_NOT_WORKING")
	root = ET.fromstring(xml)
	a = 0
	for child in root:
		name = child.find("title").text.replace("XML_NOT_WORKING", "&")
		image = child.find("thumbnail").text.replace("XML_NOT_WORKING", "&")
		fanart = child.find("fanart").text.replace("XML_NOT_WORKING", "&")
		url = child.find("link").text.replace("XML_NOT_WORKING", "&")
		type = child.find("type").text.replace("XML_NOT_WORKING", "&")
		if type == "youtube":
			videoId = url.split("?v=")[1]
			addLink(name, '%s' % a, 4, fanart, image, videoId)
		elif type == "othervideo":
			addLink(name, '%s' % a, 7, fanart, image, url.replace("&", "PARSE_NOT_WORKING"), isPlayable=True)
			print url, "debug6969"
		elif type == "androidapp":
			addLink(name, '%s' % a, 6, fanart, image, url)
		elif type == "folder":
			addDir(name, '%s' % a, 5, fanart, image, url)
		elif type == "f4m":
			print "Asdasdasds"
			print url, "asdasd"
			import urllib
			addLink(name, '%s' %a, 8, fanart, image, urllib.quote(url))
		a += 1

def update():
	if shouldUpdate():
		# UPDATE URL
		req = requests.get("http://pastebin.com/raw/gyUd0569")
		if req.status_code != 200:
			print "Something went wrong!"
		else:
			with open(os.path.join(addonPath, "default.py"), "wb") as filewriter:
				filewriter.write(req.text)
# main function

def main():
	addDir('[B]The channels in this addon are FREE & now paid for by advertising.[/B]','13',3,artpath+'All.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] All Channels inc U.S.A.','0',1,artpath+'All.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Entertainment','1',1,artpath+'nt.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Movies','2',1,artpath+'ov.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Sports','5',1,artpath+'port.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Music','3',1,artpath+'s.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] News','4',1,artpath+'ews.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Documentary','6',1,artpath+'doc.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Kids Corner','7',1,artpath+'ids.PNG',fanart)
	addDir('[COLOR lime]StreamZ[/COLOR] Food','8',1,artpath+'ood.PNG',fanart)
	xbmc.executebuiltin('Container.SetViewMode(503)')

# Getting popup text
def getDialogText():
	req = requests.get(DIALOG_URL)
	return req.text

def getErrorDialogText():
	req = requests.get(ERROR_DIALOG_URL)
	return req.text

# Getting token

def getToken(url, username):
	s = base64.b64decode("dWt0dm5vdy10b2tlbi0tX3xfLSVzLXVrdHZub3dfdG9rZW5fZ2VuZXJhdGlvbi0lcy1ffF8tMTIzNDU2X3VrdHZub3dfNjU0MzIx")%(url,	username)
	import hashlib
	return hashlib.md5(s).hexdigest()

def getUrl(url, post, headers):
	return requests.post(url, data=post, headers=headers, verify=False).content

def getUKTVUserAgent():
	try:
		username = "-1"#random.choice(usernames)
		post = {'version':'5.7'}
		post = urllib.urlencode(post)
	 
		headers = {'User-Agent': 'USER-AGENT-UKTVNOW-APP-V2', 'app-token':getToken(base64.b64decode("aHR0cDovL3VrdHZub3cubmV0L2FwcDIvdjMvZ2V0X3VzZXJfYWdlbnQ="))}
#		headers=[('User-Agent','USER-AGENT-UKTVNOW-APP-V2'),('app-token',getToken(base64.b64decode("aHR0cDovL3VrdHZub3cubmV0L2FwcDIvdjMvZ2V0X3VzZXJfYWdlbnQ="),username))]
		jsondata=getUrl(base64.b64decode("aHR0cDovL3VrdHZub3cubmV0L2FwcDMvdjMvZ2V0X3VzZXJfYWdlbnQ="),post=post,headers=headers)
		jsondata=json.loads(jsondata)	 
		import pyaes
		try:
			if 'useragent' in jsondata["msg"]:
				return jsondata["msg"]["useragent"]
		except: 
			pass
		key="wwe324jkl874qq99"
		iv="555eop564dfbaaec"
		decryptor = pyaes.new(key, pyaes.MODE_CBC, IV=iv)
		print 'user agent trying'
		ua= decryptor.decrypt(jsondata["msg"]["54b23f9b3596397b2acf70a81b2da31d"].decode("hex")).split('\0')[0]
		print ua
		return ua
	except: 
		print 'err in user agent'
		traceback.print_exc(file=sys.stdout)
		return 'USER-AGENT-UKTVNOW-APP-V2'
	
# Getting channels

def getChannels():
	token=getToken('http://uktvnow.net/uktvnow8/index.php?case=get_all_channels',username)
	print "ASDASDAADS"
	headers={'User-Agent':'USER-AGENT-UKTVNOW-APP-V2','app-token':token}
	#headers={}
	postdata={'username':username}
	print requests.post('http://uktvnow.net/uktvnow8/index.php?case=get_all_channels',data=postdata,headers=headers, verify=False).content
	channels = requests.post('http://uktvnow.net/uktvnow8/index.php?case=get_all_channels',data=postdata,headers=headers, verify=False).content
	print channels
	channels = channels.replace('\/','/')
	print channels
	match=re.compile('"pk_id":"(.+?)","channel_name":"(.+?)","img":"(.+?)","http_stream":"(.+?)","rtmp_stream":"(.+?)","cat_id":"(.+?)"').findall(channels)
	return match

# Showing the channels

def showChannels(url, check):
	if check and not isUpdaterInstalled():
		path = "plugin://plugin.video.youtube/?action=play_video&videoid=tkYMnU6-bYA"
		#xbmc.Player().play(path)
		play(path)
		xbmc.executebuiltin("XBMC.Container.Update(plugin://plugin.video.streamztv,replace)")
		return None
		
	text = getDialogText()
	lines = text.split("\n")
	asd = xbmcgui.Dialog().ok("StreamZTv", *lines)
	
	match = getChannels()
	print match
	for channelid,name,iconimage,stream1,stream2,cat in match:
		thumb='https://app.uktvnow.net/'+iconimage+'|User-Agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G935F Build/MMB29K)'
		if url=='0':addLink(name,'url',2,thumb,fanart,channelid)
		if cat==url:addLink(name,'url',2,thumb,fanart,channelid)
	xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)
	xbmc.executebuiltin('Container.SetViewMode(503)')

# Getting the streams

def getStreams(name, iconimage, channelid):
	playlist_token = getToken('http://uktvnow.net/uktvnow8/index.php?case=get_valid_link_revision', username+channelid)
	postdata = {'useragent':getUKTVUserAgent(),'username':username,'channel_id':channelid,'version':'7.5'}
	headers={'User-Agent':'USER-AGENT-UKTVNOW-APP-V2','app-token':playlist_token}
	channels = requests.post('http://uktvnow.net/uktvnow8/index.php?case=get_valid_link_revision',data=postdata, headers=headers,verify=False).content
	import json
	channels = json.loads(channels)
	#match=re.compile('"channel_name":"(.+?)","img":".+?","http_stream":"(.+?)","rtmp_stream":"(.+?)"').findall(channels)
	#if len(match) == 0: return
	#match = match[-1]
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	played = False

	try:
		decryptURL(channels["msg"]["channel"][0]["rtmp_stream"])
	except:
		""
	
	print channels
	#xbmc.Player().play(decryptURL(channels["msg"]["channel"][0]["http_stream"]), liz)
	play(decryptURL(channels["msg"]["channel"][0]["rtmp_stream"]), liz)
	return ok

# Decrypting the URL

def decryptURL(url):
	# magic="1579547dfghuh,difj389rjf83ff90,45h4jggf5f6g,f5fg65jj46,gr04jhsf47890$93".split(',')
	#decryptor = pyaes.new(magic[1], pyaes.MODE_CBC, IV=magic[4])
	decryptor = pyaes.new("555eop564dfbaaec", pyaes.MODE_CBC, IV="wwe324jkl874qq99")
	url= decryptor.decrypt(url.decode("hex")).split('\0')[0]
	return url

	# Play Media with Q-ADS Player

def play(item, listitem=None, windowed=False, startpos=-1):
	import os, urllib, xbmc, xbmcaddon
	addonID = "plugin.video.streamztv"
	item    = urllib.quote_plus(item)
	script  = os.path.join(xbmcaddon.Addon(id=addonID).getAddonInfo( "path" ), "default.py")
	cmd     = "RunScript(%s, item=%s&addonID=%s)" % (script, item, urllib.quote_plus(addonID))
	xbmc.executebuiltin( cmd )
	
	
# Utilities

# Add link

def addLink(name, url, mode, iconImage, fanart, channelID='', isPlayable=False):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelid="+str(channelID)+"&iconimage="+urllib.quote_plus(iconImage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconImage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': channelID } )
	liz.setProperty('fanart_image', fanart)
	#liz.addContextMenuItems([], replaceItems=True)
	liz.setProperty("IsPlayable", str(isPlayable).lower())
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

# Add directory

def addDir(name, url, mode, iconImage, fanart, channelID=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelid="+str(channelID)+"&iconimage="+urllib.quote_plus(iconImage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconImage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': channelID } )
	liz.setProperty('fanart_image', fanart)
	#liz.addContextMenuItems([], replaceItems=True)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

# Parse params

def parseParams():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
			pairsofparams=cleanedparams.split('&')
			param={}
			for i in range(len(pairsofparams)):
				splitparams={}
				splitparams=pairsofparams[i].split('=')
				if (len(splitparams))==2:
					param[splitparams[0]]=splitparams[1]
	return param

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if selfAddon.getSetting('auto-view')=='true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )
		
		
		
#############################################################################################################################
# Q - PLAYER:

import xbmc
import xbmcgui
import threading
import urllib, urllib2
import datetime
import json
import time
import os
import sys
import shutil
import urllib
from xml.dom import minidom

module_name    = "Q-ADS Player"
cache_file     = os.path.join(xbmc.translatePath("special://temp"), "QADS_Cache")
cache_file_ext = ["",".gif",".png",".jpg"]
debugging      = True

def make_cache():
	for ext in cache_file_ext:
		cache   = cache_file + ext
		basedir = os.path.dirname(cache)
		if not os.path.exists(basedir):
			os.makedirs(basedir)
		if not os.path.exists(cache):
			with open(cache, 'a'):
				os.utime(cache, None)

class AdOverlay(object):
	def __init__(self, windowid, player):
		self.window	   = xbmcgui.Window(windowid)
		self.screenx, self.screeny = self.get_skin_resolution_offset()
		self.player	   = player
		self.addon_id	 = self.player.addon_id
		self.type		 = "default"
		self.repeat_delay = None
		self.ad		   = None
		self.image_meta   = None
		self.duration	 = None
		self.images	   = []

	def show(self):
		for image in self.images:
			self.window.addControl(image)

	def hide(self):
		for image in self.images:
			self.window.removeControl(image)
			self.images.remove(image)

	def get_skin_resolution_offset(self):
		w = int(self.window.getWidth())
		h = int(self.window.getHeight())
		xmlFile = os.path.join(xbmc.translatePath("special://skin/"), "addon.xml")
		xmldoc  = minidom.parse(xmlFile)
		res	 = xmldoc.getElementsByTagName("res")
		w_check = False
		h_check = False
		for r in res:
			try: # Set default values if available
				if r.attributes["default"].value == "true":
					use_w   = int(r.attributes["width"].value)
					use_h   = int(r.attributes["height"].value)
			except:
				pass
			try: # Check if currently set res is available to render in this skin
				if int(r.attributes["width"].value) == w:
					w_check = True
				if int(r.attributes["height"].value) == h:
					h_check = True
			except:
				pass
		if not w_check and not h_check:
			try: # Current skin does not support rendering in this res. Let's try to use defaults
				w = use_w
				h = use_h
			except:
				pass
		return w, h

	def cacheImage(self):
		try:
			url	  = self.image_meta["img_url"]
			self.player._log("Retrieving %s" % url)
			response = urllib2.urlopen(url)
			dest = cache_file
			for suff in cache_file_ext:
				if not suff == "" and suff in os.path.basename(url):
					dest = cache_file+suff
					break
			self.player._log("Downloading image to %s" % dest)
			with open(dest, "wb") as local_file:
				local_file.write(response.read())
			response.close()
			self.image_meta["img_cache_file"] = dest
		except urllib2.HTTPError, e:
			self.player._log("HTTP Error: - %s" % url, message2=e.code, level=4)
		except urllib2.URLError, e:
			self.player._log("URL Error: - %s" % url, message2=e.reason, level=4)

	def displayAd(self):
		# Draw it on the screen
		if self.image_meta:
			self.duration	 = int(self.image_meta["duration"])
			if "repeat_delay" in self.image_meta: self.repeat_delay = int(self.image_meta["repeat_delay"])
			self.player._log("Draw advertisement on screen")
			# Set location attributes 
			I = self.image_meta["img_url"]
			W = int(float(float(self.image_meta["width"]) / float(1920)) * self.screenx)
			H = int(float(float(self.image_meta["height"]) / float(1080)) * self.screeny)
			X = int(float(float(self.image_meta["pos_x"]) / float(1920)) * self.screenx)
			Y = int(float(float(self.image_meta["pos_y"]) / float(1080)) * self.screeny)
			#Y = int(self.image_meta["pos_y"])
			ad = xbmcgui.ControlImage(X, Y, W, H, I, aspectRatio=0)
			self.cacheImage() # Set as local cached file if possible:
			if "img_cache_file" in self.image_meta and os.path.exists(self.image_meta["img_cache_file"]):
				ad.setImage(self.image_meta["img_cache_file"])
			#self.addControl(self.ad)
			if not ad in self.images:
				self.images.append(ad)

	def getImageMeta(self): 
		meta = self.get_remote()
		if "image_details" in meta:
			self.image_meta = meta["image_details"]
			self.player._log("getImageMeta", message2=self.image_meta)

	def get_remote(self):
		self.player._log("Getting remote data")
		url  = "http://k-ads.co.uk/api/"
		data = urllib.urlencode({
							"addon_id" : self.addon_id,
							"get_ad"  : True,
							"display_type"  : self.type,
							"day_today"  : self.today_is(),
							"local_time"  : time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
							"type"  : "list",
							"list"  : "full"})
		req  = urllib2.Request(url=url, data=data)
		req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3")
		response = urllib2.urlopen(req)
		data = response.read()
		response.close()
		try:
			return json.loads(data)
		except Exception, e:
			self.player._log("Exception getting remote information", message2=e, level=4)
			return False

	def today_is(self): 
		day = datetime.datetime.today().weekday()
		week   = ['Monday', 
			  'Tuesday', 
			  'Wednesday', 
			  'Thursday',  
			  'Friday', 
			  'Saturday',
			  'Sunday']
		return week[day]

	def main_loop(self):
		while not xbmc.abortRequested and not self.player._closed:
			self.player._log("Starting Main GUI Loop")
			self.getImageMeta()
			self.displayAd()
			self.show()
			# Display timer:
			timer = 0
			if self.duration and self.images:
				# Set a timer loop to show another ad
				self.player._log("Setting duration timer - %s" % str(self.duration))
				while not xbmc.abortRequested and not self.player._closed and not timer == int(self.duration):
					self.player._log("timer - %s" % str(timer))
					timer += 1
					xbmc.Monitor().waitForAbort(1)
				self.hide()
				#self.ad.setVisible(False)
			# Repeat timer:
			timer = 0
			if self.repeat_delay: # (This function is currently disabled until further notice)
				# Set a timer loop to show another ad
				self.player._log("Setting repeat timer - %s" % str(self.repeat_delay))
				while not xbmc.abortRequested and not self.player._closed and not timer == int(self.repeat_delay):
					timer += 1
					xbmc.Monitor().waitForAbort(1)
			else:
				break
		# Close this window


class QPlayer(xbmc.Player):
	STATE_STOPPED   = "stopped"
	STATE_PLAYING   = "playing"
	STATE_PAUSED	= "paused"
	STATE_BUFFERING = "buffering"
	addon_id		= "Undefined Video Addon"
	debugging	   = False
	_closed		 = False
 
	def __init__(self):
		self.playerthread  = None
		self.windowthread  = None
		self.play_item	 = None
		self.Player_Window = None
		self.hasInfo	   = None
		make_cache()

	def close(self, shutdown=False):
		self._closed   = True
		self.play_item = None
		# if self.windowthread:
		#	 self.windowthread.join()
		self.stop()

	def control(self, cmd):
		if cmd == 'play':
			if xbmc.getCondVisibility('Player.Paused | !Player.Playing'):
				xbmc.executebuiltin('PlayerControl(Play)')
		elif cmd == 'pause':
			if not xbmc.getCondVisibility('Player.Paused'):
				xbmc.executebuiltin('PlayerControl(Play)')

	def _log(self, message, message2="", level=0):
		if self.debugging:
			if not level:
				level = xbmc.LOGDEBUG
			''' Available log levels:
										xbmc.LOGDEBUG = 0
										xbmc.LOGERROR = 4
										xbmc.LOGFATAL = 6
										xbmc.LOGINFO = 1
										xbmc.LOGNONE = 7
										xbmc.LOGNOTICE = 2
										xbmc.LOGSEVERE = 5
										xbmc.LOGWARNING = 3
			'''
			message = 'MODULE[%s] - %s' % (module_name,str(message))
			if message2:
				# Message2 can support other objects:
				if isinstance(message2, basestring):
					message = "%s - %s" % (message,str(message2))
				elif isinstance(message2, dict) or isinstance(message2, list):
					import pprint
					message2 = pprint.pformat(message2, indent=1)
					message = "%s \n%s" % (message,str(message2))
				else:
					message = "%s - %s" % (message,str(message2))
			try:
				xbmc.log("### [%s]: %s" % (self.addon_id,message), level=level )
			except UnicodeEncodeError:
				xbmc.log("### [%s]: %s" % (self.addon_id,message.encode("utf-8", "ignore")), level=level )
			except:
				xbmc.log("### [%s]: %s" % (self.addon_id,'ERROR DEBUG'), level=level )

	def window_old(self):
		self.Player_Window = AdOverlay(player = self)
		self.Player_Window.show()
		self.Player_Window.main_loop()
		self.Player_Window.close()
		self._log('Player: PLAYER:WINDOW closed. If playback continues, then the ad will not be displayed again')
		#self.Player_Window.show_overlay(self) # pass player controls to window

	def window(self):
		display = False
		while not xbmc.abortRequested and not self._closed and not display:
			ActWin = xbmcgui.getCurrentWindowId()
			if ActWin == 12005:
				display = True
				myWidget = AdOverlay(12005, self)	 # 12005: fullscreenvideo
				myWidget.main_loop()
		self._log('Player: PLAYER:WINDOW closed. If playback continues, then the ad will not be displayed again')

	def start_threads(self):
		self._log('Player: Starting Threads')
		if not self.playerthread or not self.playerthread.isAlive():
			self.playerthread = threading.Thread(target=self._monitor, name='PLAYER:MONITOR')
			self.playerthread.start()
		while not self.isPlayingVideo() and not self.isPlayingAudio() and not xbmc.abortRequested and not self._closed: # Wait until video actuall starts befor playing
			xbmc.Monitor().waitForAbort(0.1)
		if self.isPlayingVideo() and not self.windowthread or not self.windowthread.isAlive():
			self.windowthread = threading.Thread(target=self.window, name='PLAYER:WINDOW')
			self.windowthread.start()

	@property
	def playState(self):
		if xbmc.getCondVisibility('Player.Playing'):
			return self.STATE_PLAYING
		elif xbmc.getCondVisibility('Player.Caching'):
			return self.STATE_BUFFERING
		elif xbmc.getCondVisibility('Player.Paused'):
			return self.STATE_PAUSED
		return self.STATE_STOPPED

	def play(self, *args, **kwargs):
		self.started = False
		xbmc.Player.play(self, *args, **kwargs)

	def playVideo(self, item, listitem=None, windowed=False, startpos=-1):
		self.play(item, listitem, windowed=windowed, startpos=startpos)
		self.start_threads()
		while not xbmc.abortRequested and not self._closed:
			xbmc.Monitor().waitForAbort(0.1)

	def _monitor(self):
		while not xbmc.abortRequested and not self._closed:
			if not self.isPlaying():
				self._log('Player: Idling...')
			self._log('Player: waiting...')
			while not self.isPlaying() and not xbmc.abortRequested and not self._closed:
				xbmc.Monitor().waitForAbort(0.1)
				self._log('Player: not yet playing...')
			if self.isPlayingVideo():
				self._log('Monitoring video...')
				self._videoMonitor()
			elif self.isPlaying():
				self._log('Monitoring pre-play...')
				self._preplayMonitor()
		#self.handler.close()
		self.close()
		self._log('Player: Closed')

	def _preplayMonitor(self):
		while self.isPlaying() and not self.isPlayingVideo() and not self.isPlayingAudio() and not xbmc.abortRequested and not self._closed:
			xbmc.Monitor().waitForAbort(0.1)

	def _videoMonitor(self):
		hasFullScreened = False
		while self.isPlayingVideo() and not xbmc.abortRequested and not self._closed:
			self.currentTime = self.getTime()
			xbmc.Monitor().waitForAbort(0.1)
		self.close()


def get_params():
		param=[]
		if len(sys.argv)>=1:
		   params=sys.argv[1]
		   cleanedparams=params.replace('?','')
		   if (params[len(params)-1]=='/'):
				params=params[0:len(params)-2]
		   pairsofparams=cleanedparams.split('&')
		   param={}
		   for i in range(len(pairsofparams)):
				  splitparams={}
				  splitparams=pairsofparams[i].split('=')
				  if (len(splitparams))==2:
						 param[splitparams[0]]=splitparams[1]
		return param



################MAIN##################

def start_player(params):
	MyPlayer = QPlayer()
	try:
		MyPlayer.addon_id  = urllib.unquote_plus(params.get("addonID"))
	except:
		pass
	try:
		if params.get("debugging") == "true":
			debugging = True
		MyPlayer.debugging = debugging
	except:
		pass
	MyPlayer.playVideo(urllib.unquote_plus(params.get("item")))

	
#params = parseParams()
try:
	params = dict(parse_qsl(sys.argv[2][1:]))
except:
	params = get_params()
params = params if params else {}
url = None
name = None
mode = None
iconImage = None
channelID = None

#print str(params) + " asd"
try:
	url = urllib.unquote_plus(params["url"])
except Exception as e:
	print e
	pass

try:
	name = urllib.unquote_plus(params["name"])
except:
	pass

try:
	mode = int(params["mode"])
except Exception as e:
	print e
	pass

try:
	iconImage = urllib.unquote_plus(params["iconimage"])
except:
	pass

try:
	channelID = urllib.unquote_plus(params["channelid"])
except:
	pass

if mode != None:
	print "ads: " + str(mode)

if mode == None or url == None or len(url) < 1:
	if params and params.get("item"):
		start_player(params)
	else:
		print update()
		main()
elif mode == 1:
	showChannels(url, checkDirs[url])
elif mode == 2:
	getStreams(name, iconImage, channelID)
elif mode == 3:
	xml = getXml(xml_url)
	parseXml(xml)
elif mode == 4:
	xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/?action=play_video&videoid=%s)' % channelID)
elif mode == 5:
	xml = getXml(channelID)
	parseXml(xml)
elif mode == 6:
	xbmc.executebuiltin('StartAndroidActivity("%s")' % channelID)
elif mode == 7:
	#print channelID.replace("PARSE_NOT_WORKING", "&"), "aosdadasdasdnjlbnvaiwjdfopajdoi"
	liz = xbmcgui.ListItem(path=channelID.replace("PARSE_NOT_WORKING", "&"))
	liz.setProperty("IsPlayable", 'true')
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
elif mode == 8:
	print "working or not working? "
	import urllib
	#print urllib.unquote(channelID).replace("&amp;", "&"), "ASDASDASD"
	xbmc.executebuiltin('PlayMedia(%s)' % urllib.unquote(channelID).replace("&amp;", "&"))

if mode != 7:
	try:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))
	except:
		pass