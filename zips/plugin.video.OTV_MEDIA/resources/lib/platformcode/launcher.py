# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Distributed under the terms of GNU General Public License v3 (GPLv3)
# http://www.gnu.org/licenses/gpl-3.0.html
# ------------------------------------------------------------
# XBMC Launcher (xbmc / kodi / boxee)
# ------------------------------------------------------------

import os
import re
import sys
import urllib2
import xbmc

from resources.lib.httpkir import channeltools
from resources.lib.httpkir import config
from resources.lib.httpkir import downloadtools
from resources.lib.httpkir import jsontools
from resources.lib.httpkir import logger
from resources.lib.httpkir import scrapertools
from resources.lib.httpkir.item import Item
from platformcode import platformtools


def start():
    """ First function that is executed when entering the plugin.
    Within this function, all calls to the
    Functions that we want to run just open the plugin
    """
    logger.info("dss.platformcode.launcher start")

    # Test if all the required directories are created
    config.verify_directories_created()


def run():
    logger.info("dss.platformcode.launcher run")

    # Extract item from sys.argv
    if sys.argv[2]:
        item = Item().fromurl(sys.argv[2])

    # If no item, this is mainlist
    else:
        item = Item(channel="channelselector", action="getmainlist", viewmode="movie")

    if item.action != "actualiza":
        logger.info("dss.platformcode.launcher "+item.tostring())
    
    try:
        if item.action == "editor_keymap":
            from platformcode import editor_keymap
            return editor_keymap.start()
        
        # If item has no action, stops here
        if item.action == "":
            logger.info("dss.platformcode.launcher Item sin accion")
            return

        # Action for main menu in channelselector
        if item.action == "getmainlist":
            import channelselector
            itemlist = channelselector.getmainlist()

            # Check for updates only on first screen
            if config.get_setting("updatecheck") == "true":
                logger.info("Check for plugin updates enabled")
                from core import updater
                
                try:
                    update, version_publicada, message, url_repo, serv = updater.check()

                    if update:
                        new_item = Item(title="Descargar versión "+version_publicada, channel="updater",
                                        action="actualiza", thumbnail=channelselector.get_thumbnail_path() +
                                        "Crystal_Clear_action_info.png", version=version_publicada, url=url_repo,
                                        server=serv)
                        if config.get_setting("updateauto") == "true":
                            updater.actualiza(new_item)
                            new_item = Item(title="Info para ver los cambios en la nueva versión instalada",
                                            plot=message, action="", channel="",
                                            thumbnail=channelselector.get_thumbnail_path() +
                                            "Crystal_Clear_action_info.png", text_color="red")
                            itemlist.insert(0, new_item)
                        else:
                            platformtools.dialog_ok("Versión "+version_publicada+" disponible",
                                                message)

                            itemlist.insert(0, new_item)
                except:
                    import traceback
                    logger.info(traceback.format_exc())
                    logger.info("dss.platformcode.launcher Fallo al verificar la actualización")

            else:
                logger.info("dss.platformcode.launcher Check for plugin updates disabled")

            if not config.get_setting("primer_uso_matchcenter"):
                config.set_setting("primer_uso_matchcenter", "true")
                platformtools.dialog_ok("MatchCenter activado", "Reinicia Kodi para usarlo (pulsar tecla U)",
                                        "La tecla, botones y otras opciones pueden cambiarse en Configuración -> Preferencias -> MatchCenter")

            file_keyboard = xbmc.translatePath("special://profile/keymaps/deportesalacarta.xml")
            if config.get_setting("matchcenter_enabled") == "true" and not os.path.exists(file_keyboard):
                tecla = "61525"
                tecla_guardada = config.get_setting("keymap_edit", "editor_keymap")
                if tecla_guardada:
                    tecla = tecla_guardada
                from core import filetools
                data = '<keymap><global><keyboard><key id="%s">'  % tecla + 'runplugin(plugin://plugin.video.dss/?ewogICAgImFjdGlvbiI6ICJzdGFydCIsIAogICAgImNoYW5uZWwiOiAibWF0Y2hjZW50ZXIiLCAKICAgICJpbmZvTGFiZWxzIjoge30KfQ%3D%3D))</key></keyboard></global></keymap>'
                filetools.write(file_keyboard, data)
            elif config.get_setting("matchcenter_enabled") == "false" and os.path.exists(file_keyboard):
                from core import filetools
                try:
                    filetools.remove(file_keyboard)
                except:
                    pass
            
            platformtools.render_items(itemlist, item)

        # Action for updating plugin
        elif item.action == "actualiza":
            from core import updater
            updater.actualiza(item)
            xbmc.executebuiltin("Container.Refresh")

        # Action for channel listing on channelselector
        elif item.action == "filterchannels":
            import channelselector
            itemlist = channelselector.filterchannels(item.channel_type)

            platformtools.render_items(itemlist, item)

        # Action in certain channel specified in "action" and "channel" parameters
        else:
            can_open_channel = True

            # Checks if channel exists
            channel_file = os.path.join(config.get_runtime_path(), 'channels', item.channel+".py")
            logger.info("dss.platformcode.launcher channel_file=%s" % channel_file)

            channel = None

            if os.path.exists(channel_file):
                try:
                    channel = __import__('channels.%s' % item.channel, None, None, ["channels.%s" % item.channel])
                except ImportError:
                    exec "import channels."+item.channel+" as channel"

            logger.info("deportesalacarta.platformcode.launcher running channel "+channel.__name__+" "+channel.__file__)

            # Special play action
            if item.action == "play":
                logger.info("dss.platformcode.launcher play")
                # logger.debug("item_toPlay: " + "\n" + item.tostring('\n'))

                # First checks if channel has a "play" function
                if hasattr(channel, 'play'):
                    logger.info("dss.platformcode.launcher executing channel 'play' method")
                    itemlist = channel.play(item)
                    b_favourite = item.isFavourite
                    # Play should return a list of playable URLS
                    if len(itemlist) > 0 and isinstance(itemlist[0], Item):
                        item = itemlist[0]
                        if b_favourite:
                            item.isFavourite = True
                        platformtools.play_video(item)

                    #Permitir varias calidades desde play en el canal
                    elif len(itemlist) > 0 and isinstance(itemlist[0], list):
                        item.video_urls = itemlist
                        platformtools.play_video(item)

                    # If not, shows user an error message
                    else:
                        platformtools.dialog_ok("plugin", "There is nothing to play")

                # If player don't have a "play" function, not uses the standard play from platformtools
                else:
                    logger.info("dss.platformcode.launcher executing core 'play' method")
                    platformtools.play_video(item)

            # Special action for findvideos, where the plugin looks for known urls
            elif item.action == "findvideos":

                # First checks if channel has a "findvideos" function
                if hasattr(channel, 'findvideos'):
                    itemlist = getattr(channel, item.action)(item)

                # If not, uses the generic findvideos function
                else:
                    logger.info("dss.platformcode.launcher no channel 'findvideos' method, "
                                "executing core method")
                    from core import servertools
                    itemlist = servertools.find_video_items(item)

                platformtools.render_items(itemlist, item)

            # Special action for searching, first asks for the words then call the "search" function
            elif item.action == "search":
                logger.info("dss.platformcode.launcher search")
                
                tecleado = platformtools.dialog_input("")
                if tecleado is not None:
                    tecleado = tecleado.replace(" ", "+")
                    # TODO revisar 'personal.py' porque no tiene función search y daría problemas
                    itemlist = channel.search(item, tecleado)
                else:
                    itemlist = []
                
                platformtools.render_items(itemlist, item)

            # For all other actions
            else:
                logger.info("dss.platformcode.launcher executing channel '"+item.action+"' method")
                itemlist = getattr(channel, item.action)(item)
                platformtools.render_items(itemlist, item)

    except urllib2.URLError, e:
        import traceback
        logger.error("dss.platformcode.launcher "+traceback.format_exc())

        # Grab inner and third party errors
        if hasattr(e, 'reason'):
            logger.info("dss.platformcode.launcher Razon del error, codigo: "+str(e.reason[0])+", Razon: " +
                        str(e.reason[1]))
            texto = config.get_localized_string(30050)  # "No se puede conectar con el sitio web"
            platformtools.dialog_ok("plugin", texto)

        # Grab server response errors
        elif hasattr(e, 'code'):
            logger.info("dss.platformcode.launcher codigo de error HTTP : %d" % e.code)
            # "El sitio web no funciona correctamente (error http %d)"
            platformtools.dialog_ok("plugin", config.get_localized_string(30051) % e.code)
    
    except:
        import traceback
        logger.error("dss.platformcode.launcher "+traceback.format_exc())
        
        patron = 'File "'+os.path.join(config.get_runtime_path(), "channels", "").replace("\\", "\\\\")+'([^.]+)\.py"'
        canal = scrapertools.find_single_match(traceback.format_exc(), patron)
        
        try:
            xbmc_version = int(xbmc.getInfoLabel("System.BuildVersion").split(".", 1)[0])
            if xbmc_version > 13:
                log_name = "kodi.log"
            else:
                log_name = "xbmc.log"
            log_message = "Ruta: "+xbmc.translatePath("special://logpath")+log_name
        except:
            log_message = ""

        if canal:
            platformtools.dialog_ok(
                "Error inesperado en el canal " + canal,
                "Puede deberse a un fallo de conexión, la web del canal "
                "ha cambiado su estructura, o un error interno de deportesalacarta.",
                "Para saber más detalles, consulta el log.", log_message)
        else:
            platformtools.dialog_ok(
                "Se ha producido un error en pelisalacarta",
                "Comprueba el log para ver mas detalles del error.",
                log_message)
