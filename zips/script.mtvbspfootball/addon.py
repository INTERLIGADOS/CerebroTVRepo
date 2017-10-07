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
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=2779&title=2779")')
  
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.cypherstream/?description&iconimage=http%3a%2f%2fwww.apkmirror.com%2fwp-content%2fuploads%2f2016%2f07%2f579a975ed024a.png&mode=8&name=%5bCOLOR%20yellow%5dSky%20Sports%20Football%5b%2fCOLOR%5d&url=mpd%3a%2f%2ff5e3855d29156d0f9db77949ac7ad499.m3u8",return)')
   
menuoptions()