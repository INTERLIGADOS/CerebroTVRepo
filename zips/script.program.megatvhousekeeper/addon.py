import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import sfile
import time
import datetime




HOME2     = xbmc.translatePath('special://userdata')
file2 = os.path.join(HOME2, 'housekeeper.xml')
file3 = os.path.join(HOME2, 'lock.xml')

with open(file3, 'r') as myfile:
    lock=int(myfile.read())


    
if lock < 1:
    fo = open(file3, "w")
    fo.write(str(1));
    fo.close()



    with open(file2, 'r') as myfile:
        lastrun=int(myfile.read())
    
    #if lastrun == "":
    #   lastrun = 1

    checktime = int(time.time())+604800 #7 days
    timenow = int(time.time())

    remindtime = timenow+7200 # 1 hour

    #lastrun = int(lastrun)


    xbmc.log("Last Run "+str(lastrun))
    xbmc.log("New Time "+str(checktime))
    if lastrun < timenow:

        #FOLDERS
        ZEUS     = xbmc.translatePath('special://home/addons/repository.zeus/')
        ZEUS2    = xbmc.translatePath('special://home/addons/plugin.video.zeus/')
        EXPT     = xbmc.translatePath('special://home/addons/repository.team.expat/')
        DAFF     = xbmc.translatePath('special://home/addons/repository.daffyslist/')
        I4AT     = xbmc.translatePath('special://home/addons/plugin.video.i4atv/')
        EXPT2    = xbmc.translatePath('special://home/addons/plugin.video.expattv/')
        DAFF2    = xbmc.translatePath('special://home/addons/plugin.video.Daffyslist/')
        iVUE     = xbmc.translatePath('special://home/addons/xbmc.repo.iVueTvGuide/')
        EPHU     = xbmc.translatePath('special://home/addons/script.episodehunter/')
        IZLI     = xbmc.translatePath('special://home/addons/plugin.video.israelive')
        TEMP     = xbmc.translatePath('special://home/addons/script.mtvb/')
        TEMP2    = xbmc.translatePath('special://home/addons/script.megatvinstall/')
        TEMP3    = xbmc.translatePath('special://home/addons/script.installdone/')

        #CACHE
        CACHE    = xbmc.translatePath('special://home/cache/')
        #FILES
        MZip     = xbmc.translatePath('special://home/userdata/_mega_temp.zip')
        MZip2     = xbmc.translatePath('special://home/userdata/install.zip')
        MZip3     = xbmc.translatePath('special://home/userdata/install2.zip')
        MZip4     = xbmc.translatePath('special://home/userdata/install3.zip')
        #THUMBS
        thumbs     = xbmc.translatePath('special://home/userdata/Thumbnails/')

        try: sfile.rmtree(TEMP3)
        except: pass
        try: sfile.rmtree(ZEUS)
        except: pass
        try: sfile.rmtree(EXPT)
        except: pass
        try: sfile.rmtree(DAFF)
        except: pass
        try: sfile.rmtree(I4AT)
        except: pass
        try: sfile.rmtree(EXPT2)
        except: pass
        try: sfile.rmtree(DAFF2)
        except: pass
        try: sfile.rmtree(iVUE)
        except: pass
        try: sfile.rmtree(ZEUS2)
        except: pass
        try: sfile.rmtree(EPHU)
        except: pass
        try: sfile.rmtree(TEMP)
        except: pass
        try: sfile.rmtree(TEMP2)
        except: pass
        try: sfile.rmtree(CACHE)
        except: pass
        #FILES
        try: utils.DeleteFile(MZip)
        except: pass
        try: utils.DeleteFile(MZip2)
        except: pass
        try: utils.DeleteFile(MZip3)
        except: pass
        try: utils.DeleteFile(MZip4)
        except: pass
        update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]It has been 7 days, I need to clean your CerebroTV up[/COLOR]","[COLOR turquoise]Do you want me to clean it now and exit SPMC/Kodi" ,"OR  [COLOR turquoise]     A reminded in 2 hours.[/COLOR]")
        if update:
            fo = open(file2, "w")
            fo.write(str(checktime));
            fo.close()
            fo = open(file3, "w")
            fo.write(str(0));
            fo.close()
            try: sfile.rmtree(thumbs)
            except: pass
            try: os.mkdir(thumbs)
            except: pass
            xbmc.executebuiltin('RunAddon(script.program.exitkodi2)')
        else:
            fo = open(file2, "w")
            fo.write(str(remindtime));
            fo.close()
else: 
    exit()
        
#else:
    #fo = open(file2, "w")
    #fo.write(str(checktime));
    #fo.close()
    #dummyval=1
