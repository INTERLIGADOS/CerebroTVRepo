# -*- coding: utf-8 -*-

'''
    bennu Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,sys,re,xbmcgui,os
import pyxbmct
pyxbmct = pyxbmct.addonwindow

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

content = params.get('content')

name = params.get('name')

title = params.get('title')

url = params.get('url')

image = params.get('image')

fanart = params.get('fanart')

source = params.get('source')

try: worker = params.get('worker')
except: worker = '0'

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0

class TextBox(pyxbmct.AddonDialogWindow):

    def __init__(self, title='Bennu'):
        super(TextBox, self).__init__(title)
        self.setGeometry(800, 600, 14, 30, 0, 3, 5)
        self.set_info_controls()
        self.set_active_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_info_controls(self):

        Background   = pyxbmct.Image(xbmc.translatePath(os.path.join('special://home/addons/plugin.video.bennu', 'art/note.png')))
        self.placeControl(Background, -2, -1, 17, 34)
        self.textbox = pyxbmct.TextBox()
        self.placeControl(self.textbox, 0, 1, 13, 28)
        self.textbox.setText(msg_text)
        self.textbox.autoScroll(1000, 800, 1000)

    def set_active_controls(self):
        self.button = pyxbmct.Button('Close')
        self.placeControl(self.button, 12,26,1,4)
        self.connect(self.button, self.close)

    def set_navigation(self):
        self.button.controlUp(self.button)
        self.button.controlDown(self.button)
        self.button.controlRight(self.button)
        self.button.controlLeft(self.button)
        self.setFocus(self.button)

    def setAnimation(self, control):
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=200',), ('WindowClose', 'effect=fade start=100 end=0 time=300',)])

if action == None:
    from resources.lib.modules import client
    from resources.lib.modules import cache
    from resources.lib.modules import control
    run = control.setting('first.info')
    if run == '': run = 'true'
    
    if run == 'true':
        global msg_text
        msg_text = cache.get(client.request, 1, 'https://pastebin.com/raw/rMSzEpaZ')
        window = TextBox('XXX-O-DUS')
        window.doModal()
        del window

    from resources.lib.indexers import bennustreams
    bennustreams.indexer().root()
    
elif action == 'directory':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import bennustreams
    if worker == '1': bennustreams.indexer().getx(url, worker=True)
    else: bennustreams.indexer().getx(url)

elif action == 'imdb_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getimdb(url)

elif action == 'trakt_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().gettrakt(url)
    
elif action == 'rotten_list':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().getrotten(url)
    
elif action == 'developer':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().developer()

elif action == 'private':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().private()

elif action == 'parental':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().parental_controls()

elif action == 'tvtuner':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import bennustreams
    bennustreams.player().play(url, content)
    
elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)
    
elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'browser':
    from resources.lib.indexers import bennustreams
    bennustreams.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().search(url=None)

elif action == 'addSearch':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().delSearch()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader_bennu
    downloader_bennu.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, windowedtrailer=windowedtrailer)

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheMeta':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheMeta()
  
elif action == 'clearCacheProviders':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheProviders()

elif action == 'clearCacheAll':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheAll()
    
elif action == 'radios':
    from resources.lib.indexers import phradios
    phradios.radios()

elif action == 'radioResolve':
    from resources.lib.indexers import phradios
    phradios.radioResolve(url)

elif action == 'radio1fm':
    from resources.lib.indexers import phradios
    phradios.radio1fm()

elif action == 'radio181fm':
    from resources.lib.indexers import phradios
    phradios.radio181fm()

elif action == 'radiocast':
    from resources.lib.indexers import phradios
    phradios.kickinradio()

elif action == 'kickinradiocats':
    from resources.lib.indexers import phradios
    phradios.kickinradiocats(url)


else:
    if 'search' in action:
        url = action.split('search=')[1]
        url = url + '|SECTION|'
        from resources.lib.indexers import bennustreams
        bennustreams.indexer().search(url)
    else: quit()