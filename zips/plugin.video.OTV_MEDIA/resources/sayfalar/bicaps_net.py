#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
SITE_IDENTIFIER = 'bicaps_net'
SITE_NAME = 'Bicaps.net'
SITE_DESC = 'Films  streaming'
 
URL_MAIN = 'http://www.bicaps.net/'

TURK_SINEMA = (True, 'showGenre')

 
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
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'SÃ©ries nouveaute', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'SÃ©ries liste complete', 'series.png', oOutputParameterHandler)
    
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
        sUrl = 'http://www.bicaps.net/?s=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
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
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
   
def bicaps(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://www.bicaps.net/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)

    sUrl = 'http://www.bicaps.net/'

    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
   
    sPattern = '<li class="cat-item cat-item-.*?"><a href="(.*?)" title=".*?">(.*?)</a>'
    
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
           
            Link = aEntry[0]
           
            sTitle  = sTitle  + ' [COLOR skyblue]' + sTitle +'[/COLOR]'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sTitle, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

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
def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    data = resp.content
                          
    sHtmlContent = re.findall('<div class="moviefilm">.*?<a href="(.*?)">.*?<span class="tr-altyazi"></span><img src="(.*?)" alt="(.*?)"', data, re.S)
         
    for sUrl,sPicture,sTitle in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()   
def showMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codÃ© il y a meme pas une seconde par l'addon
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
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<div class="movief"><a href="(.*?)">(.*?)</a>'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="moviefilm">.*?<img src="(.*?)".*?<div class="movief"><a href="(.*?)">(.*?)</a>'
    
    sHtmlContent = sHtmlContent.replace('\n','').replace('-izle/','-izle/6/')
    
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
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
            #not found better way
            sTitle = alfabekodla(sTitle)
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
                oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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
    sPattern = '<span class=\'current\'>.+?</span><a class="page larger" href="(.+?)">'
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
    oParser = cParser()
    sPattern = '<div class="keremiya_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?)"><span>(.*?)</span></a>'
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
            oGui.addTV(SITE_IDENTIFIER, 'streams',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    
   

    sPattern = '<!--baslik:.*?--.*?<ifram.+?src=[\'|"](.*?)[\'|"]'
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
def streams():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
   
    sPattern = '<!--baslik:.*?--.*?<ifram.+?src=[\'|"](.+?)[\'|"]'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

          
            sHosterUrl = str(aEntry).encode('utf-8', 'ignore')            
            if 'http://filmakinesi.' in sHosterUrl:
                sHosterUrl=sHosterUrl.replace("http://filmakinesi.net/player/url/","")
                        
                        
                url1="%s" % (sHosterUrl) 
                print url1
                url2 = base64.b64decode(url1)
                print url2
                url3 = terscevir(url2)            
                streamurl=base64.b64decode(url3) 
                print streamurl                    
                if "ok.ru" in streamurl:
                               streamurl=streamurl.replace('gâ',"")  
                               Url= "http://m.ok.ru/video/%s" % (streamurl.replace("ok/",""))
                               oOutputParameterHandler = cOutputParameterHandler()
                               oOutputParameterHandler.addParameter('siteUrl', Url)
                               oGui.addTV(SITE_IDENTIFIER, 'mokru', sMovieTitle, '', '', '', oOutputParameterHandler)     
                               
                if "mail/" in streamurl:                     
                               streamurl=streamurl.replace('mailgâ',"") 
                               urlan = re.findall('mail/(.*?)/(.*?)/', streamurl)
                               if urlan:         
                                           for (url1),(url2) in urlan:
                                
                               
                                                                                            
                                                      
                                                Url= "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (url1,url2)
                                                oOutputParameterHandler = cOutputParameterHandler()
                                                oOutputParameterHandler.addParameter('siteUrl', str(Url))
                                                oGui.addTV(SITE_IDENTIFIER, 'mailru', sMovieTitle, '', '', '', oOutputParameterHandler)	     
                                           
                                    			                                  
                if "vk/" in streamurl:     
                                   streamurl=streamurl.replace('gâ',"")  
                                   urlan = re.findall('vk/(.*?)/(.*?)/([a-z0-9]+)', streamurl)
                                   if urlan:         
                                           for (url1),(url2),(url3) in urlan:
                                
                               
                                                sHosterUrl= "http://vk.com/video_ext.php?oid=%s&id=%s&hash=%s" % (url1,url2,url3)
                                                
                if "uptostream/" in streamurl:     
                                      streamurl=streamurl.replace('gâ',"")  
                                      streamurl=streamurl.replace("uptostream/","") 
                                      
                                      sHosterUrl= "http://uptostream.com/iframe/%s" % (streamurl)
                                                         
                if "openload/" in streamurl:     
                                      streamurl=streamurl.replace('gâ',"")  
                                      streamurl=streamurl.replace("openload/","") 
                                      
                                      sHosterUrl= "https://openload.co/embed/%s" % (streamurl)
                                      
            
                            #redirection tinyurl
                      #test pr liens raccourcis
            if "ok.ru" in sHosterUrl:
                               
                               
                               sHosterUrl=sHosterUrl.replace('//ok.ru/videoembed/',"").replace('https://ok.ru/videoembed/',"")   
                               Url= "http://m.ok.ru/video/%s" % sHosterUrl
                               oOutputParameterHandler = cOutputParameterHandler()
                               oOutputParameterHandler.addParameter('siteUrl', Url)
                               oGui.addTV(SITE_IDENTIFIER, 'mokru', sMovieTitle, '', '', '', oOutputParameterHandler)             
            if 'mail.ru' in sHosterUrl:
                       id_raw = re.findall('mail.ru/.*?mail/(.*?)/.*?/(\d*)\.html',  sHosterUrl)
                       if id_raw:
                           (m_user, m_id) = id_raw[0]
                       Url = "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (m_user, m_id)
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'mailru', sMovieTitle, '', '', '', oOutputParameterHandler)	     

           
            
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

