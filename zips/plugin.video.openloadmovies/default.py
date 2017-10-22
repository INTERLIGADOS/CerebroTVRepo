import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, dandy
import xbmcaddon
from addon.common.addon import Addon
from md_request import open_url
addon_id='plugin.video.openloadmovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0'


# SITE = selfAddon.getSetting('website')
# SITE = SITE.replace('PopNow','http://getmypopcornnow.xyz/')
# SITE = SITE.replace('Oload','http://openloadmovies.net/')
# SITE = SITE.replace('PubOnline','http://pubfilmonline.net/')

BASEURL = 'http://pubfilmonline.net/'

def MENU():
    addDir('[B][COLOR cornflowerblue]Trending[/COLOR][/B]',BASEURL + 'trending/?get=movies',5,ART + 'trend.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]Featured[/COLOR][/B]',BASEURL + 'genre/featured/',5,ART + 'feature.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]All Movies[/COLOR][/B]',BASEURL + 'movies/',5,ART + 'all_mov.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]Genres[/COLOR][/B]',BASEURL + 'ratings/',3,ART + 'genres.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]Release Year[/COLOR][/B]',BASEURL + 'trending/',4,ART + 'release.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]IMDB Top Movies[/COLOR][/B]',BASEURL + 'top-imdb/',7,ART + 'imdb.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]TV Shows[/COLOR][/B]',BASEURL + 'tvseries/',8,ART + 'tv_shows.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]IMDB Top TV[/COLOR][/B]',BASEURL + 'top-imdb/',2,ART + 'tv_imdb.jpg',FANART,'')
    addDir('[B][COLOR cornflowerblue]Search[/COLOR][/B]','url',6,ART + 'search.jpg',FANART,'')
    setView('tvshows', 'tvshows-view')

def Get_content(url):
    OPEN = open_url(url).content
    Regex = re.compile('item movies.+?img src="(.+?)" alt="(.+?)".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,name,url in Regex:
            icon = icon.replace('w185','w300_and_h450_bestv2')
            name = name.replace('&#8217;','\'').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8211;','-')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,icon,FANART,'')
    np = re.compile('class=.+?current.+?<a href=\'(.+?)\'',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,5,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_Genres(url):
    OPEN = open_url(url).content
    Regex = re.compile('<ul class="genres scrolling">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a href="(.+?)"',re.DOTALL).findall(str(Regex))
    for url in Regex2:
        name = url.split('/')[4]
        name = name.split('/')[0].split('.')[0].title()
        addDir('[B][COLOR cornflowerblue]%s[/COLOR][/B]' %name,url,5,ART + 'genres.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_Years(url):
    OPEN = open_url(url).content
    Regex = re.compile('<h2>Release (.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            addDir('[B][COLOR cornflowerblue]%s[/COLOR][/B]' %name,url,5,ICON,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_imdb(url):
    OPEN = open_url(url).content
    Regex = re.compile('Movies</h3>(.+?)TV Shows</h3>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<div class="image">.+?<img src="(.+?)" /></a>.+?<a href="(.+?)">(.+?)</a></div>',re.DOTALL).findall(str(Regex))
    for icon,url,name in Regex2:
            icon = icon.replace('w90','w300_and_h450_bestv2')
            name = name.replace('&#8211;',':').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#8217;','\'')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_tv_imdb(url):
    OPEN = open_url(url).content
    Regex = re.compile('TV Shows</h3>(.+?)<footer class="main">',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<img src="(.+?)".+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(Regex))
    for icon,url,name in Regex2:
            icon = icon.replace('w90','w300_and_h450_bestv2')
            name = name.replace('&#8217;','').replace('#038;','').replace('\\xc3\\xa9','e').replace('&#039;','\'')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,9,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
    
def Get_TV(url):
    OPEN = open_url(url).content
    Regex = re.compile('class="item tvshows".+?src="(.+?)" alt="(.+?)".+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,name,url in Regex:
            icon = icon.replace('w185','w300_and_h450_bestv2')
            name = name.replace('&#8217;','\'')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,9,icon,FANART,'')
    np = re.compile('class="current".+?<a href=\'(.+?)\'',re.DOTALL).findall(OPEN)
    for url in np:
            addDir('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,8,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_show_content(url):
    OPEN = open_url(url).content
    Regex = re.compile('<div class="imagen">.+?<div class="numerando">(.+?)</div>.+?<a href="(.+?)">(.+?)</a>',re.DOTALL).findall(OPEN)
    for name1,url,name2 in Regex:
            name = name1+'   '+name2
            name = name.replace('&#039;','\'').replace('amp;','')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_links(url):
    OPEN = open_url(url).content
    PAGE = re.compile('<iframe src="(.+?)"').findall(OPEN)[0]
    headers = {'User-Agent':User_Agent}
    link = open_url(PAGE,headers=headers).content
    Regex = re.compile('/embed/(.+?)\' id="(.+?)"',re.DOTALL).findall(link)
    for url,label in Regex:
        url = 'https://embed1.vidics.tv/embed/' + url 
        addDir('[B][COLOR white]%s[/COLOR][/B]' %label,url,100,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Search():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = BASEURL + '/?s=' + search
                search_res(url)
    
def search_res(url):
    OPEN = open_url(url).content
    Regex = re.compile('<div class="result-item">.+?<a href="(.+?)">.+?<img src="(.+?)" alt="(.+?)"',re.DOTALL).findall(OPEN)
    for url,icon,name in Regex:
            name = name.replace('&#8217;','').replace('#038;','')
            icon = icon.replace('w90','w300_and_h450_bestv2')
            if '/tvseries/' in url:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,9,icon,FANART,'')    
            else:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)') 

def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )


        
def RESOLVE(url):
    res_quality = []
    stream_url = []
    quality = ''
    HOLDER = open_url(url).content
    if '<iframe src=' in HOLDER:
        PAGE = re.compile('<iframe src="(.+?)"').findall(HOLDER)[0]
        headers = {'User-Agent':User_Agent}
        GETLINKS = open_url(PAGE,headers=headers).content
        try:
            match = re.compile('/embed/(.+?)\' id="(.+?)"').findall(GETLINKS)
            for link,label in match: 
                    link = 'https://embed1.vidics.tv/embed/' + link        
                    quality = '[B][COLOR white]%s[/COLOR][/B]' %label
                    res_quality.append(quality)
                    stream_url.append(link)
            if len(match) >1:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.select('Please Select Quality',res_quality)
                    if ret == -1:
                        return
                    elif ret > -1:
                        url = stream_url[ret]
            else:
                url = re.compile("'/embed/(.+?)\'").findall(GETLINKS)[0]
                url = 'https://embed1.vidics.tv/embed/' + url
    
        except:
            xbmc.executebuiltin("XBMC.Notification([COLOR cornflowerblue]Sorry[/COLOR],[COLOR cornflowerblue]Link Unavailable[/COLOR] ,2000)")
        

    
        refx = url
        headers = {'User-Agent':User_Agent}
        link = open_url(url,headers=headers).content
        playlink = re.compile("<script>.+?'(.+?)'",re.DOTALL).findall(link)[0]
        url = playlink +'|User-Agent=Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0&Referer='+refx
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={"Title": name})
        liz.setProperty("IsPlayable","true")
        liz.setPath(url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
    else:
        res_quality = []
        stream_url = []
        quality = ''
        refx=url
        OPEN = open_url(url).content
        IDS = re.compile('data-ids="(.+?)"').findall(OPEN)[0]
        SERVER = re.compile('data-servers="(.+?)"').findall(OPEN)[0]
        NONCE = re.compile('"ajax_get_video_info":"(.+?)"').findall(OPEN)[0]
    
        headers = {'Origin':'http://pubfilmonline.net', 'Referer':url,
                   'X-Requested-With':'XMLHttpRequest', 'User_Agent': User_Agent}

        req_url = 'http://pubfilmonline.net/wp-admin/admin-ajax.php'

        form_data = {'action':'ajax_get_video_info','ids':IDS,'server':SERVER,'nonce':NONCE}

        link = open_url(req_url, 'post', data=form_data, headers=headers).content
        try:
            match = re.compile('"file".+?"(.+?)".+?"label".+?"(.+?)"').findall(link)
            for link,label in match:                       
                    quality = '[B][COLOR white]%s[/COLOR][/B]' %label
                    res_quality.append(quality)
                    stream_url.append(link)
            if len(match) >1:
                    dialog = xbmcgui.Dialog()
                    ret = dialog.select('Please Select Quality',res_quality)
                    if ret == -1:
                        return
                    elif ret > -1:
                        url = stream_url[ret]
            else:
                url = re.compile('"file".+?"(.+?)"').findall(link)[0]
    
        except:
            xbmc.executebuiltin("XBMC.Notification([COLOR cornflowerblue]Sorry[/COLOR],[COLOR cornflowerblue]Link Unavailable[/COLOR] ,2000)")
        

    
        url = url.replace('\/','/')
        #print ':::::::::::::::::::::::::::::'+url
        #url = url +'|User-Agent=Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0&Referer='+refx
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={"Title": name})
        liz.setProperty("IsPlayable","true")
        liz.setPath(url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
###odd resolve       



    
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
	return param


                
def addDir(name,url,mode,iconimage,fanart,description):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	liz.setProperty('fanart_image', fanart)
	if mode==100:
		liz.setProperty("IsPlayable","true")
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok


params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None




try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	description=urllib.unquote_plus(params["description"])
except:
	pass

if mode==None or url==None or len(url)<1 : MENU()
elif mode == 2 : Get_tv_imdb(url)
elif mode == 3 : Get_Genres(url)
elif mode == 4 : Get_Years(url)
elif mode == 5 : Get_content(url) 
elif mode == 6 : Search()
elif mode == 7 : Get_imdb(url)
elif mode == 8 : Get_TV(url)
elif mode == 9 : Get_show_content(url)
elif mode == 10 : Get_links(url)
elif mode ==100: RESOLVE(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))

















