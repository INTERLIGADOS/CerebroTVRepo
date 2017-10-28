import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os,cookielib
from datetime import datetime,tzinfo,timedelta
import json
import base64

dp = xbmcgui.DialogProgress()

def resolve(url):
        import requests
        if 'tvcatchup' in url:
            open = OPEN_URL(url)
            url  = re.compile('   var.+?"(.+?)"').findall(open)[0]
            url  = base64.b64decode(url)
            url  = url  + '|User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

        elif 'ustreamix' in url:
            url = ustreamixresolve(url)
                                    
        elif 'arconaitv' in url:
            ref  = url
            open = OPEN_URL(url)
            url  = re.compile('source src="(.*?)"',re.DOTALL).findall(open)[0]
            url  = (url).replace('\/','/')
            url  = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36&Referer='+ref  
            
#####           
        elif 'firstone.tv' in url:
            #ref  = url
            url = url+'|User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36&Referer=https://www.firstone.tv/ucount.php?i=5842f648660464416771ec2b145a7783&u=no&c=1501896711557'

#######     
        else:
            url = url
        return (url).replace('<p>','')

def ustreamixresolve(url):
    import re,base64,requests
    html = OPEN_URL(url)
    ohtm = eval(re.findall('VNB.*?(\[.*?\])',html,re.DOTALL)[0])
    oval = int(re.findall('replace.*?- (\d*)',html)[0])
    phtml = ''
    for oht in ohtm:
        phtml += chr(int(re.findall('\D*(\d*)',oht.decode('base64'))[0]) - oval)
                
    strurl = re.findall("var stream = '(.*?)'",phtml)[0]
    tokurl = re.findall('src="(.*?)"',phtml)[0]
    hdr = {}
    hdr['Referer'] = url
    tokpg = requests.get(tokurl,headers=hdr,verify=False).text
    token = re.findall('jdtk="(.*?)"',tokpg)[0]
    url   = strurl+token+'|referer=&User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36&&X-Requested-With: ShockwaveFlash/25.0.0.171'
    return url
        
def getCookiesString(cookieJar):
    try:
        cookieString=""
        for index, cookie in enumerate(cookieJar):
            cookieString+=cookie.name + "=" + cookie.value +";"
    except: pass
    #print 'cookieString',cookieString
    return cookieString

def getTVPCookieJar(updatedUName=False):
    cookieJar=None
    print 'updatedUName',updatedUName
    try:
        cookieJar = cookielib.LWPCookieJar()
        if not updatedUName:
            cookieJar.load(TVPCOOKIEFILE,ignore_discard=True)
    except: 
        cookieJar=None

    if not cookieJar:
        cookieJar = cookielib.LWPCookieJar()
    return cookieJar
    
def OPEN_URL(url):
    import requests
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    link = requests.session().get(url, headers=headers, verify=False).text
    link = link.encode('ascii', 'ignore')
    return link
    
def getUrl(url, cookieJar=None,post=None, timeout=10, headers=None,jsonpost=False):

    cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
    header_in_page=None
    if '|' in url:
        url,header_in_page=url.split('|')
    req = urllib2.Request(url)

    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    req.add_header('Accept-Encoding','gzip')

    if headers:
        for h,hv in headers:
            req.add_header(h,hv)
    if header_in_page:
        header_in_page=header_in_page.split('&')
        
        for h in header_in_page:
            if len(h.split('='))==2:
                n,v=h.split('=')
            else:
                vals=h.split('=')
                n=vals[0]
                v='='.join(vals[1:])
            req.add_header(n,v)
            
    if jsonpost:
        req.add_header('Content-Type', 'application/json')
    response = opener.open(req,post,timeout=timeout)
    if response.info().get('Content-Encoding') == 'gzip':
            from StringIO import StringIO
            import gzip
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            link = f.read()
    else:
        link=response.read()
    response.close()
    return link;
    
def regex_from_to(text, from_string, to_string, excluding=True):
    import re,string
    if excluding:
        try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
        except: r = ''
    else:
        try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
        except: r = ''
    return r

def regex_get_all(text, start_with, end_with):
    import re
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r
    
def PlayLive(name,url,iconimage):
    #dp.create(AddonTitle,"Finding link...",'[COLOR yellow]Please wait........[/COLOR]','')   
    #dp.update(0)
    url = url.strip()

    if url.endswith('.ts'):
        url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=TSDOWNLOADER'
    elif url.endswith('.mpegts'):
        url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=TSDOWNLOADER'
    elif url.endswith('.m3u8'):
        url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)+'&amp;streamtype=HLSRETRY'
    elif url.endswith('.f4m'):
        url = 'plugin://plugin.video.f4mTester/?url='+urllib.quote_plus(url)

    else: url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'            

    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={'Title':name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
        
    #dp.close()
    xbmc.Player().play(url,liz,False)
    quit()  
   
    