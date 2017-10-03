import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


if myplatform == 'android': # Android 
    opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://cerebrotv.co.uk/index.php/buy/' ) )
else:
    opensite = webbrowser . open('http://cerebrotv.co.uk/index.php/buy/')
