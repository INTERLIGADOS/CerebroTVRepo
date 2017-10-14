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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sports Menu[/COLOR][/B]', [
    '[B][COLOR=gold]      >> Sports TV Guide << [/COLOR][/B](UK)', 
    '[B][COLOR=green]      Sports Channels[/COLOR][/B]', 
    '[B][COLOR=white]      Pay Per View (PPV)[/COLOR][/B]',
    '[B][COLOR=green]      UFC/MMA[/B][/COLOR]',
    '[B][COLOR=white]      Boxing Live + Replays[/B][/COLOR]',
    '[B][COLOR=green]      WWE[/B][/COLOR]'])
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
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.sports)')
   
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fsports.xml",return)')
   
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fppv.xml",return)')

def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ufc-finest/",return)')

def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bob.unleashed/?description=No%20information%20available&fanart=http%3a%2f%2fi.imgur.com%2fnMvCf9l.jpg&iconimage=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2freloaded%2ficons%2fMain%2fMain-Shepo.png&mode=get_list&name=Boxing&url=http%3a%2f%2fwww.norestrictions.club%2fshepo%2fbase.xml",return)')

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bob.unleashed/?description=No%20information%20available&fanart=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2freloaded%2fthemes%2fmovies%2fmovies3.jpg&iconimage=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2freloaded%2ficons%2fSports%2fWWE.png&mode=get_list&name=WWE&url=http%3a%2f%2fwww.norestrictions.club%2fdeez%2freplays%2freplays.xml",return)')
    
menuoptions()