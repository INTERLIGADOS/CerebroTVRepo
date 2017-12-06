#-*- coding: utf-8 -*-
#http://getproxi.es/TR-proxies//^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
import urlparse,sys,re,xbmcgui,os
try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database


title = 'OTV_MEDIA'
import control
import binascii
import js2py
from resources.lib.otvhelper import *                  
SITE_IDENTIFIER = 'orhantv'
SITE_NAME = 'OTV_MEDIA'
from youtubecom_tr import YouTUBE 
from turkvod_org import TUrKVod
from myvideo_az import MYVIDEOAZ 
from myvideo_ge import MYVIDEOGeor
from filmon_com import FILMON
from Arabic_tv import Arabictv
from liveonlinetv247 import Sport
from liveonlinetv247 import Almanlivestream
import urlparse,sys,re,xbmcgui,os
import re,unicodedata
HOST = 'ajanspor7.tv'
import binascii         

def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku        
url1="PXdXYjQ1Q1praDJMbWxUTTI4V2NrbFdadzRXY25KRE52TTNMdDkyWXVRbmJsUm5idk5tY2xOWGQ0OW1ZdzltY2s1Q2JrOXlMNk1IYzBSSGE="
url2 = base64.b64decode(url1)
url3 =  okuoku(url2)            
streamurl=base64.b64decode(url3)
def amzddecode(k4):                                                                                                                                                                                          
	k4 = k4.replace('htup>+.akegw|gv7#~q+ixa?bem&k7w8 mi!','https://yayin2.betajani.net/hls/lig1.m3u8?st=').replace('htupw>./lej}mqmnl`fjrd}b?"{)lns0rt{*4t+b.*gg/','https://canlimacyayiniajanspor.us/hls/lig1.m3u8?st=').replace('#a>','&e=').replace('','').replace('2f626567686565','macyayinajanspor.us/hls/lig1.m3u8?st=').replace('0645978320','canlimacyayiniajanspor.us/hls/lig1.m3u8?st=').replace('074342858670','%').replace('093857354460','www').replace('07463394760','/')
	k4 = k4.replace('6a','a').replace('0890','b').replace('0920','c').replace('0970','d').replace('0740','e').replace('0940','f').replace('60','g').replace('0140','h').replace('6c','i')
	k4 = k4.replace('6e','j').replace('0130','k').replace('0110','l').replace('7f','m').replace('63','n').replace('0460','p').replace('0710','q').replace('0270','r')
	k4 = k4.replace('0340','s').replace('7e','t').replace('0860','u').replace('77','v').replace('0330','w').replace('0830','x').replace('0350','y').replace('01230','z')
	k4 = k4.replace('0910','A').replace('0160','B').replace('0590','C').replace('0690','D').replace('47','E').replace('56','F').replace('0720','G').replace('0580','H').replace('46','I')
	k4 = k4.replace('4c','J').replace('0730','K').replace('0120','L').replace('0750','M').replace('0210','N').replace('5c','P').replace('51','Q').replace('0780','R')
	k4 = k4.replace('0650','S').replace('0420','T').replace('5d','U').replace('098340','V').replace('09740','W').replace('047450','X').replace('08820','Y').replace('59','Z')
	k4 = k4.replace('6d','m').replace('45','E').replace('08658476940','$').replace('09284656560','/').replace('0856483980','%').replace('0847337644730','*')
	k4 = k4.replace('01928595750','?').replace('087535889970','\\').replace('05372893470','^').replace('085337390560','&').replace('085337777560','+').replace('033779940','.')
	k4 = k4.replace('011996430','#').replace('0774411990','"').replace('09774320','(') .replace('0777224880',')').replace('087232220','{').replace('07772374260','}').replace("086735754840","'").replace('0573757534590',':').replace('05731122590',';')
	k4 = k4.replace('083475590','!').replace('0777446310','|').replace('097544770','[').replace('07547382590','\]').replace('08345867760', '_').replace('0847785894580','-')
	k4 = k4.replace('0760','1').replace('0660','2').replace('09190','3').replace('07590','4').replace('3c','5').replace('0950','6').replace('07210','7').replace('36','8').replace('28','9').replace('0810','0').replace('39','8')
	return k4	
                 
def streamangodecode(encoded):
        #from https://github.com/jsergio123/script.module.urlresolver
        _0x59b81a = ""
        k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        k = k[::-1]

        count = 0
        D="B7"
        for index in range(0, len(encoded) - 1):
            while count <= len(encoded) - 1:
                _0x4a2f3a = k.index(encoded[count])
                count += 1
                _0x29d5bf = k.index(encoded[count])
                count += 1
                _0x3b6833 = k.index(encoded[count])
                count += 1
                _0x426d70 = k.index(encoded[count])
                count += 1

                _0x2e4782 = ((_0x4a2f3a << 2) | (_0x29d5bf >> 4))
                _0x2c0540 = (((_0x29d5bf & 15) << 4) | (_0x3b6833 >> 2))
                _0x5a46ef = ((_0x3b6833 & 3) << 6) | _0x426d70
               

                _0x59b81a = str(_0x59b81a) + chr(_0x2e4782)

                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x2c0540)
                if _0x3b6833 != 64:
                    _0x59b81a = str(_0x59b81a) + chr(_0x5a46ef)

        return _0x59b81a
def clear():
    try:
        cacheFile = os.path.join(control.dataPath, 'regex.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("DROP TABLE IF EXISTS regex")
        dbcur.execute("VACUUM")
        dbcon.commit()
    except:
        pass

def aes_decdecrypt(result):
        
            from resources.lib import pyaes
            aes = pyaes.AESModeOfOperationOFB(control.key, iv=control.iv)
            result = aes.decrypt(result.decode('string-escape'))
            return result
        
def aes_decencrypt(result):
            
            from resources.lib import pyaes
            aes = pyaes.AESModeOfOperationCBC(control.key, iv=control.iv)
            result = aes.decrypt(result)
            return result
      
def orhantv():
    oGui = cGui()              
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'orhatvturk', 'TürK_MEDIA', 'https://img3.picload.org/image/rappiapc/turk_bayragi_tc_16.png', 'https://img3.picload.org/image/rappiapc/turk_bayragi_tc_16.png', '', oOutputParameterHandler)
    
        
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'TUrKVod', 'TÜrK_Vod', 'https://picload.org/thumbnail/rwlgpaci/icon.jpg', 'https://picload.org/thumbnail/rwlgpaci/icon.jpg', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'MYVIDEOAZ', 'MYVIDEO AZ', 'https://lh3.googleusercontent.com/RjKlop05To_i4dPLitHZv4paU5FE4aU_F7ye7Gyf8rJbqPiQKgg04sNJ2HDGW-2u-PE=w300-rw', 'https://lh3.googleusercontent.com/RjKlop05To_i4dPLitHZv4paU5FE4aU_F7ye7Gyf8rJbqPiQKgg04sNJ2HDGW-2u-PE=w300-rw', '', oOutputParameterHandler)

    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'orhantvalman', 'GERMAN_MEDIA', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Schwarz_Rot_Gold.svg/1000px-Schwarz_Rot_Gold.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Schwarz_Rot_Gold.svg/1000px-Schwarz_Rot_Gold.svg.png', '', oOutputParameterHandler)

    
    liz=xbmcgui.ListItem('IPTV_int',thumbnailImage= "https://superrepo.org/static/images/icons/original/xplugin.video.xtream-codes.png.pagespeed.ic.7uLaZTpLY3.png",iconImage="DefaultFolder.png")
    uurl="plugin://plugin.video.OTV_MEDIA/PLUG?fanart=C%3a%5cUsers%5corhantv%5cAppData%5cRoaming%5cXBMC%5caddons%5cplugin.video.live.streams%5cfanart.jpg&mode=1&name=dddddd&url="+streamurl
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), listitem=liz,url=uurl,isFolder=True)   
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'MCategories', 'IPTV_int2', 'https://superrepo.org/static/images/icons/original/xplugin.video.xtream-codes.png.pagespeed.ic.7uLaZTpLY3.png', 'https://superrepo.org/static/images/icons/original/xplugin.video.xtream-codes.png.pagespeed.ic.7uLaZTpLY3.png', '', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'Arabictv', 'ARABIC TV', 'http://ndl.mgccw.com/mu3/app/20140612/17/1402576108781/ss/1_small.png', 'http://ndl.mgccw.com/mu3/app/20140612/17/1402576108781/ss/1_small.png', '', oOutputParameterHandler)


    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'MYVIDEOGeor', 'MYVIDEO Georgia', 'https://lh3.googleusercontent.com/VWgWZC9dpnsPSawJcThoUA6J_r4G8Qlk5hR3vNCdVVLTIm2DC5s0T9I2Ypi8nLxjd7w=w300-rw', 'https://lh3.googleusercontent.com/VWgWZC9dpnsPSawJcThoUA6J_r4G8Qlk5hR3vNCdVVLTIm2DC5s0T9I2Ypi8nLxjd7w=w300-rw', '', oOutputParameterHandler)
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'Sport', 'SPORT', 'http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg', 'http://cliparting.com/wp-content/uploads/2016/06/Sports-clipart-free-clipart-images.jpg', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'YouTUBE', 'YouTUBE', 'https://cdn.pixabay.com/photo/2015/03/10/17/23/youtube-667451_960_720.png', 'https://cdn.pixabay.com/photo/2015/03/10/17/23/youtube-667451_960_720.png', '', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'FILMON', 'FILMON', 'http://talkbusiness360.com/wp-content/uploads/2017/03/FilmOn-TV-img-390x215.png', 'http://talkbusiness360.com/wp-content/uploads/2017/03/FilmOn-TV-img-390x215.png', '', oOutputParameterHandler)
    
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'viewDialog', '[COLOR teal]OTV MEDIA Update Info[/COLOR]', 'http://das2014.sciencesconf.org/conference/das2014/pages/info.PNG', 'http://das2014.sciencesconf.org/conference/das2014/pages/info.PNG', '', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://orhantv')
    oGui.addTV(SITE_IDENTIFIER, 'PlaylistCategories', '[COLOR teal]My PlayList[/COLOR]', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1EJoofnHYe-8L92TT8nWdn6uqBZpQxEE9YhVKII2oAUN-Jk9V', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1EJoofnHYe-8L92TT8nWdn6uqBZpQxEE9YhVKII2oAUN-Jk9V', '', oOutputParameterHandler)
                                     
    oGui.setEndOfDirectory()                    
def mmdecodeURL():    
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'

    url = 'https://h5p2p.peer-stream.com/chunks/orfeins_hd.webm_9moGtIK8gcJlStOH._a_42496.chk' +TIK
    name ='test'                                                                                          
                
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')

def bennms():        
    url = 'https://dl.dropboxusercontent.com/s/zve0u4hvid4f10l/mtv_de.xml?dl=0'
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().get(url)
#callbackpath="https://cdn.syndication.twimg.com/widgets/followbutton/info.json?callback=__twttr.setFollowersCountAndFollowing&lang=en&screen_names=ajanspor_tv"
from filmakinesi_org import turksinema
from canlifm_com import Radyo
from coukyoutube_tr import coukyoutube
from mynet_com import mynetcom
from iptvbox import iptvturk
from kanald_com_tr import turkTV
from diziizle_net import turkdizi                  
from turkhaber_tr  import turkhaber   
def decodeSourceURL(uhash):
    uhash= uhash.decode('ISO-8859-15').encode( "utf-8") 
    return decode(uhash)
from oneplay import func_L

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

import logging
import base64
def yaz64(s):
    """Add missing padding to string and return the decoded base64 string."""
    log = logging.getLogger()
    s = str(s).strip()
    try:
        return base64.b64decode(s)
    except TypeError:
        padding = len(s) % 4
        if padding == 1:
            log.error("Invalid base64 string: {}".format(s))
            return ''
        elif padding == 2:
            s += b'=='
        elif padding == 3:
            s += b'='
        return base64.b64decode(s)
def yaz64(e):
        _keyStr="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
        t = ""
        f = 0
        e = re.sub(r"[^A-Za-z0-9\+\/\=]", "", e)
        while f < len(e):
            s = _keyStr.find(e[f])
            f += 1
            o = _keyStr.find(e[f]) if f < len(e) else 0
            f += 1
            u = _keyStr.find(e[f]) if f < len(e) else 0
            f += 1
            a = _keyStr.find(e[f]) if f < len(e) else 0
            f += 1
            n = s<<2|o>>4
            r = (o&15)<<4|u>>2
            i = (u&3)<<6|a
            t = t + chr(n)
            if u != 64: t = t + chr(r)
            if a != 64: t = t + chr(i)
        return t

#h t u p w > . / b e g h e e e c t k ~ m o u x q ` z g t *w s 0 v q o 4 v p  & 8 x ' f *. c { 3 I > F 9 V n q 5 g w l G h P c q K l i ,Y f " l 9= =4 5 =9 5 2 5%
#h t t p s : / / m a c y a y i n i a j a n s p o r . u s / h l s / l i g 1 . m 3 u 8 ? s t = p j u E m K w l m K t Z t v 2 - O L 3 8 k Q & e = 1 5 0 5 0 3 2 6 2 6
def okuoku(cba):
        oku = ""
        i = len(cba) - 1
        while i >= 0:
            oku += cba[i]
            i -= 1
        return oku      

def geantsat1():
    sUrl='http://www.geantsat.com/free-iptv/' 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://miplayer.net/embed.php?id=ligtv1&width=650&height=480&autoplay=true', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(sUrl, headers = headers).text

    liste = re.findall('<a style="font-size: 20px;" href="(.*?)"',data, re.S)
    for Url in liste:
    
        return Url   
def o0OOOooo0OOo ( s ) :
 O0O = [ s [ OoO0O00 : OoO0O00 + 3 ] for OoO0O00 in range ( 0 , len ( s ) , 3 ) ]
 return '' . join ( chr ( int ( val ) ) for val in O0O )
from urlparse import urlparse
import js2py  




def matvcomtr():
    oGui = cGui()                           
    liste = []
    liste.append( ['ATV CANLI','#EXTINF:0 tvg-name=".*?".*?>(TR:.*?)\n(.*)\n'] ) 
    liste.append( ['ATV YEDEK','https://canlitv.co/atv.html'] ) 
    liste.append( ['A HABER CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/ahaberhd/ahaberhd.m3u8'] )
    liste.append( ['A SPOR CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/asporhd/asporhd.m3u8']) 
    liste.append( ['minikaGO CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikago/minikago.m3u8']) 
    liste.append( ['minikaCOCUK CANLI','http://videotoken.tmgrup.com.tr/webtv/secure?url=http://trkvz-live.ercdn.net/minikagococuk/minikagococuk.m3u8'] ) 
    liste.append( ['YENİ DİZİLER','http://www.atv.com.tr/(S(w3ia53anisrqi0zawpcegfnk))/diziler'] )
    liste.append( ['KLASİK DİZİLER','http://www.atv.com.tr/(S(w3ia53anisrqi0zawpcegfnk))/klasik-diziler'] )
    for sTitle,sUrl2 in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'PROGRAMLAR':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema',  sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'KLASİK DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'ArshowSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'YENİ DİZİLER':
             oGui.addDir(SITE_IDENTIFIER, 'showSinema', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'DİZİLER ABC':
             oGui.addDir(SITE_IDENTIFIER, 'Hosters', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'ATV YEDEK':
             oGui.addDir(SITE_IDENTIFIER, 'canlitvzoneBox', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'mplay__weebtv',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()

def livestreamtv():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = 'http://www.live-stream.tv/online/fernsehen/deutsch/arte.html'
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    oParser = cParser()
    sPattern = 'class="list-group sidebarActive">(.+?)<div id="sidenavTwitter"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    sHtmlContent = aResult                                
    sPattern = '<a href="(.*?)" class="list-group-item">.*?<img src="(.*?)" alt="(.*?)"'
    sHtmlContent = sHtmlContent
    sHtmlContent = alfabekodla(sHtmlContent)
    oParser = cParser()                                                               
    aResult = oParser.parse(sHtmlContent, sPattern)
    if not (aResult[0] == False):
        total = len(aResult[1])
        dialog = cConfig().createDialog(SITE_NAME)
       
        for aEntry in aResult[1]:
            cConfig().updateDialog(dialog, total)
            if dialog.iscanceled():
                break
            sTitle = alfabekodla(aEntry[2])
                                               
            sPicture = 'http://www.live-stream.tv'+str(aEntry[1])
            
                
            sUrl = str(aEntry[0])
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
                
            #not found better way
            #sTitle = unicode(sTitle, errors='replace')
            #sTitle = sTitle.encode('ascii', 'ignore').decode('ascii')
           
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('sThumbnail', sPicture) #sortis du poster
 
            oGui.addMovie(SITE_IDENTIFIER, 'PLAYlivestreamtv', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
 
        cConfig().finishDialog(dialog) 
        
         
    oGui.setEndOfDirectory()
  
from resources.lib import  unwise    
def PLAYlivestreamtv():
    oGui = cGui()
    UA='Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
   
    oInputParameterHandler = cInputParameterHandler()
    Url = oInputParameterHandler.getValue('siteUrl')
    referer = oInputParameterHandler.getValue('siteUrl')
    name = oInputParameterHandler.getValue('sMovieTitle')
    
                                
    dat= requests.get(Url).content
                  
    urll = re.findall('<iframe src="(.*?)"',dat, re.S)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36','Referer': referer  }
    urlm= requests.get(urll, headers = headers).text
    urlm=urlm.replace('\r',"").replace('\s',"").replace('\n',"").replace(';eval',"eval").replace(';</script>',"</script>")
                                                                     
    
    TIK='|User-Agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'

    urlh = re.findall('<script type="text/javascript">(eval.function.w,i,s,e.*?)</script>',urlm, re.S)[0]                       
       
    urlk =unwise.unwise_process(urlh) 
    urlk = urlk.replace('//',"").replace('\r',"").replace('\s',"").replace('\n',"").replace('; eval',"eval")
    urln = re.findall('(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))',urlk, re.S)[0]                       
    
    urlw =  cPacker().unpack(urln)
    urlw = urlw.replace('\\',"")
    baseUrl = re.findall('baseUrl:"(.*?)"',urlw, re.S)[0] 
    TIK='|User-Agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25&Referer='+referer
            
    url = re.findall("source:'(.*?)'",urlw, re.S)[0]
    url = url.replace('https:',"https://").replace('http:',"http://")
    cookie = getUrl(urll, output='cookie').result 
    if url.find('akamaihd') > -1:      
         url =url +'|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&X-Forwarded-For=62.75.128.93' 
    else:
         url =url+ '|User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3&Referer='+ urll
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
    
      

def sshowBox3(url,name):
   
    name = alfabekodla(name)
    
    from resources.lib.hlsplayer import hlsproxy
    
    progress = xbmcgui.DialogProgress()
    import checkbad
    checkbad.do_block_check(False)
    stopPlaying=threading.Event()
    _bitrate =0
    f4m_proxy=hlsproxy()
    stopPlaying.clear()
    runningthread=thread.start_new_thread(f4m_proxy.start,(stopPlaying,))
    progress.create('Starting HLS Player')
    streamtype='HLSRETRY'                                                                   
    
    progress.update( 20, "", 'Loading local proxy', "" )
    url_to_play=f4m_proxy.prepare_url(url,proxy,use_proxy_for_chunks,maxbitrate=maxbitrate,simpleDownloader=simpleDownloader,auth=auth,streamtype=streamtype,swf=swf ,callbackpath=callbackpath,callbackparam=callbackparam)
    listitem = xbmcgui.ListItem(name,path=url_to_play, iconImage=iconImage, thumbnailImage=iconImage)
    listitem.setInfo('video', {'Title': name})
    if setResolved:
        return url_to_play, listitem
    mplayer = MyPlayer()    
    mplayer.stopPlaying = stopPlaying
    progress.close() 
    mplayer.play(url_to_play,listitem)

    firstTime=True
    played=False
    while True:
       if stopPlaying.isSet():
           break;
       if xbmc.Player().isPlaying():
           played=True
       xbmc.log('Sleeping...')
       xbmc.sleep(200)
                #if firstTime:
                #    xbmc.executebuiltin('Dialog.Close(all,True)')
                #    firstTime=False
            #stopPlaying.isSet()

    print 'Job done'
    return played
class MyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 



def _m3u8Exit(self):
     import otv_kuresel
     otv_kuresel.yt_tmp_storage_dirty = True    
     
class mmMyPlayer (xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)

    def play(self, url, listitem):
        print 'Now im playing... %s' % url
        self.stopPlaying.clear()
        xbmc.Player( ).play(url, listitem)
        
    def onPlayBackEnded( self ):
        # Will be called when xbmc stops playing a file
        print "seting event in onPlayBackEnded " 
        self.stopPlaying.set();
        print "stop Event is SET" 
    def onPlayBackStopped( self ):
        # Will be called when user stops xbmc playing a file
        print "seting event in onPlayBackStopped " 
        self.stopPlaying.set();
        print "stop Event is SET" 

def root(url):
        
        try:
          
            url = base64.b64decode(url)
            
           
            return url
        except:
            pass
enc=''
def _m3u8Exit(url):
     
     return url

url1="PXdXYjQ1Q1praDJMbWxUTTI4V2NrbFdadzRXY25KRE52TTNMdDkyWXVRbmJsUm5idk5tY2xOWGQ0OW1ZdzltY2s1Q2JrOXlMNk1IYzBSSGE="
url2 = base64.b64decode(url1)
url3 =  okuoku(url2)            
streamurl=base64.b64decode(url3)
def weebtv():
    oGui = cGui() 
    
    from resources.lib.indexers import bennustreams
    bennustreams.indexer().root()
    


def hextranslate(s):
        res = ""
        for i in range(len(s)/2):
                realIdx = i*2
                res = res + chr(int(s[realIdx:realIdx+2],16))
        return res    

           
mac =''		
def StartPort(url, mac = None):
        url = url.replace('TURKvodModul@','').replace('@m3u@TURKvod','?')
        sign = '?'
        url = url.strip(' \t\n\r')
        if url.find('?') > -1:
            sign = '&'
        if mac != None:
            security_key = ""
            security_param = ""
            url = url + sign + 'box_mac=' + mac + security_key + security_param
        if url.find('|') > -1:
                parts = url.split('|')
                url = parts[0]
                pass#print "Here in Turkvod url 6 =", url
                cookie = parts[1]
                req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 TURKvod 8.0',
                 'Connection': 'Close',
                 'Cookie': cookie})
        else:
                req = urllib2.Request(url, None, {'User-agent': 'Mozilla/5.0 TURKvod 8.0',
                 'Connection': 'Close'})
        xmlstream = urllib2.urlopen(req).read()
        pass#print "Here in Turkvod xmlstream  =", xmlstream 

        return xmlstream


def mmdecodeURL():
                                   
#    url =otvkodla(img_url)
                                               
    sUrl= "http://cricfree.sc/sky-sports-golf-live-stream" 			
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': 'http://cricfree.sc/', 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    data = requests.get(sUrl, headers = headers).text
#    url = unicode(url, 'latin-1')#converti en unicode
    urll = re.findall('<div class="iframe">.*?<iframe.*?src="(.*?)"',data, re.S)[0]   
    dat= requests.get(urll, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': sUrl, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}).text 
    dat = dat.replace('&amp;','&')

    urlk = re.findall('<iframe.*?src="(.*?)"></iframe>',dat, re.S)[0]   
                                                                   
    urln = requests.get(urlk, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': urll , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}).text 
    urln = urln.replace('&amp;','&')
    urlk = re.findall('<iframe.*?src="(.*?)"></iframe>',urln, re.S)[0] 
    urlm = requests.get(urlk, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36 OPR/41.0.2353.69', 'Referer': urlk , 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}).text 

    urlm = urlm.replace('","','').replace('\/','/').replace('(','').replace(')','').replace('[','').replace(']','')
#    urlk = re.findall('return"(.*?)"',urlm, re.S)[0]   
#    key = re.findall('join"" + (.*?).join',urlm, re.S)[0]   
#    key1 = re.findall('"" + document.getElementById"(.*?)"',urlm, re.S)[0]   
    
#    token = re.findall('var '+key+' = "(.*?)"',urlm, re.S)[0]
#    token1 = re.findall('var '+key1+' = "(.*?)"',urlm, re.S)[0]               
    url= urlm
    name ='test'                                                                                          
                
    addLink('[COLOR lightblue][B]OTV MEDIA >>  [/B][/COLOR]'+name,url,'')
            
#            url = 'https://yayin2.kuralbet25.com/hls/lig1.m3u8?st=xOoqxCRIYuZvLSYzcIw76Q&e=1507559184'
#            url = base64.b64encode(urll)
            

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty("IsPlayable", "true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=str(url),listitem=liz)
        xbmc.Player().play(url,liz)
        sys.exit()
        return ok
def orhatvturk():
    oGui = cGui()              
    liste = []
    liste.append( ['Türk TV','https://lh6.ggpht.com/oRC2FbooV1AM_CzYXld6WS0UNmmILRDVmE30zRcNjDsxgFX-Qrz_Z-ks9P3MCteWMg=h1080'] ) 
    liste.append( ['Türk Dizi','https://pbs.twimg.com/profile_images/543610023973097472/lEtD1thL.png'])
    liste.append( ['Türk Spor','https://www.tvipx.com/wp-content/uploads/2017/01/tv_arayuz_iptv.png'] ) 
    liste.append( ['Türk Sinema','http://www.nekadarizlendi.com/wp-content/uploads/2017/02/Ekran-Resmi-2017-02-19-11.50.16.png'])
    liste.append( ['Türk Haber TV ler','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsAq3k8fdg482MolI1daokIi6Y7YGZ7F0nKBmcsauda0UqWXgtlw']) 

    liste.append( ['Türk Cizgi Film','https://i1.imgiz.com/rshots/8054/oyun-hamurundan-pepee-cizgi-film-karakterleri-oyun-hamuru-ile-pepee-yapimi-izle_8054045-3940_1200x630.jpg']) 
    liste.append( ['Türkce KARAOKE','http://twenty23three.com/wp-content/uploads/2016/05/1.png']) 
    liste.append( ['Türk Video','https://img7.mynet.com/mmynet/mynet-logo.png']) 
    liste.append( ['Türk Radyo','http://muzikonair.com/wp-content/uploads/radyo-kanallari-muzikonair1-830x470.jpg']) 
    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'Türk Spor':
             oGui.addMovie(SITE_IDENTIFIER, 'Sport',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk TV':
             oGui.addMovie(SITE_IDENTIFIER, 'turkTV',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Dizi':
             oGui.addMovie(SITE_IDENTIFIER, 'turkdizi', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Sinema':
             oGui.addMovie(SITE_IDENTIFIER, 'turksinema', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Cizgi Film':
             oGui.addMovie(SITE_IDENTIFIER, 'coukyoutube', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Video':
             oGui.addMovie(SITE_IDENTIFIER, 'mynetcom', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Radyo':
             oGui.addMovie(SITE_IDENTIFIER, 'Radyo', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türkce KARAOKE':
             oGui.addMovie(SITE_IDENTIFIER, 'xkaraoketr', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'Türk Haber TV ler':
             oGui.addMovie(SITE_IDENTIFIER, 'turkhaber', sTitle, sPicture, sPicture, '', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()                    



def xkaraoketr():
    oGui = cGui()
    from youtubecom_tr import KARAOKEturk                 
    KARAOKEturk()                
    oGui.setEndOfDirectory()



 
from adult_eu import pincode
from radio_de import radiode
from filmpalast_to import almanKINO


def orhantvalman():
    oGui = cGui()              
    liste = []
    liste.append( ['KINO FILME','https://cdn.pixabay.com/photo/2013/07/13/14/03/film-162028_960_720.png'] ) 
    liste.append( ['TV SENDER','https://vmaz.me/wp-content/uploads/2014/12/tv2.png'])
    liste.append( ['RADIO','http://st.depositphotos.com/1581702/3519/i/950/depositphotos_35197653-stock-photo-old-radio-antique-brown-radio.jpg'] ) 
    liste.append( ['ADULT','https://cdn.pixabay.com/photo/2015/03/30/03/31/hair-697938_960_720.jpg'])
   
    for sTitle,sPicture in liste:
                       
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sPicture)
        if sTitle == 'KINO FILME':
             oGui.addMovie(SITE_IDENTIFIER, 'almanKINO',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'TV SENDER':
             oGui.addMovie(SITE_IDENTIFIER, 'Almanlivestream',sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'RADIO':
             oGui.addMovie(SITE_IDENTIFIER, 'radiode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
        elif sTitle == 'ADULT':
             oGui.addMovie(SITE_IDENTIFIER, 'pincode', sTitle, sPicture, sPicture, '', oOutputParameterHandler)
              
        else:
             oGui.addDir(SITE_IDENTIFIER, 'showBox',  sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()                    


















param= ''

def Iptvint25():
        oGui = cGui()
        from turkvod_org import Categories
        Categories(param)

    
def Iptvint2():
        oGui = cGui()
        from default import Iptvint2
        Iptvint2()  
def TurkCategories():
        oGui = cGui()
        from resources.sayfalar.iptvbox import iptvturk
        iptvturk()                   
    
    


def PlaylistCategories():
        oGui = cGui()
        from default  import PlaylistCategories
        PlaylistCategories()                   
                    
def Almantv():
        oGui = cGui()
        from default import Almantv
        Almantv() 
    
def MCategories():
        oGui = cGui()
        from default  import MCategories
        MCategories() 

import urlparse,sys,re,xbmcgui,os
import pyxbmct
pyxbmct = pyxbmct.addonwindow



def viewDialog():
    url='https://dl.dropboxusercontent.com/s/8p15unh67s2drk4/Tips.txt'
    global msg_text
    
    if url.startswith('https'): msg_text = client.request(url)
    else: 
        with open(url,mode='r')as f: msg_text = f.read()
    
    #xxxtext.TextWindow(msg_text)
    window = TextBox('OTV_MEDIA')
    window.doModal()
    del window

class TextBox(pyxbmct.AddonDialogWindow):
   
    def __init__(self, title = 'OTV_MEDIA'):
        super(TextBox, self).__init__(title)
        self.setGeometry(800, 700, 14, 30, 0, 3, 5)
        self.set_info_controls()
        self.set_active_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)

    def set_info_controls(self):

        Background   = pyxbmct.Image(xbmc.translatePath(os.path.join('special://home/addons/plugin.video.OTV_MEDIA', 'art/note.png')))
        self.placeControl(Background, -2, -1, 17, 34)
        self.textbox = pyxbmct.TextBox()
        self.placeControl(self.textbox, 0, 1, 13, 28)
        self.textbox.setText(msg_text)
        self.textbox.autoScroll(1000, 800, 1000)

    def set_active_controls(self):
        self.button = pyxbmct.Button('Close')
        self.placeControl(self.button, 12,26,1,4)
        self.connect(self.button, self.close)

    def set_navigation(self):
        self.button.controlUp(self.button)
        self.button.controlDown(self.button)
        self.button.controlRight(self.button)
        self.button.controlLeft(self.button)
        self.setFocus(self.button)

    def setAnimation(self, control):
        control.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=200',), ('WindowClose', 'effect=fade start=100 end=0 time=300',)])
  
       
