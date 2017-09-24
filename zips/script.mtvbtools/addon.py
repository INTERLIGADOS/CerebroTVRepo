import time
import xbmc
import os
import xbmcgui
import urllib2
from urllib import urlopen
import re
import platform

##
#dp = xbmcgui.DialogProgress()

#print dir(platform)

#for x in dir(platform):
#    if x[0].isalnum():
#        try:
#            result = getattr(platform, x)()
#            print "platform."+x+": "+result
#            dp.create("[COLOR tomato]CerebroTV[/COLOR]","platform."+x+" ",""+result)
#            xbmc.sleep(1000)
#        except TypeError:
#            continue

HOME     = xbmc.translatePath('special://userdata/')
file2    = os.path.join(HOME, 'megatvbox.xml')
iddata   = os.path.join(HOME, 'networksettings.xml')


with open(file2, 'r') as myfile:
    data=float(myfile.read())
    
with open(iddata, 'r') as myfile:
    data300=str(myfile.read())
    
def getPublicIp():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'

    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4,
        function5,
        function6,
        function7,
        function8,
        function9,
        function10,
        function11,
        function12
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Tools Menu[/COLOR][/B]', [
    '[B][COLOR=cyan]Show Me My Wifi Signal[/COLOR][/B] - ([I]Andriod [/I])',
    '[B][COLOR=gold]Show My Info[/COLOR][/B]',
    '[B][I][COLOR=yellow]CerebroTV House Keeper[/COLOR][/B][/I] (clean up system and reboot)', 
    '[B][COLOR=green]Test My Connection Speed[/COLOR][/B]', 
    '[B][COLOR=lightblue]Re-Download the last update[/COLOR][/B]', 
    '[B][COLOR=pink]Move Build to SPMC/KODI[/COLOR][/B]', 
    '[B][COLOR=orange]Fresh Install of Build[/COLOR][/B]', 
    '[B][COLOR=lightblue]Open Main Box Settings[/COLOR][/B]', 
    '[B][COLOR=lightblue]Open Main Box Settings[/COLOR][/B]' , 
    '[B][COLOR=lightblue]Open Main Box Settings[/COLOR][/B]', 
    '[B][COLOR=green]FRESH INSTALL[/COLOR][/B]',
    '[B][COLOR=cyan]Web Browser[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-12]
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
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.farproc.wifi.analyzer")')    

def function2():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]CerebroTV[/COLOR]","Collecting Data","Few Second.....")
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B] ## MY BOX INFO ##[/COLOR][/B]", "[COLOR=red]My ID[/COLOR]: [COLOR=green]"+str(data300)+"[/COLOR]", "[COLOR=red]Build Version[/COLOR]: [COLOR=green]"+str(data)+"[/COLOR]","[COLOR=red]IP Address (public)[/COLOR]: [COLOR=green]"+str(getPublicIp())+"[/COLOR]")

def function3():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.program.megatvhousekeeper3?sf_options=desc%3DMega+TV+Box+Wait%26_options_sf",return)')

def function4():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.speedtestnet?sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cscript.speedtestnet%5Cfanart.jpg%26desc%3DARNU+Box+Speed+Tester+powered+by+speedtest.net+will+give+you+accurate+Internet+speed%2Fping+test+results.+%5Cn+Brought+to+you+by+http%3A%2F%2Fwww.arnubox.com%26_options_sf",return)')

def function5():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.megatvupdater",return)')
    
def function6():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://script.megamove",return)')
    
def function7():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('RunAddon("script.cerebrotv")')

def function8(): # ANDROID 4
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.mbx.settingsmbox")')
    xbmc.executebuiltin('StartAndroidActivity("com.android.tv.settings")')
    xbmc.executebuiltin('StartAndroidActivity("com.mbox.settings")')

def function9(): # ANDROID 6
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.mbx.settingsmbox")')
    xbmc.executebuiltin('StartAndroidActivity("com.android.tv.settings")')
    xbmc.executebuiltin('StartAndroidActivity("com.mbox.settings")')
    
def function10(): # ANDROID 5
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.mbx.settingsmbox")')
    xbmc.executebuiltin('StartAndroidActivity("com.android.tv.settings")')
    xbmc.executebuiltin('StartAndroidActivity("com.mbox.settings")')
    
def function11():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('RunAddon("script.cerebrotv")')
    
def function12():
    #the content of function 1
    #dp = xbmcgui.DialogProgress()
    #dp.create("[COLOR tomato]CerebroTV[/COLOR]","PLEASE EXIT KODI OR PULL THE POWER LEAD","PLEASE EXIT KODI OR PULL THE POWER LEAD")
    #xbmc.sleep(5000)
    xbmc.executebuiltin('StartAndroidActivity("com.android.browser")')  


menuoptions()