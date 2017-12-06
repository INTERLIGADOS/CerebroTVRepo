#	-*-	coding:	utf-8	-*-

from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.pluginHandler import cPluginHandler
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.lib.db import cDb


import xbmc, xbmcgui, xbmcplugin, sys
import xbmcaddon,xbmcvfs
import time

from resources.lib.otvhelper import * 
class OTVPlayer():
    
    
        	
	def __init__(self,  playList, playIdx=0, playAll=False, listTitle=None, plType='local', title_inr=0, cover=False, ltype='', autoScrSaver=False, showPlaylist=True, listEntryPar=None, playList2=[], playerMode='VIDEO', useResume=True, bufferingOpt='None',  embeddedCoverArt=False):
                              
	
               
                	
	       
                
		self.playerMode = playerMode
		self.keyPlayNextLocked = False
		self.isTSVideo = False
		self.showGlobalPlaylist = True
		self.showPlaylist = showPlaylist
		self.scrSaver = ''
		self.saverActive = False
		self.autoScrSaver = autoScrSaver
		self.pl_open = False
		self.seekBarLocked = False
		self.listTitle = listTitle
		self.playAll = playAll
		self.playList = playList
		self.playIdx = playIdx
		self.plType = plType
	
	
                
		self.ltype = ltype
	        self.playVideo()

                
	


	def playVideo(self):
		print "playVideo:"
		self.isTSVideo = False

		self.resetMySpass()
		if self.plType == 'global':
			self.getVideo2()
		else:
			self.cover2 = False
			self.getVideo()

	def playSelectedVideo(self, idx):
		self.playIdx = idx
		self.playVideo()

	def dataError(self, error):
		print "dataError:"
		printl(error,self,"E")
		if config.orhantv1.sp_show_errors.value:
			self.session.openWithCallback(self.dataError2, MessageBox, str(error), MessageBox.TYPE_INFO, timeout=10)
		else:
			reactor.callLater(2, self.dataError2, None)
        def resetMySpass(self):
		self.myspass_ofs = 0L
		self.myspass_len = 0L
		self.mySpassPath = None
		self.isMySpass = False
		self.isRetroTv = False
		self.isNumberSeek = False
	def dataError2(self, res):
		self.playNextStream(config.orhantv1.sp_on_movie_eof.value)
        def checkSkipShowHideLock(self):
		pass
	def playStream(self, title, url, **kwargs):
		if not url:
	
			self._initStream(title, url, **kwargs)

	def _initStream(self, title, url, album='', artist='', imgurl=''):
		

		print "playStream: ",title,url
		
                self.url = url 
                self.title = title 
                playlist=xbmc.PlayList(xbmc.PLAYER_CORE_DVDPLAYER); 
		playlist.clear();
		listitem1 = xbmcgui.ListItem(title)
		playlist.add(url,listitem1);
		
		sPlayerType = PlayerType()
		xbmcPlayer = xbmc.Player(sPlayerType)
		xbmcPlayer.playprevious(playlist)
		xbmcPlayer.play(playlist) 
	def playNextStream(self, value):
		print "playNextStream:"
		if not self.playAll or self.playLen <= 1:
			self.handleLeave(value)
		else:
			if self.playIdx in range(0, self.playLen-1):
				self.playIdx += 1
			else:
				self.playIdx = 0
			self.playVideo()

	
	
	
	
	def getVideo(self):
		print "getVideo:"
	        
                title = str(self.playList[self.playIdx][0])
		url =str(self.playList[self.playIdx][1])
		if len(self.playList[0]) == 3:
			iurl = self.playList[self.playIdx][2]
		else:
			iurl = ''
		self.playStream(title, url, imgurl=iurl)

	def getVideo2(self):
		print "getVideo2:"
		if self.playLen > 0:
			titel = self.playList2[self.playIdx][1]
			url = self.playList2[self.playIdx][2]
			album = self.playList2[self.playIdx][3]
			artist = self.playList2[self.playIdx][4]
			imgurl = self.playList2[self.playIdx][7]
			self.cover2 = self.playList2[self.playIdx][8] == '1' and self.plType == 'global'

			if len(self.playList2[self.playIdx]) < 6:
				ltype = ''
			else:
				ltype = self.playList2[self.playIdx][5]

			if ltype == 'youtube':
				YoutubeLink(self.session).getLink(self.playStream, self.dataError, titel, url, imgurl)
			elif ltype == 'putpattv':
				token = self.playList2[self.playIdx][6]
				PutpattvLink(self.session).getLink(self.playStream, self.dataError, titel, url, token, imgurl)
			elif ltype == 'myvideoaz':
				token = self.playList2[self.playIdx][6]
				MyvideoLink(self.session).getLink(self.playStream, self.dataError, titel, url, token, imgurl)
			elif ltype == 'songsto' and not url:
				token = self.playList2[self.playIdx][6]
				SongstoLink(self.session).getLink(self.playStream, self.dataError, titel, artist, album, token, imgurl)
			elif mechanizeModule and ltype == 'canna':
				CannaLink(self.session).getLink(self.playStream, self.dataError, titel, artist, album, url, imgurl)
			elif ltype == 'eighties':
				token = self.playList2[self.playIdx][6]
				EightiesLink(self.session).getLink(self.playStream, self.dataError, titel, artist, album, url, token, imgurl)
			elif ltype == 'mtv':
				MTVdeLink(self.session).getLink(self.playStream, self.dataError, titel, artist, url, imgurl)
			elif url:
				self.playStream(titel, url, album, artist, imgurl=imgurl)
		else:
			self.close()

	
    
    
        
    
    
def GetRealUrl(url):
    oParser = cParser()
    sPattern = '\[REGEX\](.+?)\[URL\](.+$)'
    aResult = oParser.parse(url, sPattern)
    
    if (aResult):
        reg = aResult[1][0][0]
        url2 = aResult[1][0][1]
        oRequestHandler = cRequestHandler(url2)
        sHtmlContent = oRequestHandler.request()
        
        aResult = oParser.parse(sHtmlContent, reg)
        if (aResult):
            url = aResult[1][0]
            
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()
        
    return url
def sPlayerType():
        oConfig = cConfig()
        sPlayerType = oConfig.getSetting('playerType')
        
        try:
            if (sPlayerType == '0'):
                cConfig().log("playertype from config: auto")
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                cConfig().log("playertype from config: mplayer")
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                cConfig().log("playertype from config: dvdplayer")
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False

