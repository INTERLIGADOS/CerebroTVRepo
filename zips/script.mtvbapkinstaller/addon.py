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

ipaddy="0.0.0.0"
HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')
with open(iddata, 'r') as myfile:
    data300=str(myfile.read())
response = urllib2.urlopen('http://cerebrotv.co.uk/TV-DATA/auth2.php?id='+str(data300)+'&ok=OK&ip='+ipaddy).read()
if not response == "OK":
    xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],NO CODE FOUND, ..,4000,)")
    exit()

HOME1     = '/storage/emulated/0/epsxe/bios/'
HOME11     = '/storage/emulated/0/epsxe/'
HOME3     = '/sdcard/epsxe/bios/'
HOME2     = xbmc.translatePath('special://home')
file = '/storage/emulated/0/Download/downloaded.apk'
file2 = os.path.join(HOME1, 'SCPH1001.bin')
file3 = os.path.join(HOME3, 'SCPH1001.bin')

del1     = xbmc.translatePath('/storage/emulated/0/Download/downloaded.apk')
del2     = xbmc.translatePath('/storage/emulated/0/Download/downloaded.apk')
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

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV App Installer[/COLOR]","Downloading App Installer","This make take a few seconds.")
    try:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
        
    except Exception, e:
        xbmc.executebuiltin("Notification(DOWNLOAD FAILED,Try Again,)")
        #print(e)
        #exit()
 
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
        function8,
        function9,
        function10,
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
        function22,
        function23
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] APP Installer[/COLOR][/B]', [
    '[B][COLOR=green]      Download[/COLOR] SPMC 16.7.1[/B] For Android 5+',
    '[B][COLOR=green]      Download[/COLOR] Kodi 17.6[/B] For Android 5+',
    '[B][COLOR=green]      Download[/COLOR] FTMC 16.2[/B] For Android 4.x', 
    '[B][COLOR=green]      Download[/COLOR] CerebroTV Launcher[/B] For All Android', 
    '[B][COLOR=green]      Download[/COLOR] Box Rebooter[/B] For All Android (Needs Root/SU)', 
    '[B][COLOR=green]      Download[/COLOR] MegaDrive Emulator[/B] For All Android (Retro Game Player)', 
    '[B][COLOR=green]      Download[/COLOR] M.A.M.E[/B] For All Android (Retro Game Player)', 
    '[B][COLOR=green]      Download[/COLOR] ePSXe[/B] For All Android (PlaySation 1)', 
    '[B][COLOR=green]      Download[/COLOR] Mobdro[/B] - ([I]Android [/I])', 
    '[B][COLOR=green]      Download[/COLOR] Wifi Analyzer[/B] View your wifi singal - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] KingRoot[/B] [COLOR=red] Try and root your device.[/COLOR]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] ShowBox[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] Swift Streams[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] ES File Explorer[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] TeamViewer Quick Support[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] CCleaner[/B]  - ([I]Android [/I]) (SYSTEM CLEANER)',  
    '[B][COLOR=green]      Download[/COLOR] Hola VPN[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] SENS Emulator[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] YouTube App[/B]  - ([I]Android [/I])',  
    '[B][COLOR=green]      Download[/COLOR] GooglePlay Update[/B]  - ([I]Android [/I])',
    '[B][COLOR=green]      Download[/COLOR] Connection Speed Tester[/B]  - ([I]Android [/I])',
    '[B][COLOR=green]      Download[/COLOR] M.A.M.E[/B] For All Android (Retro Game Player) (Version 2)',
    '[B][COLOR=green]      Download[/COLOR] Google Chrome Web Browser[/B] For Android 5+'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-23]
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
    DownloaderClass("http://mtvb.co.uk/apks/spmc.exe",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    xbmc.executebuiltin('quit')
    
def function2():
    DownloaderClass("http://mtvb.co.uk/apks/kodi.exe",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    xbmc.executebuiltin('quit')
    
def function3():
    DownloaderClass("http://mtvb.co.uk/apks/ftmc.exe",file)
    xbmc.executebuiltin("Notification(DOWNLOAD COMPLETE,Opening APK Installer,)")
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    xbmc.executebuiltin('quit')
    
def function4():
    DownloaderClass("http://mtvb.co.uk/apks/cerebrotv.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    
def function5():
    DownloaderClass("http://mtvb.co.uk/apks/reboot.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')

def function6():
    DownloaderClass("http://mtvb.co.uk/apks/megadrive.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')

    
def function7():
    DownloaderClass("http://mtvb.co.uk/apks/mame.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    
def function8():
    if not os.path.exists(HOME11):
        try: os.mkdir(HOME11)
        except: pass
    if not os.path.exists(HOME1):
        try: os.mkdir(HOME1)
        except: pass
    DownloaderClass("http://mtvb.co.uk/apks/SCPH1001.exe",file2)
    xbmc.sleep(1000)
    DownloaderClass("http://mtvb.co.uk/apks/PSX.exe",file)
    xbmc.sleep(1000)
    #DownloaderClass("http://mtvb.co.uk/apks/SCPH1001.exe",file3)
    #xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    
def function9():
    DownloaderClass("http://mtvb.co.uk/apks/mobdro.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    
    
def function10():
    DownloaderClass("http://mtvb.co.uk/apks/wifi.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')
    
def function11():
    DownloaderClass("http://mtvb.co.uk/apks/root.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')

def function12():
    DownloaderClass("http://mtvb.co.uk/apks/showbox.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")')  
    
def function13():
    DownloaderClass("http://mtvb.co.uk/apks/SwiftStream.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function14():
    DownloaderClass("http://mtvb.co.uk/apks/esfile.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function15():
    DownloaderClass("http://mtvb.co.uk/apks/tv.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function16():
    DownloaderClass("http://mtvb.co.uk/apks/cc.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function17():
    DownloaderClass("http://mtvb.co.uk/apks/vpn.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function18():
    DownloaderClass("http://mtvb.co.uk/apks/sens.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function19():
    DownloaderClass("http://mtvb.co.uk/apks/youtube.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function20():
    DownloaderClass("http://mtvb.co.uk/apks/googleplay.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function21():
    DownloaderClass("http://mtvb.co.uk/apks/speedtest.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function22():
    DownloaderClass("http://mtvb.co.uk/apks/MAME2.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 
    
def function23():
    DownloaderClass("http://mtvb.co.uk/apks/googlechrome.exe",file)
    xbmc.sleep(1000)
    xbmc.executebuiltin('StartAndroidActivity("com.droidlogic.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.gsoft.appinstall")')
    xbmc.executebuiltin('StartAndroidActivity("com.estrongs.android.pop")') 

myplatform = platform()
if myplatform == 'android':    
    #dialog = xbmcgui.Dialog()
    #dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "Firestick & nVida Shield devices", "Install App Manually after download","(needs es file explorer) Internal Storage / Download")
    menuoptions()
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]INFOMATION[/COLOR][/B]", "ANDROID SYSTEMS ONLY", "","")

