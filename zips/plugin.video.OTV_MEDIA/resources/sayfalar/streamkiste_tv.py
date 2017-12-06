#-*- coding: utf-8 -*-
from resources.lib.otvhelper import *
SITE_IDENTIFIER = 'streamkiste_tv'
SITE_NAME = 'HDfilme'
SITE_DESC = 'Replay TV'
lsearch = 'http://streamkiste.tv/js/live-search0.js'
URL_MAIN = 'http://hdfilme.tv'
ALMAN_SINEMA = (True, 'showGenre')
baseurl = 'http://filmpalast.to'
streamurl = 'http://filmpalast.to/stream/{id}/1'
import xbmc
import xbmcgui,xbmcaddon,os
BG= '!CA6gDi9HlBonO2yzo1VBtIauyJ5hcZQHAAAAR1cAAABonAOZJplTzO_ktpQCr7T5JP274eYQj3K5YuvY5BeSLz8OlT7rlxQegm_8_NMLSoTu8Ht8eemZIsWORbgrTJewlEdywSZkkiaMb508AwIhlfs1LkcWXAq5WciajhwvKnRkAO7-2IWyEeykhUi_qvmCFO8wS-Of9EvVWnCZULK5acQoZnT0qGrAcvjntvfhFyvSf-yEpjpKac_5SCXPUOHVrmgggVzNEi7j4x9CBREGReCroayYFKdoW4o0gBeh3B8anqYieSLMJCmeYn6U4Ek8LoPgbmucqo7c0XNXAazXVNNL9hzZlripQgfdQ32eDCBfALpbs6vOy1nY_nJLretjSym7GgrEokWg5l_kkm6Qtd6vw2tdG28YIHZ4rtFr3m79BFf6vZp20AUfoX6UA4cy_FPDbCxT8oh-sXbol9x5If2PPzA97LmytjbYdxFG20e0fAGM6mT64NmfVSH9wyl8LmEtE5lg7xgNt0pqRknuLZtXh_yYwZ3b-tzQ8OOOpoRHB9kPEYsDU_DPdhnTr-BdmegxUiucI-vskHp9vGw_k14rUKCxLs7X__D2y0uRe1qB05sFn-k2Qd6CCwxZv-9Cy2z91QS2uXNmEw-lIqQNBMdSPFT9gIBO5tsCMENejDMYXMe1xxpa0azEHGXI4LzDE4Mvc2nvIbqY-yP4NnuT_yWBdAoKSWEJtPQLa-3nTg_9cTkBb9OUlpb31kSReJAPB02wOauoFX0hl4zvNs12xFksbUnT6dQ5OijTsNGp7m77a-RrHaBgghthkp1PMIdPhlKzCSkZhu5qJ3DYNwXCDqxetqQ7bDBCwqGQz_RoIwG5kN_JPNUwJuezAtZmCFNbz2BKokdkiKX1xkhmc3sd0D-O_yggDdjVHSUD0kSaQAaGGdg9u1m_ImM-_oscsu1WORcLiSvc0gpr91gI5EPsbXxVIOkrt9LkOKafyajPb-2U07NSspJsqf7jMXV74pOdtQicyHkLTlrhwikGtA7bUW47C6jM7wZebKgbjQIxdnaZXOGSwXgMhVZSqi8Y8TlDpOD7hmT1gANMUBadLAVdPOBEqiVVHfHxR0hzTdDi1ae7zeV9oKEgZgFHt_HMablsY9Fv4rI8OfeMOnOntEMQYSNN-nIjMPrd0saYGRW_VHiLVXrRp-D90DwSYlyym9TckNeSR22qybVyFrkAAXaCrZdZ7c1haYA7A5HACJ08JaAwOnDqR8kOWktG_HE8'
__addon__ = xbmcaddon.Addon('plugin.video.OTV_MEDIA')
__sLang__ = 'de'

def getg():
    return None
    cookieJar = cookielib.LWPCookieJar()
    try:
        cookieJar.load("./gsite.jwl")
    except:
        pass
 
import urlparse, urllib,urllib2,cookielib
def LgetUrl(url, cookieJar=None,post=None, timeout=20, headers=None, noredir=False):

    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)

    if noredir:
        opener = urllib2.build_opener(NoRedirection,cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    else:
        opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    #opener = urllib2.install_opener(opener)
    req = urllib2.Request(url)

    if headers:
        for h,hv in headers:
            req.add_header(h,hv)
    else:
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
        req.add_header('Accept-Language', __sLang__)        

    xbmc.log('post : ' + str(post))
    response = opener.open(req,post,timeout=timeout)
    link=response.read()
    response.close()
    return link;
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
cookieJar=cj
class cInputWindow(xbmcgui.WindowDialog):
    def __init__(self, *args, **kwargs):
        
        self.cptloc = kwargs.get('captcha')
        self.img = xbmcgui.ControlImage(335,200,624,400,"")
        xbmc.sleep(500)
        self.img = xbmcgui.ControlImage(335,200,624,400,self.cptloc)
        xbmc.sleep(500)
        
        bg_image =  os.path.join( __addon__.getAddonInfo('path'), 'resources/art/' ) + "background.png"
        check_image =  os.path.join( __addon__.getAddonInfo('path'), 'resources/art/' ) + "trans_checked.png"
        uncheck_image =  os.path.join( __addon__.getAddonInfo('path'), 'resources/art/' ) + "trans_unchecked1.png"
        
        self.ctrlBackgound = xbmcgui.ControlImage(
            0,0, 
            1280, 720, 
            bg_image
        )
        self.cancelled=False
        self.addControl (self.ctrlBackgound)
        self.msg = kwargs.get('msg')+'\nNormally there are 3-4 selections and 2 rounds of pictures'
        self.roundnum=kwargs.get('roundnum')
        self.strActionInfo = xbmcgui.ControlLabel(335, 120, 700, 300, self.msg, 'font13', '0xFFFF00FF')
        self.addControl(self.strActionInfo)
        
        self.strActionInfo = xbmcgui.ControlLabel(335, 20, 724, 400, 'Captcha round %s'%(str(self.roundnum)), 'font40', '0xFFFF00FF')
        self.addControl(self.strActionInfo)
        
        self.addControl(self.img)
        
        self.chk=[0]*9
        self.chkbutton=[0]*9
        self.chkstate=[False]*9
        
        #self.chk[0] = xbmcgui.ControlCheckMark(335,200,200,200,'select',checkWidth=30, checkHeight=30)
        if 1==2:
            self.chk[0]= xbmcgui.ControlCheckMark(335, 190, 220, 150, '1', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[1]= xbmcgui.ControlCheckMark(335+200, 190, 220, 150, '2', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[2]= xbmcgui.ControlCheckMark(335+400, 190, 220, 150, '3', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            
            self.chk[3]= xbmcgui.ControlCheckMark(335, 190+130, 220, 150, '4', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[4]= xbmcgui.ControlCheckMark(335+200, 190+130, 220, 150, '5', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[5]= xbmcgui.ControlCheckMark(335+400, 190+130, 220, 150, '6', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
          
            
            self.chk[6]= xbmcgui.ControlCheckMark(335, 190+260, 220, 150, '7', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[7]= xbmcgui.ControlCheckMark(335+200, 190+260, 220, 150, '8', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[8]= xbmcgui.ControlCheckMark(335+400, 190+260, 220, 150, '9', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
        else:
        
            self.chk[0]= xbmcgui.ControlImage(335, 190, 220, 150,check_image)# '', font='font1',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[1]= xbmcgui.ControlImage(335+200, 190, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[2]= xbmcgui.ControlImage(335+400, 190, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            
            self.chk[3]= xbmcgui.ControlImage(335, 190+130, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[4]= xbmcgui.ControlImage(335+200, 190+130, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[5]= xbmcgui.ControlImage(335+400, 190+130, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
          
            
            self.chk[6]= xbmcgui.ControlImage(335, 190+260, 220, 150,check_image)#, '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[7]= xbmcgui.ControlImage(335+200, 190+260, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
            self.chk[8]= xbmcgui.ControlImage(335+400, 190+260, 220, 150,check_image)# '', font='font14',focusTexture=check_image ,noFocusTexture=uncheck_image,checkWidth=220,checkHeight=150)
        
        
            self.chkbutton[0]= xbmcgui.ControlButton(335, 190, 210, 150, '1', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[1]= xbmcgui.ControlButton(335+200, 190, 220, 150, '2', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[2]= xbmcgui.ControlButton(335+400, 190, 220, 150, '3', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            
            self.chkbutton[3]= xbmcgui.ControlButton(335, 190+130, 210, 150, '4', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[4]= xbmcgui.ControlButton(335+200, 190+130, 220, 150, '5', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[5]= xbmcgui.ControlButton(335+400, 190+130, 220, 150, '6', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
          
            
            self.chkbutton[6]= xbmcgui.ControlButton(335, 190+260, 210, 150, '7', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[7]= xbmcgui.ControlButton(335+200, 190+260, 220, 150, '8', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            self.chkbutton[8]= xbmcgui.ControlButton(335+400, 190+260, 220, 150, '9', font='font1');#,focusTexture=check_image ,noFocusTexture=uncheck_image);#,checkWidth=220,checkHeight=150)
            
        

        
        for obj in self.chk:
            self.addControl(obj )
            obj.setVisible(False)
        for obj in self.chkbutton:
            self.addControl(obj )
        
        
        
        #self.chk[0].setSelected(False)
        
        self.cancelbutton = xbmcgui.ControlButton(335+312-100,610,100,40,'Cancel',alignment=2)
        self.okbutton = xbmcgui.ControlButton(335+312+50,610,100,40,'OK',alignment=2)
        self.addControl(self.okbutton)
        self.addControl(self.cancelbutton)

        self.chkbutton[6].controlDown(self.cancelbutton);  self.chkbutton[6].controlUp(self.chkbutton[3])
        self.chkbutton[7].controlDown(self.cancelbutton);  self.chkbutton[7].controlUp(self.chkbutton[4])
        self.chkbutton[8].controlDown(self.okbutton);      self.chkbutton[8].controlUp(self.chkbutton[5])
        
        
        self.chkbutton[6].controlLeft(self.chkbutton[8]);self.chkbutton[6].controlRight(self.chkbutton[7]);
        self.chkbutton[7].controlLeft(self.chkbutton[6]);self.chkbutton[7].controlRight(self.chkbutton[8]);
        self.chkbutton[8].controlLeft(self.chkbutton[7]);self.chkbutton[8].controlRight(self.chkbutton[6]);
        
        self.chkbutton[3].controlDown(self.chkbutton[6]);  self.chkbutton[3].controlUp(self.chkbutton[0])
        self.chkbutton[4].controlDown(self.chkbutton[7]);  self.chkbutton[4].controlUp(self.chkbutton[1])
        self.chkbutton[5].controlDown(self.chkbutton[8]);  self.chkbutton[5].controlUp(self.chkbutton[2])
        
        self.chkbutton[3].controlLeft(self.chkbutton[5]);self.chkbutton[3].controlRight(self.chkbutton[4]);
        self.chkbutton[4].controlLeft(self.chkbutton[3]);self.chkbutton[4].controlRight(self.chkbutton[5]);
        self.chkbutton[5].controlLeft(self.chkbutton[4]);self.chkbutton[5].controlRight(self.chkbutton[3]);

        self.chkbutton[0].controlDown(self.chkbutton[3]);  self.chkbutton[0].controlUp(self.cancelbutton)
        self.chkbutton[1].controlDown(self.chkbutton[4]);  self.chkbutton[1].controlUp(self.cancelbutton)
        self.chkbutton[2].controlDown(self.chkbutton[5]);  self.chkbutton[2].controlUp(self.okbutton)
        
        self.chkbutton[0].controlLeft(self.chkbutton[2]);self.chkbutton[0].controlRight(self.chkbutton[1]);
        self.chkbutton[1].controlLeft(self.chkbutton[0]);self.chkbutton[1].controlRight(self.chkbutton[2]);
        self.chkbutton[2].controlLeft(self.chkbutton[1]);self.chkbutton[2].controlRight(self.chkbutton[0]);
        
        self.cancelled=False
        self.setFocus(self.okbutton)
        self.okbutton.controlLeft(self.cancelbutton);self.okbutton.controlRight(self.cancelbutton); 
        self.cancelbutton.controlLeft(self.okbutton); self.cancelbutton.controlRight(self.okbutton);
        self.okbutton.controlDown(self.chkbutton[2]);self.okbutton.controlUp(self.chkbutton[8]); 
        self.cancelbutton.controlDown(self.chkbutton[0]); self.cancelbutton.controlUp(self.chkbutton[6]);         
        #self.kbd = xbmc.Keyboard()

    def get(self):
        self.doModal()
        #self.kbd.doModal()
        #if (self.kbd.isConfirmed()):
        #   text = self.kbd.getText()
        #   self.close()
        #   return text
        #xbmc.sleep(5000)
        self.close()
        if not self.cancelled:
            retval=""
            for objn in range(9):
                if self.chkstate[objn]:#self.chk[objn].getSelected() :
                    retval+=("" if retval=="" else ",")+str(objn)
            return  retval
            
        else:
            return ""
#    def onControl(self,control):
#        if control == self.okbutton:
#            self.close()
#        elif control == self.cancelbutton:
#            self.cancelled=True
#            self.close()
    def anythingChecked(self):
        for obj in self.chkstate:
            if obj:#obj.getSelected():
                return True
        return False
    
    
    def onControl(self,control):
        if   control==self.okbutton: 
            if self.anythingChecked():
                self.close()
        elif control== self.cancelbutton:
            self.cancelled=True
            self.close()
        try:
            #print control
            if 'xbmcgui.ControlButton' in repr(type(control)):
                index=control.getLabel()
                #print 'index',index
                if index.isnumeric():
                    #print 'index2',index
                    #self.chk[int(index)-1].setSelected(not self.chk[int(index)-1].getSelected())
                    self.chkstate[int(index)-1]= not self.chkstate[int(index)-1]
                    self.chk[int(index)-1].setVisible(self.chkstate[int(index)-1])
                    #print 'ddone'
                    
        except: pass
#    def onClick(self, controlId):
#        print 'CLICKED',controlId
    def onAction(self, action):
        if action == 10:#ACTION_PREVIOUS_MENU:
            self.cancelled=True
            self.close()


def _get(request,post=None):
    """Performs a GET request for the given url and returns the response"""
    return opener.open(request,post).read()
def sEcho(s):
    s = s
    if '=1' in s:
        s = s.replace('=1', '=2')
        return s
    if '=2' in s:
        s = s.replace('=2', '=3')
        return s
    if '=3' in s:
        s = s.replace('=3', '=4')
        return s
    if '=4' in s:
        s = s.replace('=4', '=5')
        return s
    if '=5' in s:
        s = s.replace('=5', '=6')
        return s
    if '=6' in s:
        s = s.replace('=6', '=7')
        return s
    if '=7' in s:
        s = s.replace('=7', '=8')
        return s
    if '=8' in s:
        s = s.replace('=8', '=9')
        return s
    if '=9' in s:
        s = s.replace('=9', '=10')
        return s
    if '=10' in s:
        s = s.replace('=10', '=11')
        return s
    if '=11' in s:
        s = s.replace('=11', '=12')
        return s
    if '=12' in s:
        s = s.replace('=12', '=13')
        return s
    if '=13' in s:
        s = s.replace('=13', '=14')
        return s
    if '=14' in s:
        s = s.replace('=14', '=15')
        return s
    if '=15' in s:
        s = s.replace('=15', '=16')
        return s
    if '=16' in s:
        s = s.replace('=16', '=17')
        return s
    if '=17' in s:
        s = s.replace('=17', '=18')
        return s
    if '=18' in s:
        s = s.replace('=18', '=19')
        return s
    if '=19' in s:
        s = s.replace('=19', '=20')
        return s
    if '=20' in s:
        s = s.replace('=20', '=21')
        return s
    if '=21' in s:
        s = s.replace('=21', '=22')
        return s
    if '=22' in s:
        s = s.replace('=22', '=23')
        return s
    if '=23' in s:
        s = s.replace('=23', '=24')
        return s
    if '=24' in s:
        s = s.replace('=24', '=25')
        return s
    if '=25' in s:
        s = s.replace('=25', '=26')
        return s
    if '=26' in s:
        s = s.replace('=26', '=27')
        return s
    if '=27' in s:
        s = s.replace('=27', '=28')
        return s
    if '=28' in s:
        s = s.replace('=28', '=29')
        return s
    if '=29' in s:
        s = s.replace('=29', '=30')
        return s
    if '=30' in s:
        s = s.replace('=30', '=31')
        return s
    if '=31' in s:
        s = s.replace('=31', '=32')
        return s
    if '=32' in s:
        s = s.replace('=32', '=33')
        return s
    if '=33' in s:
        s = s.replace('=33', '=34')
        return s
    if '=34' in s:
        s = s.replace('=34', '=35')
        return s
    if '=35' in s:
        s = s.replace('=35', '=36')
        return s
    if '=36' in s:
        s = s.replace('=36', '=37')
        return s
    if '=37' in s:
        s = s.replace('=37', '=38')
        return s
    if '=38' in s:
        s = s.replace('=38', '=39')
        return s
    if '=39' in s:
        s = s.replace('=39', '=40')
        return s
    if '=40' in s:
        s = s.replace('=40', '=41')
        return s
    if '=41' in s:
        s = s.replace('=41', '=42')
        return s
    if '=42' in s:
        s = s.replace('=42', '=43')
        return s
    if '=43' in s:
        s = s.replace('=43', '=44')
        return s
    if '=44' in s:
        s = s.replace('=44', '=45')
        return s
    if '=45' in s:
        s = s.replace('=45', '=46')
        return s
    if '=46' in s:
        s = s.replace('=46', '=47')
        return s
    if '=47' in s:
        s = s.replace('=47', '=48')
        return s
    if '=48' in s:
        s = s.replace('=48', '=49')
        return s
    if '=49' in s:
        s = s.replace('=49', '=50')
        return s
    return False
            


def streamkiste():
    oGui = cGui()
    tarzlistesi = [('Suche', 'http://hdfilme.tv/movie-search?key=%s&page_film=', 'http://hdfilme.tv/movie-search?key=%s&page_film='),
     ('Letzte Updates', 'kinofilme', 'update'),
     ('Beliebte Filme', 'kinofilme', 'popular'),
     ('Genre Filme', 'http://streamkiste.tv/cat/kinofilme/sortby/popular/', 'http://streamkiste.tv/cat/kinofilme/sortby/update/'),
     ('Filme nach Jahren', 'http://streamkiste.tv/cat/kinofilme/sortby/popular/', 'http://streamkiste.tv/cat/kinofilme/sortby/update/')]
    for sTitle, wq,sortby in tarzlistesi:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('wq', wq)
        oOutputParameterHandler.addParameter('sortby', sortby)
        oOutputParameterHandler.addParameter('siteUrl', wq)
        if sTitle == 'Genre Filme':
            oGui.addDir(SITE_IDENTIFIER, 'GenreFILME', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Filme nach Jahren':
            oGui.addDir(SITE_IDENTIFIER, 'YearsGenreFILME', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Genre FILME':
            oGui.addDir(SITE_IDENTIFIER, 'showSHOW', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Genre SERIEN':
            oGui.addDir(SITE_IDENTIFIER, 'hdfilmeGenreSERIEN', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Suche':
            oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        else:
            oGui.addDir(SITE_IDENTIFIER, 'streamkisteMovies', sTitle, 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

  
def ddizizleABC():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    urll = oInputParameterHandler.getValue('siteUrl')
    url = HTTPKIR(urll)
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')


def addLink(name, url, iconimage):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title': name})
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=str(url), listitem=liz)
    xbmc.Player().play(url, liz)
    sys.exit()
    return ok

            
def GenreFILME():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
    oParser = cParser()
    sPattern = '<h4 class="title"><span>Genres</span></h4>(.*?)<div class="tags">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li><a href="/cat/(.*?)/">(.*?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = aEntry[1]
            sPicture = aEntry[0]
            wq = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('wq', wq)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'streamkisteMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()

              
def YearsGenreFILME():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    sHtmlContent = HTTPKIR(url)
    sHtmlContent = sHtmlContent.replace('\\s', '').replace('\r', '').replace('\n', '')
    oParser = cParser()
    sPattern = '<h4 class="title"><span>Years</span></h4>(.*?)<div class="film-content category">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult
    sPattern = '<li class="year-item year-.*?"><a href="/cat/(.*?)/year/(.*?)/">(.*?)</a></li>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = aEntry[2]
            sPicture = aEntry[1]
            year = aEntry[1]
            wq = str(aEntry[0])
            sTitle = alfabekodla(sTitle)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('wq', wq)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('year', year)
            oGui.addMovie(SITE_IDENTIFIER, 'streamkisteMovies', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def streamkisteMovies():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sortby = oInputParameterHandler.getValue('sortby')
    year = oInputParameterHandler.getValue('year')
    wq = oInputParameterHandler.getValue('wq')
    urll = "http://streamkiste.tv/include/fetch.php" 			
    
    info = {'page': '1', 'type': 'cat', 'wq':wq,'sortby':sortby}
                
                                                    
    url = net.http_POST(urll, info).content
    url= unicodedata.normalize('NFD', url).encode('ascii', 'ignore')#vire accent
    url = url.encode( "utf-8")
    url = urllib.unquote_plus(url)           
    url = url.replace('‹','')      
    sHtmlContent = re.findall('<div class="movie-poster">.*?<a href="(.*?)">.*?<img data-src="(.*?)">.*?<span class="movie-title">.*?<a href=".*?" title="(.*?)">', url, re.S)
    for sUrl, sPicture, sTitle in sHtmlContent:
        sTitle = alfabekodla(sTitle)
        ssUrl='http://streamkiste.tv'+ sUrl
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', ssUrl)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addMovie(SITE_IDENTIFIER, 'Moviesshow', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def Moviesshow():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    urll = oInputParameterHandler.getValue('siteUrl')
    url = HTTPKIR(urll)
    Content = re.findall('e="(.*?)",i="",o="(.*?)"',url, re.S)
    (pid, ceck)= Content[0]
    
    sHtmlContent = re.findall('<li class="stream"><div id="stream-links"><a href="#video" data-mirror="(.*?)" data-host="(.*?)" title="(.*?)">',  url, re.S)
    for mirror,host, sTitle in sHtmlContent:
        
        
             
          cookie = getUrl(urll, output='cookie').result
          req = urllib2.Request(urll)
          req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
          req.add_header('Cookie',cookie)
          req.add_header('Content-Type','application/x-www-form-urlencoded') 
          req.add_header('Host','streamkiste.tv')   
          req.add_header('Origin','http://streamkiste.tv')
          req.add_header('Referer',urll) 
          req.add_header('Content-Length','45')
          req.add_header('Connection','keep-alive')
          req.add_header('Accept-Language','de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4')
          req.add_header('Accept-Encoding','gzip, deflate')
          req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
          info={'pid':pid , 'mirror': mirror, 'host':host,'ceck':ceck,'frame':'2'}
#          sUrl=performCaptcha(urll,cj)
          sUrl = net.http_POST(urll, info).content                                                         
          
          sTitle = alfabekodla(sTitle)
       
             
          
          oOutputParameterHandler = cOutputParameterHandler()
          oOutputParameterHandler.addParameter('siteUrl', sUrl)
          oOutputParameterHandler.addParameter('urll', urll)
          oGui.addTV(SITE_IDENTIFIER, 'hshowMovies', sTitle, '', '', '', oOutputParameterHandler)
                                     
    oGui.setEndOfDirectory()                                          
def recaptcha(sUrl):
          headers=[("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0"),
                 #("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
                 ("Referer", "https://www.google.com/recaptcha/api2/demo"),
                 ("Accept-Language", 'de')]
          filePath = 'c://c.jpeg'
          import random
          n = random.randint(1,1000)
          filePath = 'c://c' + str(n) + '.jpeg'
          sitekey = re.findall('sitekey:"(.*?)"',sUrl, re.S)[0]
          keyname = re.findall('name="(.*?)"',sUrl, re.S)[0]
          rec= re.findall('<script src="(https://www.google.com/.*?render=explicit)"',sUrl, re.S)[0]
          gcookieJar = getg()               
          botguardstring      = "!A" 
          reca=LgetUrl(rec) 
          recap = re.findall("po.src = 'https://www.gstatic.com/recaptcha/api2/(.*?)/recaptcha__(.*?).js'",reca, re.S)
          (pide,lang)= recap[0]
          recaptch = 'https://www.google.com/recaptcha/api2/anchor?k='+sitekey+'&co=aHR0cDovL3N0cmVhbWtpc3RlLnR2Ojgw&hl='+lang+'&v='+pide+'&size=invisible&cb='+keyname
          recaptc = LgetUrl(recaptch)
          import time
          time.sleep(1) 
          recaptca = re.findall('<input type="hidden" id="recaptcha-token" value="(.*?)">',recaptc, re.S)[0]
          
          recaptchs= 'https://www.google.com/recaptcha/api2/userverify?k=6LcGFzMUAAAAAJaE5lmKtD_Oi_YzC837_Nwt6Btv'
                  
#          info = {'v':pide,'c':recaptca,'response':'eyJyZXNwb25zZSI6IiIsInMiOiIzYTMxIn0','t':'','ct':'','bg':BG}
#     
          info = {'recaptcha-token':recaptca}
#          sUrl=performCaptcha(urll,cj)
#               Url = getUrl("https://www.google.com/recaptcha/api2/userverify?k="+sitekey ,post=postdata,headers=headers)                         
  
          Url = net.http_POST(recaptchs, info).content 
          
          return Url[0]
                                                                        
def hshowMovies():               
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    urll = oInputParameterHandler.getValue('urll')
    url =recaptcha(sUrl)
    url = alfabekodla(url)
    referer = [('Referer',url)]
    url = gegetUrl(urll, headers=referer)
    name = 'test'
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]' + name, url, '')

                                                                                            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok



def showMovies(sSearch = ''):
    oGui = cGui()
    if sSearch:
        sSearch = urllib2.unquote(sSearch)
        query_args = {'do': 'search',
         'subaction': 'search',
         'story': str(sSearch),
         'x': '0',
         'y': '0'}
        data = urllib.urlencode(query_args)
        headers = {'User-Agent': 'Mozilla 5.10'}
        url = 'http://hdfilme.tv/'
        request = urllib2.Request(url, data, headers)
        try:
            reponse = urllib2.urlopen(request)
        except URLError as e:
            print e.read()
            print e.reason

        sHtmlContent = reponse.read()
        sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    else:
        oInputParameterHandler = cInputParameterHandler()
        url = oInputParameterHandler.getValue('siteUrl')
        sHtmlContent = HTTPKIR(url)
    sPattern = '<div class="box-product clearfix" data-popover="movie-data-popover-(.*?)">.*?<img class="img" src="(.*?)" onerror="this.src=.*?" alt="(.*?)">'
    sHtmlContent = sHtmlContent
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not aResult[0] == False:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = cUtil().unescape(aEntry[2])
            sPicture = str(aEntry[1])
            Url = str(aEntry[0])
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', Url)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            if '/serie/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            elif '/anime/' in aEntry[1]:
                oGui.addTV(SITE_IDENTIFIER, 'serieHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'MOVIEHosters', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
        if not sSearch:
            sNextPage = sEcho(str(url))
            if sNextPage != False:
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sNextPage)
                oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    if not sSearch:
        oGui.setEndOfDirectory()


def __NextPage(sHtmlContent, url):
    sPattern = '<li class="active">.*?<a href="javascript:void(0)" data-page="(.*?)">'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        url = url + '?page=' + aResult[1][0]
        if 'desc' in url:
            url = url + '&page=' + aResult[1][0]
        return str(url)


def __checkForNextPage(sHtmlContent):
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sPattern = '</a> <a href="(.*?)" class="syfno">Sonraki Sayfa &raquo;</a>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        return str(sUrl) + aResult[1][0]
    return False


def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Urlk = 'http://hdfilme.tv/'
    referer = [('Referer', Urlk)]
    adata = gegetUrl(Url, headers=referer)
    sHtmlContent = base64.b64decode(adata)
    sPattern = '"label":"(.*?)","file":"(.*?)"'              
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            TUK = '|Referer=' + Url + '&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
            sTitle =aEntry[0]
            sUrl = aEntry[1].replace('\\/', '/') + TUK
            sTitle = alfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'play__hdfilme', sTitle, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def MOVIEHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    Urlk = 'http://hdfilme.tv/'
    Urll = 'http://hdfilme.tv/movie/getlink/' + Url + '/1'
    referer = [('Referer', Urlk)]
    adata = gegetUrl(Urll, headers=referer)
    sHtmlContent = base64.b64decode(adata)
    sPattern = '"label":"(.*?)","file":"(.*?)"'             
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] == True:
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            TUK = '|Referer=' + Urll + '&User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
            sGenre = cUtil().unescape(aEntry[0])
            sUrl = aEntry[1].replace('\\/', '/') + TUK
            sTitle = aEntry[0].decode('latin-1').encode('utf-8')
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addTV(SITE_IDENTIFIER, 'play__hdfilme', sGenre, '', '', '', oOutputParameterHandler)

        cConfig().finishDialog(dialog)
    oGui.setEndOfDirectory()


def play__hdfilme():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTitle = alfabekodla(sTitle)
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(sTitle)
    oGuiElement.setMediaUrl(sUrl)
    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()


def mshowHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    streamid = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    sUrl = getStreamSRC(streamid)
    sHosterUrl = sUrl
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    if oHoster != False:
        sMovieTitle = cUtil().DecoTitle(sMovieTitle)
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumbnail)
    oGui.setEndOfDirectory()