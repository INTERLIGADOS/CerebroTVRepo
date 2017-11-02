import time
import xbmc
import os
import xbmcgui
import urllib2

HOME     = xbmc.translatePath('special://userdata/')
iddata   = os.path.join(HOME, 'networksettings.xml')

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Exit / Reboot[/COLOR][/B]', [
    '[B][COLOR=green]Reboot Box[/COLOR][/B] (Needs Reboot.apk)',
    '[B][COLOR=green]Exit / Reboot[/COLOR][/B] (Need Admin/ADB Shell/Root/SU Access)',
    '[B][COLOR=green]Exit Kodi[/COLOR][/B] (All Devices, will take some time!!)'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
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
    if os.path.exists(iddata):
        with open(iddata, 'r') as mymega:
            userid=mymega.read()
        try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
        except: pass
    xbmc.executebuiltin('StartAndroidActivity("fr.petrus.tools.reboot")')

def function2():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    if os.path.exists(iddata):
        with open(iddata, 'r') as mymega:
            userid=mymega.read()
        try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
        except: pass
    xbmc.executebuiltin('RunAddon(script.program.tvguiderefresh3)')

def function3():
    xbmc.executebuiltin("Notification(CerebroTV,Closing SPMC/Kodi, Will take a few seconds,7000,)")
    xbmc.sleep(1000)
    if os.path.exists(iddata):
        with open(iddata, 'r') as mymega:
            userid=mymega.read()
        try: response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(userid)+'&die=1').read()
        except: pass
    xbmc.executebuiltin('RunAddon(script.program.tvguiderefresh3)')

menuoptions()