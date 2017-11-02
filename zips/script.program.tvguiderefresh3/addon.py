import xbmc
import os
import xbmcgui


#file    = "special://userdata/addon_data/script.tvguidetecbox/master.xml"
file    = "master.xml"
try: os.remove(xbmc.translatePath("special://userdata/addon_data/script.mtvbtvguidesky/uksky.xml"))
except: pass

#xbmc.sleep(1000)
#xbmcgui.Dialog().ok("TV Guide Data Deleted","Will Load Fresh Freeview TV Gudie Data")
xbmc.executebuiltin('RunAddon(script.mtvbtvguidesky)')
#xbmc.executebuiltin('Dialog.Close(all, true)')



#import os
#import xbmc
#os.system("su -c 'reboot'")
#xbmc.executebuiltin("Notification(CerebroTV,Please wait Kodi is closing, DO NOT power off!,10000,)")
#xbmc.executebuiltin('RefreshRSS')
#xbmc.executebuiltin('ReloadSkin()')
#xbmc.sleep(5000)
#xbmc.executebuiltin('Quit')