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
        function5,
        function6,
        function7,
        function8,
        function9,
        function10
        )
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] BBC 1 Links[/COLOR][/B]', 
    [
    '[B][COLOR=green]      BBC1 HD[/COLOR] Link 1[/B]' , 
    '[B][COLOR=green]      BBC1 HD[/COLOR] Link 2[/B]', 
    '[B][COLOR=green]      BBC1 SD[/COLOR][/B] (No Geo Lock)',
    '[B][COLOR=green]      BBC1 HD[/COLOR][/B] (No Geo Lock) (NO UK BLOCK ON HD)',
    '[B][COLOR=green]      BBC1 London HD[/COLOR][/B]',
    '[B][COLOR=green]      BBC1 NI HD[/COLOR][/B]',
    '[B][COLOR=green]      BBC1 Scotland HD[/COLOR][/B]',
    '[B][COLOR=green]      BBC1 Wales HD[/COLOR][/B]',
    '[B][COLOR=green]      BBC1 Regional HD[/COLOR][/B]',
    '[B][COLOR=green]      BBC1 Red Button[/COLOR][/B]'
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-10]
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


def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_one_hd&mode=203&name=BBC+One&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_one.png&description=&subtitles_url=&logged_in=False")')

def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.freeview/?url=http%3A%2F%2Fvs-hls-uk-live.akamaized.net%2Fpool_30%2Flive%2Fbbc_one_hd%2Fbbc_one_hd.isml%2Fbbc_one_hd-pa4%253d128000-video%253d5070016.m3u8&mode=1&name=BBC+One+HD")')

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.livehub/?description&iconimage=http%3a%2f%2fgeekpeaksoftware.com%2fwp-content%2fuploads%2f2016%2f10%2fmobdro.png&mode=10&name=%5bB%5d%5bCOLOR%20white%5dBBC%20One%5b%2fCOLOR%5d%5b%2fB%5d&url=mpd%3a%2f%2fa8f14a834d2d09054715803924e798b2.m3u8",return)')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.ProjectCypher/?url=http%3A%2F%2Fthaiweb12.mine.nu%3A8000%2Flive%2Fwebtro2%2FOdEsGsRYFX%2F691.ts&mode=12")')

def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_one_london&mode=203&name=BBC+One+London&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_one.png&description=&subtitles_url=&logged_in=False")')

def function6():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_one_northern_ireland_hd&mode=203&name=BBC+One+Northern+Ireland&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_one_northern_ireland.png&description=&subtitles_url=&logged_in=False")')

def function7():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_one_scotland_hd&mode=203&name=BBC+One+Scotland&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_one_scotland.png&description=&subtitles_url=&logged_in=False")')

def function8():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.iplayerwww/?url=bbc_one_wales_hd&mode=203&name=BBC+One+Wales&iconimage=C%3A%5CUsers%5Cbiglad%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.iplayerwww%5Cmedia%5Cbbc_one_wales.png&description=&subtitles_url=&logged_in=False")')

def function9():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.program.super.favourites/?label=bbc&mode=400&path=special%3A%2F%2Fprofile%2Faddon_data%2Fplugin.program.super.favourites%2FSuper%20Favourites%5Cbbc&sf_options=fanart%3Dspecial%3A%2F%2Fhome%2Faddons%5Cplugin.program.super.favourites%5Cfanart.jpg%26_options_sf",return)')

def function10():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.iplayerwww/?description&iconimage=C%3a%5cUsers%5cbigla%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.iplayerwww%5cmedia%5ctv.png&logged_in=False&mode=118&name=Red%20Button&subtitles_url&url=url",return)')
      
menuoptions()