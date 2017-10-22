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
import urlparse

try: import xbmc; __devel__ = False
except: __devel__ = True

################################################################################
#  Constant Definitions
################################################################################

__ADDON_ID__ = "plugin.video.mobdina"                                           ## FIXME: need a good way to make this
                                                                                #         global
LOGLEVEL = {
    0: "DEBUG",
    1: "INFO",
    2: "NOTICE",
    3: "WARNING",
    4: "ERROR",
    5: "SEVERE",
    6: "FATAL",
    7: "NONE",
}

################################################################################
#  Class Definitions
################################################################################

class XbmcUtil:

    LOGDEBUG   = 0
    LOGINFO    = 1
    LOGNOTICE  = 2
    LOGWARNING = 3
    LOGERROR   = 4
    LOGSEVERE  = 5
    LOGFATAL   = 6
    LOGNONE    = 7

    @staticmethod
    def getLogger():
        return _xbmcLog if not __devel__ else _consoleLog

    @staticmethod
    def getPluginUri():
        return "plugin://{}".format(__ADDON_ID__)

    @staticmethod
    def parseParams(args):
        return dict(urlparse.parse_qsl(re.sub("\?", "", args)))

class XmlUtil:

    @staticmethod
    def parseTag(element, tag):
        tmp = element.find(tag)
        if tmp is not None and tmp.text is not None:
            return tmp.text.strip()
        return ""

################################################################################
#  Function Definitions
################################################################################


def _xbmcLog(message, level=XbmcUtil.LOGDEBUG):
    try:
        if isinstance(message, unicode): message = message.encode('utf-8')
        xbmc.log('{}/ {}'.format(__ADDON_ID__, message), level)
    except: pass


def _consoleLog(message, level=XbmcUtil.LOGDEBUG):
    print('[{}] {}'.format(LOGLEVEL[level], message))


def _getDOMContent(html, name, match, ret):  # Cleanup
    endstr = u"</" + name  # + ">"

    start = html.find(match)
    end = html.find(endstr, start)
    pos = html.find("<" + name, start + 1 )

    while pos < end and pos != -1:  # Ignore too early </endstr> return
        tend = html.find(endstr, end + len(endstr))
        if tend != -1:
            end = tend
        pos = html.find("<" + name, pos + 1)

    if start == -1 and end == -1:
        result = u""
    elif start > -1 and end > -1:
        result = html[start + len(match):end]
    elif end > -1:
        result = html[:end]
    elif start > -1:
        result = html[start + len(match):]

    if ret:
        endstr = html[end:html.find(">", html.find(endstr)) + 1]
        result = match + result + endstr

    return result


def _getDOMAttributes(match, name, ret):
    lst = re.compile('<' + name + '.*?' + ret + '=([\'"].[^>]*?[\'"])>', re.M | re.S).findall(match)
    if len(lst) == 0:
        lst = re.compile('<' + name + '.*?' + ret + '=(.[^>]*?)>', re.M | re.S).findall(match)
    ret = []
    for tmp in lst:
        cont_char = tmp[0]
        if cont_char in "'\"":

            # Limit down to next variable.
            if tmp.find('=' + cont_char, tmp.find(cont_char, 1)) > -1:
                tmp = tmp[:tmp.find('=' + cont_char, tmp.find(cont_char, 1))]

            # Limit to the last quotation mark
            if tmp.rfind(cont_char, 1) > -1:
                tmp = tmp[1:tmp.rfind(cont_char)]
        else:
            if tmp.find(" ") > 0:
                tmp = tmp[:tmp.find(" ")]
            elif tmp.find("/") > 0:
                tmp = tmp[:tmp.find("/")]
            elif tmp.find(">") > 0:
                tmp = tmp[:tmp.find(">")]

        ret.append(tmp.strip())

    return ret


def _getDOMElements(item, name, attrs):
    lst = []
    for key in attrs:
        lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=[\'"]' + attrs[key] + '[\'"].*?>))', re.M | re.S).findall(item)
        if len(lst2) == 0 and attrs[key].find(" ") == -1:  # Try matching without quotation marks
            lst2 = re.compile('(<' + name + '[^>]*?(?:' + key + '=' + attrs[key] + '.*?>))', re.M | re.S).findall(item)

        if len(lst) == 0:
            lst = lst2
            lst2 = []
        else:
            test = range(len(lst))
            test.reverse()
            for i in test:  # Delete anything missing from the next list.
                if not lst[i] in lst2:
                    del(lst[i])

    if len(lst) == 0 and attrs == {}:
        lst = re.compile('(<' + name + '>)', re.M | re.S).findall(item)
        if len(lst) == 0:
            lst = re.compile('(<' + name + ' .*?>)', re.M | re.S).findall(item)

    return lst


def parseDOM(html, name=u"", attrs={}, ret=False):

    if isinstance(name, str): # Should be handled
        try: name = name #.decode("utf-8")
        except: log("Couldn't decode name binary string: " + repr(name), XbmcUtil.LOGERROR)

    if isinstance(html, str):
        try:
            html = [html.decode("utf-8")] # Replace with chardet thingy
        except:
            log("Couldn't decode html binary string. Data length: " + repr(len(html)), XbmcUtil.LOGERROR)
            html = [html]
    elif isinstance(html, unicode):
        html = [html]
    elif not isinstance(html, list):
        log("Input isn't list or string/unicode.")
        return u""

    if not name.strip():
        log("Missing tag name")
        return u""

    ret_lst = []
    for item in html:
        temp_item = re.compile('(<[^>]*?\n[^>]*?>)').findall(item)
        for match in temp_item:
            item = item.replace(match, match.replace("\n", " "))

        lst = _getDOMElements(item, name, attrs)

        if isinstance(ret, str):
            lst2 = []
            for match in lst:
                lst2 += _getDOMAttributes(match, name, ret)
            lst = lst2
        else:
            lst2 = []
            for match in lst:
                temp = _getDOMContent(item, name, match, ret).strip()
                item = item[item.find(temp, item.find(match)) + len(temp):]
                lst2.append(temp)
            lst = lst2
        ret_lst += lst

    return ret_lst


log = XbmcUtil.getLogger()
