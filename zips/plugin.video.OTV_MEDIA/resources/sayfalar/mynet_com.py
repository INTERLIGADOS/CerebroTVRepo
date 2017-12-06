#-*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
SITE_IDENTIFIER = 'mynet_com'
SITE_NAME = 'mynet TV'
SITE_DESC = 'Films  streaming'
 
URL_MAIN = 'http://www.bicaps.net/'



MOVIE_GENRES = (True, 'showGenre')
YUPA = 'https://www.youtube.com'
MOVIE_MOVIE = (True, 'showGenre')
MOVIE_NEWS = (True, 'showGenre')
MOVIE_NOTES = (True, 'showGenre')

MOVIE_COMMENTS = (True, 'showGenre')
MOVIE_GENRES = (True, 'showGenre')

 
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
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'S√©ries nouveaute', 'series.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'S√©ries liste complete', 'series.png', oOutputParameterHandler)
    
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
        sUrl = 'http://www.mynet.com/tv/ara/?s=' + sSearchText
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
   
def mynetcom(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)

    sUrl = 'http://www.mynet.com/tv/'

    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<li><a href="','<li rel="217"><a href="').replace('" itemprop="url"','"')
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
                
    sPattern = '<li rel=".*?"><a href="(.*?)".*?>(.*?)</a></li>'
    
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
def showMessage(heading='OTV_MEDIA', message = '', times = 2000, pics = ''):
                try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
                except Exception, e:
                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )                                           

                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )

def searchowMovies(sUrl):
    oGui = cGui()
    resp = net.http_GET(sUrl)
    data = resp.content
         
                                
    sHtmlContent = re.findall('<div class="thm-con">.*?<a href="(.*?)">.*?<img.*?data-original="(.*?)">.*?<h3>(.*?)</h3>', data, re.S)
       
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
        #on redecode la recherhce cod√© il y a meme pas une seconde par l'addon
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
        sPattern = '<li class=".*?">.*?<a href="(.*?)" title="(.*?)" itemprop="url" class="clearfix">.*?<span class="img-body" style="background-image:url.(.*?).">'
 
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<li class=".*?">.*?<a href="(.*?)" title="(.*?)" itemprop="url" class="clearfix">.*?<span class="img-body" style="background-image:url.(.*?).">'
    
    sHtmlContent = sHtmlContent
    
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
           
            sTitle = aEntry[1]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
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
    sPattern = '<li class="active"><a id=".*?" href=".*?".*?">.*?</a></li>*?<li><a id=".*?" href="(.*?)"'
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
    sPattern = '<div id="video_container">(.+?)</video>'
     
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<source src="(.*?)" type="(.*?)"/>'
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
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox3',  sTitle, '', sThumbnail, '', oOutputParameterHandler)

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
                               streamurl=streamurl.replace('g‚',"")  
                               Url= "http://m.ok.ru/video/%s" % (streamurl.replace("ok/",""))
                               oOutputParameterHandler = cOutputParameterHandler()
                               oOutputParameterHandler.addParameter('siteUrl', Url)
                               oGui.addTV(SITE_IDENTIFIER, 'mokru', sMovieTitle, '', '', '', oOutputParameterHandler)     
                               
                if "mail/" in streamurl:                     
                               streamurl=streamurl.replace('mailg‚',"") 
                               urlan = re.findall('mail/(.*?)/(.*?)/', streamurl)
                               if urlan:         
                                           for (url1),(url2) in urlan:
                                
                               
                                                                                            
                                                      
                                                Url= "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (url1,url2)
                                                oOutputParameterHandler = cOutputParameterHandler()
                                                oOutputParameterHandler.addParameter('siteUrl', str(Url))
                                                oGui.addTV(SITE_IDENTIFIER, 'mailru', sMovieTitle, '', '', '', oOutputParameterHandler)	     
                                           
                                    			                                  
                if "vk/" in streamurl:     
                                   streamurl=streamurl.replace('g‚',"")  
                                   urlan = re.findall('vk/(.*?)/(.*?)/([a-z0-9]+)', streamurl)
                                   if urlan:         
                                           for (url1),(url2),(url3) in urlan:
                                
                               
                                                sHosterUrl= "http://vk.com/video_ext.php?oid=%s&id=%s&hash=%s" % (url1,url2,url3)
                                                
                if "uptostream/" in streamurl:     
                                      streamurl=streamurl.replace('g‚',"")  
                                      streamurl=streamurl.replace("uptostream/","") 
                                      
                                      sHosterUrl= "http://uptostream.com/iframe/%s" % (streamurl)
                                                         
                if "openload/" in streamurl:     
                                      streamurl=streamurl.replace('g‚',"")  
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
def sshowBox3():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "http://www.mynet.com/tv/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(url,headers=referer) 
     
    sHosterUrl = re.findall('<source src="(.*?)" type="video/mp4"/>', data, re.S)[0]
                            
                   



    

   

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
