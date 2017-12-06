#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
 
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'

 
SITE_IDENTIFIER = 'xCanLiTVlive'
SITE_NAME = 'CanLiTVlive.co'
MOVIE_VIEWS = (True, 'CanLiTVlive')
def CanLiTVlive(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = 'http://www.canlitvlive.co/tvizle.php?&t=2&pos=r&tv=tv-8'
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    urla  = "netiyi=9bec3b6f4c00317e65a5b4ade8bc8cc4"
                       
    req = urllib2.Request(url)
    req.add_header('User-Agent', useragent)
    response = urllib2.urlopen(req)
    sHtmlContent= response.read()                  
    
                                                  
    
    sPattern = '</span><a href="(.*?)" class="name previi" data-pre="(.*?)">(.*?)</a>'
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
            sTitle = aEntry[2]
            Link = 'http:' +aEntry[0]
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(sTitle )
    
                      
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://www.canlitvlive.co/[makelist.param1]', 'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    data= requests.get(url, headers = headers).text                      
    playlist =  re.findall('filexxx= "(http.*?)"', data)[0]                     
    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
    url = playlist + '|' + Header
         
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
   