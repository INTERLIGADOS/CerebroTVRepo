#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   

SITE_IDENTIFIER = 'saraydorf_tv'
SITE_NAME = 'saraydorf'
SITE_DESC = 'Replay TV'
URL_MAIN = 'http://saraydorf.de/'     
Player_User_Agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
SPORT_SPORTS = (True, 'showGenre')

def decodeHtml(data):

	
		data = data.decode('unicode-escape').encode('UTF-8') 
		return data

def iso8859_Decode(txt):
	txt = txt.replace('\xe4','ä').replace('\xf6','ö').replace('\xfc','ü').replace('\xdf','ß')
	txt = txt.replace('\xc4','Ä').replace('\xd6','Ö').replace('\xdc','Ü')
	txt.decode('iso-8859-1').encode('utf-8')
	return txt

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

def showGenre():
    oGui = cGui()
    liste = []
    liste.append( ['saraydorf Futbol','http://opus.re/index-PLAYLIST.php'] )
    liste.append( ['liveonlinetv247','http://www.liveonlinetv247.info/tvchannels.php'] )
    for sTitle,sUrl2 in liste:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == '7/24  TV':
             oGui.addDir(SITE_IDENTIFIER, 'Asonicstream', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'liveonlinetv247':
             oGui.addDir(SITE_IDENTIFIER, 'liveonlinetv247', sTitle, 'genres.png', oOutputParameterHandler)        
        elif sTitle == 'BELGESELLER-harfler':
             oGui.addDir(SITE_IDENTIFIER, 'sinemaABC', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'TURKTV-SPOR':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'racacaxtvga', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def racacaxtvga():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://racacaxtv.ga/mega.php?category=VG91dGVz&pls=RnJhbmNvcGhvbmVz'
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
                                     
    oRequestHandler = cRequestHandler(sUrl)                                            
    sHtmlContent = oRequestHandler.request();
    
                
    sPattern = '<a class="item app" href="(.*?)">.*?<img error="1" draggable="false" class="item_icon" src="(.*?)".*?<div class="item_name">(.*?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = decodeHtml(aEntry[2])
           
            sThumbnail =aEntry[1]
            sUrl =aEntry[0]
            
            
            sTitle = cUtil().DecoTitle(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'racacaxtvga2', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def racacaxtvga2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
   
                                     
    oRequestHandler = cRequestHandler(sUrl)                                            
    sHtmlContent = oRequestHandler.request();
    
                
    sPattern = '<a class="item app" href="(.*?)">.*?<img error="1" draggable="false" class="item_icon" src="(.*?)".*?<div class="item_name">(.*?)</div>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
              
           
            
            
            TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
               
            sTitle = decodeHtml(aEntry[2])
           
            sThumbnail =aEntry[1]
            sUrl =aEntry[0]+TIK
            
            
            sTitle = cUtil().DecoTitle(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox3', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
def opusdorf():
    oGui = cGui()
   
    url = 'http://opus.re/index-PLAYLIST.php'
   
   
                                     
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Referer': 'http://opus.re/index.php', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    sHtml = requests.get(url, headers = headers).text
    sHtml = sHtml.replace('title=" "','title="TV"').replace('title=""','title="TV"')
    urlan = re.findall('src=\'./(.*?)&\';"><img src="(.*?)" width=".*?" height=".*?" border=".*?" alt=".*?" title="(.*?)"', sHtml)
    for url1,url2,url3 in urlan:            
            sTitle = alfabekodla(url3)
            sThumbnail ='http://www.opus.re'+url2
            sUrl ='http://www.opus.re/'+url1
            sUrl =sUrl.replace(' ','-')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox4', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory()

def liveonlinetv247():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sOrder = oInputParameterHandler.getValue('sOrder')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    sPattern = '<li><a href="(/watch.*?)">(.*?)</a></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)          
    
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                
            sTitle = aEntry[1]
            surl ='http://www.liveonlinetv247.info'+ aEntry[0]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', surl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oGui.addDirectTV(SITE_IDENTIFIER, 'play__liveonlinetv24', sDisplayTitle, 'libretv.png' , '', oOutputParameterHandler)    
        
        cConfig().finishDialog(dialog)
        
        oGui.setEndOfDirectory()
    oGui.setEndOfDirectory()
def play__liveonlinetv24():
    net = Net()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    sTitle = alfabekodla(sTitle)
    
   
    
    datam = requests.get(url).content
    tream = re.findall('>Live Sports Schedule</a></p><p><a href="(.*?)"><img src="http://www.liveonlinetv247.info/images/play.png"', datam, re.S)[0]
    tream = tream.replace('www.liveonlinetv247.info/','www.liveonlinetv247.info/embed/')
    data= requests.get(tream).content
    Url= re.findall('<source type="application/x-mpegurl" src="(.*?)">', data, re.S)[0]
    data= requests.get(Url).content
    
    
    Header = 'User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X)'   
    
    Url1= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,RESOLUTION=.*?,CODECS=".*?"\n(.*?)\n', data, re.S)[0]
    Url2= re.findall('(http.*?)playlist.m3u8.*?', Url, re.S)[0]
    
    sUrl =Url2+Url1 
    sThumbnail ='http://www.liveonlinetv247.info/images/livesports.png'
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
    oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
    oGui.addTV(SITE_IDENTIFIER, 'showhlsetryplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)


def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="film_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?.html.*?)"><span>(.*?)</span></a>'
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

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'streams', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    
def sshowBox4():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')                                           
    sTitle = alfabekodla(sTitle)    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Referer': 'http://opus.re/index-PLAYLIST.php', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(url, headers = headers).text               
    data =data.replace('value="src=','file: "').replace('<a class="item app" href="','file: "').replace('&amp;','&')
    sUrl = re.findall('file: "(.*?)",', data, re.S)[0]                                    
    if 'opus.re' in sUrl:              
	    data= requests.get(sUrl).content
	    Url= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2290000\n(.*?)\n', data, re.S)[0]
    

	    

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(Url))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showhlsetryplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)

    else:        	                                                                           
                        
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showhlsetryplayer', sTitle, '', sThumbnail, '', oOutputParameterHandler)

       

    
    oGui.setEndOfDirectory()

def playopus():
    net = Net()
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
         
   
    Header = 'User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X)'                                                                      
                                            
  
    data= requests.get(url).content
    Url= re.findall('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2290000\n(.*?)\n', data, re.S)[0]
    

    sHosterUrl =Url +'|'+ Header

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        
                    
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  

def sshowBox3():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  