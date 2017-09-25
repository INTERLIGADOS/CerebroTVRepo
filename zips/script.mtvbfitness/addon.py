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
        function4
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Fitness & Learning[/COLOR][/B]', ['[B][COLOR=green]Workout & Fitness 1[/COLOR][/B]', '[B][COLOR=green]Workout & Fitness 2[/COLOR][/B]', '[B][COLOR=lightblue]Teach Yourself[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.goodfellas/?fanart=http%3a%2f%2fwww.pixhoster.info%2ff%2f2016-08%2f1595fe974afe6ac6188a6046ae9df4f5.png&mode=1&name=Fitness&url=http%3a%2f%2fgoo.gl%2f60aGJx",return)')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.Evolve/?description&fanart=http%3a%2f%2fwww.matsbuilds.uk%2fpics%2fevolve%2ffanart.jpg&mode=1&name=%5bB%5d%5bCOLOR%20red%5dF%5b%2fCOLOR%5d%5bCOLOR%20white%5ditness%5b%2fCOLOR%5d%5b%2fB%5d&url=http%3a%2f%2fpastebin.com%2fraw%2f3jhBuQDC",return)')

def function3():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.phstreams/?action=directory&content=0&url=http%3a%2f%2fbit.ly%2fLearnWithCosmixSection",return)')

def function4():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.phstreams/?action=directory&content=0&url=http%3a%2f%2fbit.ly%2fLearnWithCosmixSection",return)')

menuoptions()