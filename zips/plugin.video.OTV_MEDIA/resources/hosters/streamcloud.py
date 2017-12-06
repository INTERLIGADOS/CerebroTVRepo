#-*- coding: utf-8 -*-
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.config import cConfig
from resources.lib.gui.gui import cGui
from resources.hosters.hoster import iHoster
from t0mm0.common.net import Net
import base64
import xbmc


class cHoster(iHoster):

    def __init__(self):
        self.__sDisplayName = 'streamcloud.eu'
        self.__sFileName = self.__sDisplayName
        self.__sHD = ''
        self.net = Net()
    def getDisplayName(self):
        return  self.__sDisplayName

    def setDisplayName(self, sDisplayName):
        self.__sDisplayName = sDisplayName + ' [COLOR skyblue]'+self.__sDisplayName+'[/COLOR]'

    def setFileName(self, sFileName):
        self.__sFileName = sFileName

    def getFileName(self):
        return self.__sFileName

    def getPluginIdentifier(self):
        return 'streamcloud'
        
    def setHD(self, sHD):
        self.__sHD = ''

    def getHD(self):
        return self.__sHD

    def isDownloadable(self):
        return True

    def isJDownloaderable(self):
        return True

    def getPattern(self):
        return ''
    
    def __getIdFromUrl(self, sUrl):
        sPattern = "id=([^<]+)"
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if (aResult[0] == True):
            return aResult[1][0]

        return ''

    def setUrl(self, sUrl):
        self.__sUrl = str(sUrl)

    def checkUrl(self, sUrl):
        return True

    def __getUrl(self, media_id):
        return
    
    def getMediaLink(self):
        return self.__getMediaLinkForGuest()

    def __getMediaLinkForGuest(self):

        url = self.__sUrl
       
        resp = self.net.http_GET(url)
        r = resp.content 
        post_url = resp.get_url()
        r = r.replace('"referer" value=""', '"referer" value="http://queveohoy.net/ver-parkland-online"')
        form_values = {}
        for i in re.finditer('<input.*?name="(.*?)".*?value="(.*?)">', r):
            form_values[i.group(1)] = i.group(2)

        
        html = self.net.http_POST(post_url, form_data=form_values).content
        api_call = re.findall('file: "(.+?)",', html)[0]
        
        if (api_call):

            return True, api_call
        else:
            cGui().showInfo(self.__sDisplayName, 'Fichier introuvable' , 5)
        
        return False, False
