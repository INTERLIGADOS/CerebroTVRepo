#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *    
from liveonlinetv247 import adultHosters                  

SITE_IDENTIFIER = 'adult_eu'
SITE_NAME = 'ADULT'
ADULT_ADULT = (True, 'pincode')
phAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
hos = int(sys.argv[1]) 

def pincode():
    oGui = cGui()
    pincode = oGui.pinKeyBoard()
    if ADULT_PIN in pincode:  
            showGenre()

class track():
    def __init__(self,page,data=''):
        self.page=page
        self.page =0
        self.page += 1
        self.data=data

def get_HTML(url, post = None, ref = None):
    html = ''

    if ref == None:
        ref = 'http://'+urlparse(url).hostname

    request = urllib2.Request(urllib.unquote(url), post)

    request.add_header('User-Agent', 'Mozilla/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)')
    request.add_header('Host', (url))
    request.add_header('Accept', '*/*')
    request.add_header('Accept-Language', 'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4')
    request.add_header('Referer', ref)
    #request.add_header('Cookie', 'MG_6532=1')

    ret = 502
    idx = 5

    while ret == 502 and idx > 0:
        try:
            f = urllib2.urlopen(request)
            ret = 0
        except IOError, e:
            if hasattr(e, 'reason'):
                xbmc.log('We failed to reach a server. Reason: '+ str(e.reason))
            elif hasattr(e, 'code'):
                xbmc.log('The server couldn\'t fulfill the request. Error code: '+ str(e.code))
                ret = e.code

        if ret == 502:
            time.sleep(1)
        idx = idx -1

    if ret == 0:
        html = f.read()
        f.close()

    return html
def getPage(url, cookieJar=None,post=None, timeout=20, headers=None):

    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    if headers:
        for h,hv in headers:
            req.add_header(h,hv)

    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;


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
    tarzlistesi= []
    tarzlistesi.append(("LiveTV", "http://www.hdporn.net/channels/"))
    tarzlistesi.append(("LiveTV2", "http://www.hdporn.net/channels/"))
    tarzlistesi.append(("DBRAZZERS videos", "http://ero-tv.org/uppod/pl/playlist_video69-897.txt"))
    tarzlistesi.append(("HDPorn", "http://www.hdporn.net/channels/"))
    tarzlistesi.append(("RedTube", "http://www.redtube.com/categories"))
    tarzlistesi.append(("PornHD", "http://www.pornhd.com/category"))
    tarzlistesi.append(("PornHub", "http://www.pornhub.com/categories"))
    tarzlistesi.append(("Eporner", "https://www.eporner.com/categories/"))
    
    for sTitle,sUrl2 in tarzlistesi:              
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'HDPorn':
             oGui.addDir(SITE_IDENTIFIER, 'hdpornGenre',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'RedTube':
             oGui.addDir(SITE_IDENTIFIER, 'redtubeGenre', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'PornHD':
             oGui.addDir(SITE_IDENTIFIER, 'pornhdGenre', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'PornHub':
             oGui.addDir(SITE_IDENTIFIER, 'pornhubGenre', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'LiveTV':
             oGui.addDir(SITE_IDENTIFIER, 'LiveTV', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'LiveTV2':
             oGui.addDir(SITE_IDENTIFIER, 'adultHosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DBRAZZERS videos':
             oGui.addDir(SITE_IDENTIFIER, 'GetPlayList', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'epornhubGenre',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
        
def LiveTV():
    oGui = cGui()
   

        #oInputParameterHandler = cInputParameterHandler()
        #sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl ='http://oklivetv.com/genre/adult-18/?orderby=likes'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    url = requests.get(sUrl, headers = headers).text
#    url = unicode(url, 'latin-1')#converti en unicode
    url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
    url = url.encode( "utf-8")
    url = urllib.unquote_plus(url) 
    url = url.replace('�','')
 
       
    sPattern = '<div class="thumb">.*?<a class="clip-link" data-id=".*?" title="(.*?)" href="(.*?)">.*?<img src="(.*?)"'
     
   
                                                                                
    #fh = open('c:\\test.txt', "w")
    #fh.write(sHtmlContent)
    #fh.close()
    
    oParser = cParser()
    aResult = oParser.parse(url, sPattern)
   
    #print aResult
   
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
           
           
            sPicture = str(aEntry[2])
                            
            sUrl = str(aEntry[1])
            
            
            sTitle = alfabekodla(str(aEntry[0]))         
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'play__LiveTV', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
    oGui.setEndOfDirectory()
                                                                                        
     
    
def play__LiveTV():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    sTitle = alfabekodla(sTitle)                            
    dat= requests.get(Url).content
                           
    url = re.findall("<iframe style='width:100%;height:100%;background-color: #1A1A1A;' scrolling='no' frameborder='0' src='(.*?)'",dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Referer': referer  }
    data= requests.get(url, headers = headers).text
  
    ken = re.findall('<script>.*?<iframe .*?src="(.*?)"',data, re.S)[0]                         
    dataken= requests.get(ken, headers = headers).text
    sHosterUrl = re.findall('<source src="(.*?)"', dataken, re.S)[0]
    TIK='|Referer='+url+'&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Mobile Safari/537.36'
    sHosterUrl = sHosterUrl+TIK
    sPicture ="https://tvshqip.tv/tv/wp-content/uploads/2016/05/logo.png"
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()      
  

def GetPlayList():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    pos = oInputParameterHandler.getValue('sMovieTitle')
    img = oInputParameterHandler.getValue('sThumbnail')
    resp = net.http_GET(url)
    data = resp.content 
 
    s_url = ''
    s_num = 0
    for rec in re.compile('{(.+?)}', re.MULTILINE|re.DOTALL).findall(data.replace('{"playlist":[', '')):
        for par in rec.replace('"','').split(','):
            if par.split(':')[0]== 'comment':
                sTitle =' Video'+  str(s_num+1) #par.split(':')[1]+' '
            if par.split(':')[0]== 'file':
                if 'http' in par.split(':')[1]:
                    s_url = par.split(':')[1]+':'+par.split(':')[2]
               
        s_num += 1

        if s_num >= pos :
                    sPicture='http://ero-tv.org/wp-content/uploads/2014/08/brazzers.gif'
                    sTitle = alfabekodla(sTitle)
                    liste = []
                    liste.append( [sTitle,s_url] )
                    oOutputParameterHandler = cOutputParameterHandler()
                    oOutputParameterHandler.addParameter('siteUrl', str(s_url))
                    oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                    oOutputParameterHandler.addParameter('liste', str(liste))
                    oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
                    oGui.addMovie(SITE_IDENTIFIER, 'otvplay__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()
def otvplay__():
    global session
    oInputParameterHandler = cInputParameterHandler()
    idx = oInputParameterHandler.getValue('liste').getSelectedIndex()
    playlist = oInputParameterHandler.getValue('liste')
    session.open(NunaPlayer ,playlist,int(idx), True, None)
        
  
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

def dizizleABC():
    oGui = cGui()
  
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(sTitle)       
        
  
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            

def addLink(name,url,iconimage):
       
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        


def otvplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle)
    sHosterUrl = sUrl
    



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 

def pornhdGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                        	
    
    if re.match('.*?<li class="category">', data, re.S):    
      data = data.replace("\n",'')
      tarzlistesi = re.findall('<li class="category">.*?<a href="(.*?)">.*?data-original="(.*?)".*?</span>(.*?)</a>', data , re.S)
      for sUrl,sPicture,sTitle in tarzlistesi:
        Url ='http://www.pornhd.com'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhdliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def pornhdliste():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
       
    resp = net.http_GET(url)
    sHtmlContent = resp.content
    
    tarzlistesi = re.findall('data-video=".*?" ><a class="thumb" href="(.*?)"><img alt="(.*?)".*?data-original="(.*?)"', sHtmlContent , re.S)
    for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='https://www.pornhd.com'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhdHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
  
def pornhdNextPage(sHtmlContent,sUrl):
    oGui = cGui()
    

                                 
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<li class="next ">.*?<span class="icon jsFilter js-link" data-query-key="page" data-query-value="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl)+'?page='+ aResult[1][0]
    return False


def hdpornGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                        	
    
    if re.match('.*?<div id="main">', data, re.S):    
      data = data.replace("\n",'')
      tarzlistesi = re.findall('<div class="content">.*?<a href="(.*?)" title="(.*?)".*?src="(.*?)"', data , re.S)
      for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='http://hdporn.net'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'hdpornliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  



def hdpornliste():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
       
    resp = net.http_GET(url)
    sHtmlContent = resp.content
    tarzlistesi = re.findall('<div class="content col-xs-12 col-sm-4 col-md-3">.*?<a  href=".*?" title="(.*?)" target="_self">.*?src="(.*?)".*?this.src="(.*?)-.*?.jpg"', sHtmlContent , re.S)
    for sTitle,sPicture,sUrl in tarzlistesi:
        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
        sTitle = alfabekodla(sTitle)
        Url = sUrl.replace('thumbs','videos')+ '|' + Header 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) 
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  

def hdpornNextPage(sHtmlContent,url):
    oGui = cGui()
    

    
      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '<div id="pagination">.*?<span>.*?</span><a href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl)+ aResult[1][0]
    return False


def redtubeGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
                                                                                 
    resp = net.http_GET(url)                       
    sHtmlContent = resp.content
    sHtmlContent = sHtmlContent.replace("\n",'').replace("//cdne",'http://cdne')
    tarzlistesi = re.findall('<div class="video">.*?<a href="(.*?)" title="(.*?)">.*?data-src="(.*?)"', sHtmlContent , re.S)
    for sUrl,sTitle ,sPicture in tarzlistesi:
        Url ='http://www.redtube.com'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'redtubeliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()    
     
def redtubeliste(sSearch = ''):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                        	
    data = data.replace("\n",'')
      
                               
    tarzlistesi = re.findall('<img title="(.*?)".*?id="(.*?)".*?data-src="(.*?)"', data , re.S)
    for sTitle,sUrl,sPicture in tarzlistesi:
        Url ='http://www.redtube.com/'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        
        oGui.addMovie(SITE_IDENTIFIER, 'redtubeHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()  
def redtubeNextPage(sHtmlContent,sUrl):
    oGui = cGui()
    
    
    
    kUrl ='http://www.redtube.com'  
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = 'id="currentPageNum"><b>.*?</b></a>.*?<a href="(.*?)" title=".*?" onclick="trackByCookie.*?'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(kUrl)+ aResult[1][0]
    return False



def pornhubGenre():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                       	

						
							               
    tarzlistesi = re.findall('<div class="category-wrapper">.*?<a href="(.*?)" alt=".*?" class="js-mxp" data-mxptype="Category" data-mxptext="(.*?)">.*?<img src="(.*?)"', data , re.S)
    for sUrl,sTitle,sPicture in tarzlistesi:
        Url ='https://de.pornhub.com'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'pornhubliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def pornhubliste(sSearch = ''):
   
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
        sUrl= oInputParameterHandler.getValue('siteUrl')
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()  
        
   

                                            
                                          
                                             
			                                                                                                     	
                                            
                               
        sPattern = '<div class="phimage">.*?<a href="(.*?)" title="(.*?)".*?data-mediumthumb="(.*?)"'
                                         
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
           
            sTitle = alfabekodla(aEntry[1]) 
           
            sPicture = aEntry[2]
                
            Url ='http://www.pornhub.com'+ aEntry[0]+'&utm_source=twitter&utm_medium=social'
            
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'pornhubHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
          
            sNextPage = pornhubNextPage(sHtmlContent,sUrl)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pornhubliste', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                              #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
def pornhubNextPage(sHtmlContent,sUrl):
    oGui = cGui()
                 
   
    sHtmlContent =sHtmlContent.replace('amp;','')
    kUrl ='http://www.pornhub.com'                                      
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = ' <li class="page_current"><span class="greyButton">.*?<li class="page_number"><a class="greyButton" href="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(kUrl)+ aResult[1][0]
    return False                 
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


def mpornhdHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('Thumbnail')
    
    resp = net.http_GET(url)
    sHtmlContent = resp.content
    sHtmlContent = sHtmlContent.replace('\/','/')
    sTitle = cUtil().DecoTitle(sTitle)       
    sPattern = '"720p":"(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
          
    if (aResult[0] == True):
        
        
            
        sUrl= '' + aResult[1][0]
           
        

        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sUrl)
        oGuiElement.setThumbnail(sThumbnail)

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()
        return
        
    oGui.setEndOfDirectory()    
def play__():
   

    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    name=  alfabekodla(sTitle)
      
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

def play2():
    

    oInputParameterHandler = cInputParameterHandler()
    rest = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    sHosterUrl= rest + '|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36' + Header    

    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
    
def redtubeHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
        
    resp = net.http_GET(url)
    sHtmlContent = resp.content
    sHtmlContent = sHtmlContent.replace('\/','/')
    tarzlistesi = re.findall('"quality":"(.*?)","videoUrl":"(.*?)"', sHtmlContent , re.S)
    for sTitle,Url in tarzlistesi:
        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    
        MAIN = 'http:'
        Url = str(Url)
        if not 'http' in Url:
                Url = str(MAIN) + Url + '|' + Header 
        sPicture  = "http://cdne-st.redtubefiles.com/images/logos/logo_RT_premium.png?v=5d9a2e0cf0b93d9f391d915e19214fe37f64c3501481841392"
        sTitle =  alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'play__', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory() 
def mmmredtubeHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
  
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                        	
    data = data.replace('\/','/')
      
                               
    tarzlistesi = re.findall('sources: ."480":"(.*?)".*?videoTitle: "(.*?)"', data , re.S)
    # 1 seul resultat et sur leur propre hebergeur
    for sUrl,sTitle in tarzlistesi:
        
       
            
    
    
        Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
        sTitle =  alfabekodla(sTitle)
        sHosterUrl = sHosterUrl + '|' + Header  
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
     
        
 
def pornhdHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle = cUtil().DecoTitle(sTitle)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/','/')
    oParser = cParser()
      
    sPattern =  '"720p":"(http.*?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
     
    # 1 seul resultat et sur leur propre hebergeur
    if (aResult[0] == True):
        
        
            
        sUrl= '' + aResult[1][0]
    
    
       
        sTitle =  alfabekodla(sTitle)
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sUrl)
        

        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer()  
        return False
        
        
    oGui.setEndOfDirectory()
    
def GetRealUrl(url):
    oParser = cParser()
    sPattern = '\[REGEX\](.+?)\[URL\](.+$)'
    aResult = oParser.parse(url, sPattern)
    
    if (aResult):
        reg = aResult[1][0][0]
        url2 = aResult[1][0][1]
        oRequestHandler = cRequestHandler(url2)
        sHtmlContent = oRequestHandler.request()
        
        aResult = oParser.parse(sHtmlContent, reg)
        if (aResult):
            url = aResult[1][0]
            
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
        
    return url
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
    

def epornhubGenre():
    oGui = cGui()
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    data = requests.get(Url).content
                                                                                                         	

						
							              
    tarzlistesi = re.findall('<div class="categoriesbox" id=".*?"> <div class="ctbinner"> <a href="(.*?)" title=".*?"> <img src="(.*?)" alt="(.*?)">', data , re.S)
    for sUrl,sPicture,sTitle in tarzlistesi:
        Url ='http://www.eporner.com'+ sUrl
        sTitle = alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addMovie(SITE_IDENTIFIER, 'epornhubliste', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory() 
def epornhubliste(sSearch = ''):
   
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
        url = oInputParameterHandler.getValue('siteUrl')
        sUrl=url
        resp = net.http_GET(url)
	sHtmlContent = resp.content
        
   

                                            
                                          
                                             
			                                                                                                     	
                                            
                               
        sPattern = 'class="mb.*?>\s*<a\shref="(.*?)"\stitle="(.*?)".*?src="(.*?)"'
                                         
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
           
            sTitle = alfabekodla(aEntry[1]) 
           
            sPicture = aEntry[2]
                
            Url ='http://www.eporner.com'+ aEntry[0]
            
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'epornerHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
           
        if not sSearch:
          
            sNextPage = pornhubNextPage(sHtmlContent,sUrl)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'pornhubliste', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                              #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def epornerHosters():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
   
  
    url = oInputParameterHandler.getValue('siteUrl')
    resp = net.http_GET(url)
    data = resp.content                                                                                                        	
    data = data.replace('\/','/')
      
                              
    tarzlistesi = re.findall('</td> </tr> <tr> <td style="vertical-align:top;"><strong>(.*?)</strong></td> <td> <a href="(.*?)">Download MP4.*?</a> </td>', data , re.S)
    # 1 seul resultat et sur leur propre hebergeur
    for sTitle,sUrl in tarzlistesi:
        
       
            
        Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
        sTitle =  alfabekodla(sTitle)    
        Url ='http://www.eporner.com'+sUrl
        Url = Url + '|' + Header  
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
     
   
def pornhubHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sTitle =  alfabekodla(sTitle)
                              
                          
    urla  = "http://www.pornhub.com/front/set_tablet?redirect=Hyei3SW2wf5odRgmrizzvkMxm72b4XXcjfONUPH7Jcn3KsCJk7y1wQt5ZaNcornt&amp;token=MTQ4OTMzOTMzNJKrf2dyDlkwYSagaiMRp4esP0KsYeXlyyb73Io1SkvMR7Dz3sPjEfSIXbCk3LT2tnsBV9_yK4Ek-kEVTvfo9RI."
    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
                                                            
    import js2py                                                                                                         
    referer=[('Referer',urla)]       
    data=getUrl(Url).result                                                                                         
    data=data.replace('\/','/')
    
    js = re.findall('(var flashvars_(?:\d+).*?)loadScriptUniqueId', data, re.S)    
    urls = str(js2py.eval_js(js[0]))
    if urls.startswith('http'):
	playurl = urls
    else:
        playurl = re.findall('\'(http[s]?://cdn.*?\.mp4.*?)\'', urls, re.S)
        playurl = playurl[-1]                     
    otvhelper.player_agent = phAgent    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', playurl)
    oGui.addDir(SITE_IDENTIFIER, 'play__', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    
from resources.lib import gPlayer    
class NunaPlayer(listPlayer):

	def __init__(self, session, playList, playIdx=0, playAll=True, listTitle=None):
		
                listPlayer.__init__(self, session,  playList, playIdx=playIdx, playAll=playAll, listTitle=listTitle)
                
	def getVideo(self):
		self.nunaName = self.playList[self.playIdx][1]
		stream_url =  self.playList[self.playIdx][0]
                self.playStream(self.nunaName, stream_url)  
                                 
    