#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                  

SITE_IDENTIFIER = 'showtv_com_tr'
SITE_NAME = 'SHOW TV'
SITE_DESC = 'télévision'
from resources.sayfalar.youtubecom_tr import youtubeplayer 
URL_MAIN = 'http://www.showtv.com.tr'
from xcanlitvzone import sshowBox19              

MOVIE_HD = (True, 'showGenre')
MOVIE_VIEWS = (True, 'showGenre')
icon = 'tv.png'        
sRootArt = cConfig().getRootArt()
URL_MAINA = "http://www.showtv.com.tr/dizi/pagination/%s/%s/%s"
class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data
ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
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
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
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

def decodeHtml(data):

	
		data = data.decode('unicode-escape').encode('UTF-8') 
		return data
 
def showtvcomtr():
    oGui = cGui()
                  
    tarzlistesi = []           
    tarzlistesi.append(("SHOWTV", "http://www.showtv.com.tr/canli-yayin"))
    tarzlistesi.append(("SHOWTV YEDEK", "https://www.youtube.com/watch?v=GdqjBKiz6s4"))
    
    tarzlistesi.append(("SHOWTURK", "http://www.showturk.com.tr/canli-yayin/showturk"))
    tarzlistesi.append(("SHOWMAX", "https://www.youtube.com/watch?v=DzPDPtxeY2Y"))
    tarzlistesi.append(("HABERTURK", "https://www.youtube.com/watch?v=5g0yljXFatk"))
    tarzlistesi.append(("BLOOMBERGHT", "http://www.bloomberght.com/tv"))
    tarzlistesi.append(("Business HT", "http://www.businessht.com.tr/canli-yayin"))
    tarzlistesi.append(("Diziler", "http://www.showtv.com.tr/diziler"))
    for sTitle,sUrl2 in tarzlistesi:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Diziler':
             oGui.addDir(SITE_IDENTIFIER, 'diziler',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SHOWTV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'youtubeplayer', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SHOWTV':
             oGui.addDir(SITE_IDENTIFIER, 'showtv2', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'SHOWMAX':
             oGui.addDir(SITE_IDENTIFIER, 'youtubeplayer', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'HABERTURK':
             oGui.addDir(SITE_IDENTIFIER, 'youtubeplayer', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showtv',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def trttelevis():
    oGui = cGui()
                    
    tarzlistesi= []                
    tarzlistesi.append(("TRT 1 HD", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trt1", "http://www.trt1.com.tr/_assets/img/trt1_logo.png"))
    tarzlistesi.append(("TRT HABER HD", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trthaber", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTHABER.png"))
    tarzlistesi.append(("TRT SPOR HD", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtspor", "http://www.trtspor.com.tr/static/img/logo/logo.png"))
    tarzlistesi.append(("TRT HD", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trthd", "http://www.trt.net.tr/img/logolar/tv_logo/p_trthd.png"))
    tarzlistesi.append(("TRT Çocuk", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtcocuk", "http://www.trtcocuk.com/images/logo.gif"))
    tarzlistesi.append(("TRT T�rk", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtturk", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTT%C3%9CRK.png"))
    tarzlistesi.append(("TRT Avaz", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtavaz", "http://www.trtavaz.com.tr/img/avaz_header_kivrik.png"))
    tarzlistesi.append(("TRT Okul", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtokul", "http://www.trtokul.com.tr//images/logo.png"))
    tarzlistesi.append(("TRT M�zik", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtmuzik", "http://www.trt.net.tr/img/logolar/tv_logo/p_TRTM%C3%9CZ%C4%B0K.png"))
    tarzlistesi.append(("TRT Belgesel", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtbelgesel", "http://www.trtbelgesel.net.tr/images/trtbelgesel-logo.png"))
    tarzlistesi.append(("TRT Arap�a", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtarapca", "http://www.trtarabic.tv/ar/images/stories/demo/frontpage-new/rt1.jpg"))
    tarzlistesi.append(("TRT 6", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trt6", "http://www.trt.net.tr/trt6/img/logo2.png"))
    tarzlistesi.append(("TRT 6 (TR-ZAZ)", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=tv6tr", "http://www.trt.net.tr/img/logolar/tv_logo/p_tv6tr.png"))
               
    tarzlistesi.append(("TRT Diyanet", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trtdiyanet", "http://www.diyanet.tv/images/logo.png"))
    tarzlistesi.append(("TRT 3 - TBMM TV", "http://www.trt.net.tr/anasayfa/canli.aspx?y=tv&k=trt3tbmmtv", "http://www.trt.net.tr/img/logolar/tv_logo/p_trt3tbmmtv.png"))

               
    for sTitle,sUrl,sPicture in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
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

def diziler(sSearch = ''):
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
         
      
        sPattern = '<div class="dizi.*?id="dizi.*?">.*?<a href="(.*?)"><img class="diziImage" src="(.*?)".*?<li class="dizi_adi">(.*?)</li>'                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent= sHtmlContent.replace('<li class="white">','<li class="black">')


                                                                             
                                                                          

                    
        sPattern = '<li class="black">.*?<a href="(/dizi/.*?)">.*?<img src="(.*?)">.*?<div class="title">(.*?)</div>'
                                                                                     

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
                oGui.addMovie(SITE_IDENTIFIER, 'showdizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def mHosters():
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

def dizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
                      
    referer=[('Referer',Url)]
    url=gegetUrl(Url,headers=referer) 
       
            
    name ='test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

def showdizi(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        Url = oInputParameterHandler.getValue('siteUrl')
        urla  = "http://www.showtv.com.tr/"
                                                    
        referer=[('Referer',urla)]
        data=gegetUrl(Url,headers=referer) 
                                                 
        streamDaten = re.findall('<div class="swiper-wrapper">.*?<a href="(/dizi/tum_bolumler.*?)"', data, re.S) 
        sUrl = "http://www.showtv.com.tr%s"  % (streamDaten[0])     
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        



                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                                                                                                                                                                     
        sPattern = '<div class="box-xs-12 box-sm-12 box-md-6 box-lmd-4 box-lg-4 iterate">.*?<a data-ajax-link  href="(/dizi/tum_bolumler.*?)".*?<img data-ajax-image  src="(.*?)">.*?<div class="box-info-title"  data-ajax-title>(.*?)</div>'
                                 
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
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'Genreparca', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
            sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizi2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

from resources.lib import gPlayer
def partnext(s):
      s=s
      if '-parca-1-izle/' in s:
	s=s.replace('-parca-1-izle/','-parca-1-izle/')
        return s 
      if '-parca-1-izle/' in s:
	s=s.replace('-parca-1-izle/','-parca-2-izle/')
        return s 
      if '-parca-2-izle/' in s:
	s=s.replace('-parca-2-izle/','-parca-3-izle/')
        return s 
      if '-parca-3-izle/' in s:	
        s=s.replace('-parca-3-izle/','-parca-4-izle/')
        return s 
      if '-parca-4-izle/' in s:	
        s=s.replace('-parca-4-izle/','-parca-5-izle/')
        return s 
      if '-parca-5-izle/' in s:	
        s=s.replace('-parca-5-izle/','-parca-6-izle/')
        return s 
      if '-parca-6-izle/' in s:	
        s=s.replace('-parca-4-izle/','-parca-7-izle/')
        return s 
      if '-parca-7-izle/' in s:	
        s=s.replace('-parca-5-izle/','-parca-8-izle/')
        return s 
      return False 
     
def playnext(url):
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'[makelist.param3]','Accept':'/*','Connection':'keep-alive'}).text
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("\u0130",'I')          
    link=re.findall('"name":"Standart","file":"(.*?)","type":"application/x-mpegURL"',sHtmlContent)[0]
    return link       
      

def Genreparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sHtmlContent=requests.get(url,headers={'User-Agent':ua,'Referer':'http://www.showtv.com.tr/','Accept':'/*','Connection':'keep-alive'}).text
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("\u0130",'I')          
    urll='http://www.showtv.com.tr'+re.findall('<li class="selected"><a href="(.*?)">',sHtmlContent)[0]
    
   
      

   
    
    
   
    sUrl =playnext(urll.replace("-parca-1-izle/",'-parca-1-izle/'))
    sUrl1 =playnext(urll.replace("-parca-1-izle/",'-parca-2-izle/'))
    sUrl2 =playnext(urll.replace("-parca-1-izle/",'-parca-3-izle/'))
    sUrl3 =playnext(urll.replace("-parca-1-izle/",'-parca-4-izle/'))
    sUrl4 =playnext(urll.replace("-parca-1-izle/",'-parca-5-izle/'))
    sUrl5 =playnext(urll.replace("-parca-1-izle/",'-parca-6-izle/'))
    sUrl6 =playnext(urll.replace("-parca-1-izle/",'-parca-7-izle/'))
    sUrl7 =playnext(urll.replace("-parca-1-izle/",'-parca-8-izle/'))
    
    playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl,listitem1);
    listitem2 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl1,listitem2);
    listitem3 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl2,listitem3);
    listitem4 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl3,listitem4);
    listitem5 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl4,listitem5);                                                                         
    listitem6 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl5,listitem6);
    listitem7 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl6,listitem7);                                                                         
    listitem8 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl7,listitem8);
    player_type = sPlayerType()
    xbmcPlayer = xbmc.Player (player_type); 
    xbmcPlayer.play (playlist)    


def showdizi2(sSearch = ''):
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
        sPattern = '<li>.*?<a href="(/.*?)">.*?<img alt="" class="lazyload" data-original="(.*?)" src=".*?"></img>.*?<strong>(.*?)</strong>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
           
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        


                                                          
                                                                                                             	
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'                      
                                                                                                                                                                                     
        sPattern = '"title":"(.*?)".*?"image":"(.*?)".*?"link":"(.*?)"'
                                    
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("\u0130",'I')                                              
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
           
            sTitle = cUtil().unescape(aEntry[0])
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[2])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl 
           
            #not found better way
          
            sTitle =alfabekodla(sTitle)
           
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
            sNextPage = __ccheckForNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showdizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
                
def __ccheckForNextPage(sHtmlContent):

    url = re.findall('<div class="center">.*?<a href="javascript:void.*?" class="load-more-button" id="loadMoreItem" data-serie="(.*?)" data-type="(.*?)" data-page="(.*?)">',sHtmlContent, re.S)
    for bir,iki,uc in url:
        URL= "http://www.showtv.com.tr/dizi/pagination/%s/%s/%s"% (bir,iki,uc)
        return str(URL)
    return False    
def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    
                
    sHtmlContent = sHtmlContent.replace("\/",'/').replace("\u0130",'I')          
    Pattern = '"name":"(.*?)","file":"(.*?)","type":"video/mp4"'
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
           
            sTitle = cUtil().unescape(aEntry[0])
            
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl 
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addTV(SITE_IDENTIFIER, 'sshow', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()   
def showshowHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace("\/",'/')
    
    sHtmlContent = alfabekodla(sHtmlContent)            
    sPattern = 'var videoUrl = "(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    for track in aResult:
           
        sHosterUrl = track
        sTitle =alfabekodla(sTitle)
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return False
def showtv2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    data= data.replace("\/","/").replace('playlist.m3u8','chunklist_b848000.m3u8')
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    url  = re.findall('"ht_stream_m3u8":"(.*?)"', data, re.S)[0]                                      
    
        
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    sHosterUrl= url+'|' + Header 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 


class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True    


def showtv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                             
    
    urla  = Url
                                         
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer)                         
    data= data.replace("\/",'/').replace("&quot;",'"').replace('var videoUrl = "','ht_stream_m3u8":"')    
               
    sUrl = re.findall('"ht_stream_m3u8":"(.*?)"', data, re.S)[0]
    
    
    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
    url= sUrl+ '|' + Header 
    name=  alfabekodla(sTitle) 
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    progress.update( 20, "", 'OTV HLS Player', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played
class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player().play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True    
def sshow():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
    sHosterUrl = sHosterUrl + '|' + Header 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  

def diziplay():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
                             
    
    urla  = Url
                                         
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer)                         
    data= data.replace("\/",'/') 
               
    url = re.findall('"name":"Standart","file":"(.*?)"', data, re.S)[0]
                      
    sTitle =  alfabekodla(sTitle) 
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(url)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
    return False