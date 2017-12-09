# -*- coding: utf-8 -*-

'''
    showboxarize2 Add-on

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


import urlparse,sys,urllib
import xbmcaddon,xbmcplugin,xbmcgui,xbmc

#addon_handle = int(sys.argv[1])
#xbmcplugin.setContent(addon_handle, 'movies')

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')


if action == None:
    from resources.lib.indexers import navigator
    navigator.navigator().root()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'smuSettings':
    try: import urlresolver
    except: pass
    urlresolver.display_settings()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)
    #xbmcplugin.setContent(addon_handle, 'movies')

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()
    #xbmcplugin.setContent(addon_handle, 'movies')
	
elif action == 'pair':
    xbmc.executebuiltin('RunAddon(script.cerebro.pairwith.laucnher)')
