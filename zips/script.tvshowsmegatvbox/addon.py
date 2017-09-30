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
        function3,
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11
        )
        
    call = dialog.select('[B][COLOR=yellow]TV Box Sets[/COLOR][/B]', [
    '[B]      TV Mix[/B]          [I](Good for latest episodes UK & USA)[/I] USE THIS THEN SEARCH IN [COLOR red] StreamHub[/COLOR] for the show!' , 
    '[B]      Stream Hub[/B]  [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]', 
    '[B]      Poseidon[/B]       [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]',
    '[B]      Specto[/B]          [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]' , 
    '[B]      Elysium[/B]         [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]',
    '[B]      Covenant[/B]      [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]', 
    '[B]      1Channel[/B]      [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]', 
    '[B]      S.A.L.T.S.[/B]     [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]', 
    '[B]      CerebroTV[/B]   [I](TV Show Box sets & Latest Episodes)[/I] [COLOR red]HD[/COLOR]' , 
    '[B]      UK Soaps Catch Up[/B] [COLOR red]HD[/COLOR]' , 
    '[B]      UK / USA TV Catch Up[/B] [COLOR red]HD[/COLOR]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-11]
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
    #the content of function 2
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.tvmix/",return)')
    
def function2():
    #the content of function 2
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.streamhub/?action=tvNavigator",return)')
    
def function3():
    #the content of function 2
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.poseidon/?action=tvNavigator",return)')
    
def function4():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.specto/?action=tvNavigator",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    
def function5():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.elysium/?action=tvNavigator",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    
def function6():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.covenant/?action=tvNavigator",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)

def function7():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.1channel/?mode=BrowseListMenu&section=tv",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    
def function8():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.salts/?mode=browse&section=TV",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)   
     
def function9():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=tvNavigator",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)  

def function10():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.covenant/?action=tvNetworks",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)  
 
def function11():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.Stallion-IPTV/?fanart=http%3a%2f%2fs19.postimg.org%2fsmdbasv8j%2ffanart.jpg&mode=53&name=%5bCOLOR%20deepskyblue%5d%5bB%5dNETWORKS%5b%2fB%5d%5b%2fCOLOR%5d&url=plugin%3a%2f%2fplugin.video.specto%2f%3faction%3dtvNetworks",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    
    
menuoptions()