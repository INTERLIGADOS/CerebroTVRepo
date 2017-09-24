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
        
    call = dialog.select('[B][COLOR=yellow]24/7 Section[/COLOR][/B]', ['[B]   >> 24/7 TV Shows & Movies <<[/B]','[B]   >> 24/7 TV Shows On Demand << [I](Random Every Click)[/I][/B]'])
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




def function2():
    #xbmc.executebuiltin("Notification(CerebroTV,Attempting to load channel data, ..,7000,)")
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fkisakuldlanor%2fsuomynona%2fmaster%2fzipss%2f001-247-main.xml",return)')
    
   
def function1():
    #xbmc.executebuiltin("Notification(CerebroTV,Attempting to load channel data, ..,7000,)")
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.snstream/?description&iconimage=micon&mode=41&name=%5bB%5d%5bCOLOR%20yellow%5d24%2f7%5b%2fCOLOR%5d%5b%2fB%5d&url=CAT%3d247Shows",return)')
       
        
menuoptions()