#-*- coding: utf-8 -*-
iconimage=None
from socket import timeout
from resources.lib.otvhelper import *
from resources.lib.otvhelper import showotvplayer
import json, base64
import CommonFunctions
from resources.sayfalar.saraydorf_tv import racacaxtvga
import json
from cookielib import CookieJar
from datetime import datetime, date, timedelta
common = CommonFunctions
#from resources.sayfalar.canlitv_mobi import webtvlist
import hashlib
import os.path
from xml.dom import minidom
from urlparse import parse_qs
import time

import re,unicodedata
from xiptvozel import iptvuser_info
import sys
from sonicstream_tv import sonicGenre,sshowBox4
HOST = 'XBMC'
SITE_IDENTIFIER = 'iptvbox'
SITE_NAME = '[COLOR orange]IPTV GERMANY[/COLOR]'
SITE_DESC = 'Regarder la télévision'
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvMjJ0NGJxbXJtdG55Zng3L290dmlwdHYubTN1P2RsPTA="
URL_WEB=base64.b64decode(yen)
addonPath = xbmcaddon.Addon().getAddonInfo("path")
addonversion =xbmcaddon.Addon().getAddonInfo("version")
addonArt = os.path.join(addonPath,'resources/images')
URL_FREE = 'https://annuel.framapad.org/p/vstream/export/txt'
ssUrl= 'http://www.wod-1.org:8000/get.php?username=201webtv&password=morra&type=m3u'
settings = xbmcaddon.Addon(id='plugin.video.OTV_MEDIA')
URL_LIBRETV = 'http://www.m3uliste.pw/'
IPTV_LINKS = 'http://www.m3uliste.pw/'
#URL_LIBRETV = 'http://libretv.me/Liste-m3u/Liste-anonymes/(PB)Redeneobux(USA).m3u'
KURD_TV=  "http://karwan.tv/"
Android_User_Agent = 'Peers.TV/6.10.2 Android/4.4.4 phone/Galaxy Tab E/arm64'
Player_User_Agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
cafile = 'cacert.pem'
mode =None
play=False
SPORT_SPORTS = (True, 'load')
#play = addon.queries.get('play', None)
ALMAN_TV= (True, 'load')
#url = addon.queries.get('playurl', None)

name=''
proxy_string=None
proxy_use_chunks=True
auth_string=''
streamtype='HDS'
setResolved=False
proxy=None
use_proxy_for_chunks=False
auth_string=None
streamtype='HDS'
setResolved=False
swf=""
_callback=None
callbackparam=""
iconImage=""
maxbitrate=0
simpleDownloader=False
play=True
def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString
def _downloadUrl(url1):
        
         req = urllib2.Request(url1, None, {'User-agent': 'Mozilla/5.0 TURKvod 4 Mozilla/5.0 nStreamVOD 0.1(Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3',
         'Connection': 'Close'})     
         url1=urllib2.urlopen(req).read()
         
         
	 return url1	
def _substitute_entity(match):
        ent = match.group(3)
        if match.group(1) == '#':
            # decoding by number
            if match.group(2) == '':
                # number is in decimal
                return unichr(int(ent))
            elif match.group(2) == 'x':
                # number is in hex
                return unichr(int('0x' + ent, 16))
        else:
            # they were using a name
            cp = n2cp.get(ent)
            if cp: return unichr(cp)
            else: return match.group()

def decode_html(data):
	try:
		if not type(data) == unicode:
			data = unicode(data, 'utf-8', errors='ignore')
		entity_re = re.compile(r'&(#?)(x?)(\w+);')
    		return entity_re.subn(_substitute_entity, data)[0]
	except:
		traceback.print_exc()
		#print [data]
		return data

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

def root():
        req = urllib2.Request(base64.b64decode("aHR0cDovL2hpdGl0LnRrL21haW4vdmlwLnBocD9maWx0ZXI9dmFy"), None, {'User-agent': 'Mozilla/5.0 seyirTURK_E2','Connection': 'Close'})
        return base64.b64decode(urllib2.urlopen(req).read())
userdata = xbmc.translatePath('special://userdata')
UA = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
icon = 'tv.png'        
sRootArt = cConfig().getRootArt()
def Readcookie(Domain):
        Name = os.path.join(PathCache,'Cookie_'+ str(Domain) +'.txt')
        
        try:
            file = open(Name,'r')
            data = file.read()
            file.close()
        except:
            return ''
        
        return data
def root():
        req = urllib2.Request(base64.b64decode("aHR0cDovL2hpdGl0LnRrL21haW4vZ2V0cm9vdC5waHA="), None, {'User-agent': 'Mozilla/5.0 seyirTURK_E2','Connection': 'Close'})
        return base64.b64decode(urllib2.urlopen(req).read())
def get_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 seyirTURK_KODI (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


Android_User_Agent = 'Peers.TV/6.10.2 Android/4.4.4 phone/Galaxy Tab E/arm64'
Player_User_Agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:35.0) Gecko/20100101 Firefox/35.0'


def get(url, headers=None, data=None):
    if data is None:
        data = {}
    if headers is None:
        headers = {}
    session = requests.session()
    headers["User-Agent"] = Player_User_Agent
    return session.get(url, data=data, headers=headers)


class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data

def iptvturk():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','genres.png')
    oGui.addDir(SITE_IDENTIFIER, 'sonicGenre', 'TURK IPTV LINK', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','genres.png')
    oGui.addDir(SITE_IDENTIFIER, 'iptvturke', 'TURK IPTV LINK 1', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','genres.png')
    oGui.addDir(SITE_IDENTIFIER, 'iptvturko', 'TURK IPTV LINK 2', 'genres.png', oOutputParameterHandler)
      
            
    oGui.setEndOfDirectory()
    
def iptvturke():
    oGui = cGui()
    scraper = cfscrape.create_scraper()
#    urla= "https://freeworldwideiptv.com/"
#    referer=[('Referer',urla)]
#    sUrl= "https://freeworldwideiptv.com/tag/free-turkey-m3u/"
    urla=scraper.get("http://iptvsatlinks.blogspot.de/search/label/Turkish").content  
    channels = re.findall("<h3 class='post-title entry-title' itemprop='name'>.*?<a href='(.*?)'>(.*?)</a>",urla, re.S)
    for Link,sTitle in channels:         
                                
                               
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'iptvturke2', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
def iptvturke2():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl= oInputParameterHandler.getValue('siteUrl')
    
                    
                                     
    urla= "http://iptvsatlinks.blogspot.de/"
    referer=[('Referer',urla)]                                      
    url=gegetUrl(sUrl,headers=referer)                                                      
    url=url.replace('\r',"").replace('\s',"").replace('\n',"")
    sHtmlContent = re.findall('<div class="code">(.*?)&nbsp;</div>', url, re.S)[0]
    channels = re.findall("/>#EXTINF:.*?,(TR.*?)<br />(.*?)<br", sHtmlContent, re.S)            
    for sTitle,Link in channels:         
                                
              
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'TSpanel', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
                                 
def TSpanel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    MAIN = oInputParameterHandler.getValue('siteUrl')                  
    liste = []                
    
    liste.append( ['Oynat',MAIN] )
    liste.append( ['Panele Gir',MAIN] )

               
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
      
        if sTitle == 'Panele Gir':
             oGui.addDir(SITE_IDENTIFIER, 'iptvuser_info',  sTitle, 'genres.png', oOutputParameterHandler)
       
        else:
             oGui.addDir(SITE_IDENTIFIER, 'showotsplayer',  sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def iptvturko():
    oGui = cGui()
    scraper = cfscrape.create_scraper()
#    urla= "https://freeworldwideiptv.com/"
#    referer=[('Referer',urla)]
#    sUrl= "https://freeworldwideiptv.com/tag/free-turkey-m3u/"
    urla=scraper.get("https://freeworldwideiptv.com/tag/free-turkey-m3u/").content  
    channels = re.findall('<h2 class="title">.*?<a href="(.*?)" title="(.*?)"',urla, re.S)
    for Link,sTitle in channels:         
                                
              
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'iptvturk2', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
def iptvturk2():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl= oInputParameterHandler.getValue('siteUrl')
    
    
                                     
    scraper = cfscrape.create_scraper()
    url=scraper.get(""+sUrl).content                                                       
    url=url.replace('\r',"").replace('\s',"").replace('\n',"").replace('http',"<k>http").replace('.ts',".ts</k>")
    sHtmlContent = re.findall('<pre class="alt2" dir="ltr" style="height:.*?">(.*?)</pre>', url, re.S)[0]
    channels = re.findall("#EXTINF:.*?,(.*?)<k>(.*?)</k>", sHtmlContent, re.S)            
    for sTitle,Link in channels:         
                                
              
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'showotsplayer', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()







def skygermany():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://urhd.tv/country/germany'
    urla= "http://urhd.tv/"
    referer=[('Referer',urla)]
             
    data=gegetUrl(sUrl,headers=referer)                                                                                     
    data=  data.replace('%3a',':').replace('?u=n1info#User-Agent=&quot;AppleCoreMedia',':TV')                     
    tarzlistesi = re.findall('<div class="Channel__poster">.*?<a href="(.*?)">.*?<img src="(.*?)".*?<div class="card-footer" title="(.*?)">', data, re.S)
    for sUrl,sPicture,sTitle in tarzlistesi:                                    
                                              
            
        sTitle =  alfabekodla(sTitle )
        TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        sUrl='http://urhd.tv%s/embed'%sUrl
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if '.m3u8'  in sUrl:
          oGui.addMovie(SITE_IDENTIFIER, 'showotvplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)    
        elif 'racacaxtv.ga'  in sUrl:
          oGui.addMovie(SITE_IDENTIFIER, 'webtvlist', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
          oGui.addMovie(SITE_IDENTIFIER, 'playskygermany', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def playskygermany():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    rUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    urla= "http://urhd.tv/"
    referer=[('Referer',urla)]                                      
    data=gegetUrl(rUrl,headers=referer) 
    sHosterUrl = re.findall("file: '(.*?)'", data, re.S)[0]
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    sHosterUrl = sHosterUrl+TIK
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 

def arnavutchan():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://albanian.tv/page/1/') 
    oGui.addDir(SITE_IDENTIFIER, 'arnavutchan33', 'TVshqip.tv', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8/tv/wp-content/uploads/2016/05/logo.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'tv.png')
    oGui.addDir(SITE_IDENTIFIER, 'arnavutchan3', 'TVmak.com', 'tv.png', oOutputParameterHandler)
    
        
    
    
    oGui.setEndOfDirectory()



def peerstv(): #affiche les genres
    oGui = cGui()
    Url='http://m.peers.tv/show/tvc/ranenoe_serdtse/102008119/?autoplay=1'
    sHtmlContent = getUrl(Url).result

   
    sHtmlContent = sHtmlContent.replace('\/',"/")                                  
    sPattern = '"title": "(.*?)".*?"stream": "(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture='http://s1.peers.tv/i/ptv/logo.png'
            TIK='|Referer=http://m.peers.tv/show/karusel/mi_mi_mishki/98451739/?autoplay=1&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
                         
                              
            Link = aEntry[1]+TIK
            Link = Link.replace('http://hls.peers.tv',"http://ger1.peers.tv")           
            sTitle =  alfabekodla(aEntry[0])
                                          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'otvplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 


def weebtv(): #affiche les genres
    oGui = cGui()
    sUrl = 'http://weeb.tv/api/getChannelList'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    sPattern = '"cid":"(.*?)","channel_name":".*?","channel_title":"(.*?)".*?,"channel_logo_url":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = str(aEntry[2])
            
            Link = aEntry[0]
            u =  aEntry[1]
           
            uu = u.decode('utf8')
            sTitle = uu.encode('cp1250')                              
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'play__weebtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def play__weebtv():
    oGui = cGui()
    url = 'http://weeb.tv/api/setPlayer'
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    channel = oInputParameterHandler.getValue('siteUrl')
    post = { 'platform': HOST, 'channel': channel }
    data = urllib.urlencode(post)
    headers = { 'User-Agent' : HOST }
    request = urllib2.Request(url,data, headers)
    response = urllib2.urlopen(request)
    data = response.read()
    data = data.replace('%2F', '/').replace('%3A', ':').replace('12=1', '12=2')
    streamDaten = re.findall('73=(.*?)&10=(.*?)&11=(.*?)&', data, re.S)
    if streamDaten:
        playPath, rtmp, File = streamDaten[0]
    sHosterUrl = '%s/%s live=1 pageUrl=token swfUrl=%s' % (rtmp, File, playPath)
       
    sTitle =  alfabekodla(sTitle)   
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
def arnavutchan2(): #affiche les genres
    oGui = cGui()
    
    
    liste = []
    liste.append( ["Tv Shqip Live","http://albanian.tv/"] ) 
    liste.append( ["SPORT","http://www.rexswain.com/cgi-bin/httpview.cgi?url=http://albanian.tv/supersport-2-live/&uag=Mozilla/5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/60.0.3112.90+Safari/537.36&ref=&aen=&req=GET&ver=1.1&fmt=AUTO"] ) 
    for sTitle,sUrl in liste:                       
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)  
        sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'arnavutchan33', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

def fflashx2(data):
        TIK='|User-Agent=User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

                  
        urll = re.findall("src: '(.*?)',type: 'video/mp4',label: '.*?'", data)[0]
        url= urll+TIK
           
        name = 'flashx.tv'
        addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok


def arnavutchan44(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    data = requests.get(url, headers = headers).text


                                                                                         
                              
    streamDaten = re.compile('<TT>&lt;di.*?class="featured-post�featured-post-.*?".*?<TT>&lt;a.*?ref="(.*?)".*?itle="(.*?)".*?<TT>&lt;img.*?data-layzr="(.*?)"').findall(data)
    
    for sUrl,  sTitle,sPicture in streamDaten:                          
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)  
       
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'sportsntvlive.com'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'sportsntvlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
           oGui.addMovie(SITE_IDENTIFIER, 'play__arnavutchan2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
    oGui.setEndOfDirectory()


def Almanlivestream(): #affiche les genres
    oGui = cGui()              
    tarzlistesi= []                
    tarzlistesi.append(("Sky_Deutschland", "http://tv.kostenloshdtv.com/10692", "https://upload.wikimedia.org/wikipedia/de/f/f4/Sky_Deutschland.png"))
                                 
    tarzlistesi.append(("Deutsche TV ", "http://tv.kostenloshdtv.com/10691", "http://www.kostenloshdtv.com/wp-content/uploads/2017/09/rtl-144x96.png"))
    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'play__almantv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()


def laklak(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku  
def play__almantv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(sTitle)
    referer=[('Referer',sUrl)]                                      
    url=gegetUrl(sUrl,headers=referer) 
#    linka = re.findall('file: webhdiptv."(.*?)"', datam, re.S)[0]            
    
#    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36' 
    
               
   # url  =linka +TIK    
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
            
#            url = 'https://yayin2.kuralbet25.com/hls/lig1.m3u8?st=xOoqxCRIYuZvLSYzcIw76Q&e=1507559184'
#            url = base64.b64encode(urll)
            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

def mplay__almantv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(sTitle)
    
    referer=[('Referer',sUrl)]                                      
    datam=gegetUrl(sUrl,headers=referer) 
    Linklaklak = re.findall('file: webhdiptv."(.*?)_(.*?)"', datam, re.S)
    for sHos ,sterUrl in Linklaklak:
    
        
       linkkm = laklak(sHos)
       linkam =laklak(sterUrl)
       linkk = base64.b64decode(linkkm+'==')                                                                                                            

       linka = base64.b64decode(linkam+'==')

                                   
       sterUrl = re.findall('http://(.*?.webhdiptv.com:85)/.*?', linka, re.S)[0]
       TIK='|Connection=keep-alive&Host='+sterUrl+'&Range=bytes=0-&Referer='+sUrl+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36' 
    
               
       url  =linka +'?'+linkk+TIK             
      
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

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok


def arnavutchan33(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.voirfilms.org/rechercher'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
         
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
  
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
        sHtmlContent= requests.get(url, headers = headers).text
        sHtmlContent = sHtmlContent.replace('\/',"/")
        
                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="home-thumb">.*?<a href="(.*?)" title="(.*?)".*?<img.*?srcset="(.*?)200w,.*?"'
    
    
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = aEntry[1]
            sTitle =  alfabekodla(sTitle) 
            sPicture = str(aEntry[2])
            
                
            sUrl = str(aEntry[0])
            
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'play__arnavutchan2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'arnavutchan33', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

                                               
def __NextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = "<span class='page-numbers current'>.*?</span>.*?<a class='page-numbers' href='(.*?)'"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(aResult[1][0]) 


def sportsntvlive():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    Url =  alfabekodla(Url)
    
    
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
          
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    dat=requests.get(Url).content
   
    ken = re.findall('<p><center><iframe src="(.*?)"',dat, re.S)[0]
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"                        
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    datan= requests.get(ken).content
    rUrl = re.findall('<center><iframe src="(http://sportstvstream.me/frames/.*?)"', datan, re.S)[0]
    TIK='|Referer=http://sportstvstream.me/&User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    datam= requests.get(rUrl).content
    HosterUrl = re.findall('fid="(.*?)".*?type="text/javascript" src="(.*?)"', datam, re.S)[0]
    for fid,js in HosterUrl:          
                                                                        
         datani= requests.get(js).content
         Hoster = re.findall('src=(.*?)channel', datani, re.S)[0]
         sterUrl = "%schannel=%s&vw=640&vh=400"%s (Hoster,js)
         HosterUrl = re.findall('<source src="(.*?)"></video>.*?streamrootKey: "(.*?)"', sterUrl, re.S)
         for m3u8,key in HosterUrl:
            sHosterUrl = m3u8+'?key='+key+TIK                       
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oOutputParameterHandler.addParameter('siteUrl', str(sHosterUrl))
            oGui.addMovie(SITE_IDENTIFIER, 'showotvplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()



def play__arnavutchan2():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                                
    dat= requests.get(Url).content
    
                            
    url = re.findall('<p><iframe src="(.*?)"',dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
    data= requests.get(url, headers = headers).text
    arl ="https://live.albanian.tv/token.php"  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer':url  }
    date= requests.get(arl, headers = headers).text
    token = re.findall('file:stream_url+"(.*?)"',date, re.S)[0]                         
    sHosterUrl = re.findall('var stream_url = "(.*?)"', data, re.S)[0]
    TIK='|Referer='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'
    sHosterUrl = sHosterUrl+''+token+TIK
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    
def arnavutchan3(): #affiche les genres
    oGui = cGui()
    sUrl = 'http://tvmak.com/'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    sPattern = "value: \"(.*?)\",img: '(.*?)', url: '(.*?)'"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = str(aEntry[1])
            
            Link = aEntry[2]
            sTitle =  alfabekodla(aEntry[0])
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'play__arnavutchan', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def play__arnavutchan():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    rUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
         
    
    
    
    urla= "http://tvmak.com/"
    referer=[('Referer',urla)]
    data=gegetUrl(rUrl,headers=referer) 
    sHosterUrl = re.findall('<source type="application/x-mpegurl" src="(.*?)">', data, re.S)[0]
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    sHosterUrl = sHosterUrl+TIK
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
def showBox():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    playlist = parseM3U(sUrl)

    for track in playlist:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', str(track.path))
        oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
        oGui.addDir(SITE_IDENTIFIER, 'showotsplayer', track.title, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()
def mshowWeb():
    oGui = cGui()

  
    sUrl = URL_WEB

    playlist = parseWebM3U(sUrl)
    
    if not playlist:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addText(SITE_IDENTIFIER, "[COLOR red] Probleme de lecture avec la playlist[/COLOR] ", oOutputParameterHandler)
        
    else:
        for track in playlist:
            sThumb = track.icon
            if not sThumb:
                sThumb = 'tv.png'
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(track.path))
            oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sRootArt + '/tv/' + sThumb))
            if 'web.tv'  in track.path:
               oGui.addDirectTV(SITE_IDENTIFIER, 'webtvlist', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    
            elif 'racacaxtv.ga'  in track.path:
               oGui.addDirectTV(SITE_IDENTIFIER, 'webtvlist', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    

            else:
               oGui.addDirectTV(SITE_IDENTIFIER, 'user_info', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    
            
    oGui.setEndOfDirectory()
def showWeb():
    oGui = cGui()
    urla= "http://www.m3uliste.pw/"
    referer=[('Referer',urla)]
    sUrl= "http://www.m3uliste.pw/"
    urla=gegetUrl(sUrl,headers=referer) 
    channels = re.findall('<div class="zs-accordio.*?" name="(.*?)" onclick="fnChangeTab.*?">(.*?)<em></em></div>',urla, re.S)
    for Link,sTitle in channels:         
                                
            
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'showWeb2', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()
def showWeb2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    tab= oInputParameterHandler.getValue('siteUrl')
    
    
    urla= "http://www.m3uliste.pw/"
    referer=[('Referer',urla)]
    sUrl= "http://www.m3uliste.pw/"
    sHtmlContent=gegetUrl(sUrl,headers=referer)                                                         
    sHtmlContent=sHtmlContent.replace('&amp;','&')
    oParser = cParser()
    sPattern = '<div class="zs-accordio.*?" name="'+tab+'" onclick="fnChangeTab.*?">(.*?)<div class="'
                
    sult = oParser.parse(sHtmlContent, sPattern)
               
                
    sPattern = '>(http:\/\/(.*?)\/.*?get.php.*?)<'
                 
    aResult = oParser.parse(sult, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break    
            
            sThumbnail="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5GTXqTr_gcagwIAgEzzwl8QkpxoI-0DEbQ0gRkQc1vQb0sdlF"
            sTitle  = re.findall('username=(.*?)&', aEntry[0], re.S)
            sTitle = alfabekodla(sTitle[0] )
            surl =''+ aEntry[0]
            surl=surl.replace('&amp;','&')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(surl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'user_info', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def iptvgermany():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'https://github.com/pixbox-hdf/HDFreaks/blob/master/IPTV/userbouquet.iptv_germany.tv'
    urla= "https://github.com/"
    referer=[('Referer',urla)]
    
    data=gegetUrl(sUrl,headers=referer)                                                                                     
    data=  data.replace('%3a',':').replace('?u=n1info#User-Agent=&quot;AppleCoreMedia',':TV')                     
    tarzlistesi = re.findall('<td id="LC.*?>#SERVICE.*?(rtmp|http[^"]+):.*?<td id="LC.*?>#DESCRIPTION(.*?)</td>', data, re.S)
    for sUrl,sTitle in tarzlistesi:                                    
        
        sPicture="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5GTXqTr_gcagwIAgEzzwl8QkpxoI-0DEbQ0gRkQc1vQb0sdlF"
    
        sTitle =  alfabekodla(sTitle )
        TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
        sUrl=sUrl+TIK
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if '.m3u8'  in sUrl:
          oGui.addMovie(SITE_IDENTIFIER, 'showotvplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)    
        elif 'racacaxtv.ga'  in sUrl:
          oGui.addMovie(SITE_IDENTIFIER, 'webtvlist', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
          oGui.addMovie(SITE_IDENTIFIER, 'showotsplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def liveonlinetv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sOrder = oInputParameterHandler.getValue('sOrder')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    sPattern = '<li><a href="(/watch.*?)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            sTitle = aEntry[1]
            surl ='http://www.liveonlinetv247.info'+ aEntry[0]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDirectTV(SITE_IDENTIFIER, 'play__liveonlinetv24', sDisplayTitle, 'libretv.png' , '', oOutputParameterHandler)    
        
        cConfig().finishDialog(dialog)
        
        oGui.setEndOfDirectory()

def kurdtv():
    oGui = cGui()
    sUrl = 'http://karwan.tv/'
    data = getUrl(sUrl).result
    data =data.replace('\n','')
    tarzlistesi = re.findall('<a target="_parent".*?class="bt-image-link".*?title="(.*?)" href="(.*?)">.*?<img class= "hovereffect" width=".*?" height=".*?" src="(.*?)"', data, re.S)
    for sTitle,sUrl,sPicture in tarzlistesi:
        ssUrl = 'http://karwan.tv'+ sUrl
       
        sTitle =  alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', ssUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

        oGui.addMovie(SITE_IDENTIFIER, 'play__kurdtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
    oGui.setEndOfDirectory()
def play__liveonlinetv24():
    net = Net()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
   
    
    datam = requests.get(url).content
    tream = re.findall('>Live Sports Schedule</a></p><p><a href="(.*?)"><img src="http://www.liveonlinetv247.info/images/play.png"', datam, re.S)[0]
    tream = tream.replace('www.liveonlinetv247.info/','www.liveonlinetv247.info/embed/')
    data= requests.get(tream).content
    Url= re.findall('<source type="application/x-mpegurl" src="(.*?)">', data, re.S)[0]
    
    sHosterUrl =Url + '|User-Agent=%s' % Player_User_Agent

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        
                    
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  


def play__kurdtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    rUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    

    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    
    data= requests.get(rUrl).content
    tream = re.findall('<div class="art-article"><iframe.*?src="(.*?)"', data, re.S)[0]
    urlk= "http://karwan.tv/%s" % (tream)
    datam= requests.get(urlk).content 
    Url = re.findall("hls: '(.*?)'", datam, re.S)[0]
    sHosterUrl  = Url + TIK
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    
def alaskawatch():
    oGui = cGui()

   	                                              
    liz=xbmcgui.ListItem('M3u8/Lists',thumbnailImage= "https://dl.dropboxusercontent.com/u/272613616/IPTV/beceriksizlerlogo_yeni_version2.png",iconImage="DefaultFolder.png")   
    uurl="plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cshani%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url=https%3a%2f%2fraw.githubusercontent.com%2fzombiB%2fReplay%2fmaster%2fzombiList.xml"
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)

    oGui.setEndOfDirectory()
    
def showWebbbib():
    oGui = cGui()

   		#name,url,mode,icon
    liz=xbmcgui.ListItem('M3u8/Lists',thumbnailImage= "https://dl.dropboxusercontent.com/u/272613616/IPTV/beceriksizlerlogo_yeni_version2.png",iconImage="DefaultFolder.png")
    uurl="plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cshani%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url=https%3a%2f%2fdl.dropboxusercontent.com%2fu%2f272613616%2fkodi-xbmc.xml"
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)

    oGui.setEndOfDirectory()
    
def showWebbbi():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    playlist = parseWebM3U(sUrl)
    
    if not playlist:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addText(SITE_IDENTIFIER, "[COLOR red] Probleme de lecture avec la playlist[/COLOR] ", oOutputParameterHandler)
        
    else:
        for track in playlist:
            sThumb = track.icon
            if not sThumb:
                sThumb = 'tv.png'
            TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(track.path))
            oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sRootArt + '/tv/' + sThumb))
            oGui.addDirectTV(SITE_IDENTIFIER, 'showotsplayer', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    
  
    oGui.setEndOfDirectory()
                                          
  
def showLibreMenu():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sOrder', '2')
    oGui.addDir(SITE_IDENTIFIER, 'showLibre', 'Aujourd\'hui', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sOrder', '1')
    oGui.addDir(SITE_IDENTIFIER, 'showLibre', 'Ce mois-ci', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sOrder', '0')
    oGui.addDir(SITE_IDENTIFIER, 'showLibre', 'Anterieur', 'libretv.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def showshowWeb():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    playlist = parseWebM3U(sUrl)
    
    if not playlist:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://')
        oGui.addText(SITE_IDENTIFIER, "[COLOR red] Probleme de lecture avec la playlist[/COLOR] ", oOutputParameterHandler)
        
    else:
        for track in playlist:
            sThumb = track.icon
            if not sThumb:
                sThumb = 'tv.png'
            TIK='&amp;streamtype=TSDOWNLOADER|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(track.path))
            oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sRootArt + '/tv/' + sThumb))
            oGui.addDirectTV(SITE_IDENTIFIER, 'showotsplayer', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    
  
    oGui.setEndOfDirectory()
def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
    
def iptvultra():
    oGui = cGui()
    
    
        
    url = "http://www.iptvultra.com" 
    urla = net.http_GET(url).content
    
    channels = re.findall('class="rctitles2".+?href="(.+?)">(.+?)</a>',urla, re.S)
    for Link,sTitle in channels:         
              
              
              
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'iptvultra2', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()                                       
def iptvultra2():
       oGui = cGui()
      
       oInputParameterHandler = cInputParameterHandler()
       Title = oInputParameterHandler.getValue('sMovieTitle')
       urll = oInputParameterHandler.getValue('siteUrl')    
              
       url = adfly.unshorten(''+urll)
       url= url[0] 
                   
                    
            
       url= net.http_GET(url).content
       import time
       time.sleep(5)   
       
       
       channels = re.findall('".+?\[@\](.+?)\[@\].+?\[@\].+?\[@\](.+?)"', url, re.S)
       for sTitle  ,Link in channels:         
              sTitle =decode_html(sTitle) 
              sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
              sTitle = sTitle.encode( "utf-8")
              sTitle = urllib.unquote_plus(sTitle)
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'showotsplayer', sTitle, 'genres.png', oOutputParameterHandler)
        
                                                    
                                    

       oGui.setEndOfDirectory()

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
    
def showLibretv():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    playlist = parseLibretvM3U(sUrl)

    for track in playlist:
        
        sTitle = track.title
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)    
        try: 
            sTitle = urllib.unquote_plus(sTitle)
        except:

            sTitle = 'none'
            
        sthumb = str(track.icon)
        if len(sthumb) > 0:
            sthumb = 'http://libretv.me/icon/' + sthumb
        else:
            sthumb = 'http://libretv.me/icon/libretv.png'
        
        sData = str(track.data)
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', str(track.path))
        oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
        oOutputParameterHandler.addParameter('sThumbnail', sthumb)
        
        #garbage
        if 'http://touski' in track.path or re.search('[0-9]\.[0-9]\.[0-9].[0-9]', track.path):
            oGui.addText(SITE_IDENTIFIER, sTitle, oOutputParameterHandler)
        #real stream
        elif 'rtmp' in track.path or 'm3u8' in track.path:
            oGui.addDirectTV(SITE_IDENTIFIER, 'play__', sTitle, sthumb, sthumb, oOutputParameterHandler)
        #folder
        elif '.m3u' in track.path : 
            oGui.addDirectTV(SITE_IDENTIFIER, 'showLibretv', sTitle, sthumb, sthumb, oOutputParameterHandler)  
        #unknow link, loaded as normal stream
        else:
            oGui.addDirectTV(SITE_IDENTIFIER, 'SPORT_SPORTS', sTitle, sthumb, sthumb, oOutputParameterHandler)
  
    oGui.setEndOfDirectory()

# import code https://github.com/dvndrsn/M3uParser #
# David Anderson code thanck's for good job #

def parseWebM3U(infile):
    inf = urllib.urlopen(infile)

    line = inf.readline()

    if not line.startswith('#EXTM3U'):
       return

    playlist=[]
    song=track(None,None,None,None)

    for line in inf:
        line=line.strip()
        if line.startswith('#EXTINF:'):
            length,title=line.split('#EXTINF:')[1].split(',',1)
            try:
                licon = line.split('#EXTINF:')[1].partition('tvg-logo=')[2]
                icon = licon.split('"')[1]
            except:
                icon = "tv.png"
            song=track(length,title,None,icon)
        elif (len(line) != 0):
            if not (line.startswith('!') or line.startswith('#')):
                song.path=line
                playlist.append(song)
                song=track(None,None,None,None)

    inf.close()
    
    return playlist

def parseM3U(infile):
    inf = open(infile,'r')

    line = inf.readline()
    if not line.startswith('#EXTM3U'):
       return

    playlist=[]
    song=track(None,None,None,None)

    for line in inf:
        line=line.strip()
        if line.startswith('#EXTINF:'):
            length,title=line.split('#EXTINF:')[1].split(',',1)
            song=track(length,title,None,None)
        elif (len(line) != 0):
            if not line.startswith('!'):
                song.path=line
                playlist.append(song)
                song=track(None,None,None,None)

    inf.close()

    return playlist


#http://libretv.me/Liste-m3u/Liste-anonymes/(PB)Marchannel.m3u 
def parseLibretvM3U(infile):
    
    #print infile
    
    #version normale
    inf = urllib.urlopen(infile)
    
    #version qui memorise les m3u
    #file = GetLibreTVFile(infile)
    #inf = open(file, "r")
    
    line = inf.readline()

    playlist=[]
    
    #if not (line.startswith('#EXTM3U') or line.startswith('#EXTINF:')):
    #    return playlist
    
    song=track(None,None,None,None)
    
    ValidEntry = False
 
    for line in inf:
        line=line.strip()
        if line.startswith('#EXTINF:'):
            
            m = re.search(',([^,]+?)$', line)
            if m:
                title = m.groups(1)[0]
                length = 0
            
                ValidEntry = True
                
                m = re.search('tvg-logo="(.+?)"', line)
                if m:
                    logo = m.groups(1)[0]
                else:
                    logo = ''
                    
                m = re.search('group-title="(.+?)"', line)
                if m:
                    data = m.groups(1)[0]
                else:
                    data = None
                
                song=track(length,title,None,logo,data)
        elif (len(line) != 0):
            if (not line.startswith('#') and ValidEntry):
                ValidEntry = False
                song.path=line
                playlist.append(song)
                song=track(None,None,None,None)

    inf.close()
    return playlist

    
def GetRealUrl(url):
    oParser = cParser()
    sPattern = '\[REGEX\](.+?)\[URL\](.+$)'
    aResult = oParser.parse(url, sPattern)
    
    if (aResult):
        reg = aResult[1][0][0]
        url2 = aResult[1][0][1]
        oRequestHandler = cRequestHandler(url2)
        sHtmlContent = oRequestHandler.request()
        
        aResult = oParser.parse(sHtmlContent, reg)
        if (aResult):
            url = aResult[1][0]
            
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
        
    return url
    
 
    
def otvplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
          
        
   
    
def GetRealUrl(url):
    oParser = cParser()
    sPattern = '\[REGEX\](.+?)\[URL\](.+$)'
    aResult = oParser.parse(url, sPattern)
    
    if (aResult):
        reg = aResult[1][0][0]
        url2 = aResult[1][0][1]
        oRequestHandler = cRequestHandler(url2)
        sHtmlContent = oRequestHandler.request()
        
        aResult = oParser.parse(sHtmlContent, reg)
        if (aResult):
            url = aResult[1][0]
            
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
        
    return url
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
    

def openwindows():
    xbmc.executebuiltin( "ActivateWindow(%d, return)" % ( 10601, ) )
    return
    
def GetLibreTVFile(Webfile):
    
    PathCache = cConfig().getSettingCache()
    Name = os.path.join(PathCache,'LibreTV'+ time.strftime("%d%m") +'.m3u')

    try:
        #ckeck if file exist
        file = open(Name,'r')
        file.close()
    except:
        #delete old file
        files = os.listdir(PathCache)
        for file in files:
            if 'LibreTV' in file:
                os.remove(os.path.join(PathCache,file))
                
        #download new file
        inf = urllib.urlopen(Webfile)
        line = inf.read()
        
        #save it
        file = open(Name,'w')
        file.write(line)
        
        #clear
        file.close()
        inf.close()

    return Name



def saraydorf():
    
 #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    oParser = cParser()
    
    
    sPattern = '"Baslik":"(.*?)","Logo":".*?","Resim":"(.*?)","Playlist":"(.*?)"'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    print aResult 
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = str(aEntry[1])
            
            Link = aEntry[2]
            sTitle =  alfabekodla(sTitle)
            sTitle = aEntry[0].decode("latin-1").encode("utf-8")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'CanLiTV3', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()   

def user_info(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    ssUrl= IPTVdep(sUrl)
    
  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': ssUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    sHtmlContent = requests.get(ssUrl, headers = headers).text

               
    sPattern = '{"category_id":"(.*?)","category_name":"(.*?)","parent_id":.*?}'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            
            Link = aEntry[0]
            sTitle =  alfabekodla(sTitle)
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('ssUrl', ssUrl)
            oOutputParameterHandler.addParameter('siteUrl', Link)
           
            oGui.addDir(SITE_IDENTIFIER, 'user_info3', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def user_info3(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    ssUrl = oInputParameterHandler.getValue('ssUrl')
    
    referer=[('Referer',ssUrl)]
    data=gegetUrl(ssUrl,headers=referer) 
    sHosterUrl = re.findall('"username":"(.*?)","password":"(.*?)".*?"server_info":{"url":"(.*?)","port":"(.*?)"', data, re.S)
    (username,password,url,port) =sHosterUrl[0]

   
    


    oRequestHandler = cRequestHandler(ssUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '"category_id":"%s"'%sUrl+',"series_no".*?"tv_archive_duration":0},"(.*?)":{"num":.*?,"name":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = str(aEntry[1])
            
            
              
            Urll = 'http://%s:%s/live/%s/%s/%s.ts' % (url,port,username,password,aEntry[0])
            if Urll == None:
              callback(Urll)
            
            
            sTitle =  alfabekodla(sTitle)
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Urll)
            oGui.addDir(SITE_IDENTIFIER, 'showotsplayer', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
#Urll = 'http://%s:%s/live/%s/%s/%s.ts' % (url,port,username,password,aEntry[0])
def sshowBox3mmm():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
   
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  