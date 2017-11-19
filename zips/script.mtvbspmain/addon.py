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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Main Event Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Main Event Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F40.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaa%2Fsiyyekksp1%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+5&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Feuropean_u21_champ.jpg&description=")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaa%2Fsiyyekksp1%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+2&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Flive_star_sixes.jpg&description=")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dSky%20Sport%20Main%20Event%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.jokerstream.com%2fp%2fsky-sports-1-hd_14.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fsky1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17804%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2flive.b-c-e.us%2fSkySports1UK2.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fnowwatchtvlive.cc%2fsky-sports-main-event-hd-live-stream-online-hdtv%2f%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-main-event-live-stream%23%0d%0a")')     

    
menuoptions()