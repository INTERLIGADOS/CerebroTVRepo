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
        function5
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky Fox Links[/COLOR][/B]',
    ['[B][COLOR=white]      Fox UK Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Fox UK Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      Fox UK Link 3[/COLOR][/B]' ,
    '[B][COLOR=white]      Fox UK Link 4[/COLOR][/B]' ,
    '[B][COLOR=white]      Fox UK Link 5[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2F62.210.141.126%3A8080%2Ffox%2Fmpegts&mode=12")')

def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dFox%20UK%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fc37f98026cb0acb60766071a6e45c01b.m3u8",return)')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.FTFA/?action=play&url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2F15pUsZKUIw%2F4boblpukUd%2F454.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DF.T.F.A&content=0")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2F11gb.gcdn.co%2Flive%2Fonline%2Ftv%2F1684.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&mode=12")')

def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.FTFA/?action=play&url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2F185.2.83.209%3A8000%2Flive%2F123456%2F123456%2F460.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DF.T.F.A&content=0")')

menuoptions()