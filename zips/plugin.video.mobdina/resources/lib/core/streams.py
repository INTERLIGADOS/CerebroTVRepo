# -*- coding: UTF-8 -*-
#/*  ==== Author :: _beastMaster [ SweetWork Copyright (C) 2017 ] ==============
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# *  ===========================================================================
# *  
# */

import re
import random
import urlparse

from resources.lib.common import client, control

from resources.lib.common.utils import XbmcUtil

################################################################################
#  Constant Definitions
################################################################################

SUBLINK_PATTERN = r'#sublink: (.+?) #'

META_TAGS = [
    'title', 'originaltitle', 'tvshowtitle', 'year', 'season', 'episode', 
    'genre', 'rating', 'votes', 'director', 'writer', 'plot', 'tagline',
]

SDPRESETS = [
    'primewire_mv_tv', 'watchfree_mv_tv', 'movie25_mv', 'watchseries_tv', 
    'dizibox_tv',
]

HDPRESETS = [
    'primewire_mv_tv', 'watchfree_mv_tv', 'movie25_mv', 'watchseries_tv', 
    'dizibox_tv', 'dizigold_tv', 'dizilab_tv', 'miradetodo_mv', 
    'onemovies_mv_tv', 'onlinedizi_tv', 'pelispedia_mv_tv', 'pubfilm_mv_tv', 
    'putlocker_mv_tv', 'sezonlukdizi_tv', 'usmovies_mv', 'usseries_tv', 
    'watch1080_mv',
]

log = XbmcUtil.getLogger()
log_wrapper = "{_caller}/ {_msg}"

################################################################################
#  Class Definitions
################################################################################

class Resolver:

    _progress = 0

    direct = False

    def __init__(self, handle):
        self.tag = self.__class__.__name__
        self.handle = handle
        self.progress_dialog = control.progressDialog

        self._preprocessors = set([
            self._check_regex,
        ])

        self._processors = set([
            self._catch_rtmp,
            self._catch_m3u8,
            self._catch_presets,
            self._catch_builtins,
            self._catch_googleContent,
            self._catch_urlresolver,
            self._catch_liveresolver,
        ])

        self._preprocessor_wt = 30 / len(self._preprocessors)
        self._processor_wt = 70 / len(self._processors)

    def get(self, url):
        """ This is an artifact from references used in writing this add-on.
        """
        if url is None or len(url) <= 0: return
        items = re.compile('<sublink>(.+?)</sublink>').findall(url)
        if len(items) == 0: items = [url]                                       
        items = [("Link {}".format(int(items.index(i)) + 1), i) for i in items]

        if len(items) == 1:
            url = items[0][1]
        else:
            select = control.selectDialog(
                [i[0] for i in items], 
                control.infoLabel('listitem.label')
            )
            if select == -1: return
            else: url = items[select][1]

        return url

    def process(self, url):
        self.progress_dialog.create(                                            
            control.addonInfo('name'), 
            control.lang(30726).encode('utf-8')
        )
        self._updateProgress()

        for _preprocess in self._preprocessors:
            result = _preprocess(url)
            self._progress += self._preprocessor_wt
            self._updateProgress()
            if result is not None: url = result

        for _process in self._processors:
            result = _process(url)
            self._progress += self._processor_wt
            self._updateProgress()
            if result is not None:
                self._updateProgress(done=True)
                return result

        # if self.direct:
        #     self._updateProgress(done=True)
        #     return url

    def resolve(self, url):
        url = self.get(url)                                                     
        if not url or len(url) <= 0: return

        if "#sublink:" in url:
            sublinks = re.findall(SUBLINK_PATTERN, url)
            mirror_list = ["Mirror {}".format(i + 1) for i, _ in enumerate(sublinks)]
            selection = control.selectDialog(mirror_list)
            if selection is None:
                control.infoDialog(control.lang(30705).encode('utf-8'))
                return
            url = sublinks[selection]

        if "mpd://" in url:
            from resources.lib.modules import mobdro
            url = mobdro.linkifyMobdro(url, mirror_index=random.randint(0, 4))

        # log("Attempting to resolve '{}'".format(url))
        url = self.process(url)                                                 
        if url is None:
            control.infoDialog(control.lang(30705).encode('utf-8'))
            return 

        meta = {}
        for i in META_TAGS:
            try: meta[i] = control.infoLabel('listitem.%s' % i)
            except: pass
        meta = dict((k,v) for k, v in meta.iteritems() if not v == '')

        if not 'title' in meta: 
            meta['title'] = control.infoLabel('listitem.label')

        icon = control.infoLabel('listitem.icon')
        title = meta['title']

        proxyHelper = self._getProxyHelper(url)
        if proxyHelper:
            return proxyHelper.playF4mLink(url, title, None, None, "", icon)
        
        # log("Creating playable item for resolved url '{}'".format(url))
        item = control.createItem(path=url, iconImage=icon, thumbnailImage=icon)
        item.setArt({'icon': icon})
        item.setInfo(type='Video', infoLabels=meta)

        # log("Beginning stream playback ...")
        control.player.play(url, item)
        control.resolve(self.handle, True, item)

        for i in range(0, 240):
            if control.player.isPlayingVideo(): break
            control.sleep(1000)
        while control.player.isPlayingVideo():
                control.sleep(2000)
        control.sleep(5000)

    def _updateProgress(self, done=False):
        if done or self._progress >= 100:
            self._progress = 0
            self.progress_dialog.close()
        else:
            self.progress_dialog.update(
                self._progress, 
                control.lang(30726).encode('utf-8'), 
                control.lang(30731).encode('utf-8')
            )

    def _extractExt(self, url):
        try:
            tmp = url.split('?')[0].split('&')[0].split('|')[0]
            return tmp.rsplit('.')[-1].replace('/', '').lower()
        except: return

    def _getProxyHelper(self, url):
        if not '.f4m'in url or not self._extractExt(url) == 'f4m': return

        ## NOTE: This imports the old exodus scrapers (legacy code)
        from resources.lib.modules.f4mproxy.F4mProxy import f4mProxyHelper

        return f4mProxyHelper()

    def _check_regex(self, url):
        tag = ".".join([self.tag, "_check_regex"])
        if not '</regex>' in url: return

        ## NOTE: This imports the old exodus scrapers (legacy code)
        from resources.lib.modules import regex                                 
        log(log_wrapper.format(_caller=tag, _msg="executing preprocessor"))

        return regex.resolve(url)

    def _catch_rtmp(self, url):
        tag = ".".join([self.tag, "_catch_rtmp"])
        if not url.startswith('rtmp'): return

        result = None
        if len(re.compile('\s*timeout=(\d*)').findall(url)) == 0:
            result = " ".join([url, "timeout=10"])

        if result:
            self.direct = True
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result

    def _catch_m3u8(self, url):
        tag = ".".join([self.tag, "_catch_m3u8"])
        if '.m3u8' not in url or self._extractExt(url) != 'm3u8': return

        self.direct = True
        self._updateProgress(done=True)
        log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return url

    def _catch_presets(self, url):
        tag = ".".join([self.tag, "_catch_presets"])
        result = None
        try:
            preset = re.findall('<preset>(.+?)</preset>', url)[0]
            title = re.findall('<title>(.+?)</title>', url)[0]
            year = re.findall('<year>(.+?)</year>', url)[0]
            imdb = re.findall('<imdb>(.+?)</imdb>', url)[0]
        except: return

        try: 
            tvdb = re.findall('<tvdb>(.+?)</tvdb>', url)[0]
            tvshowtitle = re.findall('<tvshowtitle>(.+?)</tvshowtitle>', url)[0]
            premiered = re.findall('<premiered>(.+?)</premiered>', url)[0]
            season = re.findall('<season>(.+?)</season>', url)[0]
            episode = re.findall('<episode>(.+?)</episode>', url)[0]                
        except: 
            tvdb = tvshowtitle = premiered = season = episode = None

        presets = SDPRESETS if preset == 'searchsd' else HDPRESETS

        ## NOTE: This imports the old exodus scrapers (legacy code)
        from resources.lib.sources import sources

        tmp = sources().getSources(
            title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, 
            presetDict=presets, 
            progress=False, 
            timeout=20
        )

        result = sources().sourcesDirect(tmp, progress=False)

        if result is not None: 
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result

    def _catch_builtins(self, url):
        tag = ".".join([self.tag, "_catch_builtins"])
        ## NOTE: This imports the old exodus scrapers (legacy code)
        from resources.lib.sources import sources

        result = None
        tmp = sources().getURISource(url)

        if tmp is None or len(tmp) <= 0: return

        result = sources().sourcesDirect(tmp, progress=False)

        if result is not None: 
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result

    def _catch_googleContent(self, url):
        tag = ".".join([self.tag, "_catch_googleContent"])
        if not '.google.com' in url: return

        ## NOTE: This imports the old exodus scrapers (legacy code)
        from resources.lib.modules import directstream                          
        
        result = None
        try: result = directstream.google(url)[0]['url']
        except: return

        if result is not None: 
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result

    def _catch_urlresolver(self, url):
        tag = ".".join([self.tag, "_catch_urlresolver"])
        import urlresolver

        result = None
        try: 
            tmp = urlresolver.HostedMediaFile(
                url=url, 
                include_disabled=True, 
                include_universal=False
            )
        except: tmp = urlresolver.HostedMediaFile(url=url)

        if not tmp.valid_url(): return

        result = tmp.resolve()
        if 'plugin://plugin.video.youtube' in result: return

        if result is not None: 
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result

    def _catch_liveresolver(self, url):
        tag = ".".join([self.tag, "_catch_liveresolver"])
        import liveresolver

        result = liveresolver.resolve(url)

        if result is not None: 
            self._updateProgress(done=True)
            log(log_wrapper.format(_caller=tag, _msg="resolved stream url"))

        return result
