#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
ALMAN_SINEMA = (True, 'load')
SITE_IDENTIFIER = 'movie2k_com'
SITE_NAME = 'Movie2k.com'

SITE_ICON = 'movie4k.png'
URL_MAIN = 'http://www.movie4k.to/'
URL_MOVIES = URL_MAIN + 'index.php?lang=de'
URL_TOP_MOVIES = 'http://www.movie4k.to/movies-top.html'
URL_MOVIES_GENRE = URL_MAIN + 'genres-movies.html'
URL_MOVIES_ALL_WITH_CHARACTER = 'http://www.m2k.to/movies-all.html'
URL_MOVIES_ALL = URL_MAIN + 'movies-all'
URL_SERIES = 'http://www.movie4k.to/tvshows_featured.php'
URL_SERIES_ALL = 'http://www.movie4k.to/tvshows-all.html'
URL_SERIES_TOP = 'http://www.movie4k.to/tvshows-top.html'
URL_SERIES_GENRE = 'http://www.movie4k.to/genres-tvshows.html'

URL_SEARCH = 'http://www.movie4k.to/movies.php?list=searchnew534'
URL_XXX = URL_MAIN + 'xxx-updates.html'
URL_XXX_ALL = URL_MAIN +'xxx-all'
URL_XXX_GENRE = URL_MAIN + 'genres-xxx.html'


def load():
    
        
    oGui = cGui()
    __createMainMenuItem(oGui, 'Filme', '', 'showMovieMenu')
    __createMainMenuItem(oGui, 'Serien', '', 'showSeriesMenu')
    
    __createMainMenuItem(oGui, 'XXX', '', 'showXXXMenu')
    __createMainMenuItem(oGui, 'Suche', '', 'showSearch')
    oGui.setEndOfDirectory()

def showMovieMenu():
    oGui = cGui()
    __createMainMenuItem(oGui, 'Kinofilme', URL_MOVIES, 'showMoviesAndSeries')
    __createMainMenuItem(oGui, 'Alle Filme', URL_MOVIES_ALL, 'showCharacters')
    __createMainMenuItem(oGui, 'Genre', URL_MOVIES_GENRE, 'showGenre')
    oGui.setEndOfDirectory()

def showSeriesMenu():
    oGui = cGui()
    __createMainMenuItem(oGui, 'Featured', URL_SERIES, 'showMoviesAndSeries')
    __createMainMenuItem(oGui, 'Alle Serien', URL_SERIES_ALL, 'showAllSeries')
    __createMainMenuItem(oGui, 'Top Serien', URL_SERIES_TOP, 'parseMovieSimpleList')
    __createMainMenuItem(oGui, 'Genre', URL_SERIES_GENRE, 'showGenre')
    oGui.setEndOfDirectory()

def showXXXMenu():
    oGui = cGui()
    __createMainMenuItem(oGui, 'Aktuelles', URL_XXX, 'showMoviesAndSeries')
    __createMainMenuItem(oGui, 'Alle XXXFilme', URL_XXX_ALL, 'showCharacters')
    __createMainMenuItem(oGui, 'Genre', URL_XXX_GENRE, 'showGenre')
    oGui.setEndOfDirectory()

def showCharacters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    if (oInputParameterHandler.exist('sUrl')):
        baseUrl = oInputParameterHandler.getValue('sUrl')


        __createCharacters(oGui, '#', baseUrl)
        import string   
        for letter in string.uppercase[:26]:
           __createCharacters(oGui, letter, baseUrl) 
    oGui.setEndOfDirectory()
def __createCharacters(oGui, sCharacter, sBaseUrl):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setFunction('parseMovieSimpleList') 
    oGuiElement.setTitle(sCharacter)
    if (sCharacter == '#'):
        sUrl = sBaseUrl + '-1-1.html'
    else:
        sUrl = sBaseUrl + '-' + str(sCharacter) + '-1.html'
        
    oOutputParameterHandler = ParameterHandler()
    oOutputParameterHandler.setParam('sUrl', sUrl)
    oGui.addFolder(oGuiElement, oOutputParameterHandler)        

def showAllSeries():
    oInputParameterHandler = cInputParameterHandler()
    if (oInputParameterHandler.exist('sUrl')):
        sUrl = oInputParameterHandler.getValue('sUrl')

        oRequest = cRequestHandler(sUrl)
        sHtmlContent = oRequest.request()
        __parseMovieSimpleList(sHtmlContent, 1)
def showAdult():
    oConfig = bConfig()
    if oConfig.getSetting('showAdult')=='true':    
        return True
    return False 

def showSearch():    
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        __callSearch(sSearchText)

    oGui.setEndOfDirectory()

def __callSearch(sSearchText):
    oRequest = cRequestHandler(URL_SEARCH)
    oRequest.setRequestType(cRequestHandler.REQUEST_TYPE_POST)
    oRequest.addParameters('search', sSearchText)
    sHtmlContent = oRequest.request()

    __parseMovieSimpleList(sHtmlContent, 1)
    

def __checkForNextPage(sHtmlContent, iCurrentPage):
    iNextPage = int(iCurrentPage) + 1
    iNextPage = str(iNextPage) + ' '
    
    sPattern = '<a href="([^"]+)">' + iNextPage + '</a>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return aResult[1][0]
    return False

def showGenre():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    if (oInputParameterHandler.exist('sUrl')):
        sUrl = oInputParameterHandler.getValue('sUrl')

        oRequest = cRequestHandler(sUrl)
        sHtmlContent = commonon().getPage(sUrl)

        sPattern = '<TR>.*?<a href="([^"]+)">([^<]+)</a>.*?>([^<]+)</TD>'

        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)

        if (aResult[0] == True):
            for aEntry in aResult[1]:
                oGuiElement = cGuiElement()
                oGuiElement.setSiteName(SITE_IDENTIFIER)
                oGuiElement.setFunction('parseMovieSimpleList')

                sTitle = aEntry[1] + ' (' + aEntry[2] + ')'

                oGuiElement.setTitle(sTitle)
                sUrl =URL_MAIN + aEntry[0]
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('sUrl', sUrl)
                oGui.addFolder(oGuiElement, oOutputParameterHandler)

        oGui.setEndOfDirectory()

def parseMovieSimpleList():
    oInputParameterHandler = cInputParameterHandler()

    if (oInputParameterHandler.exist('iPage')):
        iPage = oInputParameterHandler.getValue('iPage')
    else:
        iPage = 1

    if (oInputParameterHandler.exist('sUrl')):
        sUrl = oInputParameterHandler.getValue('sUrl')

        oRequest = cRequestHandler(sUrl)
        sHtmlContent = commonon().getPage(sUrl)

        __parseMovieSimpleList(sHtmlContent, iPage)

def __parseMovieSimpleList(sHtmlContent, iPage):
    oGui = cGui()
    sPattern = '<TR[^>]*>\s*<TD[^>]*id="tdmovies"[^>]*>\s*<a href="([^"]+)">(.*?)</a>.*?<img[^>]*border=0[^>]*src="/img/([^"]+)"[^>]*>.*?</TR>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        for aEntry in aResult[1]:
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setFunction('showHoster')

            sTitle = aEntry[1].strip().replace('\t', '') +  __getLanmguage(aEntry[2])
            oGuiElement.setTitle(sTitle)
            sUrl = URL_MAIN + aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('sUrl', sUrl)
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

    sNextUrl = __checkForNextPage(sHtmlContent, iPage)    
    if (sNextUrl != False):
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setFunction('parseMovieSimpleList')
        oGuiElement.setTitle('[COLOR teal]Next >>>[/COLOR]')

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sUrl', sNextUrl)
        oOutputParameterHandler.addParameter('iPage', int(iPage) + 1)
        oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showMoviesAndSeries():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    if (oInputParameterHandler.exist('sUrl')):
        sUrl = oInputParameterHandler.getValue('sUrl')


        oRequest = cRequestHandler(sUrl)
        sHtmlContent = commonon().getPage(sUrl)
       

        sPattern = '<div style="float:left">.*?<a href="(.*?)"><img src="(.*?)" border.*? style=".*?" alt="(.*?)" title=".*?"></a>.*?<img src="/img/(.*?).png"'

                                                                                                                                             
        oParser = cParser()                                                                                                                
        aResult = oParser.parse(sHtmlContent, sPattern)

        if (aResult[0] == True):
            for aEntry in aResult[1]:
                
                sPicture = aEntry[1]
                

                sTitle = aEntry[2].strip().replace('kostenlos', '') +  __getLanmguage(aEntry[3]) 
                
                sUrl = URL_MAIN + aEntry[0]
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                oGui.addMovie(SITE_IDENTIFIER, 'parseHoster', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def __createInfo(oGui, sHtmlContent):
    sPattern = '<img src="thumbs/([^"]+)".*?<div class="beschreibung">(.*?)<'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setTitle('info (press Info Button)')
            oGuiElement.setThumbnail(URL_MAIN + 'thumbs/' + str(aEntry[0]))
            oGuiElement.setFunction('dummyFolder')
            oGuiElement.setDescription(cUtil().removeHtmlTags(str(aEntry[1])))
            oGui.addFolder(oGuiElement)

def dummyFolder():
    oGui = cGui()
    oGui.setEndOfDirectory()

def showHoster():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    if (oInputParameterHandler.exist('sUrl')):
        sUrl = oInputParameterHandler.getValue('sUrl')
        
        oRequest = cRequestHandler(sUrl)
        sHtmlContent = commonon().getPage(sUrl)

        __createInfo(oGui, sHtmlContent)
        
        sPattern = '<tr id="tablemoviesindex2">.*?<a href="([^"]+)">([^<]+)<.*?width="16">(.*?)</a>.*?alt="([^"]+)"'
        #sPattern = '<tr id="tablemoviesindex2">.*?<a href="([^"]+)">.*?width="16">(.*?)</a>.*?alt="([^"]+)"'

        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        
        if (aResult[0] == True):
            for aEntry in aResult[1]:
                sHoster = aEntry[2].strip()
                if (__checkHoster(sHoster) == True):

                    oGuiElement = cGuiElement()
                    oGuiElement.setSiteName(SITE_IDENTIFIER)
                    oGuiElement.setFunction('parseHoster')

                    sTitle = aEntry[1] + ' - ' + aEntry[2] + ' - ' + aEntry[3]
                    oGuiElement.setTitle(sTitle)

                    sUrl = URL_MAIN + aEntry[0]
                    
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('sUrl', sUrl)
                    oOutputParameterHandler.addParameter('sTitle', sTitle)
                    oOutputParameterHandler.addParameter('sHoster', sHoster)
                    oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkHoster(sHoster):
    if (sHoster == 'Mystream'):
        return True

    if (sHoster == 'loaded.it'):
        return True

    if (sHoster == 'Novamov'):
        return True

    if (sHoster == 'Stream2k'):
        return True

    #if (sHoster == 'UploadC'):
    #    return True

    #if (sHoster == 'Loombo'):
    #    return True

    if (sHoster == 'VideoWeed'):
        return True

    if (sHoster == 'Streamesel'):
        return True

    if (sHoster == 'MegaVideo'):
        return True

    if (sHoster == 'Duckload'):
        return True

    if (sHoster == 'Movshare'):
        return True

    if (sHoster == 'FileStage'):
        return True

    if (sHoster == 'Tubeload'):
        return True

    if (sHoster == 'Screen4u'):
        return True

    if (sHoster == 'CheckThisV'):
        return True

    if (sHoster == 'Xvidstage'):
        return True

    if (sHoster == 'DivX Hoste'):
        return True

    return False

def __getMovieTitle(sHtmlContent):
    sPattern = '<h1 style="font-size:18px;">(.*?)<img'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
	return str(aResult[1][0]).strip()

    return False

def showHosters():
   
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)                            
    sHtmlContent = commonon().getPage(sUrl)
    sHtmlContent = (str(sHtmlContent)).replace('\\','')
    oParser = cParser()
    sPattern = '</SCRIPT><tr id="tablemoviesindex2">(.+?)</table>'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)">.*?<.*?lt="(.*?)"'
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
            Url = URL_MAIN+ aEntry[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'parseHoster', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def parseHoster():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = commonon().getPage(sUrl)
    
  
    

    sPattern = '<BR>.*?<a target="_blank" href="(.*?)">'
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
    return ' (EN)'

def __createMainMenuItem(oGui, sTitle, sUrl, sFunction):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setFunction(sFunction)
    oGuiElement.setTitle(sTitle)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('sUrl', sUrl)    
    oGui.addFolder(oGuiElement, oOutputParameterHandler)