#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   
SITE_IDENTIFIER = 'ustream_tv'
SITE_NAME = 'Ustream'
SITE_DESC = 'Replay TV'
from random import randint                  
MOVIE_diziizle = 'http://www.diziizle.net/sinemalar/'
URL_MAIN = 'http://canlifm.com'
base = 'http://www.ustream.tv'
dev_key = 'D9B39696EF3F310EA840C3A8EFC8306D'

import urllib
import urllib2
import sys
import traceback
import time
try: import json
except Exception: import simplejson as json 
from random import randint
def make_request(url):
        try:
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest', 'Content-Length': '26'}
            Headers = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4,tr;q=0.2',
            'Connection':'keep-alive',
            'Cookie':'demographics=1a28fbc7c674c0b994d22639b1e5b881e3QDAAAAYWdlaSoAAAB0BgAAAGdlbmRlcnQBAAAAbTA=; __utma=27069237.1446999061.1401292467.1403714634.1403720644.3; __utmz=27069237.1401292467.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); GEUP=f65a8bbb0046458bf8b3a2730415f135aesHAAA=; dkv=cbf351699ea59a6fffe3dc61a190e131e3QEAAAAdGxpcGn2+LdTMA==; a_Pnz.resume=; PREF=al=de&fv=14.0.0&f1=50000000&f5=30; VISITOR_INFO1_LIVE=NoLV7PrCC84; SID=DQAAAAoBAAAenFdjG-lHU8zC2C81qlQkr-CqRnoMhqDgsQhEzYVfpyAJbL66CJb6GPkK1LESvN2fk3WbRSySrzETfFBblESGT1zhvRiMjPWVmGMsPyaM2Ubc0HVGrZfKU1LNF3trlIgMkZ2JgdOFxEvywT8KEZ-6Uf4dEp2SjrpDjeQsYSPLChOil5aJEYloN99Covu6dopWvFJZ1GXEq1qNCwTPmtUJ4UJrM_yGleLI4ss3b1ofwj-Hu8Hl5tqBNsDCZ_LuDWoVEJnBGqBaP73LQBH5XD-ia7ZJMyQIKQF3Kz-Cn_KocavJc7Q-Dw2IJqZ_hm74kuyIW9fDekLMkogWvoHZxjKqRnei76uxhJv4eiKxSUb6og; HSID=ANl0O9nSOhgPyDr2S; SSID=AJlmav1amgHOd5c3T; APISID=9dyCTocrLMS263Pm/AxSz5xTOw6rwlieSo; SAPISID=GXxuhIJweus4DHFt/A4yDGozdOTud4MKEX; YSC=2ZwzJysyyQE; LOGIN_INFO=2f6d86c4fc1e290d454d5cf78ffbd02dc2oAAAB7IjgiOiAxNjU2NjY0NDMxOTksICI0IjogIkdBSUEiLCAiNyI6IDE0MDY2NDEzMjksICIxIjogMSwgIjMiOiA1NDIwMjY0MDksICIyIjogIlQ3UVNXblNjNy1PRGxRZGZUV1Z4ZUE9PSJ9  ',
            'Host':'www.ustream.tv',
            'Referer':'http://www.ustream.tv',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'} 

            req = urllib2.Request(url,None,Headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            
           
            if hasattr(e, 'code'):
                
                xbmc.executebuiltin("XBMC.Notification(Ustream,HTTP ERROR: "+str(e.code)+",5000)")


RADYO_GENRES = (True, 'showGenre')
Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
Player_User_Agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
  
URL_SEARCH = ('', 'showMovies')
def load():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/') 
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler) 
    
    #rajout listage film nouveauté   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films Nouveautés', 'news.png', oOutputParameterHandler)
  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIE[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIE[1], 'Films', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films Genres', 'genres.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'DIZILER-harfler', 'series.png', oOutputParameterHandler)
            
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
    
def Ustream():
    oGui = cGui()
    tarzlistesi= []
    tarzlistesi.append(("Search","http://www.ustream.tv/search?q=%s/all.json"))
    tarzlistesi.append(("Animals","https://www.ustream.tv/ajax-alwayscache/explore/pets-animals/all.json"))
    tarzlistesi.append(("All","https://www.ustream.tv/ajax-alwayscache/explore/all.json"))
    tarzlistesi.append(("News","https://www.ustream.tv/ajax-alwayscache/explore/news/all.json"))
    tarzlistesi.append(("Entertainment","https://www.ustream.tv/ajax-alwayscache/explore/entertainment/all.json"))
    tarzlistesi.append(("Sports","https://www.ustream.tv/ajax-alwayscache/explore/sports/all.json"))
    tarzlistesi.append(("Spirituality/All","https://www.ustream.tv/ajax-alwayscache/explore/spirituality/all.json"))
    tarzlistesi.append(("Music","https://www.ustream.tv/ajax-alwayscache/explore/music/all.json"))
    tarzlistesi.append(("Technology","https://www.ustream.tv/ajax-alwayscache/explore/technology/all.json"))
    tarzlistesi.append(("education","https://www.ustream.tv/ajax-alwayscache/explore/education/all.json"))
    tarzlistesi.append(("24-7/All","https://www.ustream.tv/ajax-alwayscache/explore/24-7/all.json"))
                     
    for sTitle,sUrl2 in tarzlistesi:
        sTitle =  alfabekodla(sTitle)   
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oGui.addDir(SITE_IDENTIFIER, 'top20radyo',  sTitle, 'genres.png', oOutputParameterHandler)      
                    
    oGui.setEndOfDirectory()
def top20radyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')

    
    
    urla  = "http://www.ustream.tv/"
                
    referer=[('Referer',urla)]                                                                                     

    data=gegetUrl(sUrl,headers=referer) 
    data = data.replace('<', ' <').replace('\\n', ' ').replace('\\r', ' ').replace('\\t', ' ').replace('\\','')
    
    channels=re.findall('<img src="(.*?)"  alt="(.*?)" width=".*?" height=".*?"/>.*?data-content-id="(.*?)"', data, re.S)
            
    for sPicture,sTitle,Url in channels:
            
            sTitle =  alfabekodla(sTitle)
                        
                    
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'getLink', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()    

def getLink():
    oGui = cGui()
    referer='http://www.ustream.tv'
   
    oInputParameterHandler = cInputParameterHandler()
    mediaId = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    sTitle = alfabekodla(sTitle)
    WS_URL = "http://r{0}-1-{1}-{2}-{3}.ums.ustream.tv"

    rsid = "{0:x}:{1:x}".format(randint(0, 1e10), randint(0, 1e10))
    rpin = "_rpin.{0:x}".format(randint(0, 1e15))
    
    apiUrl = WS_URL.format(randint(0, 0xffffff), mediaId, 'channel', 'lp-live') + '/1/ustream'
    url = apiUrl + '?' + urllib.urlencode([('media', mediaId), ('referrer', referer), ('appVersion', 2), ('application', 'channel'), ('rsid', rsid), ('appId', 11), ('rpin', rpin), ('type', 'viewer') ])
    
    params = {'Referer':'http://www.ustream.tv', 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'}
    data = getPage(url, params)
    
    
    data = json.loads(data)
    host = data[0]['args'][0]['host'].encode('utf-8')
    connectionId = data[0]['args'][0]['connectionId']
    if len(host):
        apiUrl = "http://" + host + '/1/ustream'
    url = apiUrl + '?connectionId=' + str(connectionId)
    
    for i in range(5):
        data = getPage(url, params)
       
        if 'm3u8' in data:
            break
        time.sleep(1)
    data = json.loads(data)
    playlistUrl = data[0]['args'][0]['stream'][0]['url'].encode('utf-8')
    
    urlk = getPage(playlistUrl, params)
    channels= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=.*?,CODECS=".*?",RESOLUTION=(.*?),BANDWIDTH=.*?\n(.*?)\n', urlk, re.S)
    for sTitle,Url in channels:
            
            sTitle =  alfabekodla(sTitle)
                        
                    
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'showtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

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

   

   
def get_hls(url):
        data = make_request(url)
        sHosterUrl= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=.*?,CODECS=".*?",RESOLUTION=.*?,BANDWIDTH=.*?\n(.*?)\n', data, re.S)

        streams = re.findall(pattern, data)
        if streams:
            best = 0
            for bandwidth, stream_url in streams:
                if int(bandwidth) > best:
                    best = int(bandwidth)
                    playurl = stream_url
            return playurl
        else:
            addon_log('hls resolved url: %s' %url)
            return url

def getPage(url, params={}):
    
    
    try:
        req = urllib2.Request(url)
        if 'Referer' in params:
            req.add_header('Referer', params['Referer'])
        if 'User-Agent' in params:
            req.add_header('User-Agent', params['User-Agent'])
        resp = urllib2.urlopen(req)
        data = resp.read()
        
    except Exception:
        printExc()
    return  data
    
def showtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                             
    
     
    
    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
    sHosterUrl= Url + '|' + Header 
    name=  alfabekodla(sTitle) 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
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

