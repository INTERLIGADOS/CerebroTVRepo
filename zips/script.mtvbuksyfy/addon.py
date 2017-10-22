import time
import xbmc
import os
import xbmcgui
import urllib2

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Sky SYFY Links[/COLOR][/B]', ['[B][COLOR=white]      Sky SYFY 1[/COLOR][/B]' , '[B][COLOR=white]      Sky SYFY 2[/COLOR][/B]' , '[B][COLOR=white]      Sky SYFY 3[/COLOR][/B]' , '[B][COLOR=white]      Sky SYFY 4[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        return func()
    else:
        func = funcs[call]
        return func()
    return 


def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.falconultratv/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Fstreamtype%3DTSDOWNLOADER%26amp%3Burl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2F15pUsZKUIw%2F4boblpukUd%2F251.ts%3Bname%3DCerebro+UK+SYFY&mode=12")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.FTFA/?action=play&url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2F15pUsZKUIw%2F4boblpukUd%2F251.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DF.T.F.A&content=0")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.falconultratv/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Fstreamtype%3DTSDOWNLOADER%26amp%3Burl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2F15pUsZKUIw%2F4boblpukUd%2F249.ts%3Bname%3DCerebro+UK+SYFY&mode=12")')
    
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.Milhano/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%253A%252F%252Fsecure.selling-team.net%252Flive%252FGiovanni.carrette%252FfvgrZeBaHw%252F73222.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26name%3DUK%253A%2520Syfy&mode=12")')
 

menuoptions()