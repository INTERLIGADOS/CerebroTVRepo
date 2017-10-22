import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,subprocess
import urllib2
import sfile

HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')


#thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')
#try: sfile.rmtree(thumbs)
#except: pass	

dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()
	
if os.path.exists(iddata):
    with open(iddata, 'r') as mymega:
        userid=mymega.read()
    try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
    except: pass
    
xbmc.executebuiltin("Notification(CerebroTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
xbmc.sleep(1000)
try: os.system("su -c 'reboot'")
except: pass
#try: os.system('adb shell am force-stop com.semperpax.spmc16')
#except: pass
try: os.system('TASKKILL /im SPMC.exe /f')
except: pass
try: os.system('TASKKILL /im XBMC.exe /f')
except: pass
xbmc.executebuiltin('Quit')
exit()
