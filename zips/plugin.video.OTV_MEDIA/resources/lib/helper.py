import sys, os, xbmc, xbmcgui, xbmcaddon, xbmcplugin, gzip, sqlite3, urllib, urllib2, re, json, traceback
from datetime import datetime, timedelta
from assets import Assets
from playlist import *
from ga import ga
from resources.lib.gui.gui import cGui
def update(name, location, crash=None):
  p = {}
  p['an'] = addon.getAddonInfo('name')
  p['av'] = addon.getAddonInfo('version')
  p['ec'] = 'Addon actions'
  p['ea'] = name
  p['ev'] = '1'
  p['ul'] = xbmc.getLanguage()
  p['cd'] = location
  ga('UA-79422131-7').update(p, crash)
    
def show_categories():
  update('browse', 'Categories')
  oGui = cGui()
  cats = []
  try:
    conn = sqlite3.connect(db)
    cursor = conn.execute('''SELECT * FROM categories''')
    
    li = xbmcgui.ListItem('Всички')
    url = "%s?id=0&mode=show_channels" % sys.argv[0]
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, True)

    #Add categories
    for row in cursor:
      li = xbmcgui.ListItem(row[1])
      url = "%s?id=%s&mode=show_channels" % (sys.argv[0], row[0])
      xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, li, True)
      
  except Exception, er:
    xbmc.log(str(er), xbmc.LOGERROR)
  return cats
  oGui.setEndOfDirectory()
def show_channels(id):
  channels = get_channels(id)
  for c in channels:      
    if c.disabled:
      c.name = '[COLOR brown]%s[/COLOR]' % c.name
    playable = c.streams == 1 and c.playpath != ''
    li = xbmcgui.ListItem(c.name, iconImage = c.logo, thumbnailImage = c.logo)
    li.setInfo( type = "Video", infoLabels = { "Title" : c.name } )
    li.setProperty("IsPlayable", str(playable))
    #     self.playable = False if self.streams > 1 or self.player_url != '' else True

    if playable:
      u = c.playpath
    else:
      u = "%s?id=%s&mode=show_streams" % (sys.argv[0], c.id)
    
    xbmcplugin.addDirectoryItem(int(sys.argv[1]), u, li, False) 

def get_channels(id):
  xbmc.log("id: " + id)
  channels = []
  try:
    conn = sqlite3.connect(db)
    sign = "="
    no_radio_rule = ""
    if id == str(0):
      sign = '<>' 
      no_radio_rule = "AND c.category_id <> 7"
      
    q = '''
    SELECT c.id, c.disabled, c.name, cat.name AS category, c.logo, COUNT(s.id) AS streams, s.stream_url, s.page_url, s.player_url, c.epg_id, u.string, c.ordering
    FROM channels AS c 
    JOIN streams AS s ON c.id = s.channel_id 
    JOIN categories as cat ON c.category_id = cat.id
    JOIN user_agents as u ON u.id = s.user_agent_id
    WHERE c.category_id %s %s %s %s
    GROUP BY c.id, c.name 
    ORDER BY c.ordering''' % (sign, id, no_radio_rule, disabled_query)
    cursor = conn.execute(q)
    #xbmc.log(q)
    
    for row in cursor:
      c = Channel(row)
      channels.append(c)
  except Exception, er:
    xbmc.log('get_channels() '  + str(sys.exc_info()[0]) + ': ' + str(sys.exc_info()[1]) + ''.join(traceback.format_stack()), xbmc.LOGERROR)
  return channels

def show_streams(id):
  streams = get_streams(id)
  select = 0
  if len(streams) > 1:
    dialog = xbmcgui.Dialog()
    select = dialog.select('Изберете стрийм', [s.comment for s in streams])
    if select == -1: 
      return False
  url = streams[select].url
  xbmc.log('FreeBGTvs resolved url %s' % url)
  item = xbmcgui.ListItem(path=url)
  item.setInfo( type = "Video", infoLabels = { "Title" : ''} )
  item.setProperty("IsPlayable", str(True))
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), succeeded=True, listitem=item)
  
def get_streams(id):
  streams = []
  try:
    conn = sqlite3.connect(db)
    cursor = conn.execute('''SELECT s.*, u.string AS user_agent FROM streams AS s JOIN user_agents as u ON s.user_agent_id == u.id WHERE channel_id = %s %s''' %  (id, disabled_query))
    for row in cursor:
      c = Stream(row, xbmc.log)
      
      streams.append(c)
  except Exception, er:
    xbmc.log(str(er), xbmc.LOGERROR)
  return streams  

def play_channel(channel_id, stream_index = 0):
  urls = get_streams(id)
  s = urls[stream_index]
  li = xbmcgui.ListItem(s.name, iconImage = s.logo, thumbnailImage = s.logo, path=s.stream_url)
  li.setInfo( type = "Video", infoLabels = { "Title" : s.name } )
  li.setProperty("IsPlayable", 'True')
  xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=li)
  
  
def get_params():
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace('?','')
    if (params[len(params)-1] == '/'):
      params = params[0:len(params) - 2]
    pairsofparams = cleanedparams.split('&')
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split('=')
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
  return param

clist = []
categories = []

addon = xbmcaddon.Addon(id = 'plugin.video.OTV_MEDIA')
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
profile_dir = xbmc.translatePath(addon.getAddonInfo('profile'))

show_disabled =  True if addon.getSetting('show_disabled') == "true" else False
disabled_query = '''AND s.disabled = 0''' if show_disabled == False else ''
cwd = xbmc.translatePath( addon.getAddonInfo('path') ).decode('utf-8')
local_db = xbmc.translatePath(os.path.join( cwd, 'resources', 'tv.db' ))
#url = 'http://offshoregit.com/harrygg/assets/tv.db.gz'
url = 'http://github.com/harrygg/plugin.program.freebgtvs/raw/master/resources/tv.db'
a = Assets(profile_dir, url, local_db, xbmc.log)
db = a.file
try:
  db = os.environ['BGTVS_DB']
except Exception:
  pass