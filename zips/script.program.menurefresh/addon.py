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

LOCATION     = "http://megatvbox.uk/uk.zip"
HOME     = xbmc.translatePath('special://home')
ROOT     = xbmc.translatePath('special://home')
file2     = os.path.join(ROOT, 'uk.zip')



def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("[COLOR tomato]Cerebro TV Menu Updater[/COLOR]","Downloading New TV Guide Data","This will take a few seconds.")
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
                        
        #xbmc.executebuiltin('RunAddon(script.tvguide.cerebrotv.uk)')
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
            #file3 = os.path.join(HOME, 'mchangelog.xml')
            #open(file3, 'w+')
            #userdata = "test|test"
            #with open(file3, 'w') as f:
                #f.write(userdata)
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
        dialog.ok("[COLOR tomato]Cerebro TV Menu Updated[/COLOR]", " ", " ","Press OK or Back to Continue")



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


dp.close()
download(LOCATION,file2) 
