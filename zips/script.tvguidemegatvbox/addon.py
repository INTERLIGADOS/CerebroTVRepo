import time
import xbmc
import os
import xbmcgui
import urllib2
import utils
import sfile

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
		function5,
		function6
        )
        
    call = dialog.select('[B][COLOR=yellow]Live TV Menu[/COLOR][/B]', [ 
    '[B]      >> [COLOR=gold]Open Cerebro[/COLOR] [COLOR=red]UK[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' ,
	'[B]      >> [COLOR=yellow]Open Cerebro[/COLOR] [COLOR=red]USA[/COLOR] [COLOR=gold]TV Guide[/COLOR] << [/B]' , 	
    '[B]      >> [COLOR=gold]My TV Guide [/COLOR]<<[/B] (make your own)',
    '[B]      >> [COLOR=yellow]Cerebro IPTV[/COLOR] << Live TV (Many Options)[/B]',
    '[B]      >> [COLOR=gold]Cerebro Media[/COLOR] <<[/B] (Access All Options)',
    '[B]      >> [COLOR=gold]Cerbro Christmas Fire Places[/COLOR] <<[/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-6]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk)')
	
def function2():
    xbmc.executebuiltin('RunAddon(script.cerebro.tvguide.open4)')
    
def function3():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk.2017)')
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fLive.xml",return)')
    
def function5():
    xbmc.executebuiltin('RunAddon(plugin.video.wargames)')
	
def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=[COLOR black]fireplace[/COLOR]&mode=400&path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper%20Favourites%5Cfireplace&sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cplugin.program.super.favourites%5Cfanart.jpg%26_options_sf")')
    
menuoptions()