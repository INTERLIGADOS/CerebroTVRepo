#-*- coding: utf-8 -*-


from resources.lib.otvhelper import *
 
AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path')

default = os.path.join(addonDir, 'default.py')
 
SITE_IDENTIFIER = 'iptvtv_mobi'
SITE_NAME = 'IPTV TÜRK'


yediyirmi = 'http://sonicstream.tv/App/data/tv.php?id=29731'

MOVIE_TURK = (True, 'load')



 
def load():
    oGui = cGui()
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', CANLIPTV)
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'TÚRKTV spor ve ulusal', 'search.png', oOutputParameterHandler)
   
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl',IDturk)
    oGui.addDir(SITE_IDENTIFIER, 'MshowGenre', 'TÚRKTV GENEL KANALLAR', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', yediyirmi)
    oGui.addDir(SITE_IDENTIFIER, 'Asonicstream', '7/24  TV', 'search.png', oOutputParameterHandler)
           
    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        showMovies(sSearchText)
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
   
def MshowGenre(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    data = getUrl(sUrl)  
   
    channels = re.findall('<meta http-equiv="refresh" content="0;URL=(.*?)">', data, re.S)[0]  

    oRequestHandler = cRequestHandler(channels)
    sHtmlContent = oRequestHandler.request()
 
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
    
    sPattern = '<a title=".*?" href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
    
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
            sTitle  = aEntry[2]
            Link = aEntry[0]
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'kkksshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    
def kkksshowBox1():
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
def showGenre():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    
    
    data = gegetUrl(sUrl)  
    channels = re.findall('#EXTINF:-1,(.*?)\n(.*?)\n', data, re.S)                                    
    for sTitle ,sUrl in channels: 
            
            sTitle =  alfabekodla(sTitle)
            sPicture ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMmeXyixY3J_CYfMd6A0eUIdyM-cpho53UCwRhz0aaikgJYPik'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
       

        

       
    oGui.setEndOfDirectory()
 
                                     
         
      
          
       
def play__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    #sUrl = '[REGEX]{"url": "([^"]+)"}[URL]http://hdfauthftv-a.akamaihd.net/esi/TA?format=json&url=http%3A%2F%2Flive.francetv.fr%2Fsimulcast%2FFrance_2%2Fhds%2Findex.m3u8&callback=_jsonp_loader_callback_request_2'
    #Special url
    if '[REGEX]' in sUrl:
        sUrl = GetRealUrl(sUrl)
        sUrl = sUrl + '|User-Agent=Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36'
    
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
        
def mmMshowGenre(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')

    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 
    
    sPattern = '<a title=".*?" href="(.*?)">.*?<img src="(.*?)" alt="(.*?)"'
    
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
            sTitle  = aEntry[2]
            Link = aEntry[0]
            sTitle =  alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory() 
def msshowBox1():
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
def Asonicstream(): #affiche les genres
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
      
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
            
    Urlo  = "http://sonicstream.tv/App/in.5fa2987984adb.php?app=5fa2987984adac50845"
    urla  = "http://sonicstream.tv/"
                
    referer=[('Referer',urla)]                                                                                     
     
    data=gegetUrl(Urlo,headers=referer)                                               

    IDA=re.findall('location.href="(.*?)"', data, re.S)[0]
    
    channels=re.findall('<div class="listType" >.*?<a href="(.*?)" title="(.*?)">.*?<img src="(.*?)">', sHtmlContent, re.S)
        
    for Link,sTitle,sPicture in channels:
            
            sTitle =  alfabekodla(sTitle)
                     
    
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'sshowBox4', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        

    oGui.setEndOfDirectory()    
    
def sshowBox4():
    oGui = cGui()
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urlo  = "http://sonicstream.tv/App/in.5fa2987984adb.php?app=5fa2987984adac50845"
    urla  = "http://sonicstream.tv/"
                
    referer=[('Referer',urla)]                                                                                     
     
    dat=gegetUrl(Urlo,headers=referer)                                               
    Urlom  = "http://sonicstream.tv/"                                                                                           
                                  
    IDA=re.findall('location.href="(.*?)"', dat, re.S)[0]  
    gent  = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    Agent=[('Referer',Urlom )] 
    url= "http://sonicstream.tv/App/%s%s" %(IDA,sUrl)  
    
    data = gegetUrl(url,headers=Agent)  
    channels = re.findall('data=".*?secury=(.*?)&serverID=(.*?)&getChannel=(.*?)"', data, re.S)                                    
    for secury,serverID,getChannel in channels:              
	                                                                           
        TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'

#        playlist = 'rtmp://'+serverID+'.streamgo1.stream:1935/edge/?'+secury+' playpath=ch'+getChannel+' swfUrl=http://sonicstream.tv/App/webPlayer.swf?secury='+secury+'&serverID='+serverID+'&getChannel='+getChannel+' pageUrl='+url+ 'flashVer=WIN\\2023,0,0,205'
        playlist = 'http://'+serverID+'.streamgo1.stream:1935/edge/ch'+getChannel+'/playlist.m3u8?secury='+secury

        sTitle =  alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', playlist)
        oGui.addDir(SITE_IDENTIFIER, 'showotvplayer', sTitle, 'genres.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()                                   
         
def sshowBox1():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    iconimage = oInputParameterHandler.getValue('sThumbnail')
    name =  alfabekodla(name )
    
    from default  import PlayUrl
    PlayUrl(name, url, iconimage)
    
    oGui.setEndOfDirectory()                                        
  