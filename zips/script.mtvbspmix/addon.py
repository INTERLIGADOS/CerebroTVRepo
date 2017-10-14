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
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=2756&title=2756")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaa%2Fsiyyekksp2%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Sky+Sports+Mix&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Fsky_sports.jpg&description=")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sports%20Mix%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-mix-live-stream%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcrichd.sc%2fupdate%2fskysmix.php%23%0d%0a")')
      
menuoptions()