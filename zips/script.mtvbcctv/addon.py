import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] CCTV & Webcams[/COLOR][/B]', ['[B][COLOR=green]CCTV & Web Cams 1[/COLOR][/B]', '[B][COLOR=green]CCTV & Web Cams 2[/COLOR][/B]', '[B][COLOR=green]NASA Live Streams[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.goodfellas/?fanart=http%3a%2f%2fwww.pixhoster.info%2ff%2f2016-09%2f1fa780e2d827b35ee5038bf8b2c8dd63.png&mode=1&name=Web%20Cams&url=http%3a%2f%2fgoo.gl%2fZqroXR",return)')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ukturk/?description&fanart=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.ukturk%5cfanart.jpg&iconimage=http%3a%2f%2fukturk.offshorepastebin.com%2fUKTurk%2fthumbs%2fnew%2fUk%2520turk%2520thumbnails%2520cctv.jpg&mode=1&name=CCTV&url=http%3a%2f%2fukturk.offshorepastebin.com%2fUKTurk%2fCCTV.txt",return)')

def function3():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ProjectCypher/?fanart=http%3a%2f%2fcypher-media.com%2fcypher%2fimages%2ffanart.jpg&mode=1&name=%5bB%5d%5bCOLOR%20yellow%5d---%5b%2fCOLOR%5d%20%5bCOLOR%20red%5dNASA%5b%2fCOLOR%5d%20%5bCOLOR%20white%5d%20Live%20Streams%20%5bCOLOR%20blue%5dDirectory%5b%2fCOLOR%5d%5b%2fCOLOR%5d%20%5bCOLOR%20yellow%5d---%5b%2fCOLOR%5d%5b%2fB%5d&url=http%3a%2f%2fcypher-media.com%2fcypher%2fcyphernasa.xml%24%24LSProEncKey%3dcypher%24%24",return)')

menuoptions()