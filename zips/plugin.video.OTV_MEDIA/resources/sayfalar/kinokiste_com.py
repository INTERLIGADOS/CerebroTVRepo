#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
from xstream import * 
MOVIE_COMMENTS = (True, 'load')
SITE_IDENTIFIER = 'kinokiste_com'
SITE_NAME = 'KinoKiste.com'

URL_MAIN = 'http://movie4k.to'
URL_CINEMA = 'http://movie4k.to/movies-updates.html'
URL_NEW = 'http://movie4k.to/o/neue-filme/'
URL_BLOCKBUSTER = 'http://movie4k.to/blockbuster/'
URL_ALL = 'http://movie4k.to/movies-all.html'

def load():
    
        
    oGui = cGui()
    __createMenuEntry(oGui, 'showMovieEntries', 'Aktuelle Kinofilme', URL_CINEMA, 1)
    __createMenuEntry(oGui, 'showMovieEntries', 'Neue Filme', URL_NEW, 1)
    __createMenuEntry(oGui, 'showMovieEntries', 'Blockbuster', URL_BLOCKBUSTER, 1)
    __createMenuEntry(oGui, 'showAllMovies', 'Filme A-Z', URL_ALL)
    __createMenuEntry(oGui, 'showGenre', 'Genre', URL_MAIN)
    __createMenuEntry(oGui, 'showSearch', 'Suche', URL_MAIN)
    oGui.setEndOfDirectory()

def __createMenuEntry(oGui, sFunction, sLabel, sUrl, iPage = False):
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setFunction(sFunction)
    oGuiElement.setTitle(sLabel)
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    if (iPage != False):
        oOutputParameterHandler.addParameter('page', iPage)
    oGui.addFolder(oGuiElement, oOutputParameterHandler)

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sSearchText = sSearchText.replace(' ', '+')
        oRequestHandler = cRequestHandler(URL_MAIN + '/')
        oRequestHandler.addParameters('q', sSearchText)
        sUrl = oRequestHandler.getRequestUri()        
        __showMovieEntries(sUrl)
        return

    oGui.setEndOfDirectory()

def showMovieEntries():    
    oInputParameterHandler = cInputParameterHandler()
    sSiteUrl = oInputParameterHandler.getValue('siteUrl')
    iPage = oInputParameterHandler.getValue('page')    
    __showMovieEntries(sSiteUrl, iPage)

def __showMovieEntries(sSiteUrl, iPage = False):
    if (iPage != False):
        sUrl = str(sSiteUrl) + str(iPage) + '/'
    else:
        sUrl = sSiteUrl

    oGui = cGui()
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<div class="mbox.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)".*?<div class="decor">.*?<div class="title">(.*?)</div>'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
         for aEntry in aResult[1]:
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setFunction('showHosters')
            oGuiElement.setThumbnail(URL_MAIN + str(aEntry[1]))
            oGuiElement.setDescription(str(aEntry[2]))
	    sTitle = cUtil().removeHtmlTags(str(aEntry[3]))
            oGuiElement.setTitle(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + str(aEntry[0]))
	    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

    if (iPage != False):
        bNextPage = __checkForNextSite(sHtmlContent)
        if (bNextPage == True):
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setFunction('showMovieEntries')
            oGuiElement.setTitle('next..')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sSiteUrl)
            oOutputParameterHandler.addParameter('page', int(iPage) + 1)
            oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()
       

def __checkForNextSite(sHtmlContent):
    sPattern = '<div class="pager bottom">(.*?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sHtmlContent = aResult[1][0]
        sPattern = '<a href="([^"]+)" title="N.*?" class="next">'
                
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)        
        if (aResult[0] == True):
            return True

    return False;

def showAllMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<div class="actorsindex">(.*?)<div class="boxfooter">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sHtmlContent = aResult[1][0]

        sPattern = '<li><a href="([^"]+)" title=".*?">(.*?)</a></li>'
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            for aEntry in aResult[1]:
                oGuiElement = cGuiElement()
                oGuiElement.setSiteName(SITE_IDENTIFIER)
                oGuiElement.setFunction('showHosters')
		sTitle = cUtil().removeHtmlTags(str(aEntry[1]))
                oGuiElement.setTitle(sTitle)

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + str(aEntry[0]))
		oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<ul class="subnav">(.*?)</ul>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sHtmlContent = aResult[1][0]

        sPattern = '<a href="([^"]+)" title=".*?">(.*?)</a></li>'
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            for aEntry in aResult[1]:
                oGuiElement = cGuiElement()
                oGuiElement.setSiteName(SITE_IDENTIFIER)
                oGuiElement.setFunction('showMovieEntries')
                oGuiElement.setTitle(cUtil().removeHtmlTags(str(aEntry[1])))

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + str(aEntry[0]))
                oOutputParameterHandler.addParameter('page', 1)
                oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def __createInfo(oGui, sHtmlContent):
    sPattern = '<div class="cover"><img src="([^"]+)".*?<div class="excerpt".*?<div>(.*?)<div class="fix">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(SITE_IDENTIFIER)
            oGuiElement.setTitle('info (press Info Button)')
            oGuiElement.setThumbnail(URL_MAIN  + str(aEntry[0]))
            oGuiElement.setFunction('dummyFolder')
            oGuiElement.setDescription(cUtil().removeHtmlTags(str(aEntry[1])).replace('\t', ''))
            oGui.addFolder(oGuiElement)

def dummyFolder():
    oGui = cGui()
    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    __createInfo(oGui, sHtmlContent)

    sPattern = '<ul class="streamlist">(.*?)</ul>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sHtmlContent = aResult[1][0]

        sPattern = '<a href="([^"]+)".*?>(.*?)</a>'
        oParser = cParser()
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
             for aEntry in aResult[1]:
                oHoster = __checkHoster(str(aEntry[1]))
                if (oHoster != False):
                    oGuiElement = cGuiElement()
                    oGuiElement.setSiteName(SITE_IDENTIFIER)
                    oGuiElement.setFunction('getHosterUrlandPlay')
                    oGuiElement.setTitle(str(aEntry[1]))
                    
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + str(aEntry[0]))
                    oOutputParameterHandler.addParameter('hosterName', oHoster.getPluginIdentifier())
		    oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
                    oGui.addFolder(oGuiElement, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def getHosterUrlandPlay():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sHoster = oInputParameterHandler.getValue('hosterName')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<div class="hostwrapper">.*?src=([^ ]+) '
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
        
    if (aResult[0] == True):
        sStreamUrl = aResult[1][0]
        sStreamUrl = str(sStreamUrl).replace('"', '').replace("'", '')
    
        oHoster = cHosterHandler().getHoster(sHoster)
	oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sStreamUrl)
        oGui.setEndOfDirectory()
        return

    oGui.setEndOfDirectory()

def __checkHoster(sHosterName):
    sHosterName = str(sHosterName)
    if (sHosterName.startswith('ecostream')):
        return cHosterHandler().getHoster('ecostream')

    if (sHosterName.startswith('movshare')):
        return cHosterHandler().getHoster('movshare')

    if (sHosterName.startswith('novamov')):
        return cHosterHandler().getHoster('novamov')

    if (sHosterName.startswith('videoweed')):
        return cHosterHandler().getHoster('videoweed')

    return False
