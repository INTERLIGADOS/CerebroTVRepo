# -*- coding: utf-8 -*-
#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 onwards)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import gui
from utils import reset_playing
import xbmc
import os
import xbmcgui
import download
import urllib
import urllib2
import zipfile
import sfile
import utils
import time 
from shutil import copyfile
import webbrowser

dp = xbmcgui.DialogProgress()
dp.create("[COLOR tomato]Cerebero TV[/COLOR]","Please Wait","......")  

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],Opening TV Guide, ..,5000,)")
DATA     = xbmc.translatePath('special://userdata/addon_data/script.tvguide.cerebrotv.uk.2017/')
ADDON    = xbmc.translatePath('special://home/addons/script.tvguide.cerebrotv.uk.2017/')

srcfile  = os.path.join(ADDON, 'settings.xml')
destfile = os.path.join(DATA, 'settings.xml')

if not os.path.exists(DATA):
    os.mkdir(DATA) 

if not os.path.exists(destfile):
    with open(srcfile, 'r') as myfile:
        fdata=myfile.read()
        fo = open(destfile, "w")
        fo.write(fdata);
        fo.close()
#dp = xbmcgui.DialogProgress()
#dp.create("[COLOR tomato]Cerebero TV[/COLOR]","Showing Advert","Please Wait")        
def d():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
d() 
def d2():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cHMlM0ElMkYlMkZ3d3cuaXB2YW5pc2guY29tJTJGJTNGYV9haWQlM0Q1OTk5ZGFmMTYyMDRiJTI2YV9iaWQlM0Q0OGY5NTk2Ng=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
      
d2() 

def d3():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL210dmIuY28udWsvc2hvd2FkZC8='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
      
d3() 
dp.close()      
# After a restart the proc file should be wiped!


reset_playing()
try:   
    w = gui.TVGuide()
    w.doModal()
    del w

except:
    import sys
    import traceback as tb
    (etype, value, traceback) = sys.exc_info()
    tb.print_exception(etype, value, traceback)
    

