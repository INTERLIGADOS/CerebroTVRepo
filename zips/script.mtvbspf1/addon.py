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
    xbmc.executebuiltin('PlayMedia("plugin://script.cypherstream/?description&iconimage=http%3a%2f%2fwww.apkmirror.com%2fwp-content%2fuploads%2f2016%2f07%2f579a975ed024a.png&mode=8&name=%5bCOLOR%20yellow%5dSky%20Sports%20F1%5b%2fCOLOR%5d&url=mpd%3a%2f%2f343b4b2909705b5f5babe196c05c7895.m3u8")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Fstreamtype%3DTSDOWNLOADER%26url%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F288.ts%26streamtype%3DTSDOWNLOADER%3Bname%3DSUPREMACY-ADD-ON&mode=12")')
    
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F38.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')

      
menuoptions()