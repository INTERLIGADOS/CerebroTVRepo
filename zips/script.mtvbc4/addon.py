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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dChannel%204%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fe77d2afa4363dad35c713745802d7bee.m3u8")')
    
def function3():
    xbmc.executebuiltin('PlayMedia("plugin://program.apollo/?action=apollo&imdb=9999&season=1681&title=1681")')


menuoptions()