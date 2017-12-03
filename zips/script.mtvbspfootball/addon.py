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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Football Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Football Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Football Link 2[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Football Link 3[/COLOR][/B]',
    '[B][COLOR=white]      Sky Sports Football Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dSky%2bSports%2bFootball%26url%3dhttp%253A%252F%252Fmamahd.com%252Fp%252Fmama.php%253Fid%253D17806%2526match%253DSky%252520Sports%252520Football%252520vs%252520%26cfg%3dmamahd.com.cfg%2540Streams%2540videoTitle%26videoTitle%3dSky%2bSports%2bFootball%26director%3dmamahd.com%26genre%3dTV%26referer%3dhttps%253A%252F%252Fmamahd.tv%252F%26definedIn%3dmamahd.com.cfg%26icon%3dC%253A%255CUsers%255Cbigla%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Cmamahd.png%26type%3drss%26title_%3dSkySports%2bFootball&mode=1")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dSky%2bSports%2bFootball%26url%3dhttp%253A%252F%252Fmamahd.com%252Fp%252Fmama.php%253Fid%253D17806%2526match%253DSky%252520Sports%252520Football%252520vs%252520%26cfg%3dmamahd.com.cfg%2540Streams%2540videoTitle%26videoTitle%3dSky%2bSports%2bFootball%26director%3dmamahd.com%26genre%3dTV%26referer%3dhttps%253A%252F%252Fmamahd.tv%252F%26definedIn%3dmamahd.com.cfg%26icon%3dC%253A%255CUsers%255Cbigla%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Cmamahd.png%26type%3drss%26title_%3dSkySports%2bFootball&mode=1")')
  
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dSky%2bSports%2bFootball%26url%3dhttp%253A%252F%252Fmamahd.com%252Fp%252Fmama.php%253Fid%253D17806%2526match%253DSky%252520Sports%252520Football%252520vs%252520%26cfg%3dmamahd.com.cfg%2540Streams%2540videoTitle%26videoTitle%3dSky%2bSports%2bFootball%26director%3dmamahd.com%26genre%3dTV%26referer%3dhttps%253A%252F%252Fmamahd.tv%252F%26definedIn%3dmamahd.com.cfg%26icon%3dC%253A%255CUsers%255Cbigla%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Cmamahd.png%26type%3drss%26title_%3dSkySports%2bFootball&mode=1")')
   
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.SportsDevil/?item=catcher%3dstreams%26title%3dSky%2bSports%2bFootball%26url%3dhttp%253A%252F%252Fmamahd.com%252Fp%252Fmama.php%253Fid%253D17806%2526match%253DSky%252520Sports%252520Football%252520vs%252520%26cfg%3dmamahd.com.cfg%2540Streams%2540videoTitle%26videoTitle%3dSky%2bSports%2bFootball%26director%3dmamahd.com%26genre%3dTV%26referer%3dhttps%253A%252F%252Fmamahd.tv%252F%26definedIn%3dmamahd.com.cfg%26icon%3dC%253A%255CUsers%255Cbigla%255CAppData%255CRoaming%255CKodi%255Caddons%255Cplugin.video.SportsDevil%255Cresources%255Cimages%255Cmamahd.png%26type%3drss%26title_%3dSkySports%2bFootball&mode=1")')
    
menuoptions()