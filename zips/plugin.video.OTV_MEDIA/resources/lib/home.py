#-*- coding: utf-8 -*-
import urllib2, urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, shutil, time, zipfile, re, stat, xbmcvfs, base64
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.siteHandler import cSiteHandler
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.db import cDb
import os
import urllib
import xbmc
def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku  
url1="PT1BYnRobkwyUkhjcDlpYmhsbmNrRjJMbkozYnVRM2NweG1iaGxuY2tGMkx2b0RjMFJIYQ=="
url2 = base64.b64decode(url1)
url3 =  okuoku(url2)            
streamurl=base64.b64decode(url3)
SITE_IDENTIFIER = 'cHome'
SITE_NAME = 'Home'
color_cherches = cConfig().getSetting('color_cherches')
color_cherchev = cConfig().getSetting('color_cherchev')
color_iptv = cConfig().getSetting('color_iptv')
color_films = cConfig().getSetting('color_films')
color_series = cConfig().getSetting('color_series')
color_anims = cConfig().getSetting('color_anims')
color_tvs = cConfig().getSetting('color_tvs')
color_sports = cConfig().getSetting('color_sports')
color_docs = cConfig().getSetting('color_docs')
color_videos = cConfig().getSetting('color_videos')
color_replaytvs = cConfig().getSetting('color_replaytvs')

class cHome:
        

    def load(self):
        oGui = cGui()

        if (cConfig().getSetting('home_films') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR '+color_cherches+']'+cConfig().getlanguage(30076)+'[/COLOR]', 'search.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_cherchev') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('turkvod_org', 'showGenre', '[COLOR '+color_cherchev+']'+cConfig().getlanguage(30114)+'[/COLOR]', 'searchtmdb.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_cherchev') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('myvideo_az', 'showGenre', '[COLOR '+color_cherchev+']'+cConfig().getlanguage(30088)+'[/COLOR]', 'searchtmdb.png', oOutputParameterHandler)
        
        if (cConfig().getSetting('home_tv') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('filmon_com', 'showGenre', '[COLOR '+color_tvs+']'+cConfig().getlanguage(30115)+'[/COLOR]', 'tv.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_tvs') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'MCategories', '[COLOR '+color_tvs+']'+cConfig().getlanguage(30116)+'[/COLOR]', 'tv.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_replaytvs') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('youtubecom_tr', 'showGenre', '[COLOR '+color_tvs+']'+cConfig().getlanguage(30117)+'[/COLOR]', 'tv.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_iptv') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'Iptvint2', '[COLOR '+color_iptv+']'+cConfig().getlanguage(30118)+'[/COLOR]', 'tv.png', oOutputParameterHandler)

        
        if (cConfig().getSetting('home_series') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+'[/COLOR]', 'series.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_anims') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('ustream_tv', 'showGenre', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+'[/COLOR]', 'animes.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_docs') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir('myvideo_ge', 'showGenre', '[COLOR '+color_docs+']'+cConfig().getlanguage(30112)+'[/COLOR]', 'doc.png', oOutputParameterHandler)

        if (cConfig().getSetting('home_sports') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'sportSports', '[COLOR '+color_sports+']'+cConfig().getlanguage(30113)+'[/COLOR]', 'sport.png', oOutputParameterHandler)

       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'UpateCategories', '[COLOR teal]'+cConfig().getlanguage(30210)+'[/COLOR]', 'mark.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER,'localplaylist', '[COLOR teal]My PlayList[/COLOR]', 'download.png', oOutputParameterHandler)

        
        
        if (cConfig().getSetting('home_update') == 'true'):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            oGui.addDir(SITE_IDENTIFIER, 'showUpdate', '[COLOR green]Update -Guncelleme[/COLOR]', 'update.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()
        if (cConfig().getSetting("active-view") == 'true'):
            xbmc.executebuiltin('Container.SetViewMode(%s)' % cConfig().getSetting('accueil-view'))

    def showUpdate(self):
        try:
            from resources.lib.about import cAbout
            cAbout().checkdownload()
        except:
            pass
        return

    def showDocs(self):
        oGui = cGui()

        # Affiche les Nouveautés Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'docNews', '[COLOR '+color_docs+']'+cConfig().getlanguage(30112)+' ('+cConfig().getlanguage(30101)+')[/COLOR]', 'news.png', oOutputParameterHandler)

        # Affiche les Genres Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'docGenres', '[COLOR '+color_docs+']'+cConfig().getlanguage(30112)+' ('+cConfig().getlanguage(30105)+')[/COLOR]', 'genres.png', oOutputParameterHandler)

        # Affiche les Sources Documentaires
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'docDocs', '[COLOR '+color_docs+']'+cConfig().getlanguage(30138)+'[/COLOR]', 'host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showNets(self):
        oGui = cGui()

        # Affiche les Nouveautés Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'netsNews', '[COLOR '+color_videos+']'+cConfig().getlanguage(30114)+' ('+cConfig().getlanguage(30101)+')[/COLOR]', 'news.png', oOutputParameterHandler)

        # Affiche les Genres Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'netsGenres', '[COLOR '+color_videos+']'+cConfig().getlanguage(30114)+' ('+cConfig().getlanguage(30105)+')[/COLOR]', 'genres.png', oOutputParameterHandler)

        # Affiche les Sources Vidéos
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieNets', '[COLOR '+color_videos+']'+cConfig().getlanguage(30138)+'[/COLOR]', 'host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showTV(self):
        oGui = cGui()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('iptvbox', 'load', '[COLOR '+color_tvs+']Television Box[/COLOR]', 'tv.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir('myvideo_az', 'showGenre', '[COLOR '+color_tvs+']Tv du net[/COLOR]', 'tv.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showMovies(self):
        oGui = cGui()
                
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'TurkCategories', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30101)+')[/COLOR]', 'films_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieViews', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30102)+')[/COLOR]', 'films_views.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieHD', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30160)+')[/COLOR]', 'films_hd.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieComments', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30103)+')[/COLOR]', 'films_comments.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieNotes', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30104)+')[/COLOR]', 'films_notes.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieGenres', '[COLOR '+color_films+']'+cConfig().getlanguage(30076)+' ('+cConfig().getlanguage(30105)+')[/COLOR]', 'films_genres.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        # oGui.addDir(SITE_IDENTIFIER, 'movieVF', '[COLOR '+color_films+']'+cConfig().getlanguage(30134)+'[/COLOR]', 'films_vf.png', oOutputParameterHandler)

        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        # oGui.addDir(SITE_IDENTIFIER, 'movieVOSTFR', '[COLOR '+color_films+']'+cConfig().getlanguage(30135)+'[/COLOR]', 'films_vostfr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'movieMovie', '[COLOR '+color_films+']'+cConfig().getlanguage(30138)+'[/COLOR]', 'films_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showSeries(self):
        oGui = cGui()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'serieNews', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+' ('+cConfig().getlanguage(30134)+')[/COLOR]', 'series_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'serieGenres', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+' ('+cConfig().getlanguage(30135)+')[/COLOR]', 'series_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'Almantv', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+' ('+cConfig().getlanguage(30107)+')[/COLOR]', 'series_vf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'serieVostfrs', '[COLOR '+color_series+']'+cConfig().getlanguage(30121)+' ('+cConfig().getlanguage(30108)+')[/COLOR]', 'series_vostfr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'serieSeries', '[COLOR '+color_series+']'+cConfig().getlanguage(30138)+'[/COLOR]', 'series_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def showAnimes(self):
        oGui = cGui()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'animNews', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+' ('+cConfig().getlanguage(30101)+')[/COLOR]', 'animes_news.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'animVfs', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+' ('+cConfig().getlanguage(30107)+')[/COLOR]', 'animes_vf.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'animVostfrs', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+' ('+cConfig().getlanguage(30108)+')[/COLOR]', 'animes_vostfr.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'animGenres', '[COLOR '+color_anims+']'+cConfig().getlanguage(30122)+' ('+cConfig().getlanguage(30199)+')[/COLOR]', 'animes_genres.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oGui.addDir(SITE_IDENTIFIER, 'animAnims', '[COLOR '+color_anims+']'+cConfig().getlanguage(30138)+'[/COLOR]', 'animes_host.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()

   
    def showSources(self):
        oGui = cGui()

        oPluginHandler = cPluginHandler()
        aPlugins = oPluginHandler.getAvailablePlugins()
        for aPlugin in aPlugins:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
            icon = 'sayfalar/%s.png' % (aPlugin[1])
            oGui.addDir(aPlugin[1], 'load', aPlugin[0], icon, oOutputParameterHandler)

        oGui.setEndOfDirectory()

    def movieMovie(self):
        self.__callpluging('MOVIE_MOVIE', color_films, 'films_host.png')

    def movieTurk(self):
        self.__callpluging('MOVIE_TURK', color_films, 'films_news.png')

    def movieViews(self):
        self.__callpluging('MOVIE_VIEWS', color_films, 'films_views.png')

    def movieHD(self):
        self.__callpluging('MOVIE_HD', color_films, 'films_hd.png')

    def movieComments(self):
        self.__callpluging('TURK_SINEMA', color_films, 'films_comments.png')

    def movieNotes(self):
        self.__callpluging('MOVIE_NOTES', color_films, 'films_notes.png')

    def movieGenres(self):
        self.__callpluging('RADYO_GENRES', color_films, 'films_genres.png')

    def movieVF(self):
        self.__callpluging('MOVIE_VF', color_films, 'films_vf.png')

    def movieVOSTFR(self):
        self.__callpluging('MOVIE_VOSTFR', color_films, 'films_vostfr.png')

    def serieSeries(self):
        self.__callpluging('SERIE_SERIES', color_series, 'series_host.png')

    def serieNews(self):
        self.__callpluging('ALMAN_SINEMA', color_series, 'series_news.png')

    def serieVfs(self):
        self.__callpluging('ALMAN_TV', color_series, 'series_vf.png')

    def serieVostfrs(self):
        self.__callpluging('ADULT_ADULT', color_series, 'series_vostfr.png')

    def serieGenres(self):
        self.__callpluging('ALMAN_RADIO', color_series, 'series_genres.png')

    def animAnims(self):
        self.__callpluging('ANIM_ANIMS', color_anims, 'animes_host.png')

    def animNews(self):
        self.__callpluging('ANIM_NEWS', color_anims, 'animes_news.png')

    def animVfs(self):
        self.__callpluging('ANIM_VFS', color_anims, 'animes_vf.png')

    def animGenres(self):
        self.__callpluging('ANIM_GENRES', color_anims, 'animes_genres.png')

    def animVostfrs(self):
        self.__callpluging('ANIM_VOSTFRS', color_anims , 'animes_vostfr.png')

    def animMovies(self):
        self.__callpluging('ANIM_MOVIES', color_anims, 'animes.png')

    def docDocs(self):
        self.__callpluging('DOC_DOCS', color_docs, 'doc.png')

    def docNews(self):
        self.__callpluging('DOC_NEWS', color_docs, 'news.png')

    def docGenres(self):
        self.__callpluging('DOC_GENRES', color_docs, 'genres.png')

    def sportSports(self):
        self.__callpluging('SPORT_SPORTS', color_sports, 'sport.png')

    def movieNets(self):
        self.__callpluging('MOVIE_NETS', color_videos, 'buzz.png')

    def netsNews(self):
        self.__callpluging('NETS_NEWS', color_videos, 'news.png')

    def  netsGenres(self):
        self.__callpluging('NETS_GENRES', color_videos, 'genres.png')

    def replayReplay(self):
        self.__callpluging('REPLAYTV_REPLAYTV', color_replaytvs, 'replay_host.png')

    def replayNews(self):
        self.__callpluging('REPLAYTV_NEWS', color_replaytvs, 'replay_news.png')

    def replayGenres(self):
        self.__callpluging('REPLAYTV_GENRES', color_replaytvs, 'replay_genres.png')

    def showSearch(self):

        if (cConfig().getSetting("history-view") == 'true'):
            readdb = 'True'
        else:
            readdb = 'False'

        oGui = cGui()

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oOutputParameterHandler.addParameter('disp', 'search1')
        oOutputParameterHandler.addParameter('readdb', readdb)
        sLabel1 = cConfig().getlanguage(30077)+": "+cConfig().getSetting('search1_label')
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', sLabel1, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oOutputParameterHandler.addParameter('disp', 'search2')
        oOutputParameterHandler.addParameter('readdb', readdb)
        sLabel2 = cConfig().getlanguage(30089)+": "+cConfig().getSetting('search2_label')
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', sLabel2, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oOutputParameterHandler.addParameter('disp', 'search3')
        oOutputParameterHandler.addParameter('readdb', readdb)
        sLabel3 = cConfig().getlanguage(30090)+": "+cConfig().getSetting('search3_label')
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', sLabel3, 'search.png', oOutputParameterHandler)

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oOutputParameterHandler.addParameter('disp', 'search4')
        oOutputParameterHandler.addParameter('readdb', readdb)
        sLabel4 = cConfig().getlanguage(30091)+": "+cConfig().getSetting('search4_label')
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', sLabel4, 'search.png', oOutputParameterHandler)


        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
        oOutputParameterHandler.addParameter('disp', 'search10')
        oOutputParameterHandler.addParameter('readdb', readdb)
        oGui.addDir(SITE_IDENTIFIER, 'searchMovie', '[COLOR orange]Search: Alluc_ee[/COLOR]', 'search.png', oOutputParameterHandler)

        #history
        if (cConfig().getSetting("history-view") == 'true'):

            row = cDb().get_history()
            if row:
                oGui.addText(SITE_IDENTIFIER, "[COLOR azure]Your History[/COLOR]")
            for match in row:

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
                oOutputParameterHandler.addParameter('searchtext', match[1])
                oOutputParameterHandler.addParameter('disp', match[2])
                oOutputParameterHandler.addParameter('readdb', 'False')
                oGui.addDir(SITE_IDENTIFIER, 'searchMovie', "- "+match[1], 'search.png', oOutputParameterHandler)

            if row:

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
                oGui.addDir(SITE_IDENTIFIER, 'delSearch', '[COLOR red]Remove l\'historique[/COLOR]', 'search.png', oOutputParameterHandler)


        oGui.setEndOfDirectory()

    def searchMovie2(self):
        oInputParameterHandler = cInputParameterHandler()
        sDisp = oInputParameterHandler.getValue('disp')
        oHandler = cRechercheHandler()
        liste = oHandler.getAvailablePlugins(sDisp)
        self.__callsearch(liste, sDisp)

    def delSearch(self):
        cDb().del_history()
        return True


    def __callpluging(self, sVar, sColor, sIcon):
        oGui = cGui()
        oPluginHandler = cSiteHandler()
        aPlugins = oPluginHandler.getAvailablePlugins(sVar)
        for aPlugin in aPlugins:
            try:
                #exec "import "+aPlugin[1]
                #exec "sSiteUrl = "+aPlugin[1]+"."+sVar
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', aPlugin[0])
                icon = 'sayfalar/%s.png' % (aPlugin[2])
                oGui.addDir(aPlugin[2], aPlugin[3], '[COLOR '+sColor+']'+aPlugin[1]+'[/COLOR]', icon, oOutputParameterHandler)
            except:
                pass

        oGui.setEndOfDirectory()

    def searchMovie(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('searchtext')
        sReadDB = oInputParameterHandler.getValue('readdb')
        sDisp = oInputParameterHandler.getValue('disp')

        oHandler = cRechercheHandler()
        oHandler.setText(sSearchText)
        oHandler.setDisp(sDisp)
        aPlugins = oHandler.getAvailablePlugins()

        if (sReadDB != 'False' and aPlugins == True):
            meta = {}
            meta['title'] = oHandler.getText()
            meta['disp'] = oHandler.getDisp()
            cDb().insert_history(meta)
                        
        oGui.setEndOfDirectory()
    
    def Iptvint2(self):
        oGui = cGui()
        from default import Iptvint2
        Iptvint2()  
    def TurkCategories(self):
        oGui = cGui()
        from resources.sayfalar.iptvbox import iptvturk
        iptvturk()                   
    
    
    def UpateCategories(self):
        oGui = cGui()
        from default import *
        checkforupdates(REMOTE_VERSION_FILE, LOCAL_VERSION_FILE,0)
        if Addon.getSetting('autoupdate') == "true":
            comon.write_file(Tfile , '*')        
        sys.exit()

    def PlaylistCategories(self):
        oGui = cGui()
        from default  import PlaylistCategories
        PlaylistCategories()                   
                    
    def Almantv(self):
        oGui = cGui()
        from default import Almantv
        Almantv() 
    
    def MCategories(self):
        oGui = cGui()
        from default  import MCategories
        MCategories() 