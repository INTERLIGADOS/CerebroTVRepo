#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   
SITE_IDENTIFIER = 'diziizle_net'
SITE_NAME = 'diziizle.net'


URL_MAIN = 'http://www.diziizle.net/'
URL_http = 'http:'
MOVIE_HD = (True, 'showGenre')
YURL_MAIN = 'http://www.youtube.com/embed/'
from atv_com_tr import atvcomtr
from fox_com_tr import foxcomtr
from tv8_com_tr import tv8comtr
from trt_net_tr import trtnettr 
from showtv_com_tr import showtvcomtr
from diziizlehdfull_net import diziizlehdfulltr
from startv_com_tr import startvcomtr
from kanald_com_tr import  kanald
def turkdizi():
    oGui = cGui()
    liste = []
    liste.append( ['Dizi izle','https://canlitv.co/static/images/logo.png'])
    liste.append( ['Diziizle HDFull','http://www.fox.com.tr/upload/photos/1494588336.jpg'])
    liste.append( ['FOX TV ve Diziler','http://vignette2.wikia.nocookie.net/outcastdatabase/images/a/ac/Fox_logo.png/revision/latest?cb=20150807073232'] )
    liste.append( ['Kanal D ve Diziler','https://s.kanald.com.tr/ps/kanald_proxy/assets/img/logo.v2.png?v=7'] ) 
    liste.append( ['ATV ve Diziler','http://i.atv.com.tr/2016/10/05/1475672802843.png'])
    liste.append( ['STAR TV ve Diziler','https://upload.wikimedia.org/wikipedia/de/8/87/Logo_Star_TV_ab_2012.png']) 
    liste.append( ['SHOW TV ve Diziler','https://upload.wikimedia.org/wikipedia/commons/f/f1/Logo_of_Show_TV.png']) 
    liste.append( ['TV 8 ve Diziler','https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png']) 
    liste.append( ['TRT ve Diziler','http://www.trt.net.tr/images2012/trtlogo.png']) 
    
    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Kanal D ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'kanald',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'ATV ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'atvcomtr',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FOX TV ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'foxcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'SHOW TV ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'showtvcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'TV 8 ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'tv8comtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'TRT ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'trtnettr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'STAR TV ve Diziler':
             oGui.addMovie(SITE_IDENTIFIER, 'startvcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Dizi izle':
             oGui.addMovie(SITE_IDENTIFIER, 'diziizle', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Diziizle HDFull':
             oGui.addMovie(SITE_IDENTIFIER, 'diziizlehdfulltr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       
               
        else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
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
 
def mmshowGenre(): #affiche les genres
    oGui = cGui()
    
    
    Url = 'http://www.ddizi1.com/'
    
    urla  = "http://www.ddizi1.com/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url) 
  
    
   
    aResult =re.findall('<li><a href="(.*?)" title=".*?">(.*?)</a></li>', data, re.S)
  
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sGenre = cUtil().unescape(aEntry[1])
            Link = cUtil().unescape(aEntry[0])
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")

           
                       
            ssUrl = str(aEntry[0])
            if not 'http' in ssUrl:
                ssUrl = str(URL_MAIN) + ssUrl
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', ssUrl)
            oGui.addTV(SITE_IDENTIFIER, 'showSinema', sGenre, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def diziizle():
    oGui = cGui()
                 
    tarzlistesi = []
    tarzlistesi.append(("DIZILER", "https://www.diziizle.net/diziler/"))
    tarzlistesi.append(("DIZILER-ABC", "https://www.diziizle.net/diziler/"))
    tarzlistesi.append(("SINEMALAR", "https://www.diziizle.net/sinemalar/"))
    tarzlistesi.append(("SINEMALAR-ABC", "https://www.diziizle.net/sinemalar/"))
    tarzlistesi.append(("ANIMASYONLAR", "https://www.diziizle.net/sinemalar/?kategori=Animasyon"))
    tarzlistesi.append(("BELGESELLER", "https://www.diziizle.net/belgeseller/"))
    tarzlistesi.append(("BELGESELLER-ABC", "https://www.diziizle.net/belgeseller/"))
    tarzlistesi.append(("3D SINEMA", "https://www.diziizle.net/sinemalar/?kategori=3D"))    
    for sTitle,sUrl in tarzlistesi:
       
        sPicture= 'http://www.diziizle.net/resimler/logo.png'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if 'SINEMALAR-ABC' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'SinemaABC', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'DIZILER-ABC' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'dizizleABC', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'BELGESELLER-ABC' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'SinemaABC', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'SINEMALAR' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'ANIMASYONLAR' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif 'BELGESELLER' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif '3D SINEMA' in sTitle:
             oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def SinemaABC():
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
        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
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
        oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
       
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
        sPattern = '<div class="four-box"><div class="dizi-box2"><a title=".*?" href="(.*?)"><img src="(.*?)" width=".*?" height=".*?" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
                #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width="100" height="140" alt="(.*?)"'

    
    
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
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
                sPicture = str(URL_http) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_http) + sUrl
           
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
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

def FilmABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    ssUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(ssUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<strong>(.+?)</strong>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                

    Pattern = '<a href="(.*?)">(.*?)</a> &bull;'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
   
    print aResult
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
            sTitle = alfabekodla(aEntry[1])
                            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(ssUrl) + sUrl 
           
            
            sThumbnail= 'http://www.diziizle.net/resimler/logo.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'showSinema', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

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
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width="100" height="140" alt="(.*?)"/></a>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
      
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
                                                                                                                        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)".*?<div class="ad"><a href=".*?" title=".*?">(.*?)</a></div>'
    
    sHtmlContent = sHtmlContent.replace('<br/>','+').replace('//www.','http://www.')
    
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
                sPicture = str(URL_http) + sPicture
                
            sUrl = str(aEntry[0])
            Url = 'https://www.youtube.com/results?search_query='+sTitle   
            Url= Url.replace(' ','+')          
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'youtubeshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __bolmcheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def __bolmcheckForNextPage(sHtmlContent):                     
    urlan= re.findall('<td width="52">.+?&raquo; <a href=\'(.+?) \'.+?<a href=".+?" class="aktifsyfno">.+?</a></span><a href="(.+?)"',sHtmlContent,  re.S)  
    for (url2),(url3) in urlan:
        ssUrl ='http:'+url2+url3
        return ssUrl

    return False                                                      
              
def __checkForNextPage(sHtmlContent):                     
    urlan= re.findall('<link rel="canonical" href="(.+?)"/>.+?<a href=".+?" class="aktifsyfno">.+?</a></span><a href="(.+?)"',sHtmlContent,  re.S)  
    for (url2),(url3) in urlan:
        ssUrl ='http:'+url2+url3
        return ssUrl

    return False        

def Decode(param):
    #-- define variables
    loc_3 = [0,0,0,0]
    loc_4 = [0,0,0]
    loc_2 = ''
    #-- define hash parameters for decoding
    dec = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
    hash1 = ["0", "5", "u", "w", "6", "n", "H", "o", "B", "p", "N", "M", "D", "R", "z", "G", "V", "e", "i", "3", "m", "W", "U", "7", "g", "="]
    hash2 = ["c", "T", "I", "4", "Q", "Z", "v", "Y", "y", "X", "k", "b", "8", "a", "J", "d", "1", "x", "L", "t", "l", "2", "f", "s", "9", "h"]

    #-- decode
    for i in range(0, len(hash1)):
        re1 = hash1[i]
        re2 = hash2[i]

        param = param.replace(re1, '___')
        param = param.replace(re2, re1)
        param = param.replace('___', re2)

    i = 0
    while i < len(param):
        j = 0
        while j < 4 and i+j < len(param):
            loc_3[j] = dec.find(param[i+j])
            j = j + 1

        loc_4[0] = (loc_3[0] << 2) + ((loc_3[1] & 48) >> 4);
        loc_4[1] = ((loc_3[1] & 15) << 4) + ((loc_3[2] & 60) >> 2);
        loc_4[2] = ((loc_3[2] & 3) << 6) + loc_3[3];

        j = 0
        while j < 3:
            if loc_3[j + 1] == 64:
                break
            try:
                loc_2 += unichr(loc_4[j])
            except:
                pass
            j = j + 1

        i = i + 4;

    return loc_2




def showHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
                
    
    resp = net.http_GET(url)
    sHtmlContent = resp.content    
    oParser = cParser()
   
    sPattern = '<div class="video_ekran_player">(.*?)allowfullscreen'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult            
            
    sPattern = 'src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            
            sHosterUrl= aEntry
            if not 'http' in sHosterUrl:
                sHosterUrl = str(URL_http) + sHosterUrl
             
            if 'http://enter.az' in sHosterUrl:
                
                        
                        
                       Url = sHosterUrl             #test pr liens raccourcis
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'enteraz', '[COLOR violet]enter.az-resolver [COLOR teal]'+ sMovieTitle +'[/COLOR][/COLOR]', '', '', '', oOutputParameterHandler)	     
                
                            
              
             
            if '"http://embed.movshare.eu' in sHosterUrl:
              
                       			             
                       Url = sHosterUrl  	
                                                  
                                  #test pr liens raccourcis
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl',Url)
                       oGui.addTV(SITE_IDENTIFIER, 'estreamto', '[COLOR violet]OTV-resolver [COLOR teal]'+ sMovieTitle +'[/COLOR][/COLOR]', '', '', '', oOutputParameterHandler)	     
            
            if 'http://www.flashx.tv' in sHosterUrl:
              
                       			             
				
                                                      
                       Url = sHosterUrl             #test pr liens raccourcis
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'flashxx', '[COLOR violet]OTV-resolver [COLOR teal]'+ sMovieTitle +'[/COLOR][/COLOR]', '', '', '', oOutputParameterHandler)	     

            if 'goo.gl' in sHosterUrl:
                       
                       url = sHosterUrl
                       sHosterUrl = requests.get(url).content  
                      
                      

            if 'mail.ru' in sHosterUrl:
                       
                       Url = sHosterUrl
                       
                       oOutputParameterHandler = cOutputParameterHandler()
                       oOutputParameterHandler.addParameter('siteUrl', str(Url))
                       oGui.addTV(SITE_IDENTIFIER, 'mailru', '[COLOR violet]OTV-resolver [COLOR teal]'+ sMovieTitle +'[/COLOR][/COLOR]', '', '', '', oOutputParameterHandler)	     
	     

           
            
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()
def enteraz(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content
                          
    playlist = re.findall('<option value="(.*?)">(.*?)</option>', data, re.S)
    for sUrl,sGenre in playlist:
            
            sGenre = alfabekodla(sGenre)    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox25', sGenre, '', '', '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()  
def sshowBox25():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    import time
    urla  = "http://enter.az/flvplayerm/player.swf?=1"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
          
    file_url= re.findall('value="st=(.*?)&file=(.*?)&', data)
    if file_url:
	(st,fil) = (file_url)[0]
    url = 'http://gegen-abzocke.com/xml/nstrim/enter/code.php?code_url=' + fil
    sHosterUrl = requests.get(url).content  
     
    Header = '|User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X)'                                                                      
                          
          
    sHosterUrl = sHosterUrl+ '|' + Header
    
    sMovieTitle= alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    time.sleep(10)
    sThumbnail= 'http://www.diziizle.net/resimler/logo.png'
    if (oHoster != False):
         sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
         oHoster.setDisplayName(sMovieTitle)
         oHoster.setFileName(sMovieTitle)
         cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

def youtubeshowMovies(sSearch = ''):
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
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[0])

           
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
def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')

 
    sHosterUrl= 'https://www.youtube.com/watch?v=' + sUrl
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = sMovieTitle
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
  
def mp4canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    ssUrl= 'http://keepvid.com/?url=https://www.youtube.com/watch?v=' + Url
    oRequestHandler = cRequestHandler(ssUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = 'Full Video<\/dt>(.+?)Video Only<\/dt><dd>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
                

    Pattern = '<a href="([^"]+)&title.+?alt=""/>([^<]+)<\/span>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, Pattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sGenre = cUtil().unescape(aEntry[1])
            Link = cUtil().unescape(aEntry[0])
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")

           
                       
            ssUrl = str(aEntry[0])
            if not 'http' in ssUrl:
                ssUrl = str(URL_MAIN) + ssUrl
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', ssUrl)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox3', sGenre, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
  
   
    
    

    
def sshowBox3():
    oGui = cGui()
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
    