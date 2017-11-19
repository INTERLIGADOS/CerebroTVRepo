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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Action Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Action Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Action Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F42.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F42.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')
	
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?action=play&url=http%3A%2F%2F93.190.138.54%3A8000%2Flive%2FJYiopS12plm0ipJY%2FMgftrlH87iKr45n%2F42.m3u8%7CUser-Agent%3DONLINETVCLIENT_X60000_X25000_X4000MEGA_V1770%26amp%3Bmode%3D12%26quo&content=0")')
	
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1131&title=1131")')
   
menuoptions()