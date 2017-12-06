#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *                   

SITE_IDENTIFIER = 'Arabic_tv'
SITE_NAME = 'Arabic TV'
SITE_DESC = 'Replay TV'
import cookielib
import re
import urllib2,urllib
from BeautifulSoup import BeautifulSoup
TELEDUNET_CHANNEL_PAGE = 'http://www.teledunet.com/'
import xbmcaddon
import time
#addon_id = 'plugin.video.shahidmbcnet'
selfAddon = xbmcaddon.Addon()

from youtubecom_tr import YOUTUBEplaylist
import re,json
ALMAN_SINEMA = (True, 'showGenre') 

headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding':'gzip, deflate, sdch',
         'Accept-Language':'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
         'Cache-Control':'max-age=0',
         'Connection':'keep-alive',
         'Cookie':'PHPSESSID=vdim08d5apol9179tpk5vm01t',
         'Host':'www.teledunet.com',
         'Referer':'http://www.teledunet.com/',
         'Upgrade-Insecure-Requests':'1',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

#userName='orhan'
#password='t12344321'                


streamurl = 'http://filmpalast.to/stream/{id}/1'

import urllib2,urllib,cgi, re
import HTMLParser
import json
import traceback
import os
import cookielib
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
import datetime
import time
import sys
HEADER_HOST = 'www.teledunet.com'
HEADER_USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
TELEDUNET_TIMEPLAYER_URL = 'http://www.teledunet.com/mobile/'
PPV_CHANNEL_URL='rtmp://www.teledunet.com/live/'
TELEDUNET_CHANNEL_PAGE = 'http://www.teledunet.com/mobile/?con'
HEADER_REFERER = 'http://www.teledunet.com/'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding':'gzip, deflate, sdch',
         'Accept-Language':'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
         'Cache-Control':'max-age=0',
         'Connection':'keep-alive',
         'Cookie':'PHPSESSID=vdim08d5apol9179tpk5vm01t',
         'Host':'www.teledunet.com',
         'Referer':'http://www.teledunet.com/',
         'Upgrade-Insecure-Requests':'1',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()

def _html(url, rheaders=None):
    """Downloads the resource at the given url and parses via BeautifulSoup"""
    headers = { "User-Agent": HEADER_USER_AGENT  }
    if rheaders:
        headers.update(rheaders);
    request = urllib2.Request (url , headers = headers)
    return BeautifulSoup(_get(request), convertEntities=BeautifulSoup.HTML_ENTITIES)


def __get_cookie_session():
    # Fetch the main Teledunet website to be given a Session ID
    _html('http://www.teledunet.com/')

    for cookie in cj:
        if cookie.name == 'PHPSESSID':
            return 'PHPSESSID=%s' % cookie.value

    raise Exception('Cannot find PHP session from Teledunet')
def egetUrl(url, cookieJar=None,post=None,referer=None):

	cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
	opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
	#opener = urllib2.install_opener(opener)
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
	if referer:
		req.add_header('Referer',referer)
	response = opener.open(req,post,timeout=30)
	link=response.read()
	response.close()
	return link;

def performLogin():
	try:
		cookieJar=cookielib.LWPCookieJar()
		userName=selfAddon.getSetting( "teledunetTvLogin" )
		password=selfAddon.getSetting( "teledunetTvPassword" )
		print 'Values are ',userName,password
		post={'login':userName,'password':password,'rememberme':'1','submitlogin':'Login Now'}
		post = urllib.urlencode(post)
		html_text=egetUrl("http://www.teledunet.com/plugin_tv_login.php?referer=http%3A%2F%2Fwww.teledunet.com%2F",cookieJar,post)
		cookieJar.save (COOKIEFILE,ignore_discard=True)
		#print 'cookie jar saved',cookieJar
		#html_text=getUrl("http://www.teledunet.com/",cookieJar,referer='http://www.teledunet.com/boutique/connexion.php')
		#cookieJar.save (COOKIEFILE,ignore_discard=True)
		return shouldforceLogin(cookieJar)==False
	except:
		traceback.print_exc(file=sys.stdout)
		return False

def shouldforceLogin(cookieJar=None):
    try:
        url="http://www.teledunet.com/plugin_tv_login.php?referer=http%3A%2F%2Fwww.teledunet.com%2F"
        if not cookieJar:
            cookieJar=getCookieJar()
        html_txt=egetUrl(url,cookieJar)
        
            
        if '<input name="connect_user"' in html_txt:
            return True
        else:
            return False
    except:
        traceback.print_exc(file=sys.stdout)
    return True


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
            sUrl = 'http://filmpalast.to/search/title/'+sSearchText  
            sUrl= sUrl.replace(' ','%20')
            searchowMovies(sUrl)
            oGui.setEndOfDirectory()
            return  
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
def Teledunet():
        oGui = cGui()
        urla  = "http://www.teledunet.com/plugin_tv_login.php?referer=http%3A%2F%2Fwww.teledunet.com%2F"                                
        cookie = getUrl(urla, output='cookie').result 
        req = urllib2.Request('http://www.teledunet.com/plugin_tv_login.php')
       
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
        req.add_header('Referer','http://www.teledunet.com/')
        req.add_header('Host','www.teledunet.com')
        req.add_header('Cookie',''+cookie)
        req.add_header('Upgrade-Insecure-Requests','1')
        req.add_header('Connection','keep-alive')                
        req.add_header('Accept-Language','de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7') 
        req.add_header('Accept-Encoding','gzip, deflate')
        req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        userName=selfAddon.getSetting( "teledunetTvLogin" )
	password=selfAddon.getSetting( "teledunetTvPassword" )

	post={'connect_user':userName,'connect_password':password}
        
        time.sleep(6)

          
	urll ='http://www.teledunet.com/'
        data = net.http_POST(urll, post).content
        urlp = re.findall('url=(.*?)"',data ,re.S)[0]
        aut ='https://www.google.fr/url?sa=t&source=web&rct=j&url='+ urlp
        urla  = "http://www.teledunet.com/"
                       
        referer=[('Referer',aut)]
        data =gegetUrl(urla,headers=referer)        
        data =data.replace("id_membre_connected=''","id_membre_connected='orhan'").replace("idu_curent_user='_","idu_curent_user='orhan_")
        dz= re.findall("dz='(.*?)'",data ,re.S)[0]
        ip= re.findall("ip='(.*?)'",data ,re.S)[0]
#        req = urllib2.Request(''+auta)#access main page too
#        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
#        data =_get(req)
        aut = re.findall("idu_curent_user='(.*?)'",data ,re.S)[0]
        
        
        urll = 'http://www.teledunet.com/plugin_tv_channels.php?get_channels=1&top_watch=1&id_membre=orhan'                 
        data = requests.get(urll, headers = headers).text 
        channels = re.findall('<img.*?:url.\'(.*?)\'.*?<td width=100% onclick="play_channel.*?,\'rtmp://.*?:1935/.*?/(.*?)\'.*?color-:#000000;">(.*?)</div>.*?<input type=hidden id="rtmp_.*?" value="(rtmp://.*?:1935/.*?)/.*?">', data, re.S)
        for  image ,stream,sTitle,rtmp in channels:
               userName=selfAddon.getSetting( "teledunetTvLogin" )                                                                                                                                                                                                          
               sPicture ='http://www.teledunet.com/'+ image.replace(' ','%20')
               sUrl = '%s?idu=%s'% (rtmp,aut)+' playpath='+stream+' swfUrl=http://www.teledunet.com/mobile/rtmp_player/player.swf live=1 pageUrl=http://www.teledunet.com/rtmp_player/?channel=%s&streamer=%s?idu=%s' %(stream,rtmp,aut)+'&dz='+dz +'&ip='+ip
                      
#               sUrl = '%s?idu=trimode%s/%s'% (rtmp,aut,stream)
#               sUrl = '%s?idu=%s%s/%s'% (rtmp,self.user,self.aut,stream)+' swfUrl=http://www.teledunet.com/mobile/rtmp_player/player.swf live=1 pageUrl=http://www.teledunet.com/mobile/rtmp_player/?channel=%s&streamer=%s?idu=%s  flashVer=WIN/2022,0,0,192'% (stream,rtmp,self.aut)+' '
               
	       oOutputParameterHandler = cOutputParameterHandler()
	       oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle)) 
               oOutputParameterHandler.addParameter('siteUrl', sUrl)
               oGui.addMovie(SITE_IDENTIFIER, 'play__rabictv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        oGui.setEndOfDirectory()

def mArabictv():
          oGui = cGui()
          
          req = urllib2.Request('http://dlst18.in/dl/vip/film/3/?MA')#access main page too
          req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
          
          data=_get(req)
          channels = re.findall('<a href="(.*?)">(.*?)</A>', data, re.S)
	  for  url,name in channels:
              
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
sPicture="Please go to http://www.teledunet.com/ page do you sign up and go to otv media settinings teledunet login there must always be a local login connection to teledunet there via pc or cellphone and so on ... and all channels are open .. "
def Arabictv():
    oGui = cGui()                           
    liste = []
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://orhantv') 
    oGui.addTV(SITE_IDENTIFIER, 'Teledunet','Teledunet', '','http://www.teledunet.com/logo//Teledunet%20tv.jpg', sPicture, oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/watch?v=kskjGO9QQ38&list=PLgWdHvAnfCMc1YtzDPpJOoU0LBlRm4SQ0') 
    oGui.addDir(SITE_IDENTIFIER, 'YOUTUBEplaylist', 'Arabic Live 70 Channels', 'genres.png', oOutputParameterHandler) 

    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/watch?v=YfH6U8CNp58&index=6&list=PLr3kP-8J1gQNAnUyb2b6d5YecHM7t6fqF') 
    oGui.addDir(SITE_IDENTIFIER, 'YOUTUBEplaylist', 'Arabic Live Channels 2', 'genres.png', oOutputParameterHandler) 
    
    oOutputParameterHandler = cOutputParameterHandler() 
    oOutputParameterHandler.addParameter('siteUrl', 'https://www.youtube.com/watch?v=7NgyiRV8Fas&list=PLlLSJMqQl75cnDGtlOrRkGX9jZgj24rm_') 
    oGui.addDir(SITE_IDENTIFIER, 'YOUTUBEplaylist', 'Arabic Live Channels 3', 'genres.png', oOutputParameterHandler) 

    
    liste.append( ['Categories','https://livetvhd.net/api/categories'] ) 

    for sTitle,sUrl2 in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'Categories':
             oGui.addDir(SITE_IDENTIFIER, 'Categories',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == '--All--':
             oGui.addDir(SITE_IDENTIFIER, 'nArabictv', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'YOUTUBEplaylist',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()                                                                                            
def AllMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    category = oInputParameterHandler.getValue('category')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('\/','/')
    sHtmlContent = re.findall('<a class="post-frame 138" href="(.*?)" title="live tv channels"></a>.*?<img width="180" height="135" src="(.*?)" class="attachment-post-thumbnail wp-post-image".*?<h2><a rel="bookmark" title=".*?">(.*?)</a></h2>',sHtmlContent, re.S)
             
    for Url,Pictures,sTitle in sHtmlContent:
                                                                                                                                                                                                      
            sPicture = "http://arabtvz.com/%s" % ( str(Pictures))                                                                                                                               
            sTitle = alfabekodla(sTitle)
            sUrl = "http://arabtvz.com/%s" % ( str(Url))
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'kkksshowBox1', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
    oGui.setEndOfDirectory()  
   


def Categories():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
   
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
   
       #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
    sPattern = '"name": "(.*?)".*?"seo_name": "(.*?)"'
                                                                
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
           
            sTitle = aEntry[0]
            sPicture = aEntry[1]
              
            Url = str(aEntry[1])
            
                
            sTitle = alfabekodla(sTitle)
            sUrl = "https://livetvhd.net/api/videos/category/%s" % ( str(Url))
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('category', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
            oGui.addMovie(SITE_IDENTIFIER, 'categoryMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def categoryMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    category = oInputParameterHandler.getValue('category')
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sHtmlContent =sHtmlContent.replace('\/','/')
    sHtmlContent = re.findall('"title": "(.*?)".*?"slug": "(.*?)".*?"url": "(.*?)".*?"thumbnail": "(.*?)"',sHtmlContent, re.S)
             
    for sTitle,sUrl,stream,sPicture in sHtmlContent:
                                      
                          
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('stream', stream)
            oOutputParameterHandler.addParameter('category', category)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oGui.addMovie(SITE_IDENTIFIER, 'play__Arabictv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
         
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
        url =  sSearch
        request = urllib2.Request(url,headers)
     
        try:
            reponse = urllib2.urlopen(request)
        except URLError, e:
            print e.read()
            print e.reason
     
        sHtmlContent = reponse.read()
        
 
        #sPattern = '<div class="imagefilm">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)"'
        sPattern ='</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
        
        #sPattern = '<div class="imagefilm"> *<a href="(.+?)" title="(.+?)".+?<img src="(.+?)" alt="(.+?)"'
        sPattern = '</cite>.*?<a href="(.*?)" title="(.*?)"> <img src="(.*?)"'
    
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
           
            sTitle = cUtil().unescape(aEntry[1])
            sPicture = str(aEntry[2])
            if not 'http' in sPicture:
                sPicture = str(URL_MAIN) + sPicture
                
            Url = str(aEntry[0])
            if not 'http' in Url:
                Url = str(URL_MAIN) + Url
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/sinemalar/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'pageshowMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showfilm', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showSinema', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
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
        sPattern = '<small class="rb">.*?<a href="(.*?)" title=".*?"> <img src="(.*?)" class="cover-opacity" alt="(.*?)"/>'
                    
    else:
        oInputParameterHandler = cInputParameterHandler()
        page = oInputParameterHandler.getValue('siteUrl')
        sUrl = oInputParameterHandler.getValue('siteUrl')+'&page='+page
   
        oRequestHandler = cRequestHandler(sUrl)
        sHtmlContent = oRequestHandler.request()
          
       
    sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    
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
           
            sTitle = cUtil().unescape(aEntry[2])
            sPicture = str(aEntry[1])
                        
            Url = str(aEntry[0])
           
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
          
 
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog)
           
        if not sSearch:
            sNextPage = __NextPage(sHtmlContent)#cherche la page suivante
            if (sNextPage != False):
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('page', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showHosters', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
                #Ajoute une entrer pour le lien Next | pas de addMisc pas de poster et de description inutile donc
 
    if not sSearch:
        oGui.setEndOfDirectory()

def __NextPage(sHtmlContent):
    sHtmlContent = sHtmlContent.replace("'",'"')    
    sPattern = '<li class="active">.*?<a href="javascript:void(0)" data-page="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(aResult[1][0]) 
         
def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '</a> <a href="(.*?)" class="syfno">Sonraki Sayfa &raquo;</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        return str(sUrl) + aResult[1][0]

    return False

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')                  
    Urlk='http://hdfilme.tv/'
   
    Urll='http://hdfilme.tv/movie/getlink/6950'+ Url+ '/1'
    referer=[('Referer',Urlk)]
    adata=gegetUrl(Urll,headers=referer) 
    
    sHtmlContent=base64.b64decode(adata)   

    
    
    #sPattern = '<a href="((?:categorie\.php\?watch=)|(?:&#99;&#97;&#116;&#101;&#103;&#111;&#114;&#105;&#101;&#46;&#112;&#104;&#112;&#63;&#119;&#97;&#116;&#99;&#104;&#61;).+?)" onmouseover=.+?decoration:none;">(.+?)<\/a>'
                                               
    sPattern = '"file":"(.*?)4","label":"(.*?)"'
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            
            sGenre = cUtil().unescape(aEntry[0])
            sUrl= aEntry[0].replace('\/','/')
            sTitle = aEntry[1].decode("latin-1").encode("utf-8")
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'play__hdfilme', sGenre, '', '', '', oOutputParameterHandler)
        cConfig().finishDialog(dialog)   
                           
    oGui.setEndOfDirectory()    
def play__Arabictv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    stream = oInputParameterHandler.getValue('stream')
    category = oInputParameterHandler.getValue('category')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    Urllk='https://livetvhd.net/video/'+category+'/' +sUrl
    
    meaders={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Accept-Encoding':'gzip, deflate, br',
         'Accept-Language':'de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4',
         'Cache-Control':'max-age=0',
         'Connection':'keep-alive',
         'Cookie':'__cfduid=d32bdf9d9b241a16d3995cc3a7fb04adb1508227980; cookieconsent_dismissed=yes; _ga=GA1.2.1331539591.1508227980; _gid=GA1.2.723596109.1508446336; laravel_session=484bc65ad10c9661f74cb6a63a5ea7ed81d63637',
        
         'Referer':Urllk,
         'Upgrade-Insecure-Requests':'1',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
                                               
    
    Urll='https://livetvhd.net/api/videos'
    sHtmlContent = requests.get(Urll, headers = meaders).text 
    sHtmlContent =sHtmlContent.replace('\/','/')
    cookie = getUrl(Urllk, output='Cookie').result
    token = re.findall('"token": "(.*?)"', sHtmlContent,re.S)[0]
    Url= stream+'?token=' + token +'|Referer='+Urllk

    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(Url)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
def play__rabictv():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
  
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
def kkksshowBox1():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    urla  = "http://arabtvz.com/"
                       
    referer=[('Referer',urla)]
    data=gegetUrl(Url,headers=referer) 
    urll = re.findall('<iframe width="1000" height="700" allowfullscreen="0".*?src="(.*?)"', data, re.S)[0]                                     
             
	              
 
                                                            
                        
    
    data = requests.get(urll, headers = {'Referer': Url, 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0 Iceweasel/44.0', 'Accept': '*/*'}).text
    if '<source type="application/x-mpegurl"' in data: 
          sHosterUrl = re.findall('<source type="application/x-mpegurl"src="(.*?)"',data, re.S)[0]
          url=sHosterUrl+ '|Referer=http://releases.flowplayer.org/swf/flowplayer-3.2.18.swf&User-Agent=iPad'
		             	                                                
    if "netConnectionUrl" in data: 
          sHosterUrl = re.findall("netConnectionUrl: '(.*?)'",data, re.S)[0]
          url=sHosterUrl+ '|Referer=http://releases.flowplayer.org/swf/flowplayer-3.2.18.swf&User-Agent=iPad'
        
    if "player-frame-wrapper" in data: 
          rUrl = re.findall('<iframe src="(.*?)"',data, re.S)[0]
          if 'www.youtube.com' in rUrl:
              oOutputParameterHandler = cOutputParameterHandler()
              oOutputParameterHandler.addParameter('siteUrl', rUrl)
              oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', '', '', oOutputParameterHandler)
          referer=[('Referer',urla)]
          dat=gegetUrl(rUrl,headers=referer) 
          sHosterUrl = re.findall("src: '(.*?)'", dat, re.S)[0]       
          
          url=sHosterUrl+ '|Referer=http://releases.flowplayer.org/swf/flowplayer-3.2.18.swf&User-Agent=iPad'
        
                    
                        
         
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
def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sHosterUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
 
    
    #oHoster = __checkHoster(sHosterUrl)
    oHoster = cHosterGui().checkHoster(sHosterUrl)

    if (oHoster != False):
        
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)

    oGui.setEndOfDirectory()