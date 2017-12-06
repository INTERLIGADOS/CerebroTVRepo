#-*- coding: utf-8 -*-


from resources.lib.otvhelper import *
 
useragent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'

 
SITE_IDENTIFIER = 'canlitv_mobi'
SITE_NAME = 'CanLiTV_mobi'

 
URL_MAIN = 'http://filmakinesi.org/'


MOVIE_VIEWS = (True, 'showGenre')

class track():
    def __init__(self, length, title, path, icon,data=''):
        self.length = length
        self.title = title
        self.path = path
        self.icon = icon
        self.data = data
 
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
           
def showGenre():                                                                                                                                                                     
    oGui = cGui()                                                                                                                                                             
    liste = []
    liz=xbmcgui.ListItem('CanLiTV+Livecamera',thumbnailImage= "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT4qdute2DJQ-HkP3iOi9Uy8cDS1rVEHjrJyqRI9DxoU--fhaYh",iconImage="DefaultFolder.png")
    uurl="plugin://plugin.video.OTV_MEDIA/?fanart=C%3a%5cUsers%5corhantv%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url=https%3a%2f%2fdl.dropboxusercontent.com%2fs%2fzij10762q4r5pvb%2fipradyotvdelisi.xml.xml"
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)                                                                                
    liste.append( ['CanLiTVlive.co','http://www.canlitvlive.co/tvizle.php?&t=2&pos=r&tv=tv-8'] )
    liste.append( ['CanLiTV','http://www.fox.com.tr/bolum-izle'] )
    liste.append( ['HDTVler','http://www.hdtvler1.net/'] )                 
    
    for sTitle,sUrl2 in liste:
        
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Kolay Tv':
             oGui.addDir(SITE_IDENTIFIER, 'MshowGenre',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'HDTVler':
             oGui.addDir(SITE_IDENTIFIER, 'OCanlshowGenre', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'CanLiTVlive.co':
             oGui.addDir(SITE_IDENTIFIER, 'CanLiTVlive', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ÖZBeCeRiKsIzLeR TV':
             oGui.addDir(SITE_IDENTIFIER, 'MshowGenre', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'CanLiTVshowGenre',  sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()   
def CanLiTVlive(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = 'http://www.canlitvlive.co/tvizle.php?&t=2&pos=r&tv=tv-8'
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    urla  = "netiyi=9bec3b6f4c00317e65a5b4ade8bc8cc4"
                       
    req = urllib2.Request(url)
    req.add_header('User-Agent', useragent)
    response = urllib2.urlopen(req)
    sHtmlContent= response.read()                  
    
                                                  
    
    sPattern = '<span class="sirasi" style="display:none;">(.*?)</span><a href="(.*?)" class="name previi" data-pre="(.*?)">(.*?)</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = str(aEntry[2])
            sTitle = aEntry[0]+ ':' + aEntry[3]
            Link = aEntry[1]
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'atvBox', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 


def OCanlshowGenre(): #affiche les genres

    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    tarzlistesi = []
  
                               
    tarzlistesi.append(("Genel Kanallar", "http://m.canlitv.com/?kat=Genel"))
    tarzlistesi.append(("Haber Kanallari", "http://m.canlitv.com/?kat=Haber"))
    tarzlistesi.append(("Spor Kanallari", "http://m.canlitv.com/?kat=Spor"))
    tarzlistesi.append(("Cocuk Kanallari", "http://m.canlitv.com/?kat=Cocuk"))
    tarzlistesi.append(("Belgesel Kanallari", "http://m.canlitv.com/?kat=Belgesel"))
    tarzlistesi.append(("Dini Kanallar", "http://m.canlitv.com/?kat=Dini"))
    for sTitle,sUrl in tarzlistesi:
       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showradyolist', sTitle, 'genres.png', oOutputParameterHandler)
       
    oGui.setEndOfDirectory()


def showradyolist():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')                  
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    oParser = cParser()
    sPattern = '<div id="kanal_listesi">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
   
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    

    sPattern = '<a href="./(.*?)" title="(.*?)canl.*?">.*?<div class="kanal_resim"><img src="../(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = "http://m.canlitv.com/"+aEntry[2] 
            sTitle =aEntry[1].replace("canl&#305;","").replace("izle","")
            sUrl ="http://m.canlitv.com/"+aEntry[0]
            
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addMovie(SITE_IDENTIFIER, 'atvBox', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)
           
        
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'mcanlitv', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()    

def mcanlitv():
    oGui = cGui()
    urlkk= "http://m.canlitv.com/" 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '<a href="(.*?)" title="(.*?)">.*?<div class="kanal_resim"><img src="(.*?)"'
                                                                  
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
           
            sTitle = aEntry[2]
            sPicture = str(aEntry[1])
            if not 'http' in sPicture:
                sPicture = str(urlkk) + sPicture
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(urlkk) + sUrl
           
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'CanLiTVshowGenre', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        
        sNextPage = __checkForNextPage(sHtmlContent,sUrl)#cherche la page suivante
        if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'mcanlitv', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 

        oGui.setEndOfDirectory()
                           
   
def __checkForNextPage(sHtmlContent,sUrl):                     
    sPattern = "<div class='sayfa_no_aktif'><a href='(.+?)'>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl =sUrl+aResult[1][0]
        return sUrl

    return False


def CanLiTVshowGenre(): #affiche les genres
    oGui = cGui()
    sUrl=''+CANLITVHOST 
    oInputParameterHandler = cInputParameterHandler()
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('\/',"/")
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '"Baslik":"(.*?)","Logo":".*?","Resim":"(.*?)","Playlist":"(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sPicture = str(aEntry[1])
            sTitle  = aEntry[0].replace("TV BOLUMUNE DON","")
            Link = aEntry[2]
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'CanLiTV2', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
def CanLiTV2(): #affiche les genres
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    

    
    data = commonon().getPage(url)
    data = str(data).replace('\/',"/")
       
    
   
    playlist= re.findall('"Baslik":"(.*?)","Logo":".*?","Resim":"(.*?)","Playlist":"","Stream":"(.*?)"', data, re.S)
    for title,sPicture,track in playlist:
        track = track.replace('\/',"/")    
        title =  alfabekodla(title)    
        
        oOutputParameterHandler = cOutputParameterHandler()
      
        oOutputParameterHandler.addParameter('sMovieTitle', str(title))
        oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
        oOutputParameterHandler.addParameter('siteUrl', str(track))
        oGui.addMovie(SITE_IDENTIFIER, 'play__', title, sPicture, sPicture, '', oOutputParameterHandler)

        

    oGui.setEndOfDirectory() 
def sshowBox19():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(name )
    
    url = 'plugin://plugin.video.OTV_MEDIAM/?url='+urllib.quote_plus(url)+'&streamtype=HLS&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
    xbmc.executebuiltin('Dialog.Close(all, true)')
    
    
def sshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://www.kolaytv.com/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    url = re.findall('<iframe width="100%" height="100%" src="(.*?)"', data, re.S)[0]                                     
    print url          
	           
                                                              
                         
    urla  = "http://www.kolaytv.com/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(url,headers=referer)			             	                                                
    print data
    aaencoded = re.search('<script type="text/rocketscript">(.*?) </script>',data)
    dtext = AADecoder(aaencoded.group(1)).decode()
    
                     
    playlist = re.findall("= '(.*?)'", dtext)[0]                     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    
    
    sHosterUrl = playlist + '|' + Header
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
def sshowBox4():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle =  alfabekodla(sTitle )
    url = oInputParameterHandler.getValue('siteUrl')
    if "m.canlitv.com/atv" in url:      
	sURL ='https://securevideotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/atvhd/atvhd.m3u8'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sURL)
        oGui.addTV(SITE_IDENTIFIER, 'atvBox', sTitle, '', '', '', oOutputParameterHandler)	     

    if "m.canlitv.com/tv-8" in url:
        sURL ='http://www.tv8.com.tr/canli-yayin'
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
        oGui.addTV(SITE_IDENTIFIER, 'tv8canli', sTitle, '', '', '', oOutputParameterHandler)
    
    else:
        req = urllib2.Request(url)

        req.add_header('User-Agent', useragent)
        response = urllib2.urlopen(req)

        rd = response.read()

   

		    
        sHosterUrl= re.findall('file.*?"(.+?)"',rd)[0]                          

    

        Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
        sHosterUrl = sHosterUrl + '|' + Header 
    
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setTitle(sTitle)
        oGuiElement.setMediaUrl(sHosterUrl)
        oPlayer = cPlayer()
        oPlayer.clearPlayList()
        oPlayer.addItemToPlaylist(oGuiElement)
        oPlayer.startPlayer() 
def tv8canli():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    
    urla  = "http://www.tv8.com.tr/"
                      
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    data=data.replace('"SecurePath": "', '"SecurePath":"')      
    streamDaten = re.findall('src\'\:  "(http.*?/tv8hd.m3u8.*?)"', data, re.S)
    if streamDaten:
                  (serviceUrl )= streamDaten[0]
                       
                          
    sHosterUrl = "%s"  % (serviceUrl.replace('\u0026', "&"))



    

    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
                         
def atvBox():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle =  alfabekodla(sTitle )
    req = urllib2.Request(url)
    req.add_header('User-Agent', useragent)
    response = urllib2.urlopen(req)
    rd = response.read()
    rest= re.findall('file: "(.+?)"',rd)[0]                          
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
                         
                                                   
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    data = commonon().getPage(url)
                          
                     
    playlist =  re.findall('file.*?"(.+?)"', data)[0]                     
    Header = 'User-Agent=Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; Nexus One Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    
    
    sHosterUrl = playlist + '|' + Header
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer() 
         
      
def play__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
        
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(title)
    oGuiElement.setMediaUrl(url)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
        
def showWebbbib():
    oGui = cGui()

   		#name,url,mode,icon
    liz=xbmcgui.ListItem('Liste ac',thumbnailImage= "https://dl.dropboxusercontent.com/u/272613616/IPTV/beceriksizlerlogo_yeni_version2.png",iconImage="DefaultFolder.png")
    uurl="plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5cshani%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url=https%3a%2f%2fdl.dropboxusercontent.com%2fu%2f272613616%2fkodi-xbmc.xml"
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)

    oGui.setEndOfDirectory()
        

