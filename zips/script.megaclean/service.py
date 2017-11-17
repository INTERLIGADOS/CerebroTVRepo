






































































































































































































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
from resources.lib.kodion.impl import Context
from resources.lib.kodion.constants import setting

context = Context()

version = context.get_system_version().get_version()
application = context.get_system_version().get_app_name()
settings = context.get_settings()


appversion = 0
if version >= (17, 0):
    appversion = "kodi17"
elif version >= (16, 5) and application == 'SPMC':
    appversion = "spmc"
else:
    appversion = "kodi16"
    
HOME     = xbmc.translatePath('special://addons/script.megatvinstall/')
HOME2    = xbmc.translatePath('special://userdata/')
HOME3    = xbmc.translatePath('special://home/')
IDBACKUP = xbmc.translatePath('special://home/MTVB-DATA/')
LOCATION  = "http://mtvb.co.uk/install.zip"
LOCATION1 = "http://mtvb.co.uk/install2.zip"
LOCATION2 = "http://mtvb.co.uk/install3.zip"


ROOT     = xbmc.translatePath('special://home')
file     =   os.path.join(HOME2, 'install.zip')
file1     =  os.path.join(HOME2, 'install2.zip')
file2     =  os.path.join(HOME2, 'install3.zip')
file3    = os.path.join(HOME, 'service.py')
file100  = os.path.join(HOME2, 'megatvbox.xml')
file200 = os.path.join(HOME2, 'freeview.xml') 
file201     = os.path.join(HOME3, 'skin.zip')
file300     = os.path.join(HOME3, '_mega_temp.zip')
iddata   = os.path.join(HOME2, 'networksettings.xml')
iddata2  = os.path.join(IDBACKUP, 'networksettings.xml')
ipaddy="0.0.0.0"




legacy = os.path.join(HOME2, 'mchangelog.xml')

if os.path.exists(legacy):
    dummyval=1
else:
    isfv = 'TEST|TEST'
    fo = open(legacy, "w")
    fo.write(isfv);
    fo.close()
    
if os.path.exists(file200):
    dummyval=1
else:
    isfv = '0'
    fo = open(file200, "w")
    fo.write(isfv);
    fo.close()
    
if os.path.exists(file100):
    dummyval=1
else:
    isfv = '1'
    fo = open(file100, "w")
    fo.write(isfv);
    fo.close()

with open(file200, 'r') as myfile:
    data200=float(myfile.read())
isfreeview = float(data200)

if isfreeview > 0:
    msgstr = " Swap to Free View Only Mode"
    file2dl = "http://megatvbox.eu/freeview.zip"
else:
    msgstr = "Swap to FULL Only Mode"
    file2dl = "http://megatvbox.eu/full.zip"

with open(file100, 'r') as myfile:
    data=float(myfile.read())      
response2 = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/updater.php?show=yes&v=1').read()
#dialog = xbmcgui.Dialog()
#dialog.ok("[COLOR=red][B]INFO[/COLOR][/B]", str(response2), str(response2),"www.facebook.com/mtvb1/")
file2dl1="http://megatvbox.eu/"+str(response2)+".zip"


GETTEXT  = utils.GETTEXT
noconnection = False

dp = xbmcgui.DialogProgress()



def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False 



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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        try: os.system('adb shell am force-stop com.semperpax.spmc16')
        except: pass
        try: os.system("su -c 'reboot'")
        except: pass		
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    
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
      dp = utils.Progress("[COLOR tomato]CerebroTV[/COLOR]", line1 = "[COLOR yellow]Downloading new menu data[/COLOR].", line2 = "[COLOR gold]Please Wait Download in Progress[/COLOR]", line3 = "test")
      dp.update(percent)

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to connect to the internet", "","Press OK to Continue")
    myplatform = platform()
    if myplatform == 'windows': # Windows
        dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'linux': #Linux
        dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'osx': # OSX
        dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Kodi will now close please connect your computer to the internet", "","Press OK to Continue")
        killxbmc()
    elif myplatform == 'android': # Android  
        dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "We will now try and open network settings..", "","Press OK to Continue")
        xbmc.executebuiltin("StartAndroidActivity(com.mbx.settingsmbox)")
        if dialog.yesno("[COLOR yellow]CerebroTV[/COLOR]"," " ,"[COLOR yellow]Did You Get Connected?[/COLOR]", " ",'[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
            xbmc.sleep(3000)
            DownloaderClass(LOCATION,file)
        else:
            dialog.ok("[COLOR=red][B]ERROR NO CONNECTION[/COLOR][/B]", "Kodi will now close.", "","Press OK to Continue")
            killxbmc()			
        exit();		

def DownloaderClass3(url,dest):
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFO[/COLOR][/B]", str(file2dl1), str(dest),"www.facebook.com/mtvb1/")
    #killxbmc()
    
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading Latest Build Data","This make take a while.")
    try:
        urllib.urlretrieve(file2dl1,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        if os.path.exists(file300):
            file3 = os.path.join(HOME2, 'mchangelog.xml')
            open(file3, 'w+')
            userdata = "test|test"
            with open(file3, 'w') as f:
                f.write(userdata)
            zfile = zipfile.ZipFile(file300, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, HOME3)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        

        dp.create("[COLOR tomato]CerebroTV[/COLOR]","Cleaning Up Files","Pleaze Wait")	
        xbmc.sleep(5000)
        utils.DeleteFile(file)
        utils.DeleteFile(file1)
        try: os.unlink(file1)
        except: pass 
        utils.DeleteFile(file2)
        utils.DeleteFile(file3)
        utils.DeleteFile(file200)
        utils.DeleteFile(file300)
        utils.DeleteFile(file1)
        try: os.remove(file)
        except: pass
        try: os.remove(file1)
        except: pass
        try: os.remove(file2)
        except: pass
        try: os.remove(file3)
        except: pass
        try: os.remove(file200)
        except: pass
        try: os.remove(file300)
        except: pass
        try: os.remove(file1)
        except: pass
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","Update Complete","Closing....")
        xbmc.sleep(5000)
        killxbmc()
        exit()

    except Exception, e:
        xbmcgui.Dialog().ok("[COLOR tomato]CerebroTV[/COLOR]","Server Busy.......", "Please Try Again.")
        killxbmc()
        #print(e)
        exit()
 

def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFO[/COLOR][/B]", str(url), str(dest),"www.facebook.com/mtvb1/")
    #killxbmc()
    dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading Layout Info ","This make take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        if os.path.exists(dest):
            file3 = os.path.join(HOME2, 'mchangelog.xml')
            open(file3, 'w+')
            userdata = "test|test"
            with open(file3, 'w') as f:
                f.write(userdata)
            zfile = zipfile.ZipFile(file201, 'r')	
            nItem = float(len(zfile.infolist()))
            index = 0
            for item in zfile.infolist():
                index += 1
			
                percent  = int(index / nItem *100)
                filename = item.filename
                dp.update(percent)
                try:
                    zfile.extract(item, HOME3)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        

        
        
        DownloaderClass3(file2dl1,file300)
        exit()

    except Exception, e:
        xbmcgui.Dialog().ok("[COLOR tomato]CerebroTV[/COLOR]","Server Busy.......", "Please Try Again.")
        killxbmc()
        #print(e)
        exit()
 

def DownloaderClass(url,dest):
    if os.path.exists(file):
        os.remove(file)
        xbmc.sleep(1000)
    #DownloaderClass2(file2dl,file201)
    #exit()
    #filevid = 'http://mtvb.co.uk/mtvb.mp4'
    #xbmc.Player().play(filevid)  
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Installer[/COLOR]","Downloading Data [COLOR=green]Part 1[/COLOR]","[COLOR=red]DO NO TURN OFF[/COLOR]")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        xbmc.sleep(1000)
        dp.create("[COLOR tomato]CerebroTV Installer[/COLOR]","Downloading Data [COLOR=green]Part 2[/COLOR]","[COLOR=red]DO NO TURN OFF[/COLOR]")
        urllib.urlretrieve(LOCATION1,file1,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        xbmc.sleep(1000)
        dp.create("[COLOR tomato]CerebroTV Installer[/COLOR]","Downloading Data [COLOR=green]Part 3[/COLOR]","[COLOR=red]DO NO TURN OFF[/COLOR]")
        urllib.urlretrieve(LOCATION2,file2,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Installer[/COLOR]","Downloading Data [COLOR=green]Part 3[/COLOR]","[COLOR=red]DO NO TURN OFF[/COLOR]")
        if os.path.exists(file):
            dp.create("[COLOR tomato]CerebroTV[/COLOR]","Installing [COLOR=green]Part 1[/COLOR] Please Wait","[COLOR=red]DO NO TURN OFF[/COLOR].. THIS MAKE TAKE SOME TIME")
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
                    
        if os.path.exists(file1):
            dp.create("[COLOR tomato]CerebroTV[/COLOR]","Installing [COLOR=green]part 2[/COLOR] Please Wait","[COLOR=red]DO NO TURN OFF[/COLOR].. THIS MAKE TAKE SOME TIME")
            zfile = zipfile.ZipFile(file1, 'r')	
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
                    
        if os.path.exists(file2):
            dp.create("[COLOR tomato]CerebroTV[/COLOR]","Installing [COLOR=green]part 3[/COLOR] Please Wait","[COLOR=red]DO NO TURN OFF[/COLOR].. THIS MAKE TAKE SOME TIME")
            zfile = zipfile.ZipFile(file1, 'r')	
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
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]","Doing Clean Up","Nearly Done.....")
        utils.DeleteFile(file)
        utils.DeleteFile(file1)
        utils.DeleteFile(file2)
        utils.DeleteFile(file3)
        utils.DeleteFile(file200)
        utils.DeleteFile(file300)
        utils.DeleteFile(file1)
        try: os.remove(file)
        except: pass
        try: os.remove(file1)
        except: pass
        try: os.remove(file2)
        except: pass
        try: os.remove(file3)
        except: pass
        try: os.remove(file200)
        except: pass
        try: os.remove(file300)
        except: pass
        try: os.remove(file1)
        except: pass
        #os.remove(file)
        #xbmc.sleep(2000)
        #os.remove(file1)
        #os.remove(file3)
        #xbmc.sleep(2000)
        #sfile.rmtree(HOME)
        #xbmc.sleep(2000)
        #dp.close()
        #dialog = xbmcgui.Dialog()
        #os.remove(file)
        DownloaderClass2(file2dl,file201)
        #DownloaderClass3(file2dl1,file300)
        #dialog.ok("[COLOR=red][B] ## Completed ##[/COLOR][/B]", "Kodi Will now exit", "Thank you for choosing CerebroTV","Press OK to Continue")
        #killxbmc()
        
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

        
def GetCode():
    if os.path.exists(iddata):
        DownloaderClass(LOCATION,file)
        return
    if os.path.exists(iddata2):
        with open(iddata2, 'r') as myfile:
            data300=str(myfile.read())
        fo = open(iddata, "w")
        fo.write(data300);
        fo.close()
        DownloaderClass(LOCATION,file)
        return
    dialog = xbmcgui.Dialog()
    dp = xbmcgui.DialogProgress()
    dialog.ok("[COLOR=red][B]CerebroTV Authentication System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","www.facebook.com/mtvb1/")
    userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
    if userid =="":
        dp.create("[COLOR=red][B]CODE NOT RIGHT[/COLOR][/B]","CerebroTV WILL NOW EXIT","PLEASE TRY AGAIN")
        xbmc.sleep(15000)		
        try: os.remove(iddata)
        except: pass
        killxbmc()
    choice = xbmcgui.Dialog().yesno('[COLOR=white]Is this code correct[/COLOR]', '[B][COLOR=white]Is this code correct[/COLOR] [COLOR=red]'+str(userid)+'[/COLOR][/B]', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Continue')
    if choice == 0:
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR=red][B]CODE NOT RIGHT[/COLOR][/B]","CerebroTV WILL NOW EXIT","PLEASE TRY AGAIN")
        #xbmc.sleep(15000)		
        try: os.remove(iddata)
        except: pass
        xbmc.sleep(2000)
        GetCode()
    #elif choice == 1:
        #pass
    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
    if response == "INUSE":	
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]INFORMATION[/COLOR][/B]","Your Code has been used by someone else","Contact you seller......")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=red][B]INFORMATION[/COLOR][/B]","Your Code has been used by someone else","Contact you seller......")
        xbmc.sleep(15000)
        killxbmc()
    elif response == "OK":	
        fo = open(iddata, "w")
        fo.write(userid);
        fo.close()
        dp.create("[COLOR=white][B]Authentication Successful[/COLOR][/B]","[B][COLOR=red]Thank you choosing CerebroTV[/COLOR][/B]","[B][COLOR=red]ID : "+str(userid)+"[/COLOR][/B]")
        xbmc.sleep(3500)
        dp.close()
        DownloaderClass(LOCATION,file)
    else:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")
        xbmc.sleep(15000)
        killxbmc()
    exit()


  
#if os.path.exists(file200):
#    letsgo="ok"
#else:
#letsgo="nogo"

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select('[B][COLOR=red]CerebroTV[/COLOR][COLOR=red] Wizard[/COLOR][/B]', [
	'[B][COLOR=red]      Install Build for Kodi 17[/COLOR][/B]',
	'[B][COLOR=blue]      Exit[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 

def function1():
    isfv = '0'
    fo = open(file200, "w")
    fo.write(isfv);
    fo.close()
    GetCode()
    
def function2():
    killxbmc()
    exit()
    
#if appversion == "kodi17":
#    function1()

    
choice = xbmcgui.Dialog().yesno('[COLOR tomato]CerebroTV[/COLOR]', '[COLOR yellow][B]CLEAN & RE-INSTALL[/B][/COLOR]', '', nolabel='[COLOR green][B]START[/B][/COLOR]',yeslabel='[COLOR red][B]CANCLE[/B][/COLOR]')
if choice == 1:
    exit()

    
savedid = ""
if os.path.exists(iddata):
    with open(iddata, 'r') as myfile:
        savedid=myfile.read()
dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]CerebroTV[/COLOR]","DELETING OLD FILES","PLEASE WAIT")
#xbmc.executebuiltin("Notification(CerebroTV,Deleting Files, Please wait,7000,)")


thumbs     = xbmc.translatePath('special://home/Thumbnails/')
addons     = xbmc.translatePath('special://home/addons/')
userdata     = xbmc.translatePath('special://home/userdata/')
temp     = xbmc.translatePath('special://temp/')

try: os.remove(thumbs)
except: pass

try: os.rmdir(addons)
except: pass

try: os.remove(addons)
except: pass

try: os.remove(userdata)
except: pass

try: os.rmdir(userdata)
except: pass

try: sfile.rmtree(thumbs)
except: pass

try: sfile.rmtree(addons)
except: pass

try: sfile.rmtree(userdata)
except: pass

try: sfile.rmtree(temp)
except: pass

if not os.path.exists(thumbs):
    os.makedirs(thumbs)

if not os.path.exists(addons):
    os.makedirs(addons)
    
if not os.path.exists(userdata):
    os.makedirs(userdata)
    
if savedid != "":
    fo = open(iddata, "w")
    fo.write(savedid);
    fo.close()
    GetCode()
    

		
choice = xbmcgui.Dialog().yesno('[COLOR tomato]CerebroTV[/COLOR]', 'Would you like to install CerebroTV Now', 'www.megatvbox.co.uk', nolabel='No, Forget it?',yeslabel='Yes, Continue!')
if choice == 0:
    exit()
elif choice == 1:
    menuoptions()
    #GetCode()
	
	
exit()


