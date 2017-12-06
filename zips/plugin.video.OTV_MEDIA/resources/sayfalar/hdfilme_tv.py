#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
SITE_IDENTIFIER = 'hdfilme_tv'
SITE_NAME = 'HDfilme'
SITE_DESC = 'Replay TV'
MOVIE_diziizle = 'http://www.diziizle.net/sinemalar/'
URL_MAIN = 'http://hdfilme.tv'
ALMAN_SINEMA = (True, 'showGenre')
baseurl = 'http://filmpalast.to'
streamurl = 'http://filmpalast.to/stream/{id}/1'

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
    sSearchText = oGui.showKeyBoard()
    if sSearchText != False:
        sUrl = 'http://hdfilme.tv/movie-search?key=' + sSearchText
        sUrl = sUrl.replace(' ', '%20')
        searchowMovies(sUrl)
        oGui.setEndOfDirectory()
        return
        

def hdfilme():
    oGui = cGui()
    tarzlistesi = [('Suche', 'http://hdfilme.tv/movie-search?key=%s&page_film='),
     ('NEUE FILME', 'http://hdfilme.tv/movie-movies?page=1'),
     ('Genre FILME', 'http://hdfilme.tv/movie-movies'),
     ('NEUE SERIEN', 'http://hdfilme.tv/movie-series?page=1'),
     ('Genre SERIEN', 'http://hdfilme.tv/movie-series')]
    for sTitle, sUrl2 in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'NEUE FILME':
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Genre FILME':
            oGui.addDir(SITE_IDENTIFIER, 'hdfilmeGenreFILME', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'NEUE SERIEN':
            oGui.addDir(SITE_IDENTIFIER, 'showSHOW', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Genre SERIEN':
            oGui.addDir(SITE_IDENTIFIER, 'hdfilmeGenreSERIEN', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Suche':
            oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)

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


def hdfilmeGenreSERIEN():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
    oParser = cParser()
    sPattern = '>Genre</option>(.*?)</select>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<option value="(.*?)">(.*?)</option>'
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
            sPicture = aEntry[0]
            sUrl = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            sUrl = 'http://hdfilme.tv/movie-series?category=%s&country=&sort=top&sort_type=desc&page=1' % str(sUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'showSHOW', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def hdfilmeGenreFILME():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
    oParser = cParser()
    sPattern = '>Genre</option>(.*?)</select>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<option value="(.*?)">(.*?)</option>'
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
            sPicture = aEntry[0]
            sUrl = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            sUrl = 'http://hdfilme.tv/movie-movies?category=%s&country=&sort=top&sort_type=desc&page=1' % str(sUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'showMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def searchowMovies(sUrl):
    oGui = cGui()
    data = HTTPKIR(sUrl)       
    sHtmlContent = re.findall('<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">', data, re.S)
    for sUrl, sPicture, sTitle in sHtmlContent:
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'MOVIEHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSHOW(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sSearch = urllib2.unquote(sSearch)
        query_args = {'do': 'search',
         'subaction': 'search',
         'story': str(sSearch),
         'x': '0',
         'y': '0'}
        data = urllib.urlencode(query_args)
        headers = {'User-Agent': 'Mozilla 5.10'}
        url = 'http://hdfilme.tv/'
        request = urllib2.Request(url, data, headers)
        try:
            reponse = urllib2.urlopen(request)
        except URLError as e:
            print e.read()
            print e.reason

        sHtmlContent = reponse.read()
        sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    else:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        sHtmlContent = HTTPKIR(url)
    sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<a href="(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">.*?<div class="episode">(.*?)</div>'
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = cUtil().unescape(aEntry[3]) + '-episode-' + aEntry[4]
            sPicture = str(aEntry[2])
            Url = str(aEntry[1])
            Urlid = str(aEntry[0])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('siteid', Urlid)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Moviesshow', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
        if not sSearch:
            sNextPage = sEcho(str(url))
            if sNextPage != False:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSHOW', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    if not sSearch:
        oGui.setEndOfDirectory()


def Moviesshow():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Urlid = oInputParameterHandler.getValue('siteid')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content
    sHtmlContent = re.findall('<a class="new".*?episode="(.*?)" _link="" _sub="" href="http://.*?episode=(.*?)">', data, re.S)
    for sUrl, sTitle in sHtmlContent:
        sTitle = 'episode : ' + sTitle
        Urll = 'http://hdfilme.tv/movie/getlink/' + Urlid + '/' + sUrl
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Urll)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sSearch = urllib2.unquote(sSearch)
        query_args = {'do': 'search',
         'subaction': 'search',
         'story': str(sSearch),
         'x': '0',
         'y': '0'}
        data = urllib.urlencode(query_args)
        headers = {'User-Agent': 'Mozilla 5.10'}
        url = 'http://hdfilme.tv/'
        request = urllib2.Request(url, data, headers)
        try:
            reponse = urllib2.urlopen(request)
        except URLError as e:
            print e.read()
            print e.reason

        sHtmlContent = reponse.read()
        sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    else:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        sHtmlContent = HTTPKIR(url)
    sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = cUtil().unescape(aEntry[2])
            sPicture = str(aEntry[1])
            Url = str(aEntry[0])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'MOVIEHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
        if not sSearch:
            sNextPage = sEcho(str(url))
            if sNextPage != False:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    if not sSearch:
        oGui.setEndOfDirectory()


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


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Urlk = 'http://hdfilme.tv/'
    referer = [('Referer', Urlk)]
    adata = gegetUrl(Url, headers=referer)
    sHtmlContent = base64.b64decode(adata)
    sPattern = '"label":"(.*?)","file":"(.*?)"'              
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            TUK = '|Referer=' + Url + '&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
            sTitle =aEntry[0]
            sUrl = aEntry[1].replace('\\/', '/') + TUK
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'play__hdfilme', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def MOVIEHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Urlk = 'http://hdfilme.tv/'
    Urll = 'http://hdfilme.tv/movie/getlink/' + Url + '/1'
    referer = [('Referer', Urlk)]
    adata = gegetUrl(Urll, headers=referer)
    sHtmlContent = base64.b64decode(adata)
    sPattern = '"label":"(.*?)","file":"(.*?)"'             
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            TUK = '|Referer=' + Urll + '&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
            sGenre = cUtil().unescape(aEntry[0])
            sUrl = aEntry[1].replace('\\/', '/') + TUK
            sTitle = aEntry[0].decode('latin-1').encode('utf-8')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'play__hdfilme', sGenre, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


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


def mshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    streamid = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl = getStreamSRC(streamid)
    sHosterUrl = sUrl
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if oHoster != False:
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()