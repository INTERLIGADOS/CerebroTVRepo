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

import os

try: import xbmc, xbmcvfs, xbmcgui, xbmcplugin, xbmcaddon; __devel__ = False
except: __devel__ = True

################################################################################
#  XBMC Aliased Function Definitions
################################################################################

if not __devel__:

    addonInfo = xbmcaddon.Addon().getAddonInfo

    setting = xbmcaddon.Addon(id='plugin.video.mobdina').getSetting

    execute = xbmc.executebuiltin
    
    makeFile = xbmcvfs.mkdir
    
    dialog = xbmcgui.Dialog()

    progressDialog = xbmcgui.DialogProgress()
    
    createItem = xbmcgui.ListItem
    
    addItem = xbmcplugin.addDirectoryItem

    endDirectory = xbmcplugin.endOfDirectory

    lang = xbmcaddon.Addon().getLocalizedString

    infoLabel = xbmc.getInfoLabel

    player = xbmc.Player()

    resolve = xbmcplugin.setResolvedUrl

    translate = xbmc.translatePath

    dataPath = translate(addonInfo('profile')).decode('utf-8')

    cacheFile = os.path.join(dataPath, 'cache.db')

    sleep = xbmc.sleep

################################################################################
#  Function Definitions
################################################################################


def idle():
    if __devel__: return None
    else: return execute('Dialog.Close(busydialog)')


def selectDialog(list, heading=addonInfo('name')):
    return None if __devel__ else \
        dialog.select(heading, list)


def yesNoDialog(l1, l2, l3, header=addonInfo('name'), no='cancel', yes='ok'):
    return None if __devel__ else \
        dialog.yesno(
            header, line1=l1, line2=l2, line3=l3, nolabel=no, yeslabel=yes
        )


def infoDialog(message, header=addonInfo('name'), icon=addonInfo('icon'), time=3000):
    if __devel__: return
    try: dialog.notification(header, message, icon, time, sound=False)
    except: execute("Notification({}, {}, {}, {})".format(
        header, message, time, icon))


def openSettings(query=None, id=addonInfo('id')):
    if not __devel__:
        idle()
        execute('Addon.OpenSettings(%s)' % id)
        if not query: return
        c, f = query.split('.')
        execute('SetFocus(%i)' % (int(c) + 100))
        execute('SetFocus(%i)' % (int(f) + 200))
        