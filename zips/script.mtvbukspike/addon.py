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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] UK Spike Channel Links[/COLOR][/B]', [
    '[B][COLOR=white]      Spike Channel  Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Spike Channel  Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      Spike Channel  Link 3[/COLOR][/B]' ,
    '[B][COLOR=white]      Spike Channel  Link 4[/COLOR][/B]'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.livehub2/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dSpike%20UK%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2f3036779a6ef01d9c0da3b7e139a6445d.m3u8")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.streamztv/?url=url&mode=2&name=Spike+UK&channelid=289&iconimage=https%3A%2F%2Fapp.uktvnow.net%2Fimages%2Fchannel_imgs%2F290616022506spike.jpg%7CUser-Agent%3DDalvik%2F2.1.0+%28Linux%3B+U%3B+Android+6.0.1%3B+SM-G935F+Build%2FMMB29K%29")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2Fthaiweb12.mine.nu%3A8000%2Flive%2Fwebtro2%2FOdEsGsRYFX%2F700.ts&mode=12")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2F62.210.141.126%3A8080%2Fspike%2Fmpegts&mode=12")')

menuoptions()