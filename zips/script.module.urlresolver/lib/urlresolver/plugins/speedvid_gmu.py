"""
speedvid urlresolver plugin
Copyright (C) 2015 tknorris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import re
from lib import helpers
from urlresolver import common
from urlresolver.resolver import ResolverError

logger = common.log_utils.Logger.get_logger(__name__)
logger.disable()

net = common.Net()

def get_media_url(url, media_id):
    headers = {'User-Agent': common.RAND_UA}
    html = net.http_GET(url, headers=headers).content
    
    if html:
        packed = re.search("""\|href\|(\d+)\|html\|location\|(\d+)\|%s\|window\|sp""" % media_id, html)
        if packed:
            location_href = "http://www.speedvid.net/sp-%s-%s-%s.html" % (media_id, packed.group(1), packed.group(2))
        
            return helpers.get_media_url(location_href, patterns=['''file:["'](?P<url>(?!http://s(?:13|57))[^"']+)''']).replace(' ', '%20')
        
    raise ResolverError('File not found')
