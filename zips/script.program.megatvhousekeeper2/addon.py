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
IZLI     = xbmc.translatePath('special://home/addons/plugin.video.SoapCatchup/')
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
try: sfile.rmtree(IZLI)
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
try: utils.DeleteFile(MZip)
except: pass
try: utils.DeleteFile(MZip2)
except: pass
try: utils.DeleteFile(MZip3)
except: pass
try: utils.DeleteFile(MZip4)
except: pass


#TV GUIDE DATA
#try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguide/guide.xml"))
#except: pass
#try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguideusa/usatv.xml"))
#except: pass
try: utils.DeleteFile(MZip)
except: pass






