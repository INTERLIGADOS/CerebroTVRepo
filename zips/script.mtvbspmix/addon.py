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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F418.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')
      
menuoptions()