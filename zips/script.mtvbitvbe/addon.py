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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] ITV Be Links[/COLOR][/B]', ['[B][COLOR=green]      ITV Be HD[/COLOR][/B]' , '[B][COLOR=green]      ITV Be SD[/COLOR][/B]'])
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
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.itv/?url=http%3A%2F%2Fitvbeliveios-i.akamaihd.net%2Fhls%2Flive%2F219078%2Fitvlive%2FITVBE%2Fmaster_Main1800.m3u8&mode=7&name=ITVBe+Live&iconimage=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.itv%5Cart%2F8.jpg")')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.notfilmon/?url=http%3A%2F%2Fwww.filmon.com%2Fgroup%2Fuk-live-tv&mode=2&name=ITVBe&iconimage=https%3A%2F%2Fstatic.filmon.com%2Fassets%2Fchannels%2F3211%2Fbig_logo.png&description=3211&group=UK+LIVE+TV")')


menuoptions()