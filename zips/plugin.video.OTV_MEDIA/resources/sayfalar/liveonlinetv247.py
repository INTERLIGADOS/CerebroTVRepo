#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   

from livescore import futbolozet
from sport365 import mainlist
from resources.lib.httpkir import scrapertools
from sonicstream_tv import sonicGenre,sshowBox4
from resources.lib import common

from sport365 import mainlist
SITE_IDENTIFIER = 'liveonlinetv247'
SITE_NAME = 'liveonlinetv247'

SITE_DESC = 'Replay TV'
UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69'    
Player_User_Agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
SPORT_SPORTS = (True, 'liveonlinetv247')
def _downloadUrl(url):
        headers = {'User-Agent': UA ,
                   #'Host' : 'hqq.tv',
                   'Referer': 'https://ajanspor7.tv',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   #'Accept-Encoding':'gzip, deflate, br',
                   #'Content-Type': 'text/html; charset=utf-8'
                   }
        
        req = urllib2.Request(url,None,headers)

        response = urllib2.urlopen(req)
        html = response.read()
        response.close()

        return  html

def MediaHeaders(chann,cookie,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                                    
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'Cookie':cookie,'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4; Nexus 7 Build/KRT16M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.92 Safari/537.36','Referer':ref ,'X-Requested-With': 'ShockwaveFlash/27.0.0.183',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann  

def mediaHeaders(chann,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)','Referer':ref ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann  
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

def Sport():             
    oGui = cGui()
    liste = []
    liste.append( ['SPOR TV Türk','http://www.golnet.tv/tr/izle/bein-sport-2'] )
    liste.append( ['sport365','http://vegoltv2.com/canli-mac-izle/bein-sports-hd-1/'] )
    liste.append( ['TV + SPORT TV int [HQ] channels','http://saraydorf.de/spor/index.html'] )
    liste.append( ['TV + SPORT TV int','http://www.liveonlinetv247.info/tvchannels.php'] )
    liste.append( ['Golnet.TV.TR','http://www.golnet.tv/tr/izle/bein-sport-2'] )
    liste.append( ['betexpertv.com.TV.TR','http://www.betexpertv.com/'] )
    liste.append( ['xscorestv.TV.TR','http://www.xscorestv.com/'] )
    liste.append( ['TürkTV+SPORT int','http://saraydorf.de/spor/index.html'] )
    #    liste.append( ['Show Sport TV','http://showsport-tv.com/channel/watch-bein-sport-2-live-online.html'] )
    liste.append( ['WORLD FUTBOOL Live Scores  Özet','http://saraydorf.de/spor/index.html'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'WORLD FUTBOOL Live Scores  Özet':
             oGui.addDir(SITE_IDENTIFIER, 'futbolozet','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV + SPORT TV int':
             oGui.addDir(SITE_IDENTIFIER, 'liveonlinetv247','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'BELGESELLER-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'futbolozet','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TürkTV+SPORT int':
             oGui.addDir(SITE_IDENTIFIER, 'sonicGenre','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Show Sport TV':
             oGui.addDir(SITE_IDENTIFIER, 'showsport','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'Golnet.TV.TR':
             oGui.addDir(SITE_IDENTIFIER, 'golnettv','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'betexpertv.com.TV.TR':
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'xscorestv.TV.TR':
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'SPOR TV Türk':
             oGui.addDir(SITE_IDENTIFIER, 'sporHosters','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'TV + SPORT TV int [HQ] channels':
             oGui.addDir(SITE_IDENTIFIER, 'livemobiletv247','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        

        elif sTitle == 'sport365':
             oGui.addDir(SITE_IDENTIFIER, 'mainlist','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
       
        else:
             oGui.addDir(SITE_IDENTIFIER, 'saraydorf', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def livemobiletv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = url_all_products
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('\/','/')                                                                                                   
    oParser = cParser()
    sPattern = '"id":"(.*?)","category":"(.*?)","channel_name":"(.*?)","channel_link":"(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            id =aEntry[0]
            surl =aEntry[3]
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            if  'NSFW'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'pincode', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Scores'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'mainlist', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'Schedule'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'schedulelivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)        
            elif 'More Channels'in sTitle:
               oGui.addTV(SITE_IDENTIFIER, 'MoreChannels', sTitle, '',img, '', oOutputParameterHandler)        

            else:
               oGui.addTV(SITE_IDENTIFIER, 'HOSTlivemobiletv247', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()   
def MoreChannels():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                
    oParser = cParser()
    sPattern = '<li><a href="(.*?php)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            sTitle = aEntry[1]
          
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'MoreMoreChannels', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def schedulelivemobiletv247():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                 
    oParser = cParser()
    sPattern = 'datetime="(.*?)">(.*?)</time>.*?<div class="entry-content">.*?<p>(.*?)<a href="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[3]
            sTitle = aEntry[2]+ ' :'+ 'Schedule Timezone: Europe/London :'+ aEntry[0]+ ' :'+ aEntry[1] 
            img ='http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'play__liveonlinetv24', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def MoreMoreChannels():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                
    oParser = cParser()
    sPattern = '<li><a href="(.*?php)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            sTitle = aEntry[1]
          
            
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'HOSTlivemobiletv247', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def HOSTlivemobiletv247():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':sUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    sHtmlContent = requests.get(sUrl, headers = headers).text
    
                 
    oParser = cParser()
    sPattern = '<li><a target="_top" href="(.*?)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            img ='http://pic.accessify.com/thumbnails/777x423/l/liveonlinetv247.com.png'
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__livemobiletv247', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()

def play__livemobiletv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    name = alfabekodla(sTitle)
    
                              
                     
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':Url, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text               
    urll = re.findall('src=.*[",\'](.*m3u8.*?)[",\']', data, re.S)[0]  
    sUrlkk  =mediaHeaders(urll,Url)
    url =sUrlkk+'|Referer='+Url+'&User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
    
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
def vegoltv2():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<div class="active in tab-pane" id="t-5-7-24-tv">(.+?)</tbody'
               
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                 
    oParser = cParser()
    sPattern = '<td><a href="(.*?)" title="(.*?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='http://vegoltv2.com'+ aEntry[0]
            img ='http://vegoltv2.com/wp-content/uploads/2017/08/vegoltv-logo.png'
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__vegoltv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__vegoltv2():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    urla  = "http://vegoltv2.com/"
    name = oInputParameterHandler.getValue('sMovieTitle')                  
    referer=[('Referer',urla)]
    datam=gegetUrl(sUrl,headers=referer) 
  
    sUrll= re.findall('<iframe allowfullscreen class="embed-responsive-item" src="(.*?)"></iframe>', datam, re.S)[0]   
    sUrlkk='http://vegoltv2.com'+ sUrll 
    tam=gegetUrl(sUrlkk,headers=referer)     
    url= re.findall('poster:".*?",source:"(.*?)"', tam, re.S)[0]
    url =url+'|Referer='+sUrlkk+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    
    
   
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')


def betexpertv():
    oGui = cGui()
    liste = []
    liste.append( ['7/24 Canli TV','item live'] )
    liste.append( ['FUTBOL','item football'] )
    liste.append( ['BASKETBOL','item basketball'] )
    liste.append( ['TENIS','item tennis'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24 Canli TV':
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv3',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'betexpertv2', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def golnettv():
    oGui = cGui()
    liste = []
    liste.append( ['7/24 Canli TV','item live'] )
    liste.append( ['FUTBOL','item football'] )
    liste.append( ['BASKETBOL','item basketball'] )
    liste.append( ['TENIS','item tennis'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24 Canli TV':
             oGui.addDir(SITE_IDENTIFIER, 'golnettv3',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'golnettv2', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def laklak(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku  
def betexpertv3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.betexpertv.com/'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="live">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.betexpertv.com/assets/uploads/settings/main_logo_739.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__betexpertv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()     
def betexpertv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.betexpertv.com/'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="time">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                              
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.betexpertv.com/assets/uploads/settings/main_logo_739.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__betexpertv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__betexpertv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urlk='http://www.betexpertv.com/'
    Urll='http://www.betexpertv.com/tr/izle/'+ Url
    referer=[('Referer',Urlk)]
    adata=gegetUrl(Urll,headers=referer) 
    fida= re.findall('<iframe src="(.*?)"',adata, re.S)[0]
                    
    referer=[('Referer',fida)]
    adat=gegetUrl(fida,headers=referer) 
    if not '<script>eval' in adat:
        sUrl="http://www.betexpertv.com/assets/images/nosignal.jpg"
    fid= re.findall('<script>eval.atob."(.*?)"',adat, re.S)[0]
    
    bit=base64.b64decode(fid)     
   
    sUrlk = re.findall('",source:"(.*?)",',bit, re.S)[0]   
    sUrl =sUrlk+'|Referer='+Urll+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()

def golnettv3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.golnet.tv/tr/izle/bein-sport-2'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="live">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.golnet.tv/assets/uploads/settings/main_logo_660.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__golnettv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()     
def golnettv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'http://www.golnet.tv/tr/izle/bein-sport-2'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()
    sPattern = '<div class="'+item+'">.*?<a href="http://.*?/tr/izle/(.*?)" title="(.*?)">.*?<span class="time">(.*?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                              
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl =aEntry[0]
            
            sTitle = aEntry[1]+ ' :'+ aEntry[2]
            sTitle = alfabekodla(sTitle)
            img = 'http://www.golnet.tv/assets/uploads/settings/main_logo_660.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'play__golnettv2', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def play__golnettv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urlk='http://www.golnet.tv/'
   
    Urll='http://www.golnet.tv/tr/izle/'+ Url
    referer=[('Referer',Urlk)]
    adata=gegetUrl(Urll,headers=referer) 
    fida= re.findall('<iframe src="(.*?)"',adata, re.S)[0]
                    
    referer=[('Referer',fida)]
    adat=gegetUrl(fida,headers=referer) 
    if not '<script>eval' in adat:
        sUrl="http://www.golnet.tv/assets/images/nosignal.jpg"
    fid= re.findall('<script>eval.atob."(.*?)"',adat, re.S)[0]
    bit=base64.b64decode(fid)     
   
    sUrlk = re.findall('",source:"(.*?)",',bit, re.S)[0]   
    sUrl =sUrlk+'|Referer='+fida+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  


def showsport():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.hdfilmcehennemi.com/')
    oGui.addDir(SITE_IDENTIFIER, 'showsportSchedule', 'Schedule', 'genres.png', oOutputParameterHandler)

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()                          
    sPattern = '<a href="(/channel/watch.*?)"><img width="120" title="(.*?)" src="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='http://showsport-tv.com'+ aEntry[0]
            img ='http://showsport-tv.com'+ aEntry[2]
            sTitle = aEntry[1]
            sTitle = alfabekodla(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addTV(SITE_IDENTIFIER, 'pplay__showsport', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory()
def showsportSchedule():
    oGui = cGui()
         
    Urlo = "http://showsport-tv.com/" 
    oRequestHandler = cRequestHandler(Urlo )
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =sHtmlContent.replace('<div class="startdate date"','<img src="/img/Sonra.gif">')
    oParser = cParser()
    sPattern = '<div class="table-responsive">(.*?)</table>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult

                                                             
    sPattern = '<img width="20" title=".*?" src="(.*?)".*?class="time">(.*?)</span>.*?<td width="20"><a class="btn btn-success btn-xs" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):                                     
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sThumbnail= "http://showsport-tv.com" +aEntry[0]
            Url="http://showsport-tv.com" +aEntry[2]
                                
            name= re.findall('/live/(.*?).html',aEntry[2])[0]
            sTitle = "%s - %s" %(name,aEntry[1]) 
            
            sTitle = alfabekodla(sTitle)
            if "live" in sTitle:
               sTitle =  '[COLOR  lime]'+sTitle+'[/COLOR]'
               sThumbnail= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'pplay__showsport',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()



def pplay__showsport():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    datam=gegetUrl(sUrl,headers=referer) 
    sUrll=re.findall('<div id="ch_box" class="tab-content">.*?<iframe src="(/embedplayer.php.*?)&server=.*?"', datam, re.S)[0]   
    urll='http://showsport-tv.com'+ sUrll                                            
        
      
    liste = []
    liste.append( ['Server 1',urll+'&server=1'] )
    liste.append( ['Server 2',urll+'&server=2'] )
   
    for sTitle,sUrl2 in liste:
        sTitle = alfabekodla(sTitle)   
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Server 2':
             oGui.addDir(SITE_IDENTIFIER, 'playshowsport',sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'play__showsport', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def playshowsport():
    oGui = cGui()
              
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    name = oInputParameterHandler.getValue('sMovieTitle')  
    name = alfabekodla(name)
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    tam=requests.get(sUrl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04','Referer':sUrl,'Accept':'/*','Connection':'keep-alive'}).text
   
    Urll= re.findall("<script type='text/javascript'>id='(.*?)'", tam, re.S)[0]
    ref='http://bro.adca.st/stream.php?id='+ Urll    
    data=gegetUrl(ref,headers=referer)  
    tokenLink = re.findall('fass = "(.*?)"', data, re.S)[0]
    if  'token2.php' in tokenLink: 
          Link = re.findall('trap2 = "(.*?)"', data, re.S)[0] 
    
    if  'token.php' in tokenLink:
          Link = re.findall('trap = "(.*?)"', data, re.S)[0] 
    
    
    tokenurl='http://bro.adca.st/'+tokenLink+'?id='+ Urll 
    urlan=gegetUrl(tokenurl,headers=referer) 
    token = re.findall('"rumba":"(.*?)"',urlan, re.S)[0]
    
    
    
    urll = base64.b64decode(Link)
    sUrlkk  =mediaHeaders(urll,ref)
    url =sUrlkk+token+'|Referer='+ref+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
     

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

def play__showsport():
    oGui = cGui()
              
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl') 
    name = oInputParameterHandler.getValue('sMovieTitle')  
    name = alfabekodla(name)
    urla  = "http://showsport-tv.com/"
    referer=[('Referer',urla)]
    tam=requests.get(sUrl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04','Referer':sUrl,'Accept':'/*','Connection':'keep-alive'}).text
   
    Urll= re.findall("<script type='text/javascript'>id='(.*?)'", tam, re.S)[0]
    ref='http://www.allcast.is/stream.php?id='+ Urll    
    data=gegetUrl(ref,headers=referer)  
                  
    Link = re.findall('curl = "(.*?)"', data, re.S)[0] 
    urll = base64.b64decode(Link)
    sUrlkk  =mediaHeaders(urll,ref)
    url =sUrlkk+'|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
    

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

def liveonlinetv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.liveonlinetv247.info/tvchannels.php'
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
                
            sTitle = aEntry[1].replace('<b>','')
            surl ='http://www.liveonlinetv247.info'+ aEntry[0]
            surl =surl.replace(' ','%20')
            sDisplayTitle = cUtil().DecoTitle(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDirectTV(SITE_IDENTIFIER, 'play__liveonlinetv24', sDisplayTitle, 'libretv.png' , '', oOutputParameterHandler)    
        
        cConfig().finishDialog(dialog)
        
        oGui.setEndOfDirectory()

def play__liveonlinetv24():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    name = alfabekodla(sTitle)
    
                              
 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':urll, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    datam = requests.get(urll, headers = headers).text
    Ur= re.findall('style="color:white">.*?<p><a href="(https://www.liveonlinetv247.info/.*?.php)"', datam, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer': Ur, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    tam = requests.get(Ur, headers = headers).text
    Url= re.findall('<p><iframe src="(.*?)"', tam, re.S)[0]
                    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0', 'Referer':Url, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    data = requests.get(Url, headers = headers).text               
    urll = re.findall('src=.*[",\'](.*m3u8.*?)[",\']', data, re.S)[0]  
    sUrlkk  =mediaHeaders(urll,Url)
    url =sUrlkk+'|Referer='+Url+'&User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
    
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


    
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="film_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?.html.*?)"><span>(.*?)</span></a>'
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
            oGui.addTV(SITE_IDENTIFIER, 'streams', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    
def sshowBox5():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
                                               
        
    resp = net.http_GET(url)
    data = resp.content	                
    data =data.replace('\n','')
    channels = re.findall('<video controls height="480" width="650" src="(.*?)"', data, re.S)                                    
    for sUrl in channels:              
	                                                                           
                        
            sThumbnail ='http://www.liveonlinetv247.info/images/livesports.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showotvplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)

       

    oGui.setEndOfDirectory()
 
def sporHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="spor">(.+?)<div class="sporson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
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
            Thumbnail ='https://www.ulantv.com/'+ aEntry[2]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def turktvHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="turktv">(.+?)<div class="turktvson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
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
            Thumbnail =aEntry[2]
            if not 'http' in Thumbnail:
                 Thumbnail ='https://www.ulantv.com/'+ Thumbnail
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            if  '?id=' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'sshowBox4', sTitle, '', Thumbnail, '', oOutputParameterHandler)
       
            else:

                 oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def Almanlivestream(): #affiche les genres
    oGui = cGui()              
    tarzlistesi= []                
    tarzlistesi.append(("Sky_Deutschland", "http://tv.kostenloshdtv.com/10692", "https://upload.wikimedia.org/wikipedia/de/f/f4/Sky_Deutschland.png"))
    tarzlistesi.append(("Deutsche TV ", "http://tv.kostenloshdtv.com/10691", "http://www.kostenloshdtv.com/wp-content/uploads/2017/09/rtl-144x96.png"))
    tarzlistesi.append(("Deutsche TV2", "http://tv.kostenloshdtv.com/10691", "http://www.kostenloshdtv.com/wp-content/uploads/2017/09/rtl-144x96.png"))

    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'Sky_Deutschland':
            oGui.addMovie(SITE_IDENTIFIER, 'SkyDeutschland', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Deutsche TV2':
            oGui.addMovie(SITE_IDENTIFIER, 'livestreamtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
            oGui.addMovie(SITE_IDENTIFIER, 'almantvHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
def livestreamtv():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.live-stream.tv/online/fernsehen/deutsch/arte.html'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = 'class="list-group sidebarActive">(.+?)<div id="sidenavTwitter"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                
    sPattern = '<a href="(.*?)" class="list-group-item">.*?<img src="(.*?)" alt="(.*?)"'
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
            sTitle = alfabekodla(aEntry[2])
                                               
            sPicture = 'http://www.live-stream.tv'+str(aEntry[1])
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
                
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'PLAYlivestreamtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
         
    oGui.setEndOfDirectory()
  
from resources.lib import  unwise    
def PLAYlivestreamtv():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
                                
    dat= requests.get(Url).content
                  
    urll = re.findall('<iframe src="(.*?)"',dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36','Referer': referer  }
    urlm= requests.get(urll, headers = headers).text
    urlm=urlm.replace('\r',"").replace('\s',"").replace('\n',"").replace(';eval',"eval").replace(';</script>',"</script>")
                                                                     
    
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'

    urlh = re.findall('<script type="text/javascript">(eval.function.w,i,s,e.*?)</script>',urlm, re.S)[0]                       
       
    urlk =unwise.unwise_process(urlh) 
    urlk = urlk.replace('//',"").replace('\r',"").replace('\s',"").replace('\n',"").replace('; eval',"eval")
    urln = re.findall('(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))',urlk, re.S)[0]                       
    
    urlw =  cPacker().unpack(urln)
    urlw = urlw.replace('\\',"")
    baseUrl = re.findall('baseUrl:"(.*?)"',urlw, re.S)[0] 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25&Referer='+referer
            
    url = re.findall("source:'(.*?)'",urlw, re.S)[0]
    url = url.replace('https:',"https://").replace('http:',"http://")
    cookie = getUrl(urll, output='cookie').result 
    if url.find('akamaihd') > -1:      
         url =url +'|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&X-Forwarded-For=62.75.128.93' 
    else:
         url =url+ '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&Referer='+ urll
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def SkyDeutschland():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    item = oInputParameterHandler.getValue('siteUrl')
    sUrl = 'https://www.tata.to/channels'
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('<div class="item live active ">','<div class="item live">')                                                                                                   
    oParser = cParser()                         
                                                                                     
    sPattern = '<div class="ml-item-content">.*?<a href="https://www.tata.to/channel/(.*?)" class="ml-image">.*?<img src="(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):                                                                               
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            
            surl ='https://www.tata.to/channel/'+aEntry[0]    
                                                              
            img = aEntry[1]
            sTitle = aEntry[0]
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumbnail', str(img))
            oGui.addTV(SITE_IDENTIFIER, 'PLAYSkyDeutschland', sTitle, '',img, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        
    oGui.setEndOfDirectory() 

def PLAYSkyDeutschland():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    ref = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')                                                                                       
    url='https://www.tata.to/'                                                                                                                                     
    cookie = getUrl(url, output='cookie').result
    headers = {'Cookie':cookie,'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)', 'Upgrade-Insecure-Requests': '1'}
    dat = requests.get(Url, headers = headers).text                                  
    dat =dat.replace('embed.html','index.m3u8')
    chann=re.findall('<div class="tv-play" data-src="(.*?)"', dat, re.S)[0]                                    
    
#    url=requests.get(urlo,headers={'Host':'s2.skyfall.to','User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Referer':urlo, }).text
    
 #   cookie='VID=2SlVa309oFH4; mrcu=EE18510E964723319742F901060A; p=IxQAAMr+IQAA; video_key=203516; s='
    
#    data=requests.get(chann,headers=headers ).text
    status= urlencode(headers)      
#    status =status.replace('index.m3u8','status.json')
#    urlm= re.findall('#EXT-X-STREAM-INF:RESOLUTION=.*?,FRAME-RATE=.*?,CODECS=".*?",BANDWIDTH=.*?,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
#    channels = re.findall('https://(.*?)/index.m3u8.*?', chann, re.S)[0] 
    url =chann +'|'+status                 
    name =sTitle
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
    
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
def almantvHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="almantv">(.+?)<div class="almantvson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
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
            Thumbnail =aEntry[2]
            if not 'http' in Thumbnail:
                 Thumbnail ='https://www.ulantv.com/'+ Thumbnail
            
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            if  'kostenlos' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'play__kostenlos', sTitle, '', Thumbnail, '', oOutputParameterHandler)
            elif  'live-stream.tv' in aEntry[0]:
                 oGui.addTV(SITE_IDENTIFIER, 'PLAYlivestreamtv', sTitle, '', Thumbnail, '', oOutputParameterHandler)

            else:

                 oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def play__kostenlos():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sUr= 'http://www.kostenloslivetv.com/'
  
        
    referer=[('Referer',sUr)]                                      
    datam=gegetUrl(sUrl,headers=referer) 
    sUrlm = re.findall('<p><iframe src="(.*?)"', datam, re.S)[0]
       
         
       
               
    name = alfabekodla(name)
    
    referer=[('Referer',sUrl)]                                      
    datam=gegetUrl(sUrlm,headers=referer) 
    sterUrl = re.findall('file: webhdiptv."(.*?)"', datam, re.S)[0]
   
    
    headers = {'Referer':sUrlm,'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)', 'Upgrade-Insecure-Requests': '1'}
    
       
    linkam =laklak(sterUrl)
       
    chann = base64.b64decode(linkam+'==')
    status= urlencode(headers)      
    url =chann +'|'+status
    
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
def amddLink(name,url,iconimage):

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



def adultHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(SPORTS)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="adult">(.+?)<div class="adultson">'
                
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<div class="resent-grid-img recommended-grid-img"><a href="(.*?)" title="(.*?)"><img src="(.*?)"'
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
            Thumbnail ='https://www.ulantv.com/'+ aEntry[2]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(Thumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'play__tvizle', sTitle, '', Thumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

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