import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcvfs,os,sys,datetime,string,hashlib,net
from resources.lib.modules.plugintools import *
import xbmcaddon
import json
from cookielib import CookieJar
from resources.lib.modules.common import *

def	vod_itv_shows():
	url   = 'https://www.itv.com/hub/shows'
	link  = open_url(url)
	link  = link
	
	matches = plugintools.find_multiple_matches(link,'<li class="grid-list__item width--one-half width--custard--one-third js-lazy">(.*?)</li>')
	
	for entry in matches:
	   
		name	  = plugintools.find_single_match(entry,'<h3 class="tout__title complex-link__target theme__target">(.+?)</h3>').replace('\n','').replace('							','').replace('						','').replace('					','')
		url	   = plugintools.find_single_match(entry,'<a href="(.+?)"')
		iconimage = plugintools.find_single_match(entry,'<img class="fluid-media__media" src="(.+?)"').replace('w=276&amp;h=156','w=1280&h=720').replace('&amp;','&')
		
		addDir(name,url,16,iconimage)
		xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
		xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
		
def	vod_itv_episodes(url):
	url   = url
	link  = open_url(url)
	link  = link
	
	matches = plugintools.find_multiple_matches(link,'<li class="grid-list__item width--one-half width--custard--one-third js-lazy">(.*?)</li>')
	
	for entry in matches:
	   
		name	  = plugintools.find_single_match(entry,'<h3 class="tout__title complex-link__target theme__target">(.+?)</h3>').replace('\n','').replace('							','').replace('						','').replace('					','')
		url	   = plugintools.find_single_match(entry,'<a href="(.+?)"')
		iconimage = plugintools.find_single_match(entry,'<img class="fluid-media__media" src="(.+?)"').replace('w=276&amp;h=156','w=1280&h=720').replace('&amp;','&')
		
		addDir(name,url,14,iconimage)
		xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
		xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
		
