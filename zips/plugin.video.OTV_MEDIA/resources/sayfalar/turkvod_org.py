#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
import urllib, urllib2, re, sys, os
import xbmcplugin, xbmcgui
import urlparse
import codecs
import xbmcaddon
import xbmc
import base64
from resources.lib.common import addon_id
MOVIE_COMMENTS = (True, 'showplayer')
SITE_IDENTIFIER = 'turkvod_org'



from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

import pickle
import xml.dom.minidom as mn
from urlparse import parse_qs
import hashlib
from urllib import unquote_plus

         
#SITE_IDENTIFIER = addonDir


std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}

def debug(obj, text = ''):
    print datetime.fromtimestamp(time()).strftime('[%H:%M:%S]')
    print '%s' % text + ' %s\n' % obj


def mod_request(url, param = None):
    
    url = 'http://' + url.replace('http://', '')
    html = ''
    try:
        debug(url, 'MODUL REQUEST URL')
        req = urllib2.Request(url, param, {'User-agent': UA,
         'Connection': 'Close'})
        html = urllib2.urlopen(req).read()
    except Exception as ex:
        print ex
        print 'REQUEST Exception'

    return html
mac =""
	
def showplayer():
    
    url = 'plugin://plugin.video.OTV_MEDIA/?mode=199' 
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    



from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

import pickle
import xml.dom.minidom as mn
from urlparse import parse_qs
import hashlib
from urllib import unquote_plus

         
Host = "http://trvod.me/80//index.php"

std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}

def construct_request(params):
	return '%s?%s' % (sys.argv[0], urllib.urlencode(params))
		
ADULT_PIN="7686"
std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}

def construct_request(params):
	return '%s?%s' % (sys.argv[0], urllib.urlencode(params))
		
def _downloadUrl(url):
                url = re.findall("(.*?)&title.*?", url)[0]
		return url
               
		     
def StartPort(url, mac = None):
        url = url.replace('TURKvodModul@','').replace('@m3u@TURKvod','?')
        sign = '?'
        url = url.strip(' \t\n\r')
        if url.find('?') > -1:
            sign = '&'
        if mac != None:
            security_key = ""
            security_param = ""
            url = url + sign + 'box_mac=' + mac + security_key + security_param
        if url.find('|') > -1:
                parts = url.split('|')
                url = parts[0]
                pass#print "Here in Turkvod url 6 =", url
                cookie = parts[1]
                req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 TURKvod 8.0',
                 'Connection': 'Close',
                 'Cookie': cookie})
        else:
                req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 TURKvod 8.0',
                 'Connection': 'Close'})
        xmlstream = urllib2.urlopen(req).read()
        pass#print "Here in Turkvod xmlstream  =", xmlstream 

        return xmlstream
		
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvNDJncW4wZWlkcW82MTlmL2hkZC54bWw="
yeni =base64.b64decode(yen)
http = yeni+mac				
def terscevir(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        
   

def TUrKVod():
	oGui = cGui()
        
        start = Host
      
	if Addon.getSetting('mac') != None:
		box_mac = Addon.getSetting('mac')
	else:
		box_mac = None
	try: searchon = params['search']
	except: searchon = None
	try: 
		url=urllib.unquote(params['link'])
		if box_mac != None:
			sign = '?'
			if url.find('?') > -1:	
				sign = '&'
			url = url + sign + 'box_mac=' + box_mac
		else:
			url = url
	except:
		url = start
	xml = StartPort(url, mac)
	print 'HTTP LEN = [%s]' % len(xml)
	if url.find('m3u') > -1:
		m3u(xml)
	else:
			xml = mn.parseString(xml)
	n = 0
	if searchon == None:
		try: search = xml.getElementsByTagName('search_on')[0].firstChild.data
		except: search = None	
	if search != None:
		kbd = xbmc.Keyboard()
		kbd.setDefault('')
		kbd.setHeading('Search')
		kbd.doModal()
		if kbd.isConfirmed():
			sts=kbd.getText();
			sign = '?'
			if url.find('?') > -1:	
				sign = '&'
			sts = sts.replace(' ','%20')
			url2 = url + sign + 'search=' + sts
			print url2
			xml = StartPort(url2, mac)
		else:
			xml = StartPort(url)
		print 'HTTP LEN = [%s]' % len(xml)
		xml = mn.parseString(xml)
		playlist(xml)
	else:
		if url.find('m3u') > -1:
			m3u(xml)
		else:
			playlist(xml)
                oGui.setEndOfDirectory()		
def showGenre2():
	oGui = cGui()                             
        
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')	
        if url.find('&title') > -1:
            url = _downloadUrl(url)
        start = url 
      
	if Addon.getSetting('mac') != None:
		box_mac = Addon.getSetting('mac')
	else:
		box_mac = None
	try: searchon = params['search']
	except: searchon = None
	try: 
		url=urllib.unquote(params['link'])
		if box_mac != None:
			sign = '?'
			if url.find('?') > -1:	
				sign = '&'
			url = url + sign + 'box_mac=' + box_mac
		else:
			url = url
	except:
		url = start
	xml = StartPort(url, mac)
	print 'HTTP LEN = [%s]' % len(xml)
	if url.find('m3u') > -1:
		m3u(xml)
	else:
			xml = mn.parseString(xml)
	n = 0
	if searchon == None:
		try: search = xml.getElementsByTagName('search_on')[0].firstChild.data
		except: search = None	
	if search != None:
		kbd = xbmc.Keyboard()
		kbd.setDefault('')
		kbd.setHeading('Search')
		kbd.doModal()
		if kbd.isConfirmed():
			sts=kbd.getText();
			sign = '?'
			if url.find('?') > -1:	
				sign = '&'
			sts = sts.replace(' ','%20')
			url2 = url + sign + 'search=' + sts
			print url2
			xml = StartPort(url2, mac)
		else:
			xml = StartPort(url)
		print 'HTTP LEN = [%s]' % len(xml)
		xml = mn.parseString(xml)
		playlist(xml)
	else:
		if url.find('m3u') > -1:
			m3u(xml)
		else:
			playlist(xml)
                oGui.setEndOfDirectory()
                		
         
def playlist(xml):
	n = 0                                                                                                                                                                          
	oGui = cGui()
        
        
        xml = xml
        for prev_page_url in xml.getElementsByTagName('prev_page_url'):
		prev_url = xml.getElementsByTagName('prev_page_url')[0].firstChild.data
		prev_title =  "[COLOR FFFFFF00]<-" + prev_page_url.getAttribute('text').encode('utf-8') +'[/COLOR]'
		prev_url = prev_url.replace('TURKvodModul@','')
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', prev_url)
                oGui.addDir(SITE_IDENTIFIER, 'showGenre2',prev_title , 'next.png', oOutputParameterHandler)

	        
        for channel in xml.getElementsByTagName('channel'):
		try: title = channel.getElementsByTagName('title')[0].firstChild.data.encode('utf-8')
		except: title = 'No title or error'
		title = title.replace('<b>', '')
		title = title.replace('</b>', '')
		try:
			description = channel.getElementsByTagName('description')[0].firstChild.data.encode('utf-8')
			img_src_list = re.findall('img .*?src="(.*?)"', description)
			if len(img_src_list) > 0:
				img_src = img_src_list[0]
			else:
				img_src_list = re.findall("img .*?src='(.*?)'", description)
				if len(img_src_list) > 0:
					img_src = img_src_list[0]
				else:	
					img_src = 'DefaultVideo.png'
					       
			
                        description = description.replace('<br>', '\n')
			description = description.replace('<br/>', '\n')
			description = description.replace('</h1>', '</h1>\n')
			description = description.replace('</h2>', '</h2>\n')
			description = description.replace('&nbsp;', ' ')
			description4playlist_html = description
			text = re.compile('<[\\/\\!]*?[^<>]*?>')
			description = text.sub('', description)
			plot = description
		except: 
			description = 'No description'
			plot = description
			img_src = 'DefaultVideo.png'
		n = n+1
		try: 
			link = channel.getElementsByTagName('playlist_url')[0].firstChild.data
			link = link.replace('TURKvodModul@','')
                        oOutputParameterHandler = cOutputParameterHandler()
			oOutputParameterHandler.addParameter('siteUrl', link)
			oGui.addMovie(SITE_IDENTIFIER, 'showGenre2', title, img_src, img_src, '', oOutputParameterHandler)

		       
                except: link = None
		try: 
			stream = channel.getElementsByTagName('stream_url')[0].firstChild.data
	
			oOutputParameterHandler = cOutputParameterHandler()
			oOutputParameterHandler.addParameter('siteUrl', stream)
			oGui.addMovie(SITE_IDENTIFIER, 'turkvodstreams', title, img_src, img_src, '', oOutputParameterHandler)

                except: stream = None	
	for next_page_url in xml.getElementsByTagName('next_page_url'):
		next_url = xml.getElementsByTagName('next_page_url')[0].firstChild.data
		next_title =  "[COLOR FFFFFF00]->" + next_page_url.getAttribute('text').encode('utf-8') +'[/COLOR]'
		next_url = next_url.replace('TURKvodModul@','')
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', next_url)
                oGui.addDir(SITE_IDENTIFIER, 'showGenre2',next_title , 'next.png', oOutputParameterHandler)

	        oGui.setEndOfDirectory()
def m3u(xml):
        oGui = cGui()
        m3u = xml
	regex = re.findall('#EXTINF.*,(.*\\s)\\s*(.*)', m3u)
	if not len(regex) > 0:
		regex = re.findall('((.*.+)(.*))', m3u)
	for text in regex:
		title = text[0].strip()
		url = text[1].strip()
		oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', url)
                oGui.addDir(SITE_IDENTIFIER, 'otvplay__',title , 'next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()	
def turkvodstreams():
                    oGui = cGui()
    
                    oInputParameterHandler = cInputParameterHandler()
                    url = oInputParameterHandler.getValue('siteUrl')
                    name = oInputParameterHandler.getValue('sMovieTitle')
                    streamurl =kshowHosters(url)
                    if not streamurl:
                            
                            playTurkvodplayer(name, url)
                    else:
                            playTurkvodplayer(name, url)
                            if url:
                              url = url
                            playTurkvodplayer(name, url)
                            if streamurl:
                              url=[]  
                              title=[]  
                              title=streamurl[2]
                              for o in streamurl[1]:
                                    url.append(str(o))
                              if len(url) == 1:
                                    url = url[0]
                              elif len(url) > 1:
                                    dialog2 = xbmcgui.Dialog()
                                    ret = dialog2.select('Select Quality',title)
                                    if (ret > -1):
                                       url = url[ret]
                                       for name in streamurl[2]:
                                          playTurkvodplayer(name, url)
                                          return False, False


def kshowHosters(url):
    oGui = cGui()
    
    sMovieTitle = 'sMovieTitle'
    sThumbnail = 'sThumbnail'
   
    sHosterUrl = url
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()



def playTurkvodplayer(name, url):
                        
                        
     
     name ='test'
     addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def addLink(name,url,iconimage):
        oGui = cGui()
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        oGui.setEndOfDirectory()
def playTurkvod2(params):
                    name = params['title']
                    url = urllib.unquote(params['stream'])
                    url = str(url).encode('utf-8', 'ignore')
                    try: img = params['img']
                    except: img = 'DefaultVideo.png'
                    playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
                    playlist.clear();
                    listitem1 = xbmcgui.ListItem(name)
                    playlist.add(url,listitem1);
                    player_type = sPlayerType()
                    xbmcPlayer = xbmc.Player (player_type); 
                    xbmcPlayer.play (playlist)       

def sPlayerType():
        
       
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
        
    




def otvplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle)
    sHosterUrl = sUrl
    



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 