import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2       
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky 2 Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky 2 Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Sky 2 Link 2[/COLOR][/B]'
	])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
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
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.216.192:7071/routernew/SKYTWO/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5Dsky+two%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F52368_sky222.jpg&description=sky+two+sky+two+sky+two+sky+two+sky+two+sky+two")')
    
    
menuoptions()