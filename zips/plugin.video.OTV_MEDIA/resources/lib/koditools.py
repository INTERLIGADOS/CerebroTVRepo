#	-*-	coding:	utf-8	-*-
from urllib2 import Request, URLError, urlopen as urlopen2
from socket import gaierror, error
from resources.lib.gui.guiElement import cGuiElement
import re, httplib, urllib, urllib2, os, cookielib, socket, sha, shutil, datetime, math, hashlib, random, json, md5, string, xml.etree.cElementTree, StringIO, Queue, threading, sys
from urllib import quote, unquote_plus, unquote, urlencode
from urlparse import parse_qs, parse_qsl
iconimage=None
import base64
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
import common
import re
import string
from resources.lib.pCommon import common, CParsingHelper,GetCookieDir
from parser import JJDecoder
from parser import cPacker
import re,xbmcgui,unicodedata
import urllib2,urllib,re,HTMLParser,cookielib
import sys,os,base64,time
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from resources.lib.aadecode import AADecoder

import unwise
import re, cookielib, time, xbmcgui, xbmc, os, urllib2
from urllib2 import Request, URLError, urlopen as urlopen2
from urlparse import parse_qs
from urllib import quote, urlencode, unquote_plus, unquote
from httplib import HTTPConnection, CannotSendRequest, BadStatusLine, HTTPException
from socket import gaierror, error
from t0mm0.common.net import Net
from jsunpacker import cJsUnpacker
from resources.lib.gui.gui import cGui
from resources.lib.util import cUtil,VSlog
from resources.lib.parser import cParser
from resources.lib.handler.requestHandler import cRequestHandler
import requests
import re
net = Net()
import jsunpack
import logger     
cm = common()
from httpkir import httptools,scrapertools
SITE_IDENTIFIER = 'youtubecom_tr'
SITE_NAME = 'koditools'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
def unescape(src):
    s = src.decode('string-escape')
    u = s.decode('utf8')
    
    return u.encode('unicode-escape')
def waitmsg(sec, msg):
		isec = int(sec)
		if isec > 0:
			dialog = xbmcgui.DialogProgress()
			dialog.create('Resolving', '%s Link.. Wait %s sec.' % (msg, sec))
			dialog.update(0)
			c = 100 / isec
			i = 1
			p = 0
			while i < isec+1:
				p += int(c)
				time.sleep(1)
				dialog.update(int(p))
				i += 1
			dialog.close()


import re
def rm(fullname):
    try:
        os.remove(fullname)
        return True
    except Exception as ex:
        print ex
    return False

def check_url(url):
    import urlparse
    parts = urlparse.urlsplit(url)
    if not parts.scheme or not parts.netloc:
        return False
    else:
        return True
from  rutrans import detranslify
def showLinks(sUrl):
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    url  = sHtmlContent
    return url          
def mediaHeaders(chann,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69','Referer':ref ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann     
from resources.lib import jsunprotect
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


def ABCkodla(sMovieTitle):
    
    sMovieTitle = sMovieTitle.decode("unicode_escape").encode("utf-8")#vire accent et '\'
     #on repasse en utf-8
 
    return sMovieTitle

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'

def youtube(url):                    
    from resources.lib.youtube import get_video_url,find_videos
    oGui = cGui()	
    data = url
    page_url =find_videos(data)
    (name,urlm,urlk)=page_url[0] 
    channel = get_video_url(urlm)
    for sTitle, sUrl in channel:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory() 

def closeload(url):
    oGui = cGui()
                      
    
    referer=[('Referer',url)]
    urll=gegetUrl(url,headers=referer) 
    urll=urll.replace(',{}))',",{}))</script>").replace('\s',"").replace('\n',"")
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    sPattern = "(eval.function.p,a,c,k,e,d.*?)</script>"
    aResult = re.findall(sPattern,urll)
        
    if (aResult):
       sUnpacked = cPacker().unpack(aResult[0])
       urlll = re.findall('"file":"(.*?)"', sUnpacked, re.S|re.I)[0]+ TIK 
       name = 'closeload'
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,urlll,'') 

def uptostream(url):
    oGui = cGui()
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    if not 'http' in url:
       url = 'http:'+ url
    
    data=requests.get(url,headers={'Host':'uptostream.com','User-Agent':UA,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;','Connection':'keep-alive'}).text
                            
    stream_url = re.findall("<source src='(.*?)' type='video/mp4' data-res='(.*?)'.*?lang='(.*?)'",data, re.S)
    for sUrl,sTitle,lang in stream_url:
                                              
         
        sUrl = 'https:'+ sUrl+ TIK 
        sTitle =sTitle+':'+lang         
        sTitle =alfabekodla(sTitle)   
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
def streamangodecode( encoded, code):
        #from https://github.com/jsergio123/script.module.urlresolver
        _0x59b81a = ""
        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        k = k[::-1]

        count = 0

        for index in range(0, len(encoded) - 1):
            while count <= len(encoded) - 1:
                _0x4a2f3a = k.index(encoded[count])
                count += 1
                _0x29d5bf = k.index(encoded[count])
                count += 1
                _0x3b6833 = k.index(encoded[count])
                count += 1
                _0x426d70 = k.index(encoded[count])
                count += 1

                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
                _0x2e4782 = _0x2e4782 ^ code

                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

        return _0x59b81a

def streamango(url):
    oGui = cGui()
  
    if not 'http' in url:
       url = 'http:'+ url
    
    data=requests.get(url,headers={'Host':'streamango.com','User-Agent':UA,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;','Connection':'keep-alive'}).text
            
    matches = re.findall('type:"video/([^"]+)",src:d\\(\'([^\']+)\',(.*?)\\).+?height:(\\d+)', data, re.DOTALL | re.MULTILINE)
    for ext, encoded, code, quality in matches:
        media_url = streamangodecode(encoded, int(code))
        if not 'http' in media_url:
           media_url= 'http:'+ media_url
        name = 'streamango.com'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,media_url,'')
def wholecloud(url):
    oGui = cGui()
    url = url.replace('movshare.net', 'wholecloud.net')
    headers = {'User-Agent': UA,'Referer': url}
    media_id = re.findall('(?:video/|embed(?:/|\\.php)\\?(?:v|id)=)([A-Za-z0-9]+)', url, re.IGNORECASE)[0]
    url = 'http://www.wholecloud.net/video/' + media_id
    TIK='|Refere='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    data=requests.get(url,headers={'Host':'www.wholecloud.net','User-Agent':UA,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;','Connection':'keep-alive'}).text
    fname = re.findall('<input type="hidden" name="stepkey".*?alue="(.*?)">', data)
    info = { 'stepkey': fname[0], 'submit':'submit'}
    urlk = net.http_POST(url, info).content   
    urll = re.findall('<source src="(.*?flv)" type=\'video/x-flv\'>', urlk, re.S|re.I)[0]+ TIK 
    name = 'wholecloud.net'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,urll,'')
                     
        
def streamcloud(url):
		net = Net()
                if not 'http' in url:
                   url = 'http:'+ url
                data = net.http_GET(url).content
		id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
		fname = re.findall('<input type="hidden" name="fname".*?alue="(.*?)">', data)
		hash = re.findall('<input type="hidden" name="hash" value="(.*?)">', data)
		if id and fname and hash:
		    url = "http://streamcloud.eu/%s" % id[0]			
		    info = {'op': 'download2', 'usr_login': '', 'id': id[0], 'fname': fname[0], 'referer': '', 'hash': hash[0], 'imhuman':'Weiter+zum+Video'}
                
                    name = "streamcloud.eu" 
		    data = net.http_POST(url, info).content
		    stream_url = re.findall('file: "(.*?)"', data)
                    url =stream_url[0]
                    name = 'streamcloud'
                    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
    
def mflashxx(url):
    

    net = Net()
    data = net.http_GET(url).content

    cookie = getUrl(url, output='cookie').result
 #   cookie='VID=2SlVa309oFH4; mrcu=EE18510E964723319742F901060A; p=IxQAAMr+IQAA; video_key=203516; s='
    h = "|Cookie=%s" % urllib.quote(cookie)            
    id = re.findall('<input type="hidden" name="id".*?value="(.*?)">', data)
    fname = re.findall('<input type="hidden" name="fname".*?alue="(.*?)">', data)
    hash = re.findall('<input type="hidden" name="hash" value="(.*?)">', data)
    if id and fname and hash:
			
	post = {'op': 'download1', 'usr_login': '', 'id': id[0], 'fname': fname[0], 'referer': '', 'hash': hash[0], 'imhuman':'Weiter+zum+Video'}

        time.sleep(6)

    
	urll ='https://www.flashx.tv/dl?playnow'
        urlk = net.http_POST(urll, post).content
        url = re.findall("src: '(.*?)',type: 'video/mp4',label: '.*?'",urlk , re.S)[0]+h
#       for sUrl,sTitle in stream_url:
                                              
        name = 'Flashx'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def thevideome(url):
    oGui = cGui()	
    data = net.http_GET(url).content
    stream_url = re.findall('"file":"(.*?)","label":"(.*?)"', data,re.DOTALL)
    for sUrl,sTitle in stream_url:
        key = re.findall("var lets_play_a_game='(.*?)'",data,re.DOTALL)
        ke = re.findall("'rc=[^<>]+?\/(.+?)'\.concat",data,re.DOTALL)
        url2 = 'https://thevideo.me/'+ ke[0]+'/' + key[0] 
       
       
                
        data_pack= net.http_GET(url2).content
        data_pack = data_pack.replace('|httpfallback','').replace('|in',"").replace('|indexOf',"").replace('|jwConfig',"").replace('|return',"").replace('|sources',"").replace('|ua',"").replace('|vt',"").replace('|file',"").replace('|false',"").replace('|direct',"").replace('|var',"").replace('|for',"").replace('|if',"").replace('|playlist',"").replace('|length',"").replace('|function',"").replace('|',"")
        keyi = re.findall(",30,'(.+?)'.split",data_pack,re.DOTALL)
        sUrl=sUrl+ '?direct=false&ua=1&vt='+keyi[0]
        
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
            
        
def vidmoly(url):                    
    oGui = cGui()	
    if not 'http' in url:
       url = 'http:'+ url
    data = net.http_GET(url).content
    data=data.replace('sources: ["https://',"")
     
    stream = re.findall('"(https://.*?/v.mp4)"',data, re.S)
    for stream_url in stream:
       tarzlistesi= [] 
       tarzlistesi.append(("sd", "%s"  % stream_url ))
       tarzlistesi.append(("hd", "%s" % stream_url ))
       tarzlistesi.append(("full", "%s" % stream_url ))        
       for sTitle,sUrl in tarzlistesi:
    
                                              
          TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

          sUrl= sUrl+TIK
         
          sTitle = alfabekodla(sTitle)         
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
          oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
          oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
       

def raptu(url):                    
    oGui = cGui()	
    data = net.http_GET(url).content
    data=data.replace('\/',"/").replace('"file":"https://www.raptu.com',"")
      
    stream_url = re.findall('"file":"(.*?)","label":"(.*?)"',data, re.S)
    for sUrl,sTitle in stream_url:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
   
def name_prepare(videoTitle):
        print 'DUZELTME ONCESI:',videoTitle
        videoTitle=videoTitle.replace('�zle',"").replace('T�rk�e',"").replace('Turkce',"").replace('Dublaj',"|TR|").replace('Altyaz�l�'," [ ALTYAZILI ] ").replace('izle',"").replace('Full',"").replace('720p',"").replace('HD',"")
        return videoTitle   
        
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link=link.replace('\xFD',"i").replace('&#39;&#39;',"\"").replace('&#39;',"\'").replace('\xf6',"o").replace('&amp;',"&").replace('\xd6',"O").replace('\xfc',"u").replace('\xdd',"I").replace('\xfd',"i").replace('\xe7',"c").replace('\xde',"s").replace('\xfe',"s").replace('\xc7',"c").replace('\xf0',"g")
        link=link.replace('\xc5\x9f',"s").replace('&#038;',"&").replace('&#8217;',"'").replace('\xc3\xbc',"u").replace('\xc3\x87',"C").replace('\xc4\xb1',"�").replace('&#8211;',"-").replace('\xc3\xa7',"c").replace('\xc3\x96',"O").replace('\xc5\x9e',"S").replace('\xc3\xb6',"o").replace('\xc4\x9f',"g").replace('\xc4\xb0',"I").replace('\xe2\x80\x93',"-")
        response.close()
        return link

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok


def addDir(name,url,thumbnail,mode,filepath):
        if thumbnail != "":
                thumbnail = os.path.join(IMAGES_PATH, thumbnail+".jpg")
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(thumbnail)+"&filepath="+urllib.quote_plus(filepath)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def videoraj(url):
        fileName ="cozucu"
        data = net.http_GET(url).content
        TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

        url = re.findall('key: "(.*?)".*?file:"(.*?)"', data, re.S)                                      
        for filekey, media_id in url:

            player_url = 'http://www.videoraj.to/api/player.api.php?pass=&numOfErrors=0&cid=1&cid3=&key=%s&user=&cid2=&file=%s' % (filekey, media_id)

            html = net.http_GET(player_url).content
            html=html.replace('%3D',"=").replace('%26',"&").replace('%3F',"?").replace('%3A',":").replace('%2F',"/").replace('\xc3\xa7',"c").replace('\xc3\x96',"O").replace('\xc5\x9e',"S").replace('\xc3\xb6',"o").replace('\xc4\x9f',"g").replace('\xc4\xb0',"I").replace('\xe2\x80\x93',"-")
	
            url= re.findall('url=(.+?)&', html)[0]+TIK  
            
            
                                                             
	    name = 'videoraj'
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')


        
def fileztv(url):
        html2  = requests.get(url).content
        urlk= re.search(r'<div class="largeDownloadButtons">.*?<a href="(.*?)">', html2, re.S)         
        urlk= url1.group(1)
       
        html  = requests.get(urlk).content
        
        urll = re.findall('file: "(.*?)"', html)
        urll= urll[0]
           
        name = 'fileztv'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,urll,'')

def vivosx(url):

            html  = requests.get(url).content
            urll= re.search(r'Core\.InitializeStream \(\'(.*?)\'\)', html)        
            
            b = base64.b64decode(urll.group(1))
            chann = json.loads(b)
            if len(chann) == 0: raise ResolverError('video not found')
            TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

            chann= chann[0]
            url= mediaHeaders(chann,url)
            url=url+TIK
            name = 'vivosx'
            addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def estreamto(url):
    oGui = cGui()
    TIK='|Referer='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    if not 'http' in url:
       url = 'http:'+ url
    
    data=requests.get(url,headers={'Host':'estream.to','User-Agent':UA,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;','Connection':'keep-alive'}).text
          
    stream_url = re.findall("<source src=\"(.*?)\" type='video/mp4' label='(.*?)'",data, re.S)
    for sUrl,sTitle in stream_url:
                                              
        sUrl =sUrl+TIK 
        
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
        
def vidzitv(url):
    oGui = cGui()                
    html  = requests.get(url).content
    urll= re.findall('file: "(https://.*?/master.m3u8)"', html)[0]        
           
    data = requests.get(urll).content


    
      
    stream_url = re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=.*?,RESOLUTION=(.*?),FRAME-RATE=.*?,CODECS=".*?"\n(.*?)\n',data, re.S)
    for sTitle,sUrl in stream_url:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  

def magix_player(name,url):
    import urlresolver
    UrlResolverPlayer = url
    playList.clear()
    media = urlresolver.HostedMediaFile(UrlResolverPlayer)
    source = media
    if source:
            url = source.resolve()
            
            playlist_yap(playList,name,url)
            xbmcPlayer.play(playList)

                  
def playlist_yap(playList,name,url):
        listitem = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage="")
        listitem.setInfo('video', {'name': name } )
        playList.add(url,listitem=listitem)
        return playList
    #---------------------------------#
USER_AGENT 	= 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36'
ACCEPT 		= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

def ok_ru(url):
        
    oGui = cGui()
    url=url.replace('https://m.ok.ru/video/',"").replace('http://ok.ru/videoembed/',"").replace('https://ok.ru/videoembed/',"").replace('https://odnoklassniki.ru/videoembed/',"")    
    url= "https://m.ok.ru/video/%s" % url
    
                      
    data= requests.get(url).content
                        
    stream = re.findall('data-embedclass="yt_layer" data-objid=".*?" href="(.*?)"', data, re.S)
    url = stream[0]
    tarzlistesi= []
    tarzlistesi.append(("full", ""+url.replace('st.mq=2','st.mq=6').replace('amp;',"") ))  
    tarzlistesi.append(("hd", "%s" % url.replace('st.mq=2','st.mq=5').replace('amp;',"") ))
    tarzlistesi.append(("sd", "%s" % url.replace('st.mq=2','st.mq=3').replace('amp;',"") ))
    tarzlistesi.append(("low", "%s" % url.replace('st.mq=2','st.mq=2').replace('amp;',"") ))
    tarzlistesi.append(("lowes", "%s" % url.replace('st.mq=2','st.mq=1').replace('amp;',"") ))
    tarzlistesi.append(("mobile", "%s" %url.replace('st.mq=2','st.mq=4').replace('amp;',"") ))
    
    
    
    
          
    
    for sTitle,sUrl in tarzlistesi:
           
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()


def http_req(url, getCookie=False):
	req = urllib2.Request(url)
	req.add_header('User-Agent', USER_AGENT)
	req.add_header('Accept', ACCEPT)
	req.add_header('Cache-Control', 'no-transform')
	response = urllib2.urlopen(req)
	source = response.read()
	response.close()
	if getCookie:
		cookie = response.headers.get('Set-Cookie')
		return {'source': source, 'cookie': cookie}
	return source
def PlayPlay(url):
    name = 'Direct line'
    url=alfabekodla(url)    
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmc.Player().play( url , listitem)
def PlayerPlayer(name,url):

    url=alfabekodla(url)    
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmc.Player().play( url , listitem)
def MailRu(url):
    oGui = cGui()
    tarzlistesi= []                 
    
    data = requests.get(url).content
  
    stream = re.findall('"metaUrl": "(.*?)"', data, re.S)
    Url = str(stream[0])
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('//cdn',"https://cdn") 
    tarzlistesi = re.findall('"url":"(https.*?)".*?"key":"(.*?)"', data, re.S)
    
    cookie = getUrl(Url, output='cookie').result
 #   cookie='VID=2SlVa309oFH4; mrcu=EE18510E964723319742F901060A; p=IxQAAMr+IQAA; video_key=203516; s='
    h = "|Cookie=%s" % urllib.quote(cookie)
    for sUrl,sTitle in tarzlistesi:
                                              
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl',str(sUrl+h))
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER , 'showBoxxx', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()  
def magictr():
       oGui = cGui() 
       sMovieTitle='http://www.youtube.com/embed/6VAquSxygQE'
       HosterUrl='http://www.youtube.com/embed/6VAquSxygQE'
        
       oHoster = cHosterGui().checkHoster(sHosterUrl)

       if (oHoster != False):
           sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
           oHoster.setDisplayName(sDisplayTitle)
           oHoster.setFileName(sMovieTitle)
           cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

       

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

#UA = 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
    
def GetIp():
    if (False):
        oRequest = cRequestHandler('http://hqq.tv/player/ip.php?type=json')
        oRequest.addHeaderEntry
        sHtmlContent = oRequest.request()
        ip = re.search('"ip":"([^"]+)"', sHtmlContent, re.DOTALL).group(1)
    else:
        import random
        for x in xrange(1,100):
            ip = "192.168."
            ip += ".".join(map(str, (random.randint(0, 255) for _ in range(2))))
        ip = base64.b64encode(ip)

    return ip

def _decode2(file_url):
    def K12K(a, typ='b'):
        codec_a = ["G", "L", "M", "N", "Z", "o", "I", "t", "V", "y", "x", "p", "R", "m", "z", "u",
                   "D", "7", "W", "v", "Q", "n", "e", "0", "b", "="]
        codec_b = ["2", "6", "i", "k", "8", "X", "J", "B", "a", "s", "d", "H", "w", "f", "T", "3",
                   "l", "c", "5", "Y", "g", "1", "4", "9", "U", "A"]
        if 'd' == typ:
            tmp = codec_a
            codec_a = codec_b
            codec_b = tmp
        idx = 0
        while idx < len(codec_a):
            a = a.replace(codec_a[idx], "___")
            a = a.replace(codec_b[idx], codec_a[idx])
            a = a.replace("___", codec_b[idx])
            idx += 1
        return a

    def _xc13(_arg1):
        _lg27 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        _local2 = ""
        _local3 = [0, 0, 0, 0]
        _local4 = [0, 0, 0]
        _local5 = 0
        while _local5 < len(_arg1):
            _local6 = 0
            while _local6 < 4 and (_local5 + _local6) < len(_arg1):
                _local3[_local6] = _lg27.find(_arg1[_local5 + _local6])
                _local6 += 1
            _local4[0] = ((_local3[0] << 2) + ((_local3[1] & 48) >> 4))
            _local4[1] = (((_local3[1] & 15) << 4) + ((_local3[2] & 60) >> 2))
            _local4[2] = (((_local3[2] & 3) << 6) + _local3[3])

            _local7 = 0
            while _local7 < len(_local4):
                if _local3[_local7 + 1] == 64:
                    break
                _local2 += chr(_local4[_local7])
                _local7 += 1
            _local5 += 4
        return _local2

    return _xc13(K12K(file_url, 'e'))

def hqqtv(url):
        headers = {'User-Agent': UA ,
                   #'Host' : 'hqq.tv',
                   'Referer': 'http://hqq.tv/',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   #'Accept-Encoding':'gzip, deflate, br',
                   #'Content-Type': 'text/html; charset=utf-8'
                   }
        
        req = urllib2.Request(url,None,headers)
        try:
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
        except urllib2.URLError, e:
            VSlog(e.read())
            VSlog(e.reason)
            html = e.read()

        Host = 'https://hqq.watch/'

        data = ''
        code_crypt = re.search('(;eval\(function\(w,i,s,e\){.+?\)\);)\s*<', html, re.DOTALL)
        if code_crypt:
            data = unwise.unwise_process(code_crypt.group(1))
        else:
            VSlog('prb1')       
            
        if data:
            http_referer = ''
            _pass = ''
            
            iss = GetIp()
            vid = re.search('var vid *= *"([^"]+)";', data, re.DOTALL).group(1)
            at = re.search('var at *= *"([^"]+)";', data, re.DOTALL).group(1)
            r = re.search('var http_referer *= *"([^"]+)";', data, re.DOTALL)
            if r:
                http_referer = r.group(1)
            
            url2 = Host + "sec/player/embed_player.php?iss=" + iss + "&vid=" + vid + "&at=" + at + "&autoplayed=yes&referer=on&http_referer=" + http_referer + "&pass=" + _pass + "&embed_from=&need_captcha=0"
            #VSlog( url2 )
            
            req = urllib2.Request(url2,None,headers)
            
            try:
                response = urllib2.urlopen(req)
                data = response.read()
                response.close()
            except urllib2.URLError, e:
                VSlog(e.read())
                VSlog(e.reason)
                data = e.read()

            data = urllib.unquote(data)

            data = DecodeAllThePage(data)

            at = re.search(r'var\s*at\s*=\s*"([^"]*?)"', data)
            
            l = re.search(r'link_1: ([a-zA-Z]+), server_1: ([a-zA-Z]+)', data)
            
            vid_server = re.search(r'var ' + l.group(2) + ' = "([^"]+)"', data).group(1)
            vid_link = re.search(r'var ' + l.group(1) + ' = "([^"]+)"', data).group(1)
            
            #new video id, not really usefull
            m = re.search(r' vid: "([a-zA-Z0-9]+)"}', data)
            if m:
                id = m.group(1)
            
            if vid_server and vid_link and at:

                #get_data = {'server': vid_server.group(1), 'link': vid_link.group(1), 'at': at.group(1), 'adb': '0/','b':'1','vid':id} #,'iss':'MzEuMz'
                get_data = {'server_1': vid_server, 'link_1': vid_link, 'at': at.group(1), 'adb': '0/','b':'1','vid':id}

                headers['x-requested-with'] = 'XMLHttpRequest'

                req = urllib2.Request(Host + "/player/get_md5.php?" + urllib.urlencode(get_data),None,headers)
                try:
                    response = urllib2.urlopen(req)
                except urllib2.URLError, e:
                    VSlog(str(e.read()))
                    VSlog(str(e.reason))
                    
                data = response.read()
                VSlog(data)
                response.close()

                file_url = re.search(r'"file"\s*:\s*"([^"]*?)"', data)
               
                if file_url:
                    list_url = _decode2(file_url.group(1).replace('\\', ''))

                #Hack, je sais pas si ca va durer longtemps, mais indispensable sur certains fichiers
                list_url = list_url.replace("?socket", ".mp4.m3u8")
                
            else:
                VSlog('prb2')
                
        
        
        
        
       
        Header = 'User-Agent=' + UA
        list_url = list_url + '|' + Header
        

        name = 'videoraj'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,list_url,'')        
            
        return False, False

                
                   
       
        

#*******************************************************************************

def DecodeAllThePage(html):
    
    #html = urllib.unquote(html)
    
    Maxloop = 10
    
    #unescape
    while (Maxloop > 0):
        Maxloop = Maxloop - 1

        r = re.search(r'unescape\("([^"]+)"\)', html, re.DOTALL | re.UNICODE)
        if not r:
            break
        
        tmp = cUtil().unescape(r.group(1))
        html = html[:r.start()] + tmp + html[r.end():]
        
    #unwise
    while (Maxloop > 0):
        Maxloop = Maxloop - 1

        r = re.search(r'(;eval\(function\(w,i,s,e\){.+?\)\);)\s*<', html, re.DOTALL | re.UNICODE)
        if not r:
            break
        
        tmp = data = unwise.unwise_process(r.group(1))
        html = html[:r.start()] + tmp + html[r.end():]

    return html
import re



def unpackByString( sJavascript):
        aSplit = sJavascript.split(";',")
        p = str(aSplit[0])

        aSplit = aSplit[1].split(",")
        a = int(aSplit[0])
        c = int(aSplit[1])
        k = aSplit[2].split(".")[0].replace("'", '').split('|')
        e = ''
        d = ''
       
        sUnpacked = str(self.__unpack(p, a, c, k, e, d))
        return sUnpacked.replace('\\', '')

def __unpack( p, a, c, k, e, d):
        while (c > 1):
            c = c -1
            if (k[c]):               
                p = re.sub('\\b' + str(self.__itoa(c, a)) +'\\b', k[c], p)
        return p

def __itoa( num, radix):
        result = ""
        while num > 0:
            result = "0123456789abcdefghijklmnopqrstuvwxyz"[num % radix] + result
            num /= radix
        return result  
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

def flashxx(baseUrl):       
        
        HTTP_HEADER = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
                        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language':'pl,en-US;q=0.7,en;q=0.3',
                        'Accept-Encoding':'gzip, deflate',
                        'DNT':1,
                        'Connection':'keep-alive',
                      }
        COOKIE_FILE = GetCookieDir('flashxtv.cookie')
        params = {'header':HTTP_HEADER, 'cookiefile':COOKIE_FILE, 'use_cookie': True, 'save_cookie':True, 'return_data':True}
        
        def __parseErrorMSG(data):
            data = cm.ph.getAllItemsBeetwenMarkers(data, '<center>', '</center>', False, False)
            for item in data:
                if 'color="red"' in item or ('ile' in item and '<script' not in item):
                    SetIPTVPlayerLastHostError(clean_html(item))
                    break
        
        def __getJS(data, params):
          for inn in data: 
            tmpUrls = re.compile("""<script[^>]+?src=['"]([^'^"]+?)['"]""", re.IGNORECASE).findall(inn)
                                     
            for tmpUrl in tmpUrls:
                if tmpUrl.startswith('.'):
                    tmpUrl = tmpUrl[1:]
                if tmpUrl.startswith('//'):
                    tmpUrl = 'http:' + tmpUrl
                if tmpUrl.startswith('/'):
                    tmpUrl = 'http://www.flashx.tv' + tmpUrl
                if cm.isValidUrl(tmpUrl) and ('flashx' in tmpUrl and 'jquery' not in tmpUrl): 
                   
                    sts, tmp = cm.getPage(tmpUrl.replace('\n', ''), params)
            
            sts, tmp = cm.getPage('https://www.flashx.tv/js/code.js', params)
            tmp = cm.ph.getAllItemsBeetwenMarkers(tmp, 'function', ';');
            for tmpItem in tmp:
                tmpItem = tmpItem.replace(' ', '')
                if '!=null' in tmpItem:
                    tmpItem   = cm.ph.getDataBeetwenMarkers(tmpItem, 'get(', ')')[1]
                    tmpUrl    = cm.ph.getSearchGroups(tmpItem, """['"](https?://[^'^"]+?)['"]""")[0]
                    if not cm.isValidUrl(tmpUrl): continue
                    getParams = cm.ph.getDataBeetwenMarkers(tmpItem, '{', '}', False)[1]
                    getParams = getParams.replace(':', '=').replace(',', '&').replace('"', '').replace("'", '')
                    tmpUrl += '?' + getParams
                    sts, tmp = cm.getPage(tmpUrl, params)
                    break
        
        if baseUrl.split('?')[0].endswith('.jsp'):
            rm(COOKIE_FILE)
            sts, data = cm.getPage(baseUrl, params)
            if not sts: return False
            
            __parseErrorMSG(data)
            
            cookies = dict(re.compile(r'''cookie\(\s*['"]([^'^"]+?)['"]\s*\,\s*['"]([^'^"]+?)['"]''', re.IGNORECASE).findall(data))
            tmpParams = dict(params)
            tmpParams['cookie_items'] = cookies
            tmpParams['header']['Referer'] = baseUrl
            
            __getJS(data, tmpParams)
            
            data = cm.ph.getDataBeetwenReMarkers(data, re.compile('<form[^>]+?method="POST"', re.IGNORECASE),  re.compile('</form>', re.IGNORECASE), True)[1]
                        
            action = cm.ph.getSearchGroups(data, '''action=['"]([^'^"]+?)['"]''', ignoreCase=True)[0]
            post_data = dict(re.compile(r'<input[^>]*name="([^"]*)"[^>]*value="([^"]*)"[^>]*>', re.IGNORECASE).findall(data))
            try:
                tmp = dict(re.findall(r'<button[^>]*name="([^"]*)"[^>]*value="([^"]*)"[^>]*>', data))
                post_data.update(tmp)
            except Exception:
                printExc()
            
            try: GetIPTVSleep().Sleep(int(cm.ph.getSearchGroups(data, '>([0-9])</span> seconds<')[0])+1)
            except Exception as ex:
                print ex
            
            if {} == post_data:  post_data = None
            if not cm.isValidUrl(action) and url != '':
                action = urljoin(baseUrl, action)
            
            sts, data = cm.getPage(action, tmpParams, post_data)
            if not sts: return False
            
           
            __parseErrorMSG(data)
            
            # get JS player script code from confirmation page
            tmp = cm.ph.getAllItemsBeetwenMarkers(data, ">eval(", '</script>', False)
            for item in tmp:
                item = item.strip()
                if item.endswith(')))'): idx = 1
                else: idx = 0
                
                for decFun in [SAWLIVETV_decryptPlayerParams, KINGFILESNET_decryptPlayerParams]:
                    decItem = urllib.unquote(unpackJSPlayerParams(item, decFun, idx))
                   
                    data += decItem + ' '
                    if decItem != '': break
            
            urls = []
            tmp = re.compile('''\{[^}]*?src[^}]+?video/mp4[^}]+?\}''').findall(data )
            for item in tmp:
                label = cm.ph.getSearchGroups(item, '''['"]?label['"]?\s*:\s*['"]([^"^']+?)['"]''')[0]
                res = cm.ph.getSearchGroups(item, '''['"]?res['"]?\s*:\s*[^0-9]?([0-9]+?)[^0-9]''')[0]
                name = '%s - %s' % (res, label)
                url = cm.ph.getSearchGroups(item, '''['"]?src['"]?\s*:\s*['"]([^"^']+?)['"]''')[0]
                params = {'name':name, 'url':url}
                if params not in urls: urls.append(params)
            
            return urls
        
        if '.tv/embed-' not in baseUrl:
            baseUrl = baseUrl.replace('.tv/', '.tv/embed-')
        if not baseUrl.endswith('.html'):
            baseUrl += '.html'
            
        
        params['header']['Referer'] = baseUrl
        SWF_URL = 'http://static.flashx.tv/player6/jwplayer.flash.swf'
        
        id = cm.ph.getSearchGroups(baseUrl+'/', 'c=([A-Za-z0-9]{12})[^A-Za-z0-9]')[0]
        if id == '': id = cm.ph.getSearchGroups(baseUrl+'/', '[^A-Za-z0-9]([A-Za-z0-9]{12})[^A-Za-z0-9]')[0]
        baseUrl = 'http://www.flashx.tv/embed.php?c=' + id
        response= []
        rm(COOKIE_FILE)
        params['return_data'] = False
        referer=[('Referer',baseUrl)]
        redirectUrl =gegetUrl(baseUrl,headers=referer) 
 
                       
            
        id = cm.ph.getSearchGroups(redirectUrl+'/', 'c=([A-Za-z0-9]{12})[^A-Za-z0-9]')[0]
        if id == '': id = cm.ph.getSearchGroups(redirectUrl+'/', '[^A-Za-z0-9]([A-Za-z0-9]{12})[^A-Za-z0-9]')[0] 
        baseUrl = 'http://www.flashx.tv/embed.php?c=' + id
        
        params['return_data'] = True
        data = cm.getPage(baseUrl, params)
        params['header']['Referer'] = redirectUrl
        params['load_cookie'] = True
        
                
        play = ''
        vid = cm.ph.getSearchGroups(redirectUrl+'/', '[^A-Za-z0-9]([A-Za-z0-9]{12})[^A-Za-z0-9]')[0]
        for item in ['playvid', 'playthis', 'playit', 'playme', 'playvideo']:
            if item+'-' in data:
                play = item
                break
        
        
        
        __getJS(data, params)
        
        url = cm.ph.getSearchGroups(redirectUrl, """(https?://[^/]+?/)""")[0] + play + '-{0}.html?{1}'.format(vid, play)
        sts, data = cm.getPage(url, params)
        if not sts: return False
        
            
        if 'fxplay' not in url and 'fxplay' in data:
            url = cm.ph.getSearchGroups(data, '"(http[^"]+?fxplay[^"]+?)"')[0]
            sts, data = cm.getPage(url)
            if not sts: return False
        
        try:
           
            __parseErrorMSG(data)
            
            tmpTab = cm.ph.getAllItemsBeetwenMarkers(data, ">eval(", '</script>', False, False)
            for tmp in tmpTab:
                tmp2 = ''
                for type in [0, 1]:
                    for fun in [SAWLIVETV_decryptPlayerParams, VIDUPME_decryptPlayerParams]:
                        tmp2 = unpackJSPlayerParams(tmp, fun, type=type)
                        
                        data = tmp2 + data
                        if tmp2 != '': 
                            
                           break
                    if tmp2 != '': break
                        
        except Exception:
            printExc()
        
        retTab = []
        linksTab = re.compile("""["']*file["']*[ ]*?:[ ]*?["']([^"^']+?)['"]""").findall(data)
        linksTab.extend(re.compile("""["']*src["']*[ ]*?:[ ]*?["']([^"^']+?)['"]""").findall(data))
        linksTab = set(linksTab)
        for item in linksTab:
            if item.endswith('/trailer.mp4'): continue
            if cm.isValidUrl(item):
                if item.split('?')[0].endswith('.smil'):
                    # get stream link
                    sts, tmp = cm.getPage(item)
                    if sts:
                        base = cm.ph.getSearchGroups(tmp, 'base="([^"]+?)"')[0]
                        src = cm.ph.getSearchGroups(tmp, 'src="([^"]+?)"')[0]
                        #if ':' in src:
                        #    src = src.split(':')[1]   
                        if base.startswith('rtmp'):
                            retTab.append({'name':'rtmp', 'url': base + '/' + src + ' swfUrl=%s live=1 pageUrl=%s' % (SWF_URL, redirectUrl)})
                elif '.mp4' in item:
                    retTab.append({'name':'mp4', 'url': item})
        return retTab    