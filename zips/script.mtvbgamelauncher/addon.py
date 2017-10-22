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

ipaddy="0.0.0.0"
HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')
with open(iddata, 'r') as myfile:
    data300=str(myfile.read())
response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(data300)+'&ok=OK&ip='+ipaddy).read()
if not response == "OK":
    xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],NO CODE FOUND, ..,4000,)")
    exit()



HOME1     = '/storage/emulated/0/ROMs/MAME4droid/roms/'
HOME2     = '/storage/emulated/0/Download/'
HOME3     = '/storage/emulated/0/#MEGADRIVE/'
HOME4     = '/storage/emulated/0/'
file = os.path.join(HOME2, 'CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk')
file2 = os.path.join(HOME2, 'SCPH1001.bin')

if not os.path.exists(HOME3):
    try: os.mkdir(HOME3)
    except: pass
    
if not os.path.exists(HOME1):
    try: os.mkdir(HOME1)
    except: pass

mamefile = os.path.join(HOME1, 'mame.zip')
gamefile = os.path.join(HOME2, 'psx.zip')
megafile = os.path.join(HOME3, 'mega.zip')
snesfile = os.path.join(HOME4, 'snes.zip')



del1     = xbmc.translatePath('/storage/emulated/0/Download/CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk')
del2     = xbmc.translatePath('/storage/emulated/0/Download/downlaoded.apk')
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
        #noconnection()
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
        #noconnection()
        #print(e)
        exit()
        
def DownloaderClass4(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Game Downloader[/COLOR]","Downloading MegaDrive Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(megafile, 'r')	
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
        

        utils.DeleteFile(megafile)	


    except Exception, e:
        #noconnection()
        #print(e)
        exit()
        
def DownloaderClass5(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV Game Downloader[/COLOR]","Downloading SENS Roms","This may take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        dp.create("[COLOR tomato]CerebroTV Game Installer[/COLOR]","Adding Game files to system","Please Wait.")

        zfile = zipfile.ZipFile(snesfile, 'r')	
        nItem = float(len(zfile.infolist()))
        index = 0
        for item in zfile.infolist():
            index += 1
        
            percent  = int(index / nItem *100)
            filename = item.filename
            dp.update(percent)
            try:
                zfile.extract(item, HOME4)
            except Exception, e:
                utils.log('Changelog error in extractAll')
                utils.log(e)
        

        utils.DeleteFile(snesfile)	


    except Exception, e:
        #noconnection()
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
        function16,
        function17,
        function18,
        function19,
        function20,
        function21,
        function22
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Retro Games[/COLOR][/B]', 
    ['[B][COLOR=green]Download R-Type Delta (PSX)[/COLOR][/B]'
    ,'[B][COLOR=gold]Download Bubble Bobble 2 (PSX)[/COLOR][/B]'
    , '[B][COLOR=orange]Download Crashbandicoot 3 Warped (PSX)[/COLOR][/B]'
    , '[B][COLOR=white]Download MegaDrive (Genesis) Roms[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=cyan]Download M.A.M.E Roms Part 1[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=lightblue]Download M.A.M.E Roms Part 2[/COLOR][/B] (Multi Games)'
    , '[B][COLOR=blue]Download Dragon Ball GT Final Bout (PSX)[/COLOR][/B]'
    , '[B][COLOR=orange]Download Street Fighter Zero 3 (PSX)[/COLOR][/B]'
    , '[B][COLOR=lightblue]Download R-Type 1 & 2 (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Download SNES Games (Multi Games)[/COLOR][/B]'
    , '[B][COLOR=gold]Azure Dreams (PSX)[/COLOR][/B]'
    , '[B][COLOR=gold]Harvest Moon Back to Nature (PSX)[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-12]
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
    if not os.path.exists(HOME3):
        try: os.mkdir(HOME3)
        except: pass
    DownloaderClass4("http://mtvb.co.uk/bins/MEGADRIVE.zip",megafile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch Gensoid" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.androidemu.gens")')

def function15():
    if not os.path.exists(HOME1):
        try: os.mkdir(HOME1)
        except: pass
    DownloaderClass3("http://mtvb.co.uk/bins/mame.zip",mamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch M.A.M.E" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
        
def function16():
    if not os.path.exists(HOME1):
        try: os.mkdir(HOME1)
        except: pass
    DownloaderClass3("http://mtvb.co.uk/bins/mame2.zip",mamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch M.A.M.E" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
        
def function17():
    DownloaderClass2("http://mtvb.co.uk/bins/db.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        
def function18():
    xbmc.executebuiltin("Notification(CerebroTV,THIS GAME WILL TAKE ALONG TIME TO INSTALL, ..,27000,)")
    DownloaderClass2("http://mtvb.co.uk/bins/StreetFighterZero3.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        
def function19():
    DownloaderClass2("http://mtvb.co.uk/bins/rtypes.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        
def function20():
    DownloaderClass5("http://mtvb.co.uk/bins/snes.zip",snesfile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch SENS Emulator" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.explusalpha.Snes9xPlus")') 
        
def function21():
    DownloaderClass2("http://mtvb.co.uk/bins/azuredreams.zip",gamefile)
    openapp = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV[/COLOR]","[COLOR yellow][/COLOR]","Launch ePSXe" ,"","No","Yes")
    if openapp:
        xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")') 
        
def function22():
    DownloaderClass2("http://mtvb.co.uk/bins/HarvestMoonBacktoNature.zip.zip",gamefile)
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
        function5
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Retro Games[/COLOR][/B]', ['[B][COLOR=green]Download Games[/COLOR][/B]','[B][COLOR=gold]Play Playsation 1 Games[/COLOR][/B] ([I]ePSXe[/I]) - ([I]Andriod [/I])', '[B][COLOR=orange]M.A.M.E[/COLOR][/B] ([I]Multi Arcade Machine Emulator[/I]) - ([I]Andriod [/I])', '[B][COLOR=cyan]MegaDrive Emulator[/COLOR][/B] ([I]Genesis[/I]) - ([I]Andriod [/I])', '[B][COLOR=gold]SNES Emulator[/COLOR][/B] ([I]Super Nintendo[/I]) - ([I]Andriod [/I])'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
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
    menuoptions2()
       
def function2():
    xbmc.executebuiltin('StartAndroidActivity("com.epsxe.ePSXe")')

def function3():
    xbmc.executebuiltin('StartAndroidActivity("com.seleuco.mame4droid")')
    
def function4():
    xbmc.executebuiltin('StartAndroidActivity("com.androidemu.gens")')
    
def function5():
    xbmc.executebuiltin('StartAndroidActivity("com.explusalpha.Snes9xPlus")')
    
myplatform = platform()
if myplatform == 'android':    
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "Firestick & nVida Shield devices not support yet", "","")
    menuoptions()
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "ANDROID SYSTEMS ONLY", "","")



  