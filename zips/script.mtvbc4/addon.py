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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] Channel 4 Links[/COLOR][/B]', [
    '[B][COLOR=green]      Channel 4 Link 1[/COLOR][/B]' ,
    '[B][COLOR=green]      Channel 4 Link 2[/COLOR][/B]' ,
    '[B][COLOR=green]      Channel 4 Link 3[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvplayer/?url=92&mode=200&name=%5BCOLOR+royalblue%5DChannel+4%5B%2FCOLOR%5D+-+%5BCOLOR+white%5DCome+Dine+with+Me%5B%2FCOLOR%5D&iconimage=https%3A%2F%2Fassets.tvplayer.com%2Fcommon%2Flogos%2F256%2FColour%2F92.png&description=Four+residents+of+Shropshire+battle+it+out+in+the+dinner-party+challenge.+Yvonne+hopes+her+first-class+dining+experience+will+impress%2C+but+one+guest+refuses+to+eat+her+dessert%2C+while+one+of+her%27+attention-distracting+handstands+lands+her+on+her+back+in+the+kitchen+of+interior+architect+student+Olu.+Natsai+serves+up+a+mammoth+meat-fest+she+claims+to+resemble+The+Lion+King+on+a+plate+-+much+to+the+horror+of+everyone.&genre=Entertainment")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.nemesis/?url=http%3A%2F%2Fwww.sdw-net.me%2Fchannels%2FChannel-4.html&mode=50&name=%5BCOLOR+skyblue%5DChannel+4%5B%2FCOLOR%5D&iconimage=http%3A%2F%2Fwww.sdw-net.me%2Fproduct_images%2Fs%2F715%2Fchannel4__56690_thumb.jpg&fanart=C%3A%5CUsers%5Cbigla%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.nemesis%5Cfanart.jpg")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?url=http%3A%2F%2F95.154.237.88%3A8080%2FMatH33Raaakchenl-4%2FStrm%2Findex.m3u8%7CUser-Agent%3DAppleCoreMedia%2F1.0.0.13A452+%28iPhone%3B+U%3B+CPU+OS+9_0_2+like+Mac+OS+X%3B+en_gb%29&mode=9999&name=Channel+4+UK&iconimage=http%253A%252F%252Fsmarterlogix.com%252FiosSecureApps%252FPakIndiaTVHD%252FV1-2%252FImages%252Ffootball.jpg&description=")')


menuoptions()