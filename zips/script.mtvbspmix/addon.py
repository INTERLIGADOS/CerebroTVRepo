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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Mix Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Mix Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Mix Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Mix Link 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]

        return func()
    else:
        func = funcs[call]

        return func()
    return 

    
def function1():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Sports%20Mix%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2ffce63bffcad71605ec55d7827914e7f6.m3u8",return)')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F275.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fderwentwater.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=3333&name=SKY%20SPORTS%20MIX%20HD%0d&url=http%3a%2f%2fmidnightiptvstreams.ddns.net%3a5050%2flive%2fjames2%2fjames2%2f57324.ts%0d",return)')
      
menuoptions()