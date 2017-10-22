# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys,xbmcaddon,os, dandy
import urlresolver
from addon.common.addon import Addon
import requests

addon_id='plugin.video.dandymedia'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))
s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
PATH = 'dandymedia'
VERSION = ADDON.getAddonInfo('version')
ART = ADDON_PATH + "/resources/icons/"
BASEURL = 'http://300mbmovies4u.club/'
BASEURL2 = 'http://loadmovie.biz'
BASEURL3 = 'http://cooltvseries.com/'



def Main_menu():
    addDir('[B][COLOR white]1080p Movies[/COLOR][/B]',BASEURL + 'category/hollywood-movie/english-1080p-movie/',5,ART + '1080p_mov.jpg',FANART,'')
    addDir('[B][COLOR white]720p Movies[/COLOR][/B]',BASEURL + 'category/hollywood-movie/720p-movie/',5,ART + '720p_mov.jpg',FANART,'')
    addDir('[B][COLOR white]Blu-Ray[/COLOR][/B]',BASEURL + 'category/hollywood-movie/bluray-movie-hollywood-movie/',5,ART + 'blu.jpg',FANART,'')
    addDir('[B][COLOR white]Hevc[/COLOR][/B]',BASEURL + 'category/hevc-movie/',5,ART + 'hevc_mov.jpg',FANART,'')
    addDir('[B][COLOR white]IMDB Playlist[/COLOR][/B]','https://raw.githubusercontent.com/dandy0850/iStream/master/dandymedia_2/hevc.xml',7,ART + 'imdb_list.jpg',FANART,'')
    addDir('[B][COLOR white]More Debrid Movies[/COLOR][/B]','',50,ART + 'debrid_movs.jpg',FANART,'')
    addDir('[B][COLOR white]HD TV Shows[/COLOR][/B]','',70,ART + 'hdtv_shows.jpg',FANART,'')
    addDir('[B][COLOR white]Popular TV SHOWS[/COLOR][/B]','http://123moviesonline.co/series/',20,ART + 'tv_pop.jpg',FANART,'')
    addDir('[B][COLOR white]Latest Debrid TV[/COLOR][/B]','https://scnsrc.unblocked.srl/category/tv/',25,ART + 'debrid_tv.jpg',FANART,'')
    addDir('[B][COLOR white]HD Concerts[/COLOR][/B]','https://raw.githubusercontent.com/dandy0850/iStream/master/dandymedia_2/hdconcerts.xml',7,ART + 'live.jpg',FANART,'')
    addDir('[B][COLOR white]Top Documentary[/COLOR][/B]','http://topdocumentaryfilms.com/watch-online/',60,ART + 'docu.jpg',FANART,'')
    addDir('[B][COLOR white]UK Soaps[/COLOR][/B]','',30,ART + 'uksoaps.jpg',FANART,'')
    addDir('[B][COLOR white]Childrens[/COLOR][/B]','https://raw.githubusercontent.com/dandy0850/iStream/master/test/bobbychans.txt',8,ART + 'kidstv.jpg',FANART,'')
    addDir('[B][COLOR white]Continuous Playlists[/COLOR][/B]','https://raw.githubusercontent.com/dandy0850/iStream/master/test/dmediakids.xml',89,ART + 'kidscont.jpg',FANART,'')
    setView('tvshows', 'tvshows-view')
#########################
def Get_content(url):
    referer = url
    headers = {'Host': '300mbmovies4u.lol', 'User-Agent': User_Agent, 'Referer': referer}
    OPEN = Open_Url(url)
    Regex = re.compile('id="content">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('="post-thumb".+?href="(.+?)" title="(.+?)".+?src="(.+?)"',re.DOTALL).findall(str(Regex))
    for url,name,icon in Regex2:
            name = name.replace('HEVC','-').replace('&#8211;','').replace('&#8217;','').replace('720p',' - (720p)').replace('1080p',' - (1080p)')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,10,icon,FANART,'')
    np = re.compile('rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR red]Next Page>>>[/COLOR][/B]',url,5,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')  

def Get_links(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('<strong>Download Links</strong>(.+?)<div class="box">',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a href="(.+?)"',re.DOTALL).findall(str(Regex))
    for url in Regex2:
            if 'amazon.com' in url:
                addDir('[B][COLOR white]Direct Link[/COLOR][/B]',url,100,iconimage,FANART,name)
            if urlresolver.HostedMediaFile(url):
                    name2 = url.split('//')[1].replace('www.','')
                    name2 = name2.split('/')[0].capitalize()
                    name2 = name2.replace('Uploadx.org','Uploadx.org [COLOR red](Debrid Req)[/COLOR]').replace('Clicknupload.link','Clicknupload.link [COLOR red](Krypton or Debrid Req)[/COLOR]').replace('Userscloud.com','Userscloud.com [COLOR red](Debrid Req)[/COLOR]').replace('Downace.com','Downace.com [COLOR red](Krypton Only)[/COLOR]')
                    if 'Filecloud.io' not in name2:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)
            if 'multiup.org' in url:
                    url=url.replace('https://www.multiup.org/download/','http://www.multiup.org/en/mirror/').replace('http://www.multiup.org/download/','http://www.multiup.org/en/mirror/')
                    OPEN = Open_Url(url)
                    Regex = re.compile('nameHost="(.+?)".+?validity=(.+?)dateLastChecked=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
                    for name2, validity, url in Regex:
                        if 'invalid' not in validity:
                            if urlresolver.HostedMediaFile(url):
                                if 'filecloud.io' not in name2:
                                    addDir('[B][COLOR white]%s [COLOR blue] (Multiup)[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)
    alt = re.compile('>Download.+?Link</h1>(.+?)Share this:',re.DOTALL).findall(OPEN)
    alt2 = re.compile('href="(.+?)"',re.DOTALL).findall(str(alt))
    for url in alt2:
            if urlresolver.HostedMediaFile(url):
                    name2 = url.split('//')[1].replace('www.','')
                    name2 = name2.split('/')[0].capitalize()
                    name2 = name2.replace('Uploadx.org','Uploadx.org [COLOR red](Debrid Req)[/COLOR]').replace('Clicknupload.link','Clicknupload.link [COLOR red](Krypton or Debrid Req)[/COLOR]').replace('Userscloud.com','Userscloud.com [COLOR red](Debrid Req)[/COLOR]').replace('Clicknupload.me','Clicknupload.link [COLOR red](Krypton or Debrid Req)[/COLOR]')
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)
            if 'multiup.org' in url:
                    url=url.replace('https://www.multiup.org/download/','http://www.multiup.org/en/mirror/').replace('http://www.multiup.org/download/','http://www.multiup.org/en/mirror/')
                    OPEN = Open_Url(url)
                    Regex = re.compile('nameHost="(.+?)".+?validity=(.+?)dateLastChecked=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
                    for name2, validity, url in Regex:
                        if 'invalid' not in validity:
                            if urlresolver.HostedMediaFile(url):
                                if 'filecloud.io' not in name2:
                                    name2 = name2.capitalize()
                                    addDir('[B][COLOR white]%s [COLOR blue] (Multiup)[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)            
    xbmc.executebuiltin('Container.SetViewMode(50)')
                                
#########################

#########################
def Debtv_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="post" id=.+?href="(.+?)".+?>(.+?)</a>',re.DOTALL).findall(OPEN)
    for url,name in Regex:
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,26,ART + 'debrid_tv.jpg',FANART,'')
    np = re.compile('<link rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,25,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Debtv_links(name,url):
    OPEN = Open_Url(url)
    Regex = re.compile('<a href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in Regex:
        if '.rar' not in url:
            name2 = url.split('//')[1].replace('www.','')
            name2 = name2.split('/')[0].split('.')[0].title()
            if '720p' in url:
                name2 = name2 +' [COLOR red] (720p)[/COLOR]'
                if urlresolver.HostedMediaFile(url):
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)
            if '1080p' in url:
                name2 = name2 +' [COLOR red] (1080p)[/COLOR]'
                if urlresolver.HostedMediaFile(url):
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,100,iconimage,FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')
#########################

def nitro_menu():
    addDir('[B][COLOR white]All Movies[/COLOR][/B]','http://loadmovie.biz/',51,ICON,FANART,'')
    OPEN = Open_Url('http://loadmovie.biz')
    Regex = re.compile('<ul id="menu-channels"(.+?)</ul></div>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,51,ICON,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def nitro_content(url):
    referer = url
    headers = {'Host': 'loadmovie.biz', 'User-Agent': User_Agent, 'Referer': referer}
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="post-title text-left">.+?<a href="(.+?)">(.+?)</a>.+?<img src="(.+?)"',re.DOTALL).findall(OPEN)
    for url,name,icon in Regex:
            name = name.replace('2016','(2016)').replace('2015','(2015)').replace('2014','(2014)').replace('2013','(2013)').replace('2012','(2012)').replace('2011','(2011)').replace('&#8217;','\'').replace('&#8212;',' - ')
            if 'Your support | Ask movie' not in name:
                if 'Most Popular Movies In (2017)' not in name:             
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,52,icon,FANART,'')
    np = re.compile('<link rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
        addDir('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,51,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def nitro_links(name,url,iconimage):
    OPEN = Open_Url(url)
    Regex = re.compile('<strong>Quality.+?</strong>(.+?),.+?<a href=.+?href=.+?href=.+?<a href="(.+?)"',re.DOTALL).findall(OPEN)
    for host,url in Regex:
                addDir('[B][COLOR white]Link Quality %s[/COLOR][/B]' %host,BASEURL2+url,100,iconimage,FANART,name)
    Regex1 = re.compile('Quality 1:.+?>(.+?),.+?href=.+?href=.+?href=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for host,url in Regex1:
            host = host.replace('<span class="bbcode-text">','').replace('</span>','')
            addDir('[B][COLOR white]Link Quality %s[/COLOR][/B]' %host,BASEURL2+url,100,iconimage,FANART,name)
    Regex2 = re.compile('Quality 2:.+?>(.+?),.+?href=.+?href=.+?href=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for host,url in Regex2:
            host = host.replace('<span class="bbcode-text">','').replace('</span>','')
            addDir('[B][COLOR white]Link Quality %s[/COLOR][/B]' %host,BASEURL2+url,100,iconimage,FANART,name)
    Regex3 = re.compile('Quality 3:.+?>(.+?),.+?href=.+?href=.+?href=.+?href="(.+?)"',re.DOTALL).findall(OPEN)
    for host,url in Regex3:
                addDir('[B][COLOR white]Link Quality %s[/COLOR][/B]' %host,BASEURL2+url,100,iconimage,FANART,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')

#########################
def Get_shows(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="column-4".+?href=\'(.+?)\'.+?src="(.+?)".+?<h1>(.+?)</h1>',re.DOTALL).findall(OPEN)
    for url,icon,name in Regex:
            url = url.replace('../../../../','http://123moviesonline.co/')
            icon = icon.replace('../../../../','http://123moviesonline.co/')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,21,icon,FANART,'')
    setView('tvshows', 'tvshows-view')

def Get_seasons(url):
    OPEN = Open_Url(url)
    Regex = re.compile('class="list_seasons">(.+?)</div>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)".+?>(.+?)</a>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('../../../../','http://123moviesonline.co/')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,22,iconimage,iconimage,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_episodes(url):
    OPEN = Open_Url(url)
    Regex = re.compile('class="list_episodes"(.+?)</div>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)".+?<h1>(.+?)</h1>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('../../../../','http://123moviesonline.co/')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,200,iconimage,iconimage,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')	
#########################
def Dir_playlist(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<name>(.+?)</name>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(OPEN)
    for name,icon,url,fanart in Regex:
        if 'txt' in url:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,8,icon,fanart,'')
        else:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,icon,fanart,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def Get_playlist(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>',re.DOTALL).findall(OPEN)
    for name,url,icon,fanart in Regex:
        if 'xml' in url:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,7,icon,fanart,'')
        else:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,150,icon,fanart,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
#########################

def UK_soaps():
    addDir('[B][COLOR red]Coronation Street[/COLOR][/B]','https://watchseries-online.pl/category/coronation-street',31,'http://thetvdb.com/banners/_cache/posters/71565-2.jpg','http://thetvdb.com/banners/fanart/original/71565-2.jpg','')
    addDir('[B][COLOR red]Eastenders[/COLOR][/B]','https://watchseries-online.pl/category/eastenders',31,'http://thetvdb.com/banners/_cache/posters/71753-2.jpg','http://thetvdb.com/banners/fanart/original/71753-7.jpg','')
    addDir('[B][COLOR red]Emmerdale[/COLOR][/B]','https://watchseries-online.pl/category/emmerdale',31,'http://thetvdb.com/banners/_cache/posters/77715-2.jpg','http://thetvdb.com/banners/fanart/original/77715-3.jpg','')
    addDir('[B][COLOR red]Casualty[/COLOR][/B]','https://watchseries-online.pl/category/casualty',31,'http://thetvdb.com/banners/_cache/posters/71756-4.jpg','http://thetvdb.com/banners/fanart/original/71756-2.jpg','')
    addDir('[B][COLOR red]Holby City[/COLOR][/B]','https://watchseries-online.pl/category/holby-city',31,'http://thetvdb.com/banners/_cache/posters/77235-1.jpg','http://thetvdb.com/banners/fanart/original/77235-3.jpg','')
    addDir('[B][COLOR red]Hollyoaks[/COLOR][/B]','https://watchseries-online.pl/category/hollyoaks',31,'http://thetvdb.com/banners/_cache/posters/78006-1.jpg','http://thetvdb.com/banners/fanart/original/78006-1.jpg','')
    addDir('[B][COLOR red]Doctors[/COLOR][/B]','https://watchseries-online.pl/category/doctors',31,'http://thetvdb.com/banners/_cache/posters/83729-2.jpg','http://thetvdb.com/banners/fanart/original/83729-1.jpg','')
    addDir('[B][COLOR red]Home & Away[/COLOR][/B]','https://watchseries-online.pl/category/home-and-away',31,'http://thetvdb.com/banners/_cache/posters/71890-2.jpg','http://thetvdb.com/banners/fanart/original/71890-1.jpg','')
    addDir('[B][COLOR red]Neighbours[/COLOR][/B]','https://watchseries-online.pl/category/neighbours',31,'http://thetvdb.com/banners/_cache/posters/76719-2.jpg','http://thetvdb.com/banners/fanart/original/76719-2.jpg','')
    setView('tvshows', 'tvshows-view')
def list_ep(url):
    referer = url
    headers = {'Host': 'watchseries-online.pl', 'User-Agent': User_Agent, 'Referer': referer}
    OPEN = Open_Url(url)
    Regex = re.compile("listEpisode.+?href='(.+?)'.+?</span>(.+?)</a>",re.DOTALL).findall(OPEN)
    for url,name in Regex:
            name = name.replace('&#8211;','-')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,32,iconimage,iconimage,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')    

def list_li(name,url):
    referer = url
    headers = {'Host': 'watchseries-online.pl', 'User-Agent': User_Agent, 'Referer': referer}
    OPEN = Open_Url(url)
    Regex = re.compile('<img class="host-icon".+?href="(.+?)">(.+?)</a>',re.DOTALL).findall(OPEN)
    for url,name2 in Regex:
            if urlresolver.HostedMediaFile(url).valid_url():
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name2,url,100,iconimage,iconimage,name)
    xbmc.executebuiltin('Container.SetViewMode(50)')    
#########################
def hdtv_menu():
    addDir('[B][COLOR blue]Popular Shows[/COLOR][/B]','http://cooltvseries.com/popular-tv-shows/',71,ART + 'hdtvshows.jpg',FANART,'')
    addDir('[B][COLOR blue]Latest Episodes[/COLOR][/B]','http://cooltvseries.com/moreupdates/',74,ART + 'hdtvshows.jpg',FANART,'')
    addDir('[B][COLOR blue]Alphabetically[/COLOR][/B]','',72,ART + 'hdtvshows.jpg',FANART,'')
    addDir('[B][COLOR red]Search HDTV[/COLOR][/B]','url',77,ART + 'hdtvshows.jpg',FANART,'')
    OPEN = Open_Url('http://cooltvseries.com/popular-tv-shows/')
    Regex = re.compile('<h3 class="sidebar-title">Browse By Category</h3>(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('https','http')
            if 'Documentary' not in name:
                if 'Music' not in name:
                    if 'Sport' not in name:
                        if 'War' not in name:
                            if 'Western' not in name:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,71,ART + 'hdtvshows.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def hdtv_genres():
    OPEN = Open_Url('http://cooltvseries.com/popular-tv-shows/')
    Regex = re.compile('<h3 class="sidebar-title">Browse By Category</h3>(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('https','http')
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,71,ICON,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def hdtv_alpha():
    OPEN = Open_Url('http://cooltvseries.com/popular-tv-shows/')
    Regex = re.compile('<h3 class="sidebar-title">Browse By Alphabetically</h3>(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</a></li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('https','http')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,71,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def hdtv_Get_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="box">.+?<img src="(.+?)".+?<a href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
            url = url.replace('https','http')
            icon = icon.replace('//','http://')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,75,icon,FANART,'')
    np = re.compile('<li class="next"><a href="(.+?)"',re.DOTALL).findall(OPEN)
    for url in np:
            url = url.replace('https','http')
            addDir('[B][COLOR blue]Next Page>>>[/COLOR][/B]',url,71,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(500)')
    
def hdtv_latest_ep(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="box">.+?<img src="(.+?)".+?<a href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
            url = url.replace('https','http')
            icon = icon.replace('//','http://')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,80,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def hdtv_Get_seasons(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="dwn-box">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)</li>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('https','http')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,76,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
	
def hdtv_Get_episodes(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="dwn-box">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<li><a href="(.+?)">(.+?)<span',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            url = url.replace('https','http')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,80,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def hdtv_Search():
        keyb = xbmc.Keyboard('', 'Search')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = BASEURL3 + 'search.php?search=' + search
                hdtv_search_res(url)

def hdtv_search_res(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="box">.+?<img src="(.+?)".+?<a href="(.+?)" title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
            url = url.replace('https','http')
            icon = icon.replace('//','http://')
            addDir('[B][COLOR blue]%s[/COLOR][/B]' %name,url,76,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')  

#########################
def doc_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="sitemap-wraper clear">.+?</h2>(.+?)</div>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('<a href="(.+?)" title="(.+?)"><img.+?src="(.+?)".+?</a>',re.DOTALL).findall(str(Regex))
    for url,name,icon in Regex2:
            name=name.replace('&#039;','\'')
            icon=icon.replace('-150x198','')
            addDir(name,url,150,icon,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
###############################
def get_yt_pl(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<title>(.+?)</title>.+?thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(OPEN)
    for name,icon in Regex:
        artist = name 
        artist = artist.replace('[COLOR yellow]','').replace('[/COLOR]','').replace(' ','+')
        url = 'https://www.youtube.com/results?sp=EgIQAw%253D%253D&q=' + artist
        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,90,icon,'http://4.bp.blogspot.com/-12AKy09uxnE/U7HMVz_zn3I/AAAAAAAAPiU/P_zI8X7oeAU/s1600/AT1.JPG','')
    xbmc.executebuiltin('Container.SetViewMode(50)')
	
def kids_yt(url):
    OPEN = Open_Url(url)
    Regex = re.compile('="https://i.ytimg.com/(.+?)".+?<span class="formatted-video-count-label"><b>(.+?)</b>.+?data-list-id="(.+?)".+?title=.+?title="(.+?)"',re.DOTALL).findall(OPEN)
    for icon,count,url,name in Regex:
            amount = int(count)
            name=name.replace('amp;','').replace('&quot;','').replace('&#39;','\'').title()
            name=name +'  [B][COLOR red]('+count+')'
            if amount <250:
               addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,91,'https://i.ytimg.com/%s'%icon,'http://4.bp.blogspot.com/-12AKy09uxnE/U7HMVz_zn3I/AAAAAAAAPiU/P_zI8X7oeAU/s1600/AT1.JPG','')
    np = re.compile('<a href="(.+?)".+?<span class="yt-uix-button-content">(.+?)</span>',re.DOTALL).findall(OPEN)
    for url,name in np:
            if 'Next' in name:
                url=url.replace('amp;','')
                addDir('[B][COLOR red]Next Page>>>[/COLOR][/B]','https://www.youtube.com%s'%url,90,ART + 'nextpage.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')
	
def Res_kids_yt(url):
        url = 'plugin://plugin.video.youtube/play/?playlist_id=' + url + '&order=default'
        liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)    
    
    
    

#########################
def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link
    xbmcplugin.endOfDirectory(int(sys.argv[1]))




def addDir(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==100 or mode==150 or mode==200 or mode==80 or mode==91:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def resolve(name,url,iconimage,description):
    if 'loadmovie.biz' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location'] 
            stream_url=urlresolver.HostedMediaFile(url).resolve()

    else:   
        stream_url=urlresolver.HostedMediaFile(url).resolve()
        
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def alt_resolve(url):
    if 'dailymotion' in url:
            xbmc.log(url)
            OPEN = Open_Url(url)
            try:
                    url = re.compile('"video\\\/mp4","url":"(.*?)"',re.DOTALL).findall(OPEN)[-1]
            except:
                    url = re.compile('"video\\\/mp4","url":"(.*?)"',re.DOTALL).findall(OPEN)[0]
            url = url.replace('\/','/')
            stream_url=url
    elif 'topdocumentaryfilms' in url:
            OPEN = Open_Url(url)
            url = re.compile('<meta itemprop="embedUrl" content="(.+?)"',re.DOTALL).findall(OPEN)[0]
            if 'vimeo' in url:
                url = url.replace('https://player.vimeo.com/video/','plugin://plugin.video.vimeo/play/?video_id=')
                stream_url=url
            else:
                url = url.replace('https://www.youtube.com/embed/','plugin://plugin.video.youtube/play/?video_id=')
                stream_url=url
    elif 'video.youtube' in url:
            stream_url=url
        
    else:   
            stream_url=urlresolver.resolve(url)
    
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def resolvetv(name,url,iconimage,description):
    OPEN = Open_Url(url)
    url = re.compile('<iframe src="(.+?)"',re.DOTALL).findall(OPEN)[0]    
    stream_url=urlresolver.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def hdtv_resolve(name,url,iconimage,description):
    OPEN = Open_Url(url)
    try:
        url = re.compile('href="https://cooltvseries.com/dl/(.+?)"',re.DOTALL).findall(OPEN)[-1]
        url = 'http://cooltvseries.com/dl/' + url
        headers = {'User-Agent': User_Agent}
        r = requests.get(url,headers=headers,allow_redirects=False)
        url = r.headers['location']
        url = url.replace(' ','%20')        
    except:
        url = re.compile('href="https://cooltvseries.com/dl/(.+?)"',re.DOTALL).findall(OPEN)[0]
        url = 'http://cooltvseries.com/dl/' + url
        headers = {'User-Agent': User_Agent}
        r = requests.get(url,headers=headers,allow_redirects=False)
        url = r.headers['location']
        url = url.replace(' ','%20')

    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
def setView(content, viewType):
	if content:
		xbmcplugin.setContent(int(sys.argv[1]), content)
	if addon.get_setting('auto-view') == 'true':
		xbmc.executebuiltin("Container.SetViewMode(%s)" % addon.get_setting(viewType) )		

def OPEN_UrlRez():
        xbmcaddon.Addon('script.module.urlresolver').openSettings()
        
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

params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
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
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#########################################################

if mode == None: Main_menu()
elif mode == 5 : Get_content(url)
elif mode == 10 : Get_links(name,url)
elif mode == 8 : Dir_playlist(url)
elif mode == 7 : Get_playlist(url)
elif mode == 20 : Get_shows(url)
elif mode == 22 : Get_episodes(url)
elif mode == 21 : Get_seasons(url)
elif mode == 25 : Debtv_content(url)
elif mode == 26 : Debtv_links(name,url)
elif mode == 30 : UK_soaps()
elif mode == 31 : list_ep(url)
elif mode == 32 : list_li(name,url)
elif mode == 50 : nitro_menu()
elif mode == 51 : nitro_content(url)
elif mode == 52 : nitro_links(name,url,iconimage)
elif mode == 60 : doc_content(url)
elif mode == 70 : hdtv_menu()
elif mode == 71 : hdtv_Get_content(url)
elif mode == 72 : hdtv_alpha()
elif mode == 73 : hdtv_genres()
elif mode == 74 : hdtv_latest_ep(url)
elif mode == 75 : hdtv_Get_seasons(url)
elif mode == 76 : hdtv_Get_episodes(url)
elif mode == 77 : hdtv_Search()
elif mode == 80 : hdtv_resolve(name,url,iconimage,description)
elif mode == 89 : get_yt_pl(url)
elif mode == 90 : kids_yt(url)
elif mode == 91 : Res_kids_yt(url)
elif mode == 100 : resolve(name,url,iconimage,description)
elif mode == 150 : alt_resolve(url)
elif mode == 200 : resolvetv(name,url,iconimage,description)
elif mode == 250: OPEN_UrlRez()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
