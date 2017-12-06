#-*- coding: utf-8 -*-

from resources.lib.handler.jdownloaderHandler import cJDownloaderHandler
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.gui.contextElement import cContextElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.player import cPlayer
from resources.lib.db import cDb
from resources.lib.koditools import * 
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.config import cConfig
from resources.lib.util import cUtil
import xbmc
import urllib,urllib2,re,sys

class cHosterGui:

    SITE_NAME = 'cHosterGui'
                  
    # step 1 - bGetRedirectUrl in ein extra optionsObject verpacken
    def showHoster(self, oGui, oHoster, sMediaUrl, sThumbnail, bGetRedirectUrl = False):
        
        #oInputParameterHandler = cInputParameterHandler()
        #aParams = oInputParameterHandler.getAllParameter()
        
        oGuiElement = cGuiElement()
        oGuiElement.setSiteName(self.SITE_NAME)
        #oGuiElement.setFunction('showHosterMenu')
        oGuiElement.setFunction('play')
        oGuiElement.setTitle(oHoster.getDisplayName())
        #oGuiElement.setThumbnail(sThumbnail)
        # if (oInputParameterHandler.exist('sMeta')):
            # sMeta = oInputParameterHandler.getValue('sMeta')
            # oGuiElement.setMeta(int(sMeta))
            
        oGuiElement.setFileName(oHoster.getFileName())
        oGuiElement.getInfoLabel()
        oGuiElement.setCat(4)
        #oGuiElement.setThumbnail(xbmc.getInfoLabel('ListItem.Art(thumb)'))
        if sThumbnail:
            oGuiElement.setThumbnail(sThumbnail)
            
        #oGuiElement.setMeta(1)
        oGuiElement.setIcon('host.png')
               
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('sMediaUrl', sMediaUrl)
        #oOutputParameterHandler.addParameter('sThumbnail', oGuiElement.getThumbnail())

        oOutputParameterHandler.addParameter('sHosterIdentifier', oHoster.getPluginIdentifier())
        oOutputParameterHandler.addParameter('bGetRedirectUrl', bGetRedirectUrl)
        oOutputParameterHandler.addParameter('sFileName', oHoster.getFileName())

        oOutputParameterHandler.addParameter('sTitle', oHoster.getDisplayName())
        oOutputParameterHandler.addParameter('sId', 'cHosterGui')
        oOutputParameterHandler.addParameter('siteUrl', sMediaUrl)
        #oOutputParameterHandler.addParameter('sFav', 'play')
        #oOutputParameterHandler.addParameter('sCat', '4')
        
        oGui.createContexMenuWatch(oGuiElement, oOutputParameterHandler)
        
        #context playlit menu
        oContext = cContextElement()
        oContext.setFile('cHosterGui')
        oContext.setSiteName(self.SITE_NAME)
        oContext.setFunction('addToPlaylist')
        oContext.setTitle(cConfig().getlanguage(30201))
        oContext.setOutputParameterHandler(oOutputParameterHandler)
        oGuiElement.addContextItem(oContext)
        
        #Download menu
        if (oHoster.isDownloadable() == True):
            oContext = cContextElement()
            oContext.setFile('cDownload')
            oContext.setSiteName('cDownload')
            oContext.setFunction('AddtoDownloadList')
            oContext.setTitle(cConfig().getlanguage(30202))
            oContext.setOutputParameterHandler(oOutputParameterHandler)
            oGuiElement.addContextItem(oContext)
            
        if (oHoster.isDownloadable() == True):
            #Beta context download and view menu
            oContext = cContextElement()
            oContext.setFile('cDownload')
            oContext.setSiteName('cDownload')
            oContext.setFunction('AddtoDownloadListandview')
            oContext.setTitle('DL et Visualiser')
            oContext.setOutputParameterHandler(oOutputParameterHandler)
            oGuiElement.addContextItem(oContext)           
        
        #context FAV menu
        oGui.createContexMenuFav(oGuiElement, oOutputParameterHandler)
        
        #context Library menu
        oGui.CreateSimpleMenu(oGuiElement,oOutputParameterHandler,'cLibrary','cLibrary','setLibrary','[COLOR teal]Add to library[/COLOR]')
      
        #bug
        oGui.addFolder(oGuiElement, oOutputParameterHandler, False)
         
        #oGui.addFolder(oGuiElement, oOutputParameterHandler)

    def plusHoster(self, oGui):               

        oInputParameterHandler = cInputParameterHandler()
        #aParams = oInputParameterHandler.getAllParameter()
        
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        
        #formatage pour recheche serie
        sMovieTitle = cUtil().FormatSerie(sMovieTitle)
        #nettoyage pour la recherhce
        sMovieTitle = cUtil().CleanName(sMovieTitle)
        
        sUrl = "http://www.alluc.ee/stream/lang%3Afr+"+sMovieTitle
        oOutputParameterHandler = cOutputParameterHandler()

        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir('alluc_ee', 'showMovies', 'Plus', 'search.png', oOutputParameterHandler)
        
        
    def checkHoster(self, sHosterUrl):
    
        #securitee
        
        
        #L'user a active l'url resolver ?
        if ('vkontaktecdn.com' in sHosterUrl):
           return cHosterHandler().getHoster('lien_direct')
        if ('novamov' in sHosterUrl):
            return cHosterHandler().getHoster('novamov')
        if ('divxstage' in sHosterUrl):
            return cHosterHandler().getHoster('divxstage')
        if ('vidxden' in sHosterUrl):
            return cHosterHandler().getHoster('vidxden')
        if ('vidbux' in sHosterUrl):
            return cHosterHandler().getHoster('vidbux')
        if ('megavideo' in sHosterUrl):
            return cHosterHandler().getHoster('megavideo')
        if ('videoweed' in sHosterUrl):
            return cHosterHandler().getHoster('videoweed')
        if ('youwatch' in sHosterUrl):
            return cHosterHandler().getHoster('youwatch')
        if ('turbovid' in sHosterUrl):
            return cHosterHandler().getHoster('turbovid')
        if ('youtube' in sHosterUrl):
            url = sHosterUrl 
            youtube(url)
        if ('youtu.be' in sHosterUrl):
            url = sHosterUrl 
            youtube(url)
        if ('rutube' in sHosterUrl):
            return cHosterHandler().getHoster('rutube')
        if ('exashare' in sHosterUrl):
            return cHosterHandler().getHoster('exashare')
        if ('nowvideo' in sHosterUrl):
            return cHosterHandler().getHoster('nowvideo')
        if ('vk.com' in sHosterUrl):
            return cHosterHandler().getHoster('vk')
        if ('vkontakte' in sHosterUrl):
            return cHosterHandler().getHoster('vk')
        if ('vkcom' in sHosterUrl):
            return cHosterHandler().getHoster('vk')   
        if ('videomega' in sHosterUrl):
            return cHosterHandler().getHoster('videomega')
        if ('vidto' in sHosterUrl):
            return cHosterHandler().getHoster('vidto')
        if ('vidzi' in sHosterUrl):
            url = sHosterUrl 
            
            vidzitv(url) 
        if ('cloudy' in sHosterUrl):
            return cHosterHandler().getHoster('cloudy')
        if ('http://filetrip' in sHosterUrl):
            return cHosterHandler().getHoster('filetrip')
        if ('closeload' in sHosterUrl):
             url = sHosterUrl 
            
             closeload(url)  
        if ('uptostream' in sHosterUrl):
             url = sHosterUrl 
            
             uptostream(url)   
        if ('dailymotion' in sHosterUrl):
            return cHosterHandler().getHoster('dailymotion')
        if ('dai.ly' in sHosterUrl):
            return cHosterHandler().getHoster('dailymotion')           
        if ('azerfile' in sHosterUrl):
            return cHosterHandler().getHoster('azerfile')
        if ('vodlocker' in sHosterUrl):
            return cHosterHandler().getHoster('vodlocker')
        if ('mystream' in sHosterUrl):
            return cHosterHandler().getHoster('mystream')
        if ('streamingentiercom/videophp?type=speed' in sHosterUrl):
            return cHosterHandler().getHoster('speedvideo')
        if ('speedvideo' in sHosterUrl):
            return cHosterHandler().getHoster('speedvideo')
        if ('speedvid' in sHosterUrl):
            return cHosterHandler().getHoster('speedvid')
        if ('axavid' in sHosterUrl):
            return cHosterHandler().getHoster('axavid') 
        if ('streamcloud' in sHosterUrl):
            url = sHosterUrl 
            
            streamcloud(url)  
        if ('goo.gl' in sHosterUrl):
           
            url = sHosterUrl 
            
            hqqtv(url)      
        if ('hqq.tv' in sHosterUrl):
            return cHosterHandler().getHoster('netu')
        if ('waaw' in sHosterUrl):
            return cHosterHandler().getHoster('netu')
        if ('mail.ru' in sHosterUrl):
            url=sHosterUrl
            MailRu(url)
        if ('videoraj.to' in sHosterUrl):
            url=sHosterUrl
            videoraj(url)
        if ('videohut' in sHosterUrl):
            return cHosterHandler().getHoster('videohut')
        if ('onevideo' in sHosterUrl):
            return cHosterHandler().getHoster('onevideo')
        if ('googlevideo' in sHosterUrl):
            return cHosterHandler().getHoster('googlevideo')
        if ('picasaweb' in sHosterUrl):
            return cHosterHandler().getHoster('googlevideo')
        if ('googleusercontent' in sHosterUrl):
            return cHosterHandler().getHoster('googlevideo')
        if ('video.tt' in sHosterUrl):
            return cHosterHandler().getHoster('videott')
        if ('playreplay' in sHosterUrl):
            return cHosterHandler().getHoster('playreplay')
        if ('streamin.to' in sHosterUrl):
            return cHosterHandler().getHoster('streaminto')
        if ('vodlocker' in sHosterUrl):
            return cHosterHandler().getHoster('vodlocker')
        if ('raptu.com' in sHosterUrl):
            url=sHosterUrl
            raptu(url)
        if ('flashx' in sHosterUrl):
             return cHosterHandler().getHoster('flashx')
        if ('easywatch' in sHosterUrl):
            return cHosterHandler().getHoster('easywatch')
        if ('ok.ru' in sHosterUrl):
            url=sHosterUrl                                        
            ok_ru(url)   
        if ('odnoklassniki' in sHosterUrl):
            return cHosterHandler().getHoster('ok_ru')
        if ('vimeo.com' in sHosterUrl):
            return cHosterHandler().getHoster('vimeo')
        if ('openload' in sHosterUrl):                                      
            return cHosterHandler().getHoster('openload')
        if ('oload' in sHosterUrl):
            return cHosterHandler().getHoster('openload')
        if ('streamango' in sHosterUrl):
            url=sHosterUrl                                        
            streamango(url)     
        if ('thevideo.me' in sHosterUrl):
            url=sHosterUrl                                        
            thevideome(url)    
        if ('vid.me' in sHosterUrl):
            return cHosterHandler().getHoster('vidme')
        if ('zstream' in sHosterUrl):
            return cHosterHandler().getHoster('zstream')
        if ('watching' in sHosterUrl):
            return cHosterHandler().getHoster('watching')
        if ('letwatch' in sHosterUrl):
            return cHosterHandler().getHoster('letwatch')
        if ('easyvid' in sHosterUrl):
            return cHosterHandler().getHoster('easyvid')
        if ('allvid' in sHosterUrl):
            return cHosterHandler().getHoster('allvid')
        if ('www.amazon' in sHosterUrl):
            return cHosterHandler().getHoster('amazon')
        if ('filepup' in sHosterUrl):
            return cHosterHandler().getHoster('filepup')
        if ('v-vids' in sHosterUrl):
            return cHosterHandler().getHoster('v_vids')
        if ('vid.ag' in sHosterUrl):
            return cHosterHandler().getHoster('vid_ag')
        if ('wat.tv' in sHosterUrl):
            return cHosterHandler().getHoster('wat_tv')
        
        if ('nosvideo' in sHosterUrl):
            return cHosterHandler().getHoster('nosvideo')
        if ('vimple.ru' in sHosterUrl):
            return cHosterHandler().getHoster('vimple')
        if ('allmyvideos.net' in sHosterUrl):
            return cHosterHandler().getHoster('allmyvideos')
        if ('idowatch' in sHosterUrl):
            return cHosterHandler().getHoster('idowatch')
        if ('wstream.' in sHosterUrl):
            return cHosterHandler().getHoster('wstream')
        if ('veevr.' in sHosterUrl):
            return cHosterHandler().getHoster('veevr')
        if ('watchvideo.' in sHosterUrl):
             return cHosterHandler().getHoster('watchvideo')
        if ('drive.google.com' in sHosterUrl):
            return cHosterHandler().getHoster('googledrive')
        if ('docs.google.com' in sHosterUrl):
            return cHosterHandler().getHoster('googledrive')          
        if ('estream' in sHosterUrl):
             url=sHosterUrl
             estreamto(url)
        if ('1fichier' in sHosterUrl):
            return cHosterHandler().getHoster('onefichier')
        if ('uptobox' in sHosterUrl):
            return cHosterHandler().getHoster('uptobox')
        if ('uplea.com' in sHosterUrl):
            return cHosterHandler().getHoster('uplea')            
        if ('vidmoly.me' in sHosterUrl):
            url=sHosterUrl
            vidmoly(url)
        if ('uploaded' in sHosterUrl or 'ul.to' in sHosterUrl):
            return cHosterHandler().getHoster('uploaded')
        if ('vivo.sx' in sHosterUrl ):
            url=sHosterUrl
            vivosx(url)
        if ('filez.tv' in sHosterUrl ):
            url=sHosterUrl
            fileztv(url)
        if ('wholecloud' in sHosterUrl ):
            url=sHosterUrl
            wholecloud(url)
        if ('movshare' in sHosterUrl ):
            url=sHosterUrl
            wholecloud(url)
        if ('thevid' in sHosterUrl):
            return cHosterHandler().getHoster('thevid') 
        if (sHosterUrl[-4:] in '.mp4.avi.flv.m3u8'):
            return self.getHoster('lien_direct')
        if (not sHosterUrl):
            return False
            
        #Petit nettoyage
        sHosterUrl = sHosterUrl.split('|')[0]
            
       
        try:
            import urlresolver
            host = urlresolver.HostedMediaFile(url=sHosterUrl)
            if host:
                host = cHosterHandler().getHoster('resolver')
                RH = sHosterUrl.split('/')[2]
                RH = RH.replace('www.','')
                host.setRealHost( RH[:3].upper() )
                return host
        except:
            pass

        return False
        
        # step 2
        
        
    # def showHosterMenu(self):
        # oGui = cGui()
        # oInputParameterHandler = cInputParameterHandler()

        # sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        # sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        # bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        # sFileName = oInputParameterHandler.getValue('sFileName')

        # oHoster = cHosterHandler().getHoster(sHosterIdentifier)
        # oHoster.setFileName(sFileName)

        # # play
        # self.__showPlayMenu(oGui, sMediaUrl, oHoster, bGetRedirectUrl)

        # # playlist
        # self.__showPlaylistMenu(oGui, sMediaUrl, oHoster, bGetRedirectUrl)

        # # download
        # if (oHoster.isDownloadable() == True):
            # self.__showDownloadMenu(oGui, sMediaUrl, oHoster, bGetRedirectUrl)        

        # # JD
        # if (oHoster.isJDownloaderable() == True):
            # self.__showJDMenu(oGui, sMediaUrl, oHoster, bGetRedirectUrl)    

        # oGui.setEndOfDirectory()

    # def __showPlayMenu(self, oGui, sMediaUrl, oHoster, bGetRedirectUrl):
        # oGuiElement = cGuiElement()
        # oGuiElement.setSiteName(self.SITE_NAME)
        # oGuiElement.setFunction('play')
        # oGuiElement.setTitle('play')
        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('sMediaUrl', sMediaUrl)
        # oOutputParameterHandler.addParameter('sHosterIdentifier', oHoster.getPluginIdentifier())
        # oOutputParameterHandler.addParameter('bGetRedirectUrl', bGetRedirectUrl)
        # oOutputParameterHandler.addParameter('sFileName', oHoster.getFileName())
        # oGui.addFolder(oGuiElement, oOutputParameterHandler)

    # def __showDownloadMenu(self, oGui, sMediaUrl, oHoster, bGetRedirectUrl):
        # oGuiElement = cGuiElement()
        # oGuiElement.setSiteName(self.SITE_NAME)
        # oGuiElement.setFunction('download')
        # oGuiElement.setTitle('download ueber XBMC')
        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('sMediaUrl', sMediaUrl)
        # oOutputParameterHandler.addParameter('sHosterIdentifier', oHoster.getPluginIdentifier())
        # oOutputParameterHandler.addParameter('bGetRedirectUrl', bGetRedirectUrl)
        # oOutputParameterHandler.addParameter('sFileName', oHoster.getFileName())
        # oGui.addFolder(oGuiElement, oOutputParameterHandler)

    # def __showJDMenu(self, oGui, sMediaUrl, oHoster, bGetRedirectUrl):
        # oGuiElement = cGuiElement()
        # oGuiElement.setSiteName(self.SITE_NAME)        
        # oGuiElement.setTitle('an JDownloader senden')
        # oGuiElement.setFunction('sendToJDownbloader')
        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('sMediaUrl', sMediaUrl)
        # oOutputParameterHandler.addParameter('sHosterIdentifier', oHoster.getPluginIdentifier())
        # oOutputParameterHandler.addParameter('bGetRedirectUrl', bGetRedirectUrl)
        # oOutputParameterHandler.addParameter('sFileName', oHoster.getFileName())
        # oGui.addFolder(oGuiElement, oOutputParameterHandler)

    # def __showPlaylistMenu(self, oGui, sMediaUrl, oHoster, bGetRedirectUrl):
        # oGuiElement = cGuiElement()
        # oGuiElement.setSiteName(self.SITE_NAME)
        # oGuiElement.setFunction('addToPlaylist')
        # oGuiElement.setTitle('add to playlist')
        # oOutputParameterHandler = cOutputParameterHandler()
        # oOutputParameterHandler.addParameter('sMediaUrl', sMediaUrl)
        # oOutputParameterHandler.addParameter('sHosterIdentifier', oHoster.getPluginIdentifier())
        # oOutputParameterHandler.addParameter('bGetRedirectUrl', bGetRedirectUrl)
        # oOutputParameterHandler.addParameter('sFileName', oHoster.getFileName())
        # oGui.addFolder(oGuiElement, oOutputParameterHandler)
    def getHoster(self, sHosterFileName):
        exec "from resources.hosters." + sHosterFileName + " import cHoster"

        return cHoster()
    def play(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()

        sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        sFileName = oInputParameterHandler.getValue('sFileName')
        #sThumbnail = oInputParameterHandler.getValue('sThumbnail')

        if (bGetRedirectUrl == 'True'):            
            sMediaUrl = self.__getRedirectUrl(sMediaUrl)

        cConfig().log("Hoster - play " + sMediaUrl)

        oHoster = cHosterHandler().getHoster(sHosterIdentifier)
        oHoster.setFileName(sFileName)

        sHosterName = oHoster.getDisplayName()
        cConfig().showInfo(sHosterName, 'Resolve')
        
        #oHoster.setUrl(sMediaUrl)
        #aLink = oHoster.getMediaLink()
        
        try:
        
            oHoster.setUrl(sMediaUrl)
            aLink = oHoster.getMediaLink()

            if (aLink[0] == True):
                oGuiElement = cGuiElement()
                oGuiElement.setSiteName(self.SITE_NAME)
                oGuiElement.setMediaUrl(aLink[1])
                oGuiElement.setTitle(oHoster.getFileName())
                oGuiElement.getInfoLabel()
                
                oPlayer = cPlayer()
                oPlayer.run(oGuiElement, oHoster.getFileName(), aLink[1])
                
                # oGuiElement = cGuiElement()
                # oGuiElement.setSiteName(self.SITE_NAME)
                # oGuiElement.setMediaUrl(aLink[1])
                # oGuiElement.setTitle(oHoster.getFileName())
                # oGuiElement.getInfoLabel()
                
                # oPlayer = cPlayer()
                # oPlayer.clearPlayList()
                # oPlayer.addItemToPlaylist(oGuiElement)
                # oPlayer.startPlayer()
                return
            else:
                #cConfig().showInfo(sHosterName, 'Fichier introuvable')
                cConfig().error("File not Found ")
                return

        except:
            #cConfig().showInfo(sHosterName, 'Fichier introuvable')
            cConfig().error("File not Found ")
            return

        oGui.setEndOfDirectory()

    def addToPlaylist(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()

        sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        sFileName = oInputParameterHandler.getValue('sFileName')
        

        if (bGetRedirectUrl == 'True'):
            sMediaUrl = self.__getRedirectUrl(sMediaUrl)

        cConfig().log("Hoster - play " + sMediaUrl)
        oHoster = cHosterHandler().getHoster(sHosterIdentifier)
        oHoster.setFileName(sFileName)

        #try:

        oHoster.setUrl(sMediaUrl)
        aLink = oHoster.getMediaLink()

        if (aLink[0] == True):
            oGuiElement = cGuiElement()
            oGuiElement.setSiteName(self.SITE_NAME)
            oGuiElement.setMediaUrl(aLink[1])
            oGuiElement.setTitle(oHoster.getFileName())

            oPlayer = cPlayer()
            oPlayer.addItemToPlaylist(oGuiElement)
            oGui.showInfo('Playlist', str(oHoster.getFileName()), 5);
            return

        #except:
        # cConfig().log("could not load plugin " + sHosterFileName)

        oGui.setEndOfDirectory()
        

    # def download(self):
        # oGui = cGui()
        # oInputParameterHandler = cInputParameterHandler()

        # sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        # sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        # bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        # sFileName = oInputParameterHandler.getValue('sFileName')

        # if (bGetRedirectUrl == 'True'):
            # sMediaUrl = self.__getRedirectUrl(sMediaUrl)

        # cConfig().log("Telechargement " + sMediaUrl)

        # oHoster = cHosterHandler().getHoster(sHosterIdentifier)
        # oHoster.setFileName(sFileName)

        # #try:
        # oHoster.setUrl(sMediaUrl)
        # aLink = oHoster.getMediaLink()
        # if (aLink[0] == True):
            # oDownload = cDownload()
            # oDownload.download(aLink[1], oHoster.getFileName())
            # return

        # #except:
        # # cConfig().log("Telechargement " + sHosterFileName)

        # oGui.setEndOfDirectory()

    def sendToJDownbloader(self):
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()

        sHosterIdentifier = oInputParameterHandler.getValue('sHosterIdentifier')
        sMediaUrl = oInputParameterHandler.getValue('sMediaUrl')
        bGetRedirectUrl = oInputParameterHandler.getValue('bGetRedirectUrl')
        sFileName = oInputParameterHandler.getValue('sFileName')

        if (bGetRedirectUrl == 'True'):
            sMediaUrl = self.__getRedirectUrl(sMediaUrl)

        oHoster = cHosterHandler().getHoster(sHosterIdentifier)
        oHoster.setFileName(sFileName)
        oHoster.setUrl(sMediaUrl)
        sMediaUrl = oHoster.getUrl()

        cConfig().log("Telechargement jdownloader " + sMediaUrl)

        cJDownloaderHandler().sendToJDownloader(sMediaUrl)

        

    def __getRedirectUrl(self, sUrl):
        oRequest = cRequestHandler(sUrl)
        oRequest.request()
        return oRequest.getRealUrl()

        


             

def otvkodla(data):
        data = data.replace('\\x','%')
        data = data.replace('\u00','%')
        data = data.replace('%3c','<')
        data = data.replace('%3e','>')
        data = data.replace('%5d','-')
        data = data.replace('%22','"')
        data = data.replace('%2f','/')
        data = data.replace('%2F','/')
        data = data.replace('%3A',':')
        data = data.replace('%3a',':')
        data = data.replace('%3f','?')
        data = data.replace('%3d','=')
        data = data.replace('%30','0')
        data = data.replace('%31','1')
        data = data.replace('%32','2')
        data = data.replace('%33','3')
        data = data.replace('%34','4')
        data = data.replace('%35','5')
        data = data.replace('%36','6')
        data = data.replace('%37','7')
        data = data.replace('%38','8')
        data = data.replace('%39','9')
        data = data.replace('%61','a')
        data = data.replace('%62','b')
        data = data.replace('%63',"c")
        data = data.replace('%64',"d")
        data = data.replace('%65',"e")
        data = data.replace('%66',"f")
        data = data.replace('%67',"g")
        data = data.replace('%68','h')
        data = data.replace('%69','i')
        data = data.replace('%6a','j')
        data = data.replace('%6b','k')
        data = data.replace('%6c','l')
        data = data.replace('%6d','m')
        data = data.replace('%6e','n')
        data = data.replace('%6f','o')
        data = data.replace('%70','p')
        data = data.replace('%71','q')
        data = data.replace('%2E','.')
        data = data.replace('%72','r')
        data = data.replace('%73','s')
        data = data.replace('%74','t')
        data = data.replace('%75','u')
        data = data.replace('%76','v')
        data = data.replace('%77','w')
        data = data.replace('%78','x')
        data = data.replace('%79','y')
        data = data.replace('%7a','z')
        data = data.replace('%26','&')
        data = data.replace("%25","%")
        data = data.replace("%3D","=")          
        data = data.replace("%3F","?")   
        data = data.replace("%09",".")
        data = data.replace("%09",".")
        data = data.replace("%7b","[")
        data = data.replace("%2d","-")
        data = data.replace("%2c",",")
        data = data.replace("%2b",",")
        data = data.replace("%27", "'")
        data = data.replace("%29", ")")
        data = data.replace("%28", "(")
        data = data.replace("%5f","_")
        data = data.replace("%0a",".")
        data = data.replace("%20"," ")
        data = data.replace("%2e",".")
        data = data.replace('\\x','%')
        data = data.replace('\u00','%')
        data = data.replace('%3C','<')
        data = data.replace('%3E','>')
        data = data.replace('%5D','-')
        data = data.replace('%22','"')
        data = data.replace('%2f','/')
        data = data.replace('%2F','/')
        data = data.replace('%3A',':')
        data = data.replace('%3a',':')
        data = data.replace('%3f','?')
        data = data.replace('%3d','=')
        data = data.replace('%30','0')
        data = data.replace('%31','1')
        data = data.replace('%32','2')
        data = data.replace('%33','3')
        data = data.replace('%34','4')
        data = data.replace('%35','5')
        data = data.replace('%36','6')
        data = data.replace('%37','7')
        data = data.replace('%38','8')
        data = data.replace('%39','9')
        data = data.replace('%61','a')
        data = data.replace('%62','b')
        data = data.replace('%63',"c")
        data = data.replace('%64',"d")
        data = data.replace('%65',"e")
        data = data.replace('%66',"f")
        data = data.replace('%67',"g")
        data = data.replace('%68','h')
        data = data.replace('%69','i')
        data = data.replace('%6A','j')
        data = data.replace('%6B','k')
        data = data.replace('%6C','l')
        data = data.replace('%6D','m')
        data = data.replace('%6E','n')
        data = data.replace('%6F','o')
        data = data.replace('%70','p')
        data = data.replace('%71','q')
        data = data.replace('%2E','.')
        data = data.replace('%72','r')
        data = data.replace('%73','s')
        data = data.replace('%74','t')
        data = data.replace('%75','u')
        data = data.replace('%76','v')
        data = data.replace('%77','w')
        data = data.replace('%78','x')
        data = data.replace('%79','y')
        data = data.replace('%7A','z')
        data = data.replace('%26','&')
        data = data.replace("%25","%")
        data = data.replace("%3D","=")          
        data = data.replace("%3F","?")   
        data = data.replace("%09",".")
        data = data.replace("%09",".")
        data = data.replace("%7B","[")
        data = data.replace("%2D","-")
        data = data.replace("%2C",",")
        data = data.replace("%2B",",")
        data = data.replace("%27", "'")
        data = data.replace("%29", ")")
        data = data.replace("%28", "(")
        data = data.replace("%5F","_")
        data = data.replace("%0A",".")
        data = data.replace("%20"," ")
        data = data.replace("%2e",".")
        data=data.replace('\&',"&")
        return data
def PlayUrl(name, url, iconimage=None):
    
	url=url.replace("\n","").replace("\r","")
	if not url.endswith(".ts") and not url.endswith(".f4m") and url.find(".f4m?") < 0 and not url.endswith("Player=HLS"):
            if url.endswith("?time="):
                url = url + str(time.time())
            print '--- Playing "{0}". {1}'.format(name, url)
            listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
            listitem.setInfo(type="Video", infoLabels={ "Title": name })
            
            xbmc.Player().play( url, listitem)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
            xbmc.sleep(1000)
            xbmc.executebuiltin('Dialog.Close(all, true)')
                
        else :
            if xbmc.Player().isPlaying():
                xbmc.executebuiltin( "XBMC.Action(Stop)" )
                xbmc.sleep(4000)
                xbmc.executebuiltin('Dialog.Close(all, true)')
            #xbmc.executebuiltin("XBMC.Container.Refresh()")
            if Addon.getSetting('use_shani') == "true":
                MyF4m = False
            else:
                MyF4m = True
            
            if url.endswith(".ts"):        
                StreamType = 'TSDOWNLOADER'
            elif url.find("Player=HLS") > 0:
                StreamType = 'HLS'
            else:
                StreamType = 'HDS'
            
            if MyF4m :
                url = 'plugin://plugin.video.kodilivetv/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&mode=5&iconimage=' + iconimage
                xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
                xbmc.executebuiltin('Dialog.Close(all, true)')
            else:
                f4mDir = xbmcaddon.Addon('plugin.video.f4mTester').getAddonInfo('path').decode("utf-8")
                if not os.path.exists(f4mDir):
                    AddonID = 'plugin.video.kodilivetv'
                    addon = xbmcaddon.Addon(AddonID)
                    addonname = addon.getAddonInfo('name')
                    icon = xbmcaddon.Addon(AddonID).getAddonInfo('icon')
                    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonname,"Plugin f4mTester required!", 3200, icon))
                else:
                    url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&streamtype=' + StreamType + '&name='+urllib.quote(name)+'&iconImage=' + iconimage
                    xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
                    xbmc.executebuiltin('Dialog.Close(all, true)')
