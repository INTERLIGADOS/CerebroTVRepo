#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
 
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        

url1="PT13YzAxRGQxQkhkMTltSjFOVGI5VUdjNVJuSmhkbFpMSkRaSzFFVEUxRFp5OTJkek5YWXdaU2RySjNaWkozYVpWMU05VVdiaDVtY2xOWGQvQUhhdzVTYXdGMlhzVm1iaEIzTHdBRE00b0RkbDVtTG9ObWJoWkdhejVDZGhOM0x2b0RjMFJIYQ0KDQo="
url2 = base64.b64decode(url1)
url3 =  okuoku(url2)            
streamUrl=base64.b64decode(url3) 
streamUrl=streamUrl.replace(':','%3A').replace('/','%2F').replace('=','%3D').replace('?','%3F').replace('&','%26')

SITE_IDENTIFIER = 'xiptvozel'
SITE_NAME = 'IPTV OZEL'
MOVIE_VIEWS = (True, 'user_info')
from resources.lib import comon

def iptvuser_info(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('siteUrl')
    if "get.php?username=" in url:
        channels = re.findall("http://(.*?)/get.php?username=(.*?)&password=(.*?)&type=.*?",url, re.S)
        for server,username,password in channels: 
            ssUrl = 'http://' + server + '/panel_api.php?username=' + username + '&password=' + password
    if  re.search(".m3u8|.mp4|mp3|.avi|.ts|.mkv",url, re.S):        
        channels = re.findall("http://(.*?)/live/(.*?)/(.*?)/.*?",url, re.S)
        for server,username,password in channels: 
           ssUrl = 'http://' + server + '/panel_api.php?username=' + username + '&password=' + password

   
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
    
def Kuser_info():
    oGui = cGui()
  
    
    sUrl = streamUrl
    sUrl = sUrl.replace(':','%3A').replace('/','%2F').replace('=','%3D').replace('?','%3F').replace('&','%26')
    
    ssUrl=TURKEY+sUrl

  
    
  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': ssUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = requests.get(ssUrl, headers = headers).text

       
        
    name ='test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            
sUrl = streamUrl
sUrl = sUrl
    
ssUrl=TURKEY+sUrl

HssUrl=TURKEY+sUrl
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

def user_info(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    

  
    
  
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
def user_info3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
       
  
    
  
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': ssUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(ssUrl, headers = headers).text
    sHosterUrl = re.findall('"username":"(.*?)","password":"(.*?)".*?"server_info":{"url":"(.*?)","port":"(.*?)"', data, re.S)
    (username,password,url,port) =sHosterUrl[0]
   
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': ssUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    dat = requests.get(ssUrl, headers = headers).text
    HosterUrl = re.findall('"category_id":"%s"'%sUrl+',"series_no".*?"tv_archive_duration":0},"(.*?)":{"num":.*?,"name":"(.*?)"', dat, re.S)
    for mUrl,sTitle in HosterUrl:
    

       streamUrl = 'http://%s:%s/live/%s/%s/%s.ts' % (url,port,username,password,mUrl)
       
       oOutputParameterHandler = cOutputParameterHandler()
       oOutputParameterHandler.addParameter('siteUrl',  streamUrl)
       oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
       oGui.addDir(SITE_IDENTIFIER, 'iptvplay_info', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

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

def Muser_info3(): #affiche les genres
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
            url2 = base64.b64encode(Urll)
    
            streamUrl=TURKIYE+url2

            
            
            sTitle =  alfabekodla(sTitle)
          
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',  streamUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDir(SITE_IDENTIFIER, 'iptvplay_info', sTitle, 'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
    
def iptvplay_info(): #affiche les genres
    
    
    oInputParameterHandler = cInputParameterHandler()
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = oInputParameterHandler.getValue('siteUrl')    
    
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting TS Player')
    streamtype='TSDOWNLOADER'                                                                   
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