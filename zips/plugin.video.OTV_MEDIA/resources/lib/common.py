import xbmcaddon
from xbmc import translatePath
import urllib2, urllib, sys

addonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(id = addonID)
addonName = addon.getAddonInfo('name')
addonPath = translatePath(addon.getAddonInfo('path')).decode('utf-8')

profilePath = translatePath(addon.getAddonInfo('profile')).decode('utf-8')
addon_id = addon.getAddonInfo('id')

IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'

UA_LIST = [IE_USER_AGENT, FF_USER_AGENT, OPERA_USER_AGENT, IOS_USER_AGENT, ANDROID_USER_AGENT]