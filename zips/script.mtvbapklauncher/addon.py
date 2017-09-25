import time
import xbmc
import os
import xbmcgui
import urllib2
import platform
import utils
import zipfile
import sfile
import download
import urllib
import statvfs
from decimal import Decimal


HOME1     = '/storage/emulated/0/MAME4droid/roms/'
HOME2     = xbmc.translatePath('special://home/roms/')
file = os.path.join(HOME2, 'CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk')
file2 = os.path.join(HOME2, 'SCPH1001.bin')


gamefile = os.path.join(HOME2, 'psx.zip')
mamefile = os.path.join(HOME2, 'mamezip')

del1     = xbmc.translatePath('special://home/CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk')
del2     = xbmc.translatePath('special://home/downlaoded.apk')
try: sfile.rmtree(del1)
except: pass
try: sfile.rmtree(del2)
except: pass

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

    
#xbmcgui.Dialog().ok(str(disk_stat())+"% Free", str(float(free))+" MB",str(get_fs_freespace('/storage/emulated/0/') /1024/1024)+" USED","Either close using Task Manager (If unsure pull the plug).")

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Game Downloader[/COLOR]","Downloading M.A.M.E Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        
    except Exception, e:
        xbmc.executebuiltin("Notification(DOWNLOAD FAILED,Try Again,)")
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
 
def DownloaderClass2(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Game Downloader[/COLOR]","Downloading Game","This may take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(gamefile, 'r')	
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
        

        utils.DeleteFile(gamefile)	


    except Exception, e:
        noconnection()
        #print(e)
        exit()
        
        
def DownloaderClass3(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Game Downloader[/COLOR]","Downloading Game","This may take a while.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(mamefile, 'r')	
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME1)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(mamefile)	


    except Exception, e:
        noconnection()
        #print(e)
        exit()
        
def menuoptions2():
    dialog = xbmcgui.Dialog()
    funcs = (
        function11,
        function12,
        function13,
        function14,
        function15,
        function16
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Retro Games[/COLOR][/B]', ['[B][COLOR=green]Download R-Type Delta[/COLOR][/B]','[B][COLOR=gold]Download Bubble Bobble 2[/COLOR][/B]', '[B][COLOR=orange]Download Crashbandicoot 3 Warped[/COLOR][/B]', '[B][COLOR=cyan]Download M.A.M.E Roms[/COLOR][/B] (Multi Games)', '[B][COLOR=blue]Download Dragon Ball GT Final Bout[/COLOR][/B]', '[B][COLOR=orange]Download Street Fighter Zero 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-6]
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

def function11():
    DownloaderClass2("http://mtvb.co.uk/bins/rtype.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
 
def function12():
    DownloaderClass2("http://mtvb.co.uk/bins/bb.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 

def function13():
    DownloaderClass2("http://mtvb.co.uk/bins/cb.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
         

def function14():
    DownloaderClass3("http://mtvb.co.uk/bins/mame.zip",mamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch M.A.M.E" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
        
def function15():
    DownloaderClass2("http://mtvb.co.uk/bins/db.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        
def function16():
    xbmc.executebuiltin("Notification(CerebroTV,THIS GAME WILL TAKE ALONG TIME TO INSTALL, ..,27000,)")
    DownloaderClass2("http://mtvb.co.uk/bins/StreetFighterZero3.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7,
        function8
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] App Launcher[/COLOR][/B]', [
    '[B][COLOR=green]Web Browser[/COLOR][/B]',
    '[B][COLOR=gold]Mobdro[/COLOR][/B]',
    '[B][COLOR=orange]Showbox[/COLOR][/B]',
    '[B][COLOR=lightblue]Swift Streams[/COLOR][/B]',
    '[B][COLOR=lightblue]Mirror Cast[/COLOR][/B] (If installed)',
    '[B][COLOR=lightblue]Open Quick Support[/COLOR][/B] (Conact us for this)',
    '[B][COLOR=lightblue]Google Play Store[/COLOR][/B]',
    '[B][COLOR=gold]Start VPN[/COLOR][/B] (select kodi/spmc then open)'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-8]
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
    xbmc.executebuiltin('StartAndroidActivity("com.android.browser")')
       
def function2():
    xbmc.executebuiltin('StartAndroidActivity("com.mobdro.android")')

def function3():
    xbmc.executebuiltin('StartAndroidActivity("com.tdo.showbox")')
    
def function4():
    xbmc.executebuiltin('StartAndroidActivity("com.swift.stream")')
    
def function5():
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.miracast")')  

def function6():
    xbmc.executebuiltin('StartAndroidActivity("com.teamviewer.quicksupport.market")') 

def function7():
    xbmc.executebuiltin('StartAndroidActivity("com.android.vending";)')     

def function8():
    xbmc.executebuiltin('StartAndroidActivity("org.hola")')      
    
myplatform = platform()
if myplatform == 'android':    
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "Firestick & nVida Shield devices not support yet", "","")
    menuoptions()
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "ANDROID SYSTEMS ONLY", "","")



  