#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
from startv_com_tr import COCUKshowshowSinema
SITE_IDENTIFIER = 'coukyoutube_tr'
SITE_NAME = 'CIZGI FILM'


MOVIE_diziizle = 'http://www.tv8.com.tr'
URL_MAIN = 'http://www.youtube.com/embed/'
URL_PIC = 'http://s.dogannet.tv/'


MOVIE_GENRES = (True, 'showGenre')
YUPA = 'https://www.youtube.com'
MOVIE_MOVIE = (True, 'showGenre')
MOVIE_NEWS = (True, 'showGenre')
MOVIE_NOTES = (True, 'showGenre')

MOVIE_COMMENTS = (True, 'showGenre')
MOVIE_GENRES = (True, 'showGenre')

  
URL_SEARCH = ('', 'showMovies')
def load():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'cocuk') 
    oGui.addDir(SITE_IDENTIFIER, 'COCUKshowshowSinema', 'PUHUTV Çocuk', 'search.png', oOutputParameterHandler) 
    
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
            sUrl = 'https://www.youtube.com/results?search_query='+sSearchText  
            sUrl= sUrl.replace(' ','+')
            showMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<li><div class="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix" data-context-item-id="(.*?)".*?<img.*?src="(.*?)".*?aria-hidden="true">(.*?)</span>.*?spf-link " data-sessionlink=".*?"  title="(.*?)"'
    
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
           
            sTitle =aEntry[3]+' : '+ aEntry[2]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)
           
        sNextPage = __checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()
    


def coukyoutube():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'cocuk') 
    oGui.addDir(SITE_IDENTIFIER, 'COCUKshowshowSinema', 'PUHUTV Çocuk', 'search.png', oOutputParameterHandler) 

    tarzlistesi = []
    
    tarzlistesi.append(("Cizgi Film ARA", "https://www.youtube.com/results?search_query="))
    
    tarzlistesi.append(("PEPE TUM BOLUMLER", "https://www.youtube.com/results?search_query=pepe+t%C3%BCm+b%C3%B6l%C3%BCmler"))
    tarzlistesi.append(("ANIME TURKCE",  "https://www.youtube.com/results?search_query=anime+turkce"))
    tarzlistesi.append(("turkce cizgi filmleri", "https://www.youtube.com/results?search_query=turkce+cizgi+filmleri"))
    tarzlistesi.append(("keloglan cizgi film", "https://www.youtube.com/results?search_query=keloglan+cizgi+film"))
    tarzlistesi.append(("cizgi filmleri caillou",  "https://m.youtube.com/results?search_query=t%C3%BCrk+cizgi+filmleri+caillou&spfreload=10"))
    tarzlistesi.append(("cizgi filmleri niloya",  "https://m.youtube.com/results?search_query=t%C3%BCrk+cizgi+filmleri+niloya&spfreload=10"))
    tarzlistesi.append(("minyonlar turkce dublaj",  "https://www.youtube.com/results?search_query=minyonlar+t%C3%BCrkce+dublaj+"))
    tarzlistesi.append(("turk komedi filmleri tek parca",  "https://www.youtube.com/results?search_query=turk+komedi+filmleri+tek+parca"))

    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'CANLI YAYIN':
             oGui.addDir(SITE_IDENTIFIER, 'tv8canli', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Cizgi Film ARA':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DIZI':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SINEMALAR':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  
def search():
 	oGui = cGui()
        
        input = xbmcgui.Dialog().input(__addon__.getLocalizedString(31200), type=xbmcgui.INPUT_ALPHANUM)
 	if input == '': return
	resultData = 'https://www.youtube.com/results?search_query=' + input, None
        for sUrl in liste:
       
             oOutputParameterHandler = cOutputParameterHandler()
             oOutputParameterHandler.addParameter('siteUrl', sUrl)
             oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
        oGui.setEndOfDirectory()
def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['A',sUrl+'/muzik/sanatcilar?prefix=A'] )
    liste.append( ['B',sUrl+'/muzik/sanatcilar?prefix=B'] )
    liste.append( ['C',sUrl+'/muzik/sanatcilar?prefix=C'] )
    liste.append( ['Ç',sUrl+'/muzik/sanatcilar?prefix=&#199;'] )
    liste.append( ['D',sUrl+'/muzik/sanatcilar?prefix=D'] )
    liste.append( ['E',sUrl+'/muzik/sanatcilar?prefix=E'] )
    liste.append( ['F',sUrl+'/muzik/sanatcilar?prefix=f'] )
    liste.append( ['G',sUrl+'/muzik/sanatcilar?prefix=g'] )
    liste.append( ['H',sUrl+'/muzik/sanatcilar?prefix=h'] )
    liste.append( ['I',sUrl+'/muzik/sanatcilar?prefix=i'] )
    liste.append( ['İ',sUrl+'/muzik/sanatcilar?prefix=i'] )
    liste.append( ['J',sUrl+'/muzik/sanatcilar?prefix=j'] )
    liste.append( ['K',sUrl+'/muzik/sanatcilar?prefix=k'] )
    liste.append( ['L',sUrl+'/muzik/sanatcilar?prefix=l'] )
    liste.append( ['M',sUrl+'/muzik/sanatcilar?prefix=m'] )
    liste.append( ['N',sUrl+'/muzik/sanatcilar?prefix=n'] )
    liste.append( ['O',sUrl+'/muzik/sanatcilar?prefix=o'] )
    liste.append( ['�',sUrl+'/muzik/sanatcilar?prefix=ö'] )
    liste.append( ['P',sUrl+'/muzik/sanatcilar?prefix=p'] )
    liste.append( ['R',sUrl+'/muzik/sanatcilar?prefix=r'] )
    liste.append( ['S',sUrl+'/muzik/sanatcilar?prefix=s'] ) 
    liste.append( ['ş',sUrl+'/muzik/sanatcilar?prefix=ş'] ) 
    liste.append( ['T',sUrl+'/muzik/sanatcilar?prefix=t'] )
    liste.append( ['U',sUrl+'/muzik/sanatcilar?prefix=u'] )
    liste.append( ['Ü',sUrl+'/muzik/sanatcilar?prefix=�'] )
    liste.append( ['V',sUrl+'/muzik/sanatcilar?prefix=v'] )
    liste.append( ['W',sUrl+'/muzik/sanatcilar?prefix=w'] )
    liste.append( ['X',sUrl+'/muzik/sanatcilar?prefix=x'] )
    liste.append( ['Y',sUrl+'/muzik/sanatcilar?prefix=y'] )
    liste.append( ['Z',sUrl+'/muzik/sanatcilar?prefix=z'] )
    liste.append( ['0',sUrl+'/muzik/sanatcilar?prefix=0'] )
    liste.append( ['1',sUrl+'/muzik/sanatcilar?prefix=1'] )
    liste.append( ['2',sUrl+'/muzik/sanatcilar?prefix=2'] )
    liste.append( ['3',sUrl+'/muzik/sanatcilar?prefix=3'] )
    liste.append( ['4',sUrl+'/muzik/sanatcilar?prefix=4'] )
    liste.append( ['5',sUrl+'/muzik/sanatcilar?prefix=5'] )
    liste.append( ['6',sUrl+'/muzik/sanatcilar?prefix=6'] )
    liste.append( ['7',sUrl+'/muzik/sanatcilar?prefix=7'] )
    liste.append( ['8',sUrl+'/muzik/sanatcilar?prefix=8'] )
    liste.append( ['9',sUrl+'/muzik/sanatcilar?prefix=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()


def pageshowMovies(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = ''+Url
        request = urllib2.Request(url,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
         
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<li><div class="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix" data-context-item-id="(.*?)".*?<img.*?src="(.*?)".*?aria-hidden="true">(.*?)</span>.*?data-sessionlink=".*?" title="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<li><div class="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix" data-context-item-id="(.*?)".*?<img.*?src="(.*?)".*?aria-hidden="true">(.*?)</span>.*?spf-link " data-sessionlink=".*?"  title="(.*?)"'
    sHtmlContent = sHtmlContent.replace('amp;','')
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
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
           
            sTitle =aEntry[3]+' : '+ aEntry[2]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
  
def pageshowDizi(sSearch = ''):
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
        sPattern = '<div class="thumbnail "">.*?<a href="(.*?)" data-target="myModal">.*?<img class="lazy" src=".*?" data-original="//(.*?)" alt="(.*?)" />'
    
    sHtmlContent = sHtmlContent.replace('</span> <b>','<OTV>')
    
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
           
            sTitle = aEntry[2]
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'partplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
 

def __checkForNextPage(sHtmlContent):
    sHtmlContent= sHtmlContent.replace('amp;','')
        
    sPattern = '<div class="branded-page-box search-pager  spf-link ">.*?<button class=".*?href="(.*?)"'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(YUPA)+ aResult[1][0].replace(' ','+')
    return False                        

def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    sHosterUrl = sUrl
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()

def partplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
       
    stream = re.findall("type: 'GET'.*?url: '(.*?)',", data, re.S)
    url = "http://www.netd.com%s" %(stream[0])
    tarzlistesi= []
    tarzlistesi.append(("part=1", ""+url.replace('</span> <b>','<OTV>')))
    tarzlistesi.append(("part=2", ""+url.replace('part=1-6','part=2-6')))
    tarzlistesi.append(("part=3", ""+url.replace('part=1-6','part=3-6')))
    tarzlistesi.append(("part=4", ""+url.replace('part=1-6','part=4-6')))
    tarzlistesi.append(("part=5", ""+url.replace('part=1-6','part=5-6')))
    tarzlistesi.append(("part=6", ""+url.replace('part=1-6','part=6-6')))
        
    for sTitle,sUrl in tarzlistesi:
           
         
         
        sTitle = alfabekodla(sTitle)         
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'sshowBox3', sTitle, 'tv.png', oOutputParameterHandler)
    
  
    oGui.setEndOfDirectory()




def sshowBox3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    
    urla  = "http://www.netd.com/"                   
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer)                      
    streamDaten = re.findall("defaultServiceUrl: '(.*?)'.*?path:'(.*?)',", data, re.S)	
    if streamDaten:
        (rtmp,Server) = streamDaten[0]
    
    sHosterUrl = "%s/%s" %( rtmp,Server)
    



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
