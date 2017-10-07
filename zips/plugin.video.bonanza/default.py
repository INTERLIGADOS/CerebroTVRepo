'''
    IPTV BONANZA
    Copyright (C) 2017 BONANZA
    Based on Ultimate IPTV by  Whitecream - All credits to him!
    
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


__scriptname__ = "IPTV BONANZA"
__author__ = "BONANZA"
__scriptid__ = "plugin.video.bonanza"
__version__ = "1.0.0"

import urllib, urllib2, re, gzip, socket
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,sys, os


dialog = xbmcgui.Dialog()
progress = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon(id=__scriptid__)
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
socket.setdefaulttimeout(10)

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)
bonanzaicon = xbmc.translatePath(os.path.join(rootDir, 'icon.png'))
profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
cookiePath = os.path.join(profileDir, 'cookies.lwp')


if not os.path.exists(profileDir):
    os.makedirs(profileDir)

urlopen = urllib2.urlopen
Request = urllib2.Request


def notify(header=None, msg='', duration=5000):
    if header is None: header = 'IPTV BONANZA'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, bonanzaicon)
    xbmc.executebuiltin(builtin)


def getHtml(url, referer=None, hdr=None, data=None):
    if not hdr:
        req = Request(url, data, headers)
    else:
        req = Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    if data:
        req.add_header('Content-Length', len(data))
    response = urlopen(req, timeout=20)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO( response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        f.close()
    else:
        data = response.read()    
    response.close()
    return data


def addPlayLink(name, url, mode, iconimage):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    #liz.setProperty('IsPlayable', 'true')
    liz.setInfo(type="Video", infoLabels={"Title": name})
    video_streaminfo = {'codec': 'h264'}
    liz.addStreamInfo('video', video_streaminfo)
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=False)
    return ok
    

def addDir(name, url, mode, iconimage, Folder=True):
    if url.startswith('plugin'):
        u = url
    else:
        u = (sys.argv[0] +
             "?url=" + urllib.quote_plus(url) +
             "&mode=" + str(mode) +
             "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    fanart = os.path.join(rootDir, 'fanart.jpg')
    liz.setArt({'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok


def GETFILTER():
    filterset = int(addon.getSetting('filterset')) + 1
    txtfilter = addon.getSetting('txtfilter' + str(filterset))
    return txtfilter


def OPENSETTINGS():
    addon.openSettings()
    xbmc.executebuiltin('Container.Refresh')


def INDEX():
    MAIN('http://iptvsatlinks.blogspot.com/search?max-results=40')


def MAIN(url):
    txtfilter = GETFILTER()
    if not txtfilter:
        txtfilter = "none"
    addDir('[COLOR blue][B]Current filter:[/B] '+txtfilter+'[/COLOR]', '', 5, bonanzaicon, Folder=False)
    addDir('IPTV M3u Stream Hunters', 'http://www.m3uliste.pw/', 1, 'http://www.m3uliste.pw/files/.logo-lw-scaled.jpg.png')
    
    html = getHtml(url)
    blogpage = re.compile("content='([^']+)' itemprop='image_url'.*?href='([^']+)'>([^<]+)<", re.DOTALL | re.IGNORECASE).findall(html)
    for img, url, name in blogpage:
        addDir(name, url, 1, img)
    try:
        nextp = re.compile("'blog-pager-older-link' href='([^']+)'", re.DOTALL | re.IGNORECASE).findall(html)[0]
        nextp = nextp.replace('&amp;','&')
        addDir('Next Page', nextp, 0, bonanzaicon)
    except: pass
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PAGE(url):
    html = getHtml(url)
    if ('m3uliste' in url):
        blogpage = re.compile('<div\s+class=\"zs-accordion\s+selected\"(.*?)EXTINF', re.DOTALL | re.IGNORECASE).findall(html)[0]
    else:
        blogpage = re.compile('<div class="code">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(html)[0]
    if '#EXTINF' in blogpage:
        blogpage = blogpage.replace('<br />', '\n').replace('&nbsp;','').replace('&amp;','&')
        parsem3u(blogpage)
    else:
        txtfilter = GETFILTER()
        if txtfilter:
            addDir('[COLOR blue]Search all links for: '+txtfilter+'[/COLOR]', url, 4, bonanzaicon)
        iptvlinks = re.compile("(http[^<]+)", re.DOTALL | re.IGNORECASE).findall(blogpage)
        i = 1
        for link in iptvlinks:
            link = link.replace('&amp;','&')
            name = 'Link ' + str(i) + ': ' + link
            addDir(name, link, 2, bonanzaicon)
            i = i + 1
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def SEARCHLINKS(url):
    txtfilter = GETFILTER()
    count = 0
    dp = xbmcgui.DialogProgress()
    dp.create("Searching IPTV lists","Searching for:",txtfilter)
    html = getHtml(url)
    if ('m3uliste' in url):
        blogpage = re.compile('<div\s+class=\"zs-accordion\s+selected\"(.*?)EXTINF', re.DOTALL | re.IGNORECASE).findall(html)[0]
    else:
        blogpage = re.compile('<div class="code">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(html)[0]
    iptvlinks = re.compile("(http[^<]+)", re.DOTALL | re.IGNORECASE).findall(blogpage)
    addcount = 100 / len(iptvlinks)
    for link in iptvlinks:
        dp.update(int(count))
        link = link.replace('&amp;','&')
        try:
            listup = urllib.urlopen(link).getcode()
            if listup == 200:
                    m3u = getHtml(link)
                    links = parsem3u(m3u)
                    count = count + addcount
                    if links > 0:
                        addDir('---------------------', '', 1, bonanzaicon, Folder=False)
        except:
            count = count + addcount
            pass
    dp.close()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def IPTV(url):
    try:
        m3u = getHtml(url)
        parsem3u(m3u)
    except:
        addDir('Nothing found', '', '', '', Folder=False)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def parsem3u(html, sitechk=True):
    match = re.compile('#.+,(.+?)\n(.+?)\n').findall(html)
    txtfilter = txtfilter = GETFILTER()
    txtfilter = txtfilter.split(',') if txtfilter else []
    txtfilter = [f.lower().strip() for f in txtfilter]
    i = 0
    count = 0
    for name, url in match:
        status = ""
        url = url.replace('\r','')
        if not txtfilter or any(f in name.lower() for f in txtfilter):
            if sitechk:
                if i < 5:
                    try:
                        siteup = urllib.urlopen(url).getcode()
                        status = " [COLOR red]offline[/COLOR]" if siteup != 200 else " [COLOR green]online[/COLOR]"
                    except: status = " [COLOR red]offline[/COLOR]"
                    i += 1
            addPlayLink(name+status, url, 3, bonanzaicon)
            count += 1
    return count


def PLAY(url, title):
    playmode = int(addon.getSetting('playmode'))
    iconimage = xbmc.getInfoImage("ListItem.Thumb")

    if playmode == 0:
        stype = ''
        if '.ts' in url:
            stype = 'TSDOWNLOADER'
        elif '.m3u' in url:
            stype = 'HLSRETRY'
        if stype:
            from F4mProxy import f4mProxyHelper
            f4mp=f4mProxyHelper()
            xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
            f4mp.playF4mLink(url,name,proxy=None,use_proxy_for_chunks=False, maxbitrate=0, simpleDownloader=False, auth=None, streamtype=stype,setResolved=False,swf=None , callbackpath="",callbackparam="", iconImage=iconimage)
            return
    
    listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    listitem.setInfo('video', {'Title': name})
    listitem.setProperty("IsPlayable","true")
    xbmc.Player().play(url, listitem)


def getParams():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if params[len(params) - 1] == '/':
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = getParams()
url = None
name = None
mode = None
img = None


try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: img = urllib.unquote_plus(params["img"])
except: pass

if mode is None: INDEX()
elif mode == 0: MAIN(url)
elif mode == 1: PAGE(url)
elif mode == 2: IPTV(url)
elif mode == 3: PLAY(url, name)
elif mode == 4: SEARCHLINKS(url)
elif mode == 5: OPENSETTINGS()

