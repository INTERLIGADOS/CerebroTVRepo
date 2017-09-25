import sys
import xbmcgui
import xbmcplugin
import re


import urllib2
request = urllib2.Request("http://vodlocker.to/embed?t=deadpool&chromecast=0&trailer=0&referrer=link&server=alternate")

request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')
request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')


request.get_header('Accept')
request.get_header('User-Agent')

response = urllib2.urlopen(request).read()

getmurl = response

getit = re.compile("hostname.+?<a href='(.+?)'").findall(getmurl)[0]

#import xbmc
#xbmc.Player().play(getit)

dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]TEST[/COLOR]",getit,"WORK??")
xbmc.sleep(15000) 


#xbmc.Player().play(url)