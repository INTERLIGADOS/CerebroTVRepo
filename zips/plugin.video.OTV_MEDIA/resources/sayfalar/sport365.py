# -*- coding: utf-8 -*-
from resources.lib.otvhelper import * 
SITE_IDENTIFIER = 'sport365'
SITE_NAME = 'sport365'

import os
import re
import sys
import base64
import re
import datetime
import urllib
from HTMLParser import HTMLParser
  
from resources.lib.httpkir import httptools
from resources.lib.httpkir import jsontools
from resources.lib.httpkir import scrapertools
from resources.lib.httpkir import logger
from resources.lib.httpkir import config
from resources.lib.platformcode import platformtools
from resources.lib import jscrypto
from resources.lib.httpkir.item import Item
item = Item().fromurl(sys.argv[2])

host = "http://www.sport365.live/en/main"


def mainlist():
    oGui = cGui()
                  
    tarzlistesi= []                
    tarzlistesi.append(("Schedule", "http://www.sport365.live/en/events/-/1/-/-/60", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    tarzlistesi.append(("Live", "http://www.sport365.live/en/events/1/-/-/-/-", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    tarzlistesi.append(("Schedule by language", "http://www.sport365.live/en/sidebar", "http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg"))
    
               
    for sTitle,sUrl,sPicture in tarzlistesi:
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sThumbnail', sPicture)
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == 'Schedule by language':
             oGui.addMovie(SITE_IDENTIFIER, 'languages', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        else:
             oGui.addMovie(SITE_IDENTIFIER, 'tickets', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()

   
    




def agendaglobal(item):
    itemlist = []    
    try:
        item.channel = "sport365"
        item.url = "http://www.sport365.live/en/events/-/1/-/-/60"
        item.thumbnail="http://i.imgur.com/hJ2vhip.png"
        item.fanart="http://i.imgur.com/bCn8lHB.jpg?1"
        itemlist = tickets(item)
        for item_global in itemlist:
            if item_global.action == "":
                itemlist.remove(item_global)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("{0}".format(line))
        return []

    return itemlist


def tickets():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)

    color = 'blue'

    fechas = scrapertools.find_multiple_matches(data, '<td colspan=9[^>]+>(\d+\.\d+\.\d+)<')
    if "Redifusiones" in item.title and not fechas:
        itemlist.append(item.clone(action="", title="No currently scheduled"))
        return itemlist

    for i, f in enumerate(fechas):
        delimit = '</table>'
        if i != len(fechas) - 1:
            delimit = fechas[i+1]
        bloque = scrapertools.find_single_match(data, '%s<(.*?)%s' % (f, delimit))
        patron = 'onClick=.*?,\s*"([^"]+)".*?<td rowspan=2.*?src="([^"]+)".*?<td rowspan=2.*?>(\d+:\d+)<' \
                 '.*?<td.*?>([^<]+)<.*?<td.*?>(.*?)/td>.*?<tr.*?<td colspan=2.*?>([^<]+)<'
        matches = scrapertools.find_multiple_matches(bloque, patron)
        for url, thumb, hora, title, datos, deporte in matches:
            evento = title.replace("-", "vs")
            text_color = "red"
            if "green-big.png" in thumb:
                thumb= "http://mareeg.com/wp-content/uploads/2017/02/LIVE.png"
                text_color = "lime"
                
            if "/" in deporte:
                deporte = deporte.split(" /", 1)[0]
            if "<span" in datos:
                calidad, idioma = scrapertools.find_single_match(datos, '>([^<]+)</span>([^<]+)<')
                datos = "%s/%s/%s" % (deporte, calidad.replace("HQ", "HD"), idioma)
                if idioma == "Dutch" and color:
                    text_color = color
            else:
                datos = "%s/%s" % (deporte, datos[:-1])
                if "Dutch" in datos and color:
                    text_color = color


            fecha = f.replace(".", "/")

            url = jsontools.load_json(base64.b64decode(url))
            try:
                url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
            except:
                key = getkey(True)
                url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
            sUrl = "http://www.sport365.live" + url.replace('\\/','/').replace('"',"")
            horas, minutos = hora.split(":")
            dia, mes, year = fecha.split("/")
            fecha_evento = datetime.datetime(int(year), int(mes), int(dia),
                                             int(horas), int(minutos))
            fecha_evento = fecha_evento + datetime.timedelta(hours=1)
            hora = fecha_evento.strftime("%H:%M")
            date = fecha_evento.strftime("%d/%m")
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(title))
            if len(fechas) == 1:
                sTitle = "[COLOR %s]%s - %s [/COLOR][COLOR darkorange](%s)[/COLOR]" % (text_color, hora, title, datos)
                
                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
            else:
                sTitle = "[COLOR %s][%s] %s - %s[/COLOR] [COLOR darkorange](%s)[/COLOR]" % (text_color, date, hora, title, datos)
                
                oGui.addTV(SITE_IDENTIFIER, 'findvideos',  sTitle, '', thumb, '', oOutputParameterHandler)
    oGui.setEndOfDirectory()                         

    


def languages():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)
    
    matches = scrapertools.find_multiple_matches(data, "<option value='([0-9]+)'>.*?\/\s*(.*?)<")
    for value, sTitle in matches:
        sUrl = "http://www.sport365.live/en/events/-/1/-/%s/60" % value
        sTitle =alfabekodla(sTitle)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        if sTitle == "Dutch":
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'tickets', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 


def findvideos():
    oGui = cGui()
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    info= oInputParameterHandler.getValue('sMovieTitle')
    data = httptools.downloadpage(url).data
    data = re.sub(r"\n|\r|\t|\s{2}|&nbsp;","",data)

    if "The references of the transmission will be published" in data:
        itemlist.append(item.clone(title="The links will be available between 5-10 minutes before it starts.", action=""))
        return itemlist

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)

    matches = scrapertools.find_multiple_matches(data, "<span id='span_watch_links'.*?, '([^']+)'")
    if not matches:
        matches = scrapertools.find_multiple_matches(data, "<span id='span_code_links'.*?, '([^']+)'")
    h = HTMLParser()
    for i, url in enumerate(matches):
        url = jsontools.load_json(base64.b64decode(url))
        try:
            url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
        except:
            key = getkey(True)
            url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
        data_url = url.replace('\\/','/').replace("\\", "")
        data_url = h.unescape(data_url)

        sUrl = scrapertools.find_single_match(data_url, 'src=[\'"](.*?)"')
        sTitle = "[COLOR green]Stream %s - [/COLOR][COLOR darkorange](%s)[/COLOR]" % (i+1, info)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, 'play', sTitle, 'genres.png', oOutputParameterHandler)

    
    oGui.setEndOfDirectory() 
    

def play():
    itemlist = []
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sTitle= oInputParameterHandler.getValue('sMovieTitle')
    data = httptools.downloadpage(url).data
    url = scrapertools.find_single_match(data, '<iframe.*?src="([^"]+)"')
    if not url:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []
    elif "/matras.jpg" in data:
        platformtools.dialog_notification("Stream error", "Try again after a few minutes")
        return []
    
    h = HTMLParser()
    url = h.unescape(url)
    data = httptools.downloadpage(url).data
    f = scrapertools.find_single_match(data, 'name="f" value="([^"]+)"')
    d = scrapertools.find_single_match(data, 'name="d" value="([^"]+)"')
    r = scrapertools.find_single_match(data, 'name="r" value="([^"]+)"')
    url_post = scrapertools.find_single_match(data, "'action',\s*'([^']+)'")
    if not url_post:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []

    post = {'r': r, 'd':d, 'f':f}
    post = urllib.urlencode(post)
    data = httptools.downloadpage(url_post, post).data
    try:
        get_links(data)
    except:
        pass

    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save:
        key = getkey()
    else:
        key = base64.b64decode(key_save)
    data_crypto = scrapertools.find_single_match(data, "\};[A-z0-9]{43}\(.*?,.*?,\s*'([^']+)'")
    url = jsontools.load_json(base64.b64decode(data_crypto))
    try:
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))
    except:
        key = getkey(True)
        url = jscrypto.decode(url["ct"], key, url["s"].decode("hex"))  
        
    url = url.replace('\\/', '/').replace("\\", "").replace('"', "")
    headers_test = {'Referer': url_post, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True)
    if response.code == 406:
        response = httptools.downloadpage(url, headers=headers_test, follow_redirects=False, only_headers=True, replace_headers=True, cookies=False)
    if response.code == 406:
        platformtools.dialog_notification("Stream not available", "It is not possible to connect to the broadcast")
        return []
    url += "ndex.m3u8|Referer=%s&User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X)" % url_post
    sTitle =  alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(url)
                

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def getkey(overwrite=False):
    data = httptools.downloadpage(host).data

    js = scrapertools.find_multiple_matches(data, 'src="(http://s1.medianetworkinternational.com/js/[A-z0-9]{32}.js)')
    data_js = httptools.downloadpage(js[-1]).data

    str_wise = scrapertools.find_single_match(data_js, ".join\(''\);\}\('(.*?)\)\);")
    while True:
        result = decrypt(str_wise)
        if not "w,i,s,e" in result:
            break
        str_wise = scrapertools.find_single_match(result, ".join\(''\);\}\('(.*?)\)\);")

    
    key = scrapertools.find_single_match(result, 'return "([^"]+)"')
    key_save = config.get_setting("key_cryp", "sport365")
    if not key_save or overwrite:
        key_save = config.set_setting("key_cryp", base64.b64encode(key), "sport365")    

    return key


def decrypt(data):
    cadena1, cadena2, cadena3, cadena4 = data.split("','")
    cadena4 = cadena4.replace("'", "")
    j = 0
    c = 0
    i = 0
    list1 = []
    list2 = []
    while True:
        if j < 5:
            list2.append(cadena1[j])
        else:
            if j < len(cadena1):
                list1.append(cadena1[j])
        j += 1
        if c < 5:
            list2.append(cadena2[c])
        else:
            if c < len(cadena2):
                list1.append(cadena2[c])
        c += 1
        if i < 5:
            list2.append(cadena3[i])
        else:
            if i < len(cadena3):
                list1.append(cadena3[i])
        i += 1
        if (len(cadena1) + len(cadena2) + len(cadena3) + len(cadena4)) == (len(list1) + len(list2) + len(cadena4)):
            break
    cadena5 = "".join(list1)
    cadena6 = "".join(list2)
    c = 0
    resultado = []
    j = 0
    for j in range(0, len(list1), 2):
        operando = -1
        if (ord(cadena6[c]) % 2):
            operando = 1

        try:
            resultado.append(chr(int(cadena5[j:j+2], 36) - operando))
        except:
            pass
        c += 1
        if c >= len(list2):
            c = 0
    result = "".join(resultado)

    return result


def get_links(data):
    adshell = scrapertools.find_single_match(data, "<script src=[\"'](http://tags2.adshell.net.*?)['\"]")
    data_shell = httptools.downloadpage(adshell).data

    url = scrapertools.find_single_match(data_shell, ",url:'([^']+)'")
    headers = {'Referer': adshell}
    data = httptools.downloadpage(url, headers=headers).data
