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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=Sky%20Sports%20Action&mode=600&cmd=PlayMedia%28%22plugin%3A%2F%2Fplugin.video.livehub2%2F%3Furl%3Dhttp%253A%252F%252F95.154.237.88%253A8080%252FMatH33Raaa%252Fsiyyekksp3%252Findex.m3u8%257CUser-Agent%253DAppleCoreMedia%252F1.0.0.13A452%2B%2528iPhone%253B%2BU%253B%2BCPU%2BOS%2B9_0_2%2Blike%2BMac%2BOS%2BX%253B%2Ben_gb%2529%26mode%3D9999%26name%3DChannel%2B4%26iconimage%3Dhttp%25253A%25252F%25252Fsmarterlogix.com%25252FiosSecureApps%25252FPakIndiaTVHD%25252FV1-2%25252FImages%25252Fatp_world_tour.jpg%26description%3D%26sf_options%3DwinID%253D10025%2526_options_sf%22%29&image=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Fatp_world_tour.jpg&content_type=",return)')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=Sky%20Sports%20Action%202&mode=600&cmd=PlayMedia%28%22plugin%3A%2F%2Fplugin.video.livehub2%2F%3Furl%3Dhttp%253A%252F%252F95.154.237.88%253A8080%252FMatH33Raaa%252Fsiyyekksp3%252Findex.m3u8%257CUser-Agent%253DAppleCoreMedia%252F1.0.0.13A452%2B%2528iPhone%253B%2BU%253B%2BCPU%2BOS%2B9_0_2%2Blike%2BMac%2BOS%2BX%253B%2Ben_gb%2529%26mode%3D9999%26name%3DChannel%2B1%26iconimage%3Dhttp%25253A%25252F%25252Fsmarterlogix.com%25252FiosSecureApps%25252FPakIndiaTVHD%25252FV1-2%25252FImages%25252Flive_star_sixes.jpg%26description%3D%26sf_options%3DwinID%253D10025%2526_options_sf%22%29&image=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Flive_star_sixes.jpg&content_type=",return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=Sky%20Sports%20Action%204&mode=600&cmd=PlayMedia%28%22plugin%3A%2F%2Fplugin.video.livehub2%2F%3Furl%3Dhttp%253A%252F%252F95.154.237.88%253A8080%252FMatH33Raaa%252Fsiyyekksp3%252Findex.m3u8%257CUser-Agent%253DAppleCoreMedia%252F1.0.0.13A452%2B%2528iPhone%253B%2BU%253B%2BCPU%2BOS%2B9_0_2%2Blike%2BMac%2BOS%2BX%253B%2Ben_gb%2529%26mode%3D9999%26name%3DSky%2BSports%2B3%26iconimage%3Dhttp%25253A%25252F%25252Fsmarterlogix.com%25252FiosSecureApps%25252FPakIndiaTVHD%25252FV1-2%25252FImages%25252Fsky_sports.jpg%26description%3D%26sf_options%3DwinID%253D10025%2526_options_sf%22%29&image=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Fsky_sports.jpg&content_type=",return)')
  
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1131&title=1131")')
   
menuoptions()