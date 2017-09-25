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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports News Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports News Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports News Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports News Link 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]

        return func()
    else:
        func = funcs[call]

        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Fstreamtype%3DTSDOWNLOADER%26url%3Dhttp%3A%2F%2Fiptv.dguk.co.uk%2Flive%2Fnatalie1%2Fnatalie1%2F1199.ts%26streamtype%3DTSDOWNLOADER%3Bname%3DSUPREMACY-ADD-ON&mode=12")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F273.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fderwentwater.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=3333&name=SKY%20SPORTS%20NEWS%0d&url=http%3a%2f%2fmidnightiptvstreams.ddns.net%3a5050%2flive%2fjames2%2fjames2%2f57176.ts%0d",return)')
    
menuoptions()