#-*- coding: utf-8 -*-                   
from resources.lib.otvhelper import *
from bicaps_net import bicaps
from hdfilmcehennemi_com import hdfilmcehennemi
from turkfilmleri_org import turkfilmleri
from jetfilmizle_biz import jetfilmizle
from fullfilm_org import fullfilm
from filmifullizle_org import filmifullizle
SITE_IDENTIFIER = 'filmakinesi_org'
SITE_NAME = 'Filmakinesi.org'
SITE_DESC = 'Films streaming'

TURK_SINEMA= (True, 'showGenre') 
URL_MAIN = 'http://filmakinesi.org/'

MOVIE_COMMENTS = (True, 'showGenre')
def encode_for_logging(c, encoding='ascii'):
    if isinstance(c, basestring):
        return c.encode(encoding, 'replace')
    elif isinstance(c, Iterable):
        c_ = []
        for v in c:
            c_.append(encode_for_logging(v, encoding))
        return c_
    else:
        return encode_for_logging(unicode(c))

def turksinema():
    oGui = cGui()
    liste = []
    liste.append( ['FilMakinesi','http://filmakinesi.org/wp-content/wptouch-data/uploads/mobil_logom.png'] ) 
    liste.append( ['Bicaps','http://www.bicaps.net/wp-content/uploads/bicapslogo31.png'])
    liste.append( ['Hdfilmcehennemi','https://www.hdfilmcehennemi.com/wp-content/themes/cehennem/img/logo-hdfilm.png']) 
    liste.append( ['FilmiFullizle','http://filmifullizle.co/_css/filmifullizle.png?v=1.8']) 
    liste.append( ['Jetfilmizle','https://s-media-cache-ak0.pinimg.com/originals/14/7b/2e/147b2e26bc8c2d86d8b38c7fb81ac744.png']) 
    liste.append( ['Türk Filmleri','https://fullonlinefilmizle.net/wp-content/uploads/turk-filmi-izle-turk-filmleri-full-hd-izle.png']) 
    liste.append( ['FullFilm','http://www.filmi-izle.org/wp-content/themes/KralFilm/logo/logo.png'])

    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Türk Filmleri':
             oGui.addMovie(SITE_IDENTIFIER, 'turkfilmleri',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FilmiFullizle':
             oGui.addMovie(SITE_IDENTIFIER, 'filmifullizle',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Hdfilmcehennemi':
             oGui.addMovie(SITE_IDENTIFIER, 'hdfilmcehennemi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Bicaps':
             oGui.addMovie(SITE_IDENTIFIER, 'bicaps', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FilMakinesi':
             oGui.addMovie(SITE_IDENTIFIER, 'filmakinesi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'FullFilm':
             oGui.addMovie(SITE_IDENTIFIER, 'fullfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Jetfilmizle':
             oGui.addMovie(SITE_IDENTIFIER, 'jetfilmizle', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

               
                    
                    
    oGui.setEndOfDirectory()                    

 
def showSearch():
    oGui = cGui()
 
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = 'https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=10&hl=tr&prettyPrint=false&source=gcsc&gss=.com&sig=4f0e4d5d7dc9efa79ab5cf95d689a1bc&cx=008101071101454213985:y59kkwga3hi&q=' + sSearchText
        sUrl= sUrl.replace(' ','+')
        searchowMovies(sUrl)
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
    
def filmakinesi(): #affiche les genres
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'ARA', 'search.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'https://filmakinesi.org/')
    oGui.addDir(SITE_IDENTIFIER, 'sshowMovies', 'Yeni Filmler', 'genres.png', oOutputParameterHandler)

    sUrl='https://filmakinesi.org/'
    

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    
    
    oParser = cParser()
             
    sPattern = '<li id="menu-item-.*?" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.*?"><h4><a href="(.*?)">(.*?)</a>'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sGenre = alfabekodla(aEntry[1])
            
            Link =aEntry[0]
           
            sTitle = alfabekodla(aEntry[1])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Link)
            oGui.addTV(SITE_IDENTIFIER, 'showMovies', sGenre, '', '', '', oOutputParameterHandler)
            
        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()    

def searchowMovies(sUrl):
    oGui = cGui()
    oRequestHandler = cRequestHandler(sUrl)
    data = oRequestHandler.request()
                                
    sHtmlContent = re.findall('"titleNoFormatting":"(.*?)","unescapedUrl":".*?","url":"(.*?)"', data, re.S)
         
    for sTitle,sUrl in sHtmlContent:
             
                       
            sTitle = alfabekodla(sTitle)
            sPicture='http://files.softicons.com/download/business-icons/pretty-office-iv-icons-by-custom-icon-design/png/128/addressbook-search.png'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail',  sPicture) 
            oGui.addMovie(SITE_IDENTIFIER, 'Hosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
def sshowMovies(sSearch = ''):
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
        sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.replace('.html','.html/9')
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<div class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)".*?<div class="dubla.*?">(.*?)</div>'
    
    
  
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
            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumbnail = str(aEntry[1])
            if not 'http' in  sThumbnail:
                 sThumbnail = str(URL_MAIN) +  sThumbnail
                
            
            sTitle =aEntry[2] + ' [COLOR limegreen]' + aEntry[3] +'[/COLOR]'
          
            sTitle = alfabekodla(sTitle)
             
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

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
   




def showMovies(sSearch = ''):
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
        sPattern = '<article class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        sHtmlContent = sHtmlContent.replace('.html','.html/9')
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '<article class="post-.*? film">.*?<a href="(.*?)".*?<img src="(.*?)" alt="(.*?)"'
    
    
  
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
            
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumbnail = str(aEntry[1])
            if not 'http' in  sThumbnail:
                 sThumbnail = str(URL_MAIN) +  sThumbnail
                
            
           
          
            sTitle = aEntry[2]
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail',  sThumbnail) #sortis du poster
            oGui.addTV(SITE_IDENTIFIER, 'Hosters', sTitle, '', sThumbnail, '', oOutputParameterHandler)

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
   
   
   
def __checkForNextPage(sHtmlContent):                     
    sPattern = '<ul><li class="page_info">.+?">.+?</a></li>.+?<li><a href="(.+?)">.+?</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        sUrl = aResult[1][0]
        return sUrl

    return False
 

def Hosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request();
    oParser = cParser()
    sPattern = '<div class="film_part">(.+?)</body>'
   
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<a href="(.*?.html.*?)"><span>(.*?)</span></a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            urls = aEntry[0]
            sTitle = alfabekodla(aEntry[1])
            if "Filmakinesi Özel" in sTitle:      
			  
                  
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
                        oGui.addTV(SITE_IDENTIFIER, 'ozel', sTitle, '', '', '', oOutputParameterHandler)	     

            if "Altyazılı Özel" in sTitle:
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
                        oGui.addTV(SITE_IDENTIFIER, 'ozel', sTitle, '', '', '', oOutputParameterHandler)	     
            if "Tek MAKİNE" in sTitle:
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
                        oGui.addTV(SITE_IDENTIFIER, 'MAKNEHosters', sTitle, '', '', '', oOutputParameterHandler)	     
                        oGui.addTV(SITE_IDENTIFIER, 'ozel', sTitle, '', '', '', oOutputParameterHandler)	     
            if "Tek Raj" in sTitle:
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
                        oGui.addTV(SITE_IDENTIFIER, 'videoraj', sTitle, '', '', '', oOutputParameterHandler)	     
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(urls))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            oGui.addTV(SITE_IDENTIFIER, 'streams', sTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)

    oGui.setEndOfDirectory()
    
def ODKosters():
    oGui = cGui()       
             
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    sPattern = '<p><!--baslik:(.*?)--><iframe width="640" height="360" allowfullscreen src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

           
            Url = str(aEntry[1])            
            Title = str(aEntry[0])
             
            referer=[('Referer',sUrl)]
            streamurl=gegetUrl(Url,headers=referer)                    
            sHoster = re.findall(',path:"/videoembed/(.*?)"', streamurl)              
            
                
           
            Title = alfabekodla(Title)
            HosterUrl= "https://m.ok.ru/video/%s" % sHoster[0]
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl',HosterUrl)
            oGui.addTV(SITE_IDENTIFIER, 'mokru', Title, '', '', '', oOutputParameterHandler)   
                               
        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()


def MAKNEHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    sPattern = '<!--baslik:Tek MAKİNE--><iframe src="(.*?)"'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
            Url = str(aEntry)            
           
           
            referer=[('Referer',sUrl)]
            streamurl=gegetUrl(Url,headers=referer)                    
            sHosterUrl = re.findall('src="(https://drive.google.com.*?)"', streamurl)
            sMovieTitle = alfabekodla(sMovieTitle) 
            
            oHoster = cHosterGui().checkHoster(sHosterUrl[0])

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
    sPattern = '<!--baslik:.*?--><.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
            sHosterUrl = str(aEntry)            
                                
            #xbmc.log( 'fini :' + str(sHosterUrl)) 
            
            #oHoster = __checkHoster(sHosterUrl)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle )
            oOutputParameterHandler.addParameter('sThumbnail', sThumbnail)
            oGui.addTV(SITE_IDENTIFIER, 'streams', sMovieTitle, '', sThumbnail, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

   

def terscevir(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        


def streams():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent = sHtmlContent.replace('<iframe src="http://www.promoliens.net','')
    sHtmlContent = sHtmlContent.replace("<iframe src='cache_vote.php",'')
                
   
    sPattern = '<!--baslik:.*?--><.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
                       
            sHosterUrl = str(aEntry)            
            if "https://filmakinesi.org" in sHosterUrl:
                sHosterUrl=sHosterUrl.replace("https://filmakinesi.org/player/url/","")
                        
                               
                url1="%s" % (sHosterUrl) 
              
                url2 = base64.b64decode(url1)
               
                url3 = terscevir(url2)            
                streamurl=base64.b64decode(url3) 
                                                       
                if "ok/" in streamurl:
                               oGui = cGui()
                               streamurl=streamurl.replace("ok/","") 
                               sHosterUrl= "https://m.ok.ru/video/%s" % streamurl
                                                                            
                if "mail/" in streamurl:                     
                               streamurl=streamurl.replace('mailg/',"") 
                               urlan = re.findall('mail/(.*?)/(.*?)/', streamurl)
                               if urlan:         
                                  for (url1),(url2) in urlan:
                                
                                     
                                                                                            
                                      sHosterUrl = "https://my.mail.ru/mail/%s/video/embed/_myvideo/%s?" % (url1,url2)
                                                    
                                                                            
                                                                                           
                                    			                                  
                if "vk/" in streamurl:     
                                   streamurl=streamurl.replace('g�',"")  
                                   urlan = re.findall('vk/(.*?)/(.*?)/([a-z0-9]+)', streamurl)
                                   if urlan:         
                                     for (url1),(url2),(url3) in urlan:
                                
                               
                                      sHosterUrl= "http://vk.com/video_ext.php?oid=%s&id=%s&hash=%s" % (url1,url2,url3)
                                      
                                     	     	               
                if "uptostream/" in streamurl:     
                                      streamurl=streamurl.replace('g�',"")  
                                      streamurl=streamurl.replace("uptostream/","") 
                                      
                                      sHosterUrl= "http://uptostream.com/iframe/%s" % (streamurl)
                                      
                                      	     
                if "closeload/" in streamurl:     
                                      streamurl=streamurl.replace('g�',"")  
                                      streamurl=streamurl.replace("closeload/","") 
                                      
                                      sHosterUrl= "https://closeload.com/video/embed/%s/" % (streamurl)
                                      
                                                                           	     
                if "openload/" in streamurl:     
                                      oGui = cGui()
                                      streamurl=streamurl.replace('g�',"")  
                                      streamurl=streamurl.replace("openload/","") 
                                      
                                      sHosterUrl= "https://openload.co/embed/%s" % (streamurl)
                                      
                                      
                            
                
                     
           
                                  
                      
	     

           
            
            
            oHoster = cHosterGui().checkHoster(sHosterUrl)

            if (oHoster != False):
                sDisplayTitle = cUtil().DecoTitle(sMovieTitle)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

        cConfig().finishDialog(dialog) 

    oGui.setEndOfDirectory()

def showHostersRR():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sPattern = '<!--baslik:.*?--><.*?[SRC|src]=["|\'](.*?)["|\']'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break

            #si url cryptee mangacity algo
 
    sHoster =  aEntry
    sHoster=sHoster.replace("https://filmakinesi.org/player/url/","")
                
                        
                        
    url1=sHoster
              
    url2 = base64.b64decode(url1)
               
    url3 = terscevir(url2)            
    url3 =url3
    streamurl=base64.b64decode(url3)
    streamurl=streamurl.replace('g�',"")  
    streamurl=streamurl.replace("openload/","") 
                                      
    sHosterUrl= "https://openload.co/embed/%s" % (streamurl)

    sMovieTitle = alfabekodla(sMovieTitle) 
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
def kshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
   
    sHosterUrl = sUrl
 
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()
  