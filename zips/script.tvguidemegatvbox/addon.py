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
    '[B]      >> [COLOR=gold]Open TV Guide[/COLOR] << [/B]' , 
    '[B]      >> [COLOR=yellow]Cerbro IPTV[/COLOR] << [/B]' ,
    '[B]      >> [COLOR=gold]Cerebro 24/7 TV & Movies[/COLOR] << [/B]',
    '[B]      >> [COLOR=yellow]Kids Corner[/COLOR] <<[/B]',
    '[B]      >> [COLOR=gold]My TV Guide [/COLOR]<<[/B] (make your own)',
    '[B]      >> [COLOR=yellow]Cerebro Media[/COLOR] <<[/B]'
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
    xbmc.executebuiltin('ActivateWindow(10025,&quot;plugin://plugin.video.wargames/?action=directory&amp;content=addons&amp;url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fLive.xml&quot;,return)')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2f247menu.xml",return)')
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.wargames/?action=directory&content=addons&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2fCerebroTVRepo%2fmaster%2fconfigs%2fKids.xml",return)')

def function5():
    xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk.2017)')
    
def function6():
    xbmc.executebuiltin('RunAddon(plugin.video.wargames)')
    
menuoptions()