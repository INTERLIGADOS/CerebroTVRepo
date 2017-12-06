#-*- coding: utf-8 -*-

#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
import json, base64
import CommonFunctions

import json
from datetime import datetime, date, timedelta
common = CommonFunctions

import hashlib
import os.path
from xml.dom import minidom
from urlparse import parse_qs
HOST = 'XBMC'
SITE_IDENTIFIER = 'livescore'
SITE_NAME = '[COLOR orange]WORLD FUTBOOL Live Scores  Ozet [/COLOR]'
SPORT_SPORTS = (True, 'futbolozet')
def futbolozet(): #affiche les genres
    oGui = cGui()
    url ="https://dl.dropboxusercontent.com/s/km2w2t4cqsgyqgb/AlbanianTvLive.html?dl=0"
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

    headers = {"Referer":"wss://vs52.tawk.to/s/?k=5899c4b9110e7c7f9f3de765&u=bbcr6zagdNiPRctSW%2FFYb%2FZsm1bdyDu8Gfzmb56oMzrEqeB8vlXTGn83v079fGjR&uv=2&a=587798b5620a011eeac60c7b&cver=0&pop=false&w=gkiUy8&jv=537&asver=184&ust=false&p=Tv%20Shqip%20Live%20-%20Big%20Brother%20Albania%209%20Live%20-%20Albanian%20Tv%20-%20Part%202&r=https%3A%2F%2Ftvshqip.tv%2F&EIO=3&transport=websocket&sid=-Q4-Lw7Xr6Km3BIZFQO2&__t=LeOg7SK","User-Agent":UA}

    dat= 'http://www.goalsarena.org/en/'
    import ssl
    ssl.PROTOCOL_SSLv23 = ssl.PROTOCOL_TLSv1
    data= requests.get(dat ).content
                  
                                
    streamDaten = re.compile('<span class="flags sprite-.*?"><a href="(.*?)"><im.*?alt="(.*?)"').findall(data)
    
    for sUrl,  sTitle in streamDaten:                          
        sTitle = sTitle.replace('Spor Toto',"Turkish")
        sTitle = unicode(sTitle, 'latin-1')#converti en unicode
        sTitle = unicodedata.normalize('NFD', sTitle).encode('ascii', 'ignore')#vire accent
        sTitle = sTitle.encode( "utf-8")
        sTitle = urllib.unquote_plus(sTitle)  
        sPicture='http://goalsarena.goalsarena.netdna-cdn.com/templates/gk_sportmaxum/xlogo.png.pagespeed.ic.F0IzaQsJmf.webp'    
        
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'sportsntvlive.com'  in sUrl:
           oGui.addMovie(SITE_IDENTIFIER, 'sportsntvlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        else:
           oGui.addMovie(SITE_IDENTIFIER, 'showfutbolozet', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showfutbolozet(sSearch = ''):
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
        sPattern = '<div style="float: left;">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
         
        
        sPattern = '<div class="vtitle"><div><a href="(.*?)">.*?</a></div></div></li><li><div class="vscreen"><a href=".*?"><img style="cursor:pointer;" class="videothumbss" onclick=".*?" src="(.*?)".*?alt="(.*?)"'
    
    
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
           
            sTitle = alfabekodla(aEntry[2])
            sPicture = str(aEntry[1])
                            
            sUrl = str(aEntry[0])
                      
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'play_showfutbolozet', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
                
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showfutbolozet', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()   
def __checkForNextPage(sHtmlContent):
    sPattern = '<div class="listnavigation">.*?div style="float:right; width:10%;"><a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl = aResult[1][0]
        sUrl = sUrl.replace('&amp;',"&")
        return sUrl

    return False
def play_showfutbolozet():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        sTitle = oInputParameterHandler.getValue('sMovieTitle')
        sTitle = alfabekodla(sTitle)
        
   
        ua='Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'
        data = requests.get(url).content     
        sUrl=re.findall('<ifram.*?src="(.*?)"',data)[0]
        if 'ok.ru' in sUrl:
               sUrl = sUrl
               sTitle= "OK.ru PLAY"
        if 'rutube.ru' in sUrl:
                sUrl = 'https:' + sUrl
                sTitle= "RUTUBE.ru PLAY"  
        if 'youtube.com' in sUrl:
                sUrl = 'https:' + sUrl
                sTitle= "youtube.com PLAY"  
        sThumbnail= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
             
        if sTitle == 'RUTUBE.ru PLAY':
             oGui.addDir(SITE_IDENTIFIER, 'showHosters','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'OK.ru PLAY':
             oGui.addDir(SITE_IDENTIFIER, 'showHosters','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'youtube.com PLAY':
             oGui.addDir(SITE_IDENTIFIER, 'showHosters','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TürkTV+SPORT int':
             oGui.addDir(SITE_IDENTIFIER, 'sonicGenre','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Show Sport TV Bein-Spor':
             oGui.addDir(SITE_IDENTIFIER, 'showsport','[COLOR orange]'+sTitle+'[/COLOR]', 'genres.png', oOutputParameterHandler)        
        else:
              oGui.addTV(SITE_IDENTIFIER, 'msshowBox3',  sTitle, '', sThumbnail, '', oOutputParameterHandler)
        oGui.setEndOfDirectory()
def msshowBox3():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    link = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    ua='Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04'
    source=requests.get(link,headers={'User-Agent':ua,'Referer':'http://www.goalsarena.org/','Accept':'/*','Connection':'keep-alive'}).text
    f4m=re.findall('<source src="(.*?)" type="video/mp4" class="mp4-source"/>',source)[0]
    Url='http:' + f4m

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(Url)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  

    
def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok


def showHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
 