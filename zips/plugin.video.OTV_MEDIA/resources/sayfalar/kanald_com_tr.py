#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                 
SITE_IDENTIFIER = 'kanald_com_tr'
SITE_NAME = 'KANAL D'
SITE_DESC = 'Replay TV'
NURL_MAIN= 'http://www.netd.com'
MOVIE_diziizle = 'https://www.kanald.com.tr'
URL_MAIN = 'http://www.netd.com/dizi'
URL_DMAIN = 'https://www.kanald.com.tr'
URL_PIC = 'http://assets.dogannet.tv/img/75/327x183/'
MOVIE_VIEWS = (True, 'showGenre')
MOVIE_HD = (True, 'showGenre')
URL_engelsiz = 'http://engelsiz.kanald.com.tr'
URL_engelsizpic = 'http://engelsiz.kanald.com.tr/'                  
def CleanTitle(title):
    title = cUtil().unescape(title)
    title = cUtil().removeHtmlTags(title)
    try:
        #title = unicode(title, 'utf-8')
        title = unicode(title, 'iso-8859-1')
    except:
        pass
    title = unicodedata.normalize('NFD', title).encode('ascii', 'ignore')
    
    return title.encode( "utf-8")
from atv_com_tr import atvcomtr
from fox_com_tr import foxcomtr
from tv8_com_tr import tv8comtr
from trt_net_tr import trtnettr 
from showtv_com_tr import showtvcomtr
from xcanlitvzone import Canlitvzone
from startv_com_tr import startvcomtr
from xCanLiTVlive import CanLiTVlive
from xstreamcanlitv import streamcanlitv
from xiptvozel import user_info
from xstreamcanlitv import iostreamcanlitv2
from liveonlinetv247 import turktvHosters
def turkTV():
    oGui = cGui()
    liste = []
      
    liste.append( ['FOX TV Sayfa','http://vignette2.wikia.nocookie.net/outcastdatabase/images/a/ac/Fox_logo.png/revision/latest?cb=20150807073232'] )
    liste.append( ['Kanal D Sayfa','https://upload.wikimedia.org/wikipedia/tr/thumb/c/ca/Kanal_D_logo.svg/943px-Kanal_D_logo.svg.png'] ) 
    liste.append( ['ATV Sayfa','http://i.atv.com.tr/2016/10/05/1475672802843.png'])
    liste.append( ['STAR TV Sayfa','https://upload.wikimedia.org/wikipedia/de/8/87/Logo_Star_TV_ab_2012.png']) 
    liste.append( ['SHOW TV Sayfa','https://upload.wikimedia.org/wikipedia/commons/f/f1/Logo_of_Show_TV.png']) 
    liste.append( ['TV 8 Sayfa','https://img.tv8.com.tr/s/template/v2/img/tv8-logo.png']) 
    liste.append( ['TRT Sayfa','http://www.trt.net.tr/images2012/trtlogo.png']) 
    liste.append( ['IPTV TV live','http://www.filmi-izle.org/wp-content/themes/KralFilm/logo/logo.png'])
    liste.append( ['Canli TV live.IO','http://mobile.canlitvlive.io/images/mobil-footer.png'] ) 
    liste.append( ['Canli TV zone','https://canlitv.co/static/images/logo.png'])
    liste.append( ['Canli TV live','http://www.canlitv.com/resimler/css/canlitv_logo.png'])
    liste.append( ['Canli TV stream','http://kesintisiz.tv/static/images/logo.png'])
    

    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Kanal D Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'kanald',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'ATV Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'atvcomtr',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FOX TV Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'foxcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'SHOW TV Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'showtvcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'TV 8 Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'tv8comtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'TRT Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'trtnettr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'STAR TV Sayfa':
             oGui.addMovie(SITE_IDENTIFIER, 'startvcomtr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Canli TV zone':
             oGui.addMovie(SITE_IDENTIFIER, 'Canlitvzone', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Canli TV live':
             oGui.addMovie(SITE_IDENTIFIER, 'CanLiTVlive', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Canli TV stream':
             oGui.addMovie(SITE_IDENTIFIER, 'Canlitvzone', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'IPTV TV live':
             oGui.addMovie(SITE_IDENTIFIER, 'turktvHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Canli TV live.IO':
             oGui.addMovie(SITE_IDENTIFIER, 'iostreamcanlitv2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

               
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


def partnext(s):
      s=s
      if 'part=1-6' in s:
	s=s.replace('part=1-6','part=1-6')
        return s 
      if 'part=1-6' in s:
	s=s.replace('part=1-6','part=2-6')
        return s 
      if 'part=2-6' in s:
	s=s.replace('part=2-6','part=3-6')
        return s 
      if 'part=3-6' in s:	
        s=s.replace('part=3-6','part=4-6')
        return s 
      if 'part=4-6' in s:	
        s=s.replace('part=4-6','part=5-6')
        return s 
      if 'part=5-6' in s:	
        s=s.replace('part=5-6','part=6-6')
        return s 
      return False 
def sEcho(s):
      s=s
      if '=1' in s:
	s=s.replace('=1','=2')
        return s 
      if '=2' in s:
	s=s.replace('=2','=3')
        return s 
      if '=3' in s:	
        s=s.replace('=3','=4')
        return s 
      if '=4' in s:	
        s=s.replace('=4','=5')
        return s 
      if '=5' in s:	
        s=s.replace('=5','=6')
        return s 
      if '=6' in s:	
        s=s.replace('=6','=7')
        return s 
      if '=7' in s:	
        s=s.replace('=7','=8')
        return s 
      if '=8' in s:	
        s=s.replace('=8','=9')
        return s 
      if '=9' in s:	
        s=s.replace('=9','=10')
        return s 
      if '=10' in s:	
        s=s.replace('=10','=11')
        return s 
      if '=11' in s:	
        s=s.replace('=11','=12')
        return s 
      if '=12' in s:	
        s=s.replace('=12','=13')
        return s 
      if '=13' in s:	
        s=s.replace('=13','=14')
        return s 
      if '=14' in s:	
        s=s.replace('=14','=15')
        return s 
      if '=15' in s:	
        s=s.replace('=15','=16')
        return s 
      if '=16' in s:	
        s=s.replace('=16','=17')
        return s
      if '=17' in s:	
        s=s.replace('=17','=18')
        return s 
      if '=18' in s:	
        s=s.replace('=18','=19')
        return s 
      if '=19' in s:	
        s=s.replace('=19','=20')
        return s 
      if '=20' in s:	
        s=s.replace('=20','=21')
        return s 
      if '=21' in s:	
        s=s.replace('=21','=22')
        return s 
      if '=22' in s:	
        s=s.replace('=22','=23')
        return s 
      if '=23' in s:	
        s=s.replace('=23','=24')
        return s 
      if '=24' in s:	
        s=s.replace('=24','=25')
        return s 
      if '=25' in s:	
        s=s.replace('=25','=26')
        return s 
      if '=26' in s:	
        s=s.replace('=26','=27')
        return s 
      if '=27' in s:	
        s=s.replace('=27','=28')
        return s 
      if '=28' in s:	
        s=s.replace('=28','=29')
        return s 
      if '=29' in s:	
        s=s.replace('=29','=30')
        return s 
      if '=30' in s:	
        s=s.replace('=30','=31')
        return s 
      if '=31' in s:	
        s=s.replace('=31','=32')
        return s 
      if '=32' in s:	
        s=s.replace('=32','=33')
        return s 
      if '=33' in s:	
        s=s.replace('=33','=34')
        return s 
      if '=34' in s:	
        s=s.replace('=34','=35')
        return s 
      if '=35' in s:	
        s=s.replace('=35','=36')
        return s 
      if '=36' in s:	
        s=s.replace('=36','=37')
        return s 
      if '=37' in s:	
        s=s.replace('=37','=38')
        return s 
      if '=38' in s:	
        s=s.replace('=38','=39')
        return s 
      if '=39' in s:	
        s=s.replace('=39','=40')
        return s 
      if '=40' in s:	
        s=s.replace('=40','=41')
        return s 
      if '=41' in s:	
        s=s.replace('=41','=42')
        return s 
      if '=42' in s:	
        s=s.replace('=42','=43')
        return s 
      if '=43' in s:	
        s=s.replace('=43','=44')
        return s 
      if '=44' in s:	
        s=s.replace('=44','=45')
        return s 
      if '=45' in s:	
        s=s.replace('=45','=46')
        return s 
      if '=46' in s:	
        s=s.replace('=46','=47')
        return s 
      if '=47' in s:	
        s=s.replace('=47','=48')
        return s 
      if '=48' in s:	
        s=s.replace('=48','=49')
        return s 
      if '=49' in s:	
        s=s.replace('=49','=50')
        return s 
      return False 


          

def kanald():
    oGui = cGui()
    tarzlistesi= []
    tarzlistesi.append(("KANAL D CANLI.TV", "http://www.netd.com/canli-yayin"))
    
    
    tarzlistesi.append(("Yeni DIZILER", "https://www.kanald.com.tr/diziler"))
    tarzlistesi.append(("Tüm Arşiv Dizileri", "https://www.kanald.com.tr/diziler/arsiv"))
    tarzlistesi.append(("Görme ve Işitme Engelliler için DIZILER", "http://engelsiz.kanald.com.tr/"))
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'KANAL D CANLI.TV':
             oGui.addDir(SITE_IDENTIFIER, 'kanaldTV', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'MUZIK':
             oGui.addDir(SITE_IDENTIFIER, 'showMUZIK', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Yeni DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Tüm Arşiv Dizileri':
             oGui.addDir(SITE_IDENTIFIER, 'dpageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Görme ve Isitme Engelliler için DIZILER':
             oGui.addDir(SITE_IDENTIFIER, 'showengelsiz', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
  
def kanaldTV():
    oGui = cGui()
    tarzlistesi= []                                                                                                                                                  
    tarzlistesi.append(("Kanal D Canlı Yayın", "https://s.kanald.com.tr/ps/kanald_proxy/assets/img/kanal-d.png?v=2", "https://www.kanald.com.tr/actions/content/media/542410a361361f36f4c3fcf1"))
    tarzlistesi.append(("CNN T�RK Canlı Yayın", "http://i.cnnturk.com/ps/cnnturk_proxy/ContentMainPage/frontEnd/images/cnnturk-logo.png", "http://www.cnnturk.com/action/media/51cc1dbd32dc9f19b8bc77cf"))
    tarzlistesi.append(("TV2 Canlı Yayın", "http://www.tv2.com.tr/assets/img/logo.png", "http://www.teve2.com.tr/action/media/564da04ef5ac761dbc5e0a13"))
    tarzlistesi.append(("Dream Turk Canlı Yayın", "http://dreamq.dogannet.tv/images/100/800x450/571f37e3980ea80bc034ee2b", "http://dreamturk.com.tr/actions/content/media/566ab958980ea810b4658d96"))
    tarzlistesi.append(("Dream TV Canlı Yayın", "http://www.dreamtv.com.tr/content/frontEnd/images/dream-tv-logo.png", "http://www.dreamtv.com.tr/actions/content/media/5565d197f5ac76262cb2bba5"))
    tarzlistesi.append(("Tay TV Canlı Yayın", "http://www.dreamturk.com.tr/content/frontEnd/images/dream-turk-logo.png", "http://www.dreamtv.com.tr/actions/content/media/5565d197f5ac76262cb2bba5"))
    tarzlistesi.append(("Disney", "https://s.kanald.com.tr/ps/kanald_proxy/assets/img/d-smart-v2.png", "http://www.tv2.com.tr/actions/content/media/564da04ef5ac761dbc5e0a13"))
    for sTitle,sPicture,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

       
    oGui.setEndOfDirectory()
def showengelsiz(sSearch = ''):
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
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()                      
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<li><a href="(.*?)" title="(.*?)">.*?<img src="(.*?)"'
          

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
                  
            sTitle = aEntry[1]
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_engelsizpic) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_engelsiz) + sUrl
           
           
           
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sPicture))
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'engelsizparca', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'engelsizparca', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def engelsizparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPicture= oInputParameterHandler.getValue('sThumbnail')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request() 
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '').replace('" selected>', '" >')
    oParser = cParser()
    sPattern = 'div class="list">(.*?)</select>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                                    
    sPattern = '<option value="(.*?)" >(.*?)</option>'
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
           
            wq = 'http://engelsiz.kanald.com.tr/Video/Detail/'+aEntry[0]+'/1'
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', wq)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'engelsizBox', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()
def engelsizBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    urla  = "https://www.kanald.com.tr"
     
                                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    key= re.findall("key: '(.*?)'", data)[0]   
    Server= re.findall("url: '(mp4:engelsiz/.*?.mp4)'", data)[0]
    sUrl = "rtmp://213.243.32.91:1935/vod/%s" %( Server)
     
 
   
                                                                               
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()

def showMUZIK(sSearch = ''):
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
        sPattern = '<div class="resim" id=".*?"><a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()                      
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<noscript><img src="(.*?)".*?<a href="(.*?)">.*?<b>(.*?)</span>'
    
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
                  
            sTitle = aEntry[2]+' [COLOR lightblue]'
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_PIC) + sPicture
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
           
           
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('Picture', str(sTitle))
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showMovies', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMUZIK', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def showMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')

    urla  = "https://www.kanald.com.tr/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
       
    streamDaten = re.findall('<i class="fa fa-fw fa-embed"></i></a><a class="flat action-add" data-id="(.*?)"', data, re.S) 
    sUrl = "http://www.netd.com/muzik/actions/music/getmusicvideo/%s"  % (streamDaten[0])       
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '"Title":"(.*?)","Url":"(.*?)".*?"Image":"(.*?)"'
    
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
            sTitle = alfabekodla(aEntry[0])
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_PIC) + sPicture
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
           
           
           
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()

def dpageshowMovies(sSearch = ''):
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
        url = oInputParameterHandler.getValue('siteUrl')
        urla= ":https://www.kanald.com.tr/"
        referer=[('Referer',urla)]
             
        sHtmlContent=gegetUrl(url,headers=referer)           

                                                                      
                                                                                                                  
                                                                                                                    
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="col-sm-6"><a class="thumbnail thumbnail-featured " href="(.*?)"><img src=".*?" data-src="(.*?)" alt="(.*?)"'
        
                                                     
                                                               
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    sHtmlContent = sHtmlContent.replace('u002F', "").replace('\\', "/")
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
            sPicture ='http:' +str(aEntry[1])
            
            sTitle = alfabekodla(sTitle)    
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_DMAIN) + sUrl + '/bolumler?page=1'
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pageshowDizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
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
        sPattern = '<div class="film">.*?<a href="(.*?)" title=".*?"><img src="(.*?)" width=".*?" height=".*?"  alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        urla= "https://www.kanald.com.tr/"
        referer=[('Referer',urla)]
             
        sHtmlContent=gegetUrl(url,headers=referer)           
        sHtmlContent = sHtmlContent.replace('&nbsp;', " saat:").replace('YAKINDA', "Yakinda Kanal D'de!")

                    
                                      
        
        sPattern = '<div class="col-sm-6">.*?<a class="thumbnail.*?" href="(.*?)">.*?<img src=".*?" data-src="(.*?)" alt="(.*?)".*?<b class="info hidden-xs"><span><small>(.*?)</small>(.*?)</span>'
        
    
    
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
           
            sTitle = aEntry[2]+' '+aEntry[3]+aEntry[4]
            
           
            sPicture ='http:' +str(aEntry[1])
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_DMAIN) + sUrl + '/bolumler?page=1'
                                                                
            sTitle = alfabekodla(sTitle)
                                                  
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('Picture', sPicture)
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pageshowDizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
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
        Pagen = oInputParameterHandler.getValue('siteUrl')
        sPicture = oInputParameterHandler.getValue('Picture')
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        if  'Yakinda' in sMovieTitle:
                showMessage("Yakinda Kanal D'de!")
           
                                             
       
        oRequestHandler = cRequestHandler(Pagen)
        sHtmlContent = oRequestHandler.request()       
        sHtmlContent = sHtmlContent.replace('[]', "").replace('u002F', "").replace('\\', "/").replace('\u002Fp', "").replace('\u003C', "").replace('\u003Cp', "").replace('\u003E', "")
                                                                      
                                                                                                                                  
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="col-lg-12"><div class="bg clearfix"><a href="(.*?)" class="thumbnail".*?src=".*?" data-src="(.*?)" alt="(.*?)"'
                                          
                                                               
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
           
           
                                                      
            
            sTitle = alfabekodla(aEntry[2])
                                                  
                           
#            sUrl ='http://www.netd.com'+ str(aEntry[1])+'/2500/prog_index.m3u8?'
            sPicture =  aEntry[1]
            sUrl ='https://www.kanald.com.tr'+ str(aEntry[0])
            if not 'http' in sUrl:
                sUrl ='https://www.kanald.com.tr'+ str(aEntry[1])
           
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            
            oGui.addTV(SITE_IDENTIFIER, 'DDizioynat', sTitle, '', sPicture, sPicture, oOutputParameterHandler)
        cConfig().finishDialog(dialog)
           
        if not sSearch:                                          
            
               sNextPage =sEcho(str(Pagen))
               if (sNextPage != False):
                  oOutputParameterHandler = cOutputParameterHandler()
                  oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                  oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def DDizioynat():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
    
       
    urla  = "https://www.kanald.com.tr"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    Server= re.findall('"contentid", "(.*?)"', data)[0]
    sUrl = "https://www.kanald.com.tr/actions/content/media/%s" %( Server)+'?p=1&pc=6'  
    referer=[('Referer',urla)]
    dat=gegetUrl(sUrl,headers=referer)  
    Serv= re.findall('"SecurePath":"(.*?)"', dat)[0]
    if not 'http' in Serv:
           sUrl = "https://soledge4.dogannet.tv//%s" %( Serv.replace('\u0026', "&").replace('&part=6-6', "&part=1-6"))  
    sUrl =sUrl+TIK                           
    playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    playlist.clear();
    listitem1 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=1-6'),listitem1);
    listitem2 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=2-6'),listitem2);
    listitem3 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=3-6'),listitem3);
    listitem4 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=4-6'),listitem4);
    listitem5 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=5-6'),listitem5);                                                                         
    listitem6 = xbmcgui.ListItem(''+name)
    playlist.add(sUrl.replace('part=1-6','part=6-6'),listitem6);
    
    player_type = sPlayerType()
    xbmcPlayer = xbmc.Player (player_type); 
    xbmcPlayer.play (playlist)       

def sPlayerType():
        
       
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False

def __createDisplayStart(iPage):
    return (1 * int(iPage)) - 1
         
def pageshowDizi2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    sHtmlContent=gegetUrl(Url,headers=referer)     
    

        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
#    sPattern = '"video":."description":".*?","title":"(.*?)","sys":.*?"domain_id":"(.*?)","membership_id":"netd".,"colors":.*?"uploadDate":".*?","_id":"(.*?)","metadata":."application".*?"value":"(.*?)"'
    sPattern = '"video":."description":".*?","title":"(.*?)".*?"value":"(.*?)".*?"_id":"(.*?)"'
  
    sHtmlContent = sHtmlContent.replace('u002F', "")
    
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
            sTitle = alfabekodla(aEntry[0])
            sPicture = 'http://assets.dogannet.tv/img/75/327x183/'+ str(aEntry[2])
                           
#            sUrl ='http://www.netd.com'+ str(aEntry[1])+'/2500/prog_index.m3u8?'
            
           
           
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl ='http://media.netd.com.tr/'+ str(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture,  'genres.png', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
        sNextPage =sEcho(str(Url))
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
 
    
        oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    
    sPattern = '<li class="active"><a href=".*?" class="nuxt-link-exact-active active">.*?</a></li><li><a href="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        sUrl ="http://www.netd.com"+ aResult[1][0] 
        return sUrl
               
 

 
def udizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    Url = oInputParameterHandler.getValue('siteUrl')

    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
       
    streamDaten = re.findall('<div class="col-md-3 col-sm-6"><div class="thumbnail thumbnail-play"><span><!----><a href="(.*?)"', data, re.S) 
    sUrl = "http://www.netd.com%s"  % (streamDaten[0])      
    oRequestHandler = cRequestHandler(sUrl)
    Server = oRequestHandler.request()
  
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
#    s
    aResult= re.findall('"video":."description":".*?","title":"(.*?)".*?"value":"(.*?)"',Server, re.S|re.I)
    for name,sHosterUrl in aResult:
    
        url='http://media.netd.com.tr/' +sHosterUrl
      
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
def pageshowABC(sSearch = ''):
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
        sPattern = '"title":"(.*?)".*?"type":"applicationx-mpegURL","value":"(.*?)"'
    
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
           
            sTitle =alfabekodla(aEntry[0])
            sPicture = picpic
            
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl =URL_MAIN + sUrl
           
            
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle',sTitle)
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'sshowBox3', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pageshowDizi', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
 

def __NextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl =sUrl.replace('amp;', "")
    sPattern = 'data-url="(/actions/control/episodes.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_MAIN) + aResult[1][0]+'&skip=10'

    return False             


    return False
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    
    
    urla  = "https://www.kanald.com.tr"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('"SecurePath": "', '"SecurePath":"')      
    Server= re.findall('"SecurePath":"(.*?)"', data)[0]
    sUrl = "https://soledge4.dogannet.tv//%s" %( Server.replace('\u0026', "&").replace('/index.m3u8', "/1000/prog_index.m3u8").replace('/playlist.m3u8', "/track_4_1000/playlist.m3u8"))  
       
   
                                                                               
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()

def akanald():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla ( name) 
    
                                                        
    
    
    
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    maxbitrate=9000000
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLS'                                                                   
    progress.update( 20, "", 'Loading local proxy', "" )
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
def partplay():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
     
    stream = re.findall("type: 'GET'.*?url: '/actions/control/player/(.*?)? ',", data, re.S)
    url = "http://www.netd.com/actions/content/media/" +stream[0]
    urla  = "http://www.netd.com/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer)
    
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


def play__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
   
    sUrl = sUrl+ '|User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)'
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    

    #cConfig().log("Hoster - play " + str(sTitle))
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    #tout repetter
    #xbmc.executebuiltin("xbmc.playercontrol(RepeatAll)")
    
    oPlayer.startPlayer()
    


def sshowBox3():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    oInputParameterHandler = cInputParameterHandler()
    sUrl ='http://www.netd.com'+ oInputParameterHandler.getValue('siteUrl')
    sUrltit = oInputParameterHandler.getValue('sMovieTitle')
    ua='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'                                                                            
    urla= "http://www.netd.com/"
    referer=[('Referer',sUrl)]
             
       


    Server=gegetUrl(sUrl,headers=referer)          
    Server=Server.replace('/u002F', "")
    aResult= re.findall('"title":"'+sUrltit+'".*?"type":"applicationx-mpegURL","value":"(.*?)"', Server)
    for sTitle,url in aResult:
    
        sHosterUrl='http://media.netd.com.tr/' + url
    

                  

    
        sTitle = alfabekodla(sTitle) 
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  
        return False
def showMessage(heading='TURKvod', message = '', times = 2000, pics = ''):
                try: xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")' % (heading, message, times, pics))
                except Exception, e:
                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )                                           

                        xbmc.log( '[%s]: showMessage: exec failed [%s]' % ('', e), 1 )        