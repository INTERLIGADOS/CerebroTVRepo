# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os,xbmcaddon
from addon.common.addon import Addon
import shutil,xbmcvfs
addon_id='plugin.video.openloadmovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
PATH = 'openloadmovies'
VERSION = ADDON.getAddonInfo('version')
ART = ADDON_PATH + "/resources/icons/"

def Main_menu():
    line1 = "[B][COLOR red]This addon is no longer supported or in use[/COLOR][/B]"
    line2 = "[B]And Will Now Delete itself[/B]"
    line3 = "[B]Thanks for using , Dandymedia[/B]"
    line4 = "[B]Addon Has Been Removed[/B]"
    line5 = "[B]Successfully, Thanks[/B]"
    xbmcgui.Dialog().ok(addon_name, line1, line2, line3)
    delete_addon = xbmc.translatePath('special://home/addons/'+addon_id)
    shutil.rmtree(delete_addon, ignore_errors=True)
    dialog = xbmcgui.Dialog()
    addon.log('===DELETING===ADDON===')
    xbmcgui.Dialog().ok(addon_name, line4, line5)

    
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
xbmcplugin.endOfDirectory(int(sys.argv[1]))
