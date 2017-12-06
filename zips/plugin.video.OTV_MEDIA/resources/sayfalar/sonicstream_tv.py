#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   
SITE_IDENTIFIER = 'sonicstream_tv'
SITE_NAME = 'limanbet12.com'
SITE_DESC = 'Replay TV'
SPORT_SPORTS = (True, 'showGenre')                    
from resources.sayfalar.youtubecom_tr import youtubeplayer 
import time
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

def mediaHeaders(chann):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13','Referer':'https://edge.ambelbet.com/' ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        #sSearchText = cUtil().urlEncode(sSearchText)
        sUrl = URL_SEARCH[0] + sSearchText+'/'
 
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return  
url = 'https://www.youtube.com/watch?v=9Q2k4sHRxNM'
url2 = base64.b64encode(url)
    
Urlturk=TURKIYE+url2  
def sonicGenre():
    oGui = cGui()
    liste = []
    liste.append( ['SPORT mix ALL','tab0'] )
    liste.append( ['7/24 Türk TV ve SPOR','tab3'] )
    liste.append( ['Futbol','tab1'] )
    liste.append( ['Basketbol','tab2'] )
    liste.append( ['Tenis','tab4'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24 Türk TV ve SPOR':
             oGui.addDir(SITE_IDENTIFIER, 'BBBsonicHosters',  sTitle, 'genres.png', oOutputParameterHandler)
        else:    
             oGui.addDir(SITE_IDENTIFIER, 'BsonicHosters', sTitle, 'genres.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()
               
def BBBsonicHosters():               
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=200') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Beinsport', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.ucaster.me/hembedplayer/futboltvsite50/1/750/500') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport')
    oGui.addDir(SITE_IDENTIFIER, 'ligtvchannel1', 'Beinsport', 'search.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://macyayiniajanspor.us/ts/lig-2449118077-0%s.svgz') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport')
    oGui.addDir(SITE_IDENTIFIER, 'bein2', 'Beinsport', 'search.png', oOutputParameterHandler) 
    
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://nowwatchtvlive.cc/channel-tab-frame/ligtvchannel-5.php') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport')
    oGui.addDir(SITE_IDENTIFIER, 'ligtvchannel', 'Beinsport', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=201') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport1')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Beinsport1', 'search.png', oOutputParameterHandler) 
                                                  
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=202') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport2')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Beinsport2', 'search.png', oOutputParameterHandler) 
                                                    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=203') 
    oOutputParameterHandler.addParameter('sMovieTitle','Beinsport3')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Beinsport3', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', Urlturk) 
    oOutputParameterHandler.addParameter('sMovieTitle','Tivibu spor')
    oGui.addDir(SITE_IDENTIFIER, 'youtubeplayer2', 'Tivibu spor', 'search.png', oOutputParameterHandler) 

    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=63244') 
    oOutputParameterHandler.addParameter('sMovieTitle','Tivibu spor2')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Tivibu spor2', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=63245') 
    oOutputParameterHandler.addParameter('sMovieTitle','Tivibu spor3')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Tivibu spor3', 'search.png', oOutputParameterHandler) 
                                                  
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=63240') 
    oOutputParameterHandler.addParameter('sMovieTitle','Smartspor')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Smartspor', 'search.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=63241') 
    oOutputParameterHandler.addParameter('sMovieTitle','SSpor')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'SSpor', 'search.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', '?id=63239') 
    oOutputParameterHandler.addParameter('sMovieTitle','Eurosport 2')
    oGui.addDir(SITE_IDENTIFIER, 'sshowBox4', 'Eurosport 2', 'search.png', oOutputParameterHandler) 

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
     
    Urlo = "http://sonicstream.tv/App/lmn.php" 
    oRequestHandler = cRequestHandler(Urlo )
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div id=\'%s\''%sUrl+' class="tabBox.*?>(.*?)<div id='
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="listType.*?><a href="(.*?)" title="(.*?)">.*?<img src="(.*?)">.*?<div class="listFlag">(.*?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = "%s - %s" %(aEntry[1],aEntry[3]) 
            sTitle = alfabekodla(sTitle)
            sThumbnail=aEntry[2]
            Url=aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox4',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def BsonicHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
     
    Urlo = "http://sonicstream.tv/App/lmn.php" 
    oRequestHandler = cRequestHandler(Urlo )
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace("<span style='color:Red;'>","").replace("</span>","")  
    oParser = cParser()
    sPattern = '<div id=\'%s\''%sUrl+' class="tabBox.*?>(.*?)<div id='
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    
    sPattern = '<div class="listType".*?<a href="(.*?)" title=".*?">.*?<img src="(.*?)">.*?<div class="listFlag">(.*?)</div><div class="listMatch">(.*?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sThumbnail=aEntry[2]
            Url=aEntry[0]
            sTitle = "%s - %s" %(aEntry[3],aEntry[2]) 
            
            sTitle = alfabekodla(sTitle)
            if "(CANLI)" in sTitle:
               sTitle =  '[COLOR lime]'+sTitle+'[/COLOR]'
               sThumbnail= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox4',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def msshowBox3():
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

def ligtvchannel1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urlk = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url =  'http://futboltv.site/channel/ch1.html'
    
           
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    referer=[('Referer',Url)]
    adat=gegetUrl(Urlk,headers=referer) 
    kene='http://www.pubucaster.com:1935/loadbalancer?94184'
    ea= requests.get(kene).content
    ea = ea.replace('redirect=',"")                          
    ken = re.findall('enableVideo."(.*?)"',adat, re.S)[0]
    url = "http://" + ea + ":8088/live/futboltvsite50/playlist.m3u8?id=94184&pk=" + ken
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
        
    url= url+ '|' + Header
    sshowBox3(url,name)                                  
    return


def ligtvchannel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url =  alfabekodla(Url)
    
    
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    referer=[('Referer',Url)]
    adat=gegetUrl(Url,headers=referer) 
    
    keno = re.findall('<!-- Player Code -->.*?<script type="text/javascript" src="(.*?)"></script>',adat, re.S)[0]
         
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
   
    referer=[('Referer',Url)]
    dat=gegetUrl(keno,headers=referer) 
    
    ken = re.findall('<iframe src="(.*?)"',dat, re.S)[0]
    sPicture='http://s1.peers.tv/i/ptv/logo.png'                    
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    datan= requests.get(ken).content
    Hoster = re.findall('<input type="hidden" id=".*?" value="" />.*?<input type="hidden" id=".*?" value=".*?" />.*?<input type="hidden" id=".*?" value="(.*?)" />', datan, re.S)
    for fid in Hoster:          
            bit=base64.b64decode(fid)         
            bim=base64.b64decode(bit)
            sUrl=base64.b64decode(bim)
            TIK='Referer=http://api.peer5.com/jwplayer6/assets/flashls.provider.swf'

            url = sUrl +'|'+TIK                       
            sshowBox3(url,name)


def Bsonicstream(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
      
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
            
    
    
    channels=re.findall('<div class="listType" >.*?<a href="(.*?)" title="(.*?)">.*?<img src="(.*?)">.*?<div class="listFlag">(.*?)</div>', sHtmlContent, re.S)
        
    for Link,sTitle,sPicture,saat in channels:
            
            sTitle =  alfabekodla(sTitle)
            Title = "%s - %s" %(sTitle,saat)         
    
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox4', Title, sPicture, sPicture, '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory() 
    
def sshowBox4():
 
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
#    import random
#    import math   
   
    
    
#    rand = items[math.floor(random.random() * items = ['1','2','3','4','5','6','7','8','9'])];
#    rtmpDomain = rand+".futcast11.pro:1935";

    url = "http://sonicstream.tv/App/lmn.php"+sUrl                                              
    Urlom  = "http://sonicstream.tv/"                                                                                           
    Agent=[('Referer',Urlom )] 
    
    
    data = gegetUrl(url,headers=Agent)  
    channels = re.findall('data=".*?secury=(.*?)&serverID=(.*?)&getChannel=(.*?)&.*?"', data, re.S)                                    
    for secury,serverID,getChannel in channels:              
	                                                                           
        TIK='Referer=http://sonicstream.tv/App/PlayerL.swf'
        Header = 'User-Agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13'
#        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
         
        
#        sHosterUrl = 'rtmp://'+serverID+'.futcast11.pro:1935/edge/?'+secury+' playpath=ch'+getChannel+' swfUrl=http://netspor20.tv/assets/rtmpPlayer.swf?id=1 pageUrl=http://netspor20.tv/embed/index.html?flashVer=WIN\\2023,0,0,205'
        chann = 'https://edge.ambelbet.com/edge/'+getChannel+'/playlist.m3u8'
        url=mediaHeaders(chann)+ '|' + Header
        sshowBox3(url,name)                                  
        return



def ligtvchannel():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    Url =  alfabekodla(Url)
    
    
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    referer=[('Referer',Url)]
    adat=gegetUrl(Url,headers=referer) 
    
    keno = re.findall('<!-- Player Code -->.*?<script type="text/javascript" src="(.*?)"></script>',adat, re.S)[0]
         
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
   
    referer=[('Referer',Url)]
    dat=gegetUrl(keno,headers=referer) 
    
    ken = re.findall('<iframe src="(.*?)"',dat, re.S)[0]
    sPicture='http://s1.peers.tv/i/ptv/logo.png'                    
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    datan= requests.get(ken).content
    Hoster = re.findall('<input type="hidden" id=".*?" value="" />.*?<input type="hidden" id=".*?" value=".*?" />.*?<input type="hidden" id=".*?" value="(.*?)" />', datan, re.S)
    for fid in Hoster:          
            bit=base64.b64decode(fid)         
            bim=base64.b64decode(bit)
            sUrl=base64.b64decode(bim)
            TIK='Referer=http://api.peer5.com/jwplayer6/assets/flashls.provider.swf'

            url = sUrl +'|'+TIK                       
            sshowBox3(url,name)



def msshowBox4():
 
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
#    import random
#    import math   
   
    
    
#    rand = items[math.floor(random.random() * items = ['1','2','3','4','5','6','7','8','9'])];
#    rtmpDomain = rand+".futcast11.pro:1935";

    url = "http://sonicstream.tv/App/lmn.php"+sUrl                                              
    Urlom  = "http://sonicstream.tv/"                                                                                           
    Agent=[('Referer',Urlom )] 
    
    
    data = gegetUrl(url,headers=Agent)  
    channels = re.findall('data=".*?secury=(.*?)&serverID=(.*?)&getChannel=(.*?)&.*?"', data, re.S)                                    
    for secury,serverID,getChannel in channels:              
	                                                                           
        TIK='Referer=http://sonicstream.tv/App/PlayerL.swf'
        Header = 'User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X)'
 

        sHosterUrl = 'rtmp://'+serverID+'.futcast11.pro:1935/edge/?'+secury+' playpath=ch'+getChannel+' swfUrl=http://sonicstream.tv/App/PlayerL.swf pageUrl=http://sonicstream.tv/'
#        playlist = 'http://'+serverID+'.streamgo1.stream:1935/edge/ch'+getChannel+'/playlist.m3u8?'+secury+'|' +Header
        sTitle = alfabekodla(sTitle)
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()                                   





def msshowBox3():
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
         
def sshowBox3(url,name):
   
    name = alfabekodla(name)
    
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
    progress.update( 20, "", 'Loading local proxy', "" )
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
 
     