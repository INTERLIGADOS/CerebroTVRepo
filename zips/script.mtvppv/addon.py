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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Appolo Streams[/COLOR][/B]', [
    '[B][COLOR=white]      UK Streams[/COLOR][/B]', 
    '[B][COLOR=white]      All Streams[/COLOR][/B] (with sports)'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 


def function1():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV[/COLOR]","GETTING SERVER DATA","Few Seconds......")
    xbmc.sleep(2000)
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=channels&name=21")')
    xbmc.sleep(2000)
    dp.close()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://program.apollo/?action=channels&name=21",return)')

def function2():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV[/COLOR]","GETTING SERVER DATA","Few Seconds......")
    xbmc.sleep(2000)
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=channels")')
    xbmc.sleep(2000)
    dp.close()
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://program.apollo/?action=channels",return)')
     
menuoptions()
