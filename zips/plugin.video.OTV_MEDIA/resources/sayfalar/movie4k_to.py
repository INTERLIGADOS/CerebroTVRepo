#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
from cookielib import CookieJar
ALMAN_SINEMA = (True, 'get_tokens')
SITE_IDENTIFIER = 'movie4k_to'
SITE_NAME = 'Movie4k'
import thread
SITE_ICON = 'movie4k.png'



try:
	from resources.lib import cfscrape
except:
	try:
		from resources.lib import cfscrape_old as cfscrape
	except:
		cfscrapeModule = False
	else:
		cfscrapeModule = True
else:
	cfscrapeModule = True

try:
	import requests
except:
	requestsModule = False
else:
	requestsModule = True

import urlparse
import thread
m4k_url = 'http://movie4k.tv/'
m4k_cookies = CookieJar()
m4k_ck = {}
m4k_agent = ''

def m4k_grabpage(pageurl):
	if requestsModule:
		try:
			s = requests.session()
			url = urlparse.urlparse(pageurl)
			headers = {'User-Agent': m4k_agent}
			page = s.get(url.geturl(), cookies=m4k_cookies, headers=headers)
			return page.content
		except:
			pass



def mmovie4kto():
		if requestsModule and cfscrapeModule:
		
			global m4k_ck
			global m4k_agent
			if m4k_ck == {} or m4k_agent == '':
				m4k_ck, m4k_agent = cfscrape.get_tokens(m4k_url)
				requests.cookies.cookiejar_from_dict(m4k_ck, cookiejar=m4k_cookies)
			else:
				s = requests.session()
				url = urlparse.urlparse(m4k_url)
				headers = {'user-agent': m4k_agent}
				page = s.get(url.geturl(), cookies=m4k_cookies, headers=headers, allow_redirects=False)
				if page.status_code == 503 and page.headers.get("Server") == "cloudflare-nginx":
					m4k_ck, m4k_agent = cfscrape.get_tokens(m4k_url)
					requests.cookies.cookiejar_from_dict(m4k_ck, cookiejar=m4k_cookies)
			if __getLanmguage == "de":
				m4k_ck.update({'lang':'de'})
				requests.cookies.cookiejar_from_dict(m4k_ck, cookiejar=m4k_cookies)
			elif __getLanmguage == "en":
				m4k_ck.update({'lang':'en'})
				requests.cookies.cookiejar_from_dict(m4k_ck, cookiejar=m4k_cookies)
			load()
   
                                                                                         
URL_MAIN = 'https://movie4k.tv/'                            
DE_MAIN= 'Deutsch' 
EN_MAIN= 'English' 

def movie4khtml(s):
	s=str(repr(s))[1:-1]
	s=s.replace('test123','innen')
	s=s.replace('<span class="menutag">'," [COLOR FF00FF00]=>")
	s=s.replace('</span>','[/COLOR]')
	s=s.replace('innen-1','innen')
	s=s.replace('<a class="innen" href="./rss-movies.html">RSS feed</a>','')
	s=s.replace('<a class="innen" href="./rss-tvshows.html">RSS feed</a>','')
	s=s.replace('<a class="innen" href="rss-xxx.html">RSS feed</a>','')
	s=s.replace('genres-tvshows.html">Genres','genres-tvshows.html">Serien(TV shows)Genres') 
	s=s.replace('tvshows-updates.html">','tvshows-updates.html">Serien(TV shows)')
	s=s.replace('tipp-show.html">','tipp-show.html">Serien(TV shows)')
	s=s.replace('xxx-updates.html">','xxx-updates.html">XXX ')
	s=s.replace('xxx-all.html">','xxx-all.html">XXX ')
	s=s.replace('genres-xxx.html">','genres-xxx.html">XXX ')
	s=s.replace('tipp-xxx.html">','tipp-xxx.html">XXX ')
	s=s.replace('random-xxx.html">','random-xxx.html">XXX ') 
	
        s=s.replace('\\','')
        s=s.replace('xc3xa4','c3a4')
        return s




 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'http://movie4k.tv/movies.php?list=search&start=&id=0&order=imdbrating&name=&search=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        Searchbaskaulke(sUrl)
        oGui.setEndOfDirectory()
        return

def movie4kto():
  
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://ORHAN/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Suche-Search', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=de')
    oGui.addDir(SITE_IDENTIFIER, 'gerneMovieMenu', 'deutsche Kinofilme', 'https://movie4k.tv/img/ger_flag.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=en')
    oGui.addDir(SITE_IDENTIFIER, 'gerneMovieMenu', 'english cinema movies', 'https://movie4k.tv/img/us_flag.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=fr')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'french cinema movies', 'https://movie4k.tv/img/french.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=es')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'spanish cinema movies', 'https://movie4k.tv/img/spain.png', oOutputParameterHandler)
                                                  
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=it')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'italian cinema movies', 'https://movie4k.tv/img/italia.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=jp')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'japanese cinema movies', 'https://movie4k.tv/img/japan.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=tr')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'turkish cinema movies', 'https://movie4k.tv/img/turkey.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://movie4k.tv/index.php?lang=ru')
    oGui.addDir(SITE_IDENTIFIER, 'baskaulke', 'russia cinema movies', 'https://movie4k.tv/img/russia.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()	


def Searchbaskaulke(sUrl): #affiche les genres
    oGui = cGui()
    
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                                                                                
                                                                             
    sPattern = '<TR[^>]*>\s*<TD[^>]*id="tdmovies"[^>]*>\s*<a href="([^"]+)">(.*?)</a>.*?<img[^>]*border=0[^>]*src="/img/([^"]+)"[^>]*>.*?</TR>'     
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
            sprache = str(aEntry[2])
            if  'us_ger_small.png' in sprache:            
                sprache = str(DE_MAIN)            
            if  'us_flag_small.png' in sprache:
                sprache = str(EN_MAIN) 
            sTitle =aEntry[1]+' : '+ sprache
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture ='http://movie4k.tv/img/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 

def gerneMovieMenu():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
                                                     
    oRequestHandler = cRequestHandler(sUrl)          
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =movie4khtml(sHtmlContent)                                       
    sPattern = '<div id="menue">(.*?)<FORM' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<a class="innen" href="(.*?)">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            Link = 'https://movie4k.tv/' +aEntry[0]
           
            sTitle =aEntry[1]
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            if "index.php" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'KinofilmeMovies',  sTitle, 'genres.png', oOutputParameterHandler)
            elif "movies-updates.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
            elif "tipp-film.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
            elif "movies-all.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
            elif "genres-movies.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneMovie', sTitle, 'genres.png', oOutputParameterHandler)
            elif "featuredtvshows.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'KinofilmeMovies', sTitle, 'genres.png', oOutputParameterHandler)
            elif "tvshows-updates.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
            elif "tipp-show.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
            elif "tvshows-all.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
            elif "genres-tvshows.html" in Link:
             oGui.addDir(SITE_IDENTIFIER, 'gerneShow', sTitle, 'genres.png', oOutputParameterHandler)
           
            else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def gerneXXX():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
                                                     
    oRequestHandler = cRequestHandler(sUrl)          
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =movie4khtml(sHtmlContent)                                       
    sPattern = '<TABLE id="tablemovies" cellpadding=.*? cellspacing=.*?>(.*?)</TABLE>' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<TD id="tdmovies" width="155"><a href="(xxx-genre.*?)">(.*?)</a></TD>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            Link = 'https://movie4k.tv/' +aEntry[0]
           
            sTitle =aEntry[1]
           
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies',  sTitle, 'genres.png', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def gerneShow():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
                                                     
    oRequestHandler = cRequestHandler(sUrl)          
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =movie4khtml(sHtmlContent)                                       
    sPattern = '<TABLE id="tablemovies" cellpadding=.*? cellspacing=.*?>(.*?)</TABLE>' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<TD id="tdmovies" width="155"><a href="(tvshows-genre.*?)">(.*?)</a></TD>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            Link = 'https://movie4k.tv/' +aEntry[0]
           
            sTitle =aEntry[1]
           
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowSER',  sTitle, 'genres.png', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def gerneMovie():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
                                                     
    oRequestHandler = cRequestHandler(sUrl)          
    sHtmlContent = oRequestHandler.request();
    sHtmlContent =movie4khtml(sHtmlContent)                                       
    sPattern = '<TABLE id="tablemovies" cellpadding=.*? cellspacing=.*?>(.*?)</TABLE>' 
    oParser = cParser()
    sult = oParser.parse(sHtmlContent, sPattern)
    Pattern = '<TD id="tdmovies" width="155"><a href="(movies-genre.*?)">(.*?)</a></TD>'
    oParser = cParser()
    aResult = oParser.parse(sult, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            Link = 'https://movie4k.tv/' +aEntry[0]
           
            sTitle =aEntry[1]
           
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies',  sTitle, 'genres.png', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def baskaulke(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
                                                                                              
    sPattern = '<TR[^>]*>\s*<TD[^>]*id="tdmovies"[^>]*>\s*<a href="([^"]+)">(.*?)</a>.*?<img[^>]*border=0[^>]*src="([^"]+)"[^>]*>.*?</TR>'    
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
           
            Link = 'https://movie4k.tv/' +aEntry[0]
           
            sTitle  = sTitle  + ': [COLOR skyblue]' + aEntry[2] +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
def KinofilmeMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent=sHtmlContent.replace('<div style="float: left;">','<div style="float:left">').replace('" border=0 width=105 height=150 alt="','" alt="')                                                                             
                                     
                
    sPattern = '<div style="float:left"><a href=(.*?)"><img src="(.*?)" alt="(.*?)"'
     
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
            sPicture = str(aEntry[1])
            
            sTitle =aEntry[2]
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
   
    oGui.setEndOfDirectory()   

def gerneshowMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                                                                               
                                                                     
    sPattern = '<TR[^>]*>\s*<TD[^>]*id="tdmovies"[^>]*>\s*<a href="([^"]+)">(.*?)</a>.*?<img[^>]*border=0[^>]*src="/img/([^"]+)"[^>]*>.*?</TR>'     
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
            sprache = str(aEntry[2])
            if  'us_ger_small.png' in sprache:            
                sprache = str(DE_MAIN)            
            if  'us_flag_small.png' in sprache:
                sprache = str(EN_MAIN) 
            sTitle =aEntry[1]+' : '+ sprache
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture ='https://movie4k.tv/img/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
   
    oGui.setEndOfDirectory()                          
def __checkForNextPage(sHtmlContent):                     
    sPattern = '<div id="boxwhite">.+?</div><div id="boxgrey"><a href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = str(URL_MAIN) + aResult[1][0]
        return sUrl
        
    return False
def mparseHoster():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = getUrl(sUrl).result
    
  
    

    sPattern = 'id="maincontent5".*?(?:target="_blank" href|iframe[^<]+src|value)="([^"]+)".*?id="underplayer">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def gerneshowSER():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                                                                                
                
    sPattern = '<TD id="tdmovies" width="538"><a href="(.*?)">(.*?)</a>.*?<TD id="tdmovies"><img border="0" src="/img/(.*?)"'
     
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
            sprache = str(aEntry[2])
            if  'us_ger_small.png' in sprache:            
                sprache = str(DE_MAIN)            
            if  'us_flag_small.png' in sprache:
                sprache = str(EN_MAIN) 
            sTitle =aEntry[1]+' : '+ sprache
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture ='https://movie4k.tv/img/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'gerneshowSER2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'gerneshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
   
    oGui.setEndOfDirectory()   

def gerneshowSER2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
                                                                                
                
    sPattern = '<TD id="tdmovies" width="538"><a href="(.*?)">(.*?)</a></TD>.*?<TD id="tdmovies"><img border="0" src="/img/(.*?)"'
     
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
            sprache = str(aEntry[2])
            if  'us_ger_small.png' in sprache:            
                sprache = str(DE_MAIN)            
            if  'us_flag_small.png' in sprache:
                sprache = str(EN_MAIN) 
            sTitle =aEntry[1]+' : '+ sprache
                          
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
            sPicture ='https://movie4k.tv/img/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showNewshost', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showHosters', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
   
    oGui.setEndOfDirectory()   


def showHosters():
   
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    oRequestHandler = cRequestHandler(sUrl)                            
    sHtmlContent = getUrl(sUrl).result
    sHtmlContent = sHtmlContent.replace('\\',"")
    
    oParser = cParser()
    
    sPattern = '<tr id="tablemoviesindex2">.*?<a href="([^"]+)">([^<]+)<.*?alt="(.*?) .*?width="16">.*?</a>.*?smileys/([1-9]).gif"'
    oParser = cParser()             
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
          
            sTitle = alfabekodla(aEntry[2]+':'+aEntry[1])
            Url = URL_MAIN+ aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
            oGui.addTV(SITE_IDENTIFIER, 'parseHoster', sTitle, '','https://movie4k.tv/img/logo.png', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def __getHosterFile(oGui, sHoster, sUrl, sPattern, sHtmlContent, sMovieTitle):
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    if (aResult[0] == True):
        if (sUrl == False):
            sStreamUrl = aResult[1][0]
        else:
            sStreamUrl = sUrl + aResult[1][0]

        oHoster = cHosterHandler().getHoster(sHoster)
	if (sMovieTitle != False):
	    oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sStreamUrl)
        oGui.setEndOfDirectory()
        return True

    return False

def __getLanmguage(sString):
    if (sString == 'us_ger_small'):
        return ' (DE)'
    return ' (DE)'

def __createMainMenuItem(oGui, sTitle, sUrl, sFunction):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setFunction(sFunction)
    oGuiElement.setTitle(sTitle)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('sUrl', sUrl)    
    oGui.addFolder(oGuiElement, oOutputParameterHandler)

def parseHoster():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    


    sPattern = '<a target="_blank" href="(.+?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            sHosterUrl = str(aEntry)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    