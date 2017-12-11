import xbmc
import utils
import os
import xbmcgui
import sfile
import urllib
import urllib2
import time
import re
import downloader
import extractor
import xbmc

#from resources.lib.kodion.impl import Context
#from resources.lib.kodion.constants import setting
DoStart = 0
ipaddy = "0.0.0.0"

dialog = xbmcgui.Dialog() 
update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV INSTALLER[/COLOR]","","[COLOR tomato]Would You Like to Install Now[/COLOR]?")
if not update: #IT'S BACKWARDS
    exit()

PART1  = "http://megatvbox.eu/install1.zip"
PART2  = "http://megatvbox.eu/install2.zip"
PART3  = "http://megatvbox.eu/install3.zip"
PART4  = "http://mtvb.co.uk/install4.zip"

USERDATA    = xbmc.translatePath('special://userdata/')
HOME        = xbmc.translatePath('special://home/')
ADDONS      = xbmc.translatePath('special://home/addons')
IDPATH      = '/storage/emulated/0/Download/MTVB/' 

file1     =  os.path.join(HOME, 'install.zip')
file2     =  os.path.join(HOME, 'install2.zip')
file3     =  os.path.join(HOME, 'install3.zip')
file4     =  os.path.join(HOME, 'install4.zip')
iddata    =  os.path.join(HOME, 'userdata/networksettings.xml')
idbackup = os.path.join(IDPATH, 'datafile.bin')

if not os.path.exists(IDPATH):
    try: os.mkdir(IDPATH)
    except: pass


if os.path.exists(iddata):
    with open(iddata, 'r') as myfile:
        userid=myfile.read()
    DoStart = 1
    
if os.path.exists(IDPATH):
    try:
        with open(idbackup, 'r') as myfile:
            userid=myfile.read()
        DoStart = 1
    except: pass
    
    

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
        #try: os.system("su -c 'reboot'")
        #except:  dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')		
        #dialog.ok("[COLOR=red][B]CerebroTV Updater[/COLOR][/B]", "If you\'re seeing this message it means the updater was unable", "to close kodi or reboot your deivice. Please pull the power lead or power off your tablet [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu. [COLOR=lime]DO NOT[/COLOR] press OK",'')
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
            
            
if DoStart ==0:            
    dialog.ok("[COLOR=red][B]CerebroTV Auth System[/COLOR][/B]", "You will now be asked for your [COLOR=red]Authentication Code[/COLOR]", "If you dont have one please visit","www.facebook.com/cerebrotvuk/")
    userid=Search('[B][COLOR=white]Please enter your Authentication code[/COLOR][/B]')
    if userid =="":
        dp.create("[COLOR=yellow][B]CODE NOT RIGHT[/COLOR][/B]",".","PLEASE TRY AGAIN")
        xbmc.sleep(15000)
        exit()
        
    response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&ip='+str(ipaddy)).read()
    if response == "OK":
        fo = open(iddata, "w")
        fo.write(userid);
        fo.close()
        DoStart = 1
    
    
if DoStart ==0:
    dialog.ok("[COLOR=red][B]CerebroTV Auth System[/COLOR][/B]", "Code Not Found", "Please Try Again","www.facebook.com/cerebrotvuk/")
    #xbmc.executebuiltin('RunAddon(script.cerebrotv)')
    exit()
    

response2 = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/updaternew.php?show=yes&v=1').read()
UPDATE ="http://mtvb.co.uk/"+str(response2)+".zip"



dp = xbmcgui.DialogProgress()
dp.create("Preparing System for Install","",'DO NOT TURN OFF', ' ')
#with open(iddata, 'r') as myfile:
#    userid=myfile.read()
percent = 80 
dp.update(percent)
try:
    fo = open(iddata, "w")
    fo.write(userid);
    fo.close()
except: pass
percent = 90 
dp.update(percent)
xbmc.sleep(5500)
try: 
    fo = open(idbackup, "w")
    fo.write(userid);
    fo.close()
except: pass
percent = 2100 
dp.update(percent)
xbmc.sleep(1500)
dp.close()

def getOld(old):
	try:
		old = '"%s"' % old 
		query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (old)
		response = xbmc.executeJSONRPC(query)
		response = simplejson.loads(response)
		if response.has_key('result'):
			if response['result'].has_key('value'):
				return response ['result']['value'] 
	except:
		pass
	return None

def setNew(new, value):
    try:
        new = '"%s"' % new
        value = '"%s"' % value
        query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % (new, value)
        response = xbmc.executeJSONRPC(query)
    except:
        pass
    return None

def swapSkins(skin):
	old = 'lookandfeel.skin'
	value = skin
	current = getOld(old)
	new = old
	setNew(new, value)

skindir = xbmc.getSkinDir()

downloader . download(PART1,file1,"Downloading Installer Part 1")
extractor . extract(file1,HOME,"Unpacking Part 1")
downloader . download(PART2,file2,"Downloading Installer Part 2")
extractor . extract(file2,HOME,"Unpacking Part 2")
downloader . download(PART3,file3,"Downloading Installer Part 3")
extractor . extract(file3,HOME,"Unpacking Part 3")
downloader . download(UPDATE,file4,"Downloading Latest Build Info")
extractor . extract(file4,HOME,"Unpacking Data")
try:
    fo = open(iddata, "w")
    fo.write(userid);
    fo.close()
except: pass
try: 
    fo = open(idbackup, "w")
    fo.write(userid);
    fo.close()
except: pass
#swapSkins("skin.titan")
#xbmc.sleep(22000)
killxbmc()