import sys
import xbmcgui
import xbmcplugin
import re
import urlresolver
import xbmc
import urllib2

def Search(name):
        search_entered = ''
        keyboard = xbmc.Keyboard(search_entered, 'Please Enter '+str(name))
        keyboard.doModal()
        if keyboard.isConfirmed():
            search_entered = keyboard.getText().replace(' ','%20')
            if search_entered == 0:
                return False          
        return search_entered
        if search_entered == None:
            return False 


moviename=Search('[B][COLOR=white]Enter Movie Name[/COLOR][/B]')
dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]CerebroTV[/COLOR]","If asked to pair please do so.","We are Searching...........")

request = urllib2.Request('http://vodlocker.to/embed?t=' + moviename + '&chromecast=0&trailer=0&referrer=link&server=alternate')


request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.882')
request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')


request.get_header('Accept')
request.get_header('User-Agent')

response = urllib2.urlopen(request).read()

getmurl = response

try:
	getit = re.compile('serverActive"><a href="(.+?)"').findall(getmurl)[0]
except:
	getit = re.compile("hostname.+?<a href='(.+?)'").findall(getmurl)[0]



if 'https://docs.google.com' in getit:
    getit = (getit).replace('https://docs.google.com','https://drive.google.com').replace('preview','view')

try:
    getit = urlresolver.HostedMediaFile(getit).resolve()
except:
    pass    
 
if getit:
    xbmc.Player().play(getit)
else:
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]TEST[/COLOR]",str(getit),"WORK??")
    xbmc.sleep(15000) 

del getit
exit()
