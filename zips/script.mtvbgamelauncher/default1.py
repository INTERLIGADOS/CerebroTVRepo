import os
import xbmc,xbmcaddon,subprocess
import urlparse
import xbmcgui
import resources.lib.utils as utils
from resources.lib.backup import XbmcBackup

def get_params():
    param = {}
    
    if(len(sys.argv) > 1):
        for i in sys.argv:
            args = i
            if(args.startswith('?')):
                args = args[1:]
            param.update(dict(urlparse.parse_qsl(args)))
            
    return param

#the program mode
mode = -1
params = get_params()


if("mode" in params):
    if(params['mode'] == 'backup'):
        mode = 0
    elif(params['mode'] == 'restore'):
        mode = 1

mode = 1;
#if mode wasn't passed in as arg, get from user
if(mode == -1):
    #figure out if this is a backup or a restore from the user
    mode = xbmcgui.Dialog().select(utils.getString(30010) + " " + utils.getString(30023),[utils.getString(30017)])

import os
import glob
files = glob.glob(xbmc.translatePath('special://temp/*.zip'))
for f in files:
    os.remove(f) 


import urllib2
import re
def getPublicIp():
    data = str(urllib2.urlopen('http://checkip.dyndns.com/').read())
    # data = '<html><head><title>Current IP Check</title></head><body>Current IP Address: 65.96.168.198</body></html>\r\n'

    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

#check if program should be run
if(mode != -1):
    #run the profile backup
    backup = XbmcBackup()

    if(mode == 2):
        #open the settings dialog
        utils.openSettings()
	
    elif(backup.remoteConfigured()):

        if(mode == backup.Restore):
            #get list of valid restore points
            xbmcgui.Dialog().ok("CerebroTV Updater","When you press OK some data will be         collected ready for the update.                                                     If you get an error please retry.")
            dialog = xbmcgui.Dialog()
            if dialog.yesno("[COLOR yellow]CerebroTV[/COLOR]","[COLOR yellow]The update will take about 1 hour to download[/COLOR]" , "[COLOR red]Once started DO NOT STOP IT![/COLOR]                                                                     [COLOR red]Your IP[/COLOR]:[COLOR yellow]"+getPublicIp()+"[/COLOR]                                                                    If any problems use this in report." , '[COLOR yellow]Do you want to stat the udpate now[/COLOR]','[COLOR red]NO[/COLOR]','[COLOR lime]YES[/COLOR]'):
                dummyvalue="yes"
            else:
                exit()				
            restorePoints = backup.listBackups()
            if restorePoints:
                dummyvalue="yes"
            else:
                xbmcgui.Dialog().ok(utils.getString(30010),"[COLOR yellow]Update Server seems[/COLOR] [COLOR red]offline![/COLOR]                                           Please Try Later!                                                                                     Check out Facebook page for more info.")
                exit()

            pointNames = []
            folderNames = []
            pointNames =["[COLOR yellow] >> SELECT ME TO CONTINUE OR PRESS BACK BUTTON TO CANCLE << [/COLOR]"]            
            for aDir in restorePoints:
                #pointNames.append(aDir[1])
                folderNames.append(aDir[0])
                #xbmcgui.Dialog().ok(folderNames[0],"plz")
            selectedRestore = -1

            if("archive" in params):
                #check that the user give archive exists
                if(params['archive'] in folderNames):
                    #set the index
                    selectedRestore = folderNames.index(params['archive'])
                    utils.log(str(selectedRestore) + " : " + params['archive'])
                else:
                    utils.showNotification(utils.getString(30045))
                    utils.log(params['archive'] + ' is not a valid restore point')
            else:
                #allow user to select the backup to restore from
                selectedRestore = xbmcgui.Dialog().select(utils.getString(30010) + " - " + utils.getString(30021),pointNames)

            if(selectedRestore != -1):
                backup.selectRestore(restorePoints[selectedRestore][0])

        				
        backup.run(mode)
    else:
        #can't go any further
        xbmcgui.Dialog().ok("CerebroTV","There has been an error.")
        xbmc.executebuiltin('RunAddon(script.program.sendlog)')
        import os
        import glob
        files = glob.glob(xbmc.translatePath('special://temp/*.zip'))
        for f in files:
            os.remove(f) 

        xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
        xbmc.executebuiltin('Dialog.Close(all, true)')
