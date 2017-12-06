#-*- coding: utf-8 -*-
#http://getproxi.es/TR-proxies/
from resources.lib.otvhelper import *                  
from resources.sayfalar.youtubecom_tr import youtubeplayer 
SITE_IDENTIFIER = 'startv_com_tr'
SITE_NAME = 'Star TV + PuhuTV'
SITE_DESC = 'télévision'
import xbmcplugin, xbmcgui
URL_MAIN = 'http://www.startv.com.tr'
from xcanlitvzone import sshowBox19              
from resources.lib import comon
MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
import urllib2, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64

import requests
import os
import shutil
from cookielib import CookieJar
PathCache = cConfig().getSettingCache()
def Readcookie(Domain):
        Name = os.path.join(PathCache,'Cookie_'+ str(Domain) +'.txt')
        
        try:
            file = open(Name,'r')
            data = file.read()
            file.close()
        except:
            return ''
        
        return data
def DownloaderClass(url,dest):
    
    dp = xbmcgui.DialogProgress()
    dp.create("OTV_MEDIA ZIP DOWNLOADER","Downloading File",url)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _downloadUrl(url):
		req = urllib2.Request(url)
		req.add_header('Accept', '*/*')
                req.add_header('Accept-Encoding', 'gzip, deflate')
                req.add_header('Accept-Language', 'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4')
                req.add_header('Connection', 'keep-alive')
                req.add_header('Host', 'dygvideo.dygdigital.com')

                req.add_header('Origin', 'http://www.ntv.com.tr')

                req.add_header('Referer', 'http://www.ntv.com.tr/canli-yayin/ntv')

                req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36')
		u = urllib2.urlopen(req)
		content = u.read()
		u.close()
                 
		return content



def getStoredFile(FileName):
	ret_value=None
	File_name=os.path.join(profile_path,FileName )
	try:
		data = open(File_name, "r").read()
		ret_value=data
	except:
		traceback.print_exc(file=sys.stdout)
	return ret_value
	
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



class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data
def sEcho(s):
      s=s
      if 'page=1' in s:
	s=s.replace('page=1','page=2')
        return s 
      if 'page=2' in s:
	s=s.replace('page=2','page=3')
        return s 
      if 'page=3' in s:	
        s=s.replace('page=3','page=4')
        return s 
      if 'page=4' in s:	
        s=s.replace('page=4','page=5')
        return s 
      if 'page=5' in s:	
        s=s.replace('page=5','page=6')
        return s 
      if 'page=6' in s:	
        s=s.replace('page=6','page=7')
        return s 
      if 'page=7' in s:	
        s=s.replace('page=7','page=8')
        return s 
      if 'page=8' in s:	
        s=s.replace('page=8','page=9')
        return s 
      if 'page=9' in s:	
        s=s.replace('page=9','page=10')
        return s 
      if 'page=10' in s:	
        s=s.replace('page=10','page=11')
        return s 
      if 'page=11' in s:	
        s=s.replace('page=11','page=12')
        return s 
      if 'page=12' in s:	
        s=s.replace('page=12','page=13')
        return s 
      if 'page=13' in s:	
        s=s.replace('page=13','page=14')
        return s 
      if 'page=14' in s:	
        s=s.replace('page=14','page=15')
        return s 
      if 'page=15' in s:	
        s=s.replace('page=15','page=16')
        return s 
      if 'page=16' in s:	
        s=s.replace('page=16','page=17')
        return s
      if 'page=17' in s:	
        s=s.replace('page=17','page=18')
        return s 
      if 'page=18' in s:	
        s=s.replace('page=18','page=19')
        return s 
      if 'page=19' in s:	
        s=s.replace('page=19','page=20')
        return s 
      if 'page=20' in s:	
        s=s.replace('page=20','page=21')
        return s 
      if 'page=21' in s:	
        s=s.replace('page=21','page=22')
        return s 
      if 'page=22' in s:	
        s=s.replace('page=22','page=23')
        return s 
      if 'page=23' in s:	
        s=s.replace('page=23','page=24')
        return s 
      if 'page=24' in s:	
        s=s.replace('page=24','page=25')
        return s 
      if 'page=25' in s:	
        s=s.replace('page=25','page=26')
        return s 
      if 'page=26' in s:	
        s=s.replace('page=26','page=27')
        return s 
      if 'page=27' in s:	
        s=s.replace('page=27','page=28')
        return s 
      if 'page=28' in s:	
        s=s.replace('page=28','page=29')
        return s 
      if 'page=29' in s:	
        s=s.replace('page=29','page=30')
        return s 
      if 'page=30' in s:	
        s=s.replace('page=30','page=31')
        return s 
      if 'page=31' in s:	
        s=s.replace('page=31','page=32')
        return s 
      if 'page=32' in s:	
        s=s.replace('page=32','page=33')
        return s 
      if 'page=33' in s:	
        s=s.replace('page=33','page=34')
        return s 
      if 'page=34' in s:	
        s=s.replace('page=34','page=35')
        return s 
      if 'page=35' in s:	
        s=s.replace('page=35','page=36')
        return s 
      if 'page=36' in s:	
        s=s.replace('page=36','page=37')
        return s 
      if 'page=37' in s:	
        s=s.replace('page=37','page=38')
        return s 
      if 'page=38' in s:	
        s=s.replace('page=38','page=39')
        return s 
      if 'page=39' in s:	
        s=s.replace('page=39','page=40')
        return s 
      if 'page=40' in s:	
        s=s.replace('page=40','page=41')
        return s 
      if 'page=41' in s:	
        s=s.replace('page=41','page=42')
        return s 
      if 'page=42' in s:	
        s=s.replace('page=42','page=43')
        return s 
      if 'page=43' in s:	
        s=s.replace('page=43','page=44')
        return s 
      if 'page=44' in s:	
        s=s.replace('page=44','page=45')
        return s 
      if 'page=45' in s:	
        s=s.replace('page=45','page=46')
        return s 
      if 'page=46' in s:	
        s=s.replace('page=46','page=47')
        return s 
      if 'page=47' in s:	
        s=s.replace('page=47','page=48')
        return s 
      if 'page=48' in s:	
        s=s.replace('page=48','page=49')
        return s 
      if 'page=49' in s:	
        s=s.replace('page=49','page=50')
        return s 
      return False 





def n3bu1A(n):
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

def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku      


Urlom  = "http://getproxi.es/TR-proxies/"
def aResEcho(aRes):
      aRes=aRes
      for aEntry in aRes:
	aEntry=aEntry
        return aEntry

def hTRVPV(): #affiche les genres
    oGui = cGui()
                
    
    oRequestHandler = cRequestHandler(Urlom)
    oInputParameterHandler = cInputParameterHandler()            
    sHosterUrl= oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = oRequestHandler.request()           
    sHtmlContent = sHtmlContent.replace("<script>nibble(onion('","<scriptik>").replace("<script>nibble(salt('<n","<scriptik>").replace("<script>nibble(chives(salt('","<scriptik>").replace("<script>nibble(salt(chives('","<scriptik>").replace("<script>nibble(cheese('>","<scriptik>").replace("'),'p","</scriptik>").replace("')),'proxy","</scriptik>").replace("Turkey</td>",'Turkey <span class="small">')          
    
    
    channels=re.findall('</div></span></td>.*?<scriptik>(.*?)</scriptik>.*?" />(.*?)<span class="small">', sHtmlContent, re.S)
    for Link,sTitle in channels:                    
            sTitle =  alfabekodla(sTitle) 
            Link = Link
            if re.search('uggc://', Link, re.S):
            
                 url3= n3bu1A(Link)
                 url3= url3.replace('"','/"')
                 channels=re.findall('href=/"(.*?)"', url3)                                                                                             
                 channel=aResEcho(channels)
            elif re.search('//:cggu', Link, re.S):
                 url13 =  okuoku(Link)                                                                                                                                                                                                                       
                 url3= n3bu1A(url13)
                 url3= url3.replace('"','/"')
                 channels=re.findall('href=/"(.*?)"', url3)
                 channel=aResEcho(channels)
            elif re.search('P|G|E|Y|X|W|', Link, re.S):
                 url2 = base64.b64decode(Link)
                 url3 =  okuoku(url2)                                                                                                                                                                                                                       
                 url3= url3.replace('"','/"')
                 channels=re.findall('href=/"(.*?)"', url3)                                                                                                                                                                       
                 channel=aResEcho(channels)                                                                                                                                                                                        
            
            sPicture= 'http://getproxi.es/images/24x16/TR.png' 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('proks', channel)
            oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
            oGui.addTV(SITE_IDENTIFIER, 'mmdecodeURL', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()                
                                                
                               
def TRVPV(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()            
    sUrl= oInputParameterHandler.getValue('siteUrl')
    url = "http://getproxi.es/TR-proxies/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Host': 'getproxi.es', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    sHtmlContent = requests.get(url, headers = headers).text         
    sHtmlContent = sHtmlContent.replace("<script>nibble(chives('","<scriptik>").replace("<script>nibble(cheese(chives('","<scriptik>").replace("<script>nibble(onion('","<scriptik>").replace("<script>nibble(salt('<n","<scriptik>").replace("<script>nibble(chives(salt('","<scriptik>").replace("<script>nibble(salt(chives('","<scriptik>").replace("<script>nibble(cheese('>","<scriptik>").replace("'),'p","</scriptik>").replace("')),'proxy","</scriptik>").replace("Turkey</td>",'Turkey <span class="small">')          
    sPattern = '</div></span></td>.*?<scriptik>(.*?)</scriptik>.*?" />(.*?)<span class="small">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
      
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = aEntry[1]
            sTitle =  alfabekodla(sTitle) 
            Link = aEntry[0]
            if re.search('uggc://', Link, re.S):
                 url3= n3bu1A(Link)
                 
                 channels=re.findall('href="(.*?)"', url3)                                                                                             
                 channel=aResEcho(channels)
            elif re.search('//:cggu', Link, re.S):
                 url13 =  okuoku(Link)                                                                                                                                                                                                                       
                 url3= n3bu1A(url13)
                 
                 channels=re.findall('href="(.*?)"', url3)
                 channel=aResEcho(channels)
            elif re.search('|P|G|E|Y|X|W|', Link, re.S):
                 url2 = base64.b64decode(Link)
                 url3 =  okuoku(url2)                                                                                                                                                                                                                       
                 
                 channels=re.findall('href="(.*?)"', url3)                                                                                                                                                                       
                 channel=aResEcho(channels)                                                                                                                                                                                        
            referer=[('Referer',sUrl)]
            data=gegetUrl(sUrl,headers=referer) 
                    
            chan = re.findall('"data":."id":(.*?),"uuid"', data, re.S)
            sHoster=aResEcho(chan)
            sPicture= 'http://getproxi.es/images/24x16/TR.png' 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('proks', channel)
            oOutputParameterHandler.addParameter('siteUrl', sHoster)
            oGui.addTV(SITE_IDENTIFIER, 'VPNTEST', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def VPNTEST():
                       
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()            
    sUrl= oInputParameterHandler.getValue('siteUrl')                
    urlk = oInputParameterHandler.getValue('proks')
#    chan = re.findall('"data":."id":(.*?),"uuid"', data, re.S)
    newurl='browse.php?u=https://puhutv.com/api/assets/%svideos'%(sUrl)
    wurl='index.php?q=https://puhutv.com/api/assets/%svideos'%(sUrl)
    tarzlistesi= []                
    tarzlistesi.append(('VPN TEST', newurl))
    tarzlistesi.append(('VPN TEST 2', wurl))
                                       
                   
    for sTitle,Url in tarzlistesi:
        sPicture= 'http://getproxi.es/images/24x16/TR.png'
        
        URL=urlk+Url.replace('index','/index').replace('browse','/browse')
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL)
        oGui.addTV(SITE_IDENTIFIER, 'mmdecodeURL', sTitle, sPicture, sPicture, '', oOutputParameterHandler)       
    oGui.setEndOfDirectory()


def load():
    linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
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
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
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

 
def startvcomtr():
    oGui = cGui()
    
    tarzlistesi = []                                  
    
    tarzlistesi.append(("Star TV", "http://lcgid8xu.rocketcdn.com/startvhd.stream_720p/playlist.m3u8"))
    tarzlistesi.append(("Star TV YEDEK", "https://www.youtube.com/watch?v=jWP3ntl64I4&feature=youtu.be"))
    tarzlistesi.append(("NTV", "http://nt4p9nef.rocketcdn.com/ntvhd.stream_720p/playlist.m3u8"))
    tarzlistesi.append(("NTV YEDEK", "https://www.youtube.com/watch?v=oruk-T3_xSw"))
    tarzlistesi.append(("NTV SPOR", "http://ujdwx6qj.rocketcdn.com/ntvsporhd.stream_720p/playlist.m3u8"))
    tarzlistesi.append(("NTV SPOR YEDEK", "https://www.youtube.com/watch?v=uxgKogFymQU"))
    tarzlistesi.append(("KRAL TV", "http://mid5dg6m.rocketcdn.com/kraltv_360p/playlist.m3u8"))
    tarzlistesi.append(("KRAL TV YEDEK", "https://www.youtube.com/watch?v=6N4tCSY3TIo"))
    tarzlistesi.append(("KRAL POP", "http://bqgsd19q.rocketcdn.com/kralpop_720/playlist.m3u8"))
    tarzlistesi.append(("KRAL POP YEDEK", "https://www.youtube.com/watch?v=7YzYxQPVsck"))
    tarzlistesi.append(("KRAL WORLD", "http://stmpo0wa.rocketcdn.com/kralworldtv.smil/playlist.m3u8"))
    tarzlistesi.append(("KRAL WORLD YEDEK", "https://www.youtube.com/watch?v=87j9tmFXbQI"))
    tarzlistesi.append(("YEDEK", "https://www.youtube.com/watch?v=87j9tmFXbQI"))

    tarzlistesi.append(("PuhuTV+Diziler", "https://puhutv.com/api/title_groups"))
    
    for sTitle,sUrl2 in tarzlistesi:
        sPictur= "http://www.izleyiciplatformu.com/wp-content/uploads/2017/03/Puhu-TV-Nas%C4%B1l-izlenir-Puhu-Tv-Nereden-izleyebilirim-%C4%B0%C5%9Fte-Detaylar.png"
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sPictur)
        if sTitle == 'NTV SPOR':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'NTV':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL POP':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'PuhuTV+Diziler':
             oGui.addDir(SITE_IDENTIFIER, 'katolevis', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL WORLD':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Star TV':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KRAL TV':
             oGui.addDir(SITE_IDENTIFIER, 'StarTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'StarcodeURL', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'youtubeplayer',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()

def StarTV():
                oGui = cGui()
                oInputParameterHandler = cInputParameterHandler()
                urlln= oInputParameterHandler.getValue('siteUrl')
		urla= 'http://www.ntv.com.tr/canli-yayin/ntv'                
                urlk= 'http://www.ntv.com.tr/' 
                referer=[('Referer',urlk)]
                data=gegetUrl(urla,headers=referer)                          
            
                streamDaten = re.findall('data-player-token="(.*?)"', data, re.S)
                if streamDaten:
                        (serviceUrl) = streamDaten[0]
                urlk = "http://dygvideo.dygdigital.com/live/hds/kralworldtv?token=%s"  % (serviceUrl)
                referer=[('Referer',urla)]
                data=gegetUrl(urlk,headers=referer) 
                urll = re.findall('"url":"(.*?)"', data, re.S)[0]
                url = urlln+urll
                name ='test'
                addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def StarcodeURL():
                      
                urla= 'http://www.ntv.com.tr/canli-yayin/ntv'                
                urlk= 'http://www.ntv.com.tr/' 
                
                referer=[('Referer',urlk)]
                data=gegetUrl(urla,headers=referer) 
                streamDaten = re.findall('data-player-token="(.*?)"', data, re.S)
                if streamDaten:
                        (serviceUrl) = streamDaten[0]
                                                  
                urll = "http://dygvideo.dygdigital.com/live/hls/ntv?token=%s"  % (serviceUrl)                                                                                                                                                                                                      
		
                headers = {'Referer':'http://www.ntv.com.tr/canli-yayin/ntv','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36','Host':'dygvideo.dygdigital.com','X-Requested-With': 'XMLHttpRequest'}

   
                cookie = client.request( urll, output='cookie')
                url  = client.request( urll, cookie=cookie, headers=headers)

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

def YoutubeOynat():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl= oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
 

    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
        oHoster.setDisplayName(sDisplayTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
          
       
def katolevis():
    oGui = cGui()
                    
    tarzlistesi= []                
            
    tarzlistesi.append(("Dizi", "dizi"))
    tarzlistesi.append(("Film", "film"))
    tarzlistesi.append(("Çocuk", "cocuk"))
    tarzlistesi.append(("Fi", "https://puhutv.com/api/seasons/240/episodes?e_page=1&e_per=24"))
    for sTitle,sUrl in tarzlistesi:
        
        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        
        if sTitle == 'Dizi':
             oGui.addDir(SITE_IDENTIFIER, 'puhudizi',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Film':
             oGui.addDir(SITE_IDENTIFIER, 'puhufilm', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Çocuk':
             oGui.addDir(SITE_IDENTIFIER, 'COCUKshowshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Fi':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Öneriler':
             oGui.addDir(SITE_IDENTIFIER, 'showshowSinema2', sTitle, 'genres.png', oOutputParameterHandler)
                                   
        else:
             oGui.addDir(SITE_IDENTIFIER, 'showshowSinema2',  sTitle, 'genres.png', oOutputParameterHandler)

                     
    oGui.setEndOfDirectory()
def puhufilm():
    oGui = cGui()
                    
    tarzlistesi= []                
    tarzlistesi.append(("Aile", "aile-film"))
    tarzlistesi.append(("Dram", "dram-film"))
    tarzlistesi.append(("Komedi", "komedi-film"))
    tarzlistesi.append(("Romantik", "romantik-film"))
    tarzlistesi.append(("Romantik Komedi", "romantik-komedi-film"))
    tarzlistesi.append(("Aksiyon - Macera", "aksiyon-macera-film"))
    tarzlistesi.append(("Gen�lik", "genclik-film"))
    tarzlistesi.append(("Polisiye", "polisiye-film"))
    tarzlistesi.append(("Gerilim", "gerilim-film"))
    tarzlistesi.append(("Korku", "korku-film"))
    tarzlistesi.append(("Klasikler", "klasikler-film"))
    tarzlistesi.append(("Klasikler", "klasikler-film"))
    tarzlistesi.append(("Dönem", "donem-film"))
    tarzlistesi.append(("Kült", "kult-film"))
    tarzlistesi.append(("Tiyatro", "tiyatro-film"))
                                   
                        
    for sTitle,Url in tarzlistesi:
        sUrl = "https://puhutv.com/api/slug/%s?s_page=1&s_per=40"%Url
        oOutputParameterHandler = cOutputParameterHandler()
       
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showshowSinema2', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def puhudizi():
    oGui = cGui()
                    
    tarzlistesi= []                
    tarzlistesi.append(("Aile", "aile-dizi"))
    tarzlistesi.append(("Dram", "dram-dizi"))
    tarzlistesi.append(("Komedi", "komedi-dizi"))
    tarzlistesi.append(("Romantik", "romantik-dizi"))
    tarzlistesi.append(("Romantik Komedi", "romantik-komedi-dizi"))
    tarzlistesi.append(("Aksiyon - Macera", "aksiyon-macera-dizi"))
    tarzlistesi.append(("Gen�lik", "genclik-dizi"))
    tarzlistesi.append(("Polisiye", "polisiye-dizi"))
    tarzlistesi.append(("Dönem", "donem-dizi"))
    tarzlistesi.append(("Kült", "kult-dizi"))
    
    
                          
    for sTitle,Url in tarzlistesi:
        sUrl = "https://puhutv.com/api/slug/%s?s_page=1&s_per=40"%Url
        oOutputParameterHandler = cOutputParameterHandler()
       
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    sHosterUrl = sUrl
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()

def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []      
    liste.append( ['A',sUrl+'?harf=a'] )
    liste.append( ['B',sUrl+'?harf=b'] )
    liste.append( ['C',sUrl+'?harf=c'] )
    liste.append( ['Ç',sUrl+'?harf=ç'] )
    liste.append( ['D',sUrl+'?harf=d'] )
    liste.append( ['E',sUrl+'?harf=e'] )
    liste.append( ['F',sUrl+'?harf=f'] )
    liste.append( ['G',sUrl+'?harf=g'] )
    liste.append( ['H',sUrl+'?harf=h'] )
    liste.append( ['I',sUrl+'?harf=i'] )
    liste.append( ['İ',sUrl+'?harf=i'] )
    liste.append( ['J',sUrl+'?harf=j'] )
    liste.append( ['K',sUrl+'?harf=k'] )
    liste.append( ['L',sUrl+'?harf=l'] )
    liste.append( ['M',sUrl+'?harf=m'] )
    liste.append( ['N',sUrl+'?harf=n'] )
    liste.append( ['O',sUrl+'?harf=o'] )
    liste.append( ['�',sUrl+'?harf=ö'] )
    liste.append( ['P',sUrl+'?harf=p'] )
    liste.append( ['R',sUrl+'?harf=r'] )
    liste.append( ['S',sUrl+'?harf=s'] ) 
    liste.append( ['ş',sUrl+'?harf=ş'] ) 
    liste.append( ['T',sUrl+'?harf=t'] )
    liste.append( ['U',sUrl+'?harf=u'] )
    liste.append( ['Ü',sUrl+'?harf=�'] )
    liste.append( ['V',sUrl+'?harf=v'] )
    liste.append( ['W',sUrl+'?harf=w'] )
    liste.append( ['X',sUrl+'?harf=x'] )
    liste.append( ['Y',sUrl+'?harf=y'] )
    liste.append( ['Z',sUrl+'?harf=z'] )
    liste.append( ['0',sUrl+'?harf=0'] )
    liste.append( ['1',sUrl+'?harf=1'] )
    liste.append( ['2',sUrl+'?harf=2'] )
    liste.append( ['3',sUrl+'?harf=3'] )
    liste.append( ['4',sUrl+'?harf=4'] )
    liste.append( ['5',sUrl+'?harf=5'] )
    liste.append( ['6',sUrl+'?harf=6'] )
    liste.append( ['7',sUrl+'?harf=7'] )
    liste.append( ['8',sUrl+'?harf=8'] )
    liste.append( ['9',sUrl+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def showSinema(sSearch = ''):
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
        sPattern = '<div class="img">.*?<a href="(.*?)"><img data-original="(.*?)".*?<em title=".*?">(.*?)</em>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        



                                                                                                           	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '"display_name":"(.*?)","meta_title":".*?","meta_description":".*?","title_count":(.*?),"slug":".*?","slug_path":"(.*?)"'
                                 
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            
            sTitle = alfabekodla(aEntry[0])               
            sUrl = "https://puhutv.com/api/slug/%s?s_page=1&s_per=%s"  %( aEntry[2], aEntry[1])
            sPicture= "https://i0.wp.com/teknoyo.com/wp-content/uploads/2016/12/1482235728_puhutv_logo.png?w=767"
            #not found better way
            sTitle = unicode(sTitle, errors='replace')
            sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            sTitle = aEntry[0].decode("latin-1").encode("utf-8")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if 'Film' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'showshowSinema2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif 'Cocuk' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'COCUKshowshowSinema', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showshowSinema', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
     
    Pattern = '<a href="(/diziler?sw=.*?)">(.*?)</a>'
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
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showshowSinema2(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.replace('[{','').replace('},{',',')



                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                         
        sPattern = '}],"name":"(.*?)".*?"id":.*?,"director_name":".*?","slug_path":"(.*?)".*?"1080x608":"(.*?)"'
                            
            
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            
            sPicture = 'https://'+aEntry[2]
                        
          
            sTitle = alfabekodla(aEntry[0])            
            #not found better way
#            sTitle = unicode(sTitle, errors='replace')
            sUrl ='https://puhutv.com/api/slug/'+ str(aEntry[1])
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'FilmHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()


def COCUKshowshowSinema(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        Link = "https://puhutv.com/api/slug/%s?s_page=1&s_per=40"%Url
      
        url2 = base64.b64encode(Link)
    
        sUrl=TURKIYE+url2
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        



                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                       
        sPattern = '"960x369":"(.*?)".*?,"name":"(.*?)".*?"slug_path":"(.*?)"'
                                 
    
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            
            sPicture = 'https://'+aEntry[0]
                        
          
            sTitle = alfabekodla(aEntry[1])            
            #not found better way
#            sTitle = unicode(sTitle, errors='replace')
#            sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            sUrl = aEntry[2]
         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'COCUKsesionFilmHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)          
        
           
        if not sSearch:
            sNextPage =sEcho(str(Url))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def showshowSinema(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(Url)
        sHtmlContent = oRequestHandler.request()
        



                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                       
        sPattern = '"960x369":"(.*?)".*?}],"name":"(.*?)".*?"slug_path":"(.*?)"'
                                 
    
                                    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
  
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            
            sPicture = 'https://'+aEntry[0]
                        
          
            sTitle = alfabekodla(aEntry[1])            
                     
            
            URL = aEntry[2]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',str(URL))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
   
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:                               
                oGui.addMovie(SITE_IDENTIFIER, 'sesionFilmHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage =sEcho(str(Url))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def mmHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="keremiya_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)"><span>(.*?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'streams',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def COCUKsesionFilmHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    rUrl = 'https://puhutv.com/api/slug/'+Url
    oRequestHandler = cRequestHandler(rUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('}','<OTV>')
    oParser = cParser()
    sPattern = '"seasons"(.+?)"director"'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
    Pattern =  '"id":(.*?),"name":"(.*?)","position":(.*?)<OTV>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sUrl = 'https://puhutv.com/api/seasons/%s/episodes?e_page=1&e_per=24'   %( aEntry[0])                                              
            
            sTitle = aEntry[1]+' '+aEntry[2]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
            oGui.addTV(SITE_IDENTIFIER, 'cocukpageshowMovies',sTitle, '','genres.png', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def sesionFilmHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    rUrl = 'https://puhutv.com/api/slug/'+Url
    oRequestHandler = cRequestHandler(rUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('}','<OTV>')
    oParser = cParser()
    sPattern = '"seasons"(.+?)"director"'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                
    Pattern =  '"id":(.*?),"name":"(.*?)","position":(.*?)<OTV>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sUrl = 'https://puhutv.com/api/seasons/%s/episodes?e_page=1&e_per=24'   %( aEntry[0])                                              
            
            sTitle = aEntry[1]+' '+aEntry[2]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
            oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies',sTitle, '','genres.png', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def cocukpageshowMovies(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*? </em>.*?<em>(.*?)</em>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(Url)
        sHtmlContent = oRequestHandler.request()
        
                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                    
                     
        sPattern = ',"display_name":"(.*?)","slug":"(.*?)".*?"1080x608":"(.*?)"'
    
    sHtmlContent = sHtmlContent.replace('<br />','<OTV>')
    
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
           
            sTitle = aEntry[0]
            sTitle = alfabekodla(sTitle)
            sPicture = 'https://'+aEntry[2]
                
            sUrl ='https://puhutv.com/api/slug/'+ str(aEntry[1])+'-izle'
            
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'cocukHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage =sEcho(str(Url))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()


def cocukHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    referer=[('Referer',sUrl)]
    data=gegetUrl(sUrl,headers=referer) 
    chan = re.findall('"data":."id":(.*?),"uuid"', data, re.S)[0]
    
    Link='https://puhutv.com/api/assets/%s/videos'%(chan) 
    url2 = base64.b64encode(Link)
    
    Url=TURKIYE+url2
    
    oRequestHandler = cRequestHandler(Url)
    sHtmlContent = oRequestHandler.request()
    
    Pattern =  '"id":(.*?),"url":"(.*?.mp4.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
                                                          
            sThumbnail= "http://www.izleyiciplatformu.com/wp-content/uploads/2017/03/Puhu-TV-Nas%C4%B1l-izlenir-Puhu-Tv-Nereden-izleyebilirim-%C4%B0%C5%9Fte-Detaylar.png"

            sTitle = re.findall('.*?mp4/(.*?).mp4.*?',aEntry[1], re.S)[0]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showshowHosters',sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def pageshowMovies(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*? </em>.*?<em>(.*?)</em>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(Url)
        sHtmlContent = oRequestHandler.request()
        
                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                    
                     
        sPattern = ',"display_name":"(.*?)","slug":"(.*?)".*?"1080x608":"(.*?)"'
    
    sHtmlContent = sHtmlContent.replace('<br />','<OTV>')
    
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
           
            sTitle = cUtil().unescape(aEntry[0])
            sPicture = 'https://'+aEntry[2]
                
            sUrl ='https://puhutv.com/api/slug/'+ str(aEntry[1])+'-izle'
            
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage =sEcho(str(Url))
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()



def FilmHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sThumbnail = alfabekodla(sThumbnail)
        
                     
    referer=[('Referer',sUrl)]
    data=gegetUrl(sUrl,headers=referer) 
                       
    nack = re.findall(',"assets":.."id":(.*?),"name"', data, re.S)[0]
        
    rUrl = "https://puhutv.com/api/assets/%s/videos"%(nack)  
    
    referer=[('Referer',sUrl)]
    sHtmlContent =gegetUrl(rUrl,headers=referer) 

    
    Pattern =  '"id":(.*?),"url":"(.*?.mp4.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
                                                          
            
            sTitle = re.findall('.*?mp4/(.*?).mp4.*?',aEntry[1], re.S)[0]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showshowHosters',sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
                 
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sThumbnail = alfabekodla(sThumbnail)
        
                      
    referer=[('Referer',sUrl)]
    data=gegetUrl(sUrl,headers=referer) 
                       
    nack = re.findall('"data":."id":(.*?),"uuid"', data, re.S)[0]
        
    rUrl = "https://puhutv.com/api/assets/%s/videos"%(nack)  
    
    referer=[('Referer',sUrl)]
    sHtmlContent =gegetUrl(rUrl,headers=referer) 

    
    Pattern =  '"id":(.*?),"url":"(.*?.mp4.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
                                                          
            
            sTitle = re.findall('.*?mp4/(.*?).mp4.*?',aEntry[1], re.S)[0]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[1]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showshowHosters',sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showshowHosters():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
   
           
                
                          
        
    sHosterUrl = alfabekodla(sUrl) 
    sMovieTitle = alfabekodla(sMovieTitle) 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sMovieTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False
    oGui.setEndOfDirectory()

def kraltv():                      
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    data = data.replace("'",'"').replace('device.isWeb() ? "',' src: "')
    Ur = re.findall('src: "(.*?)"', data, re.S )
    if Ur:   
         
           for rack in Ur:    
               
                  sHosterUrl = rack
                  sTitle =alfabekodla(sTitle)
                  oGuiElement = cGuiElement()
                  oGuiElement.setSiteName(SITE_IDENTIFIER)
                  oGuiElement.setTitle(sTitle)
                  oGuiElement.setMediaUrl(sHosterUrl)
        

                  oPlayer = cPlayer()
                  oPlayer.clearPlayList()
                  oPlayer.addItemToPlaylist(oGuiElement)
                  oPlayer.startPlayer()  
    else: 
                  playlist = re.findall('data-player-token="(.*?)".*?data-player-mobile="(.*?)"', data, re.S)
                  for track,nack in playlist:
                         rac = "http:%s%s"  % (nack,track)  
              
                                 
                     
                         sHosterUrl = rac
                         sTitle =alfabekodla(sTitle)
                         oGuiElement = cGuiElement()
                         oGuiElement.setSiteName(SITE_IDENTIFIER)
                         oGuiElement.setTitle(sTitle)
                         oGuiElement.setMediaUrl(sHosterUrl)
        

                         oPlayer = cPlayer()
                         oPlayer.clearPlayList()
                         oPlayer.addItemToPlaylist(oGuiElement)
                         oPlayer.startPlayer()  
                         return False
  
def showshowHosters():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
   
           
                
                          
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

          
    sHosterUrl =sHosterUrl +TIK
    sMovieTitle = alfabekodla(sMovieTitle) 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sMovieTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False
    oGui.setEndOfDirectory()  