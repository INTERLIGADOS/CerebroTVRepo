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

import json
import urllib

from resources.lib.core import swamp_api

from resources.lib.core.addon import Action, Param, Assets
from resources.lib.common.utils import XmlUtil

################################################################################
#  Constant Definitions
################################################################################

PARAM_WRAPPER = "=".join([Param.ACTION, "{action}&{extra}=%s"])

################################################################################
#  Class Definitions
################################################################################

class ListItem:
    """ This is a parent class holding common data/logic for parsing swamp-api 
        xml elements into xbmc listItems.
    """
    label = None
    isPlayable = False

    _path = None
    _paramstring = None

    def __init__(self, label=""):
        self.label = str(label)

        self._meta = {
            swamp_api.tags.title: str(label),
            swamp_api.tags.info: "",
            swamp_api.tags.genre: "",
        }

        self._assets = {
            swamp_api.tags.thumb: Assets.THUMBNAIL,
            swamp_api.tags.fanart: Assets.FANART,
        }

    def __repr__(self):
        return " ".join([
            self.__class__.__name__, 
            json.dumps({
                "label": self.label,
                "isPlayable": self.isPlayable,
                "paramstring": self.paramstring(),
                "_meta": self._meta,
                "_assets": self._assets,
            }, indent=2)
        ])

    def create(self, element):
        self.label = XmlUtil.parseTag(element, swamp_api.tags.title)

        for tag in self._meta.keys():
            tmp = XmlUtil.parseTag(element, tag)
            if tmp != "": self._meta[tag] = tmp

        for tag in self._assets.keys():
            tmp = XmlUtil.parseTag(element, tag)
            if tmp != "": self._assets[tag] = tmp

        self._setParamstring(element)

        return self

    def meta(self, key):
        if key in self._meta.keys(): return self._meta[key]
        else: 
            raise Exception("Invalid metadata type '{}'".format(key))

    def asset(self, key):
        if key in self._assets.keys(): return self._assets[key] 
        else:
            raise Exception("Invalid asset type '{}'".format(key))

    def paramstring(self):
        """ generate encoded xbmc querystring from current object state """
        return self._paramstring % (urllib.quote_plus(self._path))

    def _setParamstring(self, element):
        content_tags = {
            swamp_api.tags.link: (Action.PLAY, Param.URL),
            swamp_api.tags.internal: (Action.BROWSE, Param.QUERY),
        }

        for tag in content_tags.keys():
            path = XmlUtil.parseTag(element, tag)

            if path != "":
                self._path = path
                action, extra = content_tags[tag]

                if action == Action.PLAY: self.isPlayable = True

                self._paramstring = PARAM_WRAPPER.format(
                    action=action, extra=extra
                )

        if not self._path or not self._paramstring:
            raise Exception("Failed to parse XML element")
