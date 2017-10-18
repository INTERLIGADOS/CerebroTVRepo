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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] BT Sports 2 Links[/COLOR][/B]', [
    '[B][COLOR=white]      BT Sports 2 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 2 Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 2 Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 2 Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33RaaabB3eETtiyiy-2%2FStrm%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=BT+Sports+2&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Fbt_sports.jpg&description=")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBT%20SPORT%202%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fa0baff4a9870ad57efd54f32cf8be880.m3u8")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=923&title=923")')
  
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.mangTV/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fclient-proiptv.com%3A8080%2Flive%2FAmersfoort%2FAmersfoort%2F2512.ts%26streamtype%3DTSDOWNLOADER%26name%3D&mode=12")')
    

menuoptions()