import utils
import xbmc
import os
import xbmcgui
import zipfile
import sfile
import download
import urllib

HOME     = xbmc.translatePath('special://home')
LOCATION     = "http://cerebrotv.co.uk/TV-DATA/update.zip"
ROOT     = xbmc.translatePath('special://home')
file     = os.path.join(HOME, '_mega_temp.zip')
GETTEXT  = utils.GETTEXT


def dlProgress(count, blockSize, totalSize):
      percent = int(count*blockSize*100/totalSize)
      dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = "test")
      dp.update(percent)
      #progressBar = xbmcgui.DialogProgress()
      #progressBar.update(percent)
      #sys.stdout.write("\r" + LOCATION + "...%d%%" % percent)
      #sys.stdout.flush()
      #return percent


def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("CerebroTV","Downloading File","This make take a while.")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
    #HOME     = xbmc.translatePath('special://home')
    #location = LOCATION.replace(' ', '%20')
    #file     = os.path.join(HOME, '_mega_temp.zip')
    dp.create("CerebroTV Updater","Extracting New Update","Please Wait.")
    if os.path.exists(file):
        zfile = zipfile.ZipFile(file, 'r')	
        nItem = float(len(zfile.infolist()))
        #xbmcgui.Dialog().ok("CerebroTV","","",str(nItem))
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
    utils.DeleteFile(file)
    dp.create("CerebroTV","Update Complete","Closing.")
    os.system("su -c 'reboot'")
    xbmc.executebuiltin('Quit')
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
 

DownloaderClass(LOCATION,file)


