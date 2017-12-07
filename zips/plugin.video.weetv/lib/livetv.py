# -*- coding: utf-8 -*-

import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, xbmcaddon, json, time, process, requests
from threading import Thread
from lib import net

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


        
def aiptvuk():
    open = OPEN_URL('http://autoiptv.net/playlist.php')
    regex = re.compile('#EXTINF:.+?DOM",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(open)
    for name,url in regex:
        addDir(name,url,3,uk_icon,uk_fan,'') 
        
def aiptvca():
    open = OPEN_URL('http://autoiptv.net/playlist.php')
    regex = re.compile('#EXTINF:.+?ADA",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(open)
    for name,url in regex:
        addDir(name,url,3,ca_icon,ca_fan,'') 

def aiptvus():
    open = OPEN_URL('http://autoiptv.net/playlist.php')
    regex = re.compile('#EXTINF:.+?TATES",(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL).findall(open)
    for name,url in regex:
        addDir(name,url,3,us_icon,us_fan,'')        
                
def ca3u():
    open = OPEN_URL('https://pastebin.com/raw/iE0ND2zW')
    regex = re.compile ('#EXTINF:.+\,(.+)\n(.+)\n', re.MULTILINE|re.IGNORECASE).findall(open)
    for name,url in sorted(regex):
        addDir(name,url,3,ca_icon,ca_fan,'') 
        
def usbasic():
    open = OPEN_URL('https://pastebin.com/raw/2fHp5ei9')
    regex = re.compile ('#EXTINF:.+\,(.+)\n(.+)\n', re.MULTILINE|re.IGNORECASE).findall(open)
    for name,url in sorted(regex):
        addDir(name,url,3,us_icon,us_fan,'') 

def weeus():
    open = OPEN_URL('https://pastebin.com/raw/tBNq0Xnd')
    regex = re.compile ('#EXTINF:.+\,(.+)\n(.+)\n', re.MULTILINE|re.IGNORECASE).findall(open)
    for name,url in sorted(regex):
        addDir(name,url,3,us_icon,us_fan,'') 
        
def weeuk():
    open = OPEN_URL('https://pastebin.com/raw/JwN77Hd5')
    regex = re.compile ('#EXTINF:.+\,(.+)\n(.+)\n', re.MULTILINE|re.IGNORECASE).findall(open)
    for name,url in sorted(regex):
        addDir(name,url,3,uk_icon,uk_fan,'')        
               
def newscbc():
    open = OPEN_URL('https://pastebin.com/raw/k4Q6Hkxc')
    all  = regex_get_all(open,'<item>','</item>')
    for a in (all):
        name = regex_from_to(a,'<title>','</title>')    
        url  = regex_from_to(a,'<link>','</link>')
        thumb  = regex_from_to(a,'<thumbnail>','</thumbnail>')
        fanart  = regex_from_to(a,'<fanart>','</fanart>')
        addDir(name,url,3,cbc,news_fan,'')      
        
def news():
    open = OPEN_URL('https://pastebin.com/raw/t865iYpv')    
    regex = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(open)
    for name,url in sorted(regex):
        addDir(name,url,3,news_icon,news_fan,'')

def fluxus():
    open  = OPEN_URL('https://raw.githubusercontent.com/fluxustv/IPTV/master/list.m3u')
    #regex = re.compile ('#EXTINF:.+?("USA",|"UK",)(.*?)\n(.+?)\n', re.MULTILINE|re.IGNORECASE).findall(open) 
    regex = re.compile ('#EXTINF:.+?("USA",)(.*?)\n(.+?)\n', re.MULTILINE|re.IGNORECASE).findall(open) 
    for null,name,url in sorted(regex):
        addDir(name,url,9999,icon,us_fan,'')  
        
#########################################
def regex_get_all(text, start_with, end_with):
    import re,string
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r  

def regex_from_to(text, from_string, to_string, excluding=True):
    import re,string
    if excluding:
        try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
        except: r = ''
    else:
        try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
        except: r = ''
    return r
            
def OPEN_URL(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    link = requests.session().get(url, headers=headers, verify=False).text
    link = link.encode('ascii', 'ignore')
    return link         
    
def addDir(name,url,mode,iconimage,fanart,description):
    import xbmcgui,xbmcplugin,urllib,sys
    u=sys.argv[0]+"?url="+url+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==9999:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
    xbmcplugin.endOfDirectory   
######

