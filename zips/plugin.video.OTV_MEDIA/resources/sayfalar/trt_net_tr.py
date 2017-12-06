#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                  
SITE_IDENTIFIER = 'trt_net_tr'
SITE_NAME = 'TRT_net_tr'
SITE_DESC = 'télévision'

URL_MAIN = 'http://www.trt.tv'
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
sRootArt = cConfig().getRootArt()
MOVIE_HD = (True, 'showGenre')
class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data

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

 
def trtnettr():
    oGui = cGui()
    
    tarzlistesi = []
    
    tarzlistesi.append(("TRT TELEVIZYONLAR", "VIDEO"))
    tarzlistesi.append(("DİZİLER ve VIDEOLAR", "http://www.trt.tv/2/diziler"))
    tarzlistesi.append(("TRTHABER/VIDEO", "http://www.trthaber.com/video-galerileri.html"))
    
    for sTitle,sUrl2 in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TRT TELEVIZYONLAR':
             oGui.addDir(SITE_IDENTIFIER, 'trttelevis',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ve VIDEOLAR':
             oGui.addDir(SITE_IDENTIFIER, 'trtvideo', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'trtvideo',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()

def trtvideo():
    oGui = cGui()
                  
    tarzlistesi= []                
    tarzlistesi.append(("Dizi", "http://www.trt.tv/2/diziler"))
    tarzlistesi.append(("programlar", "http://www.trt.tv/20149/programlar"))
    tarzlistesi.append(("Belgesel", "http://www.trt.tv/20153/belgesel"))
    tarzlistesi.append(("cocuk", "http://www.trt.tv/20157/cocuk"))
		 
               
    for sTitle,sUrl in tarzlistesi:
        
        oOutputParameterHandler = cOutputParameterHandler()
        
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        
        oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()



def trttelevis():
    oGui = cGui()
                  
    tarzlistesi= []                
    tarzlistesi.append(("TRT 1 HD", "http://trtcanlitv-lh.akamaihd.net/i/TRT1HD_1@181842/master.m3u8", "http://www.trt.net.tr/img/logolar/2012/trt1hd_b.png"))
    tarzlistesi.append(("TRT HABER HD", "http://trtcanlitv-lh.akamaihd.net/i/TRTHABERHD_1@181942/master.m3u8", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTHABER.png"))
    tarzlistesi.append(("TRT SPOR HD", "http://trtcanlitv-lh.akamaihd.net/i/TRTSPOR1_1@182042/master.m3u8", "http://www.trtspor.com.tr/static/img/logo/logo.png"))
    tarzlistesi.append(("TRT World", "http://trtcanlitv-lh.akamaihd.net/i/TRTWORLD_1@321783/master.m3u8", "http://www.trt.net.tr/img/logolar/tv_logo/p_trthd.png"))
    tarzlistesi.append(("TRT Çocuk", "http://trtcanlitv-lh.akamaihd.net/i/TRTCOCUK_1@181844/master.m3u8", "http://www.trtcocuk.com/images/logo.gif"))
    tarzlistesi.append(("TRT Türk", "http://trtcanlitv-lh.akamaihd.net/i/TRTTURK_1@182144/master.m3u8", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTT%C3%9CRK.png"))
    tarzlistesi.append(("TRT Avaz", "http://trtcanlitv-lh.akamaihd.net/i/TRTAVAZ_1@182244/master.m3u8", "http://www.trtavaz.com.tr/img/avaz_header_kivrik.png"))
    tarzlistesi.append(("TRT Okul", "http://trtcanlitv-lh.akamaihd.net/i/TRTOKUL_1@182245/master.m3u8", "http://www.trtokul.com.tr//images/logo.png"))
    tarzlistesi.append(("TRT Müzik", "http://trtcanlitv-lh.akamaihd.net/i/TRTMUZIK_1@181845/master.m3u8", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTM%C3%9CZ%C4%B0K.png"))
    tarzlistesi.append(("TRT Belgesel", "http://trtcanlitv-lh.akamaihd.net/i/TRTBELGESEL_1@182145/master.m3u8", "http://www.trtbelgesel.net.tr/images/trtbelgesel-logo.png"))
    tarzlistesi.append(("TRT Arap�a", "http://trtcanlitv-lh.akamaihd.net/i/TRTARAPCA_1@181945/master.m3u8", "http://www.trtarabic.tv/ar/images/stories/demo/frontpage-new/rt1.jpg"))
    tarzlistesi.append(("TRT 6", "http://trtcanlitv-lh.akamaihd.net/i/TRT6_1@181944/master.m3u8", "http://www.trt.net.tr/trt6/img/logo2.png"))
               
    tarzlistesi.append(("TRT Diyanet", "http://trtcanlitv-lh.akamaihd.net/i/TRTDIYANET_1@182344/master.m3u8", "http://www.diyanet.tv/images/logo.png"))
    tarzlistesi.append(("TRT 3 - TBMM TV", "http://mecliscanlitv-lh.akamaihd.net/i/MECLISTV_1@127503/master.m3u8", "http://www.trt.net.tr/img/logolar/tv_logo/p_trt3tbmmtv.png"))

               
    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'sshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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

def showSinema(sSearch = ''):
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
        sPattern = '<div class="medyaKutu"><a href="(.*?)"><img src="(.*?)" width="120" height="90" /><br/>(.*?)<br/>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
       
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        


                                                                                         

                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="programs_item col-lg-3 col-md-3 col-sm-4 col-xs-4 col-xxs-6">.*?<a href="(.*?)">.*?<img class="img-responsive" src="(.*?)".*?<h4 class="video_name"><strong>(.*?)</strong>'
                                 
    sHtmlContent = sHtmlContent
    sHtmlContent =alfabekodla(sHtmlContent)
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
    
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle =alfabekodla(aEntry[2])
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
                oGui.addMovie(SITE_IDENTIFIER, 'showshowSinema', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
     
    Pattern = '<a href="(/diziler?sw=.*?)">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
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


def showshowSinema(sSearch = ''):
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
        sPattern = '<div class="medyaKutu"><a href="(.*?)"><img src="(.*?)" width="120" height="90" /> <br/>(.*?)<br/>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
       
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        


                                                                                         

                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="item_height col-lg-2 col-md-2 col-sm-3 col-xs-4 col-xxs-6" title="">.*?<a href="(.*?)">.*?<img src=".*?" class="play" alt="izle".*?<img src="(.*?)" alt="(.*?)"'
                                 
    sHtmlContent = sHtmlContent
   
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
   
 
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle =alfabekodla(aEntry[2])
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
                oGui.addMovie(SITE_IDENTIFIER, 'dizishowHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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



def pageshowMovies(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*? </em>.*?<em>(.*?)</em>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
                 
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                    

        sPattern = '<div class="programs_item .*?<a href="(.*?)">.*?<img class="img-responsive" src="(.*?)".*?<h4 class="video_name"><strong>(.*?)</strong></h4>'
    
    sHtmlContent = sHtmlContent.replace('<br />','<OTV>')
    
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
            
            sTitle =alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'dizishowHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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
                 
def __checkForNextPage(sHtmlContent):
    oGui = cGui()
                 
    sPattern = 'ajax-paging="/ajax/detail-video-list" page="(.+?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sHtmlContent)+'?&page='+ aResult[1][0]

    return False
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
        return False
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
    return False
        
    oGui.setEndOfDirectory()

def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "http://www.fox.com.tr/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
     
    streamDaten = re.findall("src : 'rtmp://.*?foxtv3(.*?)'", data, re.S)
    if streamDaten:
                  (serviceUrl )= streamDaten[0]
                       
                            
    sHosterUrl = "rtmp://foxtv-v.mncdn.com:80/foxtv_web playpath=mp4:foxtv3%s  swfUrl=http://img-foxtv2.mncdn.com/fox-player.swf  pageUrl=http://www.fox.com.tr/canli-yayin"  % (serviceUrl)



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False
def sshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =alfabekodla(sTitle) 
    
    
    urla  = "http://www.trt.net.tr/"
                       
    referer=[('Referer',urla)]
    page=gegetUrl(Url,headers=referer) 
     
   
    Title  = re.findall('BANDWIDTH=([0-9]+)', page)[0]
    if Title :
       video_tulpe_tmp = re.findall('BANDWIDTH=.*\\s(.*)', page)
       if len(video_tulpe_tmp) > 1:
          if video_tulpe_tmp[0].find('http') > -1:
             for tulpe in video_tulpe_tmp:
            
                     oInputParameterHandler = cInputParameterHandler()
                     tulpe=tulpe.replace('\r', '')
                     sTitle = oInputParameterHandler.getValue('sMovieTitle')
                     sMovieTitle = alfabekodla(sTitle)
                     sHosterUrl = tulpe

                     oGuiElement = cGuiElement()
                     oGuiElement.setSiteName(SITE_IDENTIFIER)
                     oGuiElement.setTitle(sMovieTitle)
                     oGuiElement.setMediaUrl(sHosterUrl)
        

                     oPlayer = cPlayer()
                     oPlayer.clearPlayList()
                     oPlayer.addItemToPlaylist(oGuiElement)
                     oPlayer.startPlayer()
                     return False
    oGui.setEndOfDirectory()
def dizishowHosters():

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    oParser = cParser()
                 
    sPattern = 'url: "(.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)

    # 1 seul resultat et sur leur propre hebergeur
    if (aResult[0] == True):
        
        
            
        web_url = '' + aResult[1][0]
            
        sHosterUrl = web_url

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sMovieTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return False
  
