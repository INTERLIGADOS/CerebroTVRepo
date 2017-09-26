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
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11,
        function12,
        function13,
        function14,
        function15,
        function16,
        function17
        )
        
    call = dialog.select('[B][COLOR=yellow]Movies On Demand[/COLOR][/B]', [
    '[B]      Sky Cinema On Demand[/B]',
    '[B]      StreamHub Movies[/B]',    
    '[B]      Elysium Movies[/B]', 
    '[B]      Poseidon Movies[/B]', 
    '[B]      [COLOR gold]Latest Movie Releases in [I]HD ONLY[/I][/COLOR][/B]', 
    '[B]      [COLOR yellow]Latest Movie Releases in [I]MOST IN HD [/I][/COLOR][/B]', 
    '[B]      [COLOR gold]Latest Kids Movie Releases in [I]HD ONLY[/I] [/COLOR][/B]', 
    '[B]      [COLOR yellow]Latest Movie Releases in [I]SOME IN HD [/I][/COLOR][/B]', 
    '[B]      Covenant Movies[/B]',
    '[B]      Specto Movies[/B]' , 
    '[B]      1Channel Movies[/B]', 
    '[B]      S.A.L.T.S. Movies[/B]',
    '[B]      Exodus[/B]',
    '[B]      [COLOR gold]Latest Movies[/COLOR][/B] (Some Cam Copies Lurk Here!!!!!)',
    '[B]      [COLOR green]4K Movies[/COLOR][/B] (need a fast connection!!!!)',
    '[B]      [COLOR lightblue]3D Movies[/COLOR][/B] (HD)',
    '[B]      [COLOR blue]Movie Box Sets[/COLOR][/B] (HD)'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-17]
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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.streamhub/?action=channels",return)')
    
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.streamhub/?action=movieNavigator",return)')
    
def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.elysium/?action=movieNavigator",return)')
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.poseidon/?action=movieNavigator",return)')
      
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bob.unleashed/?description=No%20information%20available&fanart=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2freloaded%2fthemes%2fmovies%2fmovies2.jpg&iconimage=http%3a%2f%2fnorestrictions.club%2fnorestrictions.club%2freloaded%2ficons%2fMain%2fMain-New-Releases.png&mode=get_list&name=New%20Releases&url=http%3a%2f%2fwww.norestrictions.club%2freloaded%2fnewreleasesmain.xml",return)')

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2ffanart.jpg.png&mode=1&name=%5bCOLOR%20red%5dNew%20Releases%5b%2fCOLOR%5d&url=http%3a%2f%2fstephen-builds.uk%2fsupremacy%2fNew%2520Releases%2fNew%2520Releases.txt",return)')

def function7():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bob.unleashed/?description=No%20information%20available&fanart=httpss%3a%2f%2f185.20.99.97%2f185.20.99.97%2fnorestrictions.club%2freloaded%2fthemes%2fmovies%2fmovies7.jpg&iconimage=https%3a%2f%2f185.20.99.97%2fnorestrictions.club%2freloaded%2ficons%2fKids%2fKids-New-Releases.png&mode=get_list&name=%5bCOLORcyan%5dClick%20For%20New%20Kids%20Movies%5b%2fCOLOR%5d&url=http%3a%2f%2fnorestrictions.noobsandnerds.com%2fmain%2fkidsnewrelease.xml",return)')
       
def function8():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.silenthunter/?action=directory&content=0&url=http%3a%2f%2fbit.ly%2f2g8sjhm",return)')
    
def function9():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.covenant/?action=movieNavigator",return)')
    
def function10():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.specto/?action=movieNavigator",return)')

def function11():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.1channel/?mode=BrowseListMenu&section=movie",return)')

def function12():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.salts/?mode=browse&section=Movies",return)')
   
def function13():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.exodus/?action=movieNavigator",return)') 

def function14():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2ffanart.jpg.png&mode=1&name=%5bCOLOR%20aqua%5dNew%20Releases%5b%2fCOLOR%5d&url=http%3a%2f%2fstephen-builds.uk%2fsupremacy%2fNew%2520Releases%2fNew%2520Releases.txt",return)')        

def function15():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=[COLOR black]4k[/COLOR]&mode=400&path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper%20Favourites%5C4k&sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cplugin.program.super.favourites%5Cfanart.jpg%26_options_sf",return)')        

def function16():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.nemesis/?description&fanart=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.nemesis%5cfanart.jpg&iconimage=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.nemesis%5cicon.png&mode=1&name=%5bCOLOR%20yellow%5d3%5bCOLOR%20aqua%5dD%20Movies%20By%20Nereus%5b%2fCOLOR%5d&url=https%3a%2f%2fpastebin.com%2fraw%2fyYMEWMGE",return)') 
    
def function17():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.bennu/?action=directory&content=0&url=https%3a%2f%2fpastebin.com%2fraw%2fvdS3Cyxe",return)') 
    
menuoptions()