# -*- coding: utf-8 -*-
import xbmcaddon,xbmc
from xbmc import translatePath


import urllib2, urllib, sys
addonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(id = addonID)
addonPath = translatePath(addon.getAddonInfo('path')).decode('utf-8')
def enum(**enums):
    return type('Enum', (), enums)
class strwithmeta(str):
    def __new__(cls,value,meta={}):
        obj = str.__new__(cls, value)
        obj.meta = {}
        if isinstance(value, strwithmeta):
            obj.meta = value.meta
        else:
            obj.meta = {}
        obj.meta.update(meta)
        return obj
###################################################
# FOREIGN import
###################################################
import urllib
import urllib2
try: import ssl
except Exception: pass
import os
import re
import string
import time
import htmlentitydefs
import cookielib
import unicodedata
import urllib2,urllib,cgi, re
import HTMLParser

import json
import traceback
import os
import cookielib
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
import datetime
import time
import sys


fileExists=''
addon_id = addon.getAddonInfo('id')
communityStreamPath = os.path.join(addonPath,'resources')
communityStreamPath =os.path.join(communityStreamPath,'community')
profile_path =  xbmc.translatePath(addon.getAddonInfo('profile'))
try:    import json
except Exception: import simplejson as json
try:
    try: from cStringIO import StringIO
    except Exception: from StringIO import StringIO 
    import gzip
except Exception: pass

###################################################
def byteify(input):
    if isinstance(input, dict):
        return dict([(byteify(key), byteify(value)) for key, value in input.iteritems()])
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
def GetCookieDir(cookieJar=None):
	try:
		
		COOKIEFILE = communityStreamPath+'/Cookie.lwp'
		try:
			cookieJar = cookielib.LWPCookieJar()
			cookieJar.load(COOKIEFILE)
		except:
			traceback.print_exc(file=sys.stdout)	
			cookieJar=None
		loginPerformed=False
		if login or not cookieJar==None:
			cookieJar=performLogin()
			loginPerformed=True
		if cookieJar:
			cookieJar.save (COOKIEFILE)
		print 'saved'
		return cookieJar,loginPerformed
	except:
		traceback.print_exc(file=sys.stdout)
		return None, False
	

	return cookieJar;
class NoRedirection(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl
    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302

class MultipartPostHandler(urllib2.BaseHandler):
    handler_order = urllib2.HTTPHandler.handler_order - 10

    def http_request(self, request):
        data = request.get_data()
        if data is not None and type(data) != str:
            content_type, data = self.encode_multipart_formdata( data )
            request.add_unredirected_header('Content-Type', content_type)
            request.add_data(data)
        return request
        
    def encode_multipart_formdata(self, fields):
        LIMIT = '-----------------------------14312495924498'
        CRLF = '\r\n'
        L = []
        for (key, value) in fields:
            L.append('--' + LIMIT)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        L.append('--' + LIMIT + '--')
        L.append('')
        body = CRLF.join(L)
        content_type = 'multipart/form-data; boundary=%s' % LIMIT
        return content_type, body
    
    https_request = http_request

class CParsingHelper:
    @staticmethod
    def getSearchGroups(data, pattern, grupsNum=1, ignoreCase=False):
        tab = []
        if ignoreCase:
            match = re.search(pattern, data, re.IGNORECASE)
        else:
            match = re.search(pattern, data)
        
        for idx in range(grupsNum):
            try:    value = match.group(idx + 1)
            except Exception: value = ''
            tab.append(value)
        return tab
        
    @staticmethod
    def getDataBeetwenReMarkers(data, pattern1, pattern2, withMarkers=True):
        match1 = pattern1.search(data)
        if None == match1 or -1 == match1.start(0): return False, ''
        match2 = pattern2.search(data[match1.end(0):])
        if None == match2 or -1 == match2.start(0): return False, ''
        
        if withMarkers:
            return True, data[match1.start(0): (match1.end(0) + match2.end(0)) ]
        else:
            return True, data[match1.end(0): (match1.end(0) + match2.start(0)) ]

        
    @staticmethod
    def getDataBeetwenMarkers(data, marker1, marker2, withMarkers=True, caseSensitive=True):
        if caseSensitive:
            idx1 = data.find(marker1)
        else:
            idx1 = data.lower().find(marker1.lower())
        if -1 == idx1: return False, ''
        if caseSensitive:
            idx2 = data.find(marker2, idx1 + len(marker1))
        else:
            idx2 = data.lower().find(marker2.lower(), idx1 + len(marker1))
        if -1 == idx2: return False, ''
        
        if withMarkers:
            idx2 = idx2 + len(marker2)
        else:
            idx1 = idx1 + len(marker1)

        return True, data[idx1:idx2]
        
    @staticmethod
    def getAllItemsBeetwenMarkers(data, marker1, marker2, withMarkers=True, caseSensitive=True):
        itemsTab = []
        if caseSensitive:
            sData = data
        else:
            sData = data.lower()
            marker1 = marker1.lower()
            marker2 = marker2.lower()
        idx1 = 0
        while True:
            idx1 = sData.find(marker1, idx1)
            if -1 == idx1: return itemsTab
            idx2 = sData.find(marker2, idx1 + len(marker1))
            if -1 == idx2: return itemsTab
            tmpIdx2 = idx2 + len(marker2) 
            if withMarkers:
                idx2 = tmpIdx2
            else:
                idx1 = idx1 + len(marker1)
            itemsTab.append(data[idx1:idx2])
            idx1 = tmpIdx2
        return itemsTab
        
    @staticmethod
    def rgetAllItemsBeetwenMarkers(data, marker1, marker2, withMarkers=True, caseSensitive=True):
        itemsTab = []
        if caseSensitive:
            sData = data
        else:
            sData = data.lower()
            marker1 = marker1.lower()
            marker2 = marker2.lower()
        idx1 = len(data)
        while True:
            idx1 = sData.rfind(marker1, 0, idx1)
            if -1 == idx1: return itemsTab
            idx2 = sData.rfind(marker2, 0, idx1)
            if -1 == idx2: return itemsTab
            
            if withMarkers:
                itemsTab.insert(0, data[idx2:idx1+len(marker1)])
            else:
                itemsTab.insert(0, data[idx2+len(marker2):idx1])
            idx1 = idx2
        return itemsTab
        
    @staticmethod
    def rgetDataBeetwenMarkers2(data, marker1, marker2, withMarkers=True, caseSensitive=True):
        if caseSensitive:
            sData = data
        else:
            sData = data.lower()
            marker1 = marker1.lower()
            marker2 = marker2.lower()
        idx1 = len(data)
        
        idx1 = sData.rfind(marker1, 0, idx1)
        if -1 == idx1: return False, ''
        idx2 = sData.rfind(marker2, 0, idx1)
        if -1 == idx2: return False, ''
        
        if withMarkers:
            return True, data[idx2:idx1+len(marker1)]
        else:
            return True, data[idx2+len(marker2):idx1]
        
    @staticmethod
    def rgetDataBeetwenMarkers(data, marker1, marker2, withMarkers = True):
        # this methods is not working as expected, but is is used in many places
        # so I will leave at it is, please use rgetDataBeetwenMarkers2
        idx1 = data.rfind(marker1)
        if -1 == idx1: return False, ''
        idx2 = data.rfind(marker2, idx1 + len(marker1))
        if -1 == idx2: return False, ''
        
        if withMarkers:
            idx2 = idx2 + len(marker2)
        else:
            idx1 = idx1 + len(marker1)
        return True, data[idx1:idx2]
    
    @staticmethod
    def getAllItemsBeetwenNodes(data, node1, node2, withNodes=True):
        if len(node1) < 2 or len(node2) < 2:
            return []
        itemsTab = []
        n1S = node1[0]
        n1E = node1[1]
        if len(node1) > 2: n1P = node1[2]
        else: n1P = None
        n2S = node2[0]
        n2E = node2[1]
        if len(node2) > 2: n2P = node2[2]
        else: n2P = None
        lastIdx = 0
        search = 1
        sData = data
        while True:
            if search == 1:
                # node 1 - start
                idx1 = sData.find(n1S, lastIdx)
                if -1 == idx1: return itemsTab
                lastIdx = idx1 + len(n1S)
                idx2 = sData.find(n1E, lastIdx)
                if -1 == idx2: return itemsTab
                lastIdx = idx2 + len(n1E)
                if n1P != None and sData.find(n1P, idx1 + len(n1S), idx2) == -1:
                    continue
                search = 2
            else:
                # node 2 - end
                tIdx1 = sData.find(n2S, lastIdx)
                if -1 == tIdx1: return itemsTab
                lastIdx = tIdx1 + len(n2S)
                tIdx2 = sData.find(n2E, lastIdx)
                if -1 == tIdx2: return itemsTab
                lastIdx = tIdx2 + len(n2E)

                if n2P != None and sData.find(n2P, tIdx1 + len(n2S), tIdx2) == -1:
                    continue

                if withNodes:
                    idx2 = tIdx2 + len(n2E)
                else:
                    idx1 = idx2 + len(n1E)
                    idx2 = tIdx1
                search = 1
                itemsTab.append(sData[idx1:idx2])
        return itemsTab
        
    @staticmethod
    def rgetAllItemsBeetwenNodes(data, node1, node2, withNodes=True):
        if len(node1) < 2 or len(node2) < 2:
            return []
        itemsTab = []
        n1S = node1[0]
        n1E = node1[1]
        if len(node1) > 2: n1P = node1[2]
        else: n1P = None
        n2S = node2[0]
        n2E = node2[1]
        if len(node2) > 2: n2P = node2[2]
        else: n2P = None
        lastIdx = len(data)
        search = 1
        sData = data
        while True:
            if search == 1:
                # node 1 - end
                idx1 = sData.rfind(n1S, 0, lastIdx)
                if -1 == idx1: return itemsTab
                lastIdx = idx1
                idx2 = sData.find(n1E, idx1+len(n1S))
                if -1 == idx2: return itemsTab
                if n1P != None and sData.find(n1P, idx1 + len(n1S), idx2) == -1:
                    continue
                search = 2
            else:
                # node 2 - start
                tIdx1 = sData.rfind(n2S, 0, lastIdx)
                if -1 == tIdx1: return itemsTab
                lastIdx = tIdx1
                tIdx2 = sData.find(n2E, tIdx1+len(n2S), idx1)
                if -1 == tIdx2: return itemsTab
                if n2P != None and sData.find(n2P, tIdx1 + len(n2S), tIdx2) == -1:
                    continue
                if withNodes:
                    s1 = tIdx1
                    s2 = idx2 + len(n1E)
                else:
                    s1 = tIdx2 + len(n2E)
                    s2 = idx1
                search = 1
                itemsTab.insert(0, sData[s1:s2])
        return itemsTab
        
    @staticmethod    
    def removeDoubles(data, pattern):
        while -1 < data.find(pattern+pattern) and '' != pattern:
            data = data.replace(pattern+pattern, pattern)
        return data 

    @staticmethod
    def replaceHtmlTags(s, replacement=''):
        tag = False
        quote = False
        out = ""
        for c in s:
                if c == '<' and not quote:
                    tag = True
                elif c == '>' and not quote:
                    tag = False
                    out += replacement
                elif (c == '"' or c == "'") and tag:
                    quote = not quote
                elif not tag:
                    out = out + c
        return re.sub('&\w+;', ' ',out)        
        
    # this method is useful only for developers 
    # to dump page code to the file
    @staticmethod
    def writeToFile(file, data, mode = "w"):
        #helper to see html returned by ajax
        file_path = file
        text_file = open(file_path, mode)
        text_file.write(data)
        text_file.close()
    
    @staticmethod
    def getNormalizeStr(txt, idx=None):
        POLISH_CHARACTERS = {u'ą':u'a', u'ć':u'c', u'ę':u'ę', u'ł':u'l', u'ń':u'n', u'ó':u'o', u'ś':u's', u'ż':u'z', u'ź':u'z',
                             u'Ą':u'A', u'Ć':u'C', u'Ę':u'E', u'Ł':u'L', u'Ń':u'N', u'Ó':u'O', u'Ś':u'S', u'Ż':u'Z', u'Ź':u'Z',
                             u'á':u'a', u'é':u'e', u'í':u'i', u'ñ':u'n', u'ó':u'o', u'ú':u'u', u'ü':u'u',
                             u'Á':u'A', u'É':u'E', u'Í':u'I', u'Ñ':u'N', u'Ó':u'O', u'Ú':u'U', u'Ü':u'U',
                            }
        txt = txt.decode('utf-8')
        if None != idx: txt = txt[idx]
        nrmtxt = unicodedata.normalize('NFC', txt)
        ret_str = []
        for item in nrmtxt:
            if ord(item) > 128:
                item = POLISH_CHARACTERS.get(item)
                if item: ret_str.append(item)
            else: # pure ASCII character
                ret_str.append(item)
        return ''.join(ret_str).encode('utf-8')
        
    @staticmethod
    def isalpha(txt, idx=None):
        return CParsingHelper.getNormalizeStr(txt, idx).isalpha()

class common:
    HOST   = 'Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/17.0'
    HEADER = None
    ph = CParsingHelper
    
    @staticmethod
    def getParamsFromUrlWithMeta(url, baseHeaderOutParams=None):
        from Plugins.Extensions.OrhanTV1.sources.tx.iptvdh import DMHelper
        HANDLED_HTTP_HEADER_PARAMS = DMHelper.HANDLED_HTTP_HEADER_PARAMS #['Host', 'User-Agent', 'Referer', 'Cookie', 'Accept',  'Range']
        outParams = {}
        tmpParams = {}
        postData = None
        if isinstance(url, strwithmeta):
            if None != baseHeaderOutParams: tmpParams['header'] = baseHeaderOutParams
            else: tmpParams['header'] = {}
            for key in url.meta:
                if key in HANDLED_HTTP_HEADER_PARAMS:
                    tmpParams['header'][key] = url.meta[key]
            if 0 < len(tmpParams['header']):
                outParams = tmpParams
            if 'iptv_proxy_gateway' in url.meta:
                outParams['proxy_gateway'] = url.meta['iptv_proxy_gateway']
            if 'iptv_http_proxy' in url.meta:
                outParams['http_proxy'] = url.meta['iptv_http_proxy']
        return outParams, postData
        
    @staticmethod
    def getBaseUrl(url):
        from urlparse import urlparse
        parsed_uri = urlparse( url )
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        return domain
    
    def __init__(self, proxyURL= '', useProxy = False, useMozillaCookieJar=True):
        self.proxyURL = proxyURL
        self.useProxy = useProxy
        self.geolocation = {}
        self.useMozillaCookieJar = useMozillaCookieJar
        
    def getCountryCode(self, lower=True):
        if 'countryCode' not in self.geolocation:
            sts, data = self.getPage('http://ip-api.com/json')
            if sts:
                try:
                    self.geolocation['countryCode'] = byteify(json.loads(data))['countryCode']
                except Exception as ex:
                    print ex
        return self.geolocation.get('countryCode', '').lower()
        
    def clearCookie(self, cookiefile, leaveNames=[], removeNames=None, ignore_discard = True):
        try:
            toRemove = []
            if not self.useMozillaCookieJar:
                cj = cookielib.LWPCookieJar()
            else:
                cj = cookielib.MozillaCookieJar()
            cj.load(cookiefile, ignore_discard = ignore_discard)
            for cookie in cj:
                if cookie.name not in leaveNames and (None == removeNames or cookie.name in removeNames):
                    toRemove.append(cookie)
            for cookie in toRemove:
                cj.clear(cookie.domain, cookie.path, cookie.name)
            cj.save(cookiefile, ignore_discard = ignore_discard)
        except Exception as ex:
            print ex
            return False
        return True
        
    def getCookieItem(self, cookiefile, item):
        ret = ''
        try:
            if not self.useMozillaCookieJar:
                cj = cookielib.LWPCookieJar()
            else:
                cj = cookielib.MozillaCookieJar()
            cj.load(cookiefile, ignore_discard = True)
            for cookie in cj:
                if cookie.name == item: ret = cookie.value
        except Exception as ex:
            print ex
        return ret
        
    def getCookieHeader(self, cookiefile, allowedNames=[]):
        ret = ''
        try:
            if not self.useMozillaCookieJar:
                cj = cookielib.LWPCookieJar()
            else:
                cj = cookielib.MozillaCookieJar()
            cj.load(cookiefile, ignore_discard = True)
            for cookie in cj:
                if 0 < len(allowedNames) and cookie.name not in allowedNames: continue
                ret += '%s=%s; ' % (cookie.name, urllib.unquote(cookie.value))
        except Exception as ex:
            print ex
        return ret

    def html_entity_decode_char(self, m):
        ent = m.group(1)
        if ent.startswith('x'):
            return unichr(int(ent[1:],16))
        try:
            return unichr(int(ent))
        except Exception:
            if ent in htmlentitydefs.name2codepoint:
                return unichr(htmlentitydefs.name2codepoint[ent])
            else:
                return ent

    def html_entity_decode(self, string):
        string = string.decode('UTF-8')
        s = re.compile("&#?(\w+?);").sub(self.html_entity_decode_char, string)
        return s.encode('UTF-8')
        
    def isValidUrl(self, url):
        return url.startswith('http://') or url.startswith('https://')
    
    def getPage(self, url, addParams = {}, post_data = None):
        ''' wraps getURLRequestData '''
        try:
            addParams['url'] = url
            if 'return_data' not in addParams:
                addParams['return_data'] = True
            response = self.getURLRequestData(addParams, post_data)
            status = True
        except urllib2.HTTPError, e:
            print e
            response = e
            status = False
        except Exception as ex:
            print ex
            response = None
            status = False
        
        if addParams['return_data'] and status and not isinstance(response, basestring):
            status = False
            
        return (status, response)
        
    def getPageWithWget(self, url, params={}, post_data=None):
        from Plugins.Extensions.OrhanTV1.sources.tx.iptvdh import DMHelper
        cmd = DMHelper.getBaseWgetCmd(params.get('header', {})) +  (" --timeout=20 --tries=1 '%s' " % url)
        if post_data != None:
            if params.get('raw_post_data', False):
                post_data_str = post_data
            else:
                post_data_str = urllib.urlencode(post_data)
            cmd += " --post-data '{0}' ".format(post_data_str)
        
        if params.get('use_cookie', False):
            cmd += " --keep-session-cookies "
            cookieFile = str(params.get('cookiefile', ''))
            if params.get('load_cookie', False) and fileExists(cookieFile):
                cmd += "  --load-cookies '%s' " %  cookieFile
            if params.get('save_cookie', False):
                cmd += "  --save-cookies '%s' " %  cookieFile
        cmd += ' -O - 2> /dev/null'
        
        from Plugins.Extensions.OrhanTV1.sources.tx.asynccall import iptv_execute
        
        data = iptv_execute()( cmd )
        
        if params.get('use_cookie', False) and params.get('save_cookie', False) and fileExists(cookieFile):
            # fix cookie 
            
            try:
                f = open(cookieFile, "r")
                cookieStr = f.read()
                f.close()
                
                marker = '# HTTP cookie file.'
                if cookieStr.startswith(marker):
                    cookieStr = cookieStr.replace(marker, '# HTTP Cookie File.')
                    f = open(cookieFile, "w")
                    f.write(cookieStr)
                    f.close()
            except Exception as ex:
                print ex
            
        
        if not data['sts'] or 0 != data['code']: 
            return False, None
        else:
            return True, data['data']
        
        
    def calcAnswer(self, data):
        sourceCode = data
        try:
            code = compile(sourceCode, '', 'exec')
        except Exception as ex:
            print ex
            return 0
        vGlobals = {"__builtins__": None, 'string': string, 'int':int, 'str':str}
        vLocals = { 'paramsTouple': None }
        try:
            exec( code, vGlobals, vLocals )
        except Exception as ex:
            print ex
            return 0
        return vLocals['a']
        
    def getPageCFProtection(self, baseUrl, params={}, post_data=None):
        cfParams = params.get('cloudflare_params', {})
        
        def _getFullUrlEmpty(url):
            return url
        _getFullUrl  = cfParams.get('full_url_handle', _getFullUrlEmpty)
        _getFullUrl2 = cfParams.get('full_url_handle2', _getFullUrlEmpty)
        
        url = baseUrl
        header = {'Referer':url, 'User-Agent':cfParams.get('User-Agent', ''), 'Accept-Encoding':'text'}
        header.update(params.get('header', {}))
        params.update({'use_cookie': True, 'save_cookie': True, 'load_cookie': True, 'cookiefile': cfParams.get('cookie_file', ''), 'header':header})
        sts, data = self.getPage(url, params, post_data)
        
        current = 0
        while current < 3:
            #if True:
            if not sts and None != data:
                start_time = time.time()
                current += 1
                doRefresh = False
                try:
                    #try: verData = data.fp.read()
                    #except Exception: verData = data
                    verData = data.fp.read()
                    
                    sitekey = self.ph.getSearchGroups(verData, 'data-sitekey="([^"]+?)"')[0]
                    id = self.ph.getSearchGroups(verData, 'data-ray="([^"]+?)"')[0]
                    if sitekey != '':
                        from Plugins.Extensions.OrhanTV1.sources.recaptcha_v2 import UnCaptchaReCaptcha
                        # google captcha
                        recaptcha = UnCaptchaReCaptcha(lang=profile_path )
                        recaptcha.HTTP_HEADER['Referer'] = baseUrl
                        if '' != cfParams.get('User-Agent', ''): recaptcha.HTTP_HEADER['User-Agent'] = cfParams['User-Agent']
                        token = recaptcha.processCaptcha(sitekey)
                        if token == '': return False, None
                    
                        sts, tmp = self.ph.getDataBeetwenMarkers(verData, '<form', '</form>', caseSensitive=False)
                        if not sts: return False, None
                        
                        url = _getFullUrl( self.ph.getSearchGroups(tmp, 'action="([^"]+?)"')[0] )
                        actionType = self.ph.getSearchGroups(tmp, 'method="([^"]+?)"', 1, True)[0].lower()
                        post_data2 = dict(re.findall(r'<input[^>]*name="([^"]*)"[^>]*value="([^"]*)"[^>]*>', tmp))
                        #post_data2['id'] = id
                        if '' != token:
                            post_data2['g-recaptcha-response'] = token
                        else:
                            continue
                        params2 = dict(params)
                        params2['header']= dict(params['header'])
                        params2['header']['Referer'] = baseUrl
                        if actionType == 'get':
                            if '?' in url:
                                url += '&'
                            else:
                                url += '?'
                            url += urllib.urlencode(post_data2)
                            post_data2 = None
                        sts, data = self.getPage(url, params2)
                    else:
                        dat = self.ph.getDataBeetwenMarkers(verData, 'setTimeout', 'submit()', False)[1]
                        tmp = self.ph.getSearchGroups(dat, '={"([^"]+?)"\:([^}]+?)};', 2)
                        varName = tmp[0]
                        expresion= ['a=%s' % tmp[1]]
                        e = re.compile('%s([-+*])=([^;]+?);' % varName).findall(dat)
                        for item in e:
                            expresion.append('a%s=%s' % (item[0], item[1]) )
                        
                        for idx in range(len(expresion)):
                            e = expresion[idx]
                            e = e.replace('!+[]', '1')
                            e = e.replace('!![]', '1')
                            e = e.replace('=+(', '=int(')
                            if '+[]' in e:
                                e = e.replace(')+(', ')+str(')
                                e = e.replace('int((', 'int(str(')
                                e = e.replace('(+[])', '(0)')
                                e = e.replace('+[]', '')
                            expresion[idx] = e
                        
                        answer = self.calcAnswer('\n'.join(expresion)) + len(cfParams['domain'])
                        refreshData = data.fp.info().get('Refresh', '')
                        
                        verData = self.ph.getDataBeetwenReMarkers(verData, re.compile('<form[^>]+?id="challenge-form"'), re.compile('</form>'), False)[1]
                        verUrl =  _getFullUrl( self.ph.getSearchGroups(verData, 'action="([^"]+?)"')[0] )
                        get_data = dict(re.findall(r'<input[^>]*name="([^"]*)"[^>]*value="([^"]*)"[^>]*>', verData))
                        get_data['jschl_answer'] = answer
                        verUrl += '?'
                        for key in get_data:
                            verUrl += '%s=%s&' % (key, get_data[key])
                        verUrl = _getFullUrl( self.ph.getSearchGroups(verData, 'action="([^"]+?)"')[0] ) + '?jschl_vc=%s&pass=%s&jschl_answer=%s' % (get_data['jschl_vc'], get_data['pass'], get_data['jschl_answer'])
                        verUrl = _getFullUrl2( verUrl )
                        params2 = dict(params)
                        params2['load_cookie'] = True
                        params2['save_cookie'] = True
                        params2['header'] = dict(params.get('header', {}))
                        params2['header'].update({'Referer':url, 'User-Agent':cfParams.get('User-Agent', ''), 'Accept-Encoding':'text'})
                        time.sleep(5-(time.time() - start_time))
                        sts, data = self.getPage(verUrl, params2, post_data)
                except Exception as ex:
                    print ex
            else:
                break
        return sts, data
        
    def saveWebFile(self, file_path, url, addParams = {}, post_data = None):
        bRet = False
        downDataSize = 0
        dictRet = {}
        try:
            outParams, postData = self.getParamsFromUrlWithMeta(url)
            addParams.update(outParams)
            if 'header' not in addParams and 'host' not in addParams:
                host = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.18) Gecko/20110621 Mandriva Linux/1.9.2.18-0.1mdv2010.2 (2010.2) Firefox/3.6.18'
                header = {'User-Agent': host, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
                addParams['header'] = header
            addParams['return_data'] = False
            sts, downHandler = self.getPage(url, addParams, post_data)

            if addParams.get('ignore_content_length', False):
                meta = downHandler.info()
                contentLength = int(meta.getheaders("Content-Length")[0])
            else:
                contentLength = None
            
            checkFromFirstBytes = addParams.get('check_first_bytes', [])
            OK = True
            if 'maintype' in addParams and addParams['maintype'] != downHandler.headers.maintype:
                if 0 == len(checkFromFirstBytes):
                    downHandler.close()
                OK = False
            
            if OK and 'subtypes' in addParams:
                OK = False
                for item in addParams['subtypes']:
                    if item == downHandler.headers.subtype:
                        OK = True
                        break
            
            if OK or len(checkFromFirstBytes):
                blockSize = addParams.get('block_size', 8192)
                fileHandler = None
                while True:
                    buffer = downHandler.read(blockSize)
                    
                    if len(checkFromFirstBytes):
                        OK = False
                        for item in checkFromFirstBytes:
                            if buffer.startswith(item):
                                OK = True
                                break
                        if not OK:
                            break
                        else:
                            checkFromFirstBytes = []
                    
                    if not buffer:
                        break
                    downDataSize += len(buffer)
                    if len(buffer):
                        if fileHandler == None:
                            fileHandler = file(file_path, "wb")
                        fileHandler.write(buffer)
                if fileHandler != None:
                    fileHandler.close()
                downHandler.close()
                if None != contentLength and contentLength == downDataSize:
                    bRet = True
        except Exception:
             print ("common.getFile download file exception")
        dictRet.update( {'sts': True, 'fsize': downDataSize} )
        return dictRet
    
    def getURLRequestData(self, params = {}, post_data = None):
        
        def urlOpen(req, customOpeners, timeout):
            if len(customOpeners) > 0:
                opener = urllib2.build_opener( *customOpeners )
                if timeout != None:
                    response = opener.open(req, timeout=timeout)
                else:
                    response = opener.open(req)
            else:
                if timeout != None:
                    response = urllib2.urlopen(req, timeout=timeout)
                else:
                    response = urllib2.urlopen(req)
            return response
        
        if not self.useMozillaCookieJar:
            cj = cookielib.LWPCookieJar()
        else:
            cj = cookielib.MozillaCookieJar()
        response = None
        req      = None
        out_data = None
        opener   = None
        
        timeout = params.get('timeout', None)
        
        if 'host' in params:
            host = params['host']
        else:
            host = self.HOST

        if 'header' in params:
            headers = params['header']
        elif None != self.HEADER:
            headers = self.HEADER
        else:
            headers = { 'User-Agent' : host }
            
        if 'User-Agent' not in headers:
            headers['User-Agent'] = host


        customOpeners = []
        #cookie support
        if 'use_cookie' not in params and 'cookiefile' in params and ('load_cookie' in params or 'save_cookie' in params):
            params['use_cookie'] = True 
        
        if params.get('use_cookie', False):
            if params.get('load_cookie', False):
                try:
                    cj.load(params['cookiefile'], ignore_discard = True)
               
                except Exception as ex:
                    print ex
            try:
                for cookieKey in params.get('cookie_items', {}).keys():
                    cookieItem = cookielib.Cookie(version=0, name=cookieKey, value=params['cookie_items'][cookieKey], port=None, port_specified=False, domain='', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
                    cj.set_cookie(cookieItem)
            except Exception as ex:
                print ex
            customOpeners.append( urllib2.HTTPCookieProcessor(cj) )
            
        if params.get('no_redirection', False):
            customOpeners.append( NoRedirection() )
        
        # debug 
        #customOpeners.append(urllib2.HTTPSHandler(debuglevel=1))
        #customOpeners.append(urllib2.HTTPHandler(debuglevel=1))
        
            #try: customOpeners.append(urllib2_ssl.HTTPSHandler(ssl_version=ssl.PROTOCOL_SSLv3)) # #PROTOCOL_TLSv1 PROTOCOL_SSLv3
            #except Exception:printExc()
            try: customOpeners.append(urllib2.HTTPSHandler(context=ssl._create_unverified_context()))
            except Exception: pass
        #proxy support
        if self.useProxy:
            http_proxy = self.proxyURL
        else:
            http_proxy = ''
        #proxy from parameters (if available) overwrite default one
        if 'http_proxy' in params:
            http_proxy = params['http_proxy']
        if '' != http_proxy:
            customOpeners.append( urllib2.ProxyHandler({"http":http_proxy}) )
            customOpeners.append( urllib2.ProxyHandler({"https":http_proxy}) )
        
        pageUrl = params['url']
        proxy_gateway = params.get('proxy_gateway', '')
        if proxy_gateway != '':
            pageUrl = proxy_gateway.format(urllib.quote_plus(pageUrl, ''))

        if None != post_data:
            if params.get('raw_post_data', False):
                dataPost = post_data
            elif params.get('multipart_post_data', False):
                customOpeners.append( MultipartPostHandler() )
                dataPost = post_data
            else:
                dataPost = urllib.urlencode(post_data)
            req = urllib2.Request(pageUrl, dataPost, headers)
        else:
            req = urllib2.Request(pageUrl, None, headers)

        if not params.get('return_data', False):
            out_data = urlOpen(req, customOpeners, timeout)
        else:
            gzip_encoding = False
            try:
                response = urlOpen(req, customOpeners, timeout)
                if response.info().get('Content-Encoding') == 'gzip':
                    gzip_encoding = True
                data = response.read()
                response.close()
            except urllib2.HTTPError, e:
                ignoreCodeRanges = params.get('ignore_http_code_ranges', [(404, 404), (500, 500)])
                ignoreCode = False
                for ignoreCodeRange in ignoreCodeRanges:
                    if e.code >= ignoreCodeRange[0] and e.code <= ignoreCodeRange[1]:
                        ignoreCode = True
                        break
                
                if ignoreCode:
                    if e.fp.info().get('Content-Encoding', '') == 'gzip':
                        gzip_encoding = True
                    data = e.fp.read()
                    #e.msg
                    #e.headers
                elif e.code == 503:
                    if params.get('use_cookie', False):
                        new_cookie = e.fp.info().get('Set-Cookie', '')
                        cj.save(params['cookiefile'], ignore_discard = True)
                    raise e
                else:
                    if e.code in [300, 302, 303, 307] and params.get('use_cookie', False) and params.get('save_cookie', False):
                        new_cookie = e.fp.info().get('Set-Cookie', '')
                        #for cookieKey in params.get('cookie_items', {}).keys():
                        #    cj.clear('', '/', cookieKey)
                        cj.save(params['cookiefile'], ignore_discard = True)
                    raise e
            try:
                if gzip_encoding:
                   
                    buf = StringIO(data)
                    f = gzip.GzipFile(fileobj=buf)
                    out_data = f.read()
                else:
                    out_data = data
            except Exception:
                out_data = data
 
        if params.get('use_cookie', False) and params.get('save_cookie', False):
            try:
                cj.save(params['cookiefile'], ignore_discard = True)
            except Exception  as ex:
                print ex
                GetCookieDir()
                raise e

        return out_data 

    def urlEncodeNonAscii(self, b):
        return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

    def iriToUri(self, iri):
        import urlparse
        parts = urlparse.urlparse(iri.decode('utf-8'))
        return urlparse.urlunparse(
            part.encode('idna') if parti==1 else self.urlEncodeNonAscii(part.encode('utf-8'))
            for parti, part in enumerate(parts)
        )

    def makeABCList(self, tab = ['0 - 9']):
        strTab = list(tab)
        for i in range(65,91):
            strTab.append(str(unichr(i)))    
        return strTab

    def isNumeric(self,s):
        try:
            float(s)
            return True
        #except ValueError:
        except Exception:
            return False
        
    def setLinkTable(self, url, host):
        strTab = []
        strTab.append(url)
        strTab.append(host)
        return strTab
    
class Chars:
    def __init__(self):
        pass
    
    def setCHARS(self):
        return CHARS
    
    def replaceString(self, array, string):
        out = string
        for i in range(len(array)):
            out = string.replace(array[i][0], array[i][1])
            string = out
        return out    
    
    def replaceChars(self, string):
        out = string
        for i in range(len(CHARS)):
            out = string.replace(CHARS[i][0], CHARS[i][1])
            string = out
        return out

