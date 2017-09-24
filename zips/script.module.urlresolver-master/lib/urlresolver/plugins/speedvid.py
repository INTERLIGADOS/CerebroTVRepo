"""
    OVERALL CREDIT TO:
        t0mm0, Eldorado, VOINAGE, BSTRDMKR, tknorris, smokdpi, TheHighway

    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0

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
"""
import re
from lib import helpers, jsunpack
from urlresolver import common
from urlresolver.resolver import UrlResolver, ResolverError

class SpeedVidResolver(UrlResolver):
    name = "SpeedVid"
    domains = ['speedvid.net']
    pattern = '(?://|\.)(speedvid\.net)/(?:embed-|p-)?([0-9a-zA-Z]+)'
    
    def __init__(self):
        self.net = common.Net()
    
    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.RAND_UA}
        html = self.net.http_GET(web_url, headers=headers).content
        
        if html:
            try:
                packed = helpers.get_packed_data(html)
                i = 0 # just incase of infinite loop
                while jsunpack.detect(packed) and i < 5:
                    i += 1
                    try: packed = jsunpack.unpack(packed)
                    except: break
                    
                location_href = re.search("""(?:window|document)\.location\.href\s*=\s*["']([^"']+)""", packed, re.I).groups()[0]
                location_href = 'http:%s' % location_href if location_href.startswith("//") else location_href
                
                return helpers.get_media_url(location_href, patterns=['''file:["'](?P<url>(?!http://s(?:13|57))[^"']+)''']).replace(' ', '%20')
                
            except Exception as e:
                raise ResolverError(e)
            
        raise ResolverError('File not found')
        
    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, 'http://www.{host}/embed-{media_id}.html')

