# -*- coding: utf-8 -*-
import xbmc


class MyXBMCPlayer(xbmc.Player):
    xbmc.executebuiltin("Notification([COLOR=gold]Cerebro TV[/COLOR],This Channel May Take A Few Clicks Checking 5 Servers,7000)")
    def __init__( self, *args, **kwargs ):
        self.is_active = True
        self.urlplayed = False
        self.pdialogue=None
        print "#XBMCPlayer#"
    
    #def play(self, url, listitem):
    #   print 'Now im playing... %s' % url
    #    self.is_active = False
    #    self.urlplayed = False
    #    xbmc.Player().play(url, listitem)

	#def setdialogue( self, pdialogue ):
	#	self.pdialogue=pdialogue
		
    def onPlayBackStarted( self ):
        if (self.pdialogue):
            self.pdialogue.close()
        self.urlplayed = True
            
    def onPlayBackEnded( self ):
        self.is_active = False
        self.urlplayed = False
        
    def onPlayBackStopped( self ):
        self.is_active = False
        self.urlplayed = False

