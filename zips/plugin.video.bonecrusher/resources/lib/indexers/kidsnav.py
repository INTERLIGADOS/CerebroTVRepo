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
        self.addDirectoryItem(32599, 'KidsNavigator', 'Kids zone.png', 'DefaultMovies.png')
        self.addDirectoryItem(32552, 'toddlerNavigator', 'Kids zone.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32613, 'TeenNavigator', 'Kids zone.png', 'DefaultMovies.png')
        self.addDirectoryItem(32602, 'NatureNavigator', 'Kids zone.png', 'DefaultMovies.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'bct.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32010, 'movieSearch', 'bcser.png', 'DefaultMovies.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

    def Kids(self, lite=False):
        self.addDirectoryItem('Kids movies', 'movies2&url=tmdbKids', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Kids T.V Shows', 'tvshows&url=tmdbKids', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')
        self.endDirectory()
		
    def Teen(self, lite=False):
        self.addDirectoryItem('Teen Movies', 'movies2&url=tmdbteen', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')        
        self.addDirectoryItem('Teen T.v Shows', 'tvshows&url=tmdbteen', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')		
        self.endDirectory()
		
    def Nature(self, lite=False):
        self.addDirectoryItem('Nature And Learning Movies', 'movies2&url=tmdblearning', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')       
        self.addDirectoryItem('Nature  And Learning T.V Shows', 'tvshows&url=tmdblearning', 'Kids zone.png', 'DefaultRecentlyAddedMovies.png')

        self.endDirectory()

    def toddler(self, lite=False):
        self.addDirectoryItem('Toddler tv shows', 'tvshows&url=tmdbtoddler', 'Kids zone.png', 'decepticons.png')
        self.addDirectoryItem('Toddler movies', 'movies2&url=tmdbtoddler', 'Kids zone.png', 'decepticons.png')

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


