import utils
import xbmc
import os
import xbmcgui
import zipfile
import sfile
import download
import urllib
import urllib2

#dp = xbmcgui.DialogProgress()
#dp.create("[COLOR tomato]CerebroTV[/COLOR]","Connection to Server","Please Wait.....")
#xbmc.sleep(1000)



HOME2     = xbmc.translatePath('special://userdata')
file2 = os.path.join(HOME2, 'megatvbox.xml')

HOME     = xbmc.translatePath('special://home')
file4 = os.path.join(HOME2, 'networksettings.xml')

file98 = os.path.join(HOME2, 'megatvbox.xml') 

#with open(file98, 'r') as myfile:
#        data=float(myfile.read())
		
with open(file98, 'r') as myfile:
    data=float(myfile.read())

megaver = float(data)+0.1

LOCATION     = "http://megatvbox.co.uk/TV-DATA/updater.php?v="+str(megaver)

ROOT     = xbmc.translatePath('special://home')
file     = os.path.join(HOME, '_mega_temp.zip')
GETTEXT  = utils.GETTEXT

file3 = os.path.join(HOME, 'mchangelog.xml')


def intro():
    file2 = 'special://userdata/addon_data/mtvb2.mp4'
    xbmc.Player().play(file2)
    xbmc.sleep(15000)
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=blue][B]CerebroTV[/COLOR][/B]","Please Wait Shutting Down....","www.megatvbox.co.uk")
    
 
def killxbmc():

    with open(file4, 'r') as myfile:
        boxid=myfile.read()
    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
    xbmc.sleep(1000)
    #choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    #if choice == 0:
    #    return
    #elif choice == 1:
    #    pass
    myplatform = platform()
    dialog = xbmcgui.Dialog()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        try: os.system("su -c 'reboot'")
        except: pass
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')    
    elif myplatform == 'linux': #Linux
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
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
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    elif myplatform == 'android': # Android  
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&die=1').read()
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
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    elif myplatform == 'windows': # Windows
        #response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
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
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)') 
    else: #ATV
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
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
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
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

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to download needed data....", "Will Try Again.","Press OK to Continue")
    xbmc.sleep(1000)
    DownloaderClass(LOCATION,file)


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading New Update","This make take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
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
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","Update Complete","Closing Kodi....")	
        killxbmc()
        exit()

    except Exception, e:
        noconnection()
        #print(e)
        exit()
 
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
 

 
if os.path.exists(file):
    utils.DeleteFile(file)



def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0

	
if ping("www.google.co.uk"):
    import re, uuid
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    if os.path.exists(file4):
        pass
    else:
        fo = open(iddata, "w")
        fo.write('install01');
        fo.close()
        xbmc.sleep(1000)
    with open(file4, 'r') as myfile:
        boxid=myfile.read()
    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&ok=OK&mac='+str(mac))
    data3=response.read()
    auth = str(data3)
    if auth == "BAD":
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=yellow][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")	
        xbmc.sleep(15000)
        intro()
        killxbmc()
        xbmc.executebuiltin('quit')
        exit()
    if auth == "INUSE":
        dp = xbmcgui.DialogProgress()
        dialog.ok("[COLOR=yellow][B]INFORMATION[/COLOR][/B]", "Your Code is in use by someone else.", "Or your have just crashed....","Please Wait 10 minuets and try again or Contact you seller......")
        dp.create("[COLOR=red][B]INFORMATION[/COLOR][/B]","Your Code is in use by someone else","Please Wait 10 minuets and try again or Contact you seller......")
        xbmc.sleep(15000)
        intro()
        killxbmc()
        xbmc.executebuiltin('quit')
        exit()
		
    dialog = xbmcgui.Dialog()
    if dialog.yesno("[COLOR yellow]CerebroTV[/COLOR]"," " ,"[COLOR yellow]Start The Update Now?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
        DownloaderClass(LOCATION,file)
        #xbmc.executebuiltin('RunAddon(script.program.megatvpopup)')
    else:
        dialog.ok("[COLOR yellow]CerebroTV[/COLOR]", "Update Cancled", "Somethings will not work right......","Press OK to Continue")
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to connect to the internet", "","Press OK to Continue")
    myplatform = platform()
    if myplatform == 'windows': # Windows
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'linux': #Linux
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'osx': # OSX
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        intro()
        killxbmc()
    elif myplatform == 'android': # Android  
        dialog.ok("[COLOR=yellow][B] ## CONNECTION ERROR ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        xbmc.executebuiltin(StartAndroidActivity('com.mbx.settingsmbox'))
        if dialog.yesno("[COLOR yellow]CerebroTV[/COLOR]"," " ,"[COLOR yellow]Start The Update Now?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
            dialog.ok("[COLOR=yellow][B] ## yes ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        else:
            dialog.ok("[COLOR=yellow][B] ## no ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")             		
        exit();
        		






