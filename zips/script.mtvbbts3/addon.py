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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] BT Sports 3 Links[/COLOR][/B]', [
    '[B][COLOR=white]      BT Sports 3 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 3 Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 3 Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 3 Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.weetv/?fanart=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.weetv%5cfanart.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fca_us.png&mode=3333&name=BT%20SPORTS%203%20HD%0d&url=http%3a%2f%2fiptv.myeasytv.xyz%3a8000%2flive%2fnig55%2fnig55%2f16934.ts%0d",return)')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2F62.210.141.126%3A8080%2Fbtsport3hd%2Fmpegts&mode=12")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBT%20SPORT%203%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fba7c7bb9f1f2be48a9041f6a308eaa92.m3u8",return)')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.DELIVERANCE/?url=plugin%3A%2F%2Fplugin.video.SportsDevil%2F%3Fmode%3D1%26amp%3Bitem%3Dcatcher%253dstreams%2526url%3Dhttp%3A%2F%2Fsstream.net%2Fbt3.html%2526referer%3Dhttp%3A%2F%2Fsstream.net%2Fbt3.html&mode=12")')
   
menuoptions()