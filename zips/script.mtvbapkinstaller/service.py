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



HOME     = xbmc.translatePath('special://userdata/')
HOME2    = xbmc.translatePath('special://home/')
LOCATION = "http://megatvbox.co.uk/TV-DATA/menu-data.zip"
file200 = os.path.join(HOME, 'freeview.xml') 

ROOT     = xbmc.translatePath('special://userdata/addon_data/plugin.program.super.favourites/')
file     = os.path.join(HOME, '_mega_temp.zip')
file3    = os.path.join(HOME, 'lock.xml')
iddata   = os.path.join(HOME, 'networksettings.xml')
GETTEXT  = utils.GETTEXT

file201     = os.path.join(HOME2, 'skin.zip')

if os.path.exists(file200):
    letsgo="ok"
else:
    letsgo="nogo"
    fo = open(file200, "w")
    fo.write('0');
    fo.close()
    
    
with open(file200, 'r') as myfile:
    data200=float(myfile.read())
isfreeview = float(data200)



skindir = xbmc.getSkinDir()


file2dl = "http://megatvbox.eu/freeview.zip"

if isfreeview > 0:
    msgstr = " Swap to Free View Only Mode"
    file2dl = "http://megatvbox.eu/freeview.zip"
else:
    msgstr = "Swap to FULL Only Mode"
    file2dl = "http://megatvbox.eu/full.zip"
    
def noconnection():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]Internet Connection Error[/COLOR][/B]","[B][COLOR=red]CerebroTV will now close / reboot[/COLOR][/B]","Please check your internet connection.")
    xbmc.sleep(6500)
    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    exit()

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV[/COLOR]", line1 = "[COLOR yellow]Downloading new menu data[/COLOR].", line2 = "[COLOR gold]Please Wait Download in Progress[/COLOR]", line3 = "test")
      dp.update(percent)


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

        
def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading New Update","This make take a while.")
    try:
        dialog = xbmcgui.Dialog()
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading New Update","This make take a while.")
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        zfile = zipfile.ZipFile(file201, 'r')	
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
			
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME2)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
                    
        

        utils.DeleteFile(file201)	
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
        exit()

    except Exception, e:
        noconnection()
        #print(e)
        exit()
    

if skindir != "skin.titan":
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## SOMETHING IS WRONG! ##[/COLOR][/B]", "We will try and fix it now", "","Press OK to Continue")
    DownloaderClass2(file2dl,file201)
    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')




noconnection = False
doload = False
fo = open(file3, "w")
fo.write(str(0));
fo.close()
#xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper2)') 
def intro():
    file2 = 'special://userdata/addon_data/mtvb.mp4'
    xbmc.Player().play(file2)
    #xbmc.sleep(15000)
    #xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper)')
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR=white][B]CerebroTV[/COLOR][/B]","Please Wait Starting Up","www.megatvbox.co.uk")
    xbmc.sleep(1000)
    
    
def intro2():
    file2 = 'special://userdata/addon_data/mtvb2.mp4'
    xbmc.Player().play(file2)
    xbmc.sleep(15000)
    #xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper)')
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]CerebroTV[/COLOR][/B]","Please Wait Shutting Down....","www.megatvbox.co.uk")
    exit()
   

def killxbmc():
    #choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    #if choice == 0:
    #    return
    #elif choice == 1:
    #    passv
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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=red]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=red]DO NOT[/COLOR] press OK",'')
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
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=red]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=red]DO NOT[/COLOR] press OK",'')
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
        try: os.system("su -c 'reboot'")
        except: pass
        xbmc.executebuiltin('Quit')		
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=red]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=red]DO NOT[/COLOR] press OK",'')
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        
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
        xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=red]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=red]DO NOT[/COLOR] press OK",'')
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
        xbmc.executebuiltin('Quit')
        dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=red]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=red]DO NOT[/COLOR] press OK",'')
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
    
	



    
	
def DownloaderClass(url,dest):
    utils.DeleteFile(file)
    xbmc.executebuiltin('UpdateAddonRepos')
    xbmc.executebuiltin('UpdateLocalAddons')
    xbmc.executebuiltin('RunAddon(script.cachesystem)')
    xbmc.executebuiltin('RunAddon(script.program.megatvboxcheckversion)')
    

 

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

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
			

def get_external_ip():
    site = urllib.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address			


def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Downloading New Update","This make take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Updater[/COLOR]","Installing New Update","Please Wait. [COLOR red]DO NOT TURN OFF!!![/COLOR]")
        if os.path.exists(file201):
            file3 = os.path.join(HOME, 'mchangelog.xml')
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
                    zfile.extract(item, HOME2)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
        

        utils.DeleteFile(file201)	
        dp.create("[COLOR tomato]CerebroTV[/COLOR]","Update Complete","Closing Kodi....")	
        killxbmc()
        exit()

    except Exception, e:
        noconnection()
        #print(e)
        exit()    
    
    
###### START OF CODE #######
dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()
if skindir != "skin.titan":
    dialog.ok("[COLOR=yellow][B]HMMMMMMM NO LAYOUT?????[/COLOR][/B]", "We have detected a problem...", "We will try and fix it","Press OK to Continue")
    if isfreeview > 0:
        DownloaderClass2(file2dlfile201,)
    else:
        DownloaderClass2(file2dl,file201)
    exit()
#intro()
#xbmc.sleep(15000) #pause for video
xbmc.executebuiltin("Notification(PLEASE WAIT, SYSTEM IS STARTING UP!,20000,)")
ipaddy="0.0.0.0"
dp.create("[COLOR=white][B]Checking Internet Connection[/COLOR][/B]","[B][COLOR=yellow]Conecting to..........[/COLOR][/B]","mtvb.co.uk")
xbmc.sleep(3500)
dp.close()
### CHECK SERVER ###
if ping("google.co.uk"):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR=white][B]Connection Successful[/COLOR][/B]","[B][COLOR=yellow]Please wait..........[/COLOR][/B]","Checking your Authentication code....")
    xbmc.sleep(3500)
    dp.close()
    doload = True
else:
    doload = False
    noconnection()
    exit()
    

if os.path.exists(iddata):
    #dialog.ok("[COLOR=yellow][B]FILE FOUND[/COLOR][/B]", "FILE FOUND", "","FILE FOUND")
    with open(iddata, 'r') as mymega:
        userid=mymega.read()	

    if userid == "megatvbot1234567890qwertyuiop2016biglad":
        dialog.ok("[COLOR=yellow][B]First Time Load[/COLOR][/B]", "Setting Up Some Data Files.", "Kodi will now close.","Press OK to Continue")
        #xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper2)') 
        try: utils.DeleteFile(iddata)
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
        exit()

    if userid == "0":
        dialog.ok("[COLOR=yellow][B]First Time Load[/COLOR][/B]", "Setting Up Some Data Files.", "Kodi will now close.","Press OK to Continue")
        #xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper2)') 
        try: utils.DeleteFile(iddata)
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
        exit()
		
    if userid == "-1":
        dialog.ok("[COLOR=yellow][B]WARNING[/COLOR][/B]", "You Have been ripped off", "Please return your device to seller for full refund","Buy CerebroTV @ www.megawow.co.uk The only site for official boxes")
        #xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper2)') 
        try: utils.DeleteFile(iddata)
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
        exit()

    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ok=OK&ip='+ipaddy).read()
    if response == "INUSE":
        dp = xbmcgui.DialogProgress()
        dialog.ok("[COLOR=red][B]INFORMATION[/COLOR][/B]", "Your Code ("+str(userid)+") is in use on our system.", "If you have just crashed Please Wait 5 minuets and try again","If you keep getting this message please contact us http://m.me/mtvb1")
        #dp.create("[COLOR=red][B]INFORMATION[/COLOR][/B]","Your Code is in use by someone else","Please Wait 10 minuets and try again or Contact you seller......")
        #xbmc.sleep(15000)
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    elif response == "OK":
        dp.create("[COLOR=white][B]Authentication Successful[/COLOR][/B]","[B][COLOR=yellow]Thank you choosing CerebroTV[/COLOR][/B]","[B][COLOR=red]ID : "+str(userid)+"[/COLOR][/B]")
        xbmc.sleep(3500)
        dp.close()
        DownloaderClass(LOCATION,file)
    else:
        dialog.ok("[COLOR=yellow][B]INFORMATION[/COLOR][/B]", "Due to unauthorized sellers trying to use our system", "","We have implemented an Authentication system.....")
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]This could also be due to the auth server been offline, please try again.[/B]")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=yellow][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]This could also be due to the auth server been offline, please try again.[/B]")	
        xbmc.sleep(15000)
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
else:
    dialog.ok("[COLOR=red][B]CerebroTV Authentication System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","www.facebook.com/mtvb1/")
    userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
    if userid =="":
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]","CerebroTV WILL NOW EXIT","PLEASE TRY AGAIN")
        xbmc.sleep(15000)		
        try: utils.DeleteFile(iddata)
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    choice = xbmcgui.Dialog().yesno('[COLOR=white]Is this code correct[/COLOR]', '[B][COLOR=white]Is this code correct[/COLOR] [COLOR=red]'+str(userid)+'[/COLOR][/B]', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Continue')
    if choice == 0:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]","CerebroTV WILL NOW EXIT","PLEASE TRY AGAIN")
        xbmc.sleep(15000)		
        try: utils.DeleteFile(iddata)
        except: pass
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #elif choice == 1:
        #pass
    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
    if response == "INUSE":	
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=yellow][B]INFORMATION[/COLOR][/B]","Your Code has been used by someone else","Contact you seller......")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=yellow][B]INFORMATION[/COLOR][/B]","Your Code has been used by someone else","Contact you seller......")
        xbmc.sleep(15000)
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    elif response == "OK":	
        fo = open(iddata, "w")
        fo.write(userid);
        fo.close()
        dp.create("[COLOR=white][B]Authentication Successful[/COLOR][/B]","[B][COLOR=yellow]Thank you choosing CerebroTV[/COLOR][/B]","[B][COLOR=red]ID : "+str(userid)+"[/COLOR][/B]")
        xbmc.sleep(3500)
        dp.close()
        DownloaderClass(LOCATION,file)
    else:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR=red][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")
        xbmc.sleep(15000)
        dp.close()
        dp.create("[COLOR=yellow][B]Authentication code Not Found![/COLOR][/B]","[B]Please Contact your seller as your code is unauthorized","[B]Only buy from www.megatvbox.co.uk[/B]")
        xbmc.sleep(15000)
        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')		
	



