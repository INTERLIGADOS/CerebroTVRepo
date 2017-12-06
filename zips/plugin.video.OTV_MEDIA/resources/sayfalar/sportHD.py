#-*- coding: utf-8 -*-

#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
import json, base64
import CommonFunctions

import json
from datetime import datetime, date, timedelta
common = CommonFunctions

import hashlib
import os.path
from xml.dom import minidom
from urlparse import parse_qs
HOST = 'XBMC'
SITE_IDENTIFIER = 'sportHD'
SITE_NAME = '[COLOR orange]sportHD[/COLOR]'
SPORT_SPORTS = (True, 'arnavutchan2')
yen= "aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvMjJ0NGJxbXJtdG55Zng3L290dmlwdHYubTN1P2RsPTA="
URL_WEB=base64.b64decode(yen)
addonPath = xbmcaddon.Addon().getAddonInfo("path")
addonversion =xbmcaddon.Addon().getAddonInfo("version")
addonArt = os.path.join(addonPath,'resources/images')
URL_FREE = 'https://annuel.framapad.org/p/vstream/export/txt'
mURL_WEB = 'http://1.panel3.us/get.php?username=alikomur&password=komur&type=m3u'
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

#play = addon.queries.get('play', None)

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
callbackpath=""
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

def playF4mLink(url,name,proxy=None,use_proxy_for_chunks=False,auth_string=None,streamtype='HDS',setResolved=False,swf="", callbackpath="", callbackparam="",iconImage=""):
    
    from lib.F4mProxy  import f4mProxyHelper 
    player=f4mProxyHelper()
    #progress = xbmcgui.DialogProgress()
    #progress.create('Starting local proxy')

    if setResolved:
        urltoplay,item=player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved,swf,callbackpath, callbackparam,iconImage)
        item.setProperty("IsPlayable", "true")
#        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

    else:
#        xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
        player.playF4mLink(url, name, proxy, use_proxy_for_chunks,maxbitrate,simpleDownloader,auth_string,streamtype,setResolved,swf,callbackpath, callbackparam,iconImage)
    
    return   


class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data

def load():
    linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_WEB)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'TV + sports', 'tv.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory()

def arnavutchan():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/') 
    oGui.addDir(SITE_IDENTIFIER, 'arnavutchan2', 'TVshqip.tv', 'https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'tv.png')
    oGui.addDir(SITE_IDENTIFIER, 'arnavutchan3', 'TVmak.com', 'tv.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def futbolozet(): #affiche les genres
    oGui = cGui()
    url ="https://dl.dropboxusercontent.com/s/km2w2t4cqsgyqgb/AlbanianTvLive.html?dl=0"
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

    headers = {"Referer":"wss://vs52.tawk.to/s/?k=5899c4b9110e7c7f9f3de765&u=bbcr6zagdNiPRctSW%2FFYb%2FZsm1bdyDu8Gfzmb56oMzrEqeB8vlXTGn83v079fGjR&uv=2&a=587798b5620a011eeac60c7b&cver=0&pop=false&w=gkiUy8&jv=537&asver=184&ust=false&p=Tv%20Shqip%20Live%20-%20Big%20Brother%20Albania%209%20Live%20-%20Albanian%20Tv%20-%20Part%202&r=https%3A%2F%2Ftvshqip.tv%2F&EIO=3&transport=websocket&sid=-Q4-Lw7Xr6Km3BIZFQO2&__t=LeOg7SK","User-Agent":UA}

    dat= 'http://www.goalsarena.org/en/'
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    data= requests.get(dat ).content
                  
                                
    streamDaten = re.compile('<span class="flags sprite-.*?"><a href="(.*?)"><im.*?alt="(.*?)"').findall(data)
    
    for sUrl,  sTitle in streamDaten:                          
        sTitle = sTitle.replace('Spor Toto',"Turkish")
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)  
        sPicture='http://goalsarena.goalsarena.netdna-cdn.com/templates/gk_sportmaxum/xlogo.png.pagespeed.ic.F0IzaQsJmf.webp'    
        
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'sportsntvlive.com'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'sportsntvlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
           oGui.addMovie(SITE_IDENTIFIER, 'showfutbolozet', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showfutbolozet(sSearch = ''):
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
        sPattern = '<div style="float: left;">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
         
        
        sPattern = '<div class="vtitle"><div><a href="(.*?)">(.*?)</a></div></div></li><li><div class="vscreen"><a href=".*?"><img style="cursor:pointer;" class="videothumbss" onclick=".*?" src="(.*?)"'
    
    
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
           
            sTitle = alfabekodla(aEntry[1])
            sPicture = str(aEntry[2])
                            
            sUrl = str(aEntry[0])
                      
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'play_showfutbolozet', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showfutbolozet', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()   
def __checkForNextPage(sHtmlContent):
    sPattern = '<div class="listnavigation">.*?div style="float:right; width:10%;"><a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        sUrl = sUrl.replace('&amp;',"&")
        return sUrl

    return False
def play_showfutbolozet():
    net = Net()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
   
    
    data = requests.get(url).content
    ua='Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'
    link=re.findall('data-config="(.*?)"',data)[0]
    url='http:' + link
    source=requests.get(url,headers={'User-Agent':ua,'Referer':'[makelist.param3]','Accept':'/*','Connection':'keep-alive'}).text
    f4m=re.findall('"f4m":".+?\/\/(.*?)"',source)[0]
    url='http://' + f4m
    source=requests.get(url,headers={'User-Agent':ua,'Referer':'[makelist.param3]','Accept':'/*','Connection':'keep-alive'}).text
    sHosterUrl ='http://' + re.findall('url=".+\/\/(.*?)"',source)[0]    
   

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        
                    
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False
def peerstv(): #affiche les genres
    oGui = cGui()
    sUrl = 'http://peers.tv/'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    sPattern = '"url": ".*?","title": "(.*?)","href": "/program/.*?","position":.*?"wide":.*?,"magnet": false,"stream": "(.*?)"'
    
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
            TIK='|Referer=http://peers.tv/&User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
                              
            Link = aEntry[1]+TIK
            Link = Link.replace('http://hls.peers.tv/',"http://ger1.peers.tv/")
            sTitle =  alfabekodla(aEntry[0])
                    
                     
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showotvplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
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
    dat ="https://dl.dropboxusercontent.com/s/z3y1fixrn1l2w7z/AlbanianTvLive.html"
    headers = {"Referer":"wss://vs52.tawk.to/s/?k=5899c4b9110e7c7f9f3de765&u=bbcr6zagdNiPRctSW%2FFYb%2FZsm1bdyDu8Gfzmb56oMzrEqeB8vlXTGn83v079fGjR&uv=2&a=587798b5620a011eeac60c7b&cver=0&pop=false&w=gkiUy8&jv=537&asver=184&ust=false&p=Tv%20Shqip%20Live%20-%20Big%20Brother%20Albania%209%20Live%20-%20Albanian%20Tv%20-%20Part%202&r=https%3A%2F%2Ftvshqip.tv%2F&EIO=3&transport=websocket&sid=-Q4-Lw7Xr6Km3BIZFQO2&__t=LeOg7SK","User-Agent":UA}

    
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    data= requests.get(dat ).content
                  
                                
    streamDaten = re.compile('<p><a href="(.*?)".*?</span>(.*?)</a>').findall(data)
    
    for sUrl,  sTitle in streamDaten:                          
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)  
        sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'tivibu-spor'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'tivibuspor', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'sunhd'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'sportsntvlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'miplayer'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'sportsntvlive2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:                             
           oGui.addMovie(SITE_IDENTIFIER, 'play__arnavutchan2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
def sportsntvlive2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    url =  alfabekodla(Url)
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    source = requests.get(url, headers = headers).text
    
    sHosterUrl = re.findall('file: "(.*?)"',source, re.S)[0]
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False 


def play__arnavutchan2():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    Url =  alfabekodla(Url)
    
   
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    arl ="https://tvshqip.tv/playerToken.php?dynamic=true"  
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    dat=requests.get(arl).content
 
    token = re.findall('token=(.*?)"',dat, re.S)[0]
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"                        
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    data= requests.get(Url).content
    sHosterUrl = re.findall("var strm='(.*?)'", data, re.S)[0]
    TIK='|Referer=https://tvshqip.tv/&User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    sHosterUrl = sHosterUrl+'?token='+token+TIK
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
    oOutputParameterHandler.addParameter('siteUrl', str(sHosterUrl))
    oGui.addMovie(SITE_IDENTIFIER, 'showotvplayer', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()
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
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox1', track.title, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()
def showWeb():
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
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(track.path))
            oOutputParameterHandler.addParameter('sMovieTitle', str(track.title))
            oOutputParameterHandler.addParameter('sThumbnail', str(sRootArt + '/tv/' + sThumb))
            oGui.addDirectTV(SITE_IDENTIFIER, 'showshowWeb', track.title, 'tv.png' , sRootArt+'/tv/'+sThumb, oOutputParameterHandler)    
            
    oGui.setEndOfDirectory()
def iptvlinks():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    urla= "http://www.m3uliste.pw/"
    referer=[('Referer',urla)]
    data=gegetUrl(sUrl,headers=referer) 
    data=data.replace('center;','IPTV LINK').replace('&amp;','&').replace('<div style=""><p style="text-align: IPTV LINK"><b style="color: rgb(255,0,0);"','')
    tarzlistesi = re.findall('<p style="text-align: (.*?)"><font color="#e89e2d">(.*?)</font>', data, re.S)
    for sTitle,sUrl in tarzlistesi:
        sUrl =  sUrl.replace('&amp;','&')
        sPicture="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR5GTXqTr_gcagwIAgEzzwl8QkpxoI-0DEbQ0gRkQc1vQb0sdlF"
        sTitle =  alfabekodla(sTitle)
       
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'showWebbbi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
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
    
    
    
    urla= "http://karwan.tv/"
    referer=[('Referer',urla)]
    datam=gegetUrl(rUrl,headers=referer) 
    tream = re.findall('<div class="art-article".*?<iframe.*?src="(.*?)"', datam, re.S)[0]
    urlk= "http://karwan.tv%s" % (tream)
    urla= "http://karwan.tv/"
    referer=[('Referer',urla)]
    data=gegetUrl(urlk,headers=referer) 
    sHosterUrl = re.findall('file: "(.*?)"', data, re.S)[0]
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
def sshowBox1():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(name )
    url = 'plugin://plugin.video.OTV_MEDIAM/?url='+urllib.quote_plus(url)+'&streamtype=TSDOWNLOADER&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')
    from default import *
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
    
def iptvultra():
    oGui = cGui()
    
    
        
    url2 = "http://www.iptvultra.com" 
    url = _downloadUrl(url2)
    
    channels = re.findall('class="rctitles2".+?href="(.+?)">(.+?)</a>', url, re.S)
    for Link,sTitle in channels:         
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'iptvultra2', sTitle, 'genres.png', oOutputParameterHandler)
        
    oGui.setEndOfDirectory()                                       
def iptvultra2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')    
   
    url = _downloadUrl(sUrl)
    
    channels = re.findall('".+?\[@\](.+?)\[@\].+?\[@\].+?\[@\](.+?)"', url, re.S)
    for sTitle,Link in channels:         
              sTitle =alfabekodla(sTitle) 
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', Link)
              oGui.addDir(SITE_IDENTIFIER, 'showotsplayer', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    
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
    sUrl =sUrl+'|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
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

def CanLiTV3(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    if '"Playlist":"http:.*?",' in sHtmlContent:  
               oOutputParameterHandler = cOutputParameterHandler()
               oOutputParameterHandler.addParameter('siteUrl', sUrl)
               oGui.addDir(SITE_IDENTIFIER, 'seyirturk', sTitle, 'genres.png', oOutputParameterHandler)
    
    sPattern = '"Baslik":"(.*?)","Logo":".*?","Resim":"(.*?)".*?"Stream":"(.*?)"'
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
            sTitle =  alfabekodla(sTitle)
            sTitle = aEntry[0].decode("latin-1").encode("utf-8")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
                   

            
            
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
