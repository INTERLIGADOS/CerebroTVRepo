from xbmcswift2 import Plugin
from xbmcswift2 import actions
import xbmc,xbmcaddon,xbmcvfs,xbmcgui
import re
from rpc import RPC
import requests
import random
import sqlite3
from datetime import datetime,timedelta
import time
#import urllib
import HTMLParser
import xbmcplugin
#import xml.etree.ElementTree as ET
#import sqlite3
import os
#import shutil
#from rpc import RPC
from types import *

plugin = Plugin()
big_list_view = False

def log2(v):
    xbmc.log(repr(v))

def log(v):
    xbmc.log(re.sub(',',',\n',repr(v)))

def get_icon_path(icon_name):
    addon_path = xbmcaddon.Addon().getAddonInfo("path")
    return os.path.join(addon_path, 'resources', 'img', icon_name+".png")


def remove_formatting(label):
    label = re.sub(r"\[/?[BI]\]",'',label)
    label = re.sub(r"\[/?COLOR.*?\]",'',label)
    return label

@plugin.route('/addon/<id>')
def addon(id):
    addon = plugin.get_storage(id)
    items = []
    for name in sorted(addon):
        url = addon[name]
        items.append(
        {
            'label': name,
            'path': url,
            'thumbnail':get_icon_path('tv'),
            'is_playable':True,
        })
    return items

@plugin.route('/player')
def player():
    if not plugin.get_setting('addons.folder'):
        dialog = xbmcgui.Dialog()
        dialog.notification("Echo INI Creator", "Set Folder",xbmcgui.NOTIFICATION_ERROR )
        xbmcaddon.Addon ('plugin.video.echoini').openSettings()

    addons = plugin.get_storage("addons")
    for a in addons.keys():
        add = plugin.get_storage(a)
        add.clear()
    addons.clear()

    folder = plugin.get_setting("addons.folder")
    file = plugin.get_setting("addons.file")
    filename = os.path.join(folder,file)
    f = xbmcvfs.File(filename,"rb")
    lines = f.read().splitlines()

    addon = None
    for line in lines:
        if line.startswith('['):
            a = line.strip('[]')
            addons[a] = a
            addon = plugin.get_storage(a)
            addon.clear()
        elif "=" in line:
            (name,url) = line.split('=',1)
            if url and addon is not None:
                addon[name] = url

    items = []
    for id in sorted(addons):
        items.append(
        {
            'label': id,
            'path': plugin.url_for('addon',id=id),
            'thumbnail':get_icon_path('tv'),
        })
    return items

@plugin.route('/play/<url>')
def play(url):
    xbmc.executebuiltin('PlayMedia(%s)' % url)

@plugin.route('/pvr_subscribe')
def pvr_subscribe():
    plugin.set_setting("pvr.subscribe","true")
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/pvr_unsubscribe')
def pvr_unsubscribe():
    plugin.set_setting("pvr.subscribe","false")
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/add_folder/<id>/<path>')
def add_folder(id,path):
    folders = plugin.get_storage('folders')
    #ids = plugin.get_storage('ids')
    folders[path] = id
    #ids[id] = id
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/remove_folder/<id>/<path>')
def remove_folder(id,path):
    folders = plugin.get_storage('folders')
    del folders[path]
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/clear')
def clear():
    folders = plugin.get_storage('folders')
    folders.clear()

@plugin.route('/folder/<id>/<path>')
def folder(id,path):
    folders = plugin.get_storage('folders')
    response = RPC.files.get_directory(media="files", directory=path, properties=["thumbnail"])
    files = response["files"]
    dirs = dict([[remove_formatting(f["label"]), f["file"]] for f in files if f["filetype"] == "directory"])
    links = {}
    thumbnails = {}
    for f in files:
        if f["filetype"] == "file":
            label = remove_formatting(f["label"])
            file = f["file"]
            while (label in links):
                label = "%s." % label
            links[label] = file
            thumbnails[label] = f["thumbnail"]

    items = []

    for label in sorted(dirs):
        path = dirs[label]
        context_items = []
        if path in folders:
            fancy_label = "[COLOR red][B]%s[/B][/COLOR] " % label
            context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Unsubscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_folder, id=id, path=path))))
        else:
            fancy_label = "[B]%s[/B]" % label
            context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Subscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_folder, id=id, path=path))))
        items.append(
        {
            'label': fancy_label,
            'path': plugin.url_for('folder',id=id, path=path),
            'thumbnail': get_icon_path('tv'),
            'context_menu': context_items,
        })

    for label in sorted(links):
        items.append(
        {
            'label': label,
            'path': plugin.url_for('play',url=links[label]),
            'thumbnail': thumbnails[label],
        })
    return items

@plugin.route('/pvr')
def pvr():
    index = 0
    urls = []
    channels = {}
    for group in ["radio","tv"]:
        urls = urls + xbmcvfs.listdir("pvr://channels/%s/All channels/" % group)[1]
    for group in ["radio","tv"]:
        groupid = "all%s" % group
        json_query = RPC.PVR.get_channels(channelgroupid=groupid, properties=[ "thumbnail", "channeltype", "hidden", "locked", "channel", "lastplayed", "broadcastnow" ] )
        if "channels" in json_query:
            for channel in json_query["channels"]:
                channelname = channel["label"]
                channelid = channel["channelid"]-1
                channellogo = channel['thumbnail']
                streamUrl = urls[index]
                index = index + 1
                url = "pvr://channels/%s/All channels/%s" % (group,streamUrl)
                channels[url] = channelname
    items = []
    for url in sorted(channels, key=lambda x: channels[x]):
        name = channels[url]
        items.append(
        {
            'label': name,
            'path': url,
            'is_playable': True,
        })
    return items

@plugin.route('/subscribe')
def subscribe():
    folders = plugin.get_storage('folders')
    ids = {}
    for folder in folders:
        id = folders[folder]
        ids[id] = id
    all_addons = []
    for type in ["xbmc.addon.video", "xbmc.addon.audio"]:
        response = RPC.addons.get_addons(type=type,properties=["name", "thumbnail"])
        if "addons" in response:
            found_addons = response["addons"]
            all_addons = all_addons + found_addons

    seen = set()
    addons = []
    for addon in all_addons:
        if addon['addonid'] not in seen:
            addons.append(addon)
        seen.add(addon['addonid'])

    items = []

    pvr = plugin.get_setting('pvr.subscribe')
    context_items = []
    label = "PVR"
    if pvr == "true":
        fancy_label = "[COLOR red][B]%s[/B][/COLOR] " % label
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Unsubscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(pvr_unsubscribe))))
    else:
        fancy_label = "[B]%s[/B]" % label
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Subscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(pvr_subscribe))))
    items.append(
    {
        'label': fancy_label,
        'path': plugin.url_for('pvr'),
        'thumbnail':get_icon_path('tv'),
        'context_menu': context_items,
    })

    addons = sorted(addons, key=lambda addon: remove_formatting(addon['name']).lower())
    for addon in addons:
        label = remove_formatting(addon['name'])
        id = addon['addonid']
        path = "plugin://%s" % id
        context_items = []
        if id in ids:
            fancy_label = "[COLOR red][B]%s[/B][/COLOR] " % label
            context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Unsubscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_folder, id=id, path=path))))
        else:
            fancy_label = "[B]%s[/B]" % label
            context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Subscribe', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_folder, id=id, path=path))))
        items.append(
        {
            'label': fancy_label,
            'path': plugin.url_for('folder',id=id, path=path),
            'thumbnail': get_icon_path('tv'),
            'context_menu': context_items,
        })
    return items

@plugin.route('/update')
def update():
    if not plugin.get_setting('addons.folder'):
        dialog = xbmcgui.Dialog()
        dialog.notification("Echo INI Creator", "Set Folder",xbmcgui.NOTIFICATION_ERROR )
        xbmcaddon.Addon ('plugin.video.echoini').openSettings()

    folders = plugin.get_storage('folders')
    streams = {}

    for folder in folders:
        log("[plugin.video.echoini] " + folder)
        path = folder
        id = folders[folder]
        if not id in streams:
            streams[id] = {}
        response = RPC.files.get_directory(media="files", directory=path, properties=["thumbnail"])
        if not 'error' in response:
            files = response["files"]
            links = {}
            thumbnails = {}
            for f in files:
                if f["filetype"] == "file":
                    label = remove_formatting(f["label"])
                    file = f["file"]
                    while (label in links):
                        label = "%s." % label
                    links[label] = file
                    thumbnails[label] = f["thumbnail"]
                    streams[id][label] = file

    if plugin.get_setting("pvr.subscribe") == "true":
        streams["plugin.video.echoini"] = {}
        items = pvr()
        for item in items:
            name = item["label"]
            url = item["path"]
            streams["plugin.video.echoini"][name] = url

    folder = plugin.get_setting("addons.folder")
    file = plugin.get_setting("addons.file")
    filename = os.path.join(folder,file)
    f = xbmcvfs.File(filename,"wb")

    # steams contains all the addon ids of the addons you are generating i.e plugin.video.sportie
    for id in sorted(streams):
        # make a line that contains the plugin to a line before all the channels i.e [plugin.video.sportie]
        line = "[%s]\n" % id
        # write that line to the ini file.
        f.write(line.encode("utf8"))
        # make the word channels contain all the streams from said addon.
        channels = streams[id]
        # for each channel in the addon. i.e bbc one
        for channel in sorted(channels):
            # Grab the URL to the channel from the list
            url = channels[channel]
            # make a list called naughty that contains all the funny characters, all within "" and seperated by a comma.
            naughty = [":","!",'"',"$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","#","~","@",";",":","/","?",".",">",",","<","|",","]
            # go through every item in the list. So in the first instance item would become :
            for item in naughty:
                # Check if that character exists in the channel name, if so replace it with a space.
                channel = channel.replace(item,' ')
            # Strip all whitespace from the beggining of the channel name (AKA Remove all spaces)
            channel=channel.lstrip()
            # Strip all whitespace from the end of the channel name (AKA Remove all spaces)
            channel=channel.rstrip()
            # Check if there are any double spaces in the channel name and replace them with a single space.
            while "  " in channel:
                # Replace double spaces with single spaces.
                channel = channel.replace("  "," ")
            #Check if the length of the channel name is one or more characters.
            if len(channel) >= 1:
                # If so make the line to conatin the channel anme and url, you can see the = below, channel before the = url after.
                line = "%s=%s\n" % (channel,url)
                #write the line to the ini file.
                f.write(line.encode("utf8"))
    #Close the file.
    f.close()
    xbmcgui.Dialog().notification("Echo INI Creator", "Finished Update")

@plugin.route('/search/<what>')
def search(what):
    if not what:
        return
    addons = plugin.get_storage("addons")
    folder = plugin.get_setting("addons.folder")
    file = plugin.get_setting("addons.file")
    filename = os.path.join(folder,file)
    f = xbmcvfs.File(filename,"rb")
    lines = f.read().splitlines()
    addon = None
    for line in lines:
        if line.startswith('['):
            a = line.strip('[]')
            addons[a] = a
            addon = plugin.get_storage(a)
            addon.clear()
        elif "=" in line:
            (name,url) = line.split('=',1)
            if url and addon is not None:
                addon[name] = url

    items = []
    for a in addons.keys():
        add = plugin.get_storage(a)
        log2(add.keys())
        exact = [x for x in add.keys() if x.lower() == what.lower()]
        log2(exact)
        partial = [x for x in add.keys() if what.lower() in x.lower()]
        ignore_space = [x for x in add.keys() if re.sub(' ','',what).lower() in re.sub(' ','',x).lower()]
        found = exact + partial
        for f in sorted(set(exact)):
            items.append({
                "label": "[COLOR green]%s [%s][/COLOR]" % (f,a),
                "path" : add[f],
                "is_playable" : True,
            })
        for f in sorted(set(partial)-set(exact)):
            items.append({
                "label": "[COLOR orange]%s [%s][/COLOR]" % (f,a),
                "path" : add[f],
                "is_playable" : True,
            })
        for f in sorted(set(ignore_space)-set(partial)-set(exact)):
            items.append({
                "label": "[COLOR red]%s [%s][/COLOR]" % (f,a),
                "path" : add[f],
                "is_playable" : True,
            })
    return items

@plugin.route('/search_dialog')
def search_dialog():
    dialog = xbmcgui.Dialog()
    what = dialog.input("Search")
    if what:
        return search(what)

@plugin.route('/add_channel')
def add_channel():
    channels = plugin.get_storage('channels')
    d = xbmcgui.Dialog()
    channel = d.input("Add Channel")
    if channel:
        channels[channel] = ""
    xbmc.executebuiltin('Container.Refresh')


@plugin.route('/remove_channel')
def remove_channel():
    channels = plugin.get_storage('channels')
    channel_list = sorted(channels)
    d = xbmcgui.Dialog()
    which = d.select("Remove Channel",channel_list)
    if which == -1:
        return
    channel = channel_list[which]
    del channels[channel]
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/remove_this_channel/<channel>')
def remove_this_channel(channel):
    channels = plugin.get_storage('channels')
    del channels[channel]
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/clear_channels')
def clear_channels():
    channels = plugin.get_storage('channels')
    channels.clear()
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/import_channels')
def import_channels():
    channels = plugin.get_storage('channels')
    d = xbmcgui.Dialog()
    filename = d.browse(1, 'Import Channels', 'files', '', False, False, 'special://home/')
    if not filename:
        return
    if filename.endswith('.ini'):
        lines = xbmcvfs.File(filename,'rb').read().splitlines()
        for line in lines:
            if not line.startswith('[') and not line.startswith('#') and "=" in line:
                channel_url = line.split('=',1)
                if len(channel_url) == 2:
                    name = channel_url[0]
                    channels[name] = ""
    xbmc.executebuiltin('Container.Refresh')

@plugin.route('/stream_search/<channel>')
def stream_search(channel):
    #folders = plugin.get_storage('folders')
    streams = {}

    folder = plugin.get_setting("addons.folder")
    file = plugin.get_setting("addons.file")
    filename = os.path.join(folder,file)
    f = xbmcvfs.File(filename,"rb")
    lines = f.read().splitlines()
    for line in lines:
        if line.startswith('['):
            addon = line.strip('[]')
            if addon not in streams:
                streams[addon] = {}
        elif "=" in line:
            (name,url) = line.split('=',1)
            if url and addon is not None:
                streams[addon][url] = name

    channel_search = channel.lower().replace(' ','')
    stream_list = []
    for id in sorted(streams):
        files = streams[id]
        for f in sorted(files, key=lambda k: files[k]):
            label = files[f]
            label_search = label.lower().replace(' ','')
            if label_search in channel_search or channel_search in label_search:
                stream_list.append((id,f,label))
    labels = ["[%s] %s" % (x[0],x[2]) for x in stream_list]
    d = xbmcgui.Dialog()
    which = d.select(channel, labels)
    if which == -1:
        return
    stream_name = stream_list[which][2]
    stream_link = stream_list[which][1]
    plugin.set_resolved_url(stream_link)

@plugin.route('/export_channels')
def export_channels():
    channels = plugin.get_storage('channels')

    f = xbmcvfs.File('special://profile/addon_data/plugin.video.echoini/export.ini','wb')
    for channel in sorted(channels):
        url = plugin.url_for('stream_search',channel=channel)
        channel = channel.replace(':','')
        s = "%s=%s\n" % (channel,url)
        f.write(s)
    f.close()

@plugin.route('/channel_player')
def channel_player():
    channels = plugin.get_storage("channels")

    items = []
    for channel in sorted(channels):
        context_items = []
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Add Channel', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_channel))))
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Remove Channel', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_this_channel, channel=channel))))
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Import Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(import_channels))))
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Export Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(export_channels))))
        context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Clear Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(clear_channels))))
        items.append(
        {
            'label': channel,
            'path': plugin.url_for('stream_search',channel=channel),
            'thumbnail':get_icon_path('tv'),
            'is_playable': True,
            'context_menu': context_items,
        })
    return items

@plugin.route('/')
def index():
    items = []
    context_items = []
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Clear Subscriptions', 'XBMC.RunPlugin(%s)' % (plugin.url_for(clear))))
    items.append(
    {
        'label': "[COLOR red]Subscribe[/COLOR]",
        'path': plugin.url_for('subscribe'),
        'thumbnail':get_icon_path('tv'),
        'context_menu': context_items,
    })
    items.append(
    {
        'label': "[COLOR green]Create[/COLOR]",
        'path': plugin.url_for('update'),
        'thumbnail':get_icon_path('tv'),
    })
    items.append(
    {
        'label': "Play",
        'path': plugin.url_for('player'),
        'thumbnail':get_icon_path('tv'),
    })
    context_items = []
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Add Channel', 'XBMC.RunPlugin(%s)' % (plugin.url_for(add_channel))))
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Remove Channel', 'XBMC.RunPlugin(%s)' % (plugin.url_for(remove_channel))))
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Import Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(import_channels))))
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Export Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(export_channels))))
    context_items.append(("[COLOR red][B]%s[/B][/COLOR] " % 'Clear Channels', 'XBMC.RunPlugin(%s)' % (plugin.url_for(clear_channels))))
    items.append(
    {
        'label': "Channels",
        'path': plugin.url_for('channel_player'),
        'thumbnail':get_icon_path('tv'),
        'context_menu': context_items,
    })
    return items

if __name__ == '__main__':
    plugin.run()
    if big_list_view == True:
        view_mode = int(plugin.get_setting('view_mode'))
        plugin.set_view_mode(view_mode)