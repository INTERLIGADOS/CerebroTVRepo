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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Arena Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Arena Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Arena Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Arena Link 3[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=2778&title=2778")')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.cypherstream/?description&iconimage=http%3a%2f%2fwww.apkmirror.com%2fwp-content%2fuploads%2f2016%2f07%2f579a975ed024a.png&mode=8&name=%5bCOLOR%20yellow%5dSky%20Sports%20Arena%5b%2fCOLOR%5d&url=mpd%3a%2f%2fa49aab2afb70ffcf3f5e97d6763fed65.m3u8",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sports%20Arena%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fsky5.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17808%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2flivetv.sc%2fChannel%2fss-arena.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fnowwatchtvlive.cc%2fsky-sports-arena-live-stream-watch-sky-sports-arena-online%2f%23%0d%0a",return)')
      
menuoptions()