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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] ITV 1 Links[/COLOR][/B]', [
    '[B][COLOR=white]      ITV1 Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV1 Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV1 Link 3[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV1 Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=http://tvcatchup.com/watch/itv&mode=9999&name=%5BB%5D%5BCOLOR+white%5D+ITV+One%5B%2FCOLOR%5D%5B%2FB%5D+-++Midsomer+Murders+&iconimage=https%3A%2F%2Fwww.tvcatchup.com%2Fchannel-images%2Fitv.png&description=&sf_options=winID%3D10025%26_options_sf")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dITV1%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fcc0b763f7c5ce91a396c0ef4fa529df9.m3u8")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.217.33:9091/routernew/ITV1/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DITV+1%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F89915_itv11.jpg&description=ITV+1+ITV+1+ITV+1+ITV+1+ITV+1ITV+1ITV+1")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.weetv/?url=http%3A%2F%2Ftvcatchup.com%2Fwatch%2Fitv&mode=9999&name=+ITV+One+-+++ITV+Evening+News+++++++++++++++++++++++++++++++++&iconimage=https%3A%2F%2Fwww.tvcatchup.com%2Fchannel-images%2Fitv.png&fanart=http%3A%2F%2Fwww.geetee.site%2Fwizchannels%2Fimages%2Fderwentwater.jpg")')

menuoptions()