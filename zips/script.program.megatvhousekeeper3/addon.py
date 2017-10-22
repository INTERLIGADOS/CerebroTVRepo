import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import sfile

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
IZLI     = xbmc.translatePath('special://home/addons/plugin.video.israelive/')
TEMP     = xbmc.translatePath('special://home/addons/script.mtvb/')
TEMP2    = xbmc.translatePath('special://home/addons/script.megatvinstall/')
TEMP3    = xbmc.translatePath('special://home/addons/script.installdone/')
TEMP4    = xbmc.translatePath('special://home/userdata/addon_data/script.extendedinfo/TheMovieDB/')
TEMP5    = xbmc.translatePath('special://home/addons/plugin.video.neotv')
TEMP6    = xbmc.translatePath('special://home/addons/plugin.video.goldencowboys')
TEMP7    = xbmc.translatePath('special://home/addons/plugin.video.theiptvcowboys')



#CACHE
CACHE    = xbmc.translatePath('special://home/cache/')
#FILES
MZip     = xbmc.translatePath('special://home/_mega_temp.zip')
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
try: sfile.rmtree(TEMP3)
except: pass
try: sfile.rmtree(TEMP4)
except: pass
try: sfile.rmtree(TEMP5)
except: pass
try: sfile.rmtree(TEMP6)
except: pass
try: sfile.rmtree(TEMP7)
except: pass
try: sfile.rmtree(CACHE)
except: pass
try: sfile.rmtree(thumbs)
except: pass


#TV GUIDE DATA
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguide/uktvguide.xml"))
except: pass
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguideusa/usatvguide.xml"))
except: pass
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguidefv/uktvguidefv.xml"))
except: pass
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguidekids/kidstvguide.xml"))
except: pass
try: os.remove(MZip)
except: pass
try: os.remove(MZip2)
except: pass
try: os.remove(MZip3)
except: pass
try: os.remove(MZip4)
except: pass
try: os.remove(xbmc.translatePath("special://home/CLICK-ME-TO-INSTALL-WHAT-YOU-JUST-DOWNLOADED.apk"))
except: pass
try: os.remove(xbmc.translatePath("special://home/downlaoded.apk"))
except: pass
try: os.remove(xbmc.translatePath("special://home/skin.zip"))
except: pass
try: os.remove(xbmc.translatePath("special://home/uk.zip"))
except: pass
try: os.remove('/storage/emulated/0/Download/downloaded.apk')
except: pass

update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
if update:
    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
else:
    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')






