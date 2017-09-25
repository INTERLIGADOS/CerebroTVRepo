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
        function6
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Music TV & Radio[/COLOR][/B]', ['[B][COLOR=green]Music TV Channels[/COLOR][/B]', '[B][COLOR=green]MTV UK [/COLOR][/B] (On Demand)', '[B][COLOR=lightblue]UK Radio[/COLOR][/B]', '[B][COLOR=white]More Live Music TV[/COLOR][/B]', '[B][COLOR=white]Audio Music Section (Chats/Albums)[/COLOR][/B]', '[B][COLOR=white]Audio Music Section 2 (Chats/Albums)[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-6]
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.picasso/?description&fanart=http%3a%2f%2fi.imgur.com%2fjz9gffT.png&iconimage=http%3a%2f%2fi.imgur.com%2fyizEAcv.png&mode=1&name=%5bB%5d%5bCOLOR%20yellow%5dLive%20Music%5b%2fCOLOR%5d%5b%2fB%5d&url=http%3a%2f%2fmatsbuilds.uk%2fMenus%2fMusic%2fIPTVMUSIC.xml",return)')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.mdmtvuk/?content_type=video",return)')

def function3():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.audio.tuneinradio/",return)')

def function4():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.white.devil/?action=directory&url=http%3a%2f%2fbrettusbuilds.com%2fbrettus%2520streams%2fLIVE%2520TV%2fmusic%2520live.xml",return)')

def function5():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.sanctuary/?description&extra&fanart=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.sanctuary%5cfanart.jpg&iconimage=http%3a%2f%2fherovision.x10host.com%2ffreeview%2fquick.png&mode=1133&name=Quicksilver%20Music&url",return)')

def function6():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10502,"plugin://plugin.audio.mp3streams/",return)')

menuoptions()