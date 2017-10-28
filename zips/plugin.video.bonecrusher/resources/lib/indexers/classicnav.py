# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
inprogress_db = control.setting('inprogress_db')

sysaddon = sys.argv[0]

syshandle = int(sys.argv[1])

artPath = control.artPath()

addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

	

class navigator:
    def root(self):
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', '', 'DefaultMovies.png')
        self.addDirectoryItem(32584, 'actionNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32585, 'adventureNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32586, 'animationNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32587, 'comedyNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32588, 'crimeNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32589, 'dramaNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32590, 'familyNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32591, 'fantasyNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32592, 'horrorNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32593, 'mysteryNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32594, 'romanceNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32595, 'scifiNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32596, 'thrillerNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32597, 'warNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32598, 'westernNavigator', 'classics.png', 'DefaultMovies.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'bct.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32010, 'movieSearch', 'bcser.png', 'DefaultMovies.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	
    def action(self, lite=False):
        self.addDirectoryItem('Classic action ', 'movies2&url=tmdbclaction', 'classics.png', 'DefaultRecentlyAddedMovies.png')      
        self.addDirectoryItem('Classic action ', 'tvshows&url=tmdbclaction', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def adventure(self, lite=False):
        self.addDirectoryItem('Classic adventure ', 'movies2&url=tmdbcladven', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic adventure  ', 'tvshows&url=tmdbcladven', 'classics.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
		
    def animation(self, lite=False):
        self.addDirectoryItem('Classic animation ', 'movies2&url=tmdbclanim', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic animation ', 'tvshows&url=tmdbclanim', 'classics.png', 'DefaultRecentlyAddedMovies.png')		
		
		
		
		

        self.endDirectory()
		
    def comedy(self, lite=False):
        self.addDirectoryItem('Classic comedy ', 'movies2&url=tmdbclcom', 'classics.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Classic comedy ', 'tvshows&url=tmdbclcom', 'classics.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
		
    def crime(self, lite=False):
        self.addDirectoryItem('Classic crime ', 'movies2&url=tmdbclcrime', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic crime ', 'tvshows&url=tmdbclcrime', 'classics.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()
		
    def drama(self, lite=False):
        self.addDirectoryItem('Classic drama ', 'movies2&url=tmdbcldram', 'classics.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Classic drama ', 'tvshows&url=tmdbcldram', 'classics.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()

    def family(self, lite=False):
        self.addDirectoryItem('Classic family ', 'movies2&url=tmdbclfam', 'classics.png', 'DefaultRecentlyAddedMovies.png')      
        self.addDirectoryItem('Classic family ', 'tvshows&url=tmdbclfam', 'classics.png', 'DefaultRecentlyAddedMovies.png')		
	
        self.endDirectory()
		
    def fantasy(self, lite=False):
        self.addDirectoryItem('Classic fantasy ', 'movies2&url=tmdbfancl', 'classics.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Classic fantasy ', 'tvshows&url=tmdbfancl', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def horror(self, lite=False):
        self.addDirectoryItem('Classic horror ', 'movies2&url=tmdbclhoro', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic horror ', 'tvshows&url=tmdbclhoro', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def mystery(self, lite=False):
        self.addDirectoryItem('Classic mystery ', 'movies2&url=tmdbclmys', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic mystery ', 'tvshows&url=tmdbclmys', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def romance(self, lite=False):
        self.addDirectoryItem('Classic romance ', 'movies2&url=tmdbclrom', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic romance ', 'tvshows&url=tmdbclrom', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def scifi(self, lite=False):
        self.addDirectoryItem('Classic scifi ', 'movies2&url=tmdbclscifi', 'classics.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Classic scifi ', 'tvshows&url=tmdbclscifi', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def thriller(self, lite=False):
        self.addDirectoryItem('Classic thriller ', 'movies2&url=tmdbclthrill', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Classic thriller ', 'tvshows&url=tmdbclthrill', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def war(self, lite=False):
        self.addDirectoryItem('Classic war', 'movies2&url=tmdbclwar', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Classic war', 'tvshows&url=tmdbclwar', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def western(self, lite=False):
        self.addDirectoryItem('Classic western movies', 'movies2&url=tmdbwesterns2', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Classic western tv shows', 'tvshows&url=tmdbwesterns2', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
   

		
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'urlresolversettings', 'tools.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=4.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=6.0', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Views', 'viewsNavigator', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Providers', 'clearSources', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Cache', 'clearCache', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'tools.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher[/B]: Clear Progress Database', 'clearProgress', 'tools.png', 'DefaultAddonProgram.png')

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'movies.png', 'DefaultMovies.png', isAction=False)
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
        control.directory(syshandle, cacheToDisc=True)


