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
        )
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports F1 Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports F1 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports F1 Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports F1 Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports F1 Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1134&title=1134")')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.cypherstream/?description&iconimage=http%3a%2f%2fwww.apkmirror.com%2fwp-content%2fuploads%2f2016%2f07%2f579a975ed024a.png&mode=8&name=%5bCOLOR%20yellow%5dSky%20Sports%20F1%5b%2fCOLOR%5d&url=mpd%3a%2f%2f343b4b2909705b5f5babe196c05c7895.m3u8",return)')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Fstreamtype%3DTSDOWNLOADER%26url%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F288.ts%26streamtype%3DTSDOWNLOADER%3Bname%3DSUPREMACY-ADD-ON&mode=12")')
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sport%20F1%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-f1-live-stream-%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17810%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2flivetv.sc%2fsky-sports-f1-hd-live-streaming%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fskyf1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3d%23%0d%0a",return)')

      
menuoptions()