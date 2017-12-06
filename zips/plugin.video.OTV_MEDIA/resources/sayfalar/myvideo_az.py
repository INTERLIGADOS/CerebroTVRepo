##-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 


SITE_IDENTIFIER = 'myvideo_az'
SITE_NAME = 'MYVIDEO AZ'
SITE_DESC = 'Replay TV'                 
pluginhandle = int(sys.argv[1])
MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'http://www.myvideo.az/'
URL_PIC = 'http://www.myvideo.az'
URL_MUZIK ='http://www.myvideo.az//'
MOVIE_MOVIE = ('http://', 'showAlpha')
MOVIE_GENRES = (True, 'showGenre')
data= "x0265x0287x0287x0064;<otv/>x061Ax061Ax0070x0283x02D9x0070x0279x006Fx0064x0071x006Fx0078x006Ex0073x01DDx0279x0254x006Fx0075x0287x01DDx0075x0287x02D9x0254x006Fx026Fx061Ax0073x061Atu7obt0gyhk39enx061Ax026Fx028Ex028Cx0131x0070x01DDx006Fx0250x007Ax02D9x0265x0287x026Fx0283" 	
MOV_TV  = otvdecode(data)
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
 
def pincode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if ADULT_PIN in pincode:  
            sUrl = 'http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=9'
            TurkMusikvod(sUrl)
            oGui.setEndOfDirectory()
            return  

def pinOcode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if ADULT_PIN in pincode:  
            sUrl = 'http://www.myvideo.az/c/movies/?ci_m=search&genre=14'
            showsinema(sUrl)
            oGui.setEndOfDirectory()
            return  
def mediaHeaders(chann,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69','Referer':ref ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
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
def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString

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
 
def Search():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://www.myvideo.az/c/search?srch_str='+sSearchText  
            Searchsinema(sUrl)
            oGui.setEndOfDirectory()
            return  
    

    
def MYVIDEOAZ():
    oGui = cGui()
    
    tarzlistesi = []     
    
    tarzlistesi.append(("Search", "http://www.myvideo.az/c/search?srch_str=%s"))
    tarzlistesi.append(("Live TV", "Live TV"))
    tarzlistesi.append(("Movies", "Movies"))
    tarzlistesi.append(("Türk FILM + DIZI video", "http://www.myvideo.az/vip&ci_m=playlist&playlist_id=269&per_page=50"))
    tarzlistesi.append(("Türk Musik Video", "http://www.myvideo.az//kanal59&ci_m=playlist&playlist_id=97&per_page=50"))
    tarzlistesi.append(("All", "http://www.myvideo.az/c/videos/?ci_m=videoslist"))
    tarzlistesi.append(("Auto & Moto", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=5"))
    tarzlistesi.append(("Azerbaycanda Çekilmis ", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=15"))
    tarzlistesi.append(("Cizgi filmleri", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=7"))
    tarzlistesi.append(("Din", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=23"))
    tarzlistesi.append(("Ekstremal", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=16"))
    tarzlistesi.append(("Erotik", ""))
    tarzlistesi.append(("Gülmeli", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=1"))
    tarzlistesi.append(("Kino ve televiziya", "http://www.myvideo.az/c/search?srch_str=turk+kino"))
    tarzlistesi.append(("Kompüter oyunlari", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=20"))
    tarzlistesi.append(("Mobil telefona Çekilenler", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=13"))
    tarzlistesi.append(("Musiqi", "http://www.myvideo.az/?video_id=1911473"))
    tarzlistesi.append(("Müxtelif", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=12"))
    tarzlistesi.append(("Meshurlar", "http://www.myvideo.az/http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=10"))
    tarzlistesi.append(("Reklam", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=8"))
    tarzlistesi.append(("Toylar", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=24"))
    tarzlistesi.append(("Turizm ve istirahet", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=11"))
    tarzlistesi.append(("Tabiat ve heyvanlar", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=4"))
    tarzlistesi.append(("Video dersler", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=21"))
    tarzlistesi.append(("Vip", "http://www.myvideo.az/vip"))
    tarzlistesi.append(("Xeberler", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=17"))
    tarzlistesi.append(("Idman", "http://www.myvideo.az/c/videos/?ci_m=videoslist&cat_id=2"))

    for sTitle,sUrl2 in tarzlistesi:
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Türk Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'TurkMusikvod',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Live TV':
             oGui.addDir(SITE_IDENTIFIER, 'showTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Movies':
             oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search':
             oGui.addDir(SITE_IDENTIFIER, 'Search', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'Erotik':
             oGui.addDir(SITE_IDENTIFIER, 'pincode', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'TurkMusikvod',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  
def TurkMusikvod(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
   
    sHtmlContent =sHtmlContent.replace('/v/', "&video_id=").replace('\n', "")                                                             
    sPattern = 'style="background-image:url.(.*?).; display:block;".*?<a href="(.*?)" class="mv_video_title bpgArial">(.*?)</a>'
    
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
                              
            sTitle = aEntry[2]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = aEntry[1]
                       
           
           
            
           
          
            sTitle = alfabekodla(sTitle)
            
    
            
            
                
                            
            
           
                               
                        
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            
            oGui.addDir(SITE_IDENTIFIER, 'sshowBox3',  sTitle, 'genres.png', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)
           
        sNextPage = __musikNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'TurkMusikvod', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def __mmcheckForNextPage(sHtmlContent):
    sHtmlContent=sHtmlContent.replace('amp;', "") 
    sPattern = '<li class="selected">.*?</li><li><a href="(.*?)" >'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return  aResult[1][0]
       
def kk__checkForNextPage(sHtmlContent):
    sHtmlContent =sHtmlContent.replace('amp;', "")
    #sPattern = '<a class="btn btn-default" href="([^<>"]+?)">\[Suivant >>\]<\/a>'
    sPattern = '<li class="selected">.*?</li><li><a href="(.*?)"'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        sUrl =aResult[1][0]     
        return sUrl 
 
    return False
  
def mm__checkForNextPage(sHtmlContent):
    oGui = cGui()
    
    sPattern = '<li class="selected">.*?</li><li><a href="(.*?)" >'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_PIC ) + aResult[1][0]

 
def showTV(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = MOV_TV
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
                                                             
    sPattern = '<div class="mv_dvr_chan_item bpgArial ">.*?<a href=".*?" title="(.*?)".*?<img align="absmiddle" src="(.*?)" alt="(.*?)"'
    
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
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[2]
            
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showBox1', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()
  
def showMovies():
    oGui = cGui()
    
    tarzlistesi = []
    
    tarzlistesi.append(("Türk filmleri ", "http://www.myvideo.az/c/movies/?ci_m=search&genre=36"))
    tarzlistesi.append(("Türk seriallari ", "http://www.myvideo.az/c/movies/?ci_m=search&genre=35"))
  
    tarzlistesi.append(("Action", "http://www.myvideo.az/c/movies/?ci_m=search&genre=22"))
    tarzlistesi.append(("Adventrure", "http://www.myvideo.az/c/movies/?ci_m=search&genre=26"))
    tarzlistesi.append(("Azerbaycan", "http://www.myvideo.az/c/movies/?ci_m=search&genre=11"))
    tarzlistesi.append(("Animation", "http://www.myvideo.az/c/movies/?ci_m=search&genre=16"))
    tarzlistesi.append(("Biography", "http://www.myvideo.az/c/movies/?ci_m=search&genre=18"))
    tarzlistesi.append(("Comedy", "http://www.myvideo.az/c/movies/?ci_m=search&genre=5"))
    tarzlistesi.append(("Criminal", "http://www.myvideo.az/c/movies/?ci_m=search&genre=36"))
    tarzlistesi.append(("Detective", "http://www.myvideo.az/c/movies/?ci_m=search&genre=12"))
    tarzlistesi.append(("Documentary", "http://www.myvideo.az/c/movies/?ci_m=search&genre=15"))
    tarzlistesi.append(("Drama", "http://www.myvideo.az/c/movies/?ci_m=search&genre=13"))
    tarzlistesi.append(("Erotik", ""))
    tarzlistesi.append(("Family", "http://www.myvideo.az/c/movies/?ci_m=search&genre=29"))
    tarzlistesi.append(("Fantasy", "http://www.myvideo.az/c/movies/?ci_m=search&genre=33"))
    tarzlistesi.append(("Azerbaijan", "http://www.myvideo.az/c/movies/?ci_m=search&genre=11"))
    tarzlistesi.append(("History", "http://www.myvideo.az/c/movies/?ci_m=search&genre=20"))
    tarzlistesi.append(("Horror", "http://www.myvideo.az/c/movies/?ci_m=search&genre=30"))
    tarzlistesi.append(("Melodrama", "http://www.myvideo.az/c/movies/?ci_m=search&genre=35"))
    tarzlistesi.append(("Music", "http://www.myvideo.az/c/movies/?ci_m=search&genre=21"))
    tarzlistesi.append(("Parody", "http://www.myvideo.az/c/movies/?ci_m=search&genre=23"))
    tarzlistesi.append(("Romantic", "http://www.myvideo.az/c/movies/?ci_m=search&genre=24"))
    tarzlistesi.append(("Russian", "http://www.myvideo.az/c/movies/?ci_m=search&genre=25"))
    tarzlistesi.append(("Seriallar", "http://www.myvideo.az/c/movies/?ci_m=search&genre=31"))
    tarzlistesi.append(("Sci-Fi", "http://www.myvideo.az/c/movies/?ci_m=search&genre=27"))
    tarzlistesi.append(("Shows", "http://www.myvideo.az/c/movies/?ci_m=search&genre=31"))
    tarzlistesi.append(("Sports", "http://www.myvideo.az/c/movies/?ci_m=search&genre=32"))
    tarzlistesi.append(("Thriller", "http://www.myvideo.az/c/movies/?ci_m=search&genre=34"))
    tarzlistesi.append(("War", "http://www.myvideo.az/c/movies/?ci_m=search&genre=28"))
    tarzlistesi.append(("Western", "http://www.myvideo.az/c/movies/?ci_m=search&genre=19"))
   
    for sTitle,sUrl2 in tarzlistesi:
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Türk Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'TurkMusikvod',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Live TV':
             oGui.addDir(SITE_IDENTIFIER, 'showTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Erotik':
             oGui.addDir(SITE_IDENTIFIER, 'pinOcode', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showsinema',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def Searchsinema(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                                                                                                                           

    sPattern = '<div class="mv_video_item_cover_cont" >.*?class="vd_go_to_video " style="background-image:url.(http://static.myvideo.az.*?jpg).; display:block;".*?<a href="(.*?)" class="mv_video_title bpgArial">(.*?)</a>'
    
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
           
            sTitle = aEntry[2]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            
                      
            
           
            sTitle = alfabekodla(sTitle)
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'sSearchBox3', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = mm__checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showsinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()   

def sSearchBox3():
    oGui = cGui()
       
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
   
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
                
    	
    resp = net.http_GET(url)
    data = resp.content
    Url = re.findall('file: "(.*?)"', data)[0]
     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    
    
   
    sHosterUrl =Url + '|' + Header
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False    
    oGui.setEndOfDirectory()
   


def showsinema(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                             
    sPattern = '<div class="mv_movie_modal_info modal-fluid-carousel left_align">.*?<a href=".*?" class="mv_movie_modal_info_cover left_cover" style="background-image:url.\'(.*?)\'.">.*?<a href="(.*?)".*?class="mv_movie_item_title bpgArial">                                          (.*?)</a>'
    
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
           
            sTitle = aEntry[2]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            
                      
            
           
            sTitle = alfabekodla(sTitle)
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = mm__checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showsinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()
def __musikNextPage(sHtmlContent):
    oGui = cGui()
   
    
    sPattern = '<li class="selected">.*?</li><li><a href="(.*?)" >'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MUZIK) + aResult[1][0]

       
    return False             
def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '</a> <a href="(.*?)" class="syfno">Sonraki Sayfa &raquo;</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl) + aResult[1][0]

    return False

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

def partplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
       
    stream = re.findall('<td class="title">.*?<a href=".*?&(.*?)" class="title">', data, re.S)
    url = "http://www.netd.com%s" %(stream[0])
    tarzlistesi= []
    tarzlistesi.append(("part=1", ""+url.replace('</span> <b>','<OTV>')))
    tarzlistesi.append(("part=2", ""+url.replace('part=1-6','part=2-6')))
    tarzlistesi.append(("part=3", ""+url.replace('part=1-6','part=3-6')))
    tarzlistesi.append(("part=4", ""+url.replace('part=1-6','part=4-6')))
    tarzlistesi.append(("part=5", ""+url.replace('part=1-6','part=5-6')))
    tarzlistesi.append(("part=6", ""+url.replace('part=1-6','part=6-6')))
        
    for sTitle,sUrl in tarzlistesi:
           
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox3', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()
    
def showBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urllk = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    sTitle = alfabekodla(sTitle)
    urlk = "https://www.myvideo.az//ios/android.php?chan=aztv"
		                                                                                                                                                                                                  
    print urlk             
    urla  = "http://www.myvideo.az/"
    referer=[('Referer',urla)]
    data=gegetUrl(urlk,headers=referer) 
    data =data.replace('\/', "/").replace('aztv', "%s")
    print data
    Url = re.findall('"st":"(.*?)"', data, re.S)[0]
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'

    sUrl =Url %Urllk  + '|' + Header
    sTitle = alfabekodla(sTitle)          
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
    oGui.addDir(SITE_IDENTIFIER, 'showhlsetryplayer', sTitle, 'tv.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

            
def sshowBox2():
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
  
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    data=getUrl(url).result 
       
    stream = re.findall('<td class="title">.*?<a href=".*?ci_m=inner&movie_id=.*?&(.*?)" class="title">', data, re.S)
    print stream
    
    url = "http://embed.myvideo.az/flv_player/jwconfigFb.php?%s.mp4"%stream[0]
		                        
            
    data=getUrl(url).result 
    Url = re.findall("<file>(.*?)</file>", data)[0]

     
    Header = 'Referer=http://www.myvideo.az/flv_player/j/playerNew.swf'
    
    
    sHosterUrl =mediaHeaders(Url, url)
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False
    oGui.setEndOfDirectory()
  

def sshowBox3():
    oGui = cGui()
       
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    url = "http://www.myvideo.az/?CIA=1&ci_c=chromeappembed%s.mp4"%sUrl.replace('?video_id', "&video_id") 
	  	                        
   
            
    	
    resp = net.http_GET(url)
    data = resp.content
    Url = re.findall('file: "(.*?)"', data)[0]
     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    
    
   
    
    sHosterUrl =mediaHeaders(Url, url)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False    
    oGui.setEndOfDirectory()
   

def PlayerType():
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
        
def otvplay__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
	
   
    playlist=xbmc.PlayList(xbmc.PLAYER_CORE_DVDPLAYER); 
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+sTitle)
    playlist.add(sUrl,listitem1);
    listitem2 = xbmcgui.ListItem(''+sTitle)
    playlist.add(sUrl,listitem2);
    listitem3 = xbmcgui.ListItem(''+sTitle)
    playlist.add(sUrl,listitem3);
    sPlayerType = PlayerType()
    xbmcPlayer = xbmc.Player(sPlayerType)
    
    xbmcPlayer.play(playlist) 
    return False
    oGui.setEndOfDirectory()
    
def changeStream():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urlk = oInputParameterHandler.getValue('siteUrl')
    title = oInputParameterHandler.getValue('sMovieTitle')
    url = "http://embed.myvideo.az/flv_player/jwconfigFb.php%s.mp4"%urlk
		                        
      
    urla  = "http://www.myvideo.az/"
    referer=[('Referer',urla)]
    data=gegetUrl(url,headers=referer) 
    Url = re.findall("<file>(.*?)</file>", data)[0]

     
    Header = 'Referer=http://www.myvideo.az/flv_player/j/playerNew.swf'
    
    
    sUrl =Url + '|' + Header
    listitem = xbmcgui.ListItem(title, path=urlk)
    xbmc.Player().play(sUrl, listitem)
    oGui.setEndOfDirectory()
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



