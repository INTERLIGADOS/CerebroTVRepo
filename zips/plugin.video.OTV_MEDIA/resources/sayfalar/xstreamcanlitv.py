#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
 
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'

 
SITE_IDENTIFIER = 'xstreamcanlitv'
SITE_NAME = 'CanLiTV.stream'
MOVIE_VIEWS = (True, 'streamcanlitv')

def streamcanlitv():
    oGui = cGui()
    urlkk= "http://www.canlitv.stream/" 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.canlitv.stream/kategoriler'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if re.match('.*?<a href="tum-kanallar">',sHtmlContent, re.S):
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
      sPattern = '<a href="(kategori/.*?)">(.*?)</a>'
                                                                 
      sHtmlContent = sHtmlContent
   
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
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(urlkk) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture = "http://www.canlitv.stream/static/images/logo.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'streamcanlitv2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
    oGui.setEndOfDirectory()
def streamcanlitv2():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<div class="tv-list-inner">(.+?)<div class="site-about">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<a href="(.*?)" title="(.*?)">'
                                                              
    sHtmlContent = sHtmlContent        
   
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
            sPicture = "http://www.canlitv.stream/static/images/logo.png"  
            sUrl = str(aEntry[0])
                       
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
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
       
    oGui.setEndOfDirectory()
            
def sshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = requests.get(Url, headers = headers).text

   

   
    urlk = re.findall('<div class="player">.*?<iframe width="100%" height="100%" src="(.*?)"', dat, re.S)[0]  
             
    sUrl = str(urlk)
    if not 'http' in sUrl:
       sUrl = str(urla) + sUrl

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    source = requests.get(sUrl, headers = headers).text
    
    sHosterUrl = re.findall("file: '(.*?)'",source, re.S)[0]
    sPicture ="https://www.canlitv.zone/logo/tivibu-spor_9147556.png"
    Header = '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    url= sHosterUrl + Header
    name = alfabekodla(sTitle) 
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
def iostreamcanlitv():
    oGui = cGui()
    urlkk= "http://www.canlitv.stream/" 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.canlitv.stream/kategoriler'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if re.match('.*?<a href="tum-kanallar">',sHtmlContent, re.S):
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
      sPattern = '<a href="(kategori/.*?)">(.*?)</a>'
                                                                 
      sHtmlContent = sHtmlContent
   
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
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(urlkk) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture = "http://www.canlitv.stream/static/images/logo.png"
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'streamcanlitv2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
    oGui.setEndOfDirectory()
def iostreamcanlitv2():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://mobile.canlitvlive.io/')
    oGui.addDir(SITE_IDENTIFIER, 'iostream', 'Yeni TV Kanallari', 'genres.png', oOutputParameterHandler)

           
    sUrl = 'http://mobile.canlitvlive.io/?s=Yerel'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '<li><a class="subheader">Kategoriler</a></li>(.+?)<div class="nav-wrapper navbar searcharea">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<li><a href="(.*?)"><i class="material-icons">.*?</i>(.*?)</a></li>'
                                                             
    sHtmlContent = sHtmlContent        
   
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
            sPicture = "http://mobile.canlitvlive.io/images/mobil-footer.png"  
            sUrl = str(aEntry[0])
                       
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
                oGui.addMovie(SITE_IDENTIFIER, 'iostream', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
       
    oGui.setEndOfDirectory()
def iostream(sSearch = ''):
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = '</center>(.+?)<div class="mobireklam">'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult    
    sPattern = '</li><li><a href="(.*?)" title=".*?"><center><h2 class="lsttop">(.*?)</h2></center><img class="logo" src="(.*?)"'
                                 
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
           
            sTitle = cUtil().unescape(aEntry[1])
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
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
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'iossshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
    oGui.setEndOfDirectory()            
def iossshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
  
                       
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': Url , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = requests.get(Url, headers = headers).text

   

   
    sHosterUrl= re.findall('file : "(.*?)"', dat, re.S)[0]  
             
    Header = '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    url= sHosterUrl + Header
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
      