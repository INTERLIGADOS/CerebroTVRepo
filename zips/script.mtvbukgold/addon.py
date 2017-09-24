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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky Gold Links[/COLOR][/B]', [
    '[B][COLOR=white]      Gold Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Gold Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      Gold Link 3[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dGOLD%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f2c0898822ab3baf7f93bea86648adb26.m3u8")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2F178.33.237.97%3A1888%2Flive%2FTZrQjaZKoO%2FryXH1oFWxZ%2F19.ts%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&mode=12&iconimage=http%3A%2F%2Fwww.goldtv.it%2Fimages%2FLOGOGOLDTV-800-600.png")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.217.33:9091/routernew/Gold/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DGold%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F28932_gold.jpg&description=Gold+Gold+Gold+Gold+GoldGold")')
 

menuoptions()