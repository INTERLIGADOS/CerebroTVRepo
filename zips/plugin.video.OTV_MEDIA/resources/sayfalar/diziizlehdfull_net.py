#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *  
HOST = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
 
SITE_IDENTIFIER = 'diziizlehdfull_net'
SITE_NAME = 'diziizlehdfull.org'
MOVIE_HD = (True, 'showGenre')
def load():
    oGui = cGui()
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_TURK[1], 'showGenre', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIE[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIE[1], 'Tout les films', 'films.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'Films par Genres', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries nouveaute', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries liste complete', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_NEWS[1], 'Animes Nouveaute', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_ANIMS[0])
    oGui.addDir(SITE_IDENTIFIER, ANIM_ANIMS[1], 'Animes Liste complete', 'series.png', oOutputParameterHandler)
           
    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        showMovies(sSearchText)
        oGui.setEndOfDirectory()
        return
        
def AlphaSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    
    dialog = cConfig().createDialog(SITE_NAME)
    
    for i in range(0,27) :
        cConfig().updateDialog(dialog, 36)
        
        if (i > 0):
            sTitle = chr(64+i)
        else:
            sTitle = '09'
            
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl + sTitle.upper() )
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal] Lettre [COLOR red]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
     
def diziizlehdfulltr(): #affiche les genres
    oGui = cGui()
    url = 'http://www.diziizlehdfulltr.com/cesur-ve-guzel-16-bolum-izle-2-mart-2017.html'
    headers = {'Host':'www.diziizlehdfulltr.com','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1', 'Referer': 'http://www.diziizlehdfull.org/[makelist.param1]', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

    channel= 'http://www.diziizlehdfulltr.com/7663&action_id=checkAllowRefresh'
    post = { 'headers':headers , 'allowwebsite': channel }
    data = urllib.urlencode(post)
                         
    request = urllib2.Request(url,data, headers)
    response = urllib2.urlopen(request)
    data = response.read()
                           
    playlist = re.findall('<option class="level-0" value="(.*?)">(.*?)</option>', data, re.S)
    for sUrl,sGenre in playlist:
            
            sGenre = alfabekodla(sGenre)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sGenre, '', '', '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()    

def showAlpha():
    oGui = cGui()
 
    liste = []
    liste.append( ['0','http://www.voirfilms.org/alphabet/0/1'] )
    liste.append( ['1','http://www.voirfilms.org/alphabet/1/1'] )
    liste.append( ['2','http://www.voirfilms.org/alphabet/2/1'] )
    liste.append( ['3','http://www.voirfilms.org/alphabet/3/1'] )
    liste.append( ['4','http://www.voirfilms.org/alphabet/4/1'] )
    liste.append( ['5','http://www.voirfilms.org/alphabet/5/1'] )
    liste.append( ['6','http://www.voirfilms.org/alphabet/6/1'] )
    liste.append( ['7','http://www.voirfilms.org/alphabet/7/1'] )
    liste.append( ['8','http://www.voirfilms.org/alphabet/8/1'] )
    liste.append( ['9','http://www.voirfilms.org/alphabet/9/1'] )
    liste.append( ['A','http://www.voirfilms.org/alphabet/a/1'] )
    liste.append( ['B','http://www.voirfilms.org/alphabet/b/1'] )
    liste.append( ['C','http://www.voirfilms.org/alphabet/c/1'] )
    liste.append( ['D','http://www.voirfilms.org/alphabet/d/1'] )
    liste.append( ['E','http://www.voirfilms.org/alphabet/e/1'] )
    liste.append( ['F','http://www.voirfilms.org/alphabet/f/1'] )
    liste.append( ['G','http://www.voirfilms.org/alphabet/g/1'] )
    liste.append( ['H','http://www.voirfilms.org/alphabet/h/1'] )
    liste.append( ['I','http://www.voirfilms.org/alphabet/i/1'] )
    liste.append( ['J','http://www.voirfilms.org/alphabet/j/1'] )
    liste.append( ['K','http://www.voirfilms.org/alphabet/k/1'] )
    liste.append( ['L','http://www.voirfilms.org/alphabet/l/1'] )
    liste.append( ['M','http://www.voirfilms.org/alphabet/m/1'] )
    liste.append( ['N','http://www.voirfilms.org/alphabet/n/1'] )
    liste.append( ['O','http://www.voirfilms.org/alphabet/o/1'] )
    liste.append( ['P','http://www.voirfilms.org/alphabet/p/1'] )
    liste.append( ['R','http://www.voirfilms.org/alphabet/r/1'] )
    liste.append( ['S','http://www.voirfilms.org/alphabet/s/1'] )
    liste.append( ['T','http://www.voirfilms.org/alphabet/t/1'] )
    liste.append( ['U','http://www.voirfilms.org/alphabet/u/1'] )
    liste.append( ['V','http://www.voirfilms.org/alphabet/v/1'] )
    liste.append( ['W','http://www.voirfilms.org/alphabet/w/1'] )
    liste.append( ['X','http://www.voirfilms.org/alphabet/x/1'] )
    liste.append( ['Y','http://www.voirfilms.org/alphabet/y/1'] )
    liste.append( ['Z','http://www.voirfilms.org/alphabet/z/1'] )
               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'films.png', oOutputParameterHandler)
       
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
        sPattern = '<div class="fixwidt.*?">.*?<a href="(.*?)">.*?<img class="izimg" src="(.*?)" alt="(.*?)"'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        sUrl='http://www.diziizlehdfulltr.com/?cat='+ Url
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()

        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="fixwidt.*?">.*?<a href="(.*?)".*?<img class="izimg" src="(.*?)" alt="(.*?)"'
    
    sHtmlContent = sHtmlContent.replace('\n','')
    
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
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sinemaPart', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
  
def __checkForNextPage(sHtmlContent):
    sPattern = '</span><a href="(.+?)" class="single_page" title=".+?">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False
 

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();

    sPattern = '<a href="(http://www.diziizlehdfull.org/.*?)"><span>(.*?)</span>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sTitle = sMovieTitle+' - '+aEntry[1]
            
            sDisplayTitle = cUtil().DecoTitle(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(aEntry[0]))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()

def sinemaPart():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['Part 1',sUrl+'/'] )
    liste.append( ['Part 2',sUrl+'/2'] )
    liste.append( ['Part 3',sUrl+'/3'] )
    liste.append( ['Tek Parca izle',sUrl+'/4'] )
    liste.append( ['Alternatif',sUrl+'/5'] )
    liste.append( ['Alternatif',sUrl+'/6'] )
    
               
    for sTitle,sUrl in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showHosters', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    sHtmlContent = sHtmlContent.replace('<iframe src="//www.facebook.com/','')


    sPattern = '<iframe.+?src=[\'|"](.+?)[\'|"]'
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

            #oHoster = __checkHoster(sHosterUrl)
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
