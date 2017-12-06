#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   

SITE_IDENTIFIER = 'filmpalast_to'
SITE_NAME = 'Filmpalast'
SITE_DESC = 'Replay TV'

URL_MAIN = 'http://filmpalast.to'
import re,json
ALMAN_SINEMA = (True, 'showGenre') 

baseurl = 'http://filmpalast.to/'

streamurl = 'http://filmpalast.to/stream/{id}/1'
def getStreamSRC(id):
	from t0mm0.common.net import Net
	net = Net()
	data = net.http_POST(streamurl.replace('{id}', id), {'streamID':id}, {'Referer':baseurl, 'X-Requested-With':'XMLHttpRequest'}).content
	for url in re.findall('"url":"([^"]+)"', data, re.S|re.I): return url.replace('\\','')

def decodeHtml(data):

	
		data = data.decode('unicode-escape').encode('UTF-8') 
		return data
from kinox_to import kinoxto
from movie4k_to import movie4kto
from netzkino import netzkino
from hdfilme_tv import hdfilme
from onlinefilme_biz import Onlinefilme
from streamkiste_tv import streamkiste
def almanKINO():
                      
    oGui = cGui()              
    liste = []
    liste.append( ['HDFilme','http://hdfilme.tv/themes/hdfilme/assets/img/logo.png'])
    liste.append( ['Filmpalast','http://filmpalast.to/themes/downloadarchive/images/logo.png'] ) 
    liste.append( ['Kinox','https://raw.githubusercontent.com/xStream-Kodi/plugin.video.xstream/nightly/resources/art/sites/kinox.png'])
    liste.append( ['Movie4kto','https://movie4kto.site/img/logo.png'] ) 
    liste.append( ['Netzkino','http://pmd.bilder.netzkino.de/bilder/webseite/logo_header_small.png'])
    liste.append( ['streamkiste_tv','http://streamkiste.tv/icon/android-chrome-192x192.png'])
    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Filmpalast':
             oGui.addMovie(SITE_IDENTIFIER, 'filmpalast',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Kinox':
             oGui.addMovie(SITE_IDENTIFIER, 'kinoxto',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Movie4kto':
             oGui.addMovie(SITE_IDENTIFIER, 'movie4kto', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Netzkino':
             oGui.addMovie(SITE_IDENTIFIER, 'netzkino', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'HDFilme':
             oGui.addMovie(SITE_IDENTIFIER, 'hdfilme', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'streamkiste_tv':
             oGui.addMovie(SITE_IDENTIFIER, 'streamkiste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Kino.de':
             oGui.addMovie(SITE_IDENTIFIER, 'load', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                                   
    oGui.setEndOfDirectory()                    
 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://filmpalast.to/search/title/'+sSearchText  
            sUrl= sUrl.replace(' ','%20')
            searchowMovies(sUrl)
            oGui.setEndOfDirectory()
            return  


def filmpalast():
    oGui = cGui()
    tarzlistesi= [ ('Suche',"http://www.filmpalast.to/search/alpha/%s"),
                   ('NEUE FILME',"http://www.filmpalast.to/movies/new"),
		   ('TOP FILME',"http://www.filmpalast.to/movies/top"),
		   ('SERIEN',"http://www.filmpalast.to/serien/view"),
		   ('Abenteuer',"http://filmpalast.to/search/genre/Abenteuer"),
		   ('Action',"http://filmpalast.to/search/genre/Action"),
                            ('Fantasy',"http://www.filmpalast.to/search/genre/Fantasy"),
                            ('Animation',"http://www.filmpalast.to/search/genre/Animation"),
                            ('Biography',"http://www.filmpalast.to/search/genre/biography/"),
                            ('Kom�die',"http://www.filmpalast.to/search/genre/Kom�die"),
                            ('Krimi',"http://www.filmpalast.to/search/genre/Krimi"),
                            ('Documentary',"http://www.filmpalast.to/search/genre/documentary/"),
                            ('Drama',"http://www.filmpalast.to/search/genre/Drama"),
                            ('Familie',"http://www.filmpalast.to/search/genre/Familie"),
                            ('History',"http://www.filmpalast.to/search/genre/history/"),
                            ('Horror',"http://www.filmpalast.to/search/genre/Horror"),
                            ('Music',"http://www.filmpalast.to/search/genre/music/"),
                            ('Musical',"http://www.filmpalast.to/search/genre/musical/"),
                            ('Mystery',"http://www.filmpalast.to/search/genre/Mystery"),
                            ('Romantik',"http://www.filmpalast.to/search/genre/Romantik"),
                            ('Sci-Fi',"http://www.filmpalast.to/search/genre/Sci-Fi"),
                            ('Short',"http://www.filmpalast.to/search/genre/short/"),
                            ('Sport',"http://www.filmpalast.to/search/genre/sport/"),
                            ('Thriller',"http://www.filmpalast.to/search/genre/thriller/"),
                            ('Krieg',"http://www.filmpalast.to/search/genre/Krieg"),
                            ('Western',"http://www.filmpalast.to/search/genre/western/"),
                            ('Movie Title 0-9',"http://www.filmpalast.to/search/alpha/0-9/"),
                            ('Movie Title A',"http://www.filmpalast.to/search/alpha/a/"),
                            ('Movie Title B',"http://www.filmpalast.to/search/alpha/b/"),
                            ('Movie Title C',"http://www.filmpalast.to/search/alpha/c/"),
                            ('Movie Title D',"http://www.filmpalast.to/search/alpha/d/"),
                            ('Movie Title E',"http://www.filmpalast.to/search/alpha/e/"),
                            ('Movie Title F',"http://www.filmpalast.to/search/alpha/f/"),
                            ('Movie Title G',"http://www.filmpalast.to/search/alpha/g/"),
                            ('Movie Title H',"http://www.filmpalast.to/search/alpha/h/"),
                            ('Movie Title I',"http://www.filmpalast.to/search/alpha/i/"),
                            ('Movie Title J',"http://www.filmpalast.to/search/alpha/j/"),
                            ('Movie Title K',"http://www.filmpalast.to/search/alpha/k/"),
                            ('Movie Title L',"http://www.filmpalast.to/search/alpha/l/"),
                            ('Movie Title M',"http://www.filmpalast.to/search/alpha/m/"),
                            ('Movie Title N',"http://www.filmpalast.to/search/alpha/n/"),
                            ('Movie Title O',"http://www.filmpalast.to/search/alpha/o/"),
                            ('Movie Title P',"http://www.filmpalast.to/search/alpha/p/"),
                            ('Movie Title Q',"http://www.filmpalast.to/search/alpha/q/"),
                            ('Movie Title R',"http://www.filmpalast.to/search/alpha/r/"),
                            ('Movie Title S',"http://www.filmpalast.to/search/alpha/s/"),
                            ('Movie Title T',"http://www.filmpalast.to/search/alpha/t/"),
                            ('Movie Title U',"http://www.filmpalast.to/search/alpha/u/"),
                            ('Movie Title V',"http://www.filmpalast.to/search/alpha/v/"),
                            ('Movie Title W',"http://www.filmpalast.to/search/alpha/w/"),
                            ('Movie Title X',"http://www.filmpalast.to/search/alpha/x/"),
                            ('Movie Title Y',"http://www.filmpalast.to/search/alpha/y/"),
                            ('Movie Title Z',"http://www.filmpalast.to/search/alpha/z/"),]

               
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'DIZILER-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SINEMALAR-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'sinemaABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SERIEN':
             oGui.addDir(SITE_IDENTIFIER, 'showSHOW', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Suche':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()

def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    data = resp.content
   
    sHtmlContent = re.findall('<small class="rb">.*?<a href="(.*?)" title=".*?"> <img src="(.*?)" class="cover-opacity" alt="(.*?)"/>', data, re.S)
         
    for sUrl,sPicture,sTitle in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'showfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
page =0
def showpage(sUrl):
           
            sUrl = "%s/%s" % (sUrl, str(page+ 1))
            showSinema(sUrl)
            return 

def showSHOW(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url =  sSearch
        request = urllib2.Request(url,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
        
 
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern ='</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
    
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
           
            sTitle = cUtil().unescape(aEntry[1])
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + Url
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                                                                     
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showStaffel', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSHOW', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
                
    if not sSearch:
        oGui.setEndOfDirectory()

def ddizizleABC():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl') 
    url = HTTPKIR(urll)
       
        
    name ='test'
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


def showStaffel(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url =  sSearch
        request = urllib2.Request(url,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
        
 
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern ='</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sPicture = oInputParameterHandler.getValue('sThumbnail')
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
    
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<li class="stitle">.*?<a id="staffId_" href="(.*?)" class="getStaffelStream" data-sid=".*?">.*?<small>(.*?)</small>'
                                         
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
           
            sTitle = cUtil().unescape(aEntry[1])
                            
            Url = str(aEntry[0])
           
          
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSHOW', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
                
    if not sSearch:
        oGui.setEndOfDirectory()
def showSinema(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url =  sSearch
        request = urllib2.Request(url,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
        
 
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern ='</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
    
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
           
            sTitle = cUtil().unescape(aEntry[1])
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + Url
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
                
    if not sSearch:
        oGui.setEndOfDirectory()
   
def showfilm():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
                                                 
    sPattern = '<p class="hostName">(.*?)</p></li>.*?<a class=".*?" data-id="(.*?)"'
    
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
            sTitle = aEntry[0].decode("latin-1").encode("utf-8")
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sGenre, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def showMovies(sSearch = ''):
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
        sPattern = '<small class="rb">.*?<a href="(.*?)" title=".*?"> <img src="(.*?)" class="cover-opacity" alt="(.*?)"/>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
    
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
           
            sTitle = cUtil().unescape(aEntry[2])
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
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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
           
            sTitle = cUtil().unescape(aEntry[2])
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
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
 
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
    sHtmlContent = sHtmlContent.replace("'",'"')    
    sPattern = '<a class="pageing button-small rb active">.*?</a> <a class="pageing button-small rb" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(aResult[1][0]) 
         
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
                      

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    streamid = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl = getStreamSRC(streamid)
    sHosterUrl = sUrl
    
    sMovieTitle = alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
