import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,subprocess
import urllib2
import sfile

#HOME     = xbmc.translatePath('special://home')
#file     = os.path.join(HOME, '_mega_time.txt')

#megatime = time.time()+9999
#with open(file, 'w') as f:
#    f.write(str(megatime))


#xbmc.executebuiltin('Quit')
#xbmc.sleep(3000)
HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')


#thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')
#try: sfile.rmtree(thumbs)
#except: pass	

dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()

def intro():
    #file2 = 'special://userdata/addon_data/mtvb2.mp4'
    #xbmc.Player().play(file2)
    #xbmc.sleep(10000)
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR=blue][B]CerebroTV[/COLOR][/B]","Please Wait Shutting Down....","If your device does not exit/reboot, please pull the power.")
    #xbmc.executebuiltin("Notification(If your device does not exit/reboot, please pull the power.,20000,)")
    #xbmc.Player().stop()
    killxbmc()
    xbmc.sleep(12000)
    xbmc.executebuiltin("Notification(If YOU CAN SEE THIS SELF REBOOT FAILED, PLEASE PULL THE POWER LEAD TO RESTART YOOUR DEVICE.,20000,)")
    
    
    
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
    
    
def killxbmc():
    #choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    #if choice == 0:
    #    return
    #elif choice == 1:
    #    pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        try: os.system('killall -9 SPMC')
        except: pass
        os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
        #os.system("su -c 'reboot'")
        exit()
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
        os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
        #os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        exit()
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        #try: os.system('adb shell am force-stop org.xbmc.kodi')
        #except: pass
        #try: os.system('adb shell am force-stop org.kodi')
        #except: pass
        #try: os.system('adb shell am force-stop org.xbmc.xbmc')
        #except: pass
        #try: os.system('adb shell am force-stop org.xbmc')
        #except: pass	
        #try: os.system('adb shell am force-stop com.semperpax.spmc16')
        #except: pass
        dp.create("[COLOR tomato]Cerebro[/COLOR]","SPMC/Kodi is now Closing","This make take a while.")
        #xbmc.sleep(1000)
        os.system("su -c 'reboot'")        
        xbmc.executebuiltin('Quit')
        xbmc.sleep(1000)
        dialog.ok("[COLOR=red][B]PLEASE REBOOT[/COLOR][/B]", "We are unable to reboot your device, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi/SPMC. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Either close using Task Manager (If unsure pull the plug).")
        #os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        exit()
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
            os.system('tskill SPMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im SPMC.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
        #os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        exit()
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    
        #os.system("su -c 'reboot'")
        #xbmc.executebuiltin('Quit')
        exit()



		
if os.path.exists(iddata):
    with open(iddata, 'r') as mymega:
        userid=mymega.read()
    try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
    except: pass
    
#dp.create("[COLOR tomato]Mega TV[/COLOR]","SPMC/Kodi is now Closing","This make take a while.")
#intro()
#xbmc.sleep(2000)
killxbmc()
#exit()
#import os
#import xbmc
#os.system("su -c 'reboot'")
#xbmc.executebuiltin("Notification(CerebroTV,Please wait Kodi is closing, DO NOT power off!,10000,)")
#xbmc.executebuiltin('RefreshRSS')
#xbmc.executebuiltin('ReloadSkin()')
#xbmc.sleep(5000)
#xbmc.executebuiltin('Quit')