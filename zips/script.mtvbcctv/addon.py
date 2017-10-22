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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.goodfellas/?fanart=http%3a%2f%2fwww.pixhoster.info%2ff%2f2016-09%2f1fa780e2d827b35ee5038bf8b2c8dd63.png&mode=1&name=Web%20Cams&url=http%3a%2f%2fgoo.gl%2fZqroXR",return)')

def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ProjectCypher/?action=directory&content=addons&url=http%3a%2f%2fcypher-media.com%2fcypher%2fcctv.xml",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ProjectCypher/?action=directory&content=addons&url=http%3a%2f%2fignorame",return)')

menuoptions()