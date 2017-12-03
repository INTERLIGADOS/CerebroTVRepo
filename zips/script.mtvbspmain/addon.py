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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Main Event Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Main Event Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 3[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dSky%2bSports%2bMain%2bEvent%26url%3dhttp%253A%252F%252Fmamahd.com%252Fp%252Fmama.php%253Fid%253D17804%2526match%253DSky%252520Sports%252520Main%252520Event%252520vs%252520%26cfg%3dmamahd.com.cfg%2540Streams%2540videoTitle%26videoTitle%3dSky%2bSports%2bMain%2bEvent%26director%3dmamahd.com%26genre%3dTV%26referer%3dhttps%253A%252F%252Fmamahd.tv%252F%26definedIn%3dmamahd.com.cfg%26icon%3dC%253A%255CUsers%255Cbigla%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Cmamahd.png%26type%3drss%26title_%3dSkySports%2bMain%2bEvent&mode=1")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaa%2Fsiyyekksp1%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+5&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Feuropean_u21_champ.jpg&description=")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaa%2Fsiyyekksp1%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+2&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Flive_star_sixes.jpg&description=")')

    
menuoptions()