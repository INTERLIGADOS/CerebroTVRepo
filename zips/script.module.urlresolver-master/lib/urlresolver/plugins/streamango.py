"""
    urlresolver Kodi Addon

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

class StreamangoResolver(UrlResolver):
    name = "streamango"
    domains = ['streamango.com']
    pattern = '(?://|\.)(streamango\.com)/(?:f/|embed/)?([0-9a-zA-Z]+)'
    
    def __init__(self):
        self.net = common.Net()
    
    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.RAND_UA}
        html = self.net.http_GET(web_url, headers=headers).content
        
        if html:
            source = re.search('''srces\.push\({type:"video/mp4",src:\s*((\w+)\(.+?\))''', html)
            if source:
                packed = re.search('(eval\s*\(function.*?)</script>', html, re.DOTALL | re.I)
                if packed:
                    packed = jsunpack.unpack(packed.group(1))
                    packed = re.sub('eval\s*\(.*\)', '', packed.replace('\\', ''))
                    js = packed + ";" + source.group(1) + ";"
                    # I dont like this but we'll see how it goes
                    try: 
                        import js2py
                        _source = js2py.eval_js(js.replace("window.%s" % source.group(2), source.group(2)))
                    except Exception as e: raise ResolverError(e)
                    
                    if _source:
                        _source = "http:%s" % _source if _source.startswith("//") else _source
                        headers.update({'Referer': web_url})
                        return _source + helpers.append_headers(headers)
        
        raise ResolverError("Unable to locate video")

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, 'http://{host}/embed/{media_id}')
