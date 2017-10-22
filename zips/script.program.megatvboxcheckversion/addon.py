import xbmc,xbmcaddon,subprocess
import os
import xbmcgui
import urllib2
import urllib
import re
import uuid
import platform

def get_external_ip():
    site = urllib.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

dp = xbmcgui.DialogProgress()


def killxbmc():
    #choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    #if choice == 0:
    #    return
    #elif choice == 1:
    #    pass
    myplatform = platform()
    dialog = xbmcgui.Dialog()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        try: os.system("su -c 'reboot'")
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        try: os.system("su -c 'reboot'")
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass 
        try: os.system("su -c 'reboot'")
        except: pass		
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
        #xbmc.executebuiltin('Quit')
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        try: os.system("su -c 'reboot'")
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    
def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0


HOME     = xbmc.translatePath('special://userdata')
file2 = os.path.join(HOME, 'megatvbox.xml')
file3 = os.path.join(HOME, 'networksettings.xml')
file4 = os.path.join(HOME, 'freeview.xml')
#if ping("www.google.co.uk"):
with open(file2, 'r') as myfile:
    data=float(myfile.read())
		
with open(file3, 'r') as myfile:
    boxid=myfile.read()
    
with open(file4, 'r') as myfile:
    data2=myfile.read()

megaver = float(data)+0.1

isfreeview = int(data2)
	
response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/megatvbox2.txt')
data2=float(response.read())


response2 = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/updater.php?show=yes&v='+ str(data))
data3=response2.read()


dp = xbmcgui.DialogProgress()
    
if data < data2:
    update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV New Version Detcted[/COLOR]","[COLOR yellow]Your Version[/COLOR]: [COLOR red]" + str(data) + "[/COLOR] [COLOR yellow]New Version: [/COLOR] [COLOR green]" + str(data3) + "[/COLOR]" ,"[COLOR tomato]Would You Like to Update Now[/COLOR]?")
else:
    update = False
    #xbmcgui.Dialog().ok("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow]You have the latest verion[/COLOR]", "[COLOR yellow]Version[/COLOR]: [COLOR green]"+str(data)+"[/COLOR]")	
    #xbmc.executebuiltin('RunAddon(script.program.repair)')
    #xbmc.executebuiltin('RunAddon(plugin.program.megatvboxnot)')


if update:
    #xbmc.executebuiltin('RunAddon(plugin.program.megatvboxnot)')
    xbmc.executebuiltin('RunAddon(script.megatvupdater)')
    xbmc.executebuiltin('Dialog.Close(all, true)')
else:
    #xbmc.executebuiltin('RunAddon(script.program.repair)')
    dialog = xbmcgui.Dialog()
    #xbmc.playSFX('special://userdata/addon_data/complete.wav',False)
    dialog.ok("[COLOR=yellow][B]CerebroTV[/COLOR][/B]", "System Start up Complete", "CerebroTV Build Version [COLOR red]" + str(data) + "[/COLOR] | You Auth ID = [COLOR green]"+str(boxid)+"[/COLOR]","Press OK to Continue")
    #xbmc.sleep(4500)
    if isfreeview > 0:
        xbmc.executebuiltin('RunAddon(script.program.tvguiderefresh5)')
    else:
        xbmc.executebuiltin('RunAddon(plugin.program.megatvboxnot)')
    xbmc.sleep(5500)
    xbmc.executebuiltin("Notification(START UP COMPLETE, www.megatvbox.co.uk.,5000,)")
#else:
#    dialog = xbmcgui.Dialog()
#    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to connect to the internet", "","Press OK to Continue")
#    myplatform = platform()
#    if myplatform == 'windows': # Windows
#        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
#        killxbmc()
#    elif myplatform == 'linux': #Linux
#        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
#        killxbmc()
#    elif myplatform == 'osx': # OSX
#        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
#        killxbmc()
#    elif myplatform == 'android': # Android  
#        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
#        xbmc.executebuiltin("StartAndroidActivity(com.mbx.settingsmbox)")
#        if dialog.yesno("[COLOR yellow]CerebroTV[/COLOR]"," " ,"[COLOR yellow]Did You Get Connected?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
#            xbmc.sleep(3000)
#            DownloaderClass(LOCATION,file)
#            #xbmc.executebuiltin('RunAddon(script.program.repair)')
#        else:
#            dialog.ok("[COLOR=yellow][B]ERROR NO CONNECTION[/COLOR][/B]", "Kodi will now close.", "","Press OK to Continue")
#            killxbmc()			
	



exit()