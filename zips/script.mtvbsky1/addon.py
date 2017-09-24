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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky 1 Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky 1 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky 1 Link 2[/COLOR][/B]',
    '[B][COLOR=white]      Sky 1 Link 3[/COLOR][/B]'
    ])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20One%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2febcd8ef93fa99c4834d0cc3275f3dcd7.m3u8")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.217.33:9091/routernew/SKYONE/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5Dsky+One%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F79832_sky11.jpg&description=sky+One+sky+One+sky+One+sky+One+sky+One+sky+One")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fderwentwater.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=2&name=SKY%201%20HD%0d&url=http%3a%2f%2fmidnightiptvstreams.ddns.net%3a5050%2flive%2fjames2%2fjames2%2f57305.ts%0d")')
  
   
menuoptions()