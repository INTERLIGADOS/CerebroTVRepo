## MTVB ##






























































import time
import xbmc
import os
import xbmcgui
import urllib2

HOME   = xbmc.translatePath('special://userdata')
file99 = os.path.join(HOME, 'networksettings.xml')
file98 = os.path.join(HOME, 'megatvbox.xml')	
file3 = os.path.join(HOME, 'lock.xml')
megaver = 0


    
with open(file99, 'r') as myfile:
    boxid=myfile.read()
    
with open(file98, 'r') as myfile:
    cversion=myfile.read()
    
def executeSomething():
    
    try:
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&tt=yes&bv='+str(cversion)).read()
        
        if response == "BAD":
            dp = xbmcgui.DialogProgress()
            dp.create("[COLOR=yellow][B]INFORMATION[/COLOR][/B]","Your Code has been been blocked","Contact us http://m.me/mtvb1")
            xbmc.sleep(15000)
            xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
            exit()
        else:
            xbmc.executebuiltin("XBMC.AlarmClock('MTVBCORE',XBMC.RunAddon(script.mtvbcore),4,silent)")
            exit()
    except: pass
    xbmc.executebuiltin("XBMC.AlarmClock('MTVBCORE',XBMC.RunAddon(script.mtvbcore),4,silent)")

executeSomething()   