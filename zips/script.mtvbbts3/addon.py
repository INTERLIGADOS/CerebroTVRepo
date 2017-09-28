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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBT%20SPORT%203%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fba7c7bb9f1f2be48a9041f6a308eaa92.m3u8")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F185.53.163.205%3A2701&content=0")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBT%20SPORT%203%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fba7c7bb9f1f2be48a9041f6a308eaa92.m3u8")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.DELIVERANCE/?url=plugin%3A%2F%2Fplugin.video.SportsDevil%2F%3Fmode%3D1%26amp%3Bitem%3Dcatcher%253dstreams%2526url%3Dhttp%3A%2F%2Fsstream.net%2Fbt3.html%2526referer%3Dhttp%3A%2F%2Fsstream.net%2Fbt3.html&mode=12")')
   
menuoptions()