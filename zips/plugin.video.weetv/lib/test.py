# -*- coding: utf-8 -*-

import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time, process, requests,re,sys,datetime,shutil,urlresolver,random,liveresolver
from threading import Thread
from lib.common_addon import Addon
import base64
from metahandler import metahandlers
from lib import dom_parser


ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.weetv/')
ICON = ADDON_PATH + 'icon.png'
icon = ADDON_PATH + 'icon.png'
FANART = ADDON_PATH + 'fanart.jpg'
fanart = ADDON_PATH + 'fanart.jpg'
addon_handle = int(sys.argv[1])
List = []
IMDB = 'http://www.imdb.com'
base_icons = 'http://www.geetee.site/wizchannels/images/'
ca_us_icon = base_icons + 'ca_us.png'
ca_icon = base_icons + 'ca.png'
us_icon = base_icons + 'us.png'
uk_icon = base_icons + 'gb.png'
sports_icon = base_icons + 'sports.png'
news_icon = base_icons + 'news.png'
news_fan = base_icons + 'newsshow.jpg'
ca_fan = base_icons + 'beaver.jpg'
uk_fan = base_icons + 'derwentwater.jpg'
us_fan = base_icons + 'usflag.jpg'
sport_fan = base_icons + 'sport.jpg'
cbc = 'http://www.geetee.site/wizchannels/images/cbc.png'
####
baseurl = 'https://pastebin.com/raw/Mbhj7Gpi'
#baseurl = 'https://pastebin.com/raw/Kf8yMGA9'

######
def test_Main_Menu(url):
    #process.Menu('Top TV Schedule','http://www.tvmaze.com/calendar',6,ICON,FANART,'','')
    #process.Menu('TV Networks','http://www.tvmaze.com/networks',4,ICON,FANART,'','') 
    #process.Menu('menu xml','',499,'','','','')
    process.Menu('Menu xmlPB','',411,'','','','')     
    process.Menu('weeTV Shows','http://www.imdb.com/list/ls025776108/',16,'','','','')                                          
    #process.Menu('IMDB Top 100 Programs','http://www.imdb.com/chart/tvmeter?ref_=m_nv_ch_tvm',301,ICON,FANART,'','')
    #process.Menu('IMDB Top Rated Shows','http://www.imdb.com/chart/toptv?pf_rd_m',301,ICON,FANART,'','')    
    #process.Menu('####################','','','','','','')          
    #process.Menu('My Watched Shows','',18,'','','','')
    #process.Menu('Latest Episodes','',19,'','','','')
    #process.Menu('Watched Shows item','',21,'','','','')   
    process.Menu('Favourites','',10,'','','','')                        
    process.Menu('Search','',308,ICON,FANART,'','')
    
    xbmcplugin.endOfDirectory(int(sys.argv[1])) 
	
def aiptvuk():
    open = OPEN_URL('http://autoiptv.net/playlist.php')
    regex = re.compile('#EXTINF:.+?DOM",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(open)
    for name,url in regex:
        addDir(name,url,3,uk_icon,uk_fan,'') 	
	
def GetMenuX():
     url = baseurl
     link=open_url(baseurl)
     match= re.compile('<item>(.+?)</item>').findall(link)
     for item in match:
         try:
            if '<channel>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                    addDir(name,url,56,iconimage,fanart)
            elif '<playlist>' in item:
                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                    url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                    addDir(name,url,543,iconimage,fanart)                    
            if '<sportsdevil>' in item:
                    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                    if len(links)==1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                         url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                         referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                         check = referer
                         suffix = "/"
                         if not check.endswith(suffix):
                             refer = check + "/"
                         else:
                             refer = check
                         link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                         url = link + '%26referer=' +refer
                         addItem(name,url,54,iconimage,fanart)   
                    elif len(links)>1:
                         name=re.compile('<title>(.+?)</title>').findall(item)[0]
                         iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                         fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                         addItem(name,url2,58,iconimage,fanart)       
            elif '<folder>'in item:
                            data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                            for name,url,iconimage,fanart in data:
                                    addDir(name,url,51,iconimage,fanart)
            else:
                            links=re.compile('<link>(.+?)</link>').findall(item)
                            if len(links)==1:
                                    data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                    lcount=len(match)
                                    for name,url,iconimage,fanart in data:
                                            if 'youtube.com/playlist' in url:
                                                    addDir(name,url,52,iconimage,fanart)
                                            else:
                                                    addLink(name,url,52,iconimage,fanart)
                            elif len(links)>1:
                                    name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                    addLink(name,url2,53,iconimage,fanart)
         except:pass
         view(link)
     #addDir('[B][COLOR yellow]~Search~[/COLOR][/B]',url,55,searchicon,fanarts)

def GetContentX(name,url,iconimage,fanart):
        url2=url
        link=open_url(url)

        match= re.compile('<item>(.+?)</item>').findall(link)
        for item in match:
            try:
                if '<channel>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<channel>(.+?)</channel>').findall(item)[0]
                        addDir(name,url,56,iconimage,fanart)
                elif '<playlist>' in item:
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        url=re.compile('<playlist>(.+?)</playlist>').findall(item)[0]
                        addDir(name,url,543,iconimage,fanart)
                elif ('<sportsdevil>' in item) and ('<link>' in item):
                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                        addItem(name,url2,58,iconimage,fanart)
                if '<sportsdevil>' in item:
                        links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
                        if len(links)==1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                             url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                             referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                             check = referer
                             suffix = "/"
                             if not check.endswith(suffix):
                                 refer = check + "/"
                             else:
                                 refer = check
                             link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' +url
                             url = link + '%26referer=' +refer
                             addItem(name,url,54,iconimage,fanart)   
                        elif len(links)>1:
                             name=re.compile('<title>(.+?)</title>').findall(item)[0]
                             iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                             fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                             addItem(name,url2,58,iconimage,fanart)
    
                elif '<folder>'in item:
                                data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                for name,url,iconimage,fanart in data:
                                        addDir(name,url,1,iconimage,fanart)
                else:
                                links=re.compile('<link>(.+?)</link>').findall(item)
                                if len(links)==1:
                                        data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                                        lcount=len(match)
                                        for name,url,iconimage,fanart in data:
                                                if 'youtube.com/playlist' in url:
                                                        addDir(name,url,52,iconimage,fanart)
                                                else:
                                                        addLink(name,url,52,iconimage,fanart)
                                elif len(links)>1:
                                        name=re.compile('<title>(.+?)</title>').findall(item)[0]
                                        iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                                        fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                                        addLink(name,url2,53,iconimage,fanart)
            except:pass
            view(link)

def YOUTUBE_CHANNEL(url):
	CHANNEL = RUNNER + url
	link = open_url(CHANNEL)
	patron = "<video>(.*?)</video>"
	videos = re.findall(patron,link,re.DOTALL)
	items = []
	for video in videos:
		item = {}
		item["name"] = find_single_match(video,"<name>([^<]+)</name>")
		item["url"] = base64.b64decode(b"cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUvcGxheS8/dmlkZW9faWQ9") + find_single_match(video,"<id>([^<]+)</id>")
		item["author"] = find_single_match(video,"<author>([^<]+)</author>")
		item["iconimage"] = find_single_match(video,"<iconimage>([^<]+)</iconimage>")
		item["date"] = find_single_match(video,"<date>([^<]+)</date>")
		
		addLink('[COLOR white]' + item["name"] + ' - on ' + item["date"] + '[/COLOR]',item["url"],57,item["iconimage"],fanart)
	
def CLEANUP(text):
    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />','\n')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&#39;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&#8211;',"&")
    text = text.replace('&#8217;',"'")
    text = text.replace('&#038;',"&")
    text = text.replace('&nbsp;'," ")
    text = text.lstrip(' ')
    text = text.lstrip('    ')
    
def GETMULTI(name,url,iconimage):   
    streamurl=[]
    streamname=[]
    streamicon=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    links=re.compile('<link>(.+?)</link>').findall(urls)
    i=1
    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )
                i=i+1
    name='[COLOR yellow]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
		quit()
    else:
		url = streamurl[select]
		print url
		if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
                elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
                else: stream_url=url
                liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
                liz.setPath(stream_url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                
def GETMULTI_SD(name,url,iconimage):
    sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='
    streamurl=[]
    streamname=[]
    streamicon=[]
    streamnumber=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(urls)
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    i=1
    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                        streamnumber.append('Stream ' + str(i))
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )
                i=i+1
    name='[COLOR yellow]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        check = streamname[select]
        suffix = "/"
        if not check.endswith(suffix):
              refer = check + "/"
        else:
              refer = check
        url = sdbase + streamurl[select] + "%26referer=" + refer
        print url

        xbmc.Player().play(url)

def PLAYSD(name,url,iconimage):    
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        xbmc.Player ().play(url, liz, False)
        
def PLAYLINK(name,url,iconimage):
    if 'youtube.com/playlist' in url:
        searchterm = url.split('list=')[1]
        ytapi = ytpl + searchterm + ytpl2
        req = urllib2.Request(ytapi)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link = link.replace('\r','').replace('\n','').replace('  ','')     
        match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
        try:
            np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
            ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
            addDir('Next Page >>',ytapi,2,nextpage,fanart)
        except:pass
        for name,ytid in match:
            url = 'https://www.youtube.com/watch?v='+ytid
            iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
            if not 'Private video' in name:
                if not 'Deleted video' in name:
                    addLink(name,url,52,iconimage,fanart)

    if 'https://www.googleapis.com/youtube/v3' in url:
            searchterm = re.compile('playlistId=(.+?)&maxResults').findall(url)[0]
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            link = link.replace('\r','').replace('\n','').replace('  ','')     
            match=re.compile('"title": "(.+?)".+?"videoId": "(.+?)"',re.DOTALL).findall(link)
            try:
                    np=re.compile('"nextPageToken": "(.+?)"').findall(link)[0]
                    ytapi = ytplpg1 + np + ytplpg2 + searchterm + ytplpg3
                    addDir('Next Page >>',ytapi,52,nextpage,fanart)
            except:pass
 
            for name,ytid in match:
                    url = 'https://www.youtube.com/watch?v='+ytid
                    iconimage = 'https://i.ytimg.com/vi/'+ytid+'/hqdefault.jpg'
                    if not 'Private video' in name:
                            if not 'Deleted video' in name:
                                    addLink(name,url,52,iconimage,fanart)
    
    if urlresolver.HostedMediaFile(url).valid_url(): stream_url = urlresolver.HostedMediaFile(url).resolve()
    elif liveresolver.isValid(url)==True: stream_url=liveresolver.resolve(url)
    else: stream_url=url
    liz = xbmcgui.ListItem(name,iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setPath(stream_url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

    if 'http' not in url:
        if '.ts'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url
        elif 'acestream' in url:
            url = "plugin://program.plexus/?url=" + url + "&mode=1&name=acestream+"
            xbmc.Player ().play(url)
        elif urlresolver.HostedMediaFile(url).valid_url():
            url = urlresolver.HostedMediaFile(url).resolve()           
        elif liveresolver.isValid(url)==True:
                url=liveresolver.resolve(url)
        liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        xbmc.Player ().play(url, liz, False)
        quit()
                            
def PLAYVIDEO(url):
	xbmc.Player().play(url)

def open_url(url):
    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'klopp')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')
        print link
        return link
    except:quit()

def open_url2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'klopp')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        print link
        return link
 
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


def addLinkMeta(name,url,mode,iconimage,itemcount,isFolder=False):
        splitName=name.partition('(')
	simplename=""
	simpleyear=""
	if len(splitName)>0:
                simplename=splitName[0]
		simpleyear=splitName[2].partition(')')
	if len(simpleyear)>0:
		simpleyear=simpleyear[0]
	mg = metahandlers.MetaData()
	meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
	liz.setInfo( type="Video", infoLabels= meta )
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(contextMenuItems, replaceItems=False)
	if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
	else: liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
	return ok
	
def addDir(name,url,mode,iconimage,fanart,description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
    liz.setProperty('fanart_image', fanart)
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name, url, mode, iconimage, fanart, description=''):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', fanart)
    liz.setProperty("IsPlayable","true")
    if 'plugin://' in url:u=url
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok
    
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)
    
def YOUTUBE_PLAYLIST(url):
    link = open_url(url)
    match = re.compile('yt-lockup-playlist yt-lockup-grid"(.+?)<div class="yt-lockup-meta">').findall(link)
    for links in match:
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        icon = re.compile ('data-thumb="(.+?)"').findall(links)[0].replace('&amp;', '&')
        title = re.compile ('<div class="yt-lockup-content">.+?title="(.+?)"').findall(links)[0]
        title = CLEANUP(title)
        if not 'http' in url:
            url1 = 'https://www.youtube.com/' + url
            addDir("[COLOR skyblue][B]" + title + "[/B][/COLOR]",url1,543,icon,fanart)
    SET_VIEW()

def YOUTUBE_PLAYLIST_PLAY(url):
    link = open_url(url)
    match = re.compile('<li class="yt-uix-scroller-scroll-unit(.+?)<span class="vertical-align">').findall(link)
    for links in match:
        title = re.compile ('video-title="(.+?)"',re.DOTALL).findall(links)[0]
        title = CLEANUP(title)
        icon = re.compile ('url="(.+?)"',re.DOTALL).findall(links)[0].replace('&amp;', '&')
        fanart = re.compile ('url="(.+?)"',re.DOTALL).findall(links)[0].replace('&amp;', '&')
        url = re.compile ('<a href="(.+?)"').findall(links)[0]
        if not 'http' in url:
            if not 'Deleted video' in title:
                url1 = 'https://www.youtube.com' + url
                addLink("[COLOR yellow][B]" + title + "[/B][/COLOR]",url1,52,icon,fanart)

def addItem(name,url,mode,iconimage,fanart, description=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty( "Fanart_Image", fanart )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def find_single_match(text,pattern):
    result = ""
    try:    
        single = re.findall(pattern,text, flags=re.DOTALL)
        result = single[0]
    except:
        result = ""
    return result

def view(link):
        try:
                match= re.compile('<layouttype>(.+?)</layouttype>').findall(link)[0]
                if layout=='thumbnail': xbmc.executebuiltin('Container.SetViewMode(500)')              
                else:xbmc.executebuiltin('Container.SetViewMode(50)')  
        except:pass
		
