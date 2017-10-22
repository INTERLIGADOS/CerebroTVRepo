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

import xml.etree.ElementTree as etree

from resources.lib.core import addon, entities, swamp_api
from resources.lib.common import client, control

from resources.lib.core.addon import Error
from resources.lib.common.utils import XbmcUtil, XmlUtil

################################################################################
#  Constant Definitions
################################################################################

log = XbmcUtil.getLogger()
log_wrapper = "{_caller}/ {_msg}"

################################################################################
#  Class Definitions
################################################################################

class Directory:

    def __init__(self, handle):
        self.tag = self.__class__.__name__
        self.handle = handle
        self.list = list()
        self.error = 0

    def main(self):
        """ The reason this has it's own method is we will probably want to be 
            able to manually inject some entries into the main menu.
        """
        root = self._getRoot(q=swamp_api.indexes.category)

        self._populate(root)
        self._render()

        if self.error != 0: return self.error

    def execute(self, path):
        root = self._getRoot(q=path)

        self._populate(root)
        self._render()

        if self.error != 0: return self.error

    def _getRoot(self, q):
        tag = ".".join([self.tag, "_getRoot"])

        req = "".join([swamp_api.portal, q, "/"])
        # log(log_wrapper.format(
        #         _caller=tag, _msg="modbro-api call '{}'".format(req)
        #     )
        # )

        data = client.request(req)
        if data is None:
            self.error = addon.swampError(tag, Error.HTTP_REQUEST)
        try:
            tree = etree.ElementTree(etree.fromstring(data))
        except:
            self.error = addon.swampError(tag, Error.INVALID_XML)
        else:
            return tree.getroot()

    def _populate(self, root):
        for element in root.findall('item'):
            self.list.append(entities.ListItem().create(element))

    def _render(self, cacheResult=True):
        tag = ".".join([self.tag, "_populatedDirectory"])

        menuItems = self.list
        if len(menuItems) > 0:    
            for mItem in menuItems:
                item = control.createItem(label=mItem.label)
                item.setInfo(type='video', infoLabels={ 
                    'title': mItem.label,
                    'plot': mItem.meta('info')
                })
                item.setArt({ 
                    'thumb': mItem.asset(swamp_api.tags.thumb), 
                    'fanart': mItem.asset(swamp_api.tags.fanart), 
                })

                url = "?".join([XbmcUtil.getPluginUri(), mItem.paramstring()])
                control.addItem(
                    handle=self.handle, url=url, listitem=item, 
                    isFolder=not mItem.isPlayable, totalItems=len(menuItems)
                )

                # log(log_wrapper.format(
                #         _caller=tag, 
                #         _msg="created ListItem '{}'".format(url)
                #     )
                # )
        else:
            self.error = addon.swampError(tag, Error.NO_RESULTS, fatal=False)

        control.endDirectory(self.handle, cacheToDisc=cacheResult)
