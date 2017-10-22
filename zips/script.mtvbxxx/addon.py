import time
import xbmc
import os
import xbmcgui
import urllib2


passxxx = "yesiam"

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
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.uwc/",return)')