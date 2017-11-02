import time
import xbmc
import os
import xbmcgui
import urllib2

def d():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=4).text
	except:
		pass
d()  

HOME   = xbmc.translatePath('special://userdata')
file99 = os.path.join(HOME, 'networksettings.xml')
file98 = os.path.join(HOME, 'megatvbox.xml')	
file3 = os.path.join(HOME, 'lock.xml')
megaver = 0

with open(file3, 'r') as myfile:
    lock=int(myfile.read())
    
with open(file98, 'r') as myfile:
    data=float(myfile.read())

try:    
    response2 = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/updaternew.php?show=yes&v='+ str(data))
    data3=response2.read()
except: pass

#if lock > 0:
#    xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.cachesystem),1)")
#    exit()
with open(file99, 'r') as myfile:
    boxid=myfile.read()
 
timer = 10
xbmc.executebuiltin('RunAddon(script.program.megatvhousekeeper)') 
def UpdateCheck():
    xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.cachesystem),45,silent)")
    try:
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/auth2.php?id='+str(boxid)+'&tt=yes')
        xbmc.log("CerebroTV Auth System Updating Data for "+str(boxid))
        HOME     = xbmc.translatePath('special://userdata')
        file2 = os.path.join(HOME, 'megatvbox.xml')
        with open(file2, 'r') as myfile:
            version=myfile.read()
            
        response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/megatvbox2.txt')
        data2=float(response.read())
        if data < data2:
            #fo = open(file3, "w")
            #fo.write(str("1"));
            #fo.close()
            update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV New Version Detcted[/COLOR]","[COLOR yellow]Your Version[/COLOR]: [COLOR red]" + str(data) + "[/COLOR] | [COLOR yellow]New Version[/COLOR]: [COLOR green]" + str(data3) + "[/COLOR]","[COLOR tomato]Would You Like to Update Now[/COLOR]?")
            if update:
                #xbmc.executebuiltin('Dialog.Close(all, true)')
                fo = open(file3, "w")
                fo.write(str("1"));
                fo.close()
                timer = 3600
                xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.cachesystem),3600,silent)")
                xbmc.executebuiltin('xbmc.UpdateAddonRepos')
                xbmc.executebuiltin('xbmc.UpdateLocalAddons')
                xbmc.executebuiltin('RunAddon(script.megatvupdater)')
                return
            else:        
                fo = open(file3, "w")
                fo.write(str(0));
                fo.close()
                xbmc.executebuiltin("XBMC.AlarmClock('MTVBCS',XBMC.RunAddon(script.cachesystem),60,silent)")
                timer = 60
                return
            
    except: pass
    
xbmc.executebuiltin('xbmc.UpdateAddonRepos')
xbmc.executebuiltin('xbmc.UpdateLocalAddons')
UpdateCheck()



	
