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
        function7
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Kids Menu[/COLOR][/B]', ['[B][COLOR=lightgreen]      >> Kids Live TV Guide << [/COLOR][/B]','[B][COLOR=green]      FilmOn Kids[/COLOR][/B]', '[B][COLOR=blue]      Kids Movies On Demand![/COLOR][/B]', '[B][COLOR=pink]      Lego Movies[/COLOR][/B]', '[B][COLOR=brown]      Looney Toons (4K)[/COLOR][/B]', '[B][COLOR=gold]      Kids Live TV[/COLOR][/B]', '[B][COLOR=lightblue]      Kids On Demand! (All Ages)[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-7]
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
    update = xbmcgui.Dialog().yesno("[COLOR tomato]TV Guide Helper[/COLOR]","[COLOR yellow][/COLOR]","" ,"","Open Guide","Update Guide")
    if update:
        xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ZemTV-shani/?url=Live&mode=54&name=Clear+Cache")')
        xbmc.sleep(4000)
        xbmc.executebuiltin('RunScript("script.program.tvguiderefresh4",return)')
    else:
        xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ZemTV-shani/?url=Live&mode=54&name=Clear+Cache")')
        xbmc.sleep(4000)
        xbmc.executebuiltin('RunScript("script.mtvbtvguidekids")')
    

def function2():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.notfilmon/?description&group=KIDS&iconimage=https%3a%2f%2fstatic.filmon.com%2fassets%2fgroups%2f13%2fbig_logo.png&mode=3&name=KIDS&url=%2fgroup%2fkids",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)

def function3():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bob/?action=directory&content=0&url=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2fmain%2fkidsmain.xml",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)

def function4():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.projectm/?fanart=http%3a%2f%2fwww.kmart.com.au%2fwcsstore%2fKmart%2fimages%2fespots%2flego-151119-hero-banner-yellowfeature-mobile.jpg&mode=1&name=%5bCOLOR%20blue%5d%5bB%5dJUST%20LEGO%5b%2fB%5d%5b%2fCOLOR%5d&url=http%3a%2f%2fpulsewizard.co.uk%2fPS.Alpha%2fLEGO.xml",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)    
    
def function5():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.goodfellas/?fanart=http%3a%2f%2fwww.goodfellasteam.com%2fgoodfellas%2ffanart%2fgoodfellas.jpg&mode=53&name=4K%20LooneyToons&url=Plugin%3a%2f%2fplugin.video.youtube%2fchannel%2fUCRL3LmQvt3G0d5UFnLPUKNA%2f%3fpage%3d0",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)   
    
def function6():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ZemTV-shani/?mode=92&name=Kids%20tv&url=40",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000) 
      
def function7():
    #the content of function 3
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.phstreams/?action=xdirectory&content=addons&url=%24doregex%5bdir%5d%7cregex%3d210ba0462fbf08ff2405165cd2a74610",return)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
menuoptions()