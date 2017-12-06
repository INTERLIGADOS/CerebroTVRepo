#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
SITE_IDENTIFIER = 'turkfilmleri_org'
SITE_NAME = 'Türk filmleri'


URL_MAIN = 'http://www.myvideo.az/'

TURK_SINEMA= (True, 'load')

URL_PIC = 'http://www.myvideo.az'
def turkfilmleri():
    oGui = cGui()
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Türk Filmi Ara', 'search.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl','http://orhantv/')
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'Türk filmleri', 'genres.png', oOutputParameterHandler)
    
              
    oGui.setEndOfDirectory()
 
def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://www.myvideo.az/c/search?srch_str='+sSearchText  
            Searchsinema2(sUrl)
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
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR azure] Lettre [COLOR teal]'+ sTitle +'[/COLOR][/COLOR]', 'genres.png', oOutputParameterHandler)
        
    cConfig().finishDialog(dialog)
    
    oGui.setEndOfDirectory()           
def showGenre(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl ='http://www.myvideo.az/c/movies/?ci_m=search&genre=36'
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                             
    sPattern = '<div class="mv_movie_modal_info modal-fluid-carousel left_align">.*?<a href=".*?" class="mv_movie_modal_info_cover left_cover" style="background-image:url.\'(.*?)\'.">.*?<a href="(.*?)".*?class="mv_movie_item_title bpgArial">                                          (.*?)</a>'
    


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
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            
                      
            
           
            sTitle = alfabekodla(sTitle)
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = mm__checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showsinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()
def showsinema(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                             
    sPattern = 'style="background-image:url.\'(.*?)\'.">.*?<a href="(.*?)".*?class="mv_movie_item_title bpgArial">                                          (.*?)</a>'
    
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
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            
                      
            
           
            sTitle = alfabekodla(sTitle)
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'sshowBox2', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = mm__checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showsinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def mm__checkForNextPage(sHtmlContent):
    oGui = cGui()
    
    sPattern = '<li class="selected">.*?</li><li><a href="(.*?)" >'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(URL_PIC ) + aResult[1][0]
def Searchsinema2(sSearch = ''):
    oGui = cGui()
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();                                                                                         
    sHtmlContent =sHtmlContent.replace('\n', "")                                                                                                                                                           

    sPattern = '<div class="mv_video_item_cover_cont" >.*?class="vd_go_to_video " style="background-image:url.(http://static.myvideo.az.*?jpg).; display:block;".*?<a href="(.*?)" class="mv_video_title bpgArial">(.*?)</a>'
    
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
            sPicture = str(aEntry[0])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            sUrl = aEntry[1]
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            
                      
            
           
            sTitle = alfabekodla(sTitle)
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'sSearchBox3', sTitle,sPicture, sPicture, '', oOutputParameterHandler)
         
        cConfig().finishDialog(dialog)                
           
        sNextPage = mm__checkForNextPage(sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showsinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()   
def sSearchBox3():
    oGui = cGui()
       
    net = Net()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
   
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
                
    	
    resp = net.http_GET(url)
    data = resp.content
    Url = re.findall('file: "(.*?)"', data)[0]
     
    Header = 'User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
    
    
    
    
   
    sHosterUrl =Url + '|' + Header
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()
    return False    
    oGui.setEndOfDirectory()
 
def sshowBox2():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    print  sUrl
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    
    data = requests.get(sUrl).content 
       
    stream = re.findall('<td class="title">.*?<a href=".*?ci_m=inner&movie_id=.*?&(.*?)" class="title">', data, re.S)
    print stream
    
    url = "http://embed.myvideo.az/flv_player/jwconfigFb.php?%s.mp4"%stream[0]
		                        
            
    data=getUrl(url).result 
    Url = re.findall("<file>(.*?)</file>", data)[0]

     
    Header = 'Referer=http://www.myvideo.az/flv_player/j/playerNew.swf'
    
    
    sHosterUrl =Url + '|' + Header
    
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sHosterUrl)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()       
    return False
    oGui.setEndOfDirectory()