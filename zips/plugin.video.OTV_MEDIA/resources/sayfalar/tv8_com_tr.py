#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                 
SITE_IDENTIFIER = 'tv8_com_tr'
SITE_NAME = 'TV8_com_tr'
SITE_DESC = 'Replay TV'
from xcanlitvzone import sshowBox19              

MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'http://www.netd.com'
URL_PIC = 'http://s.dogannet.tv/'
MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
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
          
def tv8comtr():                              
    oGui = cGui()
    tarzlistesi = []
    tarzlistesi.append(("TV8 CANLI YAYIN", "http://www.tv8.com.tr/canli-yayin"))
    tarzlistesi.append(("TV8 YEDEK", "https://canlitv.co/tv8.html"))
    tarzlistesi.append(("TV8int CANLI YAYIN", "http://www.tv8.com.tr/canli-yayin"))
    tarzlistesi.append(("TV 8.5YEDEK CANLI YAYIN", "http://www.canlitvlive.co/tvizle.php?t=2&pos=r&tv=tv8-bucuk-izle"))

    tarzlistesi.append(("Acun Medya", "https://www.acunn.com/programlar"))
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TV8 CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv8canli', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV8 YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'sshowBox19', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV8int CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv8intcanli', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TV 8.5YEDEK CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv85Box', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'programlar', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  
def kanaldTV():
    oGui = cGui()
    tarzlistesi= []             
    tarzlistesi.append(("Kanal D Canlı Yayın", "https://s.kanald.com.tr/ps/kanald_proxy/assets/img/kanal-d.png?v=2", "https://www.kanald.com.tr/actions/content/media/542410a361361f36f4c3fcf1"))
    tarzlistesi.append(("CNN T�RK Canlı Yayın", "http://i.cnnturk.com/ps/cnnturk_proxy/ContentMainPage/frontEnd/images/cnnturk-logo.png", "http://www.cnnturk.com/action/media/51cc1dbd32dc9f19b8bc77cf"))
    tarzlistesi.append(("TV2 Canlı Yayın", "http://www.tv2.com.tr/assets/img/logo.png", "http://www.tv2.com.tr/actions/content/media/564da04ef5ac761dbc5e0a13"))
    tarzlistesi.append(("Dream Turk Canlı Yayın", "http://dreamq.dogannet.tv/images/100/800x450/571f37e3980ea80bc034ee2b", "http://dreamturk.com.tr/actions/content/media/566ab958980ea810b4658d96"))
    tarzlistesi.append(("Dream TV Canlı Yayın", "http://www.dreamtv.com.tr/content/frontEnd/images/dream-tv-logo.png", "http://www.dreamtv.com.tr/actions/content/media/5565d197f5ac76262cb2bba5"))
    tarzlistesi.append(("Tay TV Canlı Yayın", "http://www.dreamturk.com.tr/content/frontEnd/images/dream-turk-logo.png", "http://www.dreamtv.com.tr/actions/content/media/5565d197f5ac76262cb2bba5"))
    tarzlistesi.append(("Disney", "https://s.kanald.com.tr/ps/kanald_proxy/assets/img/d-smart-v2.png", "http://www.tv2.com.tr/actions/content/media/564da04ef5ac761dbc5e0a13"))
    for sTitle,sPicture,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
    oGui.setEndOfDirectory()




def showmGenre(): #affiche les genres
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                
    oParser = cParser()
    sPattern = '<div class="homepageCompetitionVideoListWrapper">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                
    sPattern = '<div class="homepageCompetitionVideoListSubTitle clearfix"><h3>(.*?)</h3><a class="homepageCompetitionVideoListAllPlay" href="(.*?)" title=" Playlist">(.*?)<i class="fa fa-caret-right"></i></a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            
            Url = aEntry[1]
            Urlaa =aEntry[2]
            sTitle = alfabekodla(aEntry[0]) 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url )
            oGui.addDir(SITE_IDENTIFIER, 'videokato', sTitle, 'genres.png', oOutputParameterHandler)
           
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()  
def Survivor(): #affiche les genres
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
             
    sPattern = '<li ><h3><a href="(.*?)" title=".*?">(.*?)</a></h3></li>'
    
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
           
            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'program', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()  
def videokato():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()

    if (oInputParameterHandler.exist('iPage')):
        iPage = oInputParameterHandler.getValue('iPage')
    else:
        iPage = 1

    if (oInputParameterHandler.exist('siteUrl')):
        sUrl = oInputParameterHandler.getValue('siteUrl')
              
        
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()

        __parseMovieSimpleList(sHtmlContent, iPage)

def __parseMovieSimpleList(sHtmlContent, iPage):
   
    sPattern = '<a class="clearfix" href="(.*?)" title=".*?" onclick="ga.*?"><div class="imageDiv"><img src="(.*?)" alt="(.*?)"'
                                 
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
           
            sPicture = str(aEntry[1].replace('/70x40/', "/980x400/"))
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + sUrl            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui = cGui()
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'videoacunn', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
        sNextPage = __checkForNextPage(sHtmlContent,iPage)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oOutputParameterHandler.addParameter('iPage', int(iPage) + 1)
                oGui.addDir(SITE_IDENTIFIER, 'videokato', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent, iCurrentPage):
    iNextPage = int(iCurrentPage) + 1
    iNextPage = str(iNextPage) + ' '
    sPattern = '<link rel="canonical" href="([^"]+)"/>'+'/' + iNextPage 
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return aResult[1][0]
    return False


def program(sSearch = ''):
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
         
      
        sPattern = '<div class="dizi.*?id="dizi.*?">.*?<a href="(.*?)"><img class="diziImage" src="(.*?)".*?<li class="dizi_adi">(.*?)</li>'                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sayUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sayUrl)
        sHtmlContent = oRequestHandler.request()
        


                                                                             
                                                                          
                   
                    
        sPattern = '<a class="clearfix" href="(.*?)" title=".*?" onclick="ga.*?"><div class="imageDiv"><img src="(.*?)" alt="(.*?)"'
                                 
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
           
            sPicture = str(aEntry[1])
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
 
            if sTitle == 'VIDEOLAR':
                 oGui.addDir(SITE_IDENTIFIER, 'tv8canli', sTitle, 'genres.png', oOutputParameterHandler)
            elif sTitle == 'SORVIVOR':
                 oGui.addDir(SITE_IDENTIFIER, 'Survivor', sTitle, 'genres.png', oOutputParameterHandler)
            elif sTitle == '3 ADAM':
                 oGui.addDir(SITE_IDENTIFIER, 'ucadam', sTitle, 'genres.png', oOutputParameterHandler)
            elif sTitle == 'O SES TURKIYE':
                 oGui.addDir(SITE_IDENTIFIER, 'osesturkiye', sTitle, 'genres.png', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Survivor', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage =  __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'programlar', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def programlar():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
        


                                                                             
                                                                          

    oParser = cParser()
    sPattern = '><div class="programList clearfix">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                
    sPattern = '<li><a href="(.*?)" title=".*?"><img src="(.*?)" alt="(.*?)" />'
                                 
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
                                               
            sPicture = str(aEntry[1].replace('/70x40/', "/980x400/"))
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
 
            oGui.addMovie(SITE_IDENTIFIER, 'showmGenre', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
         
    oGui.setEndOfDirectory()



def videoacunn():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "https://www.acunn.com/"
                     
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
                              
    streamDaten = re.findall('application/x-mpegURL.*?src:"(https://.*?.mp4)"', data, re.S)
    if streamDaten:
                  (serviceUrl )= streamDaten[0]
                       
    sHosterUrl = "%s"  % (serviceUrl.replace("-240p.mp4","-720p.mp4").replace("-360p.mp4","-720p.mp4").replace("-480p.mp4","-720p.mp4"))
                                          
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False
def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    
    
    urla  = "http://www.tv8.com.tr/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('"SecurePath": "', '"SecurePath":"')      
    streamDaten = re.findall('src\':  "(.*?)"', data, re.S)
    if streamDaten:               
                  (serviceUrl )= streamDaten[0]
                       
                          
    sHost = "%s"  % (serviceUrl.replace('\u0026', "&"))

    urla  = "http://www.tv8.com.tr/"
                      
    referer=[('Referer',urla)]
    dat=gegetUrl(sHost,headers=referer) 
    dat=dat.replace('tv8int_720p.m3u8', "tv8hd_720p.m3u8")
    stream= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,NAME=720p,RESOLUTION=.*?\n(.*?)\n', dat, re.S)
    
    sHosterUrl = "https://tv8-tb-live.ercdn.net/tv8-geo/%s"  %(stream[0])
    Header = 'Referer=https://www.tv8.com.tr/canli-yayin&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= sHosterUrl+ '|' + Header 

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

def tv8intcanli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    
    
    urla  = "http://www.tv8.com.tr/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('"SecurePath": "', '"SecurePath":"')      
    streamDaten = re.findall('src\':  "(.*?)"', data, re.S)
    if streamDaten:          
                  (serviceUrl )= streamDaten[0]
                       
                          
    sHost = "%s"  % (serviceUrl.replace('\u0026', "&"))

    urla  = "http://www.tv8.com.tr/"
                      
    referer=[('Referer',urla)]
    dat=gegetUrl(sHost,headers=referer) 
    
    stream= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1200000,NAME=720p,RESOLUTION=.*?\n(.*?)\n', dat, re.S)
    
    sHosterUrl = "https://tv8-tb-live.ercdn.net/tv8-geo/%s"  %(stream[0])
    
    Header = 'Referer=https://www.tv8.com.tr/canli-yayin&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= sHosterUrl+ '|' + Header 
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

def tv85Box():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle )
    
                      
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://www.canlitvlive.co/[makelist.param1]', 'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
    data= requests.get(url, headers = headers).text                      
    playlist =  re.findall('filexxx= "(http.*?)"', data)[0]                     
    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
    sHosterUrl = playlist + '|' + Header
    sTitle =  alfabekodla(sTitle)
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
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
   
    
    urla  = "http://www.tv8.com.tr/"                   
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer)                      
    streamDaten = re.findall("src:\".*?\", type:'application/x-mpegURL'.*?src:\"(.*?)\", type:'video/mp4'", data, re.S)	
    if streamDaten:
                  (serviceUrl )= streamDaten[0]                                                                         
                       
                          
    sHosterUrl = "%s"  % (serviceUrl.replace("-240p.mp4","-720p.mp4").replace("-360p.mp4","-720p.mp4").replace("-480p.mp4","-720p.mp4").replace(".mp4","-720p.mp4").replace("-720p-720p.mp4","-720p.mp4"))    
 
    



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False