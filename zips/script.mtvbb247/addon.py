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
        
    call = dialog.select('[B][COLOR=yellow]24/7 Section[/COLOR][/B]', [
    '[B]   >> 24/7 TV Shows <<[/B]',
    '[B]   >> 24/7 TV Shows On Demand << [I](Random Every Click)[/I][/B]',
    '[B]   >> 24/7 Movies <<[/B]'])
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=http%3a%2f%2fmtvb.co.uk%2f247-2.xml",return)')
       
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=http%3a%2f%2fmtvb.co.uk%2f247.xml",return)')
 
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=http%3a%2f%2fmtvb.co.uk%2f247-movies.xml",return)')
              
menuoptions()

    