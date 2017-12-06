#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                  
SITE_IDENTIFIER = 'atv_com_tr'
SITE_NAME = 'ATV_com_tr'
SITE_DESC = 'télévision'
from xcanlitvzone import sshowBox19              
UA ='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
URL_MAIN = 'https://www.atv.com.tr'
MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
sRootArt = cConfig().getRootArt()
URL_webtv = 'https://www.atv.com.tr/webtv'
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  
def egetUrl(url, cookieJar=None,post=None,referer=None):

	cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
	opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
	#opener = urllib2.install_opener(opener)
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
	if referer:
		req.add_header('Referer',referer)
	response = opener.open(req,post,timeout=30)
	link=response.read()
	response.close()
	return link;


import ngx
import time
import socket

def access(r):
    r.log('access phase', ngx.LOG_INFO)
    r.ctx['code'] = 221

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8001))
    s.settimeout(2)
    s.send('foo')
    r.ho['X-Out'] = s.recv(10)

def content(r):
    r.status = r.ctx['code']
    r.sendHeader()
    r.send('1234567890');
    r.send('abcdefgefg', ngx.SEND_LAST)
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
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Pour Modifier ou  Ajouter des chaînes à FramaPad https://annuel.framapad.org/p/vstream [/COLOR]', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_FREE)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'FramaPad (Bêta)', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_SFR)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Sfr TV', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_ORANGE)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Orange TV', 'tv.png', oOutputParameterHandler)
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_BG)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Bouygues TV', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_WEB)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Tv du web', 'tv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Tu veux voir ta chaîne sur Libretv.me alors partage ta chaîne![/COLOR]', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_LIBRETV)
    oGui.addDir(SITE_IDENTIFIER, 'showLibreMenu', 'Libretv.me', 'libretv.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
def sEcho(s):
      s=s
      if '=1' in s:
	s=s.replace('=1','=2')
        return s 
      if '=2' in s:
	s=s.replace('=2','=3')
        return s 
      if '=3' in s:	
        s=s.replace('=3','=4')
        return s 
      if '=4' in s:	
        s=s.replace('=4','=5')
        return s 
      if '=5' in s:	
        s=s.replace('=5','=6')
        return s 
      if '=6' in s:	
        s=s.replace('=6','=7')
        return s 
      if '=7' in s:	
        s=s.replace('=7','=8')
        return s 
      if '=8' in s:	
        s=s.replace('=8','=9')
        return s 
      if '=9' in s:	
        s=s.replace('=9','=10')
        return s 
      if '=10' in s:	
        s=s.replace('=10','=11')
        return s 
      if '=11' in s:	
        s=s.replace('=11','=12')
        return s 
      if '=12' in s:	
        s=s.replace('=12','=13')
        return s 
      if '=13' in s:	
        s=s.replace('=13','=14')
        return s 
      if '=14' in s:	
        s=s.replace('=14','=15')
        return s 
      if '=15' in s:	
        s=s.replace('=15','=16')
        return s 
      if '=16' in s:	
        s=s.replace('=16','=17')
        return s
      if '=17' in s:	
        s=s.replace('=17','=18')
        return s 
      if '=18' in s:	
        s=s.replace('=18','=19')
        return s 
      if '=19' in s:	
        s=s.replace('=19','=20')
        return s 
      if '=20' in s:	
        s=s.replace('=20','=21')
        return s 
      if '=21' in s:	
        s=s.replace('=21','=22')
        return s 
      if '=22' in s:	
        s=s.replace('=22','=23')
        return s 
      if '=23' in s:	
        s=s.replace('=23','=24')
        return s 
      if '=24' in s:	
        s=s.replace('=24','=25')
        return s 
      if '=25' in s:	
        s=s.replace('=25','=26')
        return s 
      if '=26' in s:	
        s=s.replace('=26','=27')
        return s 
      if '=27' in s:	
        s=s.replace('=27','=28')
        return s 
      if '=28' in s:	
        s=s.replace('=28','=29')
        return s 
      if '=29' in s:	
        s=s.replace('=29','=30')
        return s 
      if '=30' in s:	
        s=s.replace('=30','=31')
        return s 
      if '=31' in s:	
        s=s.replace('=31','=32')
        return s 
      if '=32' in s:	
        s=s.replace('=32','=33')
        return s 
      if '=33' in s:	
        s=s.replace('=33','=34')
        return s 
      if '=34' in s:	
        s=s.replace('=34','=35')
        return s 
      if '=35' in s:	
        s=s.replace('=35','=36')
        return s 
      if '=36' in s:	
        s=s.replace('=36','=37')
        return s 
      if '=37' in s:	
        s=s.replace('=37','=38')
        return s 
      if '=38' in s:	
        s=s.replace('=38','=39')
        return s 
      if '=39' in s:	
        s=s.replace('=39','=40')
        return s 
      if '=40' in s:	
        s=s.replace('=40','=41')
        return s 
      if '=41' in s:	
        s=s.replace('=41','=42')
        return s 
      if '=42' in s:	
        s=s.replace('=42','=43')
        return s 
      if '=43' in s:	
        s=s.replace('=43','=44')
        return s 
      if '=44' in s:	
        s=s.replace('=44','=45')
        return s 
      if '=45' in s:	
        s=s.replace('=45','=46')
        return s 
      if '=46' in s:	
        s=s.replace('=46','=47')
        return s 
      if '=47' in s:	
        s=s.replace('=47','=48')
        return s 
      if '=48' in s:	
        s=s.replace('=48','=49')
        return s 
      if '=49' in s:	
        s=s.replace('=49','=50')
        return s 
      return False 

 
def atvcomtr():
    oGui = cGui()                           
    liste = []
    liste.append( ['ATV CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/atvhd/atvhd.m3u8'] ) 
    liste.append( ['ATV YEDEK','https://canlitv.co/atv.html'] ) 

    liste.append( ['A HABER CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/ahaberhd/ahaberhd.m3u8'] )
    liste.append( ['A SPOR CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/asporhd/asporhd.m3u8']) 
    liste.append( ['minikaGO CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikago/minikago.m3u8']) 
    liste.append( ['minikaCOCUK CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikagococuk/minikagococuk.m3u8'] ) 
    liste.append( ['YENİ DİZİLER','https://www.atv.com.tr/diziler'] )
    liste.append( ['KLASİK DİZİLER ABC','https://www.atv.com.tr/ajax/category-items?categoryId=afc46919-4431-4096-a0c7-73871cfcc8ac&page=1'] )
    for sTitle,sUrl2 in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'PROGRAMLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'klasikdizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def klasikdizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []                
    liste.append( ['A',URL_MAIN+'/klasik-diziler?sw=a'] )
    liste.append( ['B',URL_MAIN+'/klasik-diziler?sw=b'] )
    liste.append( ['C',URL_MAIN+'/klasik-diziler?sw=c'] )
    liste.append( ['Ç',URL_MAIN+'/klasik-diziler?sw=Ç'] )
    liste.append( ['D',URL_MAIN+'/klasik-diziler?sw=d'] )
    liste.append( ['E',URL_MAIN+'/klasik-diziler?sw=e'] )
    liste.append( ['F',URL_MAIN+'/klasik-diziler?sw=f'] )
    liste.append( ['G',URL_MAIN+'/klasik-diziler?sw=g'] )
    liste.append( ['H',URL_MAIN+'/klasik-diziler?sw=h'] )
    liste.append( ['I',URL_MAIN+'/klasik-diziler?sw=i'] )
    liste.append( ['İ',URL_MAIN+'/klasik-diziler?sw=İ'] )
    liste.append( ['J',URL_MAIN+'/klasik-diziler?sw=j'] )
    liste.append( ['K',URL_MAIN+'/klasik-diziler?sw=k'] )
    liste.append( ['L',URL_MAIN+'/klasik-diziler?sw=l'] )
    liste.append( ['M',URL_MAIN+'/klasik-diziler?sw=m'] )
    liste.append( ['N',URL_MAIN+'/klasik-diziler?sw=n'] )
    liste.append( ['O',URL_MAIN+'/klasik-diziler?sw=o'] )
    liste.append( ['Ö',URL_MAIN+'/klasik-diziler?sw=Ö'] )
    liste.append( ['P',URL_MAIN+'/klasik-diziler?sw=p'] )
    liste.append( ['R',URL_MAIN+'/klasik-diziler?sw=r'] )
    liste.append( ['S',URL_MAIN+'/klasik-diziler?sw=s'] ) 
    liste.append( ['Ş',URL_MAIN+'/klasik-diziler?sw=Ş'] ) 
    liste.append( ['T',URL_MAIN+'/klasik-diziler?sw=t'] )
    liste.append( ['U',URL_MAIN+'/klasik-diziler?sw=u'] )
    liste.append( ['Ü',URL_MAIN+'/klasik-diziler?sw=Ü'] )
    liste.append( ['V',URL_MAIN+'/klasik-diziler?sw=v'] )
    liste.append( ['W',URL_MAIN+'/klasik-diziler?sw=w'] )
    liste.append( ['X',URL_MAIN+'/klasik-diziler?sw=x'] )
    liste.append( ['Y',URL_MAIN+'/klasik-diziler?sw=y'] )
    liste.append( ['Z',URL_MAIN+'/klasik-diziler?sw=z'] )
    liste.append( ['123',URL_MAIN+'/klasik-diziler?sw=123'] )
    
               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'klasikshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def klasikshowSinema():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    
 
    oParser = cParser()
    #Decoupage pour cibler la partie Film ajouté    
    sPattern = '<ul id="series-list">(.+?)<div align="center">'
                
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    #regex pour listage films sur la partie decoupée  
    sHtmlContent = aResult
                              
    sPattern = '<li><a href="/klasik-diziler(.*?)"> <span> <img alt="" class="lazyload" data-original="(.*?)" src=".*?"> </span> <strong> <strong>(.*?)</strong>'
    aResult = oParser.parse(sHtmlContent, sPattern)
      
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = 'https://www.atv.com.tr/webtv'+ sUrl +'/bolum?&page=1'
                
            
            
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'klasikpageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
            
    oGui.setEndOfDirectory()
def klasikpageshowMovies():
        oGui = cGui()
                                                             
                                                                                                     
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
          
        cookie = getUrl(Url, output='cookie').result
        headers={'User-Agent':UA,'Cookie':cookie,'Upgrade-Insecure-requests':'1','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br'}
        url  = requests.get(Url, headers = headers).text 
        url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
        url = url.encode( "utf-8")
        url = urllib.unquote_plus(url) 
        url = url.replace('�','')      
                    
             
        oParser = cParser()                       
    #Decoupage pour cibler la partie Film ajouté    
        sPattern = '<ul id="series-video-list">(.+?)</footer>'
                    
        aResult = oParser.parse(url, sPattern)
        sHtmlContent = aResult
                   
        sPattern = '<a href="(.*?)"> <em> <img alt="" class="lazyload" data-original="(.*?)" src=".*?"> </em> <span> <em>(.*?)</em>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if not (aResult[0] == False):
                total = len(aResult[1])
                dialog = cConfig().createDialog(SITE_NAME)
       
                for aEntry in aResult[1]:
                    cConfig().updateDialog(dialog, total)
                    if dialog.iscanceled():
                        break
           
                    sTitle = alfabekodla(aEntry[2])
                    sPicture = str(aEntry[1])
                    if not 'http' in sPicture:
                        sPicture = str(URL_MAIN) + sPicture
                
                    sUrl = str(aEntry[0])
                    if not 'http' in sUrl:
                        sUrl = str(URL_MAIN) + sUrl 
                                                                
                    
                    sTitle = alfabekodla(sTitle)
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

 
                    if '/serie/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    elif '/anime/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    else:
                        oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
                cConfig().finishDialog(dialog)
           
               
                sNextPage =sEcho(str(Url))
                if (sNextPage != False):
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    
                oGui.setEndOfDirectory()

def  showSinema():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    
 
    oParser = cParser()
    #Decoupage pour cibler la partie Film ajouté    
    sPattern = '<ul id="series-list">(.+?)<div align="center">'
                
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    #regex pour listage films sur la partie decoupée  
    sHtmlContent = aResult
                              
    sPattern = '<li><a href="(.*?)"> <span> <img alt="" class="lazyload" data-original="(.*?)" src=".*?"> </span> <strong> <strong>(.*?)</strong>'
    aResult = oParser.parse(sHtmlContent, sPattern)
      
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0].replace('/diziler/','/webtv/'))
            if not 'http' in sUrl:
                sUrl = 'https://www.atv.com.tr'+ sUrl +'/bolum?&page=1'
                
            
            
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
            
    oGui.setEndOfDirectory()

def dizizleABC():
    oGui = cGui()
  
    sHtmlContent= 'http://www.atv.com.tr/webtv/sila/bolum/48?id=80536f4a-eccc-46bf-a18e-400854bfc92f'
    sHtmlContent = sHtmlContent.replace('klasik-diziler','webtv').replace('programlar','webtv').replace('diziler','webtv').replace('<ul id="series-list">','</li>')
 
    urla  = "http://www.atv.com.tr/"
                      
    referer=[('Referer',urla)]
    url=gegetUrl(sHtmlContent,headers=referer) 
       
        
    name ='test'
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

def pageshowMovies():
        oGui = cGui()
                                                             
                                                                                                     
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
          
        cookie = getUrl(Url, output='cookie').result
        headers={'User-Agent':UA,'Cookie':cookie,'Upgrade-Insecure-requests':'1','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate, br'}
        url  = requests.get(Url, headers = headers).text 
        url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
        url = url.encode( "utf-8")
        url = urllib.unquote_plus(url) 
        url = url.replace('�','')      
                    
             
        oParser = cParser()                       
    #Decoupage pour cibler la partie Film ajouté    
        sPattern = '<div class="hListParts">(.+?)<div class="cls">'
                    
        aResult = oParser.parse(url, sPattern)
        sHtmlContent = aResult
        sPattern = '<a href="(.*?)"> <em> <img alt="" class="lazyload" data-original="(.*?)" src=".*?"> </em> <span> <em>(.*?)</em>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if not (aResult[0] == False):
                total = len(aResult[1])
                dialog = cConfig().createDialog(SITE_NAME)
       
                for aEntry in aResult[1]:
                    cConfig().updateDialog(dialog, total)
                    if dialog.iscanceled():
                        break
           
                    sTitle = alfabekodla(aEntry[2])
                    sPicture = str(aEntry[1])
                    if not 'http' in sPicture:
                        sPicture = str(URL_MAIN) + sPicture
                
                    sUrl = str(aEntry[0])
                    if not 'http' in sUrl:
                        sUrl = str(URL_MAIN) + sUrl 
                                                                
                    
                    sTitle = alfabekodla(sTitle)
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster

 
                    if '/serie/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    elif '/anime/' in aEntry[1]:
                        oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                    else:
                        oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
                cConfig().finishDialog(dialog)
           
               
                sNextPage =sEcho(str(Url))
                if (sNextPage != False):
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    
                oGui.setEndOfDirectory()
                        
def ArshowSinema():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    
 
    oParser = cParser()
    #Decoupage pour cibler la partie Film ajouté    
    sPattern = '<div class="liste">(.+?)</body>'
                
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    #regex pour listage films sur la partie decoupée  
    sHtmlContent = aResult
                
                                   
    sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>.*?<strong>(.*?)</strong>'
    aResult = oParser.parse(sHtmlContent, sPattern)
      
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl+ '/bolum?&page=1'
                
            
            
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'ArshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
            
    oGui.setEndOfDirectory()



def mArshowMovies():
        oGui = cGui()
   
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        Url = Url.replace('klasik-diziler','webtv').replace('programlar','webtv').replace('diziler','webtv').replace('<ul id="series-list">','</li>')
 
        oRequestHandler = cRequestHandler(Url)
        sHtmlContent = oRequestHandler.request();
        
        oParser = cParser()
    #Decoupage pour cibler la partie Film ajouté    
        sPattern = '<div class="column">(.+?)</body>'
   
        aResult = oParser.parse(sHtmlContent, sPattern)
    #regex pour listage films sur la partie decoupée  
        sHtmlContent = aResult
    
        sPattern = '<li>.*?<a href="(/webtv/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*? </em>.*?<em>(.*?)</em>'
        aResult = oParser.parse(sHtmlContent, sPattern)
      
        if not (aResult[0] == False):
                total = len(aResult[1])
                dialog = cConfig().createDialog(SITE_NAME)
       
                for aEntry in aResult[1]:
                    cConfig().updateDialog(dialog, total)
                    if dialog.iscanceled():
                        break
           
                    sTitle = alfabekodla(aEntry[2])
                    sPicture = str(aEntry[1])
                    if not 'http' in sPicture:
                        sPicture = str(URL_MAIN) + sPicture
                
                    sUrl = str(aEntry[0])
                    if not 'http' in sUrl:
                        sUrl = str(URL_MAIN) + sUrl 
                
            
            
                    sTitle = alfabekodla(sTitle)
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                    oGui.addMovie( '', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
                cConfig().finishDialog(dialog)
           
               
                sNextPage =sEcho(str(Url))
                if (sNextPage != False):
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                    oGui.addDir(SITE_IDENTIFIER, 'ArshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    
        oGui.setEndOfDirectory()

def ArshowMovies(sSearch = ''):
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
        sPattern = '<article class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        Url = Url.replace('klasik-diziler','webtv').replace('programlar','webtv').replace('diziler','webtv').replace('<ul id="series-list">','</li>')
 
        oRequestHandler = cRequestHandler(Url)
        sHtmlContent = oRequestHandler.request();
        
        oParser = cParser()
    #Decoupage pour cibler la partie Film ajouté    
        sPattern = '<div class="column">(.+?)</body>'
   
        aResult = oParser.parse(sHtmlContent, sPattern)
    #regex pour listage films sur la partie decoupée  
        sHtmlContent = aResult
    
        sPattern = '<li>.*?<a href="(/webtv/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*? </em>.*?<em>(.*?)</em>'
    
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
            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumbnail = str(aEntry[1])
            if not 'http' in  sThumbnail:
                 sThumbnail = str(URL_MAIN) +  sThumbnail
                
            
           
          
            sTitle = alfabekodla(aEntry[2])
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage =sEcho(str(Url))#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'ArshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()


def ddizizleABC():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    urla  = "http://www.atv.com.tr/"
                      
    referer=[('Referer',urla)]
    url=gegetUrl(sUrl,headers=referer) 
       
        
    name ='test'
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

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
                

    Pattern = '<li id="part_.*?" data-point=".*?"><a href="(.*?)">(.*?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox3', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def play__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oGuiElement.setThumbnail(sThumbnail)

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()
    return False
        
    oGui.setEndOfDirectory()
def sshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    urla  = "http://www.atv.com.tr/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
     
    data=data.replace("&quot;","").replace("\/","/").replace("amp;","").replace('-',"_")
    
    url = re.findall('<input id="hdnRelatedVideo" name="hdnRelatedVideo" type="hidden" value="(.*?)"', data)
	                                                                           
                         
    			             	                                                
    
    StreamUrl = re.findall('AlternateVideoUrl:(.*?),', url[0])
                                                   
                                     
    import random
    import math   
    token=''
    token=math.floor(random.random() * 1000000 + 1)                                              
    sHosterUrl = 'http://video02.atv.com.tr/%s' % (StreamUrl[0])
           
      
          
       
        
        

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False
def sshowBox3():
    oGui = cGui()
    cookieJar=cookielib.LWPCookieJar()
    oInputParameterHandler = cInputParameterHandler()
    Urlk = oInputParameterHandler.getValue('siteUrl')
    Url = oInputParameterHandler.getValue('siteUrl')
    Url=Url.replace("?id=","id=")
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    urla  = "https://www.atv.com.tr/"
    referer=[('Referer',urla)]
    page_data=egetUrl(Urlk ,cookieJar,referer=Urlk)          
    page_data=page_data.replace("&#34;",'"')
    
       
    cookie = getUrl(urla, output='cookie').result                                 
    streamDaten = re.findall('https://www.atv.com.tr/webtv/(.*?)/bolum/(.*?)id=.*?', Url )
    if streamDaten:
       (adi, File) = streamDaten[0]   
       
       name=adi
       name=name.replace("-",'_')
       base = '0'+File
       
       sessionId = re.findall("sessionId='(.*?)'", page_data)[0] 
       
       
       url = re.findall('<input id="hdnVideo".*?value="."BaseVideoUrl":"(.*?)_0400"', page_data)[0]  
       if url.find('/') > -1:      
            base1 ='%s'%(url) 
       else:
            base1 ='0%s/%s'%(File,url) 
       import random
       import math                      
       token=math.floor(random.random() * 1000000 + 1)   
                                                                
       sUrl = 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://atv-vod.ercdn.net/'+ name + '/' + base1 + '.smil/playlist.m3u8&url2=http://atv-vod.ercdn.net/'+ name + '/' + base1 + '_0400.mp4&%s' % (token)
       headers = {'Cookie':cookie,'Referer':Urlk,'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'}
         
                       
       import ssl

# This restores the same behavior as before.
       context = ssl._create_unverified_context()
#       source = egetUrl(sUrl ,cookieJar,referer=Urlk)                
       source = requests.get(sUrl, headers = headers).text
       urlr = re.findall('"Url":"(.*?)"', source, re.S)[0]#+ '&SessionID=efuaswsqyazwpzrtu3vzydpu&StreamGroup=kirgin-cicekler&Site=atv&DeviceGroup=web'
      
       eaders = {'Content-Type':'application/vnd.apple.mpegurl','origin': 'https://www.atv.com.tr','referer':Urlk,'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
                 
#       rce =requests.get(sou, headers =eaders).text
       
       
 
       TIK='|Referer='+Urlk+'&User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    
       ou = urlr +'&SessionID='+sessionId+'&StreamGroup='+adi+'&Site=atv&DeviceGroup=web'+ TIK
       
#       rce =egetUrl(ou ,cookieJar,referer=Urlk) 
#       rce =requests.get(ou, headers =headers).text
       name ='test'
       addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,ou,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok                
def msshowBox3():      
       playlist = re.findall('"AlternateUrl":"(.*?)"', source, re.S)
       for track in playlist:
           
                   
          
       
        
                    sHosterUrl = track

                    oGuiElement = cGuiElement()
                    oGuiElement.setSiteName(SITE_IDENTIFIER)
                    oGuiElement.setTitle(sTitle)
                    oGuiElement.setMediaUrl(sHosterUrl)
        

                    oPlayer = cPlayer()
                    oPlayer.clearPlayList()
                    oPlayer.addItemToPlaylist(oGuiElement)
                    oPlayer.startPlayer()  
                    return False
 

def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    streamDaten = re.findall('https://www.atv.com.tr/webtv/(.*?)/bolum/(.*?)?id=.*?', Url )
    if streamDaten:
        (name, File) = streamDaten[0]                                            
                                     
    import random
    import math   
    token=''
    token=math.floor(random.random() * 1000000 + 1)                                              
    url = 'http://videotoken.tmgrup.com.tr/webtv/secure?url=http://atv-vod.ercdn.net/' + base + '.smil/playlist.m3u8&url2=http://atv-vod.ercdn.net/' + base + '_0400.mp4&%s' % (token)
    print url       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', 'Referer':Url, 'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    data = requests.get(url, headers = headers).text
 
     
               
    playlist = re.findall('"AlternateUrl":"(.*?)"', data, re.S)


    for track in playlist:
           
        
          
       
        
        TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
       
        sHosterUrl = track+ TIK

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  
        return False
def smshowBox1():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(name )
    
    from default  import PlayUrl
    PlayUrl(name, url, iconimage)
    
    oGui.setEndOfDirectory() 
def showBox():
    oGui = cGui()
    import random
    import math   
    token=''
    token=math.floor(random.random() * 1000000 + 1)   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle )
    iconimage =  alfabekodla(iconimage)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://www.atv.com.tr/[makelist.param1]', 'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    source = requests.get(url, headers = headers).text
               
    playlist = re.findall('"Url":"(.*?)"', source, re.S)
    for track in playlist:
           
        
          
       
                    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
       
                    sHosterUrl = track+ TIK

                    oGuiElement = cGuiElement()
                    oGuiElement.setSiteName(SITE_IDENTIFIER)
                    oGuiElement.setTitle(sTitle)
                    oGuiElement.setMediaUrl(sHosterUrl)
        

                    oPlayer = cPlayer()
                    oPlayer.clearPlayList()
                    oPlayer.addItemToPlaylist(oGuiElement)
                    oPlayer.startPlayer()  
                    return False
  
    
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
    

   
def mmmshowHosters():

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    oParser = cParser()

    sPattern = '"Url":"(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)

    # 1 seul resultat et sur leur propre hebergeur
    if (aResult[0] == True):
        
        
            
        web_url = '' + aResult[1][0]
            
        sHosterUrl = web_url

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sMovieTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return False
  
