#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   
SITE_IDENTIFIER = 'canlifm_com'
SITE_NAME = 'RADYO-canlifm.com '
SITE_DESC = 'Replay TV'

MOVIE_diziizle = 'http://www.diziizle.net/sinemalar/'
URL_MAIN = 'http://canlifm.com'



RADYO_GENRES = (True, 'showGenre')
Header = 'User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'

  
URL_SEARCH = ('', 'showMovies')
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

def Radyo():
    oGui = cGui()
    tarzlistesi= []
    tarzlistesi.append(("Gecen Ay Top20", "http://canlifm.com/karisikmuzik/banaz-dostfm"))
    tarzlistesi.append(("ILLERE GORE RADYOLAR", "http://canlifm.com/karisikmuzik/banaz-dostfm"))
    tarzlistesi.append(("Slow Müzik", "http://canlifm.com/slowradyolar/"))
    tarzlistesi.append(("Arabesk Fantazi", "http://canlifm.com/arabeskfantezi/"))
    tarzlistesi.append(("Yabanci Müzik", "http://canlifm.com/yabanci/"))
    tarzlistesi.append(("Sanat Müzigi", "http://canlifm.com/sanat/"))
    tarzlistesi.append(("Pop Müzik", "http://canlifm.com/popmuzik/"))
    tarzlistesi.append(("T�rk� Radyolari", "http://canlifm.com/turku/"))
    tarzlistesi.append(("Özgün Müzik", "http://canlifm.com/ozgun/"))
    tarzlistesi.append(("Karma Müzik", "http://canlifm.com/karisikmuzik/"))
    tarzlistesi.append(("Caz-Klasik-Rock", "http://canlifm.com/klasik/"))
    tarzlistesi.append(("Haber Radyolari", "http://canlifm.com/haber/"))
    tarzlistesi.append(("Spor Radyolari", "http://canlifm.com/spor/"))
    tarzlistesi.append(("Dini Radyolar", "http://canlifm.com/dini/"))
               
    for sTitle,sUrl2 in tarzlistesi:
        sTitle =  alfabekodla(sTitle)   
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'DIZILER-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'dizizleABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SINEMALAR-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'sinemaABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Gecen Ay Top20':
             oGui.addDir(SITE_IDENTIFIER, 'top20radyo', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ILLERE GORE RADYOLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showradyolist', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showradyo', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def top20radyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<ul>.*?<li class="sayi">.*?<li><a href="(.*?)"><span>(.*?)</span></a></li>'
                                           

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    


def showradyolist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

        
           



    sPattern = "<li class=\"rakam\">(.*?)</li>.*?<li><a href='(.*?)'><span>(.*?)</span></a></li>"
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle =aEntry[0]+'-'+ aEntry[2]
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'shradyo', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    


def shradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<td width=".*?"><a href="(.*?)">(.*?)</a></td>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def showradyo():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\n','')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<tr class="sectiontableentry.*?" >.*?<a href="(.*?)">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = aEntry[1]
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl

            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox2', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    


def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "http://canlifm.com/"
                                                                 
                                                                                                               
    referer=[('Referer',urla)]       
    data=getUrl(Url).result                                                                                         
    data=data.replace('file=','').replace('var1=','').replace('rtmp=','').replace('FlashVars','flashvars').replace('&amp;','/').replace('autostart=true&backcolor=','').replace('CCCCCC','').replace('&frontcolor=000000','').replace('&screencolor=999999&volume=100&','').replace('streamer=','')
    HosterUrl = re.findall('<center.*?<img src="(.*?)"/>.*?"flashvars".*?"(.*?)"', data, re.S)
    for Thumb,sUrl in HosterUrl:                        
                         
                                    
          sThumbnail = "http://canlifm.com"+ Thumb                                                                              
          oGuiElement = cGuiElement()
          oGuiElement.setSiteName(SITE_IDENTIFIER)
          oGuiElement.setTitle(sTitle)
          oGuiElement.setMediaUrl(sUrl.replace('/http','http').replace('autostart=true/backcolor=/frontcolor=000000/screencolor=999999/volume=100','').replace('/logo=/',''))                                                                                                                                         
          oGuiElement.setThumbnail(sThumbnail)

    #cConfig().log("Hoster - play " + str(sTitle))
          oPlayer = cPlayer()
          oPlayer.clearPlayList()
          oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
          oPlayer.startPlayer()
          return False
        

  
