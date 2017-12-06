#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')

import HTMLParser
hpar = HTMLParser.HTMLParser()
import re,xbmcgui,unicodedata

SITE_IDENTIFIER = 'myvideo_ge'
SITE_NAME = 'MYVIDEO Georgia'
SITE_DESC = 'Replay TV'                 
pluginhandle = int(sys.argv[1])
MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'http://www.myvideo.ge/'
URL_PIC = 'http://www.myvideo.ge/'
URL_MUZIK ='http://www.myvideo.ge//'
MOVIE_MOVIE = ('http://', 'showAlpha')
MOVIE_GENRES = (True, 'showGenre')
data= "x0265x0287x0287x0064;<otv/>x061Ax061Ax0070x0283x02D9x0070x0279x006Fx0064x0071x006Fx0078x006Ex0073x01DDx0279x0254x006Fx0075x0287x01DDx0075x0287x02D9x0254x006Fx026Fx061Ax0073x061Atu7obt0gyhk39enx061Ax026Fx028Ex028Cx0131x0070x01DDx006Fx0250x007Ax02D9x0265x0287x026Fx0283" 	
MOV_TV  = 'http://www.myvideo.ge/mytvbox&page=payment#&show_channels'
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
def mCleanTitle(title):
    title = cUtil().unescape(title)
    title = cUtil().removeHtmlTags(title)
    try:
        
         title =title.decode('unicode-escape').decode('koi8-r').encode('UTF-8') 
    except:
        pass
    
    
    return title
def showLinks(sUrl):
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    url  = sHtmlContent
    return url          

def CleanTitle(title):
    title = cUtil().unescape(title)
    title = cUtil().removeHtmlTags(title)
    try:
        title = title .decode('ISO-8859-15').encode( "utf-8").encode('latin-1').decode('cp1251')
      
    except:
        pass
    title = getUtf8Str( title)
    
    return title.encode( "utf-8")

def unescape(src):
    s = src.decode('string-escape')
    u = s.decode('utf8')
    
    return u.encode('unicode-escape')
def mediaHeaders(chann,ref):
                                                                                                                                                               
     parts = chann.split('|', 1)                                                                                                                                     
     chann  = parts[0]
     if len(parts) > 1:
          headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69','Referer':ref ,'X-Requested-With': 'XMLHttpRequest',  'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
          headers = str(parts[1])
     return chann

def pinOcode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if ADULT_PIN in pincode:  
            sUrl = 'http://www.myvideo.ge/c/movies/?ci_m=search&genre=14'
            showsinema(sUrl)
            oGui.setEndOfDirectory()
            return  
def getUtf8Str(st):
            idx = 0
            st2 = ''
            while idx < len(st):
                st2 += '' + st[idx:idx + 3]
                idx += 3
            return st2.decode('unicode-escape').encode('UTF-8')          
          
        
	
         
                        #file = file.decode('unicode-escape')

                
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
 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://www.myvideo.ge/c/search?srch_str='+sSearchText  
            showMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
    
def pincode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if ADULT_PIN in pincode:  
            sUrl = 'http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=9'
            TurkMusikvod(sUrl)
            oGui.setEndOfDirectory()
            return  
    
def MYVIDEOGeor():
    oGui = cGui()
    
    tarzlistesi = []     
    
    tarzlistesi.append(("Search", "http://www.myvideo.ge/c/search?srch_str=%s"))
    tarzlistesi.append(("Live TV", "http://www.myvideo.ge/c/livetv"))
    tarzlistesi.append(("Movies", "Movies"))
    tarzlistesi.append(("All", "http://www.myvideo.ge/c/videos/?ci_m=videoslist"))
    tarzlistesi.append(("Auto & Moto", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=5"))
    tarzlistesi.append(("Cartoons", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=7"))
    tarzlistesi.append(("Celebrities", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=10"))
    tarzlistesi.append(("Cookery", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=24"))
    tarzlistesi.append(("Erotic", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=9"))
    tarzlistesi.append(("Extreme", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=16"))
    tarzlistesi.append(("Fashion and Art", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=19"))
    tarzlistesi.append(("Flora & Fauna", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=4"))
    tarzlistesi.append(("Funny", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=1"))
    tarzlistesi.append(("Georgian", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=15"))
    tarzlistesi.append(("Horrible", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=18"))
    tarzlistesi.append(("Karaoke", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=25"))
    tarzlistesi.append(("Mobile Videos", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=13"))
    tarzlistesi.append(("Music", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=6"))
    tarzlistesi.append(("News and Politics", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=17"))
    tarzlistesi.append(("Other", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=12"))
    tarzlistesi.append(("Publicity", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=8"))
    tarzlistesi.append(("Religion", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=23"))
    tarzlistesi.append(("Rest and Tourism ", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=11"))
    tarzlistesi.append(("Science and Technology", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=22"))
    tarzlistesi.append(("Sport", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=2"))
    tarzlistesi.append(("TV & Cinema", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=3"))
    tarzlistesi.append(("Video Games", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=20"))
    tarzlistesi.append(("Video Tutorials", "http://www.myvideo.ge/c/videos/?ci_m=videoslist&cat_id=21"))

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
        elif sTitle == 'Erotic':
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
                           
            
             
            sTitle =aEntry[2]
            sTitle= sTitle.decode('utf-8',"replace")
            sTitle = sTitle.encode('utf-8')#On remet en utf-8

            
            sTitle = unescape(sTitle)
            sTitle =detranslify(sTitle)

            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = aEntry[1]
                       
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            
            oGui.addDir(SITE_IDENTIFIER, 'sshowBox5',  sTitle, 'genres.png', oOutputParameterHandler)
            
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
        return str(aResult[1][0] )

 
def showTV():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = MOV_TV
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    oParser = cParser()
    sPattern = '<div class="chanels-list pull-right">(.+?)</tbody>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                                         
     
    sPattern = '<td class="chanel-logo">.*?<img class="lazy" data-original="v3_imgs/tv/tv_(.*?).png" alt="Public Chanel" width="20">.*?<td class="chanel-name">(.*?)</td>'
                                           
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
                                                                                                                         
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle =unescape(aEntry[1])
            sTitle =detranslify(sTitle)
            
            sUrl = aEntry[0]
                      
            sPicture = 'https://www.myvideo.ge/v3_imgs/tv/tv_%s.png'% sUrl
            
           
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

  
        oGui.setEndOfDirectory()
  
def showMovies():
    oGui = cGui()
    
    tarzlistesi = []
    
    tarzlistesi.append(("Action", "http://www.myvideo.ge/c/movies/?ci_m=search&genre=22"))
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
    tarzlistesi.append(("Georgian", "http://www.myvideo.az/c/movies/?ci_m=search&genre=11"))
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
    sPattern = 'style="background-image:url.\'(.*?)\'.">.*?<a href="(.*?)".*?class="mv_movie_item_title bpgArial">                                          (.*?)</a>'
    
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

def showsinemage(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                             
    sPattern = '<a data-lang=".*?" title="" class="myvideo_tag_movie " href="movies/.*?/video/(.*?)/.*?">(.*?)</a>'
    
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
             
            sTitle =aEntry[1].decode('unicode-escape').encode('UTF-8')
                            
            sUrl = aEntry[0]
             
                      
           
            sPicture ='http://t1.gstatic.com/images?q=tbn:ANd9GcRVJpl9KjUMFzRXyI7AfA4j9V-jBVJh1ewrTyGs7OdOB-D1NstIUIgt'
           
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
        return str( aResult[1][0]) 

       
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
           
         
         
        sTitle =georgiadecode(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox5', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()
    
def showBox1():
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    urlk = "https://www.myvideo.ge//ios/android.php?chan="+ Url
		                                                                                                                                                                                                  
                  
    urla  = "http://www.myvideo.ge/"
    referer=[('Referer',urla)]
    data=gegetUrl(urlk,headers=referer) 
    data =data.replace('\/', "/").replace('mono.m3u8', "index.m3u8").replace('tbs01-edge04.itdc.ge', "bak01-edge03.itdc.ge").replace('tbs01-edge03.itdc.ge', "bak01-edge03.itdc.ge").replace('tbs01-edge02.itdc.ge', "bak01-edge03.itdc.ge")
    Url = re.findall('"st":"(.*?)"', data, re.S)[0]
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    sHosterUrl =Url + '|' + Header
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(name)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False

            
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    net = Net()
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    Cookie_Jar=getCookieJar()
#    data = requests.get(sUrl).content 
    urla  = "http://www.myvideo.ge/"
    referer=[('Referer',urla)]
    data=gegetUrl(sUrl,headers=referer)  
    stream = re.findall('<div class="mv_video_item_cover_cont" >.*?href="movies/.*?/video/(.*?)/.*?"', data, re.S)
    print stream
    
    url = "http://www.myvideo.ge/?CIA=1&ci_c=chromeappembed&video_id=%s.mp4"%stream[0]
	  	                        
   
            
    	
    resp = net.http_GET(url)
    data = resp.content
    Url = re.findall('file: "(.*?)"', data)[0]
     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    sHosterUrl =mediaHeaders(Url,url)
    
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
def sshowBox5():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    url = "http://www.myvideo.ge/?CIA=1&ci_c=chromeappembed%s.mp4"%sUrl
	  	                        
   
            
    	
    resp = net.http_GET(url)
    data = resp.content
    Url = re.findall('file: "(.*?)"', data)[0]
     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    
    sHosterUrl =mediaHeaders(Url,url)

                     
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
    urlk = "https://www.myvideo.ge//ios/android.php?chan="+ sUrl
		                       
         
    urla  = "http://www.myvideo.ge/"
    referer=[('Referer',urla)]
    data=gegetUrl(urlk,headers=referer) 
    data =data.replace('\/', "/").replace('mono.m3u8', "index.m3u8")
    sUrl = re.findall('"st":"(.*?)"', data, re.S)[0]	
   
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
    urlk=urlk.replace('?video_id=', "video_id=") 
    url = "http://www.myvideo.ge/?CIA=1&ci_c=chromeappembed&"+urlk
		                        
          
    data=getUrl(url).result 
    Url = re.findall('file: "(.*?)"', data)[0]

     
    Header = 'Referer=http://www.myvideo.ge/flv_player/j/playerNew.swf'
    
    
    sUrl =Url + '|' + Header
    listitem = xbmcgui.ListItem(title, path=urlk)
    xbmc.Player().play(sUrl, listitem)
    return False
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


