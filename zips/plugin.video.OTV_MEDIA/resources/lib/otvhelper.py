#	-*-	coding:	utf-8	-*-
import urllib2, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64

from urllib2 import Request, URLError, urlopen as urlopen2
from socket import gaierror, error

import re, httplib, urllib, urllib2, os, cookielib, socket, sha, shutil, datetime, math, hashlib, random, json, md5, string, xml.etree.cElementTree, StringIO, Queue, threading, sys
from urllib import quote, unquote_plus, unquote, urlencode
from urlparse import parse_qs, parse_qsl
import cryptop
import base64
import adfly
import common
import re
import string
from aadecode import AADecoder
from parser import JJDecoder
from parser import cPacker
import re,xbmcgui,unicodedata
from resources.lib.dl_deprotect import DecryptDlProtect
from resources.lib import client
from urllib import quote, unquote_plus, unquote, urlencode
from resources.lib.gui.hoster import cHosterGui
from resources.lib.packer import cPacker
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.parser import cParser

from resources.lib.player import listPlayer
import urllib2,urllib,re
from resources.lib.player import cPlayer
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

import re, cookielib, time, xbmcgui, xbmc, os, urllib2
from urllib2 import Request, URLError, urlopen as urlopen2
from urlparse import parse_qs
from urllib import quote, urlencode, unquote_plus, unquote
from httplib import HTTPConnection, CannotSendRequest, BadStatusLine, HTTPException
from socket import gaierror, error
from t0mm0.common.net import Net
from jsunpacker import cJsUnpacker
from resources.lib.util import cUtil



from resources.lib.gui.guiElement import cGuiElement



import urllib2,urllib,re
from resources.lib.player import cPlayer
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

import re, cookielib, time, xbmcgui, xbmc, os, urllib2
from urllib2 import Request, URLError, urlopen as urlopen2
from urlparse import parse_qs
from urllib import quote, urlencode, unquote_plus, unquote
from httplib import HTTPConnection, CannotSendRequest, BadStatusLine, HTTPException
from socket import gaierror, error
from t0mm0.common.net import Net
from jsunpacker import cJsUnpacker
import cfscrape

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

import xbmc
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

import requests
import re
net = Net()
import logger     

from  rutrans import detranslify

from resources.lib import jsunprotect
stopEvent=None
g_stopEvent=None
g_downloader=None
g_currentprocessor=None
proxy=None
use_proxy_for_chunks=False
maxbitrate=0
simpleDownloader=False 
auth=None 
streamtype='HLSRETRY'
setResolved=False
swf=None  
callbackpath=""
callbackparam="" 
iconImage="DefaultVideo.png"
setDisplayName = []
SITE_IDENTIFIER = 'filmakinesi_org'
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path')
mac ='AC-DE-48-00-00-80'
res_lib = os.path.join(addonDir, 'resources', 'lib')
f4mProxy = os.path.join(addonDir, 'f4mProxy')        
player_agent = None
def CheckCpacker(str):
    oParser = cParser()
    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>'
    aResult = oParser.parse(str, sPattern)
    if (aResult[0]):
        
        str2 = aResult[1][0]
        if not str2.endswith(';'):
            str2 = str2 + ';'
            
        return cPacker().unpack(str2)

    return str
def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString
REMOTE_DBG = False
# append pydev remote debugger
if REMOTE_DBG:
	# Make pydev debugger works for auto reload.
	# Note pydevd module need to be copied in XBMC\system\python\Lib\pysrc
	try:
		import pysrc.pydevd as pydevd  # with the addon script.module.pydevd, only use `import pydevd`
	# stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
		#pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True, suspend=False)
		pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
	except ImportError:
		sys.stderr.write("Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")
		sys.exit(1)

def player_type():
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

def canlitvzoneBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'https://www.canlitv.zone/' , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = requests.get(Url, headers = headers).text

   

   
    urlk = re.findall('<iframe width="100%" height="100%"  src="(.*?)"', dat, re.S) 
             
    sUrl = 'https://www.canlitv.zone/'+urlk[0] 
     
      

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    source = requests.get(sUrl, headers = headers).text
    
    rUrl = re.findall("file: '(.*?)'",source, re.S)[0]
    sPicture ="https://www.canlitv.zone/logo/tivibu-spor_9147556.png"
    Header = '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rUrl + Header
     
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
    return False


def GetEncodeString(string):
    try:
        import chardet
        string = string.decode(chardet.detect(string)["encoding"]).encode("utf-8")
    except:
        pass
    return string


def getCookieJar():
    cookieJar=None
    try:
        cookieJar = cookielib.LWPCookieJar()
        cookieJar.load(COOKIEFILE,ignore_discard=True)
    except: 
        cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()

    return cookieJar       

            
def mediaHeaders(chann):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann            
         
def flashxx():
        oGui = cGui()
        
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        sTitle = oInputParameterHandler.getValue('sMovieTitle')
        sThumbnail = oInputParameterHandler.getValue('sThumbnail')
        id = re.search('(flash-x.|flashx.)(tv|pw)/(embed-|dl\?|fxplay-|embed.php\?c=|)(\w+)', Url)
        
   		                 
                                      
        web_url = "http://www.flashx.tv/playvid-%s.html" % id.group(4)                                                 
        url = "http://www.flashx.tv/playvid-%s.html" % id.group(4)                                         
        
                                
        ids= id.group(4) 
        resp = net.http_GET(url)
	data = resp.content	                
                      
    
        oParser = cParser()    
        sHtmlContent = GetRedirectHtml(web_url,ids)
        
        if not sHtmlContent:
            return False,False
            
        
        sPattern = "(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
        aResult = re.findall(sPattern,sHtmlContent)
        
        if not aResult:
            

            
            sGoodUrl = web_url

            
            sPattern = 'reload the page! <a href="([^"]+)">!! <b>'
            data=data.replace('./reloadit',"http://www.flashx.tv/reloadit")
            aResult = re.findall(sPattern,data)
            if not aResult:
                return False,False
            sRefresh = aResult[0]
            
         
            sPattern = 'type="text\/javascript" src="([^"]+checkembed[^"]+)"><\/script>'
            aResult = re.findall(sPattern,data)
            if not aResult:
                return False,False
            sHtmlContent = GetRedirectHtml(sRefresh,ids)
            

            sHtmlContent = GetRedirectHtml(sGoodUrl,ids)
          
            sPattern = "(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
            aResult = re.findall(sPattern,sHtmlContent)
        
        if (aResult):
            sUnpacked = cPacker().unpack(aResult[0])
            links = re.findall('file:"(http.*?)",label:"(Low|Middle|High)"', sUnpacked, re.S|re.I)
            if links:
		res = ['high', 'middle', 'low']
		for best in res:
			for url, qua in links:
			    if best == qua.lower():
			     sTitle = alfabekodla(sTitle)         
			     oOutputParameterHandler = cOutputParameterHandler()
			     oOutputParameterHandler.addParameter('siteUrl',url)
			     oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
			     oGui.addDir(SITE_IDENTIFIER , 'showBoxxx','[COLOR teal]Play  [COLOR red]'+ qua +'[/COLOR][/COLOR]','tv.png', oOutputParameterHandler)
                              
  
        oGui.setEndOfDirectory()                         
		
	                     
			                             
                                                   
def videoraj():
        oInputParameterHandler = cInputParameterHandler()
        web_url = oInputParameterHandler.getValue('siteUrl')
    
        sTitle= oInputParameterHandler.getValue('sMovieTitle')
        sThumbnail = oInputParameterHandler.getValue('sThumbnail')
        
        dat = net.http_GET(web_url).content
        urls = re.findall('<p><!--baslik:Tek Raj--><iframe width="640" height="360" allowfullscreen src="(.*?)"', dat, re.S)[0] 
        referer=[('Referer',web_url)]
        urlk=gegetUrl( urls,headers=referer) 
        Urla = re.findall('target="_blank" href="(.*?)">',urlk, re.S)[0] 
        
        Urla=Urla.replace('//www.videoraj.to/v/',"")
#        
        player_url = 'http://www.videoraj.to/embed.php?id=%s&playerPage=1&autoplay=1' % (Urla)
        data = net.http_GET(player_url).content
                     
        url = re.findall("<source src=\"(.*?)\" type='video/mp4'>", data, re.S)[0]                                      
        if url:
            

           
            TIK='|User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

            sHosterUrl =url +TIK                                                    
	  
            sTitle = alfabekodla(sTitle) 
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setTitle(sTitle)
            oGuiElement.setMediaUrl(sHosterUrl)
        

            oPlayer = cPlayer()
            oPlayer.clearPlayList()
            oPlayer.addItemToPlaylist(oGuiElement)
            oPlayer.startPlayer()  
                   
def mailru():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    tarzlistesi= []                 
    
    data = requests.get(Url).content
  
    stream = re.findall('"metaUrl": "(.*?)"', data, re.S)
    Url = str(stream[0])
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('//cdn',"https://cdn") 
    tarzlistesi = re.findall('"url":"(https.*?)".*?"key":"(.*?)"', data, re.S)
    
    cookie = getUrl(Url, output='cookie').result
   
    h = "|Cookie=%s" % urllib.quote(cookie)
    for sUrl,sTitle in tarzlistesi:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl+h))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
def closeload():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    resp = net.http_GET(url)
    sHtmlContent = resp.content  
    sPattern = "(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
    aResult = re.findall(sPattern,sHtmlContent)
        
    if (aResult):
       sUnpacked = cPacker().unpack(aResult[0])
       links = re.findall('download_link="(.*?)"', sUnpacked, re.S|re.I)[0]
       sHosterUrl = links
       sTitle = alfabekodla(sTitle) 
       oGuiElement = cGuiElement()
       oGuiElement.setSiteName(SITE_IDENTIFIER)
       oGuiElement.setTitle(sTitle)
       oGuiElement.setMediaUrl(sHosterUrl)
        

       oPlayer = cPlayer()
       oPlayer.clearPlayList()
       oPlayer.addItemToPlaylist(oGuiElement)
       oPlayer.startPlayer()  
    	
 
def mokru():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
                      
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
                         
    stream = re.findall('data-embedclass="yt_layer" data-objid=".*?" href="(.*?)"', data, re.S)
    url = stream[0]
    tarzlistesi= []
    tarzlistesi.append(("mobile", "%s" %url.replace('st.mq=2','st.mq=4').replace('amp;',"") ))
    tarzlistesi.append(("lowes", "%s" % url.replace('st.mq=2','st.mq=1').replace('amp;',"") ))
    tarzlistesi.append(("low", "%s" % url.replace('st.mq=2','st.mq=2').replace('amp;',"") ))
    tarzlistesi.append(("sd", "%s" % url.replace('st.mq=2','st.mq=3').replace('amp;',"") ))
    tarzlistesi.append(("hd", "%s" % url.replace('st.mq=2','st.mq=5').replace('amp;',"") ))
    tarzlistesi.append(("full", ""+url.replace('st.mq=2','st.mq=6').replace('amp;',"") ))        
    for sTitle,sUrl in tarzlistesi:
           
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()
       			

def ozel():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    tarzlistesi= []                 
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
       
    stream = re.findall('<!--baslik:.*?--><.*?src=[\'|"](.*?)[\'|"]', data, re.S)
    Url = str(stream[0])
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    

        #cookie = getUrl(url, output='cookie').result
    tarzlistesi = re.findall('"file":"(.*?)".*?"label":"(.*?)"', data, re.S)
    for sUrl,sTitle in tarzlistesi:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()   
def showBoxxx():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    track = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    
        
    sHosterUrl = track

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
def showotvplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='HLS'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
         
def showhlsetryplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    TIK='User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    url =url
    StreamType='HLSRETRY'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
    
def showotsplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='TSDOWNLOADER'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
def laklak(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku      
def showHDSplayer():
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    iconimage = alfabekodla(iconimage)   
    name = alfabekodla(name)
    url =url
    StreamType='HDS'
    url = 'plugin://plugin.video.OTV_MEDIA/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')    
    



            
        
       
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
def play__():
    oGui = cGui()

    TIK='|User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    if '.ts' in sUrl:
            sUrl = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(sUrl)+'&amp;streamtype=TSDOWNLOADER&name='+urllib.quote(sTitle)+ TIK
  
    playlist=xbmc.PlayList(xbmc.PLAYER_CORE_DVDPLAYER); 
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+sTitle)
    playlist.add(sUrl,listitem1);
    player_type = sPlayerType()
    xbmcPlayer = xbmc.Player (player_type); 
    xbmcPlayer.play (playlist)
    return
        
    oGui.setEndOfDirectory()
         
def make_closing(base, **attrs):
    """
    Needed for BZ2File with Python (2.6), which otherwise raise "AttributeError: BZ2File instance has no attribute '__exit__'".
    """
    if not hasattr(base, '__enter__'):
        attrs['__enter__'] = lambda self: self
    if not hasattr(base, '__exit__'):
        attrs['__exit__'] = lambda self, type, value, traceback: self.close()
    return type('Closing' + base.__name__, (base, object), attrs)
    
useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0'
SPORTS ='https://dl.dropboxusercontent.com/s/k2jz15prgor015u/dcc12.html'
headers = [
    ['User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0'],
    ['Accept-Encoding', 'gzip, deflate'],
    ['Connection', 'keep-alive']
]
def urllibrequest(url, postfields = {}, headers = {}, cookie = 'cookie.lpw', loc = None):
    """
        url = 'http://www.diziizleyin.net/index.php?x=isyan'
        postfields = {'pid' : 'p2x29464a434'}
        txheaders = {'X-Requested-With':'XMLHttpRequest'}
        myrequest(url, postfields, headers, loc)
    """
    url = url if url.startswith('http://') else 'http://' + url
    req = urllib2.Request(url)
    cj = cookielib.LWPCookieJar()
    if os.path.isfile('cookie.lpw'):
        cj.load('cookie.lpw')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    if postfields:
        postfields = urllib.urlencode(postfields)
        req = urllib2.Request(url, postfields)
    req.add_header('User-Agent', useragent)
    if headers:
        for k, v in headers.items():
            req.add_header(k, v)

    response = urllib2.urlopen(req)
    if loc:
        data = response.geturl()
        response.close()
    else:
        data = response.read()
        response.close()
        cj.save('cookie.lpw')
    return data

def Play_f4mProxy(url, name, iconimage):
    
    streamtype='TSDOWNLOADER'
    maxbitrate = Addon.getSetting('BitRateMax')
    if Addon.getSetting('use_simple') == "true":
        simpledownloader = True
    else:
        simpledownloader = False
    
    sys.path.insert(0, f4mProxy)
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    if streamtype == "TSDOWNLOADER":
        
        maxbitrate=0
        player.playF4mLink(url, name, None, True, maxbitrate, simpledownloader, None, streamtype, False, None, iconimage)    
    

import sys,traceback,urllib2,re, urllib
def mcreateCookie(url,cj=None,agent='Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0'):
    urlData=''
    print  urlData
    try:
        import urlparse,cookielib,urllib2

        class NoRedirection(urllib2.HTTPErrorProcessor):    
            def http_response(self, request, response):
                return response

        def parseJSString(s):
            try:
                offset=1 if s[0]=='+' else 0
                val = int(eval(s.replace('!+[]','1').replace('!![]','1').replace('[]','0').replace('(','str(')[offset:]))
                return val
            except:
                pass

        #agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
        if cj==None:
            cj = cookielib.CookieJar()

        opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent', agent)]
        response = opener.open(url)
        result=urlData = response.read()
        response.close()
#        print result
#        print response.headers
        jschl = re.compile('name="jschl_vc" value="(.+?)"/>').findall(result)[0]

        init = re.compile('setTimeout\(function\(\){\s*.*?.*:(.*?)};').findall(result)[0]
        builder = re.compile(r"challenge-form\'\);\s*(.*)a.v").findall(result)[0]
        decryptVal = parseJSString(init)
        lines = builder.split(';')

        for line in lines:
            if len(line)>0 and '=' in line:
                sections=line.split('=')

                line_val = parseJSString(sections[1])
                decryptVal = int(eval(str(decryptVal)+sections[0][-1]+str(line_val)))

#        print urlparse.urlparse(url).netloc
        answer = decryptVal + len(urlparse.urlparse(url).netloc)

        u='/'.join(url.split('/')[:-1])
        query = '%s/cdn-cgi/l/chk_jschl?jschl_vc=%s&jschl_answer=%s' % (u, jschl, answer)

        if 'type="hidden" name="pass"' in result:
            passval=re.compile('name="pass" value="(.*?)"').findall(result)[0]
            query = '%s/cdn-cgi/l/chk_jschl?pass=%s&jschl_vc=%s&jschl_answer=%s' % (u,urllib.quote_plus(passval), jschl, answer)
            if query:
                reactor.callLater(5,  response, timeout=5)

            
 #       print query
#        import urllib2
#        opener = urllib2.build_opener(NoRedirection,urllib2.HTTPCookieProcessor(cj))
#        opener.addheaders = [('User-Agent', agent)]
        from Plugins.Extensions.OrhanTV1.adds.turktv.bicaps import turksinemabas
        add_adi="FILMAKINESI NET"
        bir=response
        print bir
        iki="http://filmakinesi.org/arama?q=%s"
        uc='<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><h4><a href="(.*?)">(.*?)</a>'                 

        
        response.open(turksinemabas,add_adi,bir,iki,uc)
 #       print response.headers
        #cookie = str(response.headers.get('Set-Cookie'))
        #response = opener.open(url)
        #print cj
#        print response.read()
        

        return urlData
        print  urlData
    except:
        traceback.print_exc(file=sys.stdout)
        return urlData
        print  urlData


import sys,traceback,urllib2,re, urllib
def createCookie(url,cj=None,agent='Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0'):
    urlData=''
    try:
        import urlparse,cookielib,urllib2

        class NoRedirection(urllib2.HTTPErrorProcessor):    
            def http_response(self, request, response):
                return response

        def parseJSString(s):
            try:
                offset=1 if s[0]=='+' else 0
                val = int(eval(s.replace('!+[]','1').replace('!![]','1').replace('[]','0').replace('(','str(')[offset:]))
                return val
            except:
                pass

        #agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
        if cj==None:
            cj = cookielib.CookieJar()

        opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-Agent', agent)]
        response = opener.open(url)
        result=urlData = response.read()
        response.close()
#        print result
#        print response.headers
        jschl = re.compile('name="jschl_vc" value="(.+?)"/>').findall(result)[0]

        init = re.compile('setTimeout\(function\(\){\s*.*?.*:(.*?)};').findall(result)[0]
        builder = re.compile(r"challenge-form\'\);\s*(.*)a.v").findall(result)[0]
        decryptVal = parseJSString(init)
        lines = builder.split(';')

        for line in lines:
            if len(line)>0 and '=' in line:
                sections=line.split('=')

                line_val = parseJSString(sections[1])
                decryptVal = int(eval(str(decryptVal)+sections[0][-1]+str(line_val)))

#        print urlparse.urlparse(url).netloc
        answer = decryptVal + len(urlparse.urlparse(url).netloc)

        u='/'.join(url.split('/')[:-1])
        query = '%s/cdn-cgi/l/chk_jschl?jschl_vc=%s&jschl_answer=%s' % (u, jschl, answer)

        if 'type="hidden" name="pass"' in result:
            passval=re.compile('name="pass" value="(.*?)"').findall(result)[0]
            query = '%s/cdn-cgi/l/chk_jschl?jschl_vc=%s&pass=%s&jschl_answer=%s' % (u,urllib.quote_plus(passval), jschl, answer)
            print query
            reactor.callLater(5,  response, timeout=5)
            print reactor
 #       print query
#        import urllib2
#        opener = urllib2.build_opener(NoRedirection,urllib2.HTTPCookieProcessor(cj))
#        opener.addheaders = [('User-Agent', agent)]
        #print opener.headers
        response = opener.open(query)
        print response
        #cookie = str(response.headers.get('Set-Cookie'))
        #response = opener.open(url)
        #print cj
#        print response.read()
        response.close()

        return urlData
    except:
        traceback.print_exc(file=sys.stdout)
        return urlData

import re
      
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvNDdoeTFteTA3Zjh0b3dkL3BsdWdpbi5waHA="
HOSsT =base64.b64decode(yen)
urlHOST = 'https://dl.dropboxusercontent.com/s/vjykn4jlza4yo32/saved_resource.html'
def TURKIYE(url):
    resp = net.http_GET(url)
    sHtmlContent = resp.content  
    sPattern = 'action="(.+?)"'
    aResult = re.findall(sPattern,sHtmlContent)
    return  aResult[0]  

TURKIYE=TURKIYE(HOSsT)                    
def TURKEY(url):
    resp = net.http_GET(url)
    sHtmlContent = resp.content  
    sPattern = 'Paction="(.+?)"'
    aResult = re.findall(sPattern,sHtmlContent)
    return  aResult[0]  

TURKEY=TURKEY(HOSsT)                    

HOSTO='PT1nQ05zMVBsOVRYcmd5UFU5VEtyQUNLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ3lZZTlsWHZseUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJb01tWGY1MWJwc0NJbzh6UC9reVcvVTJQZHRDS284elAva0NJckFDS3Y1MVhlOVdLcHNDSW9neWJlOWxYdmxDSXRBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOHpQL2tDSXJBQ0t2NTFYZTlXS3BzQ0lvOHpQL2t5Vy9VMlBkdENLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ0NLLzh6UHBBeUtnZ3liZTlsWHZsU0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvOHpQL2t5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW84elAva3lLZ2d5UC84VEtiOVRaLzAxS29neVAvOFRLZ3NDSW84RFYva1NLckFDS284bVhmNTFicEF5S284bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dneVAvOFRLckFDSy84elBwc0NJbzh6UC9reVcvVTJQZHRDSy9RMVBwc0NJb2d5YmU5bFh2bENJcmd5YmU5bFh2bFNLckFDS284bVhmNTFicEFTTGdneVBVOVRLcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDS284elAva0NJckFDS3Y1MVhlOVdLcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0tqNTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0svOHpQcHNDSW9neWJlOWxYdmxDSXRBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneWJlOWxYdmxTS3JBQ0tqNTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ0NLLzh6UHBBeUtnZ3lQVTlUS3BzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3liZTlsWHZsQ0lyZ3liZTlsWHZsU0tyQUNLdjUxWGU5V0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ0NLdjUxWGU5V0tnMENJbzhEVi9rU0tyQUNLLzh6UHBzMVBsOVRYcmd5UFU5VEtyQUNLLzh6UHBzQ0lvOG1YZjUxYnBzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOHpQL2tDSXJBQ0t2NTFYZTlXS3BzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3lQLzhUS2dzQ0lvOERWL2tTS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLdjUxWGU5V0tnc0NLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ3lQLzhUS3JBQ0tvOHpQL2tDSXJBQ0svUTFQcGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svOHpQcHMxUGw5VFhyZ3lQVTlUS3JBQ0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQLzhUS3JBQ0svOHpQcDR5Vy9VMlBkdENLL1ExUHBzQ0lvOHpQL2t5S2dneWJlOWxYdmx5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84bVhmNTFicGt5S2dneVAvOFRLYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDSy84elBwOHlXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0t2NTFYZTlXS3JBQ0svOHpQcDh5Vy84elBkdENLbzh6UC9rQ0lyQUNLdjUxWGU5V0twc0NJbzh6UC9reUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ0NLLzh6UHBBeUtnZ3liZTlsWHZsU0tyQUNLL1ExUHBzQ0lvOHpQL2t5Vy9VMlBkdENLL1ExUHBzQ0lvZ3liZTlsWHZsQ0lyZ3liZTlsWHZsU0tyQUNLbzh6UC9rQ0lyQUNLL1ExUHBreUtnZ3lQLzhUS2p0MVBsOVRYcmdDSy84elBwQXlLZ2d5YmU5bFh2bFNLckFDS2o1MVhlOVdLckFDSy84elBwUTJXL1UyUGR0Q0tvOG1YZjUxYnBBeUtvOG1YZjUxYnBreUtnZ3lQVTlUS3JBQ0svOHpQcGszVy84elBkdENLbzhtWGY1MWJwQXlLbzhtWGY1MWJwa3lLZ2d5WWU5bFh2bHlLZ2d5UC84VEtsdDFQbDlUWHJneVBVOVRLckFDSy84elBwc0NJbzhEVi9reUtnZ3lQLzhUS3R0MVBsOVRYcmd5UFU5VEtyQUNLbzhtWGY1MWJwQXlLbzhtWGY1MWJwa3lLZ2dDSy84elBwQXlLZ2d5UFU5VEtwc0NJbzh6UC9rQ2ViOVRaLzAxS29neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0t2NTFYZTlXS3JBQ0svOHpQcHMxUGw5VFhyZ0NLLzh6UHBBeUtnZ3lQVTlUS3BzQ0lvZ3lQLzhUS2dzQ0lvOG1YZjUxYnBreUtnZ3lQLzhUS2I5VFovMDFLbzhEVi9reUtnZ3lQLzhUS3JBQ0svOHpQcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW84elAva3lLZ2d5YmU5bFh2bHlLZ2d5UC84VEtiOVRaLzAxS284RFYva3lLZ2d5UC84VEtyQUNLdjUxWGU5V0tyQUNLLzh6UHBzMVBsOVRYcmdDS3Y1MVhlOVdLZ3NDS3Y1MVhlOVdLcHNDSW84RFYva3lLZ2d5UC84VEtiOVRaLzAxS29neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svUTFQcHNDSW84elAva2lMYjlUWi8wMUtvOERWL2t5S2dnQ0svOHpQcEF5S2dneVBVOVRLcHNDSW9NbVhmNTFicHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neWJlOWxYdmxDSXJneWJlOWxYdmxTS3JBQ0svOHpQcHNDSW84elAva3lXL1UyUGR0Q0svUTFQcHNDSW9neVAvOFRLZ3NDSW84RFYva1NLckFDS284elAva0NJckFDSy9RMVBwa3lLZ2d5UC84VEtiOVRaLzAxS284RFYva3lLZ2dDSy84elBwQXlLZ2d5UFU5VEtwc0NJbzh6UC9reUtnZ3lQLzhUSw'


class getUrl(object):
    def __init__(self, url, close=True, proxy=None, post=None, headers=None, mobile=False, referer=None, cookie=None, output='', timeout='10'):
        handlers = []
        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl; ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers += [urllib2.HTTPSHandler(context=ssl_context)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass
        try: headers.update(headers)
        except: headers = {}
        if 'User-Agent' in headers:
            pass
        elif not mobile == True:
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0'
        else:
            headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'referer' in headers:
            pass
        elif referer == None:
            headers['referer'] = url
        else:
            headers['referer'] = referer
        if not 'Accept-Language' in headers:
            headers['Accept-Language'] = 'en-US'
        if 'cookie' in headers:
            pass
        elif not cookie == None:
            headers['cookie'] = cookie
        request = urllib2.Request(url, data=post, headers=headers)
        response = urllib2.urlopen(request, timeout=int(timeout))
        if output == 'cookie':
            result = []
            for c in cookies: result.append('%s=%s' % (c.name, c.value))
            result = "; ".join(result)
        elif output == 'geturl':
            result = response.geturl()
        else:
            result = response.read()
        if close == True:
            response.close()
        self.result = result
 
def gegetUrl(url, cookieJar=None,post=None, timeout=20, headers=None):
    url=url.replace('www.ulantv.com','www.izletv.us')
    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;
           
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvMDZvb3pwd2poc3VzMXAxL3BsYXlsaXN0X29yaGFudHYubTN1"
IPTVHOST =base64.b64decode(yen)
url_all_products = "http://www.livemobiletv247.com/android_app/webservice/get_channels.php"
def ABCkodla(sMovieTitle):
    sMovieTitle = unicode(sMovieTitle, 'utf-8')#converti en unicode pour aider aux convertions
    sMovieTitle = unicodedata.normalize('NFD', sMovieTitle).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
    sMovieTitle = sMovieTitle.encode("utf-8").lower() #on repasse en utf-8
 
    return sMovieTitle
                    
def alfabekodla(text):
        text = (str(text)).replace('\\x','')
        text = (str(text)).replace('&auml;','ä')
	text = (str(text)).replace('\u00e4','ä')
	text = (str(text)).replace('\ufeff','ä')
        text = (str(text)).replace('&#228;','ä')
	text = (str(text)).replace('&Auml;','Ä')
	text = (str(text)).replace('\u00c4','Ä')
	text = (str(text)).replace('&#196;','Ä')
	text = (str(text)).replace('&ouml;','ö')
	text = (str(text)).replace('\u00f6','ö')
	text = (str(text)).replace('&#246;','ö')
	text = (str(text)).replace('&ouml;','Ö')
	text = (str(text)).replace('&Ouml;','Ö')
	text = (str(text)).replace('\u00d6','Ö')
	text = (str(text)).replace('&#214;','Ö')
	text = (str(text)).replace('&uuml;','ü')
	text = (str(text)).replace('\u00fc','ü')
	text = (str(text)).replace('&#252;','ü')
	text = (str(text)).replace('&Uuml;','Ü')
	text = (str(text)).replace('\u00dc','Ü')
	text = (str(text)).replace('&#220;','Ü')
        text = (str(text)).replace('tv_','player')
	text = (str(text)).replace('&szlig;','ß')
	text = (str(text)).replace('\u00df','ß')
	text = (str(text)).replace('&#223;','ß')
	text = (str(text)).replace('&amp;','&')
	text = (str(text)).replace('&quot;','\"')
	text = (str(text)).replace('&gt;','>')
	text = (str(text)).replace('&apos;',"'")
	text = (str(text)).replace('&acute;','\'')
	text = (str(text)).replace('&ndash;','-')
	text = (str(text)).replace('&bdquo;','"')
	text = (str(text)).replace('&rdquo;','"')
	text = (str(text)).replace('&ldquo;','"')
	text = (str(text)).replace('&lsquo;','\'')
	text = (str(text)).replace('&rsquo;','\'')
	text = (str(text)).replace('&#034;','\'')
	text = (str(text)).replace('&#038;','&')
	text = (str(text)).replace('&#039;','\'')
	text = (str(text)).replace('&#39;','\'')
	text = (str(text)).replace('&#160;',' ')
	text = (str(text)).replace('\u00a0',' ')
	text = (str(text)).replace('\u00b4','\'')
	text = (str(text)).replace('&#174;','')
	text = (str(text)).replace('&#225;','a')
	text = (str(text)).replace('&#233;','e')
	text = (str(text)).replace('&#243;','o')
	text = (str(text)).replace('&#8211;',"-")
	text = (str(text)).replace('\u2013',"-")
	text = (str(text)).replace('&#8216;',"'")
	text = (str(text)).replace('&#8217;',"'")
	text = (str(text)).replace('&#8220;',"'")
	text = (str(text)).replace('&#8221;','"')
	text = (str(text)).replace('&#8222;',',')
	text = (str(text)).replace('\u201e','\"')
	text = (str(text)).replace('\u201c','\"')
	text = (str(text)).replace('\u201d','\'')
	text = (str(text)).replace('\u2019s','\'')
	text = (str(text)).replace('\u00e0','à')
	text = (str(text)).replace('\u00e7','ç')
	text = (str(text)).replace('\u00e9','é')
	text = (str(text)).replace('&#xC4;','Ä')
	text = (str(text)).replace('&#xD6;','Ö')
	text = (str(text)).replace('&#xDC;','Ü')
	text = (str(text)).replace('&#xE4;','ä')
	text = (str(text)).replace('&#xF6;','ö')
	text = (str(text)).replace('&#xFC;','ü')
	text = (str(text)).replace('&#xDF;','ß')
	text = (str(text)).replace('&#xE9;','é')
	text = (str(text)).replace('&#xB7;','·')
	text = (str(text)).replace("&#x27;","'")
	text = (str(text)).replace("&#x26;","&")
	text = (str(text)).replace("&#xFB;","û")
	text = (str(text)).replace("&#xF8;","ø")   
	text = (str(text)).replace("&#x21;","!")                          
	text = (str(text)).replace("&#x3f;","?")
        text = (str(text)).replace("&#304;",  "I")       
        text = (str(text)).replace("&#304;",  "I")
        text = (str(text)).replace("&#39;", "'")
        text = (str(text)).replace('&#39;',"ş")
	text = (str(text)).replace('&#8230;','...')
	text = (str(text)).replace('\u2026','...')  
	text = (str(text)).replace('c59f','ş')
	text = (str(text)).replace('c4b1','ı')
        text = (str(text)).replace('c3b6','ö')
        text = (str(text)).replace('c3bc','ü')                    
        text = (str(text)).replace('c387','Ç')
        text = (str(text)).replace('c3a7','ç')
        text = (str(text)).replace('c396','Ö')
        text = (str(text)).replace('c4b0','İ')
        text = (str(text)).replace('c39c','ü')
        text = (str(text)).replace('c49f','ğ')
        text = (str(text)).replace('&#8234;','')
	text = (str(text)).replace("&#39;", "'")
        text = (str(text)).replace('&#39;',"ş")
	text = (str(text)).replace('&#8230;','...')
	text = (str(text)).replace('\u2026','...')
	text = (str(text)).replace('&hellip;','...')
	text = (str(text)).replace('&#8234;','')
        text = (str(text)).replace("&#231;", "ç")
        text = (str(text)).replace('&#351;',"ş")
	text = (str(text)).replace('&#350;','ş')
	text = (str(text)).replace('&#246;','ö')
	text = (str(text)).replace('&#214;','Ö')
	text = (str(text)).replace('&#199;','Ç')
        text = (str(text)).replace('\u0130','i')
        text = (str(text)).replace('\u00c7','Ç')
        text = (str(text)).replace('\u015e','�?')
        text = (str(text)).replace('\u015f','ş')
        text = (str(text)).replace('\u2014','-')
        text = (str(text)).replace('\u011e','�?')
        text = (str(text)).replace('\u0131','ı')
        text = (str(text)).replace('c59e','Ş')
        text = (str(text)).replace('c3a4','ä')
        return text  
                                          
def georgiadecode( data):                             
                        data = (str(data)).replace('%e1%83%90','a')
                        data = (str(data)).replace('\u10d1','b')
                        data = (str(data)).replace("\u10e9" , "ch")
                        data = (str(data)).replace('\u10d3',"d")
                        data = (str(data)).replace('%e1%83%94',"e")
                        data = (str(data)).replace(" %e1%83%96" , "sh")
                        data = (str(data)).replace('\u10d2',"g")
                        data = (str(data)).replace("\u10e7" , "q'")
                        data = (str(data)).replace('%e1%83%98','i')
                        data = (str(data)).replace("\u10e6" , "gh")
                        data = (str(data)).replace("\u10d9" , "k'")
                        data = (str(data)).replace('%e1%83%94','l')
                        data = (str(data)).replace('%e1%83%9b','m')
                        data = (str(data)).replace('%e1%83%9c','n')
                        data = (str(data)).replace('\u10dd','o')
                        data = (str(data)).replace('%e1%83%94','p')
                        data = (str(data)).replace("%e1%83%a5" , "k")
                        data = (str(data)).replace('%e1%83%ac','r')
                        data = (str(data)).replace('%e1%83%98','s')
                        data = (str(data)).replace('%e1%83%a2',"t'")
                        data = (str(data)).replace('%e1%83%a3','u')
                        data = (str(data)).replace('%e1%83%95','v')
                        data = (str(data)).replace('\u10e2',"t'")
                        data = (str(data)).replace("\u10df" , "zh")
                        data = (str(data)).replace("\u10ea" , "ts")
                        data = (str(data)).replace("\u10eb" , "dz")
                        data = (str(data)).replace("\u10ec" , "ts'")
                        data = (str(data)).replace("\u10ed" , "ch'")
                        data = (str(data)).replace("\u10ee" , "kh")
                        data = (str(data)).replace("\u10ef" , "j" )
                        data = (str(data)).replace("%e1%83%99" , "k'")
                        data = (str(data)).replace('%e1%83%9c','z')
                        return data



def fs(s):
	s=str(repr(s))[1:-1]
	s=s.replace('\\xb8','ё')
	s=s.replace('\\xe0','a')
	s=s.replace('\\xe1','б')
	s=s.replace('\\xe2','в')
	s=s.replace('\\xe3','г')
	s=s.replace('\\xe4','д')
	s=s.replace('\\xe5','е')
	s=s.replace('\\xe6','ж')
	s=s.replace('\\xe7','з')
	s=s.replace('\\xe8','и')
	s=s.replace('\\xe9','й')
	s=s.replace('\\xea','к')
	s=s.replace('\\xeb','л')
	s=s.replace('\\xec','м')
	s=s.replace('\\xed','н')
	s=s.replace('\\xee','о')
	s=s.replace('\\xef','п')
	s=s.replace('\\xf0','р')
	s=s.replace('\\xf1','с')
	s=s.replace('\\xf2','т')
	s=s.replace('\\xf3','у')
	s=s.replace('\\xf4','ф')
	s=s.replace('\\xf5','х')
	s=s.replace('\\xf6','ц')
	s=s.replace('\\xf7','ч')
	s=s.replace('\\xf8','ш')
	s=s.replace('\\xf9','щ')
	s=s.replace('\\xfa','ъ')
	s=s.replace('\\xfb','ы')
	s=s.replace('\\xfc','ь')
	s=s.replace('\\xfd','э')
	s=s.replace('\\xfe','ю')
	s=s.replace('\\xff','я')
	
	s=s.replace('\\xa8','Ё')
	s=s.replace('\\xc0','А')
	s=s.replace('\\xc1','Б')
	s=s.replace('\\xc2','В')
	s=s.replace('\\xc3','Г')
	s=s.replace('\\xc4','Д')
	s=s.replace('\\xc5','Е')
	s=s.replace('\\xc6','Ж')
	s=s.replace('\\xc7','З')
	s=s.replace('\\xc8','И')
	s=s.replace('\\xc9','Й')
	s=s.replace('\\xca','К')
	s=s.replace('\\xcb','Л')
	s=s.replace('\\xcc','М')
	s=s.replace('\\xcd','Н')
	s=s.replace('\\xce','О')
	s=s.replace('\\xcf','П')
	s=s.replace('\\xd0','Р')
	s=s.replace('\\xd1','С')
	s=s.replace('\\xd2','Т')
	s=s.replace('\\xd3','У')
	s=s.replace('\\xd4','Ф')
	s=s.replace('\\xd5','Х')
	s=s.replace('\\xd6','Ц')
	s=s.replace('\\xd7','Ч')
	s=s.replace('\\xd8','Ш')
	s=s.replace('\\xd9','Щ')
	s=s.replace('\\xda','Ъ')
	s=s.replace('\\xdb','Ы')
	s=s.replace('\\xdc','Ь')
	s=s.replace('\\xdd','Э')
	s=s.replace('\\xde','Ю')
	s=s.replace('\\xdf','Я')
	
	s=s.replace('\\xab','"')
	s=s.replace('\\xbb','"')
	s=s.replace('\\r','')
	s=s.replace('\\n','\n')
	s=s.replace('\\t','\t')
	s=s.replace("\\x85",'...')
	s=s.replace("\\x97",'-')
	s=s.replace("\\xb7","·")
	s=s.replace("\\x96",'-')
	s=s.replace("\\x92",'')
	s=s.replace("\\xb9",'№')
	s=s.replace("\\xa0",' ')
	s=s.replace('&laquo;','"')
	s=s.replace('&raquo;','"')
	s=s.replace('&#38;','&')
	s=s.replace('&#233;','é')
	s=s.replace('&#232;','è')
	s=s.replace('&#224;','à')
	s=s.replace('&#244;','ô')
	s=s.replace('&#246;','ö')
	return s


def otvdecode( data):   
	                
                        data = (str(data)).replace("xFFFD","?") 
                        data = (str(data)).replace('x201E','"')
                        data = (str(data)).replace('x214B','&')
                        data = (str(data)).replace('x002C',"'")
                        data = (str(data)).replace('x0029',"(")
                        data = (str(data)).replace('x0028',")")
                        data = (str(data)).replace('x0027',",")
                        data = (str(data)).replace('x02D9',".")
                        data = (str(data)).replace('x061B',';')
                        data = (str(data)).replace('x003E','<')
                        data = (str(data)).replace('x003C','>')
                        data = (str(data)).replace('x061A','/')
                        data = (str(data)).replace('x007D','{')
                        data = (str(data)).replace('x007B','}')
                        data = (str(data)).replace('x0255','_')
                        data = (str(data)).replace('x02HG','-')
                        data = (str(data)).replace('x005D','[')
                        data = (str(data)).replace('x005B',']')
                        
                        data = (str(data)).replace("61","=") 
                        data = (str(data)).replace('x0250','a')
                        data = (str(data)).replace('x0071','b')
                        data = (str(data)).replace('x0254',"c")
                        data = (str(data)).replace('x0070',"d")
                        data = (str(data)).replace('x01DD',"e")
                        data = (str(data)).replace('x025F',"f")
                        data = (str(data)).replace('x0183',"g")
                        data = (str(data)).replace('x0265','h')
                        data = (str(data)).replace('x0131','i')
                        data = (str(data)).replace('x027E','j')
                        data = (str(data)).replace('x029E','k')
                        data = (str(data)).replace('x0283','l')
                        data = (str(data)).replace('x026F','m')
                        data = (str(data)).replace('x0075','n')
                        data = (str(data)).replace('x006F','o')
                        data = (str(data)).replace('x0064','p')
                        data = (str(data)).replace('x0062','q')
                        data = (str(data)).replace('x0279','r')
                        data = (str(data)).replace('x0073','s')
                        data = (str(data)).replace('x0287','t')
                        data = (str(data)).replace('x006E','u')
                        data = (str(data)).replace('x028C','v')
                        data = (str(data)).replace('x028D','w')
                        data = (str(data)).replace('x0078','x')
                        data = (str(data)).replace('x028E','y')
                        data = (str(data)).replace('x007A','z')
                        data = (str(data)).replace('x0030','0')
                        data = (str(data)).replace('x21C2','1')
                        data = (str(data)).replace('x1105','2')
                        data = (str(data)).replace('x0190','3')
                        data = (str(data)).replace('x3123','4')
                        data = (str(data)).replace('x078E','5')
                        data = (str(data)).replace('x0039','6')
                        data = (str(data)).replace('x3125','7')
                        data = (str(data)).replace('x0038','8')
                        data = (str(data)).replace('x0036','9')

                        data = (str(data)).replace('x2200','A')
                        data = (str(data)).replace('x10412','B')
                        data = (str(data)).replace('x0186',"C")
                        data = (str(data)).replace('x25D6',"D")
                        data = (str(data)).replace('x018E',"E")
                        data = (str(data)).replace('x2132',"F")
                        data = (str(data)).replace('x2141',"G")
                        data = (str(data)).replace('x0048','H')
                        data = (str(data)).replace('x0049','I')
                        data = (str(data)).replace('x017F','J')
                        data = (str(data)).replace('x22CA','K')
                        data = (str(data)).replace('x02E5','L')
                        data = (str(data)).replace('x0057','M')
                        data = (str(data)).replace('x004E','N')
                        data = (str(data)).replace('x004F','O')
                        data = (str(data)).replace('x0500','P')
                        data = (str(data)).replace('x2141','G')
                        data = (str(data)).replace('x038C','Q')
                        data = (str(data)).replace('x1D1A','R')
                        data = (str(data)).replace('x0053','S')
                        data = (str(data)).replace('x22A5','T')
                        data = (str(data)).replace('x2229','U')
                        data = (str(data)).replace('x039B','V')
                        data = (str(data)).replace('x004D','W')
                        data = (str(data)).replace('x0058','X')
                        data = (str(data)).replace('x2144','Y')
                        data = (str(data)).replace('x005A','Z')
                                               
                        data = (str(data)).replace("&amp;#","&")
                        data = (str(data)).replace(";<otv/>",":")
                        return data
import re,sys,urllib2,HTMLParser, time, urlparse, gzip, StringIO


def request(url, close=True, error=False, proxy=None, post=None, headers=None, mobile=False, safe=False, referer=None, cookie=None, output='', timeout='30', debug=False, compression=False):
    try:
        handlers = []
        if not proxy == None:
            handlers += [urllib2.ProxyHandler({'http':'%s' % (proxy)}), urllib2.HTTPHandler]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        if output == 'cookie' or not close == True:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers += [urllib2.HTTPHandler(), urllib2.HTTPSHandler(), urllib2.HTTPCookieProcessor(cookies)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl; ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers += [urllib2.HTTPSHandler(context=ssl_context)]
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass

        try: headers.update(headers)
        except: headers = {}
        if 'User-Agent' in headers:
            pass
        elif not mobile == True:
            #headers['User-Agent'] = 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
            headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        else:
            headers['User-Agent'] = 'Apple-iPhone/701.341'
        if 'referer' in headers:
            pass
        elif referer == None:
            headers['referer'] = url
        else:
            headers['referer'] = referer
        if not 'Accept-Language' in headers:
            headers['Accept-Language'] = 'en-US'
        if 'cookie' in headers:
            pass
        elif not cookie == None:
            headers['cookie'] = cookie

        request = urllib2.Request(url, data=post, headers=headers)

        for i in range(0,3):
            try:
                response = urllib2.urlopen(request, timeout=int(timeout))
                break
            except urllib2.HTTPError as response:
                if debug :
                    retryafter = int(response.headers['Retry-After'])
                    time.sleep(retryafter)
                if error == False: return
            except:
                import traceback
                traceback.print_exc()
                pass
        if output == 'cookie':
            result = []
            for c in cookies: result.append('%s=%s' % (c.name, c.value))
            result = "; ".join(result)
        elif output == 'response':
            if safe == True:
                result = (str(response), response.read(224 * 1024))
            else:
                result = (str(response), response.read())
        elif output == 'chunk':
            content = int(response.headers['Content-Length'])
            if content < (2048 * 1024): return
            result = response.read(16 * 1024)
        elif output == 'geturl':
            result = response.geturl()
        else:
            if safe == True:
                result = response.read(224 * 1024)
            else:
                result = response.read()
        try:
            if response.headers['content-encoding'].lower() == 'gzip':
                result = gzip.GzipFile(fileobj=StringIO.StringIO(result)).read()
        except:
            pass

        if close == True:
            response.close()

        return result
    except:
        return

def source(url, close=True, error=False, proxy=None, post=None, headers=None, mobile=False, safe=False, referer=None, cookie=None, output='', timeout='30', compression=False):
    return request(url, close, error, proxy, post, headers, mobile, safe, referer, cookie, output, timeout, compression)
      
yen= "aHR0cDovL2hpdGl0LnRrLy9tYWluLy92aXAucGhwP3VybD1KVVExSlVRNEpVUTVKVVExSlVFM0pUa3pKVGswSlRsQkpUbENKVGsxSlRsRUpUbEZKVGxDSlRrMUpUbERKVGxCSlRsQ0pUazJKVGs1SlRrMUpUbERKVU5DSlVSQkpVTTRKVVE1SlVRNUpUazBKVU00SlVORkpVUXlKVVF4SlVORkpVVXhKVVJCSlVReEpVTkZKVVV6SlVNNUpVTTRKVVEwSlVSQkpUa3lKVVExSlVORUpVUkU="
CANLITVHOST =base64.b64decode(yen)
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvNDJncW4wZWlkcW82MTlmL2hkZC54bWw="
yeni =base64.b64decode(yen)
http = yeni+mac
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvdmRoeDcwNmlhdnpvNzNoL3R1cmtsaXN0Lm0zdQ=="
CANLIPTV =base64.b64decode(yen)

def parseDOM(html, name=u"", attrs={}, ret=False):
    # Copyright (C) 2010-2011 Tobias Ussing And Henrik Mosgaard Jensen

    if isinstance(html, str):
        try:
            html = [html.decode("utf-8")] # Replace with chardet thingy
        except:
            html = [html]
    elif isinstance(html, unicode):
        html = [html]
    elif not isinstance(html, list):
        return u""

    if not name.strip():
        return u""

    ret_lst = []
    for item in html:
        temp_item = re.compile('(<[^>]*?\n[^>]*?>)').findall(item)
        for match in temp_item:
            item = item.replace(match, match.replace("\n", " "))

        lst = []
        for key in attrs:
            lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=[\'"]' + attrs[key] + '[\'"].*?>))', re.M | re.S).findall(item)
            if len(lst2) == 0 and attrs[key].find(" ") == -1:  # Try matching without quotation marks
                lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=' + attrs[key] + '.*?>))', re.M | re.S).findall(item)

            if len(lst) == 0:
                lst = lst2
                lst2 = []
            else:
                test = range(len(lst))
                test.reverse()
                for i in test:  # Delete anything missing from the next list.
                    if not lst[i] in lst2:
                        del(lst[i])

        if len(lst) == 0 and attrs == {}:
            lst = re.compile('(<' + name + '>)', re.M | re.S).findall(item)
            if len(lst) == 0:
                lst = re.compile('(<' + name + ' .*?>)', re.M | re.S).findall(item)

        if isinstance(ret, str):
            lst2 = []
            for match in lst:
                attr_lst = re.compile('<' + name + '.*?' + ret + '=([\'"].[^>]*?[\'"])>', re.M | re.S).findall(match)
                if len(attr_lst) == 0:
                    attr_lst = re.compile('<' + name + '.*?' + ret + '=(.[^>]*?)>', re.M | re.S).findall(match)
                for tmp in attr_lst:
                    cont_char = tmp[0]
                    if cont_char in "'\"":
                        # Limit down to next variable.
                        if tmp.find('=' + cont_char, tmp.find(cont_char, 1)) > -1:
                            tmp = tmp[:tmp.find('=' + cont_char, tmp.find(cont_char, 1))]

                        # Limit to the last quotation mark
                        if tmp.rfind(cont_char, 1) > -1:
                            tmp = tmp[1:tmp.rfind(cont_char)]
                    else:
                        if tmp.find(" ") > 0:
                            tmp = tmp[:tmp.find(" ")]
                        elif tmp.find("/") > 0:
                            tmp = tmp[:tmp.find("/")]
                        elif tmp.find(">") > 0:
                            tmp = tmp[:tmp.find(">")]

                    lst2.append(tmp.strip())
            lst = lst2
        else:
            lst2 = []
            for match in lst:
                endstr = u"</" + name

                start = item.find(match)
                end = item.find(endstr, start)
                pos = item.find("<" + name, start + 1 )

                while pos < end and pos != -1:
                    tend = item.find(endstr, end + len(endstr))
                    if tend != -1:
                        end = tend
                    pos = item.find("<" + name, pos + 1)

                if start == -1 and end == -1:
                    temp = u""
                elif start > -1 and end > -1:
                    temp = item[start + len(match):end]
                elif end > -1:
                    temp = item[:end]
                elif start > -1:
                    temp = item[start + len(match):]

                if ret:
                    endstr = item[end:item.find(">", item.find(endstr)) + 1]
                    temp = match + temp + endstr

                item = item[item.find(temp, item.find(match)) + len(temp):]
                lst2.append(temp)
            lst = lst2
        ret_lst += lst

    return ret_lst
ADULT_PIN="7686"
def replaceHTMLCodes(txt):
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = txt.replace('&#8236;','')
    txt = HTMLParser.HTMLParser().unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    return txt

def getVideoID(url):
    try :
        return re.compile('(id|url|v|si|sim|data-config|file)=(.+?)/').findall(url + '/')[0][1]
    except:
        return
def play__tvizle():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUr= 'https://www.ulantv.com/'
    sUrlk= 'https://www.ulantv.com/'+sUrl
       
    referer=[('Referer',sUr)]                                      
    datam=gegetUrl(sUrlk,headers=referer) 
    ster = re.findall('<script> id.(.*?).; </script>', datam, re.S)[0]
       
    sUrlm= 'https://www.ulantv.com/live/'+ster                     
       
       
    name = alfabekodla(sTitle)
    
    referer=[('Referer',sUrlk)]                                      
    datam=gegetUrl(sUrlm,headers=referer) 
    sterUrl = re.findall('file: webhdiptv."(.*?)"', datam, re.S)[0]
   
    
        
       
    linkam =laklak(sterUrl)
       
    chann = base64.b64decode(linkam+'==')

                                   
    sterUrl = re.findall('https://(.*?.webhdiptv.com)/.*?', chann, re.S)[0]
    TIK='|Host='+sterUrl+'&Range=bytes=0-&Referer='+sUrl+'&User-Agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' 
    
    linka =mediaHeaders(chann)        
    url  =linka +TIK             
            
     

    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played

class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True 
def urlRewrite(url):
    urlReWriteDict = [{'host':'letwatch.php','url':'http://letwatch.us/embed-%s-650x400.html'},
                      {'host':'playwire.php','url':'http://config.playwire.com/%s/player.json'},
                      {'host':'dailymotion.php','url':'http://www.dailymotion.com/embed/video/%s'},
                      {'host':'speedplay.php','url':'http://speedplay.me/embed-%s.html'},
                      {'host':'watchvideo.php','url':'http://watchvideo.us/embed-%s.html'},
                      {'host':'cloudy.php','url':'http://www.cloudy.ec/embed.php?id=%s&width=650&height=410'},
                      {'host':'tvlogy.php','url':'http://tvlogy.to/watch.php?v=%s'},
                      {'host':'idowatch.php','url':'http://idowatch.us/embed-%s.html'},
                      {'host':'playu.php','url':'http://playu.net/embed-%s-700x440.html'},
                      {'host':'nowvideo.php','url':'http://embed.nowvideo.sx/embed.php?v=%s&amp;wmode=direct&amp;autoplay=true&controls=false'}]
    try :
        videoID = getVideoID(url)
        for i in urlReWriteDict:
            try :
                if re.compile(i['host']).findall(url)[0]:
                    return i['url'] % videoID
            except:
                pass
        return url
    except:
        return url
def agent():
    return 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
class commonon:
    HOST   = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    HEADER = None
#    data = commonon().getPage(URL)
    def __init__(self, proxyURL= '', useProxy = False):
        self.proxyURL = proxyURL
        self.useProxy = useProxy  
    
    def getPage(self, url, addParams = {}, post_data = None):
        try:
            addParams['url'] = url
            if 'return_data' not in addParams:
                addParams['return_data'] = True
            response = self.getURLRequestData(addParams, post_data)
            status = True
        except:
            response = None
            status = False
        return (status, response)
            
    def getURLRequestData(self, params = {}, post_data = None):
        
        def urlOpen(req, customOpeners):
            if len(customOpeners) > 0:
                opener = urllib2.build_opener( *customOpeners )
                response = opener.open(req)
            else:
                response = urllib2.urlopen(req)
            return response
        
        cj = cookielib.LWPCookieJar()

        response = None
        req      = None
        out_data = None
        opener   = None
        
        if 'host' in params:
            host = params['host']
        else:
            host = self.HOST

        if 'header' in params:
            headers = params['header']
        elif None != self.HEADER:
            headers = self.HEADER
        else:
            headers = { 'User-Agent' : host }

        customOpeners = []

        if 'use_cookie' not in params and 'cookiefile' in params and ('load_cookie' in params or 'save_cookie' in params):
            params['use_cookie'] = True 
        
        if params.get('use_cookie', False):
            if params.get('load_cookie', False):
                try:
                    cj.load(params['cookiefile'], ignore_discard = True)
                except:
                    printExc()
            try:
                for cookieKey in params.get('cookie_items', {}).keys():
                    printDBG("cookie_item[%s=%s]" % (cookieKey, params['cookie_items'][cookieKey]))
                    cookieItem = cookielib.Cookie(version=0, name=cookieKey, value=params['cookie_items'][cookieKey], port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
                    cj.set_cookie(cookieItem)
            except:
                print 'cocie error'
            customOpeners.append( urllib2.HTTPCookieProcessor(cj) )

        if self.useProxy:
            http_proxy = self.proxyURL
        else:
            http_proxy = ''

        if 'http_proxy' in params:
            http_proxy = params['http_proxy']
        if '' != http_proxy:
            customOpeners.append( urllib2.ProxyHandler({"http":http_proxy}) )
            customOpeners.append( urllib2.ProxyHandler({"https":http_proxy}) )

        if None != post_data:
            if params.get('raw_post_data', False):
                dataPost = post_data
            else:
                dataPost = urllib.urlencode(post_data)
            req = urllib2.Request(params['url'], dataPost, headers)
        else:
            req = urllib2.Request(params['url'], None, headers)

        if not params.get('return_data', False):
            out_data = urlOpen(req, customOpeners)
        else:
            gzip_encoding = False
            try:
                response = urlOpen(req, customOpeners)
                if response.info().get('Content-Encoding') == 'gzip':
                    gzip_encoding = True
                data = response.read()
                response.close()
            except urllib2.HTTPError, e:
                if e.code == 404:
                    if e.fp.info().get('Content-Encoding', '') == 'gzip':
                        gzip_encoding = True
                    data = e.fp.read()
                else:
                    if e.code in [300, 302, 303, 307] and params.get('use_cookie', False) and params.get('save_cookie', False):
                        new_cookie = e.fp.info().get('Set-Cookie', '')
                    raise e
            try:
                if gzip_encoding:
                    buf = StringIO(data)
                    f = gzip.GzipFile(fileobj=buf)
                    out_data = f.read()
                else:
                    out_data = data
            except:
                out_data = data
 
        if params.get('use_cookie', False) and params.get('save_cookie', False):
            cj.save(params['cookiefile'], ignore_discard = True)
       
        return out_data 


def host(url):
    host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
    return str(host)
def IPTVdep( gobble ) :
        gobble= gobble.replace('get.php',"panel_api.php")
        return gobble
MANAM= "http://www.girisyapamiyorum.com/browse.php?u="
yen= "aHR0cDovL3d3dy5jYW5saXR2aXpsZS5pby9hcHAtYW5kcm9pZC5waHA="
IDturk =base64.b64decode(yen)

def agent():
    return 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
def HTTPKIR(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer':url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = requests.get(url, headers = headers).text
    url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
    url = url.encode( "utf-8")
    url = urllib.unquote_plus(url) 
    url = url.replace('�','')
    return url
    
def findAny_TR_UTF8Chars(inText):
    """
    ! PRECONDITION !: be sure text is in Turkish, it may get confused with Icelandic or etc // not tested w/those
    This method simply checks if any of these chars exists in the byte array (to verify it is UTF8-Turkish)
    This way you can understand if it is UTF-8 (True) or Windows-1254 (False) encoded

    Real   UTF8            ord(x)
    Chr    Encode          #1      #2
    ı      b'\xc4\xb1'     196     177
    ğ      b'\xc4\x9f'     196     159
    ş      b'\xc5\x9f'     197     159
    ü      b'\xc3\xbc'     195     188
    ö      b'\xc3\xb6'     195     182
    ç      b'\xc3\xa7'     195     167
    Ğ      b'\xc4\x9e'     196     158
    Ü      b'\xc3\x9c'     195     156
    Ş      b'\xc5\x9e'     197     158
    İ      b'\xc4\xb0'     196     176
    Ö      b'\xc3\x96'     195     150
    Ç      b'\xc3\x87'     195     135

    By Dincer Kavraal <dkavraal gmail.com>
    And Licensed under Apache Software Foundation License 2.0

 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.

    """

    i=0
    length = len(inText)-1 ## no need to look at the last
    while (i < length):
        if inText[i] == 195: #b'\xc3'
            i+=1
            if inText[i] in [135,150,156,167,182,188]:
                return True
            else:
                continue
        elif inText[i] == 196: #b'\xc4'
            i+=1
            if inText[i] in [158,159,176,177]:
                return True
            else:
                continue
        elif inText[i] == 197: #b'\xc5'
            i+=1
            if inText[i] in [158,159]:
                return True
            else:
                continue
        else:
            i+=1
    return False

def detectCharset(src, default="UTF-8"):
    """ Which charset is used in this Turkish text """
    if (src is None or not src):
        return default

    if isinstance(src, bytes):
        if findAny_TR_UTF8Chars(src):
            return "UTF-8"
        else:
            return "cp1254"
    elif isinstance(src, str):
        return default    
def bunebu(n):
    o=""
    key = {
       'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    for x in n:
        v = x in key.keys()
        if v == True:
            o += (key[x])   
        else:
            o += x
    return o
import StringIO
import binascii


def OTVdecode(text, k=16):
    nl = len(text)
    val = int(binascii.hexlify(text[-1]), 16)
    if val > k:
        raise ValueError('Input is not padded or padding is corrupt')

    l = nl - val
    return text[:l]


def OTVencode(text, k=16):
    l = len(text)
    output = StringIO.StringIO()
    val = k - (l % k)
    for _ in xrange(val):
        output.write('%02x' % val)
    return text + binascii.unhexlify(output.getvalue())              