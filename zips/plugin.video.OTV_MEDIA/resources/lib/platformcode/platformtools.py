# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# platformtools
# ------------------------------------------------------------
# Herramientas responsables de adaptar los diferentes 
# cuadros de dialogo a una plataforma en concreto,
# en este caso Kodi.
# version 2.0
# ------------------------------------------------------------

import re
import os
import sys
import urllib

import xbmc
import xbmcgui
import xbmcplugin
from resources.lib.httpkir import config
from resources.lib.httpkir import logger
from resources.lib.httpkir.item import Item

DEBUG = config.get_setting("debug")


def dialog_ok(heading, line1, line2="", line3=""):
    dialog = xbmcgui.Dialog()
    return dialog.ok(heading, line1, line2, line3)


def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    dialog = xbmcgui.Dialog()
    l_icono = xbmcgui.NOTIFICATION_INFO, xbmcgui.NOTIFICATION_WARNING, xbmcgui.NOTIFICATION_ERROR
    dialog.notification(heading, message, l_icono[icon], time, sound)


def dialog_yesno(heading, line1, line2="", line3="", nolabel="No", yeslabel="Si", autoclose=""):
    dialog = xbmcgui.Dialog()
    if autoclose:
        return dialog.yesno(heading, line1, line2, line3, nolabel, yeslabel, autoclose)
    else:
        return dialog.yesno(heading, line1, line2, line3, nolabel, yeslabel)


def dialog_select(heading, _list):
    return xbmcgui.Dialog().select(heading, _list)


def dialog_progress(heading, line1, line2="", line3=""):
    dialog = xbmcgui.DialogProgress()
    dialog.create(heading, line1, line2, line3)
    return dialog


def dialog_progress_bg(heading, message=""):
    dialog = xbmcgui.DialogProgressBG()
    dialog.create(heading, message)
    return dialog


def dialog_input(default="", heading="", hidden=False):
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return keyboard.getText()
    else:
        return None


def dialog_numeric(_type, heading, default=""):
    dialog = xbmcgui.Dialog()
    dialog.numeric(_type, heading, default)
    return dialog


def itemlist_refresh():
    xbmc.executebuiltin("Container.Refresh")


def itemlist_update(item):
    xbmc.executebuiltin("Container.Update(" + sys.argv[0] + "?" + item.tourl() + ")")


def render_items(itemlist, parent_item):
    """
    Función encargada de mostrar el itemlist en kodi, se pasa como parametros el itemlist y el item del que procede
    @type itemlist: list
    @param itemlist: lista de elementos a mostrar

    @type parent_item: item
    @param parent_item: elemento padre
    """
    # Si el itemlist no es un list salimos
    if not type(itemlist) == list:
        if config.get_platform() == "boxee":
          xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)
        return

    # Si no hay ningun item, mostramos un aviso
    if not len(itemlist):
        itemlist.append(Item(title="There are no items to show"))

    # Recorremos el itemlist
    for item in itemlist:

        # Si el item no contiene categoria,le ponemos la del item padre
        if item.category == "":
            item.category = parent_item.category

        # Si el item no contiene fanart,le ponemos la del item padre
        if item.fanart == "":
            item.fanart = parent_item.fanart

        # Formatear titulo
        if item.text_color:
            item.title = '[COLOR %s]%s[/COLOR]' % (item.text_color, item.title)
        if item.text_blod:
            item.title = '[B]%s[/B]' % item.title
        if item.text_italic:
            item.title = '[I]%s[/I]' % item.title

        # IconImage para folder y video
        if item.folder:
            icon_image = "DefaultFolder.png"
        else:
            icon_image = "DefaultVideo.png"

        # Creamos el listitem
        listitem = xbmcgui.ListItem(item.title, iconImage=icon_image, thumbnailImage=item.thumbnail)

        # Ponemos el fanart
        if item.fanart:
          listitem.setProperty('fanart_image', item.fanart)
        else:
          listitem.setProperty('fanart_image', os.path.join(config.get_runtime_path(), "fanart.jpg"))                  
                             

        # TODO: ¿Se puede eliminar esta linea? yo no he visto que haga ningun efecto.
        xbmcplugin.setPluginFanart(int(sys.argv[1]), os.path.join(config.get_runtime_path(), "fanart.jpg"))

        # Añadimos los infoLabels
        set_infolabels(listitem, item)

        # Montamos el menu contextual
        context_commands = set_context_commands(item, parent_item)

        # Añadimos el item
        if config.get_platform() == "boxee":
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='%s?%s' % (sys.argv[0], item.tourl()),
                                        listitem=listitem, isFolder=item.folder)
        else:
            listitem.addContextMenuItems(context_commands, replaceItems=True)
            
            if not item.totalItems: item.totalItems = 0
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='%s?%s' % (sys.argv[0], item.tourl()),
                                        listitem=listitem, isFolder=item.folder,
                                        totalItems=item.totalItems)

    # Vista 5x3 hasta llegar al listado de canales
    if parent_item.channel not in ["channelselector", ""]:
        xbmcplugin.setContent(int(sys.argv[1]), "movies")

    # Fijamos el "breadcrumb"
    xbmcplugin.setPluginCategory(handle=int(sys.argv[1]), category=parent_item.category.capitalize())

    # No ordenar items
    xbmcplugin.addSortMethod(handle=int(sys.argv[1]), sortMethod=xbmcplugin.SORT_METHOD_NONE)

    # Viewmodes:
    # Creo que es mas lógico que al item se le especifique que vista tendra al abrirlo.
    # El cambio puede provocar que algun canal no muestre los items en la vista deseada, pero es mejor ir corrigiendolo
    # que arrastrar algo que no tiene sentido
    if config.get_setting("forceview") == "true":
        if parent_item.viewmode == "list":
            xbmc.executebuiltin("Container.SetViewMode(50)")
        elif parent_item.viewmode == "movie_with_plot":
            xbmc.executebuiltin("Container.SetViewMode(503)")
        elif parent_item.viewmode == "movie":
            xbmc.executebuiltin("Container.SetViewMode(500)")

    # Cerramos el directorio
    xbmcplugin.endOfDirectory(handle=int(sys.argv[1]), succeeded=True)


def set_infolabels(listitem, item):
    """
    Metodo para pasar la informacion al listitem (ver tmdb.set_InfoLabels() )
    item.infoLabels es un dicionario con los pares de clave/valor descritos en:
    http://mirrors.xbmc.org/docs/python-docs/14.x-helix/xbmcgui.html#ListItem-setInfo
    @param listitem: objeto xbmcgui.ListItem
    @type listitem: xbmcgui.ListItem
    @param item: objeto Item que representa a una pelicula, serie o capitulo
    @type item: item
    """
    if item.infoLabels:
      listitem.setInfo("video", item.infoLabels)
      
    if listitem.getProperty("path"):
        if item.fulltitle:
            listitem.setInfo("video", {"Title": item.fulltitle})
        else:
            listitem.setInfo("video", {"Title": item.title})
        
    # Añadido para Kodi Krypton (v17)
    if int(xbmc.getInfoLabel("System.BuildVersion").split(".", 1)[0]) > 16:
      listitem.setArt({"poster": item.thumbnail})


def set_context_commands(item, parent_item):
    """
    Función para generar los menus contextuales.
        1. Partiendo de los datos de item.context
             a. Metodo antiguo item.context tipo str separando las opciones por "|" (ejemplo: item.context = "1|2|3")
                (solo predefinidos)
            b. Metodo list: item.context es un list con las diferentes opciones del menu:
                - Predefinidos: Se cargara una opcion predefinida con un nombre.
                    item.context = ["1","2","3"]

                - dict(): Se cargara el item actual modificando los campos que se incluyan en el dict() en caso de
                    modificar los campos channel y action estos serán guardados en from_channel y from_action.
                    item.context = [{"title":"Nombre del menu", "action": "action del menu", "channel",
                                    "channel del menu"}, {...}]

        2. Añadiendo opciones segun criterios
            Se pueden añadir opciones al menu contextual a items que cumplan ciertas condiciones

        3. Añadiendo opciones a todos los items
            Se pueden añadir opciones al menu contextual para todos los items

    @param item: elemento que contiene los menu contextuales
    @type item: item
    @param parent_item:
    @type parent_item: item
    """
    context_commands = []
    version_xbmc = int(xbmc.getInfoLabel("System.BuildVersion").split(".", 1)[0])

    # Creamos un list con las diferentes opciones incluidas en item.context
    if type(item.context) == str:
        context = item.context.split("|")
    elif type(item.context) == list:
        context = item.context
    else:
        context = []

    # Opciones segun item.context
    for command in context:
        # Formato dict
        if type(command) == dict:
            # Los parametros del dict, se sobreescriben al nuevo context_item en caso de sobreescribir "action" y
            # "channel", los datos originales se guardan en "from_action" y "from_channel"
            if "action" in command:
                command["from_action"] = item.action
            if "channel" in command:
                command["from_channel"] = item.channel
            context_commands.append(
                (command["title"], "XBMC.RunPlugin(%s?%s)" % (sys.argv[0], item.clone(**command).tourl())))

    # Opciones segun criterios
    if "info_partido" in item.context:
        try:
            name1, name2 = item.evento.split(" vs ")
            if re.search(r'(?i)futbol|fútbol|soccer|football', item.deporte):
                try:
                    from core import channeltools
                    modo = channeltools.get_channel_setting("modo", "futbol_window")
                except:
                    modo = False
                partidoCommand = "XBMC.RunPlugin(%s?%s)" % ( sys.argv[ 0 ] , item.clone(channel="futbol_window", action="ventana", maximiza=modo).tourl())
                context_commands.append(("Abrir info del partido", partidoCommand))
        except:
            import traceback
            logger.info(traceback.format_exc())

    # Ir al Menu Principal (channel.mainlist)
    if parent_item.channel not in ["novedades", "channelselector"] and item.action != "mainlist" \
            and parent_item.action != "mainlist":
        context_commands.append(("Ir al Menu Principal", "XBMC.Container.Refresh (%s?%s)" %
                                 (sys.argv[0], Item(channel=item.channel, action="mainlist").tourl())))

    # Abrir configuración
    if parent_item.channel not in ["configuracion", "novedades", "buscador"]:
        context_commands.append(("Abrir Configuración", "XBMC.Container.Update(%s?%s)" %
                                 (sys.argv[0], Item(channel="configuracion", action="mainlist").tourl())))

    # Añadir a Favoritos
    '''if item.channel not in ["channelselector", "favoritos", "descargas", "buscador", "biblioteca", "novedades", "ayuda",
                            "configuracion", ""] and not parent_item.channel == "favoritos":'''
    if version_xbmc < 17 and (item.channel not in ["favoritos", "biblioteca", "ayuda",
                                                   "configuracion", ""] and not parent_item.channel == "favoritos"):
        context_commands.append((config.get_localized_string(30155), "XBMC.RunPlugin(%s?%s)" %
                                 (sys.argv[0], item.clone(channel="favoritos", action="addFavourite",
                                                          from_channel=item.channel, from_action=item.action).tourl())))

    return sorted(context_commands, key=lambda comand: comand[0])


def is_playing():
    return xbmc.Player().isPlaying()


def play_video(item, strm=False):
    logger.info("deportesalacarta.platformcode.platformtools play_video")
    #logger.debug(item.tostring('\n'))

    if item.channel == 'descargas':
        logger.info("Reproducir video local: %s [%s]" % (item.title, item.url))
        playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
        playlist.clear()
        playlist.add(item.url)
        xbmc.Player().play(playlist)
        return

    default_action = config.get_setting("default_action")
    logger.info("default_action=" + default_action)

    # Abre el diálogo de selección para ver las opciones disponibles
    opciones, video_urls, seleccion, salir = get_dialogo_opciones(item, default_action, strm)
    if salir:
        return

    # se obtienen la opción predeterminada de la configuración del addon
    seleccion = get_seleccion(default_action, opciones, seleccion, video_urls)
    if seleccion < 0:  # Cuadro cancelado
        return

    logger.info("seleccion=%d" % seleccion)
    logger.info("seleccion=%s" % opciones[seleccion])

    # se ejecuta la opcion disponible, jdwonloader, descarga, favoritos, añadir a la biblioteca... SI NO ES PLAY
    salir = set_opcion(item, seleccion, opciones, video_urls)
    if salir:
        return

    # obtenemos el video seleccionado
    mediaurl, view, mpd = get_video_seleccionado(item, seleccion, video_urls)
    if mediaurl == "":
        return

    # se obtiene la información del video.
    xlistitem = xbmcgui.ListItem(path=mediaurl, thumbnailImage=item.thumbnail)
    set_infolabels(xlistitem, item)

    if mpd:
        xlistitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
        xlistitem.setProperty('inputstream.adaptive.manifest_type', 'mpd')

    # se lanza el reproductor
    info = False
    if "_ventana" in opciones[seleccion]:
        info = True
    set_player(item, xlistitem, mediaurl, view, strm, info)

    # si es un archivo de la biblioteca enviar a marcar como visto
    if strm or item.strm_path:
        from platformcode import library
        library.mark_auto_as_watched(item)


def get_seleccion(default_action, opciones, seleccion, video_urls):
    # preguntar
    if default_action == "0":
        # "Elige una opción"
        seleccion = dialog_select(config.get_localized_string(30163), opciones)
    # Ver en calidad baja
    elif default_action == "1":
        seleccion = 0
    # Ver en alta calidad
    elif default_action == "2":
        seleccion = len(video_urls) - 1
    # jdownloader
    elif default_action == "3":
        seleccion = seleccion
    else:
        seleccion = 0
    return seleccion


def show_channel_settings(list_controls=None, dict_values=None, caption="", callback=None, item=None,
                          custom_button=None, channelpath=None):
    """
    Muestra un cuadro de configuracion personalizado para cada canal y guarda los datos al cerrarlo.
    
    Parametros: ver descripcion en xbmc_config_menu.SettingsWindow
    @param list_controls: lista de elementos a mostrar en la ventana.
    @type list_controls: list
    @param dict_values: valores que tienen la lista de elementos.
    @type dict_values: dict
    @param caption: titulo de la ventana
    @type caption: str
    @param callback: función que se llama tras cerrarse la ventana.
    @type callback: str
    @param item: item para el que se muestra la ventana de configuración.
    @type item: Item
    @param custom_button: botón personalizado, que se muestra junto a "OK" y "Cancelar".
    @type custom_button: dict

    @return: devuelve la ventana con los elementos
    @rtype: SettingsWindow
    """
    from xbmc_config_menu import SettingsWindow
    return SettingsWindow("ChannelSettings.xml", config.get_runtime_path()) \
        .start(list_controls=list_controls, dict_values=dict_values, title=caption, callback=callback, item=item,
               custom_button=custom_button, channelpath=channelpath)

def alert_no_disponible_server(server):
    # 'El vídeo ya no está en %s' , 'Prueba en otro servidor o en otro canal'
    dialog_ok(config.get_localized_string(30055), (config.get_localized_string(30057) % server),
              config.get_localized_string(30058))


def alert_unsopported_server():
    # 'Servidor no soportado o desconocido' , 'Prueba en otro servidor o en otro canal'
    dialog_ok(config.get_localized_string(30065), config.get_localized_string(30058))


def handle_wait(time_to_wait, title, text):
    logger.info("handle_wait(time_to_wait=%d)" % time_to_wait)
    espera = dialog_progress(' ' + title, "")

    secs = 0
    increment = int(100 / time_to_wait)

    cancelled = False
    while secs < time_to_wait:
        secs += 1
        percent = increment * secs
        secs_left = str((time_to_wait - secs))
        remaining_display = ' Espera ' + secs_left + ' segundos para que comience el vídeo...'
        espera.update(percent, ' ' + text, remaining_display)
        xbmc.sleep(1000)
        if espera.iscanceled():
            cancelled = True
            break

    if cancelled:
        logger.info('Espera cancelada')
        return False
    else:
        logger.info('Espera finalizada')
        return True


def get_dialogo_opciones(item, default_action, strm):
    logger.info("platformtools get_dialogo_opciones")
    #logger.debug(item.tostring('\n'))
    from core import servertools

    opciones = []
    error = False

    try:
        item.server = item.server.lower()
    except AttributeError:
        item.server = ""

    if item.server == "":
        item.server = "directo"

    # Si no es el modo normal, no muestra el diálogo porque cuelga XBMC
    muestra_dialogo = (config.get_setting("player_mode") == "0" and not strm)

    # Extrae las URL de los vídeos, y si no puedes verlo te dice el motivo
    #Permitir varias calidades para server "directo"
    if item.video_urls:
      video_urls, puedes, motivo = item.video_urls, True, ""
    else:
      video_urls, puedes, motivo = servertools.resolve_video_urls_for_playing(
          item.server, item.url, item.password, muestra_dialogo)

    seleccion = 0
    # Si puedes ver el vídeo, presenta las opciones
    if puedes:
        for video_url in video_urls:
            opciones.append(config.get_localized_string(30151) + " " + video_url[0])

        if item.server == "local":
            opciones.append(config.get_localized_string(30164))
        else:
            opcion = config.get_localized_string(30153)
            opciones.append(opcion) # "Descargar"

            if item.channel=="favoritos": 
                opciones.append(config.get_localized_string(30154)) # "Quitar de favoritos"
            else:
                opciones.append(config.get_localized_string(30155)) # "Añadir a favoritos"

            if item.channel!="descargas":
                opciones.append(config.get_localized_string(30157))
            else:
                if item.category=="errores":
                    opciones.append(config.get_localized_string(30159)) # "Borrar descarga definitivamente"
                    opciones.append(config.get_localized_string(30160)) # "Pasar de nuevo a lista de descargas"
                else:
                    opciones.append(config.get_localized_string(30156)) # "Quitar de lista de descargas"

            if config.get_setting("jdownloader_enabled") == "true":
                # "Enviar a JDownloader"
                opciones.append(config.get_localized_string(30158))

        if default_action == "3":
            seleccion = len(opciones) - 1

    # Si no puedes ver el vídeo te informa
    else:
        if item.server != "":
            if "<br/>" in motivo:
                dialog_ok("No puedes ver ese vídeo porque...", motivo.split("<br/>")[0], motivo.split("<br/>")[1],
                          item.url)
            else:
                dialog_ok("No puedes ver ese vídeo porque...", motivo, item.url)
        else:
            dialog_ok("No puedes ver ese vídeo porque...", "El servidor donde está alojado no está",
                      "soportado en pelisalacarta todavía", item.url)

        if item.channel=="favoritos": 
            opciones.append(config.get_localized_string(30154)) # "Quitar de favoritos"

        if len(opciones) == 0:
            error = True

    return opciones, video_urls, seleccion, error


def set_opcion(item, seleccion, opciones, video_urls):
    logger.info("platformtools set_opcion")
    # logger.debug(item.tostring('\n'))
    salir = False
    # No ha elegido nada, lo más probable porque haya dado al ESC
    # TODO revisar
    if seleccion == -1:
        # Para evitar el error "Uno o más elementos fallaron" al cancelar la selección desde fichero strm
        listitem = xbmcgui.ListItem(item.title, iconImage="DefaultVideo.png", thumbnailImage=item.thumbnail)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), False, listitem)

    # "Enviar a JDownloader"
    if opciones[seleccion] == config.get_localized_string(30158):
        from core import scrapertools

        # TODO comprobar que devuelve 'data'
        if item.subtitle != "":
            data = scrapertools.cachePage(config.get_setting("jdownloader") + "/action/add/links/grabber0/start1/web=" +
                                          item.url + " " + item.thumbnail + " " + item.subtitle)
        else:
            data = scrapertools.cachePage(config.get_setting("jdownloader") + "/action/add/links/grabber0/start1/web=" +
                                          item.url + " " + item.thumbnail)
        salir = True

    elif opciones[seleccion]==config.get_localized_string(30164): # Borrar archivo en descargas
        # En "extra" está el nombre del fichero en favoritos
        os.remove( item.url )
        xbmc.executebuiltin( "Container.Refresh" )
        salir = True

    # Descargar
    elif opciones[seleccion]==config.get_localized_string(30153): # "Descargar"

        download_title = item.fulltitle
        if item.hasContentDetails=="true":
            download_title = item.contentTitle

        # El vídeo de más calidad es el último
        mediaurl = video_urls[len(video_urls)-1][1]

        from core import downloadtools
        keyboard = xbmc.Keyboard(download_title)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            download_title = keyboard.getText()
            devuelve = downloadtools.downloadbest(video_urls,download_title)
            
            if devuelve==0:
                advertencia = xbmcgui.Dialog()
                resultado = advertencia.ok("plugin" , "Descargado con éxito")
            elif devuelve==-1:
                advertencia = xbmcgui.Dialog()
                resultado = advertencia.ok("plugin" , "Descarga abortada")
            else:
                advertencia = xbmcgui.Dialog()
                resultado = advertencia.ok("plugin" , "Error en la descarga")
        salir = True

    elif opciones[seleccion]==config.get_localized_string(30159): #"Borrar descarga definitivamente"
        from channels import descargas
        descargas.delete_error_bookmark(urllib.unquote_plus( item.extra ))

        advertencia = xbmcgui.Dialog()
        resultado = advertencia.ok(config.get_localized_string(30101) , item.title , config.get_localized_string(30106)) # 'Se ha quitado de la lista'
        xbmc.executebuiltin( "Container.Refresh" )
        salir = True

    elif opciones[seleccion]==config.get_localized_string(30160): #"Pasar de nuevo a lista de descargas":
        from channels import descargas
        descargas.mover_descarga_error_a_pendiente(urllib.unquote_plus( item.extra ))

        advertencia = xbmcgui.Dialog()
        resultado = advertencia.ok(config.get_localized_string(30101) , item.title , config.get_localized_string(30107)) # 'Ha pasado de nuevo a la lista de descargas'
        salir = True

    # "Quitar de favoritos"
    elif opciones[seleccion] == config.get_localized_string(30154):
        from channels import favoritos
        favoritos.delFavourite(item)
        salir = True

    # "Añadir a favoritos":
    elif opciones[seleccion] == config.get_localized_string(30155):
        from channels import favoritos
        item.from_channel = "favoritos"
        favoritos.addFavourite(item)
        salir = True

    elif opciones[seleccion]==config.get_localized_string(30156): #"Quitar de lista de descargas":
        # La categoría es el nombre del fichero en la lista de descargas
        from channels import descargas
        descargas.deletebookmark((urllib.unquote_plus( item.extra )))

        advertencia = xbmcgui.Dialog()
        resultado = advertencia.ok(config.get_localized_string(30101) , item.title , config.get_localized_string(30106)) # 'Se ha quitado de lista de descargas'

        xbmc.executebuiltin( "Container.Refresh" )
        salir = True

    elif opciones[seleccion]==config.get_localized_string(30157): #"Añadir a lista de descargas":
        from core import downloadtools

        download_title = item.fulltitle
        download_thumbnail = item.thumbnail
        download_plot = item.plot

        if item.hasContentDetails=="true":
            download_title = item.contentTitle
            download_thumbnail = item.contentThumbnail
            download_plot = item.contentPlot

        keyboard = xbmc.Keyboard(downloadtools.limpia_nombre_excepto_1(download_title))
        keyboard.doModal()
        if keyboard.isConfirmed():
            download_title = keyboard.getText()

            from channels import descargas
            descargas.savebookmark(titulo=download_title,url=item.url,thumbnail=download_thumbnail,server=item.server,plot=download_plot,fulltitle=download_title)

            advertencia = xbmcgui.Dialog()
            resultado = advertencia.ok(config.get_localized_string(30101) , download_title , config.get_localized_string(30109)) # 'se ha añadido a la lista de descargas'
        salir = True

    return salir


def get_video_seleccionado(item, seleccion, video_urls):
    logger.info("platformtools get_video_seleccionado")
    mediaurl = ""
    view = False
    wait_time = 0
    mpd = False

    # Ha elegido uno de los vídeos
    if seleccion < len(video_urls):
        mediaurl = video_urls[seleccion][1]
        if len(video_urls[seleccion]) > 4:
            wait_time = video_urls[seleccion][2]
            item.subtitle = video_urls[seleccion][3]
            mpd = True
        if len(video_urls[seleccion]) > 3:
            wait_time = video_urls[seleccion][2]
            item.subtitle = video_urls[seleccion][3]
        elif len(video_urls[seleccion]) > 2:
            wait_time = video_urls[seleccion][2]
        view = True

    # Si no hay mediaurl es porque el vídeo no está :)
    logger.info("deportesalacarta.platformcode.platformstools mediaurl=" + mediaurl)
    if mediaurl == "":
        if item.server == "unknown":
            alert_unsopported_server()
        else:
            alert_no_disponible_server(item.server)

    # Si hay un tiempo de espera (como en megaupload), lo impone ahora
    if wait_time > 0:
        continuar = handle_wait(wait_time, item.server, "Cargando vídeo...")
        if not continuar:
            mediaurl = ""

    return mediaurl, view, mpd


def set_player(item, xlistitem, mediaurl, view, strm, info):
    logger.info("platformtools set_player")
    logger.debug("item:\n" + item.tostring('\n'))

    # Movido del conector "torrent" aqui
    if item.server == "torrent":
        play_torrent(item, xlistitem, mediaurl)
        return

    # Si es un fichero strm no hace falta el play
    elif strm:
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, xlistitem)
        if item.subtitle != "":
            xbmc.sleep(2000)
            xbmc.Player().setSubtitles(item.subtitle)

    else:
        logger.info("player_mode=" + config.get_setting("player_mode"))
        logger.info("mediaurl=" + mediaurl)
        if item.server == "p2p" and info:
            from platformcode import windowinfo
            return windowinfo.start(item, xlistitem, mediaurl)
        elif config.get_setting("player_mode") == "3" or "megacrypter.com" in mediaurl:
            import download_and_play
            download_and_play.download_and_play(mediaurl, "download_and_play.tmp", config.get_setting("downloadpath"))
            return

        elif config.get_setting("player_mode") == "0" or \
                (config.get_setting("player_mode") == "3" and mediaurl.startswith("rtmp")):
            # Añadimos el listitem a una lista de reproducción (playlist)
            playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            playlist.clear()
            playlist.add(mediaurl, xlistitem)

            # Reproduce
            playersettings = config.get_setting('player_type')
            logger.info("deportesalacarta.platformcode.platformstools playersettings=" + playersettings)

            if config.get_system_platform() == "xbox":
                player_type = xbmc.PLAYER_CORE_AUTO
                if playersettings == "0":
                    player_type = xbmc.PLAYER_CORE_AUTO
                    logger.info("deportesalacarta.platformcode.platformstools PLAYER_CORE_AUTO")
                elif playersettings == "1":
                    player_type = xbmc.PLAYER_CORE_MPLAYER
                    logger.info("deportesalacarta.platformcode.platformstools PLAYER_CORE_MPLAYER")
                elif playersettings == "2":
                    player_type = xbmc.PLAYER_CORE_DVDPLAYER
                    logger.info("deportesalacarta.platformcode.platformstools PLAYER_CORE_DVDPLAYER")

                xbmc_player = xbmc.Player(player_type)
            else:
                xbmc_player = xbmc.Player()

            xbmc_player.play(playlist, xlistitem)

        elif config.get_setting("player_mode") == "1":
            logger.info("mediaurl :" + mediaurl)
            logger.info("Tras setResolvedUrl")
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, xbmcgui.ListItem(path=mediaurl))

        elif config.get_setting("player_mode") == "2":
            xbmc.executebuiltin("PlayMedia(" + mediaurl + ")")

    # TODO MIRAR DE QUITAR VIEW
    if item.subtitle != "" and view:
        logger.info("Subtítulos externos: " + item.subtitle)
        xbmc.sleep(2000)
        xbmc.Player().setSubtitles(item.subtitle)


def play_torrent(item, xlistitem, mediaurl):
    logger.info("platformtools play_torrent")
    # Opciones disponibles para Reproducir torrents
    torrent_options = list()
    torrent_options.append(["Cliente interno (necesario libtorrent)"])
    torrent_options.append(["Cliente interno MCT (necesario libtorrent)"])

    # Plugins externos se pueden añadir otros
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.xbmctorrent")'):
        torrent_options.append(["Plugin externo: xbmctorrent", "plugin://plugin.video.xbmctorrent/play/%s"])
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.pulsar")'):
        torrent_options.append(["Plugin externo: pulsar", "plugin://plugin.video.pulsar/play?uri=%s"])
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.quasar")'):
        torrent_options.append(["Plugin externo: quasar", "plugin://plugin.video.quasar/play?uri=%s"])
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.stream")'):
        torrent_options.append(["Plugin externo: stream", "plugin://plugin.video.stream/play/%s"])
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.torrenter")'):
        torrent_options.append(["Plugin externo: torrenter",
                                "plugin://plugin.video.torrenter/?action=playSTRM&url=%s"])
    if xbmc.getCondVisibility('System.HasAddon("plugin.video.torrentin")'):
        torrent_options.append(["Plugin externo: torrentin", "plugin://plugin.video.torrentin/?uri=%s&image="])

    if len(torrent_options) > 1:
        seleccion = dialog_select("Abrir torrent con...", [opcion[0] for opcion in torrent_options])
    else:
        seleccion = 0

    # Plugins externos
    if seleccion > 1:
        mediaurl = urllib.quote_plus(item.url)
        xbmc.executebuiltin("PlayMedia(" + torrent_options[seleccion][1] % mediaurl + ")")

    if seleccion == 1:
        from platformcode import mct
        mct.play(mediaurl, xlistitem, subtitle=item.subtitle)

    # Reproductor propio (libtorrent)
    if seleccion == 0:
        import time
        played = False
        debug =  (config.get_setting("debug") == "true")
        
        # Importamos el cliente
        from btserver import Client

        # Iniciamos el cliente:
        c = Client(url=mediaurl, is_playing_fnc=xbmc.Player().isPlaying, wait_time=None, timeout=10,
                   temp_path=os.path.join(config.get_data_path(), "torrent"), print_status=debug)

        # Mostramos el progreso
        progreso = dialog_progress("Pelisalacarta - Torrent", "Iniciando...")

        # Mientras el progreso no sea cancelado ni el cliente cerrado
        while not c.closed:
            try:
                # Obtenemos el estado del torrent
                s = c.status
                if debug:
                  # Montamos las tres lineas con la info del torrent
                  txt = '%.2f%% de %.1fMB %s | %.1f kB/s' % \
                        (s.progress_file, s.file_size, s.str_state, s._download_rate)
                  txt2 = 'S: %d(%d) P: %d(%d) | DHT:%s (%d) | Trakers: %d' % \
                         (s.num_seeds, s.num_complete, s.num_peers, s.num_incomplete, s.dht_state, s.dht_nodes,
                          s.trackers)
                  txt3 = 'Origen Peers TRK: %d DHT: %d PEX: %d LSD %d ' % \
                         (s.trk_peers, s.dht_peers, s.pex_peers, s.lsd_peers)
                else:
                  txt = '%.2f%% de %.1fMB %s | %.1f kB/s' % \
                        (s.progress_file, s.file_size, s.str_state, s._download_rate)
                  txt2 = 'S: %d(%d) P: %d(%d)' % (s.num_seeds, s.num_complete, s.num_peers, s.num_incomplete)
                  try:
                    txt3 = 'Deteniendo automaticamente en: %ss' % (int(s.timeout))   
                  except:
                    txt3 = ''

                progreso.update(s.buffer, txt, txt2, txt3)
                time.sleep(0.5)
                
                if progreso.iscanceled():
                  progreso.close()
                  if s.buffer == 100:
                    if dialog_yesno("Pelisalacarta - Torrent", "¿Deseas iniciar la reproduccion?"):
                      played = False
                      progreso = dialog_progress("Pelisalacarta - Torrent", "")
                      progreso.update(s.buffer, txt, txt2, txt3)
                    else:
                      progreso = dialog_progress("Pelisalacarta - Torrent", "")
                      break
                      
                  else:
                    if dialog_yesno("Pelisalacarta - Torrent", "¿Deseas cancelar el proceso?"):
                      progreso = dialog_progress("Pelisalacarta - Torrent", "")
                      break
                      
                    else:
                      progreso = dialog_progress("Pelisalacarta - Torrent", "")
                      progreso.update(s.buffer, txt, txt2, txt3)

                   
   
                # Si el buffer se ha llenado y la reproduccion no ha sido iniciada, se inicia
                if s.buffer == 100 and not played:
                    # Cerramos el progreso
                    progreso.close()

                    # Obtenemos el playlist del torrent
                    videourl = c.get_play_list()

                    # Iniciamos el reproductor
                    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
                    playlist.clear()
                    playlist.add(videourl, xlistitem)
                    xbmc_player = xbmc.Player()
                    xbmc_player.play(playlist)

                    # Marcamos como reproducido para que no se vuelva a iniciar
                    played = True

                    # Y esperamos a que el reproductor se cierre
                    while xbmc.Player().isPlaying():
                        time.sleep(1)

                    # Cuando este cerrado,  Volvemos a mostrar el dialogo
                    progreso = dialog_progress("Pelisalacarta - Torrent", "")
                    progreso.update(s.buffer, txt, txt2, txt3)

            except:
                import traceback
                logger.info(traceback.format_exc())
                break
            

        progreso.update(100, "Terminando y eliminando datos", " ", " ")

        # Detenemos el cliente
        if not c.closed:
            c.stop()

        # Y cerramos el progreso
        progreso.close()
