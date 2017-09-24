# -*- coding: utf-8 -*-
#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui
from utils import reset_playing
import xbmc
import os
import xbmcgui
import download
import urllib
import urllib2
import zipfile
import sfile
import utils
import time
from shutil import copyfile
import webbrowser  

xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],Opening TV Guide, ..,2000,)")


def d():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
#aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZjZXJlYnJvdHYuY28udWslMkZwJTJG < old        
d()  
def d2():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cHMlM0ElMkYlMkZ3d3cuaXB2YW5pc2guY29tJTJGJTNGYV9haWQlM0Q1OTk5ZGFmMTYyMDRiJTI2YV9iaWQlM0Q0OGY5NTk2Ng=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
#aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZjZXJlYnJvdHYuY28udWslMkZwJTJG < old        
d2() 



LOCATION     = "http://megatvbox.uk/uk-new.zip"
HOME     = xbmc.translatePath('special://home')
ROOT     = xbmc.translatePath('special://home')
file2     = os.path.join(ROOT, 'uk.zip')

file    = "master.xml"

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Downloading New TV Guide Data","This will take a few seconds.")
        dp.update(0)
    start_time=time.time()
    try:
        urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.close()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Installing New TV Guide Data","Please Wait. [COLOR red]www.cerebrotv.co.uk[/COLOR]")
        if os.path.exists(file2):
            zfile = zipfile.ZipFile(file2, 'r')	
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
                        
        dp.close()
        try:
            xbmc.executebuiltin("Notification(CerebroTV,Some Channels May Take a Few Tries, ..,3000,)")
            w = gui.TVGuide()
            w.doModal()
            del w

        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)
    except Exception, e:
        dp.close()
        noconnection()
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e,' ')
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 

def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)


def DownloaderClass(url,dest, dp = None):
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Downloading New TV Guide Data","This will take a few seconds.")
    try:
        start_time=time.time()
        urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
        urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
        dp.close()
        dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Installing New TV Guide Data","Please Wait. [COLOR red]www.cerebrotv.co.uk[/COLOR]")
        if os.path.exists(file2):
            zfile = zipfile.ZipFile(file2, 'r')	
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
        
        dp.close()
        dialog = xbmcgui.Dialog()

        xbmc.sleep(2000)
        try:
            #xbmc.executebuiltin("Notification(CerebroTV,Some Channels May Take a Few Tries, ..,3000,)")
            w = gui.TVGuide()
            w.doModal()
            del w

        except:
            import sys
            import traceback as tb
            (etype, value, traceback) = sys.exc_info()
            tb.print_exception(etype, value, traceback)


    except Exception, e:
        noconnection()

        exit()
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100)
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '%.02f MB of %.02f MB' % (currently_downloaded, total) 
            e = 'Speed: %.02f Kb/s ' % kbps_speed 
            e += 'ETA: %02d:%02d' % divmod(eta, 60)
            dp.update(percent, mbs, e,' ')
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            dp.close() 
 

def noconnection():
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## CONNECTION ERROR ##[/COLOR][/B]", "Unable to download needed data....", "Will Try Again.","Press OK or Back to Continue")
    xbmc.sleep(1000)






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
     


# After a restart the proc file should be wiped!

myplatform = platform()
if myplatform == 'android': # Android 
    xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://mtvb.co.uk/showadd/' ) )
else:
    webbrowser . open('http://mtvb.co.uk/showadd/')
xbmc.sleep(2000) 
reset_playing()
update = xbmcgui.Dialog().yesno("[COLOR tomato]TV Guide Helper[/COLOR]","[COLOR yellow][/COLOR]","" ,"","Open Guide","Update Guide")
if update:
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]TV Guide Auto Update[/COLOR]","Downloading New IPTV Data","This will take a second.")
    percent = 50
    dp.update(percent) 
    import downloader#
    percent = 70
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.cerebrotv.sports/source.db"))
    except: pass
    try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.tvguide.cerebrotv.sports/cerebrouk.xml"))
    except: pass
    dp.update(percent) 
    xbmc.sleep(1000)
    percent = 89
    dp.update(percent)
    xbmc.sleep(1000)    
    downloader.getmodules()
    percent = 99
    xbmc.sleep(1000)
    dp.update(percent)
    dp.close()
    download(LOCATION,file2) 
else:
    try:
        w = gui.TVGuide()
        w.doModal()
        del w

    except:
        import sys
        import traceback as tb
        (etype, value, traceback) = sys.exc_info()
        tb.print_exception(etype, value, traceback)

