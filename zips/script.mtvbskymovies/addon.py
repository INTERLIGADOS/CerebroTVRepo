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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky Cinema[/COLOR][/B]', ['[B][COLOR=green]Sky Cinema on Demand 1[/COLOR] (Select Channel) [/B]', '[B][COLOR=gold]Sky Cinema on Demand 2[/COLOR] (Select Channel) [/B]', '[B][COLOR=lightblue]Sky Cinema on Demand 3[/COLOR] (Select Channel) [/B]', 'Live Channels (Will Search then you select)'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    xbmc.executebuiltin("Notification(CerebroTV, WILL NEED TO SELECT CHANNEL, ..,17000,)")
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.super.favourites/?label=Channels&mode=650&cmd=ActivateWindow%2810025%2C%22plugin%3A%2F%2Fplugin.video.zen%2F%3Faction%3Dchannels%22%2Creturn%29&image=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cscript.zen.artwork%5Cresources%5Cmedia%5Czen%5Cchannels.png&content_type=video&sf_options=winID%3D10025%26_options_sf")')

def function2():
    xbmc.executebuiltin("Notification(CerebroTV, WILL NEED TO SELECT CHANNEL, ..,17000,)")
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.super.favourites/?label=Channels&mode=650&cmd=ActivateWindow%2810025%2C%22plugin%3A%2F%2Fplugin.video.exodus%2F%3Faction%3Dchannels%22%2Creturn%29&image=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cscript.exodus.artwork%5Cresources%5Cmedia%5Cexodus%5Cchannels.png&content_type=video&sf_options=winID%3D10025%26_options_sf")')
    
def function3():
    xbmc.executebuiltin("Notification(CerebroTV, WILL NEED TO SELECT CHANNEL, ..,17000,)")
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.super.favourites/?label=Channels&mode=650&cmd=ActivateWindow%2810025%2C%22plugin%3A%2F%2Fplugin.video.specto%2F%3Faction%3Dchannels%22%2Creturn%29&image=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cscript.specto.media%5Cresources%5Cmedia%5Cgone%5Cchannels.jpg&content_type=video")')

def function4():
    xbmc.executebuiltin("Notification(CerebroTV,Searching for channels - WILL NEED TO SELECT CHANNEL, ..,27000,)")
    xbmc.executebuiltin('PlayMedia("plugin://plugin.program.super.favourites/?label=sky+movies&mode=650&cmd=ActivateWindow%2810025%2C%22plugin%3A%2F%2Fplugin.video.sanctuary%2F%3Fdescription%26extra%3DOLD%26fanart%3DC%253a%255cUsers%255cbigla%255cAppData%255cRoaming%255cKodi%255caddons%255cplugin.video.sanctuary%255cfanart.jpg%26iconimage%3DC%253a%255cUsers%255cbigla%255cAppData%255cRoaming%255cKodi%255caddons%255cplugin.video.sanctuary%255cicon.png%26mode%3D1501%26name%3Dsky%2520movies%26url%3DLive%2520TV%22%2Creturn%29&image=special%3A%2F%2Fhome%2Faddons%5Cplugin.video.sanctuary%5Cicon.png&content_type=video")')
    
#menuoptions()
xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=channels",return)')