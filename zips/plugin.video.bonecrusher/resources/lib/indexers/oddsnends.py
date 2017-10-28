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
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem(32546, 'KfulegNavigator', 'Kung fu.png', 'decepticons.png')
#       self.addDirectoryItem(32574, 'metalNavigator', 'Rock.png', 'decepticons.png')
        self.addDirectoryItem(32544, 'MlNavigator', 'legends.png', 'decepticons.png')
        self.addDirectoryItem(32547, 'SwmNavigator', 'Sports.png', 'decepticons.png')
        self.addDirectoryItem(32578, 'darktvNavigator', 'groups.png', 'decepticons.png')
        self.addDirectoryItem(32558, 'amNavigator', 'anime.png', 'decepticons.png')
        self.addDirectoryItem(32540, 'SfimNavigator', 'Sci fi.png', 'decepticons.png')
        self.addDirectoryItem(32537, 'ParamNavigator', 'paranormal.png', 'decepticons.png')
        self.addDirectoryItem(32542, 'BrNavigator', 'B rated.png', 'decepticons.png')
        self.addDirectoryItem(32543, 'MhNavigator', 'Morbid.png', 'decepticons.png')
        self.addDirectoryItem(32572, 'kocNavigator', 'comedy.png', 'decepticons.png')
        self.addDirectoryItem(32582, 'qocNavigator', 'comedy.png', 'decepticons.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'bct.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32010, 'movieSearch', 'bcser.png', 'decepticons.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	


    def Clts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]More To Come[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('canada loves tv shows', 'tvshows&url=tmdbcanada', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Canada loves movies', 'movies2&url=tmdbcanada', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def at(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('anime tv', 'tvshows&url=tmdbanime', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Anime movies', 'movies2&url=tmdbanime', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def Tl(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Elvis Movies', 'movies2&url=tmdbelvis', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('Elvis Tv Shows', 'tvshows&url=tmdbelvis', 'classics.png', 'DefaultRecentlyAddedMovies.png')
        self.addDirectoryItem('horror legends ', 'movies2&url=tmdbHorroricons', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Clint Eastwood movies ', 'movies2&url=tmdbeastwood', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Clint Eastwood tv ', 'tvshows&url=tmdbeastwood', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('John Wayne ', 'movies2&url=tmdbjwayne', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('John Wayne tv shows', 'tvshows&url=tmdbjwayne', 'decepticons.png', 'decepticons.png')
        self.endDirectory()
		
    def Sfts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sci fi tv shows', 'tvshows&url=tmdbScfinew', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sci fi movies', 'movies2&url=tmdbScfinew', 'decepticons.png', 'decepticons.png')

        self.endDirectory()

    def Paratv(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem(' paranormal tv', 'tvshows&url=tmdbparanormal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('paranormal Movies', 'movies2&url=tmdbparanormal', 'decepticons.png', 'decepticons.png')



        self.endDirectory()

    def Kfuleg(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jet Li', 'movies2&url=tmdbjli', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Chuck Norris', 'movies2&url=tmdbchuck', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jackie Chan', 'movies2&url=tmdbchan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jean Claude Van Damme', 'movies2&url=tmdbtmdbdam', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Steven Seagal', 'movies2&url=tmdbsegal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Chow Yun-Fat', 'movies2&url=tmdbYunFat', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tony Jaa', 'movies2&url=tmdbJaa', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Donnie Yen', 'movies2&url=tmdbYen', 'decepticons.png', 'decepticons.png')

        self.endDirectory()


		
    def Br(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('B rated', 'movies2&url=tmdbBr', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def Mh(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Morbid minded movies', 'movies2&url=tmdbMh', 'decepticons.png', 'decepticons.png')



        self.endDirectory()


    def Swm(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hockey movies', 'movies2&url=tmdbhockey', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Baseball movies', 'movies2&url=tmdbBaseball', 'decepticons.png', 'decepticons.png')  
        self.addDirectoryItem('Soccer movies', 'movies2&url=tmdbSoccer', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Football movies', 'movies2&url=tmdbFootball', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Basketball movies', 'movies2&url=tmdbBasketball', 'decepticons.png', 'decepticons.png')
        self.endDirectory()

    def koc(self, lite=False):
        self.addDirectoryItem('adam sandler', 'movies2&url=tmdbadamsandler', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Gene Wilder', 'movies2&url=tmdbGeneWilder', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('bill murray', 'movies2&url=tmdbbillmurray', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('richard pryor', 'movies2&url=tmdbrichardpryor', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('eddie murphy', 'movies2&url=tmdbeddiemurphy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('George carlin', 'movies2&url=tmdbcarlin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Red fox', 'movies2&url=tmdbfox', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Red fox tv shows', 'tvshows&url=tmdbfox', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Brooks mel', 'movies2&url=tmdbBrooks', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('laurel and hardy', 'movies2&url=tmdblaurel', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('laurel and hardy tv shows', 'tvshows&url=tmdblaurel', 'decepticons.png', 'decepticons.png')

        self.endDirectory()

    def qoc(self, lite=False):
        self.addDirectoryItem('Lucy Ball', 'tvshows2&url=tmdbBall', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('carol Burnett', 'movies2&url=tmdbBurnett', 'decepticons.png', 'decepticons.png')


        self.endDirectory()

    def darktv(self, lite=False):
        self.addDirectoryItem('dark tv movies', 'movies2&url=tmdbdarktv', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('dark tv tv shows', 'tvshows&url=tmdbdarktv', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('firestick movies', 'movies2&url=tmdbfirestick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('firestick tv shows', 'tvshows&url=tmdbfirestick', 'decepticons.png', 'decepticons.png')
        

        self.endDirectory()

    def gifts(self, lite=False):
        self.addDirectoryItem('heavenly gifts movies', 'movies2&url=tmdbgifts', 'gifts1.png', 'decepticons.png')
        self.addDirectoryItem('heavenly gifts tv shows', 'tvshows&url=tmdbgifts', 'gifts1.png', 'decepticons.png')
        self.addDirectoryItem('Leons  movies', 'movies2&url=tmdbleon', 'gifts1.png', 'decepticons.png')
        self.addDirectoryItem('Leons tv shows', 'tvshows&url=tmdbleon', 'gifts1.png', 'decepticons.png')
        self.endDirectory()

      
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'urlresolversettings', 'decepticons.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=4.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=6.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Views', 'viewsNavigator', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Providers', 'clearSources', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Cache', 'clearCache', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Progress Database', 'clearProgress', 'decepticons.png', 'DefaultAddonProgram.png')

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'decepticons.png', 'decepticons.png', isAction=False)
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


