#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *    
                 
SITE_IDENTIFIER = 'karaoke_tr'
SITE_NAME = 'KARAOKE_TURK'
SITE_DESC = 'télévision'
MOVIE_HD = (True, 'showGenre')
URL_MAIN = 'http://www.fox.com.tr'
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
sRootArt = cConfig().getRootArt()
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
class track():
    def __init__(self,page,data=''):
        self.page=page
        self.page =0
        self.page += 1
        self.data=data


def load():
    linktv = cConfig().getSetting('pvr-view')
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Pour Modifier ou  Ajouter des chaînes à FramaPad https://annuel.framapad.org/p/vstream [/COLOR]', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_FREE)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'FramaPad (Bêta)', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_SFR)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Sfr TV', 'tv.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_ORANGE)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Orange TV', 'tv.png', oOutputParameterHandler)
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', URL_BG)
    # oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Bouygues TV', 'tv.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_WEB)
    oGui.addDir(SITE_IDENTIFIER, 'showWeb', 'Tv du web', 'tv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    oGui.addDir(SITE_IDENTIFIER, 'load', '[COLOR khaki]Tu veux voir ta chaîne sur Libretv.me alors partage ta chaîne![/COLOR]', 'libretv.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_LIBRETV)
    oGui.addDir(SITE_IDENTIFIER, 'showLibreMenu', 'Libretv.me', 'libretv.png', oOutputParameterHandler)


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
    from youtubecom_tr import KARAOKEturk                 
    KARAOKEturk()                
    oGui.setEndOfDirectory()
def sinemaABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []                
    liste.append( ['A',URL_MAIN+'/diziler?sw=a'] )
    liste.append( ['B',URL_MAIN+'/diziler?sw=b'] )
    liste.append( ['C',URL_MAIN+'/diziler?sw=c'] )
    liste.append( ['Ç',URL_MAIN+'/diziler?sw=ç'] )
    liste.append( ['D',URL_MAIN+'/diziler?sw=d'] )
    liste.append( ['E',URL_MAIN+'/diziler?sw=e'] )
    liste.append( ['F',URL_MAIN+'/diziler?sw=f'] )
    liste.append( ['G',URL_MAIN+'/diziler?sw=g'] )
    liste.append( ['H',URL_MAIN+'/diziler?sw=h'] )
    liste.append( ['I',URL_MAIN+'/diziler?sw=i'] )
    liste.append( ['İ',URL_MAIN+'/diziler?sw=i'] )
    liste.append( ['J',URL_MAIN+'/diziler?sw=j'] )
    liste.append( ['K',URL_MAIN+'/diziler?sw=k'] )
    liste.append( ['L',URL_MAIN+'/diziler?sw=l'] )
    liste.append( ['M',URL_MAIN+'/diziler?sw=m'] )
    liste.append( ['N',URL_MAIN+'/diziler?sw=n'] )
    liste.append( ['O',URL_MAIN+'/diziler?sw=o'] )
    liste.append( ['�',URL_MAIN+'/diziler?sw=ö'] )
    liste.append( ['P',URL_MAIN+'/diziler?sw=p'] )
    liste.append( ['R',URL_MAIN+'/diziler?sw=r'] )
    liste.append( ['S',URL_MAIN+'/diziler?sw=s'] ) 
    liste.append( ['ş',URL_MAIN+'/diziler?sw=ş'] ) 
    liste.append( ['T',URL_MAIN+'/diziler?sw=t'] )
    liste.append( ['U',URL_MAIN+'/diziler?sw=u'] )
    liste.append( ['Ü',URL_MAIN+'/diziler?sw=�'] )
    liste.append( ['V',URL_MAIN+'/diziler?sw=v'] )
    liste.append( ['W',URL_MAIN+'/diziler?sw=w'] )
    liste.append( ['X',URL_MAIN+'/diziler?sw=x'] )
    liste.append( ['Y',URL_MAIN+'/diziler?sw=y'] )
    liste.append( ['Z',URL_MAIN+'/diziler?sw=z'] )
    liste.append( ['0',URL_MAIN+'/diziler?sw=0'] )
    liste.append( ['1',URL_MAIN+'/diziler?sw=1'] )
    liste.append( ['2',URL_MAIN+'/diziler?sw=2'] )
    liste.append( ['3',URL_MAIN+'/diziler?sw=3'] )
    liste.append( ['4',URL_MAIN+'/diziler?sw=4'] )
    liste.append( ['5',URL_MAIN+'/diziler?sw=5'] )
    liste.append( ['6',URL_MAIN+'?harf=6'] )
    liste.append( ['7',URL_MAIN+'?harf=7'] )
    liste.append( ['8',URL_MAIN+'?harf=8'] )
    liste.append( ['9',URL_MAIN+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    liste = []
    liste.append( ['A',sUrl+'?harf=a'] )
    liste.append( ['B',sUrl+'?harf=b'] )
    liste.append( ['C',sUrl+'?harf=c'] )
    liste.append( ['Ç',sUrl+'?harf=ç'] )
    liste.append( ['D',sUrl+'?harf=d'] )
    liste.append( ['E',sUrl+'?harf=e'] )
    liste.append( ['F',sUrl+'?harf=f'] )
    liste.append( ['G',sUrl+'?harf=g'] )
    liste.append( ['H',sUrl+'?harf=h'] )
    liste.append( ['I',sUrl+'?harf=i'] )
    liste.append( ['İ',sUrl+'?harf=i'] )
    liste.append( ['J',sUrl+'?harf=j'] )
    liste.append( ['K',sUrl+'?harf=k'] )
    liste.append( ['L',sUrl+'?harf=l'] )
    liste.append( ['M',sUrl+'?harf=m'] )
    liste.append( ['N',sUrl+'?harf=n'] )
    liste.append( ['O',sUrl+'?harf=o'] )
    liste.append( ['�',sUrl+'?harf=ö'] )
    liste.append( ['P',sUrl+'?harf=p'] )
    liste.append( ['R',sUrl+'?harf=r'] )
    liste.append( ['S',sUrl+'?harf=s'] ) 
    liste.append( ['ş',sUrl+'?harf=ş'] ) 
    liste.append( ['T',sUrl+'?harf=t'] )
    liste.append( ['U',sUrl+'?harf=u'] )
    liste.append( ['Ü',sUrl+'?harf=�'] )
    liste.append( ['V',sUrl+'?harf=v'] )
    liste.append( ['W',sUrl+'?harf=w'] )
    liste.append( ['X',sUrl+'?harf=x'] )
    liste.append( ['Y',sUrl+'?harf=y'] )
    liste.append( ['Z',sUrl+'?harf=z'] )
    liste.append( ['0',sUrl+'?harf=0'] )
    liste.append( ['1',sUrl+'?harf=1'] )
    liste.append( ['2',sUrl+'?harf=2'] )
    liste.append( ['3',sUrl+'?harf=3'] )
    liste.append( ['4',sUrl+'?harf=4'] )
    liste.append( ['5',sUrl+'?harf=5'] )
    liste.append( ['6',sUrl+'?harf=6'] )
    liste.append( ['7',sUrl+'?harf=7'] )
    liste.append( ['8',sUrl+'?harf=8'] )
    liste.append( ['9',sUrl+'?harf=9'] )

               
    for sTitle,sUrl in liste:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()

def showdizi(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.fox.com.tr/bolum-izle'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
                                                                                                       

        sHtmlContent = reponse.read()                                                

         
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = '<div class="col-xs-12 col-sm-6 col-md-4 imgThumb">.*?<a href="(.*?)" alt="(.*?)" title=".*?">.*?<img class="img-responsive" src="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
                                                                                     

        oRequestHandler = cRequestHandler(sUrl)                                                                              
        sHtmlContent = oRequestHandler.request()
        

                                                            

                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="col span_.*?_of_.*? newsItem mb.*?".*?<a class="imageBox" href="(.*?)">.*?<img alt="" data-original="(.*?)">.*?<h5 class="mb5">(.*?)</h5></a>'

                          
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[2]) 
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
                    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)
            elif sTitle == 'Fatih Portakal ile FOX Ana Haber izle':
             oGui.addDir(SITE_IDENTIFIER, 'showhaber', sTitle, 'genres.png', oOutputParameterHandler)

            else:
             oGui.addMovie(SITE_IDENTIFIER, 'diziprogram', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def showhaber():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []
  
    tarzlistesi.append(("Haber B�ltenleri", "http://www.fox.com.tr/Fatih-Portakal-ile-FOX-Ana-Haber/haber-bultenleri"))
    tarzlistesi.append(("Haber Ekstralar", "http://www.fox.com.tr/Fatih-Portakal-ile-FOX-Ana-Haber/ekstra-videolar"))                                     
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'diziprogram', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()


def diziprogram(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.fox.com.tr/bolum-izle'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
         
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = "<div class='videoThmp'><a href='(.*?)' title='.*?'><img class='lazy' data-original='.*?' src='(.*?)' width='100%' alt='(.*?)'"                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.replace('"teamImg mobilThumb extravideolar"','"teamImg mobilThumb"').replace('programlar','webtv')
   


                                          
                                                                                                           	
                                          

        sPattern = '<div class="imageBox">.*?<a href="(.*?)">.*?<img alt="" src="(.*?)" />.*?<a href="/(.*?)/.*?/.*?">.*?<h4>(.*?)</h4>'
                                         
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
   
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = aEntry[2]+' : '+aEntry[3]
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
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
          
            sNextPage = __checkForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'diziprogram', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                              #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    

    
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<li class=\'active\'><a href=".*?">.*?</a></li>.*?<li ><a href="(.*?)">.*?</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MAIN)+ aResult[1][0]
    return False
def pageshowMovies(sSearch = ''):
    oGui = cGui()
   
    if sSearch:
        #on redecode la recherhce codé il y a meme pas une seconde par l'addon
        sSearch = urllib2.unquote(sSearch)
 
        query_args = { 'do' : 'search' , 'subaction' : 'search' , 'story' : str(sSearch) , 'x' : '0', 'y' : '0'}
        
        #print query_args
        
        data = urllib.urlencode(query_args)
        headers = {'User-Agent' : 'Mozilla 5.10'}
        url = 'http://www.fox.com.tr/bolum-izle'
        request = urllib2.Request(url,data,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
         
       #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern = "<div class='videoThmp'><a href='(.*?)' title='.*?'><img class='lazy' data-original='.*?' src='(.*?)' width='100%' alt='(.*?)'"                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        



                                                                                                             	
       
        sPattern = "<div class='videoThmp'><a href='(.*?)' title='.*?'><img class='lazy' data-original='.*?' src='(.*?)' width='100%' alt='(.*?)'"
                                 
    sHtmlContent = sHtmlContent.replace('klasik-diziler','webtv').replace('programlar','webtv')
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    print aResult
   
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
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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

def showshowHosters():
    oGui = cGui()
    import random
    import math   
    token=''
    token=math.floor(random.random() * 1000000 + 1)
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\u0026',"&")
    
                
    sPattern = '"Url":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    for track in aResult:
           
        sHosterUrl = track

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sMovieTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
def play__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oGuiElement.setThumbnail(sThumbnail)

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()
    return
        
    oGui.setEndOfDirectory()

def sshowBox2():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    import uuid
     
    
    # 1 seul resultat et sur leur propre hebergeur
    
        
        
            
    rest= 'http://mn-i.mncdn.com/foxtv_iphone/smil:foxtv_iphone.smil/playlist.m3u8?token=' + uuid.uuid4()
                                    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rest + '|' + Header  
    
                           
                  



    

   

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
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "http://www.fox.com.tr/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(url,headers=referer) 
     
    sHosterUrl = re.findall("desktopUrl = '(.*?)'", data, re.S)[0]
                            
                   



    

   

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
 

def showBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    urla  = "http://www.atv.com.tr/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
     
               
    playlist = re.findall('"Url":"(.*?)"', data, re.S)


    for track in playlist:
           
        
          
        sTitle = sTitle
        try: 
            sTitle = urllib.unquote_plus(sTitle)
        except:

            sTitle = 'atv.com.tr' 
        
        sHosterUrl = track

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  
def int_to_str( n, b, symbols='0123456789abcdefghijklmnopqrstuvwxyz'):
		return (int_to_str(n/b, b, symbols) if n >= b else "") + symbols[n%b]

def make_hash( s):
		return ''.join((int_to_str(int(s[lb:lb + 8], 16), 36) for lb in range(0, 32, 8)))   
def FOXshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    
   
    import uuid
     
    
    # 1 seul resultat et sur leur propre hebergeur
    
        
        
            
    sUrl= 'http://mn-i.mncdn.com/foxtv_iphone/smil:foxtv_iphone.smil/playlist.m3u8?token=' + uuid.uuid4()
            
       

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', sUrl)
    oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()
def showtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
                    
                             
    
    urla  = Url
                                         
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer)                         
    data= data.replace("\/",'/').replace("&quot;",'"').replace('var videoUrl = "','ht_stream_m3u8":"')    
               
    url = re.findall("mobile.*?src : '(.*?)'", data, re.S)[0]
    sUrl = "%s"  %  (url)
    sTitle =  alfabekodla(sTitle) 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()      