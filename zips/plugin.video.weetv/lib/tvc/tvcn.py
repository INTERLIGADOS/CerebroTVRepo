'''
    weeTV
    Twitter @geeteetv
    
    based on TVCatchup.com Add-on
    Copyright (C) 2017 BludhavenGrayson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import urllib
import urllib2
import re
import xbmcplugin
import xbmcgui
import xbmcvfs
import os
import sys
import datetime
import string
import hashlib
#import net
from lib import net
import xbmc
import xbmcaddon

import re,requests
from lib.tvc.common import *
from lib.tvc.plugintools import *

icon      = xbmc.translatePath(os.path.join('https://pbs.twimg.com/profile_images/461806017894825985/KhAibdjx_400x400.jpeg', 'icon.jpg'))
fanart    = xbmc.translatePath(os.path.join('http://www.geetee.site/wizchannels/images/england.png', 'fanart.jpg'))

        
def tvc_next(): 
    url9       = 'http://tvcatchup.com/next'
    iconimage = ""
    req       = urllib2.Request(url9)
    req.add_header('Referer', 'http://www.google.com')
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    #req       = urllib2.Request(url)   
    response  = urllib2.urlopen(req)
    link      = response.read()
    #xbmc.log('Response: %s' % response,  xbmc.LOGNOTICE)   
    #xbmc.log('Response: %s' % link,  xbmc.LOGNOTICE)   
    response.close()
    pattern = ""
    matches = plugintools.find_multiple_matches(link,'<div class="channelsHolder".+?>(.*?)</div>')
    xbmc.log('MATCHES: %s' % matches,  xbmc.LOGNOTICE)    
    for entry in matches:      
        getchannel = plugintools.find_single_match(entry,'alt="Watch (.+?)"')
        gettitle   = plugintools.find_single_match(entry,'<br/> (.+?) </a>').replace("&amp;","&")
        name       = getchannel+' - '+gettitle
        geturl     = plugintools.find_single_match(entry,'<a href="(.+?)"')
        url        = 'http://tvcatchup.com' + geturl
        iconimage  = plugintools.find_single_match(entry,'src="(.+?)"')
        addLink(name,url,316,iconimage)
        xbmc.log('TVCNEXTE: %s' % name,  xbmc.LOGNOTICE)

 
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
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        tvc_next()
xbmcplugin.endOfDirectory(int(sys.argv[1]))
