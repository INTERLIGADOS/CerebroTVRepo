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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky 1 Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky 1 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky 1 Link 2[/COLOR][/B]',
    '[B][COLOR=white]      Sky 1 Link 3[/COLOR][/B]',
    '[B][COLOR=white]      Sky 1 Link 4[/COLOR][/B]',
    '[B][COLOR=white]      Sky 1 Link 5[/COLOR][/B]'
    ])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20One%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2febcd8ef93fa99c4834d0cc3275f3dcd7.m3u8")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://script.snstream/?description&iconimage=http%3a%2f%2fwww.apkmirror.com%2fwp-content%2fuploads%2f2016%2f07%2f579a975ed024a.png&mode=8&name=%5bCOLOR%20yellow%5dSky%20One%5b%2fCOLOR%5d&url=mpd%3a%2f%2febcd8ef93fa99c4834d0cc3275f3dcd7.m3u8")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Flive.thecableguytv.com%3A25461%2Flive%2Fwade%2Fwade%2F373.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')
  
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Flive.thecableguytv.com%3A25461%2Flive%2Fwade%2Fwade%2F545.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function5():
    xbmc.executebuiltin('PlayMedia("plugin://script.module.streamhublive/?url=swift:http://185.21.217.33:9091/routernew/SKYONE/playlist.m3u8&mode=10&name=%5BB%5D%5BCOLOR+white%5Dsky+One%5B%2FCOLOR%5D%5B%2FB%5D&iconimage=http%3A%2F%2Fswiftstreamz.com%2FSwiftStream%2Fimages%2Fthumbs%2F93916_79832_sky11.jpg&description=sky+Onesky+Onesky+Onesky+Onesky+Onesky+Onesky+Onesky+Onesky+Onesky+One")')

    
menuoptions()