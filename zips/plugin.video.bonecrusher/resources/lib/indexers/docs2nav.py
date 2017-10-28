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
        self.addDirectoryItem(32604, 'natutredocsNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32605, 'thebibleNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32606, 'ConspiraciesNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32607, 'mentalNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32608, 'killersNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32609, 'ufoNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32610, 'mythsNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32612, 'bioNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32611, 'addictionNavigator', 'documentary.png', 'DefaultMovies.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'documentary.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32010, 'movieSearch', 'documentary.png', 'DefaultMovies.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	
    def natutredocs(self, lite=False):
        self.addDirectoryItem('natutre docs movies', 'movies2&url=tmdbnature', 'documentary.png', 'DefaultRecentlyAddedMovies.png')      
        self.addDirectoryItem('natutre docs tv', 'tvshows&url=tmdbnature', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def bible(self, lite=False):
        self.addDirectoryItem('the bible movies', 'movies2&url=tmdbbible', 'documentary.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('the bible tv shows', 'tvshows&url=tmdbbible', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def Conspiracies(self, lite=False):
        self.addDirectoryItem('Conspiracies movies', 'movies2&url=tmdbConspiracies', 'documentary.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Conspiracies tv shows', 'tvshows&url=tmdbConspiracies', 'documentary.png', 'DefaultRecentlyAddedMovies.png')		
        self.endDirectory()
		
    def mental(self, lite=False):
        self.addDirectoryItem('Mental Health movies', 'movies2&url=tmdbmental', 'documentary.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Mental health tv shows', 'tvshows&url=tmdbmental', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def killers(self, lite=False):
        self.addDirectoryItem('Killers Movies', 'movies2&url=tmdbkillers', 'documentary.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Killer tv shows', 'tvshows&url=tmdbkillers', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def ufo(self, lite=False):
        self.addDirectoryItem('Ufo movies', 'movies2&url=tmdbufo', 'documentary.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Ufo tv shows', 'tvshows&url=tmdbufo', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Other Un Explained', 'movies2&url=tmdbother', 'documentary.png', 'decepticons.png')
        self.addDirectoryItem('Other Un Explained TV', 'tvshows&url=tmdbother', 'documentary.png', 'decepticons.png')
        self.endDirectory()

    def myths(self, lite=False):
        self.addDirectoryItem('Myths movies', 'movies2&url=tmdbmyths', 'documentary.png', 'DefaultRecentlyAddedMovies.png')      
        self.addDirectoryItem('Myths tv shows', 'tvshows&url=tmdbmyths', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('urban legends', 'movies2&url=tmdburban', 'documentary.png', 'decepticons.png')
        self.addDirectoryItem('urban legends TV', 'tvshows&url=tmdburban', 'documentary.png', 'decepticons.png')
        
        self.endDirectory()
		
    def addiction(self, lite=False):
        self.addDirectoryItem('addiction movies', 'movies2&url=tmdbaddiction', 'documentary.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('addiction tv shows ', 'tvshows&url=tmdbaddiction', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()

    def bio(self, lite=False):
        self.addDirectoryItem('Biographies movies', 'movies2&url=tmdbdbiographies', 'documentary.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Biographies tv shows', 'tvshows&url=tmdbdbiographies', 'documentary.png', 'DefaultRecentlyAddedMovies.png')
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


