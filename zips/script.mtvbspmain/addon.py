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
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV[/COLOR][COLOR=red] Sky Sports Main Event Links[/COLOR][/B]', [
    '[B][COLOR=white]      Sky Sports Main Event Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      Sky Sports Main Event Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSky%20Sport%20Main%20Event%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f09e05360bef651699a48ee86801c0dfd.m3u8")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.OTV_MEDIA/?function=play__liveonlinetv24&sCat=6&sFav=play__liveonlinetv24&sId=liveonlinetv247&sMovieTitle=Sky%20Sports%20Main%20Event&site=liveonlinetv247&siteUrl=http%3a%2f%2fwww.liveonlinetv247.info%2fwatch.php%3ftitle%3dSky%20Sports%20Main%20Event%26channel%3dskysportsmainevent&title=Sky%20Sports%20Main%20Event")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?url=plugin%3A%2F%2Fplugin.video.f4mTester%2F%3Furl%3Dhttp%3A%2F%2Fmagportal.ddns.net%3A25461%2Flive%2Fultra123%2Fultra123%2F277.ts%26amp%3Bstreamtype%3DTSDOWNLOADER%26amp%3Bname%3DSUPREMACY%0D&mode=12")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectMayhem/?fanart=http%3a%2f%2falexcallejon.tv%2fwp-content%2fuploads%2f2016%2f01%2f01.jpg&iconimage=http%3a%2f%2fgreyhound-blandford.co.uk%2fwp-content%2fuploads%2f2014%2f12%2fskySportslogo.jpg&mode=30&name=%5bCOLOR%20lime%5dSky%20Sports%20Main%20Event%5b%2fCOLOR%5d&url=%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama.php%3fid%3d17804%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.liveonlinetv247.info%2fembed%2fskysports1.php%3fwidth%3d650%26height%3b%3d480%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.sdwnet.me%2fchannels%2fSky-Sports1.html%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fsky-sports-main-event-live-stream%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.livetv-free.com%2fsky-sports-1.php%23%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fsky1.html%23%0a")')     

    
menuoptions()