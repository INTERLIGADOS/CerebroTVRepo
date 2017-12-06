# -*- coding: utf-8 -*-
from resources.lib.otvhelper import *

ALMAN_SINEMA = (True, 'sshowGenre')
SITE_IDENTIFIER = 'kinox_to'
SITE_NAME = 'KinoX'
SITE_ICON = 'kinox.png'
URL_HOST= 'http://kinox.to/aGET/Mirror/'
URL_MAIN = 'http://kinox.to' 
URL_NEWS = URL_MAIN + '/index.php'
URL_CINEMA_PAGE = URL_MAIN + '/Cine-Films.html'
URL_GENRE_PAGE = URL_MAIN + '/Genre.html'
URL_MOVIE_PAGE = URL_MAIN + '/Movies.html'
URL_SERIE_PAGE = URL_MAIN + '/Series.html'
URL_DOCU_PAGE = URL_MAIN + '/Documentations.html'

URL_FAVOURITE_MOVIE_PAGE = URL_MAIN + '/Popular-Movies.html'
URL_FAVOURITE_SERIE_PAGE = URL_MAIN + '/Popular-Series.html'
URL_FAVOURITE_DOCU_PAGE = URL_MAIN + '/Popular-Documentations.html'

URL_LATEST_SERIE_PAGE = URL_MAIN + '/Latest-Series.html'
URL_LATEST_DOCU_PAGE = URL_MAIN + '/Latest-Documentations.html'

URL_SEARCH = URL_MAIN + '/Search.html'
URL_MIRROR = URL_MAIN + '/aGET/Mirror/'
URL_EPISODE_URL = URL_MAIN + '/aGET/MirrorByEpisode/'
URL_AJAX = URL_MAIN + '/aGET/List/'
URL_LANGUAGE = URL_MAIN + '/aSET/PageLang/1'
DE_MAIN= 'Deutsch' 
EN_MAIN= 'English' 
def sEcho(s):
      s=s
      if 'iDisplayStart=0' in s:
	s=s.replace('iDisplayStart=0','iDisplayStart=25')
        return s 
      if 'iDisplayStart=25' in s:
	s=s.replace('iDisplayStart=25','iDisplayStart=50')
        return s 
      if 'iDisplayStart=50' in s:	
        s=s.replace('iDisplayStart=50','iDisplayStart=75')
        return s 
      if 'iDisplayStart=75' in s:	
        s=s.replace('iDisplayStart=75','iDisplayStart=100')
        return s 
      if 'iDisplayStart=100' in s:	
        s=s.replace('iDisplayStart=100','iDisplayStart=125')
        return s 
      if 'iDisplayStart=125' in s:	
        s=s.replace('iDisplayStart=125','iDisplayStart=150')
        return s 
      if 'iDisplayStart=150' in s:	
        s=s.replace('iDisplayStart=150','iDisplayStart=175')
        return s 
      if 'iDisplayStart=175' in s:	
        s=s.replace('iDisplayStart=175','iDisplayStart=200')
        return s 
      if 'iDisplayStart=200' in s:	
        s=s.replace('iDisplayStart=200','iDisplayStart=225')
        return s 
      if 'iDisplayStart=225' in s:	
        s=s.replace('iDisplayStart=225','iDisplayStart=250')
        return s 
      if 'iDisplayStart=250' in s:	
        s=s.replace('iDisplayStart=250','iDisplayStart=275')
        return s 
      if 'iDisplayStart=275' in s:	
        s=s.replace('iDisplayStart=275','iDisplayStart=300')
        return s 
      if 'iDisplayStart=300' in s:	
        s=s.replace('iDisplayStart=300','iDisplayStart=325')
        return s 
      if 'iDisplayStart=325' in s:	
        s=s.replace('iDisplayStart=325','iDisplayStart=350')
        return s 
      if 'iDisplayStart=350' in s:	
        s=s.replace('iDisplayStart=350','iDisplayStart=375')
        return s 
      if 'iDisplayStart=375' in s:	
        s=s.replace('iDisplayStart=375','iDisplayStart=400')
        return s
      if 'iDisplayStart=400' in s:	
        s=s.replace('iDisplayStart=400','iDisplayStart=425')
        return s 
      if 'iDisplayStart=425' in s:	
        s=s.replace('iDisplayStart=425','iDisplayStart=450')
        return s 
      if 'iDisplayStart=450' in s:	
        s=s.replace('iDisplayStart=450','iDisplayStart=475')
        return s 
      if 'iDisplayStart=475' in s:	
        s=s.replace('iDisplayStart=475','iDisplayStart=500')
        return s 
      if 'iDisplayStart=500' in s:	
        s=s.replace('iDisplayStart=500','iDisplayStart=525')
        return s 
      if 'iDisplayStart=525' in s:	
        s=s.replace('iDisplayStart=525','iDisplayStart=550')
        return s 
      if 'iDisplayStart=550' in s:	
        s=s.replace('iDisplayStart=550','iDisplayStart=575')
        return s 
      if 'iDisplayStart=575' in s:	
        s=s.replace('iDisplayStart=575','iDisplayStart=600')
        return s 
      if 'iDisplayStart=600' in s:	
        s=s.replace('iDisplayStart=600','iDisplayStart=625')
        return s 
      if 'iDisplayStart=625' in s:	
        s=s.replace('iDisplayStart=625','iDisplayStart=650')
        return s 
      if 'iDisplayStart=650' in s:	
        s=s.replace('iDisplayStart=650','iDisplayStart=675')
        return s 
      if 'iDisplayStart=675' in s:	
        s=s.replace('iDisplayStart=675','iDisplayStart=700')
        return s 
      if 'iDisplayStart=700' in s:	
        s=s.replace('iDisplayStart=700','iDisplayStart=725')
        return s 
      if 'iDisplayStart=725' in s:	
        s=s.replace('iDisplayStart=725','iDisplayStart=750')
        return s 
      if 'iDisplayStart=750' in s:	
        s=s.replace('iDisplayStart=750','iDisplayStart=775')
        return s 
      if 'iDisplayStart=775' in s:	
        s=s.replace('iDisplayStart=775','iDisplayStart=800')
        return s 
      if 'iDisplayStart=800' in s:	
        s=s.replace('iDisplayStart=800','iDisplayStart=825')
        return s 
      if 'iDisplayStart=825' in s:	
        s=s.replace('iDisplayStart=825','iDisplayStart=850')
        return s 
      return False 



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
            sUrl = 'http://kinox.to/Search.html?q='+sSearchText  
            sUrl= sUrl.replace(' ','+')
            searchowMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
    
    
    
def kinoxto():
       oGui = cGui()
    
       tarzlistesi= [ ('Suche',"http://www.filmpalast.to/search/alpha/%s"),
                   ('NEUE FILME',"http://kinox.to/"),
		   ('NEWS',"http://kinox.to/"),
		   
		   ('Aktuelle Kinofilme',"http://kinox.to/Kino-filme.html"),
                   ('Filme A-Z',"http://kinox.to/Kino-filme.html"),
                   ('GENRE',"http://kinox.to/Genre/Action"),]
               
       for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'NEUE FILME':
             oGui.addDir(SITE_IDENTIFIER, 'showNews', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'NEWS':
             oGui.addDir(SITE_IDENTIFIER, 'NEWS', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'GENRE':
             oGui.addDir(SITE_IDENTIFIER, 'GENRE', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Aktuelle Kinofilme':
             oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Filme A-Z':
             oGui.addDir(SITE_IDENTIFIER, 'FilmeABC', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'Suche':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        else:
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
       oGui.setEndOfDirectory()
def GENRE():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
            
    sPattern = '<select data-placeholder="Genres.*?name="genre" multiple>(.*?)</select>' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<option value="(.*?)">(.*?)</option>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            page=0                                                                                                                                                                                                                                                                                              
            
            sUrl ='https://kinox.to/aGET/List/?sEcho=1&iColumns=7&sColumns=&iDisplayStart=0&iDisplayLength=25&iSortingCols=1&iSortCol_0=2&sSortDir_0=asc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&bSortable_4=false&bSortable_5=false&bSortable_6=true&additional=%7B"Length"%3A30%2C"fLetter"%3A"A"%2C"fGenre"%3A"'+ aEntry[0]+'"%7D'
            sTitle =aEntry[1]
            sTitle= alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
           
            oGui.addTV(SITE_IDENTIFIER, 'parseMovieResultSite', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def FilmeABC():
    oGui = cGui()
    abc = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for letter in abc:
        sUrl ='https://kinox.to/aGET/List/?sEcho=1&iColumns=7&sColumns=&iDisplayStart=0&iDisplayLength=25&iSortingCols=1&iSortCol_0=2&sSortDir_0=asc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&bSortable_4=false&bSortable_5=false&bSortable_6=true&additional=%7B"Length"%3A30%2C"fLetter"%3A"'+letter+'"%2C"fGenre"%3A"1"%7D'
        sTitle=letter
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)                                                                                                                                                                                                                                                                           
        oGui.addDir(SITE_IDENTIFIER, 'parseMovieResultSite', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def parseMovieResultSite():
    oGui = cGui()                    
    
    oInputParameterHandler = cInputParameterHandler()
    Page = oInputParameterHandler.getValue('siteUrl')
   
    sTitle= oInputParameterHandler.getValue('sMovieTitle')
    
    oRequestHandler = cRequestHandler(Page)
    
    sHtmlContent = oRequestHandler.request();
    sHtmlContent= sHtmlContent.replace('\/','/').replace('\\','')             
                                      
    sPattern = '<span class="Year">.*?,."(.*?)","movie","<a href="(.*?)" onclick="return false;">(.*?)</a>'
     
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
           
            
            
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sprache = str(aEntry[0])
            if '2' in sprache:
                sprache = str(EN_MAIN) 
            
            sprache = str(aEntry[0])
            if  '1' in sprache:
                sprache = str(DE_MAIN)  
            sTitle =aEntry[2]+':'+ sprache
            sTitle = alfabekodla(sTitle).replace(':2',':English')
                 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addTV(SITE_IDENTIFIER, 'showNewshost', sTitle, '', '', '', oOutputParameterHandler)
                      
        cConfig().finishDialog(dialog)
        
         
        sNextPage =sEcho(str(Page))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl',sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'yeniNewshost', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
           

    oGui.setEndOfDirectory()

def yeniNewshost():

    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')                  
    

    
                   
    resp = net.http_GET(url)
    data = resp.content
                            
    data = data.replace('&amp;','&')
    if re.match('.*?<div class="MirrorModule">', data, re.S):    
      Movies = re.findall('<li id="Hoster_.*?" class=".*?" rel="(.*?)"> <div class="Named">(.*?)</div>', data, re.S)
      if Movies:
	for (sUrl,sTitle) in Movies:            
            
            sTitle = alfabekodla(sTitle)
            sUrl = str(URL_HOST) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory() 



def NEWS():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
                
    sPattern = '<ul class="PopupMenu" id="pmNews">(.*?)</ul>' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<li><a href="(.*?)">(.*?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[1]
            
            sTitle= alfabekodla(sTitle)
            sUrl = str(URL_MAIN) + aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
           
            oGui.addTV(SITE_IDENTIFIER, 'showNews', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def showNews():

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

                 
    resp = net.http_GET(url)
    data = resp.content
    
    
    if re.match('.*?<h1>Frisches aus dem Kino vom', data, re.S):    
      Movies = re.findall('<td class="Title img_preview" rel="(.*?)"><a href="(.*?)" title="(.*?)" class="OverlayLabel">', data, re.S)
      if Movies:
	for (sPicture,sUrl,sTitle) in Movies:            
            sTitle = alfabekodla(sTitle)
            sPicture = str(URL_MAIN) + sPicture
            sUrl = str(URL_MAIN) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'showNewshost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
  

def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    sHtmlContent = resp.content
    
    sPattern = '<td class="Icon"><img width="16" height="11" src="/gr/sys/lng/(.*?)" alt="language"></td>.*?<td class="Title"><a href="(.*?)" onclick="return false;">(.*?)</a> <span class="Year">(.*?)</span></td>'
     
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
            sprache = str(aEntry[0])
            if  '1.png' in sprache:            
                sprache = str(DE_MAIN)            
            if  '2.png' in sprache:
                sprache = str(EN_MAIN) 
            sTitle =aEntry[2]+' : '+ sprache+' : '+ aEntry[3]
                          
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture ='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTe38dJ6-hsvuJQZK6-_Zw9yERMLXCEArPLfma7vGdR13h6sejfNw'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showNewshost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
           

        oGui.setEndOfDirectory()
    
def showMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<div class="Opt leftOpt Headlne"><a title="(.*?)" href="(.*?)".*?<div class="Thumb"><img style=".*?src="(.*?)"'
     
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
           
            sTitle =aEntry[0]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showNewshost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
           
        iNextPage = int(iPage) + 1
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)


        oGui.setEndOfDirectory()
   
def showNewshost():

    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')                  
    

    
                   
    resp = net.http_GET(url)
    data = resp.content
    
    data = data.replace('&amp;','&')
    if re.match('.*?<div class="MirrorModule">', data, re.S):    
      Movies = re.findall('<li id="Hoster_.*?" class=".*?" rel="(.*?)"> <div class="Named">(.*?)</div>', data, re.S)
      if Movies:
	for (sUrl,sTitle) in Movies:            
            
            sTitle = alfabekodla(sTitle)
            sUrl = str(URL_HOST) + sUrl
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', '', '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def showfilm():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<p class="hostName">(.*?)</p></li>.*?data-id="([^"]+)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sGenre = cUtil().unescape(aEntry[0])
            sUrl= aEntry[1]
            sTitle = aEntry[0]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sGenre, '', '', '', oOutputParameterHandler)
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
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="ust">.*?<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)".*?<div class="ad"><a href=".*?" title=".*?">(.*?)</a></div>'
    
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
           
            sTitle = (aEntry[2])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def __NextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<a class="pageing button-small rb active">.*?</a> <a class="pageing button-small rb" href=\'(.*?)\'>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(aResult[1][0]) 

    return False             


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    resp = net.http_GET(url)
    data = resp.content
    data = data.replace('\/','/').replace('\\','')
   
    extern_stream_url = re.findall('(?:href|src)="(.*?)"', data, re.S)
    if extern_stream_url:
       sHosterUrl= extern_stream_url[0]

 
    #oHoster = __checkHoster(sHosterUrl)
       oHoster = cHosterGui().checkHoster(sHosterUrl)

       if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
    
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()    
    
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()