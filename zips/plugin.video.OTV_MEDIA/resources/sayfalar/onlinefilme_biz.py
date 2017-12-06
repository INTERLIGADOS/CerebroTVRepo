#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
SITE_IDENTIFIER = 'onlinefilme_biz'
SITE_NAME = 'Onlinefilme.biz'
SITE_DESC = 'Replay TV'
lsearch = 'http://streamkiste.tv/js/live-search0.js'
URL_MAIN = 'http://onlinefilme.to/'
ALMAN_SINEMA = (True, 'showGenre')
baseurl = 'http://onlinefilme.biz/'
import re,unicodedata
               
import cookielib
cj = cookielib.CookieJar()
streamurl ='http://onlinefilme.biz/getStream.php'
def showLinks(sUrl):
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    url  = sHtmlContent
    return url          

def sEcho(s):
    s = s
    if '=1' in s:
        s = s.replace('=1', '=2')
        return s
    if '=2' in s:
        s = s.replace('=2', '=3')
        return s
    if '=3' in s:
        s = s.replace('=3', '=4')
        return s
    if '=4' in s:
        s = s.replace('=4', '=5')
        return s
    if '=5' in s:
        s = s.replace('=5', '=6')
        return s
    if '=6' in s:
        s = s.replace('=6', '=7')
        return s
    if '=7' in s:
        s = s.replace('=7', '=8')
        return s
    if '=8' in s:
        s = s.replace('=8', '=9')
        return s
    if '=9' in s:
        s = s.replace('=9', '=10')
        return s
    if '=10' in s:
        s = s.replace('=10', '=11')
        return s
    if '=11' in s:
        s = s.replace('=11', '=12')
        return s
    if '=12' in s:
        s = s.replace('=12', '=13')
        return s
    if '=13' in s:
        s = s.replace('=13', '=14')
        return s
    if '=14' in s:
        s = s.replace('=14', '=15')
        return s
    if '=15' in s:
        s = s.replace('=15', '=16')
        return s
    if '=16' in s:
        s = s.replace('=16', '=17')
        return s
    if '=17' in s:
        s = s.replace('=17', '=18')
        return s
    if '=18' in s:
        s = s.replace('=18', '=19')
        return s
    if '=19' in s:
        s = s.replace('=19', '=20')
        return s
    if '=20' in s:
        s = s.replace('=20', '=21')
        return s
    if '=21' in s:
        s = s.replace('=21', '=22')
        return s
    if '=22' in s:
        s = s.replace('=22', '=23')
        return s
    if '=23' in s:
        s = s.replace('=23', '=24')
        return s
    if '=24' in s:
        s = s.replace('=24', '=25')
        return s
    if '=25' in s:
        s = s.replace('=25', '=26')
        return s
    if '=26' in s:
        s = s.replace('=26', '=27')
        return s
    if '=27' in s:
        s = s.replace('=27', '=28')
        return s
    if '=28' in s:
        s = s.replace('=28', '=29')
        return s
    if '=29' in s:
        s = s.replace('=29', '=30')
        return s
    if '=30' in s:
        s = s.replace('=30', '=31')
        return s
    if '=31' in s:
        s = s.replace('=31', '=32')
        return s
    if '=32' in s:
        s = s.replace('=32', '=33')
        return s
    if '=33' in s:
        s = s.replace('=33', '=34')
        return s
    if '=34' in s:
        s = s.replace('=34', '=35')
        return s
    if '=35' in s:
        s = s.replace('=35', '=36')
        return s
    if '=36' in s:
        s = s.replace('=36', '=37')
        return s
    if '=37' in s:
        s = s.replace('=37', '=38')
        return s
    if '=38' in s:
        s = s.replace('=38', '=39')
        return s
    if '=39' in s:
        s = s.replace('=39', '=40')
        return s
    if '=40' in s:
        s = s.replace('=40', '=41')
        return s
    if '=41' in s:
        s = s.replace('=41', '=42')
        return s
    if '=42' in s:
        s = s.replace('=42', '=43')
        return s
    if '=43' in s:
        s = s.replace('=43', '=44')
        return s
    if '=44' in s:
        s = s.replace('=44', '=45')
        return s
    if '=45' in s:
        s = s.replace('=45', '=46')
        return s
    if '=46' in s:
        s = s.replace('=46', '=47')
        return s
    if '=47' in s:
        s = s.replace('=47', '=48')
        return s
    if '=48' in s:
        s = s.replace('=48', '=49')
        return s
    if '=49' in s:
        s = s.replace('=49', '=50')
        return s
    return False
            

def showSearch():
    oGui = cGui()
    resp = net.http_GET(lsearch)
    data = resp.content
    nonce = re.findall('nonce:"(.*?)"', data, re.S)[0]

    sSearchText = oGui.showKeyBoard()
    if sSearchText != False:
        sUrl = 'http://streamkiste.tv/include/live.php?keyword=%s&nonce=%s'% (sSearchText,nonce)
        sUrl = sUrl.replace(' ', '%20')
        searchMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def Onlinefilme():
    oGui = cGui()
    tarzlistesi = [('Suche', 'http://hdfilme.tv/movie-search?key=%s&page_film=', 'http://hdfilme.tv/movie-search?key=%s&page_film='),
     ('Letzte Updates', 'http://onlinefilme.to/', 'update'),
     ('Beliebte Filme', 'http://onlinefilme.to/', 'popular'),
     ('Genre Filme', 'http://onlinefilme.to/', 'http://streamkiste.tv/cat/kinofilme/sortby/update/')]
    for sTitle, wq,sortby in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('wq', wq)
        oOutputParameterHandler.addParameter('sortby', sortby)
        oOutputParameterHandler.addParameter('siteUrl', wq)
        if sTitle == 'Genre Filme':
            oGui.addDir(SITE_IDENTIFIER, 'GenreFILME', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Filme nach Jahren':
            oGui.addDir(SITE_IDENTIFIER, 'YearsGenreFILME', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Letzte Updates':
            oGui.addDir(SITE_IDENTIFIER, 'streamkisteMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Beliebte Filme':
            oGui.addDir(SITE_IDENTIFIER, 'kisteMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Suche':
            oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'streamkisteMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

  
def ddizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    url = HTTPKIR(urll)
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    xbmc.Player().play(url, liz)
    sys.exit()
    return ok
     

def searchMovies(url):
    oGui = cGui()
    
    resp = net.http_GET(url)
    data = resp.content
    sHtmlContent = re.findall('"(.*?)":."title":"(.*?)","url":"(.*?)","img":"(.*?)"', data, re.S)
    for nr ,sTitle, sUrl,sPicture in sHtmlContent:
        sPicture = 'http://streamkiste.tv' + sPicture
        Urll = 'http://streamkiste.tv' + sUrl
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Urll)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
            
def GenreFILME():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
    
    sPattern = '<a href="(http://onlinefilme.to/filme-online/.*?)"><strong>(.*?)</strong></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = aEntry[1]
            sPicture = aEntry[1]
            
            sUrl = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'kisteMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()

              
def YearsGenreFILME():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
  
    sPattern = '<a href="(http://onlinefilme.to/serie-online/.*?)"><strong>(.*?)</strong></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = aEntry[1]
            sPicture = aEntry[1]
            
            sUrl = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('year', year)
            oGui.addMovie(SITE_IDENTIFIER, 'kisteMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()

def kisteMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')                
                                                    
    tent = HTTPKIR(url)                                                                       
     
    sHtmlContent = re.findall('<div class="small-7 columns text-right">.*?<a href="(.*?)">.*?<img data-original="(.*?)" title="(.*?)"',tent, re.S)
    for sUrl, sPicture, sTitle in sHtmlContent:
        sTitle = alfabekodla(sTitle)
        sPicture = 'http://onlinefilme.to' + sPicture
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'MOVIEHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def streamkisteMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    tent = HTTPKIR(url)
    sHtmlContent = re.findall('<div class="small-9 columns">.*?<a href="(.*?)">.*?<img src="(.*?)" title="(.*?)"',tent, re.S)
    for sUrl, sPicture, sTitle in sHtmlContent:
        sTitle = alfabekodla(sTitle)
        sPicture = 'http://onlinefilme.to' + sPicture
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'MOVIEHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()            
#            url = 'https://yayin2.kuralbet25.com/hls/lig1.m3u8?st=xOoqxCRIYuZvLSYzcIw76Q&e=1507559184'
#            url = base64.b64encode(urll)
            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok





def __NextPage(sHtmlContent, url):
    sPattern = '<li class="active">.*?<a href="javascript:void(0)" data-page="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        url = url + '?page=' + aResult[1][0]
        if 'desc' in url:
            url = url + '&page=' + aResult[1][0]
        return str(url)


def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '</a> <a href="(.*?)" class="syfno">Sonraki Sayfa &raquo;</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        return str(sUrl) + aResult[1][0]
    return False


def MOVIEHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')

    resp = net.http_GET(url)
    data = resp.content
    urll = re.findall("<div class=\"small-5 medium-2 columns text-right\">.*?<a href='(http://onlinefilme.biz/.*?)' target='_blank' class='button small radius expand'>Weiter</a>", data, re.S)[0] 

    oRequestHandler = cRequestHandler(urll)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
                                                                                         
    sPattern = '<div class="panel">.*?<div class="link_share"><a href="javascript.*?" title="(.*?)">.*?<a href="(watch-.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = aEntry[0]
            sPicture = aEntry[1]
            
            id = aEntry[1]
            sTitle = alfabekodla(sTitle)
            data = net.http_POST(streamurl, {'l':id}).content
            url=re.findall('"link":"(.*?)"', data, re.S|re.I)[0]
            mirr ='http://onlinefilme.biz/' +url          
            
            Url =showLinks(mirr)
                                                               
            oOutputParameterHandler = cOutputParameterHandler()
        
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()

def ddizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url  = oInputParameterHandler.getValue('siteUrl')
   
    
    liz = 'test'
    showLinks(url, liz)


def addLink(name, url, iconimage):
   
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    showHosters(url, liz)
   

def play__hdfilme():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()



def showHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
  

    sMovieTitle = alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()