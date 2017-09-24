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
        function3
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] TBS (USA)[/COLOR][/B]', [
    '[B][COLOR=white]      TBS Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      TBS Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      TBS Link 3[/COLOR][/B]'])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]CerebroTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 


def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dTBS%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fc370dca571a8e9eeb48104236808fe8d.m3u8")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.weetv/?fanart=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fusflag.jpg&iconimage=http%3a%2f%2fwww.geetee.site%2fwizchannels%2fimages%2fus.png&mode=2&name=%20TBS%20%20s1%0d&url=https%3a%2f%2fstreaming1.streamlive.to%2flive%2feg5v0vdj33ls27r%2findex.m3u8%0d")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.streamztv/?url=url&mode=2&name=TBS&channelid=222&iconimage=https%3A%2F%2Fapp.uktvnow.net%2Fimages%2Fchannel_imgs%2F200116042625tbs.jpg%7CUser-Agent%3DDalvik%2F2.1.0+%28Linux%3B+U%3B+Android+6.0.1%3B+SM-G935F+Build%2FMMB29K%29")')
        
menuoptions()