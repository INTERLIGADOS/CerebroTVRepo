import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Football Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Football Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Football Link 2[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]

        return func()
    else:
        func = funcs[call]

        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Sports%20Football%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2ff5e3855d29156d0f9db77949ac7ad499.m3u8")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectMayhem/?fanart=http%3a%2f%2falexcallejon.tv%2fwp-content%2fuploads%2f2016%2f01%2f01.jpg&iconimage=http%3a%2f%2fgreyhound-blandford.co.uk%2fwp-content%2fuploads%2f2014%2f12%2fskySportslogo.jpg&mode=30&name=%5bCOLOR%20lime%5dSky%20Sports%20Football%5b%2fCOLOR%5d&url=%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17806%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-football-live-streaming%23%0a")')
   
menuoptions()