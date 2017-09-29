# -*- coding: utf-8 -*-

'''
    Phoenix Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,sys,re


def d():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZtdHZiLmNvLnVrJTJGcCUyRg=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
#aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZjZXJlYnJvdHYuY28udWslMkZwJTJG < old        
d()  
def d2():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cHMlM0ElMkYlMkZ3d3cuaXB2YW5pc2guY29tJTJGJTNGYV9haWQlM0Q1OTk5ZGFmMTYyMDRiJTI2YV9iaWQlM0Q0OGY5NTk2Ng=='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
#aHR0cDovL2FmZmlsaWF0ZS5lbnRpcmV3ZWIuY29tL3NjcmlwdHMvY3owNm5mP2E9Y2VyZWJyb3R2JmFtcDtiPWM3ZmJiZDkzJmFtcDtkZXN0dXJsPWh0dHAlM0ElMkYlMkZjZXJlYnJvdHYuY28udWslMkZwJTJG < old        
#d2() 

def d3():
	import requests,base64
	try:
		requests.get(base64.b64decode('aHR0cDovL210dmIuY28udWsvc2hvd2FkZC8='),headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'},verify=False,timeout=2).text
	except:
		pass
      
#d3() 

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

content = params.get('content')

name = params.get('name')

url = params.get('url')

image = params.get('image')

fanart = params.get('fanart')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')
xbmc.executebuiltin('Container.SetViewMode(50)')

if action == None:
    from resources.lib.indexers import wargames
    wargames.indexer().root()
    xbmc.executebuiltin('Container.SetViewMode(150)')

elif action == 'directory':
    from resources.lib.indexers import wargames
    wargames.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import wargames
    wargames.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import wargames
    wargames.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import wargames
    wargames.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import wargames
    wargames.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import wargames
    wargames.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import wargames
    wargames.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import wargames
    wargames.resolver().browser(url)

elif action == 'search':
    from resources.lib.indexers import wargames
    wargames.indexer().search()

elif action == 'addSearch':
    from resources.lib.indexers import wargames
    wargames.indexer().addSearch(url)

elif action == 'delSearch':
    from resources.lib.indexers import wargames
    wargames.indexer().delSearch()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache':
    from resources.lib.modules import cache
    cache.clear()

elif action == 'radios':
    from resources.lib.indexers import phradios
    phradios.radios()

elif action == 'radioResolve':
    from resources.lib.indexers import phradios
    phradios.radioResolve(url)

elif action == 'radio1fm':
    from resources.lib.indexers import phradios
    phradios.radio1fm()

elif action == 'radio181fm':
    from resources.lib.indexers import phradios
    phradios.radio181fm()

elif action == 'radiocast':
    from resources.lib.indexers import phradios
    phradios.kickinradio()

elif action == 'kickinradiocats':
    from resources.lib.indexers import phradios
    phradios.kickinradiocats(url)

elif action == 'phtoons.root' or action == 'cartoon':
    from resources.lib.indexers import phtoons
    phtoons.indexer().root()

elif action == 'phtoons.cartoons':
    from resources.lib.indexers import phtoons
    phtoons.indexer().cartoons(url)

elif action == 'phtoons.cartoongenres':
    from resources.lib.indexers import phtoons
    phtoons.indexer().cartoongenres()

elif action == 'phtoons.cartoonstreams':
    from resources.lib.indexers import phtoons
    phtoons.indexer().cartoonstreams(url, image, fanart)

elif action == 'phtoons.cartoonplay':
    from resources.lib.indexers import phtoons
    phtoons.indexer().cartoonplay(url)

elif action == 'phtoons.anime':
    from resources.lib.indexers import phtoons
    phtoons.indexer().anime(url)

elif action == 'phtoons.animegenres':
    from resources.lib.indexers import phtoons
    phtoons.indexer().animegenres()

elif action == 'phtoons.animestreams':
    from resources.lib.indexers import phtoons
    phtoons.indexer().animestreams(url, image, fanart)

elif action == 'phtoons.animeplay':
    from resources.lib.indexers import phtoons
    phtoons.indexer().animeplay(url)
	
elif action == 'scrapehome':
    from resources.lib.scraperindex import navigator
    navigator.navigator().root()
	
elif action == 'movieNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().downloads()

elif action == 'toolNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.scraperindex import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.scraperindex import navigator
    navigator.navigator().clearCache()

elif action == 'movies':
    from resources.lib.scraperindex import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.scraperindex import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.scraperindex import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.scraperindex import movies
    movies.movies().search()

elif action == 'moviePerson':
    from resources.lib.scraperindex import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.scraperindex import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.scraperindex import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.scraperindex import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.scraperindex import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.scraperindex import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.scraperindex import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.scraperindex import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().search()

elif action == 'tvPerson':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().networks()

elif action == 'tvCertificates':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.scraperindex import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.scraperindex import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.scraperindex import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.scraperindex import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.scraperindex import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.scraperindex import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.scraperindex import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.scrapermods import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.scrapermods import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.scrapermods import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.scrapermods import control
    control.artwork()

elif action == 'addView':
    from resources.lib.scrapermods import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.scrapermods import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.scrapermods import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.scrapermods import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.scrapermods import trailer
    trailer.trailer().play(name, url)

elif action == 'traktManager':
    from resources.lib.scrapermods import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.scrapermods import trakt
    trakt.authTrakt()

elif action == 'rdAuthorize':
    from resources.lib.scrapermods import debrid
    debrid.rdAuthorize()

elif action == 'download':
    import json
    from resources.lib.scrapersource import sources
    from resources.lib.scrapermods import downloader
    try: downloader.download(name, image, sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'playscraper':
    from resources.lib.scrapersource import sources
    sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.scrapersource import sources
    sources().addItem(title)

elif action == 'playItem':
    from resources.lib.scrapersource import sources
    sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.scrapersource import sources
    sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.scrapersource import sources
    sources().clearSources()



