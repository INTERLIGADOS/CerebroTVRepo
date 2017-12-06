# Kodi Live Downloader
import os, urllib2, ftplib, urlparse, urllib, sys, socket, xbmc, xbmcaddon, xbmcgui

class DownloadFile(object):
    """
    #####
    Basic usage:
         Use full path to download
             downloader = fileDownloader.DownloadFile('http://example.com/file.zip', "C:/Users/username/Downloads/newfilename.zip")
             downloader.download()
         Basic Authentication protected download
             downloader = fileDownloader.DownloadFile('http://example.com/file.zip', "C:/Users/username/Downloads/newfilename.zip", ('username','password'))
             downloader.download()
         Resume
             downloader = fileDownloader.DownloadFile('http://example.com/file.zip')
            downloader.resume()
    """        
    
    def __init__(self, url, localFileName=None, auth=None, timeout=120.0, autoretry=True, retries=500, origurl=None, res = None):
        """Note that auth argument expects a tuple, ('username','password')"""
        self.url = url
        self.urlFileName = None
        self.progress = 0
        self.fileSize = None
        self.localFileName = localFileName
        self.type = self.getType()
        self.auth = auth
        self.timeout = timeout
        self.retries = retries
        self.curretry = 0
        self.cur = 0
        self.origurl = origurl
        self.res = res
        self.urlFilesize = self.getUrlFileSize()
        item = [ ]
        if not self.localFileName: #if no filename given pulls filename from the url
            self.localFileName = self.getUrlFilename(self.url)

    
    def __downloadFile__(self, urlObj, fileObj, callBack=None, origurl = None, res = None):
        
        Addon = xbmcaddon.Addon('plugin.video.kodilivetv')
        icon = Addon.getAddonInfo('icon')
        localizedString = Addon.getLocalizedString
        
        self.fileSize = self.urlFilesize
        Namefile = self.localFileName.replace('\\','/')
        Namefile = Namefile.split('/')[-1]
        Namefile = Namefile.replace("_"," ")
        ext = Namefile.split(".")[-1]
        Namefile = Namefile.replace( "." + ext , "" ) 
        
        if self.cur < 1:

            xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('Download file: ', Namefile, 5100, icon))
            xbmc.log("####### Downloader Start Download ########")
            
            file_name = self.localFileName + ".resume"
            fh = open(file_name, "wb")
            if not self.fileSize:
                dim = 0
            else:
                dim = self.fileSize
            
            if not self.origurl == None:
                urlname = self.origurl
            else:
                urlname = self.url
            
            fh.write(str(dim) + "\r\n" + str(urlname))
            fh.close()
            if dim == 0:
                self.retries = self.retries - 10
            else:
                if not self.res == "yes":
                    xbmc.executebuiltin("XBMC.Container.Refresh()")
                
        while 1:
            data = ""
            try:
                data = urlObj.read(8192)
            except:
                pass
            
            if data == "":
                fileObj.close()
                if self.retries > self.curretry:
                    self.curretry += 1
                    self.resume()
                    #xbmc.log("Download auto resume : " + str(self.curretry))
                else:
                    break
            else:                    
                fileObj.write(data)
                self.cur += 8192
             
            if int(self.fileSize) <= int(self.cur):
                if os.path.isfile(self.localFileName + ".resume"):
                    os.remove(self.localFileName + ".resume")
                if os.path.isfile(self.localFileName + ".stopped"):
                    os.remove(self.localFileName + ".stopped")
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(Namefile, localizedString(10209).encode('utf-8'), 6000, icon))
                xbmc.log("####### Download finito ########")                   
                break
            
            if os.path.isfile(self.localFileName + ".stopped"):
                break
     
            if callBack:
                callBack(cursize=self.cur)

        fileObj.close() 
        urlObj.close()
        
    def __retry__(self):
        """auto-resumes up to self.retries"""
        if self.retries > self.curretry:
                self.curretry += 1
                xbmc.log("Download auto resume - retry : " + str(self.curretry))
                if self.getLocalFileSize() != self.urlFilesize:
                    self.resume()
        else:
            print 'retries all used up'
            return False, "Retries Exhausted"
                    
    def __authHttp__(self):
        """handles http basic authentication"""
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # this creates a password manager
        passman.add_password(None, self.url, self.auth[0], self.auth[1])
        # because we have put None at the start it will always
        # use this username/password combination for  urls
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        # create the AuthHandler
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        
    def __authFtp__(self):
        """handles ftp authentication"""
        ftped = urllib2.FTPHandler()
        ftpUrl = self.url.replace('ftp://', '')
        req = urllib2.Request("ftp://%s:%s@%s"%(self.auth[0], self.auth[1], ftpUrl))
        req.timeout = self.timeout
        ftpObj = ftped.ftp_open(req)
        return ftpObj
        
    def __startHttpResume__(self, restart=None, callBack=None):
        """starts to resume HTTP"""
        curSize = self.getLocalFileSize()
        self.cur = curSize
        if restart:
            f = open(self.localFileName , "wb")
        else:
            f = open(self.localFileName , "ab")
        if self.auth:
            self.__authHttp__()
        try:    
            req = urllib2.Request(self.url)
            req.headers['Range'] = 'bytes=%s-%s' % (curSize, self.getUrlFileSize())
            urllib2Obj = urllib2.urlopen(req, timeout=self.timeout)
            self.__downloadFile__(urllib2Obj, f, callBack=callBack)
        except:
            pass          

    def __startFtpResume__(self, restart=None):
        """starts to resume FTP"""
        if restart:
            f = open(self.localFileName , "wb")
        else:
            f = open(self.localFileName , "ab")
        ftper = ftplib.FTP(timeout=60)
        parseObj = urlparse.urlparse(self.url)
        baseUrl= parseObj.hostname
        urlPort = parseObj.port
        bPath = os.path.basename(parseObj.path)
        gPath = parseObj.path.replace(bPath, "")
        unEncgPath = urllib.unquote(gPath)
        fileName = urllib.unquote(os.path.basename(self.url))
        ftper.connect(baseUrl, urlPort)
        ftper.login(self.auth[0], self.auth[1])
        if len(gPath) > 1:
            ftper.cwd(unEncgPath)
        ftper.sendcmd("TYPE I")
        ftper.sendcmd("REST " + str(self.getLocalFileSize()))
        downCmd = "RETR "+ fileName
        ftper.retrbinary(downCmd, f.write)
        
    def getUrlFilename(self, url):
        """returns filename from url"""
        return urllib.unquote(os.path.basename(url))
        
    def getUrlFileSize(self):
        """gets filesize of remote file from ftp or http server"""
        if self.type == 'http' or self.type == 'https':
            if self.auth:
                authObj = self.__authHttp__()
            try:
                xbmc.sleep(100)
                socket.setdefaulttimeout(5)

                h=urllib2.HTTPHandler(debuglevel=0)
                request = urllib2.Request(self.url)

                opener = urllib2.build_opener(h)
                urllib2.install_opener(opener)
                try:
                    connexion = opener.open(request)
                    size = int(connexion.headers["Content-Length"])
                except:
                    size = 0                
                return size
            except:
                pass

    def getLocalFileSize(self):
        """gets filesize of local file"""
        size = os.stat(self.localFileName).st_size
        return size
        
    def getType(self):
        """returns protocol of url (ftp or http)"""
        type = urlparse.urlparse(self.url).scheme
        return type	
        
    def checkExists(self):
        """Checks to see if the file in the url in self.url exists"""
        if self.auth:
            if self.type == 'http' or type == 'https':
                authObj = self.__authHttp__()
                try:
                    urllib2.urlopen(self.url, timeout=self.timeout)
                except urllib2.HTTPError:
                    return False
                return True
            elif self.type == 'ftp':
                return "not yet supported"
        else:
            urllib2Obj = urllib2.urlopen(self.url, timeout=self.timeout)
            try:
                urllib2.urlopen(self.url, timeout=self.timeout)
            except urllib2.HTTPError:
                return False
            return True

    def download(self, callBack=None):
        """starts the file download"""
        self.curretry = 0
        self.cur = 0
        f = open(self.localFileName , "wb")
        if self.auth:
            if self.type == 'http' or type == 'https':
                self.__authHttp__()
                req = urllib2.Request(self.url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0' })
                urllib2Obj = urllib2.urlopen(req, timeout=self.timeout)
                self.__downloadFile__(urllib2Obj, f, callBack=callBack)
            elif self.type == 'ftp':
                self.url = self.url.replace('ftp://', '')
                authObj = self.__authFtp__()
                self.__downloadFile__(authObj, f, callBack=callBack)
        else:
            try:
                req = urllib2.Request(self.url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0' })
                urllib2Obj = urllib2.urlopen(req, timeout=self.timeout)
                self.__downloadFile__(urllib2Obj, f, callBack=callBack)
                
                #socket.setdefaulttimeout(60)

                #h=urllib2.HTTPHandler(debuglevel=0)
                #request = urllib2.Request(self.url, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0' })
                #opener = urllib2.build_opener(h)
                #urllib2.install_opener(opener)
                #connexion = opener.open(request)
                #self.__downloadFile__(connexion , f, callBack=callBack)    
                
            except:
                Addon = xbmcaddon.Addon('plugin.video.kodilivetv')
                icon = Addon.getAddonInfo('icon')
                Namefile = self.localFileName.replace('\\','/')
                Namefile = Namefile.split('/')[-1]
                Namefile = Namefile.replace("_"," ")
                ext = Namefile.split(".")[-1]
                Namefile = Namefile.replace( "." + ext , "" )
                
                xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(Namefile, "DOWNLOAD ERROR: failed connection to the server!", 5800, icon))
                if os.path.isfile(self.localFileName):
                    os.remove(self.localFileName)
                return False
        return True

    def resume(self, callBack=None):
        """attempts to resume file download"""
        type = self.getType()
        if type == 'http' or type == 'https':
            self.__startHttpResume__(callBack=callBack)
        elif type == 'ftp':
            self.__startFtpResume__()
