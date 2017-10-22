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

from resources.lib.core import addon

from resources.lib.common.utils import XbmcUtil
from resources.lib.core.addon import Action, Param, Error

################################################################################
# Constant Definitions
################################################################################

TAG = "{_caller}/ {msg}"

log = XbmcUtil.getLogger()

################################################################################
#  Class Definitions
################################################################################

class SwampAddon:

    def __init__(self, argv):
        self.tag = self.__class__.__name__
        self.base = argv[0]
        self.handle = int(argv[1])
        self.params = XbmcUtil.parseParams(argv[2])
        # log(TAG.format(
        #         _caller=self.tag, 
        #         msg="initialized {}".format(repr(self))
        #     )
        # )

    def __repr__(self):
        return json.dumps({
            "base": self.base,
            "handle": self.handle,
            "params": self.params,
        }, indent=2)

    def execute(self):
        tag = ".".join([self.tag, 'execute'])
        action = self.params.get(Param.ACTION, None)
        h = self.handle

        result = None

        if action == Action.MAINMENU:
            from resources.lib.core import menus
            result = menus.Directory(h).main()

        elif action == Action.BROWSE:
            path = self.params.get(Param.QUERY, None)
            if path is not None:
                from resources.lib.core import menus
                result = menus.Directory(h).execute(path)
            else: 
                return addon.swampError(tag, Error.MISSING_PARAM, Param.QUERY)
        
        elif action == Action.PLAY:
            url  = self.params.get(Param.URL, None)
            if url is not None:
                from resources.lib.core import streams
                streams.Resolver(h).resolve(url)
            else: 
                return addon.swampError(tag, Error.MISSING_PARAM, Param.URL)

        elif action == Action.SETTINGS:
            from resources.lib.common import control
            control.openSettings()

        elif action == Action.CLEARCACHE:
            from resources.lib.common import cache
            cache.clear()

        else: return addon.swampError(tag, Error.UNKNOWN_ACTION, action)

        return result
    