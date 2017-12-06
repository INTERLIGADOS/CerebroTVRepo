#-*- coding: utf-8 -*-

import urllib2,xbmc, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
import six          
from resources.lib.statistic import cStatistic
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.guiElement import cGuiElement

from resources.lib.gui.gui import cGui
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.config import cConfig
from resources.lib.db import cDb
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
import thread
import pytz
import pyjsparser
import tzlocal
import requests
import js2py
import  xbmc
import urllib
import urllib2
import re,threading
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import urllib, urllib2, re, sys, os
import xbmcplugin, xbmcgui
import urlparse
import codecs
import xbmcaddon
import xbmc
import base64
import ngx
import pickle
import src
from urlparse import parse_qs
import hashlib
from urllib import unquote_plus

import urlparse,sys,re,xbmcgui,os
import pyxbmct
pyxbmct = pyxbmct.addonwindow
         
#SITE_IDENTIFIER = addonDir
import cookielib,base64
iconimage=None
from resources.lib import comon
from resources.lib import logger
stopEvent=None
g_stopEvent=None
g_downloader=None
g_currentprocessor=None
proxy=None
use_proxy_for_chunks=False
maxbitrate=0
simpleDownloader=False 
auth=None 
streamtype='HLSRETRY'
setResolved=False
swf=None  
callbackpath=""
callbackparam="" 
iconImage="DefaultVideo.png"

playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)

AddonID = 'plugin.video.OTV_MEDIA'
Addon = xbmcaddon.Addon(AddonID)
localizedString = Addon.getLocalizedString
AddonName = Addon.getAddonInfo("name")
icon = Addon.getAddonInfo('icon')
addon_version = Addon.getAddonInfo('version')
addonDir = Addon.getAddonInfo('path')
addon_data_dir = os.path.join(xbmc.translatePath("special://userdata/addon_data" ), AddonID)
pwdir = os.path.join(addon_data_dir, "password")
cdir = os.path.join(xbmc.translatePath("special://temp"),"files")
debug = Addon.getSetting('debug')
profile = xbmc.translatePath(Addon.getAddonInfo('profile').decode('utf-8'))
FANART = os.path.join(addonDir, 'fanart.jpg')
functions_dir = profile
      
LOCAL_VERSION_FILE = os.path.join(os.path.join(addonDir), 'version.xml' )
REMOTE_VERSION_FILE = "https://dl.dropboxusercontent.com/s/oplxddyhwh2b5gj/version.xml"

LOCAL_VERSION_FILE2 = os.path.join(os.path.join(addonDir), 'list.xml' )
REMOTE_VERSION_FILE2 = "https://dl.dropboxusercontent.com/s/hjdh08whb1l83jt/list.xml"
                              
libDir = os.path.join(addonDir, 'resources', 'lib')
f4mProxy = os.path.join(addonDir, 'f4mProxy')
chanDir = os.path.join(addonDir, 'resources', 'channels')
#XML_FILE  = os.path.join(libDir, 'advancedsettings.xml' )
#ACTIVESETTINGSFILE = os.path.join(xbmc.translatePath('special://profile'), 'advancedsettings.xml')
playlistsFile = os.path.join(addonDir, "playLists.txt")
xbmcPlayer = xbmc.Player()
playList = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
Turkish = os.path.join(addonDir, "turkish.txt")


French = os.path.join(addonDir, "french.txt")
German = os.path.join(addonDir, "german.txt")
English = os.path.join(addonDir, "english.txt")

EXTL = [ '.m3u', '.m3u8', '.txt']
EXTV = [ '.mkv','.mp4','.avi','.ogv','.flv','.f4v','.wmv','.mpg','.mpeg','.3gp','.3g2','.webm','.ogg' ]
EXTA = [ '.mp3','.flac','.aac','.wav','.raw','.m4a','.wma','.f4a' ]
iconlist = "http://findicons.com/files/icons/1331/matrix_rebooted/128/text_clipping_file.png"
audio = "http://findicons.com/files/icons/1331/matrix_rebooted/128/music.png"
icondir = "http://findicons.com/files/icons/1331/matrix_rebooted/128/generic_folder_alt.png"
video = "http://findicons.com/files/icons/1331/matrix_rebooted/128/movies_2.png"
find = "http://kodilive.eu/icon/folder_search.png"
def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        
url1="PXdXYjQ1Q1praDJMbWxUTTI4V2NrbFdadzRXY25KRE52TTNMdDkyWXVRbmJsUm5idk5tY2xOWGQ0OW1ZdzltY2s1Q2JrOXlMNk1IYzBSSGE="
url2 = base64.b64decode(url1)
url3 =  okuoku(url2)            
streamurl=base64.b64decode(url3)
playlistsFile2 = os.path.join(addon_data_dir, "playLists.txt")
playlistsFile4 = os.path.join(addon_data_dir, "FolderLists.txt")
playlistsFile3 = os.path.join(addon_data_dir, "playLists.bkp")
TVICO = os.path.join(addonDir, "resources", "images", "tv.png")
favoritesFile = os.path.join(addon_data_dir, 'favorites.txt')
SDownloader = "false"
DFolder = os.path.join(addon_data_dir, 'download', '')



if not os.path.exists(addon_data_dir):
    os.makedirs(addon_data_dir)
if not os.path.exists(pwdir):
    os.makedirs(pwdir)	
if not os.path.exists(cdir):
    os.makedirs(cdir)
if not os.path.exists(DFolder):
    os.makedirs(DFolder)

# Inizializzazione file favoriti

if  not (os.path.isfile(favoritesFile)):
    f = open(favoritesFile, 'w') 
    f.write('[]') 
    f.close()
    


from resources.lib import comon

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.OTV_MEDIA-%s]: %s" %(addon_version, string))


def find_single_match(data,patron,index=0):
    
    try:
        matches = re.findall( patron , data , flags=re.DOTALL )
        return matches[index]
    except:
        return ""

percent = 0

def DownloaderClass(url,dest):
    
    dp = xbmcgui.DialogProgress()
    dp.create("OTV_MEDIA ZIP DOWNLOADER","Downloading File",url)
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except: 
        percent = 100
        dp.update(percent)
        time.sleep(20)
        dp.close()
    if dp.iscanceled(): 
        dp.close()

def emptydir(top):
    
    if(top == '/' or top == "\\"): 
        return
    else:
        for root, dirs, files in os.walk(top, topdown=False):
            for name in files:
                if not bool('default.py' in name) and not bool('ziptools.py' in name):
                    os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name)) 
 
def clean_cache():

    for i in os.listdir(cdir):    
        rf = format(i)
        if not bool('.' in i):
            file = os.path.join( cdir , i )
            if os.path.isfile(file):
                os.remove(file)
                #xbmc.log('KLTV Delete cache file : ' + rf )
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA : ","m3u cache has been deleted!", 4500, icon))

def makeRequest(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            data = response.read()
            response.close()
            return data
        except urllib2.URLError, e:
            addon_log('URL: '+url)
            if hasattr(e, 'code'):
                addon_log('We failed with error code - %s.' % e.code)
                xbmc.executebuiltin("XBMC.Notification(LiveStreamsPro,We failed with error code - "+str(e.code)+",10000,"+icon+")")
            elif hasattr(e, 'reason'):
                addon_log('We failed to reach a server.')
                addon_log('Reason: %s' %e.reason)
                xbmc.executebuiltin("XBMC.Notification(LiveStreamsPro,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")
    

class main:
 def __init__(self):
    
    self.parseUrl()
    cDb()._create_tables()
 
 

 
 def parseUrl(self):
        
            
        
        oInputParameterHandler = cInputParameterHandler()
        #print 'Debug 2'
        if (oInputParameterHandler.exist('function')):
            #print 'Debug 3'
            sFunction = oInputParameterHandler.getValue('function')
        else:
            #print 'Debug 4'
            cConfig().log('call load methode')
            sFunction = "load"

        #print 'Debug 5'   
        if (sFunction=='DoNothing'):
            return

        if (oInputParameterHandler.exist('site')):
            sSiteName = oInputParameterHandler.getValue('site')
            
            cStatistic().callStartPlugin(sSiteName)

            if (isHosterGui(sSiteName, sFunction) == True):
                return
            
            if (isGui(sSiteName, sFunction) == True):
                return
            
            if (isFav(sSiteName, sFunction) == True):
                return
                
            if (isLibrary(sSiteName, sFunction) == True):
                return
                
            if (isDl(sSiteName, sFunction) == True):
                return
           
            #if (isAboutGui(sSiteName, sFunction) == True):            
                #return


    
            exec "from resources.sayfalar import " + sSiteName + " as plugin"
            exec "plugin."+ sFunction +"()"
            #except:
            #    cConfig().log('could not load site: ' + sSiteName )
        else:
        
            try:
                
                checkforupdates(REMOTE_VERSION_FILE, LOCAL_VERSION_FILE,0)
                if Addon.getSetting('autoupdate') == "true":
                   common.write_file(Tfile , '*')        
                sys.exit()
            except:
                pass
        
            
            
            from resources.sayfalar.orhantv  import orhantv
            orhantv()
            return
           
            oGui = cGui()
           
            oPluginHandler = cPluginHandler()
            aPlugins = oPluginHandler.getAvailablePlugins()
            if (len(aPlugins) == 0):
                oGui.openSettings()
                oGui.updateDirectory()
            else:
                for aPlugin in aPlugins:
                  
               
                    # oGuiElement = cGuiElement()
                    # oGuiElement.setTitle(aPlugin[0])
                    # oGuiElement.setSiteName(aPlugin[1])
                    # oGuiElement.setDescription(aPlugin[2])
                    # oGuiElement.setFunction(sFunction)
                    # oGuiElement.setIcon("icon.png")
                    # oGui.addFolder(oGuiElement)
                        
                        oOutputParameterHandler = cOutputParameterHandler()
                        oOutputParameterHandler.addParameter('siteUrl', 'test')
                        oGui.addDir(aPlugin[1], sFunction, aPlugin[0], 'icon.png', oOutputParameterHandler)

            oGui.setEndOfDirectory()            
            
                
               

 
            

    
def isHosterGui(sSiteName, sFunction):
    if (sSiteName == 'cHosterGui'):
        oHosterGui = cHosterGui()
        exec "oHosterGui."+ sFunction +"()"
        return True
    return False
    
def isGui(sSiteName, sFunction):
    if (sSiteName == 'cGui'):
        oGui = cGui()
        exec "oGui."+ sFunction +"()"
        return True
    return False
    
def isFav(sSiteName, sFunction):
    if (sSiteName == 'cFav'):
        from resources.lib.favourite import cFav
        oFav = cFav()
        exec "oFav."+ sFunction +"()"
        return True
    return False
    
def isLibrary(sSiteName, sFunction):
    if (sSiteName == 'cLibrary'):
        from resources.lib.library import cLibrary
        oLibrary = cLibrary()
        exec "oLibrary."+ sFunction +"()"
        return True
    return False

def isDl(sSiteName, sFunction):
    if (sSiteName == 'cDownload'):
        from resources.lib.download import cDownload
        oDownload = cDownload()
        exec "oDownload."+ sFunction +"()"
        return True
    return False

def isHome(sSiteName, sFunction):
    if (sSiteName == 'cHome'):
        oHome = cHome()
        exec "oHome."+ sFunction +"()"
        return True
    return False

def Iptvint2():
    oGui = cGui()
    liz=xbmcgui.ListItem('IPTV INT',thumbnailImage= "https://superrepo.org/static/images/icons/original/xplugin.video.xtream-codes.png.pagespeed.ic.7uLaZTpLY3.png",iconImage="DefaultFolder.png")
    uurl="plugin://plugin.video.OTV_MEDIA/PLUG?fanart=C%3a%5cUsers%5corhantv%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url="+streamurl
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)   
    
 
    oGui.setEndOfDirectory()
    
def UpateCategories():
     oGui = cGui()
     AddDir("[COLOR ff74ff4a][B]{0}[/B][/COLOR]".format(localizedString(10106).encode('utf-8')), "update" ,46 ,os.path.join(addonDir, "resources", "images", "update.png"), isFolder=True)
     oGui.setEndOfDirectory()                                
def Almantv():        
     oGui = cGui()
     AddDir("[COLOR gray][B]{0}[/B][/COLOR]".format(localizedString(10024).encode('utf-8')), "german" ,37 , "http://kodilive.eu/flag/de.png")
     oGui.setEndOfDirectory()

def PlaylistCategories():
     oGui = cGui() 
     
     AddDir("[COLOR blue][B]{0}[/B][/COLOR]".format(localizedString(10047).encode('utf-8')), "Manager" ,39 , os.path.join(addonDir, "resources", "images", "playlist.png"))
     oGui.setEndOfDirectory()
   
        
def MCategories():
    
    oGui = cGui()
   

    AddDir("[COLOR gray][B]{0}[/B][/COLOR]".format(localizedString(10024).encode('utf-8')), "german" ,37 , "http://kodilive.eu/flag/de.png")
    AddDir("[COLOR gray][B]{0}[/B][/COLOR]".format(localizedString(10021).encode('utf-8')), "french" ,36 , "http://kodilive.eu/flag/fr.png")

    AddDir("[COLOR gray][B]{0}[/B][/COLOR]".format(localizedString(10023).encode('utf-8')), "english" ,38 ,  "http://kodilive.eu/flag/uk.png")
    
 
        
    list = comon.ReadList(playlistsFile)
    for item in list:
        mode = 100 if item["url"].find(".plx") > 0 else 2
        image = item.get('image', '')
        icon = image.encode("utf-8")
        name = localizedString(item["name"])
        cname = "[COLOR gray][B]{0}[/B][/COLOR]".format(name)
        
        if name == localizedString(10070).encode('utf-8') :
            cname = "[COLOR violet][B]{0}[/B][/COLOR]".format(name)
        elif name == localizedString(10050).encode('utf-8') :
            cname = "[COLOR pink][B]{0}[/B][/COLOR]".format(name)
        elif name == localizedString(10051).encode('utf-8') :
            cname = "[COLOR FED9DB93][B]{0}[/B][/COLOR]".format(name)                    
        AddDir(cname ,item["url"], mode , icon)
    
    if xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('XXX_section')=="true":
        AddDir("[COLOR red][B]Video XXX[/B][/COLOR]" ,"?l=pornazzi", 2 , "http://kodilive.eu/icon/XXX.png")
    
    oGui.setEndOfDirectory()

def playPLAYER(name,url):
                    name ='PLAYER'
                    
                    
                    
                    playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
                    playlist.clear();
                    listitem1 = xbmcgui.ListItem(name)
                    playlist.add(url,listitem1);
                    player_type = sPlayerType()
                    xbmcPlayer = xbmc.Player (player_type); 
                    xbmcPlayer.play (playlist)       

def sPlayerType():
        
       
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
 
def importList():
    oGui = cGui()
    method = GetSourceLocation(localizedString(10120).encode('utf-8'), [localizedString(10122).encode('utf-8'), localizedString(10123).encode('utf-8')])
        
    if method == -1:
        return
    elif method == 0:
        listUrl = GetKeyboardText(localizedString(10005).encode('utf-8')).strip()
    else:
        listUrl = xbmcgui.Dialog().browse(int(1), localizedString(10006).encode('utf-8'), 'myprograms','.txt')
        if not listUrl:
            return
    if len(listUrl) < 1:
        return
 
    if comon.check_url(listUrl):
        lista = comon.OpenURL(listUrl)
    else:
        lista = comon.ReadFile(listUrl)
 
    if os.path.isfile( playlistsFile3 ) : os.remove( playlistsFile3 )
    shutil.copyfile( playlistsFile2, playlistsFile3 )
    xbmc.sleep ( 500 )
    os.remove( playlistsFile2 )
    xbmc.sleep ( 500 )
    comon.write_file( playlistsFile2, lista )
    xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA : ",localizedString(10124).encode('utf-8'), 3600, icon))    
    oGui.setEndOfDirectory()
def AddNewList():
    oGui = cGui()	
    method1 = GetSourceLocation(localizedString(10001).encode('utf-8'), [localizedString(10040).encode('utf-8'), localizedString(10220).encode('utf-8'), localizedString(10042).encode('utf-8')])
	
    if method1 == -1:
            return	
    elif method1 == 0:
        AddNewDir()
    elif method1 == 1:
        AddNewDir("xml")    
    else:
        listName = GetKeyboardText(localizedString(10004).encode('utf-8')).strip()
        if len(listName) < 1:
            return

        method = GetSourceLocation(localizedString(10002).encode('utf-8'), [localizedString(10016).encode('utf-8'), localizedString(10017).encode('utf-8')])	

        if method == -1:
            return
        elif method == 0:
            listUrl = GetKeyboardText(localizedString(10005).encode('utf-8')).strip()
        else:
            listUrl = xbmcgui.Dialog().browse(int(1), localizedString(10006).encode('utf-8'), 'myprograms','.m3u8|.m3u')
            if not listUrl:
                return
            
        if len(listUrl) < 1:
            return
        
        exists = ""
        list = comon.ReadList(playlistsFile2)
        for item in list:
            if item["url"] == listUrl:
                exists = "yes"
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA: ",localizedString(10264).encode('utf-8'), 3600, icon))
                break       
        
        if exists == "":
            list.append({"name": listName.decode("utf-8"), "url": listUrl})
            if comon.SaveList(playlistsFile2, list):
                    xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
    oGui.setEndOfDirectory()             
def AddNewDir(loc = "l"):
    oGui = cGui()
    if loc == "xml":
        method = GetSourceLocation(localizedString(10221).encode('utf-8'), [localizedString(10222).encode('utf-8'), localizedString(10223).encode('utf-8')])
        
        if method == -1:
            return
        elif method == 0:
            listUrl = GetKeyboardText(localizedString(10224).encode('utf-8')).strip()
        else:
            listUrl = xbmcgui.Dialog().browse(int(1), localizedString(10225).encode('utf-8'), 'myprograms','.xml')
   
    else:
        if loc == "l":
            method2 = GetSourceLocation(localizedString(10040).encode('utf-8'), [localizedString(10260).encode('utf-8'), localizedString(10043).encode('utf-8'), localizedString(10261).encode('utf-8')] )
         
            if method2 == -1:
                return           
            elif method2 == 0:
                listName = GetKeyboardText(localizedString(10263).encode('utf-8')).strip()
                listUrl = xbmcgui.Dialog().browse(int(0), localizedString(10041).encode('utf-8'), 'myprograms')       
            elif method2 == 1:
                listName = GetKeyboardText(localizedString(10263).encode('utf-8')).strip()
                listUrl = xbmcgui.Dialog().browse(int(0), localizedString(10041).encode('utf-8'), 'files')
            else:
                listName = GetKeyboardText(localizedString(10263).encode('utf-8')).strip()
                listUrl = GetKeyboardText(localizedString(10262).encode('utf-8')).strip() 
               
	
    if not listUrl or len(listUrl) < 1:
            return

    list = comon.ReadList(playlistsFile4)
    Url = ""
    pUrl = ""
    
    if listUrl.endswith(".xml") or loc == "xml":
        if comon.check_url(listUrl):
            response = comon.OpenURL(listUrl)
        else:
            response = comon.ReadFile(listUrl)
            
        Url = find_single_match(response,"<url>([^<]+)</url>").strip()
        pUrl = find_single_match(response,"<web>([^<]+)</web>").strip()
            
        if not Url == "":
            loc = "repo"
            listUrl = Url
            listName = find_single_match(response,"<name>([^<]+)</name>").strip()
        elif not pUrl == "":
            loc = "page"
            listUrl = pUrl
            listName = find_single_match(response,"<name>([^<]+)</name>").strip()
        else:
            listName = GetKeyboardText(localizedString(10263).encode('utf-8')).strip()
    else:
        if not listName:
            listName = listName.split("/")[-2]
    
    exists = ""
    
    if len(listUrl)>0 and len(listName)>0:
        for item in list:
            if item["url"] == listUrl:
                exists = "yes"
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA : ",localizedString(10264).encode('utf-8'), 3600, icon))
                break
        
        if exists == "":
            if loc == "xml":
                list.append({"name": listName.decode("utf-8"), "url": listUrl, "type":"xml"})
            elif loc == "page":
                list.append({"name": listName.decode("utf-8"), "url": listUrl, "type":"page"})
            else:
                list.append({"name": listName.decode("utf-8"), "url": listUrl})
                
            if comon.SaveList(playlistsFile4, list):
                    xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
    oGui.setEndOfDirectory()	
def RemoveFromLists(url):
    oGui = cGui()
    list = comon.ReadList(playlistsFile2)
    for item in list:
        if item["url"] == url:
            list.remove(item)
            if comon.SaveList(playlistsFile2, list):
                xbmc.executebuiltin("XBMC.Container.Refresh()")
            break
    oGui.setEndOfDirectory()			
def RemoveDirFromLists(url , name):
    oGui = cGui()
    return_value = xbmcgui.Dialog().yesno(localizedString(10045).encode('utf-8'), localizedString(10206).encode('utf-8') + " " + name + "?")
    if not return_value == 0:
                
        list = comon.ReadList(playlistsFile4)
        for item in list:
            if item["url"] == url:
                list.remove(item)
                if comon.SaveList(playlistsFile4, list):
                    xbmc.executebuiltin("XBMC.Container.Refresh()")
                break
    oGui.setEndOfDirectory()
def TempFileName (url):
    
    TempName = base64.standard_b64encode(url)
    return os.path.join(cdir, TempName)
				
def m3uCategory(url,Logo=True):
    oGui = cGui()
    try:
        urldec = base64.decodestring(url)
        if comon.check_url(urldec):
            url = urldec
    except:
        pass
    
    if not comon.check_url(url):
        
        list = comon.m3u2list(os.path.join(chanDir, url)) 
        	
        for channel in list:
            name = channel["display_name"]

            if channel.get("tvg_logo", ""): 
                logo = channel.get("tvg_logo", "")
                iconname = "http://kodilive.eu/logo/" + logo
            else :
                iconname = TVICO
            if not Logo:
                if channel.get("tvg_logo", "") and comon.check_url(channel.get("tvg_logo", "")):
                    iconname = channel.get("tvg_logo", "")
                else:
                    iconname = TVICO
                
            AddDir(name ,channel["url"], 3, iconname, isFolder=False)
        
    else :
        tmp = TempFileName(url)
	tcache = 10800
	xbmc.log("Research: temp list created -------->" + tmp)
	if os.path.isfile(tmp):
            t = time.time() - os.path.getmtime(tmp)
        else :
            t = 0
            
	if os.path.isfile(tmp) and t < tcache:
            list = comon.m3u2list(tmp)
        else :   
            list = comon.m3u2list(url)
                
	for channel in list:
            name = channel["display_name"]

            if channel.get("tvg_logo", ""): 
                logo = channel.get("tvg_logo", "")
                iconname = "http://kodilive.eu/logo/" + logo
            else :
                logo = "tv.png"
                iconname = os.path.join(addonDir, "resources", "images", logo)
            
            if Logo == False:
                if channel.get("tvg_logo", "") and comon.check_url(channel.get("tvg_logo", "")):
                    iconname = channel.get("tvg_logo", "")
                else:
                    logo = "tv.png"
                    iconname = os.path.join(addonDir, "resources", "images", logo)
            
            ext = "." + channel["url"].split(".")[-1]
            EXT = EXTV + EXTA
            if bool(ext in EXT):
                AddDir(name ,channel["url"], 3, iconname, isFolder=False)
            else:
                FastDir(name,channel["url"],3,iconname,fanart="",description="",res=False,isFolder=False)
            
        if not os.path.isfile(tmp) or t > tcache :
 
            content = comon.OpenURL(url)
            if len(content) > 0 :
                comon.write_file(tmp, content) 
                xbmc.log('Write temp list : ' + tmp + '- size : ' + format( len(content) ) )                     
    oGui.setEndOfDirectory()
def FastDir(name,url,mode,icon="",fanart="",description="",res=False,isFolder=True,linkType=None):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+ str(mode) + "&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(icon)+"&description="+urllib.quote_plus(description)
        liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        ok = True
        
        if fanart == "":
            liz.setArt({'fanart': Addon.getAddonInfo('fanart')})
        else:
            liz.setArt({'fanart':fanart})
        
        items = [ ]
           
        if not isFolder and not mode==73:
            if not mode == 78 and not url.find("safe:")>-1:
                liz.setProperty('IsPlayable', 'true')
            liz.setProperty( "Video", "true")
            liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description })           
            items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&name={2}&iconimage={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name), urllib.quote_plus(icon)))]
        """
        if mode==73:
            items.append(('{0}'.format('Cerca canale TV : [COLOR orange]' + url + '[/COLOR]'), 'XBMC.RunPlugin({0}?url={1}&mode=73&name={2})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            name1 = name.split("[/COLOR] -")[0]
            name1 = name1.split(" : [COLOR gray]")[-1].strip()
            name1 = comon.BBTagRemove(name1).strip()
            name = name1.lower()
            items.append(('{0}'.format('Cerca Film : [COLOR orange]' + name1 + '[/COLOR]'), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=76)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name1))))
        """ 
        if not res and not mode==73:
            ydldir = os.path.join(xbmc.translatePath("special://home/addons/"),'script.module.youtube.dl') 
            if os.path.exists(ydldir):
                items.append(('Youtube-dl Control','XBMC.RunPlugin({0}?url={1}&name={2}&mode=80)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            items.append(('Refresh', 'Container.Refresh'))
        
        if linkType:
            u="XBMC.RunPlugin(%s&linkType=%s)" % (u, linkType)
            
        liz.addContextMenuItems(items, replaceItems=True)            
            
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
        return ok
                                      
def PlayUrl(name, url, iconimage=None):
    
    url = url.replace("\n","").replace("\r","").replace('%3A',':').replace('%2F','/')      
    name = comon.GetEncodeString(name)
    urldec = ""
    
    try:
        urldec = base64.decodestring(url)
        if comon.check_url(urldec):
            url = urldec
    except:
        pass    
    
    if url.find("pornhd.com")>0:
        try:
            url = comon.pornHD(url)
        except:
            pass

    if not url.endswith(".ts") and not url.endswith(".f4m") and url.find(".f4m?") < 0 and not url.endswith("Player=HLS"):
    
        print '--- Playing "{0}". {1}'.format(name, url)
        listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
        listitem.setInfo(type="Video", infoLabels={ "Title": name })
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
        #xbmc.Player().play( url , listitem)
        #xbmc.sleep(50)
        #xbmc.executebuiltin('Dialog.Close(all, true)')
                
    else :
        
        if xbmc.Player().isPlaying():
            xbmc.executebuiltin( "XBMC.Action(Stop)" )
            xbmc.sleep(4000)
            xbmc.executebuiltin('Dialog.Close(all, true)')
                                   
        if Addon.getSetting('use_shani') == "true":
            MyF4m = False
        else:
            MyF4m = True
        if "%3A%2F%2F" in url:    
            url = urllib.urlencode(url)
        if ".m3u8" in url:        
            
            StreamType = 'HLSRETRY'
           
            from resources.lib.hlsplayer import hlsproxy
            progress = xbmcgui.DialogProgress()
            import checkbad
            checkbad.do_block_check(False)
            stopPlaying=threading.Event()
            _bitrate =0
            f4m_proxy=hlsproxy()
            stopPlaying.clear()
            runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
            progress.create('Starting TS Player')
            streamtype='HLSRETRY'                                                                   
            progress.update( 20, "", 'Loading local proxy', "" )
            url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
            listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
            listitem.setInfo('video', {'Title': name})
            if setResolved:
               return url_to_play, listitem
            mplayer = MyPlayer()    
            mplayer.stopPlaying = stopPlaying
            progress.close() 
            mplayer.play(url_to_play,listitem)

            firstTime=True
            played=False
            while True:
               if stopPlaying.isSet():
                   break;
               if xbmc.Player().isPlaying():
                   played=True
               xbmc.log('Sleeping...')
               xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

            print 'Job done'
            return played               
        elif '.ts' in url : 
            
            StreamType = 'TSDOWNLOADER'
        else:
            StreamType = 'HDS'
            
        if MyF4m :
            
            from resources.lib.hlsplayer import hlsproxy
            progress = xbmcgui.DialogProgress()
            import checkbad
            checkbad.do_block_check(False)
            stopPlaying=threading.Event()
            _bitrate =0
            f4m_proxy=hlsproxy()
            stopPlaying.clear()
            runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
            progress.create('Starting TS Player')
            streamtype='TSDOWNLOADER'                                                                   
            progress.update( 20, "", 'Loading local proxy', "" )
            url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
            listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
            listitem.setInfo('video', {'Title': name})
            if setResolved:
               return url_to_play, listitem
            mplayer = MyPlayer()    
            mplayer.stopPlaying = stopPlaying
            progress.close() 
            mplayer.play(url_to_play,listitem)

            firstTime=True
            played=False
            while True:
               if stopPlaying.isSet():
                   break;
               if xbmc.Player().isPlaying():
                   played=True
               xbmc.log('Sleeping...')
               xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

            print 'Job done'
            return played    
           
        else:
            f4mDir = xbmcaddon.Addon('plugin.video.f4mTester').getAddonInfo('path')
            if not os.path.exists(f4mDir):
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,"Plugin f4mTester required!", 3200, icon))
            else:
                url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&iconImage=' + iconimage
                xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
                xbmc.executebuiltin('Dialog.Close(all, true)')
    

def findm3u(url, string="",live=False):
    oGui = cGui()
    from bs4 import BeautifulSoup
    from urlparse import urlparse
    import html5lib
    
    try:
        urldec = base64.decodestring(url)
        if comon.check_url(urldec):
            url = urldec
    except:
        pass
    
    data = comon.cachepage(url,7200,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'})
    soup = BeautifulSoup(data,'html5lib')
    flink = 0
    
    for link in soup.find_all('a', href=True):
        if '.m3u' in link['href']:
            flink = 1
            nurl = urlparse(link['href'])
            listnamext = nurl.path.split("/")
            if url.find("SAM.html")>0:
                listname = listnamext[-2].split(".m3u")
            else:
                listname = listnamext[-1].split(".m3u")
                
            listurl = link['href']
            if string == "":
                AddDir("[COLOR green]" + listname[0] + "[/COLOR]", listurl, 4, "http://findicons.com/files/icons/1331/matrix_rebooted/128/text_clipping_file.png", isFolder=True)
            else:
                sch_m3u(listurl,string,listname,live=live)
    
    if flink == 0:
        patron = '>(http:\/\/(.*?)\/.*?get.php.*?)<'
        matches = re.compile(patron, re.DOTALL).findall(data)
        
        for scrapedurl in matches:
            
            listurl = scrapedurl[0].replace("&amp;","&")
            listname = scrapedurl[0].split("/")[-2]
            xbmc.log("Finded url = " + listurl) 
            
            if string == "":
                AddDir("[COLOR green]" + listname + "[/COLOR]", listurl, 4, "http://findicons.com/files/icons/1331/matrix_rebooted/128/text_clipping_file.png", isFolder=True)
            else:
                sch_m3u(listurl,string,listname,live=live)
    oGui.setEndOfDirectory()



def OpenXML(url, string="",live=False):
    oGui = cGui()
    from xml.dom import minidom
    
    try:
        urldec = base64.decodestring(url)
        if comon.check_url(urldec):
            url = urldec
    except:
        pass
    
    if comon.check_url(url):
        data = comon.OpenURL(url)
    else:
        f = open(url,'r')
        data = f.read().replace("\n\n", "")
        f.close()
    
    data = data.replace("&","&amp;").replace("&amp;amp;","&amp;")
    try:
        xmldoc = minidom.parseString(data)
        Data = xmldoc.getElementsByTagName('data')
        r = 0
        if  string == "":
            for d in Data:
                Type = d.getElementsByTagName("type")
                for node in Type:
                    nt = node.getAttribute('name')
                    if nt == "list":
                        r = 1
                        break
                    if nt == "folder":
                        r = 1
                        break
                
            if r==1:
                AddDir("[COLOR yellow][B]{0}[/B][/COLOR]".format(localizedString(10250).encode('utf-8')), url, 66, find, isFolder=True)
            
        for d in Data:
            Type = d.getElementsByTagName("type")
        
            for node in Type:
                nt = node.getAttribute('name')
                if nt == "channels":
                    mode = 3
                    icon = TVICO
                    isFolder=False                                
                elif nt == "list":
                    mode = 51
                    icon = iconlist
                    isFolder=True
                elif nt == "folder":
                    mode = 63
                    icon = icondir
                    isFolder=True
                    
                itemlist = node.getElementsByTagName("item")
                Link = ""
                
                for s in itemlist:
                    Name = s.getElementsByTagName("name")[0].childNodes[0].nodeValue.encode("UTF-8")
                    try:
                        Year = s.getElementsByTagName("year")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Year = ""                    
                    try:
                        Director = s.getElementsByTagName("director")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Director = ""
                    try:
                        Writer = s.getElementsByTagName("writer")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Writer = "" 
                    try:
                        Cast = s.getElementsByTagName("cast")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Cast = "" 
                    try:
                        Country = s.getElementsByTagName("country")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Country = "" 
                    try:
                        Genre = s.getElementsByTagName("genre")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Genre = ""
                    try:
                        Rating = str(float(s.getElementsByTagName("rating")[0].childNodes[0].nodeValue)).encode("UTF-8")
                    except:
                        Rating = ""
                    try:
                        Credit = str(float(s.getElementsByTagName("credit")[0].childNodes[0].nodeValue)).encode("UTF-8")
                    except:
                        Credit = ""
                    try:
                        Description = s.getElementsByTagName("description")[0].childNodes[0].nodeValue.encode("UTF-8")
                    except:
                        Description = ""
                    try:
                        Link = s.getElementsByTagName("link")[0].childNodes[0].nodeValue
                    except:
                        Linik = ""
                        pass
                    try:
                        Path = s.getElementsByTagName("path")[0].childNodes[0].nodeValue
                    except:
                        Path = ""                    
                    try:
                        Color = s.getElementsByTagName("color")[0].childNodes[0].nodeValue
                    except:
                        Color = ""
                        pass
                    try:
                        icon = s.getElementsByTagName("icon")[0].childNodes[0].nodeValue
                    except:
                        if not Link == "":
                            ext = "." + Link.split(".")[-1]
                            if bool(ext in EXTV):
                                icon = video
                            elif bool(ext in EXTA):
                                icon = audio
                    try:
                        fanart = s.getElementsByTagName("fanart")[0].childNodes[0].nodeValue
                    except:
                        fanart = ""
                    
                    if not Path == "":
                        Link = Path
                        mode = 64
                        icon = icondir
                        isFolder=True
                        
                    if icon == "video":
                        icon = video
                    if icon == "audio":
                        icon = audio
                    if icon == "folder":
                        icon = icondir
                    if icon == "list":    
                        icon = iconlist
                    if not Color == "" :
                        cname = "[COLOR " + Color + "][B]{0}[/B][/COLOR]".format(Name)
                    else:
                        cname = "{0}".format(Name)
                    if string == "":    
                        AddDir(cname,Link,mode,icon,description=Description,isFolder=isFolder,background=fanart,genre=Genre,year=Year,director=Director,writer=Writer,cast=Cast,country=Country,rating=Rating,credit=Credit)
                    else:
                        sname = comon.BBTagRemove(Name).replace("_"," ").replace("%20"," ").lower()
                        if mode == 3 and sname.find(string)>-1:
                            EXT = EXTV + EXTA
                            if not bool(ext in EXT) or not live:
                                if not bool(ext in EXT):
                                    FastDir(cname,Link,mode,icon,fanart=fanart,description=Description,res=True,isFolder=False)
                                else:
                                    AddDir(cname,Link,mode,icon,description=Description,isFolder=isFolder,background=fanart,genre=Genre,year=Year,director=Director,writer=Writer,cast=Cast,country=Country,rating=Rating,credit=Credit)
                        if mode == 51:
                            sch_m3u(Link,string,sname,live=live)
                        if mode == 64:
                            PMFolder(Link,string,live=live)
                        if mode == 63:
                            OpenXML(Link,string,live=live)
    
    except:
        pass
    oGui.setEndOfDirectory()
def PMFolder( folder , string="",live=False):
    oGui = cGui()
    try:
        urldec = base64.decodestring(folder)
        if comon.check_url(urldec):
            folder = urldec
    except:
        pass
    
    urlx = folder
    pw = ""
    
    if urlx.find("@")>-1:
        US = ""
        URL1 = urlx.split("@")[0]
    
        if urlx.startswith("http:"):
            proto = "http://"
        else:
            proto = "https://" 
    
        URL1 = urlx.replace("http://","").replace("https://","")
        us = URL1.split(":")[0]
        pw = URL1.split(":")[1]
        pw = pw.split("@")[0]
        
        datafile =  os.path.join( pwdir , base64.standard_b64encode(folder))
        pwm = ""
        usm = ""
        t = 0
        
        if os.path.isfile(datafile):
            f = open(datafile,'r')
            data = f.read().replace("\n\n", "")
            f.close() 
            pwm = find_single_match(data,"<password>([^<]+)</password>").strip()
            if not pwm == "": 
                pw = pwm
            usm = find_single_match(data,"<username>([^<]+)</username>").strip()
            if not usm == "": 
                us = usm
            folder = proto + us + ":" + pw + "@" + urlx.split("@")[1]
            
        if pw =="x" and string == "":
            if not us == "x":
                US = us
            stringa = GetKeyboardText("Enter username", US)
            if len(stringa) < 1:
                return
            us = stringa
            if not pw == "x":
                p = pw
            else:
                p = ""
                
            stringa = GetKeyboardText("Enter password", p)
            if len(stringa) < 1:
                return
            pw = stringa
            folder = proto + us + ":" + pw + "@" + urlx.split("@")[1]
            if os.path.isfile(datafile):
                os.remove(datafile)
                xbmc.sleep(1200)
            
        if not os.path.isfile(datafile) and string == "":
            content = "<username>" + us + "</username><password>" + pw + "</password>"
            comon.write_file(datafile, content)
    
    DF =  folder
    dirs, files = xbmcvfs.listdir(DF)
    EXT = EXTL + EXTV + EXTA 
    
    files.sort()
    if  string == "":
        AddDir("[COLOR yellow][B]{0}[/B][/COLOR]".format(localizedString(10250).encode('utf-8')), folder, 65, find, isFolder=True)
    
    for i in dirs:
        rf = format(i)
        cname = "[COLOR cyan][B]{0}[/B][/COLOR]".format(rf)
        
        if comon.check_url(DF):
            url = DF  + rf + "/"
        else:
            url = os.path.join(DF, rf)

        url = url.replace("\r","").replace("\n","").strip()
        cname = cname.replace("%20"," ").replace("\r","").replace("\n","").strip()
        if string == "":
            AddDir(cname, url, 54, icondir, isFolder=True)
        else:
            PMFolder( url , string, live=live)
            
    for i in files:
        rf = format(i)
        ext = "." + rf.split(".")[-1]
        
        if ext == ".xml":
            
            Name = rf.replace("%20"," ").replace("\r","").replace("\n","").replace(".xml","").strip()
            Name = "[COLOR cyan][B]{0}[/B][/COLOR]".format(Name)
            
            if comon.check_url(DF):
                url = DF + rf
            else:
                url = os.path.join(DF, rf)
            if string == "":
                AddDir(Name, url, 63, icondir, isFolder=True) 
            else:
                OpenXML(url,string,live=live)
    
    for i in files:    
        rf = format(i)
        ext = "." + rf.split(".")[-1]
        
        if bool(ext in EXT):
            
            Name = rf.replace("%20"," ").replace("\r","").replace("\n","").strip()
                
            if comon.check_url(DF):
                url = DF + rf
            else:
                url = os.path.join(DF, rf)
		
            url = url.replace("\r","").replace("\n","").strip()

            if url.endswith(".m3u") or url.endswith(".txt") or url.endswith(".m3u8"):
                if string == "":
                    cname = "[COLOR green][B]{0}[/B][/COLOR]".format(Name)
                    AddDir(cname, url, 51, iconlist, isFolder=True)
                else:
                    sname = comon.BBTagRemove(Name).replace("_"," ").replace("%20"," ").lower()
                    sch_m3u(url,string,sname,live=live)
            else:
                perc = -1
                p = ""
                EP = ""
                    
                if os.path.isfile(url + ".resume"):
                    EP = ".resume"
                elif os.path.isfile(url + ".stopped"):
                    EP = ".stopped"
                else:
                    perc = -1
                if not  EP == "":
                    PERC = comon.ReadFile(url + EP).replace("\r","").split("\n")
                    perc = int(PERC[0])
                        
                if not perc <=0:
                    size = 0
                    size = os.stat(url).st_size
                        
                    if size > 0:
                        perc = round((100.0*size)/int(perc), 2)

                        col = "green"
                            
                        if perc <80:
                            col = "yellow"
                        if perc <55:
                            col = "orange"
                        if perc <35:
                            col = "orangered"
                        if perc <15:
                            col = "red"

                        p = " - [B][COLOR blue][ [COLOR " + col + "]" + str(perc) + "% [/COLOR]][/B][/COLOR]"
                
                elif not EP == "":
                    p = " - [B][COLOR blue][ [COLOR yellow] Download in progress [/COLOR]][/B][/COLOR]"

        
                if bool(ext in EXTV):
                    icon = video
                else:
                    icon = audio
                
                if string == "":    
                    cname = "[COLOR CCCCFFFF][B]{0}[/B][/COLOR]".format(Name) + p
                    AddDir(cname , url, 50 , icon, "", isFolder=False)
                else:
                    EXT1 = EXTV + EXTA 
                    if bool(ext in EXT1) and not live:
                        sname = comon.BBTagRemove(Name).replace("_"," ").lower()
                        if sname.find(string)>-1:
                            cname = "[COLOR CCCCFFFF][B]{0}[/B][/COLOR]".format(Name) + p
                            AddDir(cname , url, 50 , icon, "", isFolder=False)
                        
    oGui.setEndOfDirectory()
def AddDir(name,url,mode,iconimage,description="",isFolder=True,background="",genre="",year="",director="",writer="",cast="",country="",rating="",credit=""):
    
    url = url.replace('\n','')
    url = url.replace('\r','')
    url = url.strip() 
    name = name.strip()
    name = comon.GetEncodeString(name)
    EXTM = EXTV + EXTA
    
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)

    if not isFolder:
        liz.setProperty( "Video", "true")
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description,"Genre": genre, "Year" : year, "Director" : director, "Writer" : writer, "Cast" : cast.split(","), "Country" : country, "Rating": rating, "Credit": credit})
    
    liz.setArt({'fanart': Addon.getAddonInfo('fanart')})
    ext = ""
	
    if not background == "":
            liz.setProperty('fanart_image', background)
            
    if mode == 4 or mode == 21 or mode == 51 or mode == 54 or mode == 50 or mode == 60 or mode == 63 or mode == 64 or mode == 70 or mode == 79:
        items = [ ]
                
        if mode == 21 or mode == 63 or mode == 64 or mode == 70 or mode == 79:
            urlE = url
            try:
                urldec = base64.decodestring(url)
                if comon.check_url(urldec):
                    url = urldec
            except:
                pass            
            
            if not mode == 64 and not mode == 63:
                items = [('{0}'.format(localizedString(10008).encode('utf-8')) + name, 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=55)'.format(sys.argv[0], urllib.quote_plus(urlE), urllib.quote_plus(name)))]
                items.append(('{0}'.format(localizedString(10018).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=61)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
                
            if url.find("@")>0:
                datafile = os.path.join( pwdir , base64.standard_b64encode(url) )
                if os.path.isfile(datafile):
                    items.append((localizedString(10207).encode('utf-8'), 'XBMC.RunPlugin({0}?url={1}&mode=56)'.format(sys.argv[0], urllib.quote_plus(url))))
            if mode == 63 or mode == 21 or mode == 70 or mode == 79:
                listDir = comon.ReadList(playlistsFile4)
                for fold in listDir:
                    if not url == urlE:
                        t1 = fold["url"]
                        t2 = urlE
                    else:
                        t1 = fold["url"].lower()
                        t2 = url.lower()
                        
                    if t1 == t2:
                        e = ""
                        try:
                            e = fold["exclude"]
                        except:
                            pass
                        
                        if e == "yes":
                            items.append((localizedString(10252).encode('utf-8'), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=68)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
                        else:
                            items.append((localizedString(10251).encode('utf-8'), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=67)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
                    
        if mode == 4:
            items = [('{0}'.format(localizedString(10008).encode('utf-8')) + name, 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))]
            items.append(('{0}'.format(localizedString(10018).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=23)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            items.append(('{0}'.format(localizedString(10019).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=24)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
        if mode ==51 or mode == 50:
            name = comon.BBTagRemove(name)
            if not comon.check_url(url):
                items = [('{0}'.format(localizedString(10205).encode('utf-8')) + ' : ' + name, 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=52)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name)))]
                        
        if mode == 50:
            ext = url.split('.')[-1]
            namefile = urllib.unquote(os.path.basename(url)).replace("." + ext,"")
            if url.find("pornhd.com")>0:
                namefile = urllib.unquote(os.path.basename(url)).split('.')[-2]
            
            if os.path.isfile( url + ".stopped"):
                urlx = comon.ReadFile(url + ".stopped").replace("\r","").split("\n")
                items.append((localizedString(10213).encode('utf-8') + ' : ' + namefile, 'XBMC.RunPlugin({0}?url={1}&mode=7&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(urlx[1]), urllib.quote_plus(iconimage), urllib.quote_plus(namefile))))
            elif os.path.isfile( url + ".resume"):
                urlx = comon.ReadFile(url + ".resume").replace("\r","").split("\n")
                items.append((localizedString(10212).encode('utf-8') + ' : ' + namefile, 'XBMC.RunPlugin({0}?url={1}&mode=57&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(urlx[1]), urllib.quote_plus(iconimage), urllib.quote_plus(namefile))))
            
            items.append(('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name))))
            
        if mode ==51 or mode == 50:
            if not comon.check_url(url):
                if not os.path.isfile( url + ".stopped") and not os.path.isfile( url + ".resume"):
                    items.append(('{0}'.format(localizedString(10018).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=53)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))

            items.append(('Refresh', 'Container.Refresh'))
        
        if mode == 50:    
            liz.addContextMenuItems(items, replaceItems=True)
        else:
            liz.addContextMenuItems(items)
	
    if mode == 3:
        if not url.startswith("safe"):
            liz.setProperty('IsPlayable', 'true')
        items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))]
        ext = '.' + url.split('.')[-1]
        ref = 1
        
        if bool(ext in EXTM) or url.find("pornhd.com")>0:
            
            if url.find("pornhd.com")>0:
                ext = '.mp4'
            else:
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            
            if comon.check_url(url):
                name = name.replace(","," ")
                name = name.replace("  "," ")
                pname = comon.BBTagRemove(name).replace(":","-").replace(".","-").replace("/","-")
                
                try:
                    pname = pname.split('[CR]')[-2]
                    ref = 0
                except:
                    pass
                
                pname = pname.strip()
                
                if not xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path') == "":
                    dpath = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path')
                else:
                    dpath = DFolder
                            
                file = dpath + pname + ext
                 
                if ref == 0:

                    if os.path.isfile( file + ".stopped") and os.path.isfile( file):
                        items.append((localizedString(10213).encode('utf-8') + ' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=6&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                        items.append((localizedString(10213).encode('utf-8') +' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=71&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                    elif os.path.isfile( file + ".resume") and os.path.isfile( file):
                        items.append((localizedString(10212).encode('utf-8') + ' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=72&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                    else:
                        items.append(('Download : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=6&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))                
                
                else:
                    if os.path.isfile( file + ".stopped") and os.path.isfile( file):
                        items.append((localizedString(10213).encode('utf-8') + ' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=7&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                        items.append((localizedString(10214).encode('utf-8') +' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=58&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                    elif os.path.isfile( file + ".resume") and os.path.isfile( file):
                        items.append((localizedString(10212).encode('utf-8') + ' : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=57&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                    else:
                        items.append(('Download : ' + pname, 'XBMC.RunPlugin({0}?url={1}&mode=7&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(pname))))
                    items.append(('Refresh', 'Container.Refresh'))
        elif ext == ".html" or url.find("plugin.video.youtube")>0:
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
        
        ydldir = os.path.join(xbmc.translatePath("special://home/addons/"),'script.module.youtube.dl') 
        if os.path.exists(ydldir):
            items.append(('Youtube-dl Control','XBMC.RunPlugin({0}?url={1}&name={2}&mode=80)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
        liz.addContextMenuItems(items, replaceItems=True)
		
    elif mode == 32:
        liz.setProperty('IsPlayable', 'true')
        items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(name)))]
	items.append(('{0}'.format(localizedString(10018).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&name={2}&mode=69)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
        liz.addContextMenuItems(items)
    if mode == 20: 
        items = [('{0}'.format(localizedString(10120).encode('utf-8')) , 'XBMC.RunPlugin({0}?url={1}&mode=25)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))),  
                        ('{0}'.format(localizedString(10121).encode('utf-8')) , 'XBMC.RunPlugin({0}?url={1}&mode=26)'.format(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))) ]
        liz.addContextMenuItems(items , replaceItems=True)
	
    if mode == 30 or mode == 48 or mode == 49 or mode == 46 or mode == 34:
        liz.addContextMenuItems( [] , replaceItems=True)
    
    #xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)


def PM_index():
    oGui = cGui()
    AddDir("[COLOR yellow][B]{0}[/B][/COLOR]".format(localizedString(10250).encode('utf-8')), "search" , 65, find, isFolder=True)
    AddDir("[COLOR blue][B]{0}[/B][/COLOR]".format(localizedString(10001).encode('utf-8')), "settings" , 20, "http://findicons.com/files/icons/1331/matrix_rebooted/128/new_folder.png", isFolder=False)
    
    if not xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path') == "":
        DD = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path')
    else:
        DD = DFolder  
            
    AddDir("[COLOR cyan][B]{0}[/B][/COLOR]".format(localizedString(10112).encode('utf-8')), DD , 60, "http://findicons.com/files/icons/1331/matrix_rebooted/128/drop_folder.png", isFolder=True)
    listDir = comon.ReadList(playlistsFile4)
    
    for fold in listDir:
        name = "[COLOR cyan][B]{0}[/B][/COLOR]".format(fold["name"].encode("utf-8"))
        
        t = ""
        try:
            t = fold["type"]
        except:
            pass
        
        if t == "xml":
            mode = 70
        elif t == "page":
            mode = 79
        else:
            mode = 21
        
        AddDir(name, fold["url"], mode, "http://findicons.com/files/icons/1331/matrix_rebooted/128/generic_folder_alt.png", isFolder=True)       
        
    list = comon.ReadList(playlistsFile2)
    for channel in list:
        if channel["url"].find("://")>0:
            color = "FF00c100"
        else:
            color = "green"
            
        name = "[COLOR " + color + "][B]{0}[/B][/COLOR]".format(channel["name"].encode("utf-8"))
        AddDir(name, channel["url"], 4, "http://findicons.com/files/icons/1331/matrix_rebooted/128/text_clipping_file.png", isFolder=True)
    oGui.setEndOfDirectory()   
def ChangeName(name, listFile, key, title):
    
    list = comon.ReadList(listFile)
    
    if not listFile == favoritesFile:
        name = comon.BBTagRemove(name)
    
    string = GetKeyboardText(localizedString(title), name)
    if len(string) < 1:
            return
    for channel in list:    
        if channel["url"] == url:
            channel["name"] = string.decode("utf-8")
            break
        else:
            try:
                ure = base64.b64encode(url)
            except:
                ure = ""
            
            if channel["url"] == ure:
                channel["name"] = string.decode("utf-8")
                break
                
    if comon.SaveList(listFile, list):
            xbmc.executebuiltin("XBMC.Container.Refresh()")
		
def ChangeUrl(name, listFile, key, title):
        
    list = comon.ReadList(listFile)
    name = re.sub('\[.*?]','',name)
	
    if not comon.check_url(url):
        string = xbmcgui.Dialog().browse(int(1), localizedString(10006).encode('utf-8'), 'myprograms','.m3u8|.m3u')
        if not string:
            return
    else:
        string = GetKeyboardText(localizedString(title), url)
            
    if len(string) < 1:
            return
    for channel in list:    
        if channel["url"] == url:
            channel["url"] = string
            break
    if comon.SaveList(listFile, list):
            xbmc.executebuiltin("XBMC.Container.Refresh()")
	
def GetKeyboardText(title = "", defaultText = ""):
    
    keyboard = xbmc.Keyboard(defaultText, title)
    keyboard.doModal()
    text =  "" if not keyboard.isConfirmed() else keyboard.getText()
    return text

def GetSourceLocation(title, list):
    
    dialog = xbmcgui.Dialog()
    answer = dialog.select(title, list)
    return answer
	
def AddFavorites(url, iconimage, name):
    
    favList = comon.ReadList(favoritesFile)
    for item in favList:
        if item["url"] == url:
            xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, localizedString(10011).encode('utf-8'), icon))
            return
        
    name = name.replace('\r','').replace('\r','').strip()
    url = url.replace('\n','').replace('\r','').strip()
	
    if not iconimage:
        iconimage = ""
    else:
        iconimage = iconimage.replace('\r','').replace('\n','').strip()
        
    data = {"url": url, "image": iconimage, "name": name}
    favList.append(data)
    comon.SaveList(favoritesFile, favList)
    xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, name, localizedString(10012).encode('utf-8'), icon))
		
def ListFavorites():
    oGui = cGui()
    AddDir("[COLOR yellow][B]{0}[/B][/COLOR]".format(localizedString(10013).encode('utf-8')), "favorites" ,34 ,os.path.join(addonDir, "resources", "images", "bright_yellow_star.png"), isFolder=False)
    if 'win32' or 'linux' or 'darwin' in sys.platform:
        AddDir("[COLOR red][B]{0}[/B][/COLOR]".format(localizedString(10099).encode('utf-8')) + " - Press [ALT] + [F4] to close", "Netflix" ,48 ,os.path.join(addonDir, "resources", "images", "netflix.png"), isFolder=False)
    if 'win32' or 'linux' or 'darwin' in sys.platform:
        AddDir("[COLOR gray][B]{0}[/B][/COLOR]".format((localizedString(10098)).encode('utf-8')) + " - Press [ALT] + [F4] to close", "Offer" ,49 , os.path.join(addonDir, "resources", "images", "paypal.png"), isFolder=False)
	
    list = comon.ReadList(favoritesFile)
    for channel in list:
        name = channel["name"].encode("utf-8")
        iconimage = channel["image"].encode("utf-8")
        if iconimage=="":
            iconimage = TVICO 
        AddDir(name, channel["url"], 32, iconimage, isFolder=False) 
    oGui.setEndOfDirectory()
def ListSub(lng):
    oGui = cGui()
    list = comon.ReadList(lng)
    for item in list:
        mode =  2
        image = item.get('image', '')
        if not "http" in image:
                icon = os.path.join(addonDir, "resources", "images", image.encode("utf-8"))
        else:
                icon = image.encode("utf-8")
                
        try:
            name = int(item["name"])
            name = localizedString(name)
        except:
            name = item["name"]
                
        cname = "[COLOR gray][B]{0}[/B][/COLOR]".format(name)
        AddDir(cname ,item["url"], mode , icon)
    oGui.setEndOfDirectory()
def ListTB(lg):
    
    ok = show_main(lg)

def RemoveFavorties(url):
    
    list = comon.ReadList(favoritesFile) 
    for channel in list:
        if channel["url"].lower() == url.lower():
            list.remove(channel)
            break
			
    comon.SaveList(favoritesFile, list)
    xbmc.executebuiltin("XBMC.Container.Refresh()")

def AddNewFavortie():
    
    chName = GetKeyboardText("{0}".format(localizedString(10014).encode('utf-8'))).strip()
    if len(chName) < 1:
            return
    chUrl = GetKeyboardText("{0}".format(localizedString(10015).encode('utf-8'))).strip()
    if len(chUrl) < 1:
            return
		
    favList = comon.ReadList(favoritesFile)
    for item in favList:
            if item["url"].lower() == url.lower():
                    xbmc.executebuiltin("Notification({0}, '{1}' {2}, 5000, {3})".format(AddonName, chName, localizedString(10011).encode('utf-8'), icon))
                    return
			
    data = {"url": chUrl, "image": "", "name": chName.decode("utf-8")}
    favList.append(data)
    if comon.SaveList(favoritesFile, favList):
            xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}?mode=30&url=favorites')".format(AddonID))

############################################################################################
#    Modulo ricerca    

def sch_global(string,live=False):
    
    #0 - search in italian channels
    sch_m3u(os.path.join(chanDir, "it.txt"),string,localizedString(10052).encode('utf-8'),live=live)
    sch_m3u(os.path.join(chanDir, "vpnit.txt"),string,localizedString(10051).encode('utf-8'),live=live)
    sch_m3u(os.path.join(chanDir, "w_it.txt"),string,localizedString(10054).encode('utf-8'),live=live)
    
    # 1 - search in download folder
    if not xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path') == "":
        DD = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('download_path')
    else:
        DD = DFolder 
    
    PMFolder(DD,string,live=live)
    
    # 2 - search in m3ulist-index
    list = comon.ReadList(playlistsFile2)
    for channel in list:
        url = channel["url"]
        sname = comon.BBTagRemove(channel["name"]).replace("_"," ").replace("%20"," ").lower()
        sch_m3u(url,string,sname,live=live)

    # 3 - search in folder/xml-index
    listDir = comon.ReadList(playlistsFile4)
    
    for fold in listDir:
        name = fold["name"]

        try:
            t = fold["type"]
        except:
            t = ""
        try:
            e = fold["exclude"]
        except:
            e = ""
        
        if e == "":
            if t == "xml":
                OpenXML(fold["url"],string,live=live)
            elif t == "page":
                findm3u(fold["url"],string,live=live)
            else:
                PMFolder(fold["url"],string,live=live)
        
def sch_folder(url,string):
    
    string = string.lower()
    PMFolder(url,string)

def sch_xml(url,string):
    
    string = string.lower()
    OpenXML(url,string)

def sch_m3u(url,string,sname,live=False):
    oGui = cGui()
    try:
        urldec = base64.decodestring(url)
        if comon.check_url(urldec):
            url = urldec
    except:
        pass
    
    if comon.check_url(url):
        tmp = TempFileName(url)
	tcache = 18000
	
	if os.path.isfile(tmp):
            t = time.time() - os.path.getmtime(tmp)
        else :
            t = 0
        
        list = [ ]
        
	if os.path.isfile(tmp) and t < tcache:
            list = comon.m3u2list(tmp)
        else :   
            content = comon.OpenURL(url)
            if len(content)>0:
                try:
                    comon.write_file(tmp, content)
                    list = comon.m3u2list(tmp)
                except:
                    pass
            if len(list)<1:
                list = comon.m3u2list(url)
    else:            
        list = comon.m3u2list(url)
    
    for channel in list:
        name = channel["display_name"]
        name = comon.BBTagRemove(name) 
        Name = name
        name = name.replace("_"," ").lower().strip()
        url = channel["url"].strip()
        ext = "." + url.split(".")[-1].strip()
        EXT = EXTV + EXTA
        
        if not bool(ext in EXT) or not live:
        
            if name.find(string)>-1:
                if channel.get("tvg_logo", ""):
                    if comon.check_url(channel.get("tvg_logo", "")):
                        iconname = channel.get("tvg_logo", "")
                    else:
                        logo = channel.get("tvg_logo", "")
                        iconname = "http://kodilive.eu/logo/" + logo
                else :
                    iconname = TVICO

                listName = "  " + "[CR][I][COLOR blue][LIGHT]* {0}[/COLOR]".format(localizedString(10004).encode('utf-8')) + " -->  [COLOR yellow]{0}[/COLOR][/I][/LIGHT]".format(sname)
                cname = "[COLOR orange][B]{0}[/B][/COLOR]".format(Name) + listName
                if live or not bool(ext in EXT):
                    FastDir(cname,url,3,iconname,res=True,isFolder=False)
                else:
                    AddDir(cname,url,3,iconname,isFolder=False)
    oGui.setEndOfDirectory()
def sch_exclude(url, listFile, key):
    
    list = comon.ReadList(listFile)

    for channel in list:    
        if channel["url"].lower() == url.lower():
            channel["exclude"] = key
            break
        else:
            try:
                ure = base64.b64encode(url)
            except:
                ure = ""
            
            if channel["url"] == ure:
                channel["exclude"] = key
                break
            
    if comon.SaveList(listFile, list):
        xbmc.executebuiltin("XBMC.Container.Refresh()")

##########################
# Play Opus Channel

def Opus(cid):
    
    cid = cid.split(":")[1]
    #spli = cid.split(":")
    #pid = spli[2].strip()
    #cid = spli[1].strip()
    
    from xml.dom import minidom
    data = comon.OpenURL('http://racacaxtv.ga/mega.php?category=VG91dGVz&pls=RnJhbmNvcGhvbmVz')
    
    try:
        xmldoc = minidom.parseString(data)
        Data = xmldoc.getElementsByTagName('items')

        for d in Data:
            Item = d.getElementsByTagName("item")

            for node in Item:

                itemlink = node.getElementsByTagName("link")[0].childNodes[0].nodeValue.encode("UTF-8")
        
        itemlink = itemlink.replace("/394000/","/").strip()
        itemlink = itemlink.replace("/2027/","/" + cid + "/").strip()
        return itemlink
    except:
        return ""
        pass    
        
##########################
# Luci Rosse

def Pornazzi(url):
    
        global koditools
        urlbase = "http://www.iptvultra.com"
        data = comon.cachepage(urlbase,360000,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'})
        #data = comon.OpenURL(urlbase)
        patron = 'class="rctitles2".+?href="(.+?)">(.+?)</a>'
        matches = re.compile(patron, re.DOTALL).findall(data)

        for url1, name in matches:
        
                       #xbmc.log(titolo)
            #xbmc.log(url)
            #xbmc.log(scrapedimg)
            
            AddDir(name,url,3,iconname,isFolder=False)

def tvoggi():
    
    from resources.sayfalar.turkvod_org import Categories 
    Categories(params)
       
def SetteGiorniTV(day=""):
    if day == "":
        import datetime
        from datetime import date, timedelta
        start = date.today()
        icon = ""
        
        Link = ["/","/domani/","/dopodomani/","/giorno-3/","/giorno-4/","/giorno-5/","/giorno-6/"]
        Days = ["Oggi","Domani","Dopodomani","Fra 3 giorni","Fra 4 giorni","Fra 5 giorni","Fra 6 giorni"]
        
        AddDir("[COLOR gray][B]" + str(date.today()) + " - Film in TV " + Days[0] + "[/B][/COLOR]", Link[0], 75, icon, isFolder=True)
        for add in range(1, 7):
            future = start + timedelta(days=add)
            AddDir("[COLOR gray][B]" + str(future) + " - Film in TV " + Days[add] + "[/B][/COLOR]", Link[add], 75, icon, isFolder=True)
    else:
        if day == "/":
            AddDir("[COLOR red][B]ORA IN ONDA[/B][/COLOR]", day, 74, "http://a2.mzstatic.com/eu/r30/Purple/v4/3d/63/6b/3d636b8d-0001-dc5c-a0b0-42bdf738b1b4/icon_256.png", isFolder=True) 
        AddDir("[COLOR azure][B]Mattina[/B][/COLOR]", day + "?range=mt", 74, "http://www.creattor.com/files/23/787/morning-pleasure-icons-screenshots-17.png", isFolder=True)
        AddDir("[COLOR azure][B]Pomeriggio[/B][/COLOR]", day + "?range=pm", 74, "http://icons.iconarchive.com/icons/custom-icon-design/weather/256/Sunny-icon.png", isFolder=True)
        AddDir("[COLOR azure][B]Preserale[/B][/COLOR]", day + "?range=pr", 74, "https://s.evbuc.com/https_proxy?url=http%3A%2F%2Ftriumphbar.com%2Fimages%2Fhappyhour_icon.png&sig=ADR2i7_K2FSfbQ6b3dy12Xjgkq9NCEdkKg", isFolder=True)
        AddDir("[COLOR azure][B]Prima serata[/B][/COLOR]", day + "?range=ps", 74, "http://icons.iconarchive.com/icons/icons-land/vista-people/256/Occupations-Pizza-Deliveryman-Male-Light-icon.png", isFolder=True)
        AddDir("[COLOR azure][B]Seconda serata[/B][/COLOR]", day + "?range=ss", 74, "http://orig03.deviantart.net/6889/f/2014/079/7/b/movies_and_popcorn_folder_icon_by_matheusgrilo-d7ay4tw.png", isFolder=True)
        AddDir("[COLOR azure][B]Notte[/B][/COLOR]", day + "?range=nt", 74, "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Status-weather-clear-night-icon.png", isFolder=True)
        
################################################################################################

def checkforupdates(url,loc,aut):
    
    from resources.lib import ziptools
    xbmc.log('Start check for updates')
    try:
        data = urllib2.urlopen(url).read()
        xbmc.log('read xml remote data:' + data)
    except:
        data = ""
        xbmc.log('fail read xml remote data:' + url )
    try:
        f = open(loc,'r')
        data2 = f.read().replace("\n\n", "")
        f.close()
        xbmc.log('read xml local data:' + data2)
    except:
        data2 = ""
        xbmc.log('fail read xml local data')

    version_publicada = find_single_match(data,"<version>([^<]+)</version>").strip()
    tag_publicada = find_single_match(data,"<tag>([^<]+)</tag>").strip()

    version_local = find_single_match(data2,"<version>([^<]+)</version>").strip()
    tag_local = find_single_match(data,"<tag>([^<]+)</tag>").strip()

    try:
        numero_version_publicada = int(version_publicada)
        xbmc.log('number remote version:' + version_publicada)
        numero_version_local = int(version_local)
        xbmc.log('number local version:' + version_local)
    except:
        version_publicada = ""
        xbmc.log('number local version:' + version_local )
        xbmc.log('Check fail !@*')
            
    if version_publicada!="" and version_local!="":
        if (numero_version_publicada > numero_version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/lastupdate.zip'                
            UPDATE_URL = 'https://netcologne.dl.sourceforge.net/project/e2-orhantv1/plugin.video.OTV_MEDIA-' + tag_publicada + '.zip'
            xbmc.log('START DOWNLOAD UPDATE:' + UPDATE_URL)
                
            DownloaderClass(UPDATE_URL,dest)  
                  
            from resources.lib import ziptools
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                
            line7 = 'New version installed .....'
            line8 = 'Version: ' + tag_publicada 
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)
                
            if os.remove( dest ):
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            xbmc.sleep(1500)

    url = REMOTE_VERSION_FILE2
    loc = LOCAL_VERSION_FILE2
        
    try:
        data = urllib2.urlopen(url).read()
        xbmc.log('read xml remote data:' + data)
    except:
        data = ""
        xbmc.log('fail read xml remote data:' + url )
    try:
        f = open(loc,'r')
        data2 = f.read().replace("\n\n", "")
        f.close()
        xbmc.log('read xml local data:' + data2)
    except:
        data2 = ""
        xbmc.log('fail read xml local data')
            
    version_publicada = find_single_match(data,"<version>([^<]+)</version>").strip()
    tag_publicada = find_single_match(data,"<tag>([^<]+)</tag>").strip()

    version_local = find_single_match(data2,"<version>([^<]+)</version>").strip()
    dinamic_url = find_single_match(data,"<url>([^<]+)</url>").strip()
        
    try:
        numero_version_publicada = int(version_publicada)
        xbmc.log('number remote version:' + version_publicada)
        numero_version_local = int(version_local)
        xbmc.log('number local version:' + version_local)
    except:
        version_publicada = ""
        xbmc.log('number local version:' + version_local )
        xbmc.log('Check fail !@*')
            
    if version_publicada!="" and version_local!="":
        if (numero_version_publicada > numero_version_local):

            extpath = os.path.join(xbmc.translatePath("special://home/addons/")) 
            dest = addon_data_dir + '/temp.zip'  
                    
            urllib.urlretrieve(dinamic_url,dest)
            xbmc.log('START DOWNLOAD PARTIAL UPDATE:' + dinamic_url) 
                    
            from resources.lib import ziptools
            unzipper = ziptools.ziptools()
            unzipper.extract(dest,extpath)
                    
            line7 = 'Plugin data updated .....'
            line8 = 'Description: ' + tag_publicada
            xbmcgui.Dialog().ok('OTV_MEDIA', line7, line8)
                    
            if os.remove( dest ): 
                xbmc.log('TEMPORARY ZIP REMOVED')
            xbmc.executebuiltin("UpdateLocalAddons")
            xbmc.executebuiltin("UpdateAddonRepos")
            u = False
        else:
            xbmc.log('No partial updates are available' )
            u = True
                        
    if aut<1 and u:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(localizedString(10106).encode('utf-8') + " :",localizedString(10044).encode('utf-8'), 4500, icon))
        xbmc.log('Check updates:No updates are available' )
    
    #clean : old file remove
    if os.path.isfile(os.path.join(addonDir, "teleboy.py")):
        os.remove(os.path.join(addonDir, "teleboy.py"))
    if os.path.isfile(os.path.join(addonDir, "teleboy.pyo")):
        os.remove(os.path.join(addonDir, "teleboy.pyo"))
    if os.path.isfile(os.path.join(addonDir, "fileDownloader.py")):
        os.remove(os.path.join(addonDir, "fileDownloader.py"))
    if os.path.isfile(os.path.join(addonDir, "fileDownloader.pyo")):
        os.remove(os.path.join(addonDir, "fileDownloader.pyo"))   
    if os.path.isfile(os.path.join(addonDir, "ziptools.py")):
        os.remove(os.path.join(addonDir, "ziptools.py"))
    if os.path.isfile(os.path.join(addonDir, "ziptools.pyo")):
        os.remove(os.path.join(addonDir, "ziptools.pyo"))    
    if os.path.isfile(os.path.join(addonDir, "knownpaths.py")):
        os.remove(os.path.join(addonDir, "knownpaths.py"))
    if os.path.isfile(os.path.join(addonDir, "knownpaths.pyo")):
        os.remove(os.path.join(addonDir, "knownpaths.pyo"))     
    if os.path.isfile(os.path.join(libDir, "checkbad.py")):
        os.remove(os.path.join(libDir, "checkbad.py"))
    if os.path.isfile(os.path.join(libDir, "checkbad.pyo")):
        os.remove(os.path.join(libDir, "checkbad.pyo"))

# Ricerca automatica aggiornamenti
Tfile = os.path.join(addon_data_dir, 'time.txt')

if Addon.getSetting('autoupdate') == "true":

    if os.path.isfile(Tfile):
        t = time.time() - os.path.getmtime(Tfile)
        if t > 3600 :
            checkforupdates(REMOTE_VERSION_FILE, LOCAL_VERSION_FILE,36000-t)
            comon.write_file(Tfile , '*')
    else: 
        checkforupdates(REMOTE_VERSION_FILE, LOCAL_VERSION_FILE,0)
        comon.write_file(Tfile  , '*')



def Play_f4mProxy(url, name, iconimage):
    oGui = cGui()
    maxbitrate = Addon.getSetting('BitRateMax')
    if Addon.getSetting('use_simple') == "true":
        simpledownloader = True
    else:
        simpledownloader = False
    sys.path.insert(0, f4mProxy)
    from F4mProxy import f4mProxyHelper
    player=f4mProxyHelper()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
    if streamtype == "HLS":
        maxbitrate = 9000000
    player.playF4mLink(url, name, None, True, maxbitrate, simpledownloader, None, streamtype, False, None, iconimage)    
    oGui.setEndOfDirectory()

def getSoup(url,data=None):
        global viewmode,tsdownloader
        tsdownloader=False
        if url.startswith('http://') or url.startswith('https://'):
            enckey=False
            if '$$TSDOWNLOADER$$' in url:
                tsdownloader=True
                url=url.replace("$$TSDOWNLOADER$$","")
            if '$$LSProEncKey=' in url:
                enckey=url.split('$$LSProEncKey=')[1].split('$$')[0]
                rp='$$LSProEncKey=%s$$'%enckey
                url=url.replace(rp,"")
                
            data =makeRequest(url)
            if enckey:
                    import pyaes
                    enckey=enckey.encode("ascii")
                    print enckey
                    missingbytes=16-len(enckey)
                    enckey=enckey+(chr(0)*(missingbytes))
                    print repr(enckey)
                    data=base64.b64decode(data)
                    decryptor = pyaes.new(enckey , pyaes.MODE_ECB, IV=None)
                    data=decryptor.decrypt(data).split('\0')[0]
                    #print repr(data)
            if re.search("#EXTM3U",data) or 'm3u' in url:
#                print 'found m3u data'
                return data
        elif data == None:
            if not '/'  in url or not '\\' in url:
#                print 'No directory found. Lets make the url to cache dir'
                url = os.path.join(communityfiles,url)
            if xbmcvfs.exists(url):
                if url.startswith("smb://") or url.startswith("nfs://"):
                    copy = xbmcvfs.copy(url, os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    if copy:
                        data = open(os.path.join(profile, 'temp', 'sorce_temp.txt'), "r").read()
                        xbmcvfs.delete(os.path.join(profile, 'temp', 'sorce_temp.txt'))
                    else:
                        addon_log("failed to copy from smb:")
                else:
                    data = open(url, 'r').read()
                    if re.match("#EXTM3U",data)or 'm3u' in url:
#                        print 'found m3u data'
                        return data
            else:
                addon_log("Soup Data not found!")
                return
        if '<SetViewMode>' in data:
            try:
                viewmode=re.findall('<SetViewMode>(.*?)<',data)[0]
                xbmc.executebuiltin("Container.SetViewMode(%s)"%viewmode)
                print 'done setview',viewmode
            except: pass
        return BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

 
def get_params():
    
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?','')
        if (params[len(params)-1] == '/'):
                params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
                splitparams = {}
                splitparams = pairsofparams[i].split('=')
                if (len(splitparams)) == 2:
                        param[splitparams[0].lower()] = splitparams[1]
    return param

params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
station = None
user_id = None                        

try:                                                                                                                
          
    url = urllib.unquote_plus(params["url"])
    
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass
try:        
    mode = int(params["mode"])
except:
    pass
try:        
    user_id = params["userid"]
except:
    pass
try:        
    rec_id = params["recid"]
except:
    pass    
try:        
    station = urllib.unquote_plus(params["station"])
except:
    pass    
    
try:        
    description = urllib.unquote_plus(params["description"])
except:
    pass
try:
    streamtype = urllib.unquote_plus(params["streamtype"])
except:
    pass                      



if url and url.find("karwan.tv") >= 0:
    from resources.sayfalar.iptvbox import kurdtv
    kurdtv()
    url = None
if url and url.find("weeb.tv") >= 0:
    from resources.sayfalar.iptvbox import weebtv
    weebtv()
    url = None
elif url and url.find("tvmak.com") >= 0:
    from resources.sayfalar.iptvbox import arnavutchan
    arnavutchan()
    url = None
elif url and url.find("peers.tv") >= 0:
    from resources.sayfalar.iptvbox import peerstv
    peerstv()
    url = None
elif url and url.find("Almankostenlos") >= 0:
    from resources.sayfalar.iptvbox import Almanlivestream
    Almanlivestream()
    url = None
elif url and url.find("foxtvturk") >= 0:
    from resources.sayfalar.fox_com_tr import showGenre
    showGenre()
    url = None
elif url and url.find("tv8turk") >= 0:
    from resources.sayfalar.tv8_com_tr import showGenre
    showGenre()
    url = None
elif url and url.find("kanaldturk") >= 0:
    from resources.sayfalar.kanald_com_tr import showGenre
    showGenre()
    url = None
elif url and url.find("startvturk") >= 0:
    from resources.sayfalar.startv_com_tr import showGenre
    showGenre()
    url = None
elif url and url.find("showtvturk") >= 0:
    from resources.sayfalar.showtv_com_tr import showGenre
    showGenre()
    url = None
elif url and url.find("LSProEncKey=") >= 0:
    from resources.sayfalar.canlitv_mobi import CanLiTVlive
    CanLiTVlive()

    url = None
    
elif url and url.find("atvturk") >= 0:
    from resources.sayfalar.atv_com_tr import showGenre
    showGenre()
    url = None
    
elif url and url.find("trtturk") >= 0:
    from resources.sayfalar.trt_net_tr import showGenre
    showGenre()
    url = None
elif url and url.find("liveonlinetv247") >= 0:
    from resources.sayfalar.liveonlinetv247 import liveonlinetv247
    liveonlinetv247()
    url = None
elif url and url.find("opus.re") >= 0:
    from resources.sayfalar.saraydorf_tv import opusdorf
    opusdorf()
    xbmcplugin.endOfDirectory(int(sys.argv[1]), succeeded=True)
    sys.exit()    
elif url and url.find("racacaxtv.ga") >= 0:
    from resources.sayfalar.saraydorf_tv import racacaxtvga
    racacaxtvga()
    
    xbmc.executebuiltin("Container.SetViewMode(500)")
    xbmcplugin.endOfDirectory(int(sys.argv[1]), succeeded=True)
    sys.exit()     
    


if mode == None or url == None or len(url) < 1:
    main()
    
elif mode == 1:
    from PLUG  import *     
   
elif mode == 2:
    m3uCategory(url)    
elif mode == 4 or mode == 51:
    m3uCategory(url,False)
elif mode == 63 or mode == 70:
    OpenXML(url)
elif mode == 3 or mode == 32:
        PlayUrl(name, url, iconimage)
elif mode == 5:    
    Play_f4mProxy(url, name, iconimage)
elif mode == 6 or mode == 7 or mode == 59:
    comon.StartDowloader(url,name,mode,DFolder)                 
elif mode == 57 or mode == 72:
    comon.StopDowloader(url,name,mode,DFolder)
elif mode == 58 or mode == 71:
    comon.DeletePartialDowload(url,name,mode,DFolder)
elif mode == 10:
    # deleted
    sys.exit()
elif mode == 20:
    AddNewList()
elif mode == 21 or mode == 54 or mode == 60 or mode == 64:
    PMFolder( url )
elif mode == 22:
    RemoveFromLists(url)
elif mode == 23:
    ChangeName(name,playlistsFile2,"name",10004)
elif mode == 24:
    ChangeUrl(url,playlistsFile2,"url",10005)
elif mode == 61:
    ChangeName(name,playlistsFile4,"name",10004)        
elif mode == 69:
    ChangeName(name,favoritesFile,"name",10004)
elif mode == 25:
    importList()
elif mode == 26:
    if os.path.isfile( playlistsFile3 ) :
        if os.path.isfile( playlistsFile2 ) : os.remove( playlistsFile2 )
        shutil.copyfile( playlistsFile3, playlistsFile2 )
        xbmc.sleep ( 200 )
        os.remove( playlistsFile3 )
        xbmc.executebuiltin("XBMC.Container.Update('plugin://{0}')".format(AddonID))
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,localizedString(10125).encode('utf-8'), 3600, icon)) 
    else:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName,localizedString(10126).encode('utf-8'), 3600, icon))
elif mode == 30:
    ListFavorites()
elif mode == 31: 
    AddFavorites(url, iconimage, name)
elif mode == 55:
    RemoveDirFromLists(url,name)
elif mode == 56:
    os.remove( os.path.join(pwdir, base64.standard_b64encode(url))) 
    xbmc.executebuiltin("XBMC.Container.Refresh()")
elif mode == 33:
    RemoveFavorties(url)
elif mode == 34:
    AddNewFavortie()
elif mode == 85:
    ListSub(Turkish)
elif mode == 86:
    ListSub(ArslanTV)
elif mode == 35:
    ListSub(Italian)
elif mode == 36:
    ListSub(French)
elif mode == 37:
    ListSub(German)
elif mode == 38:
    ListSub(English)
elif mode == 39:
    PM_index()
elif mode == 40:
    comon.DelFile(playlistsFile2)
    sys.exit()
elif mode == 41:
    comon.DelFile(favoritesFile)
    sys.exit()
elif mode == 42:
    write_xml()
    sys.exit()
elif mode == 43:
    restore_xml()
    sys.exit()   
elif mode == 44:
    remove_xml()
    sys.exit()
elif mode == 45:        
    clean_cache()
    sys.exit()
elif mode == 46:       
    checkforupdates(REMOTE_VERSION_FILE, LOCAL_VERSION_FILE,0)
    if Addon.getSetting('autoupdate') == "true":
        comon.write_file(Tfile , '*')        
    sys.exit()
elif mode == 47:
    xbmc.executebuiltin("StopPVRManager")
    xbmc.executebuiltin("StartPVRManager") 
    sys.exit()
elif mode == 48:
    comon.Open_Netflix()        
elif mode == 49:
    comon.Open_Paypal()
elif mode == 50:
    print '--- Playing "{0}". {1}'.format(name, url)
    listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
    listitem.setInfo(type="Video", infoLabels={ "Title": name })
    xbmc.Player().play( url , listitem)
elif mode == 52:
    comon.DeleteFile(url,name)
elif mode == 53:
    string = GetKeyboardText(localizedString(10203).encode('utf-8'), name)
    if len(string) < 1:
        sys.exit()
    else:
        nurl = url.replace(name,string)
        xbmcvfs.rename(os.path.join(url) ,os.path.join(nurl))
        xbmc.executebuiltin("XBMC.Container.Refresh()")
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(name, localizedString(10202).encode('utf-8'), 5200, icon))
        sys.exit()
elif mode == 62:
    cook = os.path.join(addonDir,'resources','cookie.dat')
    if os.path.isfile(cook):
        os.remove(cook)
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA : ","Teleboy cookie has been deleted!", 4700, icon))
    sys.exit()
elif mode == 65:
    title = localizedString(10250).encode('utf-8')
    string = GetKeyboardText(title, "")
    if len(string) >0:
        string = string.lower()
        if url == "search":
            sch_global(string)
        else:
            sch_folder(url,string)
elif mode == 66:
    title = localizedString(10250).encode('utf-8')
    string = GetKeyboardText(title, "")
    if len(string) >0:
        sch_xml(url,string)
elif mode == 73:
    sch_global(url,live=True)
elif mode == 76:
    sch_global(name,live=False)
elif mode == 67:
    sch_exclude(url, playlistsFile4, "yes")
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA : ","Folder " + name + " to global research excluded!", 4000, icon))
    sys.exit()
elif mode == 68:
    sch_exclude(url, playlistsFile4, "")
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%("OTV_MEDIA: ","Folder " + name + " to global research included!", 4000, icon))
    sys.exit()
elif mode == 74:
    tvoggi(url)
elif mode == 75:    
    SetteGiorniTV(url)
elif mode == 77:
    Pornazzi(url)
    xbmc.executebuiltin("Container.SetViewMode(500)")
elif mode == 78:
    import FreeTV
    FreeTV.PlayOtherUrl ( url, name )
elif mode==12:
    
    if  'plugin' in url:
         url = '' + url
         xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
         xbmc.executebuiltin('Dialog.Close(all, true)')
    
    PlayUrl(name, url, iconimage)
   
elif mode == 27:
    from teleboy import *
    try:
        json = get_videoJson( user_id, station)
        if not json:
            exit( 1)

        title = json["data"]["epg"]["current"]["title"]
        url = json["data"]["stream"]["url"]
        if not url: 
            exit( 1)
        img = get_stationLogoURL( station )
        Player = xbmcaddon.Addon('plugin.video.OTV_MEDIA').getSetting('player')
        if  Addon.getSetting('player') == "true":
            play_url2( url, title, img )  
        else:
            play_url( url, title, img )
    except:
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(AddonName, "Swiss IP needed. Your bags ready!", 3600, icon))
elif mode == 28:
    from teleboy import *
    show_recordings(user_id)
    #make_list()
elif mode == 29:
    from teleboy import *
    url = "stream/record/%s" % rec_id
    json    = fetchApiJson( user_id, url)
    title = json["data"]["record"]["title"]
    url   = json["data"]["stream"]["url"]
    img = REC_ICON
    play_url( url, title, img )
elif mode == 79:
    findm3u(url)
elif mode == 80:
    import control                         
elif mode==100:
    xml_settings = os.path.join(addon_data_dir, "settings.xml")
    if os.path.isfile(xml_settings):
        os.remove(xml_settings)
        sys.exit()
          
elif mode==17 or mode==117:
    from PLUG  import * 
elif mode==105:
    from resources.sayfalar.iptvbox import iptvultra
    iptvultra()
elif mode==199:
    from resources.sayfalar.turkvod_org import showGenre2
    showGenre2(url)

elif mode==198:
    from PLUG  import getSources
    addon_log("getSources")
    getSources()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

elif mode==398:
    from resources.lib.indexers import bennustreams
    if worker == '1': bennustreams.indexer().getx(url, worker=True)
    else: bennustreams.indexer().getx(url)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))


