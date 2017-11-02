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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] ITV 2 Links[/COLOR][/B]', [
    '[B][COLOR=white]      ITV2 Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV2 Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV2 Link 3[/COLOR][/B]' ,
    '[B][COLOR=white]      ITV2 Link 4[/COLOR][/B]' ])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.itv/?url=https%3A%2F%2Fitv2liveios-i.akamaihd.net%2Fhls%2Flive%2F203495%2Fitvlive%2FITV2MN%2Fmaster.m3u8&mode=7&name=ITV2&iconimage=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.itv%5Cart%2F2.png")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dITV2%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f28d16f04d9b55d2ea2f826735ddffb85.m3u8")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.216.192:7071/routernew/ITV2/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DITV+2%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F35383_itv21.jpg&description=ITV+2+ITV+2+ITV+2+ITV+2+ITV+2+ITV+2")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1607&title=1607")')

menuoptions()