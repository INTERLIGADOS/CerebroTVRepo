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
        
    call = dialog.select('[B][COLOR=yellow]CerebroTV[/COLOR][COLOR=red] UK Horror Channel Links[/COLOR][/B]', [
    '[B][COLOR=white]      Horror Channel  Link 1[/COLOR][/B]' ,
    '[B][COLOR=white]      Horror Channel  Link 2[/COLOR][/B]' ,
    '[B][COLOR=white]      Horror Channel  Link 3[/COLOR][/B] (May cut off every 3 mins)' ,
    '[B][COLOR=white]      Horror Channel  Link 4[/COLOR][/B] (May cut off every 3 mins)'])
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistLoader/?logos=&move=0&mode=32&index=1&url=http%3A%2F%2Fweekendpass.ddns.net%3A8080%2Flive%2FStewart_pitt%2Frdqot3iXvC%2F3772.ts&iconimage=&cache=0&name=Horror+Channel+2")')

def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistLoader/?logos=&move=0&mode=32&index=0&url=http%3A%2F%2Fweekendpass.ddns.net%3A8080%2Flive%2FRon_red%2FDISYh1Adi5%2F3772.ts&iconimage=&cache=0&name=Horror")')

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.exabytetv/?url=%24doregex%5Bexafilmon%5D&mode=17&regexs=%7Bu%27exafilmon%27%3A%20%7B%27expres%27%3A%20u%27%22high%22%2C%22url%22%3A%22%28.%2A%3F%29%22%27%2C%20%27referer%27%3A%20u%27http%3A//www.filmon.com%27%2C%20%27name%27%3A%20u%27exafilmon%27%2C%20%27agent%27%3A%20u%27Mozilla/5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_8_2%29%20AppleWebKit/537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome/44.0.2403.89%20Safari/537.36%27%2C%20%27page%27%3A%20u%27http%3A//www.filmon.com/api-v2/channel/836%27%7D%7D")')

def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.quantum/?url=https%3A%2F%2Fwww.filmon.com%2Ftv%2Fhorror-channel&mode=1201&name=%5BCOLORred%5DFreeview+%5B%2FCOLOR%5DHorror+Channel+%7C+FilmOn")')

menuoptions()