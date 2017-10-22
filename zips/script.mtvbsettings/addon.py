import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Settings[/COLOR][/B]', ['[B][COLOR=green]      SPMC/Kodi Settings[/COLOR][/B]' , '[B][COLOR=green]      All Video Add-On`s[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
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
    xbmc.executebuiltin('ActivateWindow(Settings)')

def function2():
    xbmc.executebuiltin('ActivateWindow(10025,addons://sources/video/,return)')


menuoptions()
#xbmc.executebuiltin("Notification(CerebroTV,MAY TAKE 2-3 CLICKS, ....,5000,)")
#xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dLifetime%2bUK%26url%3dmpd%253A%252F%252Ff31ff373857e6b6e0bc44ae55da2e208.m3u8%26cfg%3dtvone1.tv.cfg%2540Streams%2540Channels%26videoTitle%3dLifetime%2bUK%26director%3dtvone1.tv%26genre%3dLive%2bTV%26referer%3dmpd%253A%252F%252Ff31ff373857e6b6e0bc44ae55da2e208.m3u8%26definedIn%3dtvone1.tv.cfg%26type%3drss&mode=1",return)')
