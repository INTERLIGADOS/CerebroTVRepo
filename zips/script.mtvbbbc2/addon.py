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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] BBC 2 Links[/COLOR][/B]', ['[B][COLOR=green]      BBC2 HD[/COLOR][/B]' , '[B][COLOR=green]      BBC2 SD[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_two_hd&mode=203&name=BBC+Two&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_two.png&description=&subtitles_url=&logged_in=False")')

def function2():   
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBBC%20Two%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fd6b64a19b548bf941f57cdd4c5d71904.m3u8")')

menuoptions()