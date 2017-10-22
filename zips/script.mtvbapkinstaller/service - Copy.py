#
#       Copyright (C) 2014
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import utils
import xbmc
import os
import xbmcgui
import zipfile
import sfile

utils.VerifyZipFiles()
utils.VerifyKeymaps()
utils.verifyPlugins()
utils.verifyLocation()

global CHANGELOG
CHANGELOG = None

ADDON    = utils.ADDON
ADDONID  = utils.ADDONID
HOME     = xbmc.translatePath('special://userdata')
ROOT     = utils.ROOT
TITLE    = utils.TITLE

GETTEXT  = utils.GETTEXT

REMOTE       = True
LOCATION     = "http://megatvbox.co.uk/TV-DATA/menu.zip"
IMPORT_RESET = True
def extractAll(filename, dp, location):
    global CHANGELOG
    CHANGELOG = None
    #xbmcgui.Dialog().ok("CerebroTV","Download Complete")
    #utils.Progress("CerebroTV Menu Updater", line1 = "Download Complete", line2 = location.replace('%20', ' '), line3 = GETTEXT(30141))
    zin = zipfile.ZipFile(filename, 'r')

    relroot = os.path.abspath(os.path.join(ROOT, os.pardir))

    root    = os.path.join(HOME, 'SF_Temp')
    profile = os.path.join(root, 'Super Favourites')

    #copy existing settings to root
    dst = os.path.join(root, 'settings.xml')
    src = os.path.join(ROOT, 'settings.xml')
    sfile.copy(src, dst)

    if IMPORT_RESET:
        try:    sfile.rmtree(os.path.join(ROOT, 'Super Favourites'))
        except: pass

    try:
        nItem = float(len(zin.infolist()))
        index = 0
        for item in zin.infolist():
            index += 1

            percent  = int(index / nItem *100)
            filename = item.filename

            locationmega = "CerebroTV Servers"
            if dp:
                dp.update(percent, GETTEXT(30140) % filename, locationmega, GETTEXT(30141))

            if filename == 'settings.xml':
                #if utils.DialogYesNo(GETTEXT(30135), line2='', line3=GETTEXT(30136), noLabel=None, yesLabel=None):
                zin.extract(item, root)
            elif filename == 'changelog.txt':
                try:
                    zin.extract(item, root)      
                    filename  = os.path.join(root, filename)
                    CHANGELOG = sfile.read(filename)
                    utils.DeleteFile(filename)
                except Exception, e:
                    utils.log('Changelog error in extractAll')
                    utils.log(e)
            elif filename.lower().startswith('super favourites'):
                zin.extract(item, root)
            elif filename.lower().startswith('s'):
                zin.extract(item, root)
            elif filename.lower().startswith('h'):
                zin.extract(item, root)
            elif filename.lower().startswith('pl'):
                zin.extract(item, root)
            else:
                zin.extract(item, profile)

    except Exception, e:
        utils.log('Error whilst unzipping %s' % location)
        utils.log(e)        
        return False

    sfile.copytree(root, ROOT)
    sfile.rmtree(root)
    return True

def _doImportFromRemote():
    try:
        location = LOCATION.replace(' ', '%20')
        file     = os.path.join(HOME, '_sf_temp.zip')

        dp = utils.Progress("[COLOR tomato]CerebroTV Checking For Updates[/COLOR]", line1 = "[COLOR yellow]Please Wait Download in Progress[/COLOR].", line2 = "[COLOR gold]CerebroTV Update Service[/COLOR]", line3 = GETTEXT(30141))

        import download
        import urllib
        download.doDownload(urllib.quote_plus(location), urllib.quote_plus(file), urllib.quote_plus(TITLE), quiet=True)

        if os.path.exists(file): 
            success = extractAll(file, dp, location.replace('%20', ' '))
            utils.DeleteFile(file)
            return success
    except Exception, e:
        utils.log('Error in _doImportFromRemote %s' % str(e))

    return False


 
gomegatvbox = True;
if gomegatvbox == True:

    _doImportFromRemote()
    #xbmc.executebuiltin("Notification(CerebroTV,Please Wait Loading Menu,15000,)")	
    xbmc.sleep(3000)
    file2 = os.path.join(HOME, 'megatvbox.xml')
    with open(file2, 'r') as myfile:
        data=float(myfile.read())

    import urllib2
    response = urllib2.urlopen('http://megatvbox.co.uk/TV-DATA/megatvbox2.txt')
    data2=float(response.read())

if data < data2:
    update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV New Version Detcted[/COLOR]","[COLOR yellow]Your Version[/COLOR]: [COLOR red]" + srt(data) + "[/COLOR] | [COLOR yellow]New Version[/COLOR]: [COLOR green]" + str(data2) + "[/COLOR]","[COLOR tomato]Would You Like to Update Now[/COLOR]?")
else:
    update = False

if update:
    xbmc.executebuiltin('RunAddon(script.megatvupdater)')
    xbmc.executebuiltin('Dialog.Close(all, true)')
else:	
    utils.LaunchSF()
    xbmc.executebuiltin('RunAddon(script.program.megatvbox)')

def checkDisabled():
    try:
        if xbmc.getCondVisibility('System.HasAddon(%s)' % utils.ADDONID) == 0:
            utils.DeleteKeymap(utils.KEYMAP_HOT)
            utils.DeleteKeymap(utils.KEYMAP_MENU)
            return True
    except:
        return False


class MyMonitor(xbmc.Monitor):
    def __init__(self):
        xbmc.Monitor.__init__(self)
        self.hotkey  = utils.ADDON.getSetting('HOTKEY')
        self.context = utils.ADDON.getSetting('CONTEXT')  == 'true'


    def onSettingsChanged(self):
        hotkey  = utils.ADDON.getSetting('HOTKEY')
        context = utils.ADDON.getSetting('CONTEXT')  == 'true'

        utils.VerifyKeymaps()

        if self.hotkey == hotkey and self.context == context:
            return

        self.hotkey  = hotkey
        self.context = context

        utils.UpdateKeymaps()


monitor = MyMonitor()

import xbmcgui
while (not xbmc.abortRequested):
    xbmc.sleep(1000)
    if checkDisabled():
        xbmc.sleep(1000)
        xbmc.executebuiltin('Action(reloadkeymaps)') 


checkDisabled()


del monitor