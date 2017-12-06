#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
thisPlugin = int(sys.argv[1])
from resources.lib import util
import re
import json

SITE_IDENTIFIER = 'youtubecom_tr'
SITE_NAME = 'YouTUBE'
SITE_DESC = 'Replay TV'
             
YUPA = 'https://www.youtube.com'
URL_MAIN = 'http://www.youtube.com/embed/'
URL_PIC = 'http://s.dogannet.tv/'
URL_LIVE = 'https://www.youtube.com/watch?v='
MOVIE_MOVIE = ('http://', 'showAlpha')
MOVIE_GENRES = (True, 'showGenre')

SERIE_SERIES = ('http://www.full-film.org/series/alphabet/', 'AlphaSearch')
SERIE_NEWS = ('http://www.full-film.org/series/page-1', 'showMovies')
 
ANIM_ANIMS = ('http://www.full-film.org/animes/alphabet/', 'AlphaSearch')
ANIM_NEWS = ('http://www.full-film.org/animes/page-1', 'showMovies')

URL_SEARCH = ('', 'showMovies')
zahl = 0;

               
   
def YOUTUBEPKIR(url):
    ref='https://www.google.de/' 
    headers = {'Cookie': 'SID=JwVgty01JtsPXzHE7EbqR8etvUZG9GLTFHfv0NH8bxHHatu7jI_939YtdwPbnHLsWCxe-g.;','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer':ref ,  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
    url = requests.get(url, headers = headers).text
    url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
    url = url.encode( "utf-8")
    url = urllib.unquote_plus(url) 
    url = url.replace('�','')
    return url
  

def load():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv/') 
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'genres.png', oOutputParameterHandler) 
    
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
    
def YouTUBE():
    oGui = cGui()
    tarzlistesi = []
    tarzlistesi.append(("Search", "https://www.youtube.com/results?search_query="))
    tarzlistesi.append(("TÚRK Sinema Musik Video", "https://www.youtube.com/results?search_query=adana+kebab+nas%C4%B1l+yap%C4%B1l%C4%B1r"))
    tarzlistesi.append(("German Cinema Musik Video", "https://www.youtube.com/results?search_query=maceraci"))
    tarzlistesi.append(("Arabic Sinema Musik Video", "https://www.youtube.com/results?search_query=maceraci"))                                     
    tarzlistesi.append(("bollywood movies full movies", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+pop")) 
    
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TÚRK Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeturk', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Arabic Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubearabic', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'German Cinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeargermany', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
    
def KARAOKEturk():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []     
    tarzlistesi.append(("karaoke tÚrkce pop",  "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+pop"))
    tarzlistesi.append(("karaoke tÚrkce sarkilar",  "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+sarkilar"))
    tarzlistesi.append(("karaoke tÚrkce tÚrkÚler", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+t%C3%BCrk%C3%BCler"))
    tarzlistesi.append(("karaoke tÚrkce arabesk", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+arabesk"))                                     
    tarzlistesi.append(("karaoke tÚrkce slow", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+slow")) 
    tarzlistesi.append(("karaoke tÚrkce damar", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+damar"))
    tarzlistesi.append(("karaoke tÚrkce ibrahim tatlises", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+ibrahim+tatlises"))
    tarzlistesi.append(("karaoke tÚrkce emrah", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+emrah"))
    tarzlistesi.append(("karaoke tÚrk�e m�sl�m", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrk%C3%A7e+m%C3%BCsl%C3%BCm+"))
    tarzlistesi.append(("karaoke tÚrk�e tarkan", "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrk%C3%A7e+tarkan"))
    tarzlistesi.append(("tÚrkce karaoke ferdi tayfur",  "https://www.youtube.com/results?search_query=t%C3%BCrk%C3%A7e+karaoke+ferdi+tayfur+"))
    tarzlistesi.append(("tÚrkce karaoke yildiz tilbe",  "https://www.youtube.com/results?search_query=t%C3%BCrk%C3%A7e+karaoke+y%C4%B1ld%C4%B1z+tilbe+"))

    tarzlistesi.append(("tÚrkce karaoke baris manco", "https://www.youtube.com/results?search_query=t%C3%BCrk%C3%A7e+karaoke+bar%C4%B1%C5%9F+man%C3%A7o"))
    tarzlistesi.append(("tÚrkce karaoke ahmet kaya", "https://www.youtube.com/results?search_query=t%C3%BCrk%C3%A7e+karaoke+ahmet+kaya+"))
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def yotubeturk():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/watch?v=zCldjArW0as&list=RDzCldjArW0as#t=44') 
    oGui.addDir(SITE_IDENTIFIER, 'YYOUTUBEplaylist', 'Oyun Havalari Album Mix', 'genres.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/user/askmuzikproduksiyon/videos?disable_polymer=1') 
    oGui.addDir(SITE_IDENTIFIER, 'playlistYOUTUBE', 'Oyun Havalari Mix', 'genres.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/user/akustikligunler/videos?disable_polymer=1') 
    oGui.addDir(SITE_IDENTIFIER, 'playlistYOUTUBE', 'Oyun Havalari Pavyon Mix', 'genres.png', oOutputParameterHandler) 
 
    tarzlistesi.append(("TÚRKCE KARAOKE",  "https://www.youtube.com/results?search_query=karaoke+t%C3%BCrkce+pop"))
    
    tarzlistesi.append(("ATATÚRK VE CANAKKALE",  "https://www.youtube.com/results?search_query=ATAT%C3%9CRK+VE+CANAKKALE"))
    tarzlistesi.append(("Adana Kebab Nasil Yapilir", "https://www.youtube.com/results?search_query=adana+kebab+nas%C4%B1l+yap%C4%B1l%C4%B1r"))
    tarzlistesi.append(("Maceraci", "https://www.youtube.com/results?search_query=maceraci"))                                     
    tarzlistesi.append(("kemanci mizrap", "https://www.youtube.com/results?search_query=kemanci+mizrap")) 
    tarzlistesi.append(("kemanci ismail", "https://www.youtube.com/results?search_query=kemanci+ismail"))
    tarzlistesi.append(("kemanci h�seyin", "https://www.youtube.com/results?search_query=kemanci+ismail"))
    tarzlistesi.append(("kemanci ferit", "https://www.youtube.com/results?search_query=kemanci+ferit"))
    tarzlistesi.append(("oyun havalari", "https://www.youtube.com/results?search_query=kemanci+ismail"))
    tarzlistesi.append(("ciftetelli oyun havasi", "https://www.youtube.com/results?search_query=ciftetelli+oyun+havasi"))
    tarzlistesi.append(("turk filmleri hd",  "https://www.youtube.com/results?search_query=turk+filmleri+hd"))
    tarzlistesi.append(("turk komedi filmleri tek parca",  "https://www.youtube.com/results?search_query=turk+komedi+filmleri+tek+parca"))

    tarzlistesi.append(("cÚneyt arkin filmleri full", "https://www.youtube.com/results?search_query=c%C3%BCneyt+arkin+filmleri+full"))
    tarzlistesi.append(("kemal sunal filmleri hd", "https://www.youtube.com/results?search_query=kemal+sunal+filmleri+hd+full+izle"))
    tarzlistesi.append(("yilmaz gÚney filmleri full", "https://www.youtube.com/results?search_query=yilmaz+g%C3%BCney+filmleri+full"))
    tarzlistesi.append(("sadri alisik filmleri full", "https://www.youtube.com/results?search_query=sadri+alisik+filmleri+full"))
    tarzlistesi.append(("tÚrkan soray filmleri full", "https://www.youtube.com/results?search_query=t%C3%BCrkan+soray+filmleri+full"))
    tarzlistesi.append(("fatma girik film full", "https://www.youtube.com/results?search_query=fatma+girik+film+full"))
    tarzlistesi.append(("Technology", "https://www.youtube.com/results?search_query=Technology"))
    tarzlistesi.append(("turk savas teknolojisi", "https://www.youtube.com/results?search_query=turk+savas+teknolojisi"))
    
                  
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'TÚRKCE KARAOKE':
             oGui.addDir(SITE_IDENTIFIER, 'KARAOKEturk', sTitle, 'genres.png', oOutputParameterHandler)
        else:     
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def playnext(url):
        oRequestHandler = cRequestHandler(url)
        sHtml = oRequestHandler.request()
        try:
            #note doit etre '{'sHtmlcontent'}'  | 18 premier '{'
            player_conf = sHtml[18 + sHtml.find("ytplayer.config = "):sHtml.find(";ytplayer.load =")]
            bracket_count = 0
            for i, char in enumerate(player_conf):
                if char == "{":
                    bracket_count += 1
                elif char == "}":
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
            else:
                util.VSlog("Cannot get JSON from HTML")

            index = i + 1
            data = json.loads(player_conf[:index])

        except Exception as e:
            util.VSlog("Cannot decode JSON: {0}"+str(e))


        stream_map = parse_stream_map(data["args"]["url_encoded_fmt_stream_map"])

        if not (stream_map == False):
            video_urls = zip(stream_map["url"],stream_map["quality"])          
            for url,name in video_urls:
                return url

def Genreparca():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    oRequestHandler = cRequestHandler(urll)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace("amp;",'').replace("\u0130",'I')          
    link=re.findall('<div class="playlist-behavior-controls">.*?<a  href=".*?".*?<a  href="(.*?)"',sHtmlContent)[0]
    urll='https://www.youtube.com'+ link 
        
    
    
    name ='index=1'
    sUrl =playnext(urll.replace("index=1",'index=1'))
    sUrl1 =playnext(urll.replace("index=1",'index=2'))
    sUrl2 =playnext(urll.replace("index=2",'index=3'))
    sUrl3 =playnext(urll.replace("index=3",'index=4'))
    sUrl4 =playnext(urll.replace("index=4",'index=5'))
    sUrl5 =playnext(urll.replace("index=5",'index=6'))
    sUrl6 =playnext(urll.replace("index=6",'index=7'))
    sUrl7 =playnext(urll.replace("index=7",'index=8'))
    
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
    
    
        
def player_type():
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


def yotubeargermany():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []
    tarzlistesi.append(("til schweiger filme in voller l�nge", "https://www.youtube.com/results?search_query=til+schweiger+filme+in+voller+l%C3%A4nge+"))

    tarzlistesi.append(("zeichentrickfilme deutsch ganzer film", "https://www.youtube.com/results?search_query=zeichentrickfilme+deutsch+ganzer+film"))
    tarzlistesi.append(("deutsche filme in voller l�nge kom�die", "https://www.youtube.com/results?search_query=alte+deutsche+filme+in+voller+l%C3%A4nge+kom%C3%B6die"))                                     
    tarzlistesi.append(("deutsche filme ufa", "https://www.youtube.com/results?search_query=alte+deutsche+filme+ufa")) 
    tarzlistesi.append(("deutsche filme 1940", "https://www.youtube.com/results?search_query=alte+deutsche+filme+1940"))
    tarzlistesi.append(("deutsche filme 1950", "https://www.youtube.com/results?search_query=alte+deutsche+filme+1950"))
    tarzlistesi.append(("deutsche filme 1960", "https://www.youtube.com/results?search_query=alte+deutsche+filme+1960"))
    tarzlistesi.append(("deutsche filme 1970", "https://www.youtube.com/results?search_query=alte+deutsche+filme+1970"))
    tarzlistesi.append(("deutsche filme 1980", "https://www.youtube.com/results?search_query=alte+deutsche+filme+1980"))

    tarzlistesi.append(("romy schneider filme in voller l�nge",  "https://www.youtube.com/results?search_query=romy+schneider+filme+in+voller+l%C3%A4nge"))
        
               
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
                  
def yotubearabic():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []
     
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/watch?v=YfH6U8CNp58&index=6&list=PLr3kP-8J1gQNAnUyb2b6d5YecHM7t6fqF') 
    oGui.addDir(SITE_IDENTIFIER, 'YOUTUBEplaylist', 'Arabic Live Channels', 'genres.png', oOutputParameterHandler) 

    tarzlistesi.append(("Arabic musik 2016", "https://www.youtube.com/results?search_query=arabische+musik+2016"))
    tarzlistesi.append(("Arabic music instrumental", "https://www.youtube.com/results?search_query=arabic+music+instrumental"))                                     
    tarzlistesi.append(("arabic music instrumental belly dance", "https://www.youtube.com/results?search_query=arabic+music+instrumental+belly+dance")) 
    tarzlistesi.append(("arabic film 2016", "https://www.youtube.com/results?search_query=arabic+film+2016"))
    tarzlistesi.append(("arabic film hd", "https://www.youtube.com/results?search_query=arabic+film+hd"))
    tarzlistesi.append(("arabic film comedy", "https://www.youtube.com/results?search_query=arabic+film+comedy"))
    tarzlistesi.append(("arabic film ???? ??? ???????/ ?????? ???+??", "https://www.youtube.com/results?search_query=arabic+film+%D9%81%D9%8A%D9%84%D9%85+%D9%83%D8%B4%D9%81+%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D9%88%D8%B1%2F+%D9%84%D9%84%D9%83%D8%A8%D8%A7%D8%B1+%D9%81%D9%82%D8%B7%2B%D9%A1%D9%A8"))
    tarzlistesi.append(("arabic wedding", "https://www.youtube.com/results?search_query=arabic+wedding"))

    tarzlistesi.append(("cartoon arabic", "https://www.youtube.com/results?search_query=cartoon+arabic"))
    tarzlistesi.append(("cartoon arabic full movie",  "https://www.youtube.com/results?search_query=cartoon+arabic+full+movie"))
    tarzlistesi.append(("tiny toon arabic", "https://www.youtube.com/results?search_query=inanilmaz+karaoke"))
    tarzlistesi.append(("arabic tvshow",  "https://www.youtube.com/results?search_query=arabic+tvshow"))
    
               
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()
def RLmmdecodeURL():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                              
#    url =otvkodla(img_url)
  
    referer=[('Referer',sUrl)]
                                
    data=gegetUrl(sUrl,headers=referer)                                            
    url= data.replace("amp;",'').replace("\\n",'').replace("\u003c",'<').replace("\u003e",'>').replace("\\",'')
                                                
    name ='test'                                               
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
def playlistYOUTUBE(sSearch = ''):


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
        sHtmlContent = sHtmlContent.replace('amp;','').replace("\\n",'').replace("\u003c",'<').replace("\u003e",'>').replace("\\",'')

        
                                                                                               
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<li class="channels-content-item yt-shelf-grid-item">.*?<img.*?src="(.*?)".*?href="(.*?)">(.*?)</a><span class="accessible-description" id="description-id-.*?">(.*?)</span></h3>'
    
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
           
            sTitle =aEntry[2]+' : '+ aEntry[3]
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = str(aEntry[1])
            if not 'http' in sUrl:
                sUrl = str(YUPA) + sUrl
           
            sTitle = alfabekodla(sTitle)
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __checkNextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'playlistYOUTUBE', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()
  

 

def __checkNextPage(sHtmlContent):
    sHtmlContent= sHtmlContent.replace('amp;','')
        
    sPattern = 'data-uix-load-more-href="(.*?)">'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(YUPA)+ aResult[1][0].replace(' ','+')
    return False       
def YYOUTUBEplaylist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                              
#    url =otvkodla(img_url)
  
    referer=[('Referer',sUrl)]
                              
    data=gegetUrl(sUrl,headers=referer)                                            
    
    
    title= re.findall('data-video-title="(.*?)".*?data-thumbnail-url="(.*?)".*?data-video-id="(.*?)"',data, re.S)
    for Title ,sPicture,sUrl in title:
               
                          sPicture = alfabekodla(sPicture)
                        
                          if not 'http' in sPicture:
                              sPicture = 'http:' + sPicture
                                    
                          Title = alfabekodla(Title)
                          
                           
                          sUrl = URL_LIVE+ sUrl
                          oOutputParameterHandler = cOutputParameterHandler()
                          oOutputParameterHandler.addParameter('siteUrl', sUrl)
                          oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
                          oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', Title, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()          
def YOUTUBEplaylist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                              
#    url =otvkodla(img_url)
  
    referer=[('Referer',sUrl)]
                              
    data=gegetUrl(sUrl,headers=referer)                                            
    
    
    title= re.findall('data-video-title="(.*?)".*?data-thumbnail-url="(.*?)".*?data-video-id="(.*?)"',data, re.S)
    for Title ,sPicture,sUrl in title:
               
                          sPicture = alfabekodla(sPicture)
                          Title = alfabekodla(Title)
                          
                           
                          sUrl = URL_LIVE+ sUrl
                          oOutputParameterHandler = cOutputParameterHandler()
                          oOutputParameterHandler.addParameter('siteUrl', sUrl)
                          oOutputParameterHandler.addParameter('sMovieTitle', str(Title))
                          oGui.addMovie(SITE_IDENTIFIER, 'youtubeplayer2', Title, sPicture, sPicture, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()         
def Playable(url):
        oRequestHandler = cRequestHandler(url)
        sHtml = oRequestHandler.request()
        try:
            #note doit etre '{'sHtmlcontent'}'  | 18 premier '{'
            player_conf = sHtml[18 + sHtml.find("ytplayer.config = "):sHtml.find(";ytplayer.load =")]
            bracket_count = 0
            for i, char in enumerate(player_conf):
                if char == "{":
                    bracket_count += 1
                elif char == "}":
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
            else:
                util.VSlog("Cannot get JSON from HTML")

            index = i + 1
            data = json.loads(player_conf[:index])

        except Exception as e:
            util.VSlog("Cannot decode JSON: {0}"+str(e))


        stream_map = parse_stream_map(data["args"]["url_encoded_fmt_stream_map"])
        if not (stream_map == False):
            video_urls = zip(stream_map["url"],stream_map["quality"])          
            return video_urls

def YOUTUBEplay():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sUrl =Playable(url)
    for url,name in sUrl:    
          
        
    
        addLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url,'')

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok

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
            oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
 
            if '&list=' in aEntry[0]:
                oGui.addTV(SITE_IDENTIFIER, 'YOUTUBEplaylist', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
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
    sMovieTitle = alfabekodla(sMovieTitle)
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = sMovieTitle
        
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
def partplay__():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    pageUrl = oInputParameterHandler.getValue('siteUrl')

    import requests
    import re
    import json
   
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0 Iceweasel/42.0'}
    r1 = requests.get(pageUrl, headers = headers)
    source = r1.text
    continuex = re.findall('data-uix-load-more-href="(.*?)"', source)[0]
    
    r = requests.get(continuex, headers = headers)
    source = r.text
    jdata = json.loads(source)
    source = jdata["load_more_widget_html"]
    page = jdata["content_html"]
    return page
    
    

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


def youtubeplayer2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
                      
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    if not '"hlsvp":"' in data:
            sMovieTitle = alfabekodla(sMovieTitle)
            sThumbnail = alfabekodla(sThumbnail)
            Url = alfabekodla(Url)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url )
            oOutputParameterHandler.addParameter('sMovieTitle', str(sMovieTitle))
            oGui.addMovie(SITE_IDENTIFIER, 'tv8canli', sMovieTitle, sThumbnail, sThumbnail, '', oOutputParameterHandler)

    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    liste= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=(.*?),CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)
    for sTitle,sUrl2 in liste:
        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
        sUrl2= sUrl2+ '|' + Header          
        sTitle='-Quality-'+sTitle
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle',sMovieTitle+sTitle)
        if sTitle == '-Quality-1280x720':
             oGui.addDir(SITE_IDENTIFIER, 'youtube1280',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-854x480':
             oGui.addDir(SITE_IDENTIFIER, 'youtube854',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-640x360':
             oGui.addDir(SITE_IDENTIFIER, 'youtube640',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-426x240':
             oGui.addDir(SITE_IDENTIFIER, 'youtube426',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-1920x1080':
             oGui.addDir(SITE_IDENTIFIER, 'youtube1920',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'youtube426',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
                   
                   
    oGui.setEndOfDirectory()
def youtubeplayer():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    url1 = '^\n                 (\n                     (?:https?://)?                                       # http(s):// (optional)\n                     (?:youtu\\.be/|(?:\\w+\\.)?youtube(?:-nocookie)?\\.com/|\n                        tube\\.majestyc\\.net/)                             # the various hostnames, with wildcard subdomains\n                     (?:.*?\\#/)?                                          # handle anchor (#/) redirect urls\n                     (?!view_play_list|my_playlists|artist|playlist)      # ignore playlist URLs\n                     (?:                                                  # the various things that can precede the ID:\n                         (?:(?:v|embed|e)/)                               # v/ or embed/ or e/\n                         |(?:                                             # or the v= param in all its forms\n                             (?:watch(?:_popup)?(?:\\.php)?)?              # preceding watch(_popup|.php) or nothing (like /?v=xxxx)\n                             (?:\\?|\\#!?)                                  # the params delimiter ? or # or #!\n                             (?:.*?&)?                                    # any other preceding param (like /?s=tuff&v=xxxx)\n                             v=\n                         )\n                     )?                                                   # optional -> youtube.com/xxxx is OK\n                 )?                                                       # all until now is optional -> you can pass the naked ID\n                 ([0-9A-Za-z_-]+)                                         # here is it! the YouTube video ID\n                 (?(1).+)?                                                # if we found the ID, everything can follow\n                 $'
    kubi = re.match(url1, url, re.VERBOSE)
    dhVideoId=  kubi.group(2)
    
    Url ='https://www.youtube.com/watch?v=%s&feature=youtu.be' % dhVideoId  
                  
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    liste= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=(.*?),CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)
    for sTitle,sUrl2 in liste:
        Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
        sUrl2= sUrl2+ '|' + Header          
        sTitle='-Quality-'+sTitle
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', Url)
        oOutputParameterHandler.addParameter('sMovieTitle',sMovieTitle+sTitle)
        if sTitle == '-Quality-1280x720':
             oGui.addDir(SITE_IDENTIFIER, 'youtube1280',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-854x480':
             oGui.addDir(SITE_IDENTIFIER, 'youtube854',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-640x360':
             oGui.addDir(SITE_IDENTIFIER, 'youtube640',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-426x240':
             oGui.addDir(SITE_IDENTIFIER, 'youtube426',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '-Quality-1920x1080':
             oGui.addDir(SITE_IDENTIFIER, 'youtube1920',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'youtube426',sMovieTitle+ sTitle, 'genres.png', oOutputParameterHandler)
                   
                   
    oGui.setEndOfDirectory()
def youtube426():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    url= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=426x240,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
    

    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= url+ '|' + Header 
    
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



def youtube640():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    url= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=640x360,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
    

    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= url+ '|' + Header 
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


def youtube854():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    url= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=854x480,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
    

    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= url+ '|' + Header 
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



def youtube1920():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    url= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=1920x1080,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= url+ '|' + Header 
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
def youtube1280():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    name = alfabekodla(name)
    referer=[('Referer',Url)]
    data=gegetUrl(Url,headers=referer) 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    urll = re.findall('"hlsvp":"(.*?)"', data, re.S)[0]                                       
    urll= urll.replace("\/","/")
    referer=[('Referer',urll)]
    data=gegetUrl(urll,headers=referer) 
    url= re.findall('#EXT-X-STREAM-INF:BANDWIDTH=.*?,CODECS=".*?",RESOLUTION=1280x720,CLOSED-CAPTIONS=NONE\n(.*?)\n',data, re.S)[0] 
    
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Mobile Safari/537.36'
    url= url+ '|' + Header 
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
     
def parse_stream_map(sHtml):
    if 'signature' in sHtml:
        videoinfo = {"itag": [],
                     "url": [],
                     "quality": [],
                     "fallback_host": [],
                     "s": [],
                     "type": [] }

        # Split individual videos
        videos = sHtml.split(",")
        # Unquote the characters and split to parameters
        videos = [video.split("&") for video in videos]
        for video in videos:
            for kv in video:
                key, value = kv.split("=")
                videoinfo.get(key, []).append(util.Unquote(value))

        return videoinfo
        
    else:
        return False
       