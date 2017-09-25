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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] More4 Links[/COLOR][/B]', ['[B][COLOR=green]      More4 SD[/COLOR][/B]' , '[B][COLOR=green]      More4 HD[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.sanctuary/?url=https%3A%2F%2Fwww.filmon.com%2Ftv%2Fmore4&mode=1201&name=More4+%7C+FilmOn")')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.echostreams/?url=more+4%0D%7CSPLIT%7Chttp%3A%2F%2Flive.softiptv.com%3A9900%2Flive%2Fjagdish%2Fjagdish%2F26200.ts&mode=3&name=%5BCOLOR+white%5DMore+4%0D%5B%2FCOLOR%5D&iconimage=C:\\Users\\bigla\\AppData\\Roaming\\Kodi\\addons\\plugin.video.echostreams\\icon.png&fanartimage=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.echostreams%5Cfanart.jpg")')


menuoptions()