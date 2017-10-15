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
        function6,
        function7,
        function8,
        function9
        )
        
    call = dialog.select('[B][COLOR=yellow]Live TV Menu[/COLOR][/B]', [
    '[B]      >> [COLOR=pink]Cerebro Media[/COLOR] <<[/B]', 
    '[B]      >> [COLOR=gold]Open TV Guide[/COLOR] << [/B]' , 
    '[B]      IPTV Lists (ALL) [/B]',
    '[B]      UK Freeview (with basic EPG data)[/B]',
    '[B]      BBC iPlayer[/B] (has regional channels)', 
    '[B]      >> [COLOR=gold]Cerebro 24/7 TV & Movies[/COLOR] << [/B]',
    '[B]      >> [COLOR=lightblue]Kids TV Guide[/COLOR] <<[/B]',
    '[B]      Kids TV[/B] (press back multi times to exit this)',
    '[B]      >> [COLOR=green]My TV Guide [/COLOR]<<[/B] (make your own)'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-9]
        return func()
    else:
        func = funcs[call]
        return func()
    return 


def function1():
    xbmc.executebuiltin('RunAddon(plugin.video.wargames)')
    
def function2():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=[COLOR black]iptv[/COLOR]&mode=400&path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper%20Favourites%5Ciptv&sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cplugin.program.super.favourites%5Cfanart.jpg%26_options_sf",return)')

def function4():
    xbmc.executebuiltin('RunAddon(plugin.video.tvplayer)')

def function5():
    xbmc.executebuiltin('RunAddon(plugin.video.iplayerwww)')

def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2f247menu.xml",return)')
    
def function7():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.kids)')
    
def function8():
    xbmc.executebuiltin('RunAddon(plugin.video.KongKidz)')

def function9():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk.2017)')
    
menuoptions()