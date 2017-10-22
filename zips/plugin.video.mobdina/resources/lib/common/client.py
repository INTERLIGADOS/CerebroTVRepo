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

import sys
import urllib2
import urlparse
import random

from resources.lib.common import cache
from resources.lib.common.utils import parseDOM

################################################################################
#  Function Definitions
################################################################################


def randomagent():
    WIN_VERS = [ 
        'Windows NT 10.0', 'Windows NT 7.0', 'Windows NT 6.3', 
        'Windows NT 6.2', 'Windows NT 6.1', 'Windows NT 6.0', 
        'Windows NT 5.1', 'Windows NT 5.0' 
    ]
    FEATURES = [ '; WOW64', '; Win64; IA64', '; Win64; x64', '' ]
    BR_VERS = [
        [ '{}.0'.format(i) for i in xrange(18, 43) ],
        [
            '37.0.2062.103', '37.0.2062.120', '37.0.2062.124', 
            '38.0.2125.101', '38.0.2125.104', '38.0.2125.111', 
            '39.0.2171.71', '39.0.2171.95', '39.0.2171.99', 
            '40.0.2214.93', '40.0.2214.111', '40.0.2214.115', 
            '42.0.2311.90', '42.0.2311.135', '42.0.2311.152', 
            '43.0.2357.81', '43.0.2357.124', 
            '44.0.2403.155', '44.0.2403.157', 
            '45.0.2454.101', '45.0.2454.85', 
            '46.0.2490.71', '46.0.2490.80', '46.0.2490.86', 
            '47.0.2526.73', '47.0.2526.80'
        ],
        [ '11.0' ],
    ]
    RAND_UAS = [
        'Mozilla/5.0 ({win_ver}{feature}; rv:{br_ver}) Gecko/20100101 Firefox/{br_ver}',
        'Mozilla/5.0 ({win_ver}{feature}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{br_ver} Safari/537.36',
        'Mozilla/5.0 ({win_ver}{feature}; Trident/7.0; rv:{br_ver}) like Gecko'
    ]
    index = random.randrange(len(RAND_UAS))
    return RAND_UAS[index].format(
        win_ver=random.choice(WIN_VERS), 
        feature=random.choice(FEATURES), 
        br_ver=random.choice(BR_VERS[index]))


def request(url, close=True, error=False, proxy=None, post=None, headers=None, 
            mobile=False, safe=False, referer=None, cookie=None, output='', 
            timeout=30):
    try:
        handlers = []

        if proxy:
            handlers.append(
                urllib2.ProxyHandler({'http': '{}'.format(proxy)}), 
                urllib2.HTTPHandler
            )
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)

        if output == 'cookie' or output == 'extended' or not close:
            import cookielib
            cookies = cookielib.LWPCookieJar()
            handlers.append(
                urllib2.HTTPHandler(), 
                urllib2.HTTPSHandler(), 
                urllib2.HTTPCookieProcessor(cookies)
            )
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)

        try:
            if sys.version_info < (2, 7, 9): raise Exception()
            import ssl 
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            handlers.append(urllib2.HTTPSHandler(context=ssl_context))
            opener = urllib2.build_opener(*handlers)
            opener = urllib2.install_opener(opener)
        except:
            pass

        try: headers.update(headers)
        except: headers = {}

        if not 'User-Agent' in headers: 
            headers['User-Agent'] = cache.get(randomagent, 1) if not mobile \
                else 'Apple-iPhone/701.341'

        if 'Referer' in headers: pass
        else:
            headers['Referer'] = referer if referer else "{}://{}/".format(
                urlparse.urlparse(url).scheme, urlparse.urlparse(url).netloc
            )

        if not 'Accept-Language' in headers: headers['Accept-Language'] = 'en-US'

        if 'Cookie' in headers: pass
        elif cookie:
            headers['Cookie'] = cookie

        request = urllib2.Request(url, data=post, headers=headers)

        try:
            response = urllib2.urlopen(request, timeout=int(timeout))
        except urllib2.HTTPError:
            if not error: return

        if output == 'cookie':
            result = []
            for c in cookies: result.append('{}={}'.format(c.name, c.value))
            result = "; ".join(result)
        elif output == 'response':
            if safe == True:
                result = (str(response.code), response.read(224 * 1024))
            else:
                result = (str(response.code), response.read())
        elif output == 'chunk':
            try: content = int(response.headers['Content-Length'])
            except: content = (2049 * 1024)
            if content < (2048 * 1024): return
            result = response.read(16 * 1024)
        elif output == 'title':
            result = response.read(1 * 1024)
            result = parseDOM(result, 'title')[0]
        elif output == 'extended':
            cookie = []
            for c in cookies: cookie.append('%s=%s' % (c.name, c.value))
            cookie = "; ".join(cookie)
            content = response.headers
            result = response.read()
            return (result, headers, content, cookie)
        elif output == 'geturl':
            result = response.geturl()
        elif output == 'headers':
            content = response.headers
            return content
        else:
            if safe == True:
                result = response.read(224 * 1024)
            else:
                result = response.read()

        if close == True:
            response.close()

        return result
    except:
        return
