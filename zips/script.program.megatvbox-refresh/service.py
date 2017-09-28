import utils
import xbmc
import os
import xbmcgui
import zipfile
import sfile
import download
import urllib
import urllib2
import time
import re


HOME     = xbmc.translatePath('special://addons/script.megatvinstall')
HOME2    = xbmc.translatePath('special://userdata/')
LOCATION = "http://mtvbusad.com/install.zip"
ROOT     = xbmc.translatePath('special://home')
file     = os.path.join(HOME2, 'install.zip')
file3    = os.path.join(HOME, 'service.py')
file100  = os.path.join(HOME2, 'megatvbox.xml')

GETTEXT  = utils.GETTEXT
noconnection = False

dp = xbmcgui.DialogProgress()


def killxbmc():
    dp = xbmcgui.DialogProgress()
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
        dialog.ok("[COLOR=red][B]Cerebro TV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]Cerebro TV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]Cerebro TV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]Cerebro TV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]Cerebro TV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    
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


def DeleteCache(url):
    print '###DELETING KODI CACHE###'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:    
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
               # dialog = xbmcgui.Dialog()
                #if dialog.yesno("Delete KODI Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                for f in files:
                    try:
                        os.unlink(os.path.join(root, f))
                    except:
                        pass
                for d in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, d))
                    except:
                        pass
    
	
def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]Cerebro TV[/COLOR]", line1 = "[COLOR yellow]Downloading new menu data[/COLOR].", line2 = "[COLOR gold]Please Wait Download in Progress[/COLOR]", line3 = "test")
      dp.update(percent)

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to connect to the internet", "","Press OK to Continue")
    myplatform = platform()
    if myplatform == 'windows': # Windows
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'linux': #Linux
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'osx': # OSX
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'android': # Android  
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        xbmc.executebuiltin("StartAndroidActivity(com.mbx.settingsmbox)")
        if dialog.yesno("[COLOR yellow]Cerebro TV[/COLOR]"," " ,"[COLOR yellow]Did You Get Connected?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
            xbmc.sleep(3000)
            DownloaderClass(LOCATION,file)
        else:
            dialog.ok("[COLOR=yellow][B]ERROR NO CONNECTION[/COLOR][/B]", "Kodi will now close.", "","Press OK to Continue")
            killxbmc()			
        exit();		

def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]Cerebro TV Updater[/COLOR]","Downloading Update "+str(megaver),"This make take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]Cerebro TV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        if os.path.exists(file):
            file3 = os.path.join(HOME, 'mchangelog.xml')
            open(file3, 'w+')
            userdata = "test|test"
            with open(file3, 'w') as f:
                f.write(userdata)
            zfile = zipfile.ZipFile(file, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, ROOT)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        

        utils.DeleteFile(file)	
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","Update Complete","Closing Kodi....")	
        killxbmc()
        exit()

    except Exception, e:
        xbmcgui.Dialog().ok("[COLOR tomato]Cerebro TV[/COLOR]","Server Busy.......", "Please Try Again.")
        #print(e)
        exit()
 

def DownloaderClass(url,dest):
    if os.path.exists(file):
        utils.DeleteFile(file)
        xbmc.sleep(1000)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]Cerebro TV Installer[/COLOR]","Downloading Build Data","This may take some time......")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        if os.path.exists(file):
            dp.create("[COLOR tomato]Cerebro TV[/COLOR]","Installing Please Wait","This will take some time")
            zfile = zipfile.ZipFile(file, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, ROOT)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
			
        #zfile.extractall(HOME)
        dp.create("[COLOR tomato]Cerebro TV[/COLOR]","Doing Clean Up","Nearly Done.....")
        utils.DeleteFile(file)
        xbmc.sleep(2000)
        utils.DeleteFile(file3)
        xbmc.sleep(2000)
        sfile.rmtree(HOME)
        xbmc.sleep(2000)
        dp.close()
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR=red][B] ## Completed ##[/COLOR][/B]", "Kodi Will now exit", "Thank you for choosing Cerebro TV","Press OK to Continue")
        killxbmc()
        
    except Exception, e:
        pass


 
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        #print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        #dp.close()


		
if os.path.exists(file100):
	exit()
else:
    choice = xbmcgui.Dialog().yesno('[COLOR tomato]Cerebro TV[/COLOR]', 'Would you like to install Cerebro TV Now', 'www.cerebrotv.co.uk', nolabel='No, Forget it?',yeslabel='Yes, Continue!')
    if choice == 0:
        exit()
    elif choice == 1:
        DownloaderClass(LOCATION,file)
	
	
exit()


