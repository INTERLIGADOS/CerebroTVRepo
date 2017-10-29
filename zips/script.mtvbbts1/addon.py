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
        function4,
        function5
        )
        
    call = dialog.select('[B][COLOR=yellow]Cerebro TV Box[/COLOR][COLOR=red] BT Sports 1 Links[/COLOR][/B]', [
    '[B][COLOR=white]      BT Sports 1 Link 1[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 1 Link 2[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 1 Link 3[/COLOR][/B]', 
    '[B][COLOR=white]      BT Sports 1 Link 4[/COLOR][/B]',
    '[B][COLOR=white]      BT Sports 1 Link 5[/COLOR][/B]'])
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33RaaabB3eETtiyiy-1%2FStrm%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=BT+Sports+1&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Fbt_sports.jpg&description=")')
  
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.falconproject/?action=play&url=%3Csublink+name%3D%22Link+1%22%3Eplugin%3A%2F%2Fplugin.video.SportsDevil%2F%3Fmode%3D1%26amp%3Bitem%3Dcatcher%253dstreams%2526url%3Dhttp%3A%2F%2Fwizhdsports.is%2Flive_streaming%2Fbtsports1%3C%2Fsublink%3E%3Csublink+name%3D%22Link+2%22%3Eplugin%3A%2F%2Fplugin.video.SportsDevil%2F%3Fmode%3D1%26amp%3Bitem%3Dcatcher%253dstreams%2526url%3Dhttp%3A%2F%2Fsstream.net%2Fbt1.html%3C%2Fsublink%3E%3Csublink+name%3D%22Link+3%22%3Eplugin%3A%2F%2Fplugin.video.SportsDevil%2F%3Fmode%3D1%26amp%3Bitem%3Dcatcher%253dstreams%2526url%3Dhttp%3A%2F%2Funblocked.lol%2Funblocked%2Fsportsphp%2Fbt1.php%3C%2Fsublink%3E&content=0")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ukturk/?url=http%3A%2F%2Faddoncloud.org%2Fukturk%2FUKTurk%2FSportsList.txt&mode=3&name=BT+Sport+1&description=&iconimage=http%3A%2F%2Fwww.liveonlinetv247.info%2Fimages%2Fbtsport1.png")')
  
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=922&title=922")')

def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.supremacy/?fanart=http%3a%2f%2fstephen-builds.uk%2fart%2f20839702_10207884860798337_363786087_o.jpg&mode=30&name=%5bCOLOR%20aqua%5dBT%20SPORT%201%5b%2fCOLOR%5d&url=%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2funblocked.lol%2funblocked%2fsportsphp%2fbt1.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fabcast.me%2fbtsport1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fvercanalestv.com%2ftv%2fdeportes%2fbt-sport-1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.liveonlinetv247.info%2fbtsport1.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2ftv.b-c-e.us%2fBTSport1.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fsstream.net%2fbt1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fwww.sdwnet.me%2fchannels%2fBT-Sport-1.html%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fcricfree.sc%2fiframe%2fcricfree%2fiframe7.php%23%0d%0asublink%3aplugin%3a%2f%2fplugin.video.SportsDevil%2f%3fmode%3d1%26item%3dcatcher%253dstreams%2526url%3dhttp%3a%2f%2fmamahd.in%2fp%2fmama2.php%3fid%3d17811%23%0d%0a")')

xbmc.executebuiltin("Notification([COLOR=gold]CerebroTV[/COLOR],Some Streams May Take 30 Seconds to Start Playing, ..,7000,)")      
menuoptions()