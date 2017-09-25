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
import shutil, errno
from resources.lib.kodion.impl import Context
from resources.lib.kodion.constants import setting

context = Context()

version = context.get_system_version().get_version()
application = context.get_system_version().get_app_name()
settings = context.get_settings()


dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()

appversion = 0
if application == 'SPMC':
    appversion = "SPMC"
    otherapp = "KODI"
else:
    appversion = "KODI"
    otherapp = "SPMC"


if appversion == 0:
    dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "", "UPDATE KODI OR SPMC TO LATEST RELEASE","")
    exit()

HOME     = xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/')
HOME2    = xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/')
HOME3    = xbmc.translatePath('special://home/')


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
    
myplatform = platform()


if not myplatform == 'android':
    dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "ANDROID SUPPORT ONLY", "","For Now")    
    exit()
    
if appversion == "KODI":
    copy1 = xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/addons/')
    copy2 = xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/userdata/')
    copy3 = xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/addons/')
    copy4 = xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/userdata/')
    if not os.path.exists(copy3):
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "", "INSTALL SPMC","")
        exit()
    
if appversion == "SPMC":
    copy1 = xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/addons/')
    copy2 = xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/userdata/')
    copy3 = xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/addons/')
    copy4 = xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/userdata/')
    if not os.path.exists(copy3):
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "", "INSTALL KODI","")
        exit()

update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV Build Mover[/COLOR]","","[COLOR gold]ANDROID 5+ Needed & ROOTED device.[/COLOR]" ," Continue?")
if not update:
    exit()

if appversion == "KODI":
    dp.create("[COLOR=white][B]PREPPING SPMC[/COLOR][/B]","","PLEASE WAIT") 
    shutil.rmtree(xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/addons/'))
    xbmc.sleep(5000)
    shutil.rmtree(xbmc.translatePath('/storage/emulated/0/Android/data/com.semperpax.spmc16/files/.spmc/userdata/'))
    xbmc.sleep(5000)

    
if appversion == "SPMC":
    dp.create("[COLOR=white][B]PREPPING KODI[/COLOR][/B]","","PLEASE WAIT") 
    shutil.rmtree(xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/addons/'))
    xbmc.sleep(5000)
    shutil.rmtree(xbmc.translatePath('/storage/emulated/0/Android/data/org.xbmc.kodi/files/.kodi/userdata/'))
    xbmc.sleep(5000)


xbmc.sleep(5000)
dp.close()
def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
dp.create("[COLOR=white][B]COPYING[/COLOR] [COLOR=gold]ADDONS[/COLOR][/B]","[B][COLOR=green]FROM :"+str(appversion)+"[/B][/COLOR] - [B][COLOR=red]TO :"+str(otherapp)+"[/B][/COLOR]","This will take some time.. Please wait.")        
#copyanything(copy1,copy3)
os.system("cp -R "+copy1+" "+copy3+"")
xbmc.sleep(5000)
dp.create("[COLOR=white][B]COPYING[/COLOR] [COLOR=lightblue]USERDATA[/COLOR][/B]","[B][COLOR=green]FROM :"+str(appversion)+"[/B][/COLOR] - [B][COLOR=red]TO :"+str(otherapp)+"[/B][/COLOR]","This will take some time.. Please wait.")   
#copyanything(copy2,copy4)
os.system("cp -R "+copy2+" "+copy4+"")
xbmc.sleep(5000)
dp.close()


dialog.ok("[COLOR=red][B]DONE[/COLOR][/B]", "ALL DONE", "","EXIT/REBOOT")
xbmc.executebuiltin("Notification(CerebroTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
xbmc.sleep(1000)
try: os.system("su -c 'reboot'")
except: pass
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
try: os.system('TASKKILL /im SPMC.exe /f')
except: pass
try: os.system('TASKKILL /im XBMC.exe /f')
except: pass
xbmc.executebuiltin('Quit')
exit() 
