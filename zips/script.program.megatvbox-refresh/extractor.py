import zipfile
import xbmcgui
import utils
import os
import xbmc
        
def extract(packedfile, unpackpath, dname, dp = None):
    if not dname:
        dname = "CerebroTV"
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create(dname,"Adding New Files to System",'[COLOR=black].[/COLOR]', 'DO NOT TURN OFF! ')
    dp.update(0)
    zfile = zipfile.ZipFile(packedfile, 'r')	
    nItem = float(len(zfile.infolist()))
    index = 0
    for item in zfile.infolist():
        index += 1                
        percent  = int(index / nItem *100)
        filename = item.filename
        dp.update(percent)
        try:
            zfile.extract(item, unpackpath)
        except Exception, e:
            utils.log('Changelog error in extractAll')
            utils.log(e)
            
    zfile.close()
    dp.close()         
    dp.create("DOING HOUSE KEEPING",'[COLOR=black].[/COLOR]','CLEANING UP', ' ')
    xbmc.sleep(2500)
    try: os.unlink(packedfile)
    except: pass
    xbmc.sleep(2500)
    try: utils.DeleteFile(packedfile)
    except: pass
    try: os.remove(packedfile)
    except: pass
    dp.close() 