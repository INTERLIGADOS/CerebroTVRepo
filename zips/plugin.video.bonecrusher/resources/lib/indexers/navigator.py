# -*- coding: utf-8 -*-
import os,sys,urlparse,base64

from resources.lib.modules import control
from resources.lib.modules import trakt
inprogress_db = control.setting('inprogress_db')

sysaddon = base64.b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLmJvbmVjcnVzaGVyLw==')

syshandle = int(sys.argv[1])

artPath = control.artPath()

addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

movielist1 = control.setting('tmdb.movielist_name1')		
movielist2 = control.setting('tmdb.movielist_name2')		
movielist3 = control.setting('tmdb.movielist_name3')		
movielist4 = control.setting('tmdb.movielist_name4')		
movielist5 = control.setting('tmdb.movielist_name5')		
movielist6 = control.setting('tmdb.movielist_name6')		
movielist7 = control.setting('tmdb.movielist_name7')		
movielist8 = control.setting('tmdb.movielist_name8')		
movielist9 = control.setting('tmdb.movielist_name9')		
movielist10 = control.setting('tmdb.movielist_name10')

tvlist1 = control.setting('tmdb.tvlist_name1')		
tvlist2 = control.setting('tmdb.tvlist_name2')		
tvlist3 = control.setting('tmdb.tvlist_name3')		
tvlist4 = control.setting('tmdb.tvlist_name4')		
tvlist5 = control.setting('tmdb.tvlist_name5')		
tvlist6 = control.setting('tmdb.tvlist_name6')		
tvlist7 = control.setting('tmdb.tvlist_name7')		
tvlist8 = control.setting('tmdb.tvlist_name8')		
tvlist9 = control.setting('tmdb.tvlist_name9')		
tvlist10 = control.setting('tmdb.tvlist_name10')		
class navigator:
    def root(self):
#       self.addDirectoryItem('pair', 'pairNavigator', 'team.png', 'decepticons.png')
        self.addDirectoryItem(32571, 'KrestsNavigator', 'Krests Wishes.png', 'decepticons.png')
        self.addDirectoryItem(32573, 'teamNavigator', 'team.png', 'decepticons.png')
        self.addDirectoryItem(32600, 'classicsNavigator', 'classics.png', 'decepticons.png')
        self.addDirectoryItem(32535, 'boxsetsNavigator', 'box sets.png', 'decepticons.png')
        self.addDirectoryItem(32599, 'kids2Navigator', 'Kids zone.png', 'decepticons.png')
        self.addDirectoryItem(32550, 'oddsNavigator', 'Users requests.png', 'decepticons.png')
        self.addDirectoryItem(32536, 'docs2navNavigator', 'documentary.png', 'decepticons.png')
        self.addDirectoryItem(32001, 'movieNavigator', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(32583, 'giftsNavigator', 'gifts1.png', 'decepticons.png')
        self.addDirectoryItem(32002, 'tvNavigator', 'BCTV.png', 'decepticons.png')
        # self.addDirectoryItem('Spotlight', 'movieWidget', 'bcsl.png', 'decepticons.png')
        self.addDirectoryItem('New Movies', 'movies&url=premiere', 'bcnm.png', 'decepticons.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem('My Bone Crusher', 'lists_navigator', 'icon.png', 'decepticons.png')
        self.addDirectoryItem(32027, 'calendars', 'bc c.png', 'decepticons.png')
        # self.addDirectoryItem(32007, 'channels', 'bc ch.png', 'decepticons.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'bct.png', 'DefaultAddonProgram.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'decepticons.png', 'DefaultFolder.png')

        self.addDirectoryItem(32010, 'searchNavigator', 'bcser.png', 'DefaultFolder.png')
        self.addDirectoryItem('Changelog', 'ShowChangelog', 'change log.png', 'DefaultFolder.png')
        self.endDirectory()

    def movies(self, lite=False):
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Featured', 'movies&url=featured', 'Featured.png', 'decepticons.png')
        self.addDirectoryItem('Trending', 'movies&url=trending', 'Trending.png', 'decepticons.png')
        self.addDirectoryItem('Populars', 'movies&url=popular', 'Populars.png', 'decepticons.png')
        self.addDirectoryItem('New Movies', 'movies&url=premiere', 'bcnm.png', 'decepticons.png')
        self.addDirectoryItem('Top Rated', 'movies&url=views', 'Top Rated.png', 'decepticons.png')
        self.addDirectoryItem('In Theaters', 'movies&url=theaters', 'In Theaters.png', 'decepticons.png')
        self.addDirectoryItem('Marvel Universe', 'movies&url=tmdbmarvel', 'Marvel.png', 'decepticons.png')
        self.addDirectoryItem('Oscar Winners', 'movies&url=tmdboscars', 'Oscar Winners.png', 'decepticons.png')
        self.addDirectoryItem('Disney Collection', 'movies&url=tmdbdisney', 'Disney.png', 'decepticons.png')
        self.addDirectoryItem('Genres', 'movieGenres', 'Genres.png', 'decepticons.png')
        self.addDirectoryItem('Years', 'movieYears', 'Years.png', 'decepticons.png')
        self.addDirectoryItem('Persons', 'moviePersons', 'Persons.png', 'decepticons.png')
        self.addDirectoryItem('Certificates', 'movieCertificates', 'Certificates.png', 'decepticons.png')
        self.addDirectoryItem(32028, 'moviePerson', 'bcser.png', 'decepticons.png')
        self.addDirectoryItem(32010, 'movieSearch', 'bcser.png', 'decepticons.png')


        self.endDirectory()

    def lists_navigator(self):
        self.addDirectoryItem('[WATCHLIST] Movies', 'movieFavourites', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem('[WATCHLIST] TV Shows', 'tvFavourites', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem('[TMDB LIST] Movies', 'movielist', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem('[TMDB LIST] Tv Shows', 'tvlist', 'BCTV.png', 'decepticons.png')

        self.endDirectory()
		
    def mymovies(self):
        self.addDirectoryItem(movielist1, 'movies&url=mycustomlist1', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist2, 'movies&url=mycustomlist2', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist3, 'movies&url=mycustomlist3', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist4, 'movies&url=mycustomlist4', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist5, 'movies&url=mycustomlist5', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist6, 'movies&url=mycustomlist6', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist7, 'movies&url=mycustomlist7', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist8, 'movies&url=mycustomlist8', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist9, 'movies&url=mycustomlist9', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(movielist10, 'movies&url=mycustomlist10', 'BC MOVIES.png', 'decepticons.png')
        self.endDirectory()

    def mytv(self):
        self.addDirectoryItem(tvlist1, 'tvshows&url=mycustomlist1', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist2, 'tvshows&url=mycustomlist2', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist3, 'tvshows&url=mycustomlist3', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist4, 'tvshows&url=mycustomlist4', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist5, 'tvshows&url=mycustomlist5', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist6, 'tvshows&url=mycustomlist6', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist7, 'tvshows&url=mycustomlist7', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist8, 'tvshows&url=mycustomlist8', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist9, 'tvshows&url=mycustomlist9', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(tvlist10, 'tvshows&url=mycustomlist10', 'BCTV.png', 'decepticons.png')
        self.endDirectory()

    def tvshows(self, lite=False):
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'BCTV.png', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Featured', 'tvshows&url=featured', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem('Populars', 'tvshows&url=popular', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem(32019, 'tvshows&url=views', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem(32026, 'tvshows&url=premiere', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem(32025, 'tvshows&url=active', 'BCTV.png', 'BCTV.png')       
        self.addDirectoryItem(32023, 'tvshows&url=rating', 'BCTV.png', 'BCTV.png')
 
        self.addDirectoryItem(32011, 'tvGenres', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem(32016, 'tvNetworks', 'BCTV.png', 'BCTV.png')
        self.addDirectoryItem(32024, 'tvshows&url=airing', 'airing-today.png', 'BCTV.png')
        self.addDirectoryItem(32027, 'calendars', 'bc c.png', 'decepticons.png')



        self.addDirectoryItem(32010, 'tvSearch', 'bcser.png', 'decepticons.png')

        self.endDirectory()
		
    def pair(self):
        xbmc.executebuiltin('RunScript("script.triangulum.pair")')
        self.endDirectory()
		
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'urlresolversettings', 'Settings.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'Settings.png', 'DefaultAddonProgram.png')
        # self.addDirectoryItem(32044, 'openSettings&query=3.1', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Providers', 'openSettings&query=3.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Debrid', 'openSettings&query=4.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=5.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Subtitles', 'openSettings&query=6.0', 'Settings.png', 'DefaultAddonProgram.png') 
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=7.0', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Lists', 'openSettings&query=8.0', 'Settings.png', 'DefaultAddonProgram.png')
		
        self.addDirectoryItem('[B]Bone Crusher[/B]: Views', 'viewsNavigator', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Providers', 'clearSources', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Cache', 'clearCache', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'Settings.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Progress Database', 'clearProgress', 'Settings.png', 'DefaultAddonProgram.png')
 
	
		
        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')
        tv_downloads = control.setting('tv.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'downloads.png', 'icon.png', isAction=False)
        self.endDirectory()


    def search(self):
        self.addDirectoryItem(32001, 'movieSearch', 'BC MOVIES.png', 'icon.png')
        self.addDirectoryItem(32002, 'tvSearch', 'BCTV.png', 'decepticons.png')
        self.addDirectoryItem(32029, 'moviePerson', 'BC MOVIES.png', 'decepticons.png')
        self.addDirectoryItem(32030, 'tvPerson', 'BCTV.png', 'decepticons.png')

        self.endDirectory()


    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import cache
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        # control.do_block_check(False)
        control.directory(syshandle, cacheToDisc=True)


