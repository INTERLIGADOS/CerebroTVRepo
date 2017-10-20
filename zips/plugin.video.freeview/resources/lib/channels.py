import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmcvfs,os,sys,datetime,string,hashlib,net,xbmc
import xbmcaddon
import json
from cookielib import CookieJar
from resources.lib.modules.common import *
from resources.lib.modules.plugintools import *

addon_id  = xbmcaddon.Addon().getAddonInfo('id')
selfAddon = xbmcaddon.Addon(id=addon_id)
fanart    = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.freeview', 'fanart.jpg'))
logos     = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.freeview/resources/logos', ''))
logos_tvp = 'https://assets.tvplayer.com/common/logos/256/Inverted/'

def getChannels():
	# BBC iPlayer
	addLink('BBC Four HD','http://vs-hls-uk-live.akamaized.net/pool_33/live/bbc_four_hd/bbc_four_hd.isml/bbc_four_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'110.png')
	addLink('BBC News HD','http://vs-hls-uk-live.akamaized.net/pool_34/live/bbc_news_channel_hd/bbc_news_channel_hd.isml/bbc_news_channel_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'111.png')
	addLink('BBC One HD','http://vs-hls-uk-live.akamaized.net/pool_30/live/bbc_one_hd/bbc_one_hd.isml/bbc_one_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'89.png')
	addLink('BBC One Northern Ireland','http://vs-hls-uk-live.akamaized.net/pool_4/live/bbc_one_northern_ireland_hd/bbc_one_northern_ireland_hd.isml/bbc_one_northern_ireland_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'89.png')
	addLink('BBC One Scotland','http://vs-hls-uk-live.akamaized.net/pool_5/live/bbc_one_scotland_hd/bbc_one_scotland_hd.isml/bbc_one_scotland_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'89.png')
	addLink('BBC One Wales','http://vs-hls-uk-live.akamaized.net/pool_3/live/bbc_one_wales_hd/bbc_one_wales_hd.isml/bbc_one_wales_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'89.png')
	addLink('BBC Two Northern Ireland','http://vs-hls-uk-live.akamaized.net/pool_5/live/bbc_two_northern_ireland_digital/bbc_two_northern_ireland_digital.isml/bbc_two_northern_ireland_digital-pa3%3d96000-video%3d1604032.norewind.m3u8',1,logos_tvp+'90.png')
	addLink('BBC Two Scotland','http://vs-hls-uk-live.akamaized.net/pool_5/live/bbc_two_scotland/bbc_two_scotland.isml/bbc_two_scotland-pa3%3d96000-video%3d1604032.norewind.m3u8',1,logos_tvp+'90.png')
	addLink('BBC Two Wales','http://vs-hls-uk-live.akamaized.net/pool_5/live/bbc_two_wales_digital/bbc_two_wales_digital.isml/bbc_two_wales_digital-pa3%3d96000-video%3d1604032.norewind.m3u8',1,logos_tvp+'90.png')
	addLink('BBC Two HD','http://vs-hls-uk-live.akamaized.net/pool_31/live/bbc_two_hd/bbc_two_hd.isml/bbc_two_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'90.png')
	#addLink('BBC Two HD','http://vs-hls-uk-live.akamaized.net/pool_31/live/bbc_two_hd/bbc_two_hd.isml/bbc_two_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'90.png')
	addLink('CBBC HD','http://vs-hls-uk-live.akamaized.net/pool_1/live/cbbc_hd/cbbc_hd.isml/cbbc_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'113.png')
	addLink('CBeebies HD','http://vs-hls-uk-live.akamaized.net/pool_2/live/cbeebies_hd/cbeebies_hd.isml/cbeebies_hd-pa4%3d128000-video%3d5070016.m3u8',1,logos_tvp+'114.png')
	
	# ITV Hub
	addLink('CITV','http://citvliveios-i.akamaihd.net/hls/live/207267/itvlive/CITVMN/master_Main1800.m3u8',1,logos+'citv.png')
	addLink('ITV2','http://itv2liveios-i.akamaihd.net/hls/live/203495/itvlive/ITV2MN/master_Main1800.m3u8',1,logos+'itv2.png')
	addLink('ITV3','http://itv3liveios-i.akamaihd.net/hls/live/207262/itvlive/ITV3MN/master_Main1800.m3u8',1,logos+'itv3.png')
	addLink('ITV4','http://itv4liveios-i.akamaihd.net/hls/live/207266/itvlive/ITV4MN/master_Main1800.m3u8',1,logos+'itv4.png')
	addLink('ITVBe','http://itvbeliveios-i.akamaihd.net/hls/live/219078/itvlive/ITVBE/master_Main1800.m3u8',1,logos+'itvbe.png')
	
	# From website
	addLink('Blaze','http://live.blaze.simplestreamcdn.com/live/blaze/bitrate1.isml/bitrate1-audio_track=64000-video=3500000.m3u8',1,logos+'blaze.png')
	addLink('London Live','http://bcoveliveios-i.akamaihd.net/hls/live/217434/3083279840001/master_900.m3u8',1,logos+'londonlive.png')
	
	# YouTube
	addLink('Sky News','plugin://plugin.video.youtube/play/?video_id=y60wDzZt8yg',1,logos+'skynews.png')
	addLink('DW News','plugin://plugin.video.youtube/play/?video_id=gNosnzCaS4I',1,logos+'dwnews.png')
	
	# TVPlayer
	addLink('4Music','128',2,logos_tvp+'128.png')
	addLink('Al Jazeera','146',2,logos_tvp+'146.png')
	addLink('BBC Alba','236',2,logos_tvp+'236.png')
	addLink('BBC Four','110',2,logos_tvp+'110.png')
	addLink('BBC News','111',2,logos_tvp+'111.png')
	addLink('BBC One','89',2,logos_tvp+'89.png')
	addLink('BBC Parliament','345',2,logos_tvp+'345.png')
	addLink('BBC Two','90',2,logos_tvp+'90.png')
	addLink('Bloomberg','514',2,logos_tvp+'514.png')
	addLink('The Box','129',2,logos_tvp+'129.png')
	addLink('Box Hits','130',2,logos_tvp+'130.png')
	addLink('Box Upfront','158',2,logos_tvp+'158.png')
	addLink('Capital TV','157',2,logos_tvp+'157.png')
	addLink('CBBC','113',2,logos_tvp+'113.png')
	addLink('CBeebies','114',2,logos_tvp+'114.png')
	addLink('Channel 4','92',2,logos_tvp+'92.png')
	addLink('Channel 5','574',2,logos_tvp+'574.png')
	addLink('Channel AKA','227',2,logos_tvp+'227.png')
	addLink('Chilled','226',2,logos_tvp+'226.png')
	addLink('Clubland','225',2,logos_tvp+'225.png')
	addLink('CNN International','286',2,logos_tvp+'286.png')
	addLink('Community Channel','259',2,logos_tvp+'259.png')
	addLink('Dave','300',2,logos_tvp+'300.png')
	addLink('Dave ja vu','317',2,logos_tvp+'317.png')
	addLink('Drama','346',2,logos_tvp+'346.png')
	addLink('Food Network','125',2,logos_tvp+'125.png')
	addLink('Food Network+1','254',2,logos_tvp+'254.png')
	addLink('Forces TV','555',2,logos_tvp+'555.png')
	addLink('Heart TV','153',2,logos_tvp+'153.png')
	addLink('Home','512',2,logos_tvp+'512.png')
	addLink('ITV1','204',2,logos_tvp+'204.png')
	addLink('Kerrang!','133',2,logos_tvp+'133.png')
	addLink('Kiss','131',2,logos_tvp+'131.png')
	addLink('Magic','132',2,logos_tvp+'132.png')
	addLink('NOW Music','228',2,logos_tvp+'228.png')
	addLink('QUEST','327',2,logos_tvp+'327.png')
	addLink('QUEST RED','577',2,logos_tvp+'577.png')
	addLink('QVC Beauty','250',2,logos_tvp+'250.png')
	addLink('QVC Extra','248',2,logos_tvp+'248.png')
	addLink('QVC Plus','344',2,logos_tvp+'344.png')
	addLink('QVC Style','249',2,logos_tvp+'249.png')
	addLink('QVC','247',2,logos_tvp+'247.png')
	addLink('Really','306',2,logos_tvp+'306.png')
	addLink('S4C','251',2,logos_tvp+'251.png')
	addLink('Travel Channel','126',2,logos_tvp+'126.png')
	addLink('Travel Channel+1','255',2,logos_tvp+'255.png')
	addLink('Yesterday','308',2,logos_tvp+'308.png')
	addLink('Yesterday+1','318',2,logos_tvp+'318.png')
	
	# TVCatchup
	addLink('CBS Drama','cbsdrama',13,logos+'cbsdrama.png')
	addLink('Challenge','challenge',13,logos+'challenge.png')
	addLink('Craft Extra','craftextra',13,logos+'craftextra.png')
	addLink('Create and Craft','createandcraft',13,logos+'createandcraft.png')
	addLink('E4','e4',13,logos+'e4.png')
	addLink('Film4','film4',13,logos+'film4.png')
	addLink('Ideal Extra','idealextra',13,logos+'idealextra.png')
	addLink('Ideal World','idealworld',13,logos+'idealworld.png')
	addLink('POP','pop',13,logos+'pop.png')
	addLink('Pick','pick',13,logos+'pick.png')
	addLink('Spike','spike',13,logos+'spike.png')
	addLink('Tiny Pop','tinypop',13,logos+'tinypop.png')
	addLink('TruTV','trutv',13,logos+'trutv.png')
	addLink('True Crime','truecrime',13,logos+'truecrime.png')
	addLink('True Entertainment','trueentertainment',13,logos+'trueentertainment.png')
	addLink('TV Warehouse','tvwarehouse',13,logos+'tvwarehouse.png')
	addLink('VIVA','viva',13,logos+'viva.png')
	addLink('Vintage TV','vintagetv',13,logos+'vintagetv.png')
	addLink('YourTV','yourtv',13,logos+'yourtv.png')
	addLink('movies4men','movies4men',13,logos+'movies4men.png')
	
	# TVCatchup Test
	#addLink('CBS Action','cbsaction',13,logos+'cbsaction.png')
	#addLink('CBS Reality','cbsreality',13,logos+'cbsreality.png')
	#addLink('Movie Mix','moviemix',13,logos+'moviemix.png')
	#addLink('Talking Pictures TV','talkingpicturestv',13,logos+'talkingpicturestv.png')
	
	
	xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
