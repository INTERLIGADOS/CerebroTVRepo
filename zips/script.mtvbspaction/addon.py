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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Action Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Action Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 4[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]

        return func()
    else:
        func = funcs[call]

        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Sports%20Action%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f189b62e7b9f4fb247a03007de1f6b056.m3u8")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F295.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fderwentwater.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fgb.png&mode=3333&name=SKY%20SPORTS%20ACTION%0d&url=http%3a%2f%2fmidnightiptvstreams.ddns.net%3a5050%2flive%2fjames2%2fjames2%2f57179.ts%0d",return)')
  
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.ProjectMayhem/?fanart=http%3a%2f%2falexcallejon.tv%2fwp-content%2fuploads%2f2016%2f01%2f01.jpg&iconimage=http%3a%2f%2fgreyhound-blandford.co.uk%2fwp-content%2fuploads%2f2014%2f12%2fskySportslogo.jpg&mode=30&name=%5bCOLOR%20lime%5dSky%20Sports%20Action%5b%2fCOLOR%5d&url=%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.liveonlinetv247.info%2fembed%2fskysports3.php%3fwidth%3d650%26height%3b%3d480%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-action-live-stream%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.livetv-free.com%2fsky-sports-3.php%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fsky3.html%23%0a",return)')
   
menuoptions()