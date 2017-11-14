import time
import xbmc
import os
import xbmcgui
import urllib2


passxxx = "imblind"

def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, '[B][COLOR=white]Please Enter [/COLOR][/B]'+str(name))
        
        keyboard.setHiddenInput(True)
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False 

            
xxxpass=Search('[B][COLOR=gold]Adult Section Password[/COLOR][/B]')

if passxxx == xxxpass:
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=[COLOR black]xxx[/COLOR]&mode=400&path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper%20Favourites%5Cxxx&sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cplugin.program.super.favourites%5Cfanart.jpg%26_options_sf",return)')