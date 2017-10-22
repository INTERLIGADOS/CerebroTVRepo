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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dITV2%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f28d16f04d9b55d2ea2f826735ddffb85.m3u8")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://78.129.138.45:8081/routernew/ITV2/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5DITV+2%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F35383_itv21.jpg&description=ITV+2+ITV+2+ITV+2+ITV+2+ITV+2+ITV+2&sf_options=winID%3D10025%26_options_sf")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dITV2%26url%3dmpd%253A%252F%252F28d16f04d9b55d2ea2f826735ddffb85.m3u8%26cfg%3dtvone1.tv.cfg%2540Streams%2540Channels%26videoTitle%3dITV2%26director%3dtvone1.tv%26genre%3dLive%2bTV%26referer%3dmpd%253A%252F%252F28d16f04d9b55d2ea2f826735ddffb85.m3u8%26definedIn%3dtvone1.tv.cfg%26type%3drss&mode=1",return)')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.echostreams/?url=itv2+hd%7CSPLIT%7Chttp%3A%2F%2Fmediaiptv.xyz%3A8000%2Flive%2Fpg%2Fpg%2F2277.ts&mode=3&name=%5BCOLOR+white%5DItv2++%5BCOLOR+blue%5D%5BB%5DHD%5B%2FB%5D%5B%2FCOLOR%5D%5B%2FCOLOR%5D&iconimage=C:\\Users\\bigla\\AppData\\Roaming\\Kodi\\addons\\plugin.video.echostreams\\icon.png&fanartimage=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.echostreams%5Cfanart.jpg")')

menuoptions()