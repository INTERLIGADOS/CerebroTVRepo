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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky 2 Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky 2 Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Sky 2 Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      Sky 2 Link 3[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Two%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f838d5a3429b075f8b9ab00c083d93989.m3u8")')
 
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Two%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f838d5a3429b075f8b9ab00c083d93989.m3u8")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.weetv/?description&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=3&name=SKY%202%0d&url=http%3a%2f%2fmajor2.ipfox.co%3a8080%2flive%2fwinsor_BRKdS5%2fG4lOS1yD%2f58.ts%0d")')
     
menuoptions()