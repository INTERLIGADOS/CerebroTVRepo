import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,hashlib,time
import datetime
import httplib2
import base64,time
import kodi
from HTMLParser import HTMLParser
from resources.lib.modules import plugintools
from resources.lib.modules import regex
from resources.lib.modules import checker
from resources.lib.modules import dom_parser
from resources.lib.modules import log_utils
from resources.lib.modules import cache
from resources.lib.modules import cache_dir
from resources.lib.modules import soccerstreams
from resources.lib.modules import resolvable

addon_id            = 'plugin.video.sportie'
AddonTitle          = '[COLOR mediumpurple]SPORTIE[/COLOR]'
fanarts             = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
DATA_FOLDER         = xbmc.translatePath(os.path.join('special://profile/addon_data/' , addon_id))
DB_FOLDER           = xbmc.translatePath(os.path.join('special://profile/' , 'Database'))
SETTINGS_FILE       = xbmc.translatePath(os.path.join(DATA_FOLDER, 'settings.xml'))
TESTINGS_FILE       = xbmc.translatePath(os.path.join(DATA_FOLDER, 'testings.xml'))
REDDIT_FILE         = xbmc.translatePath(os.path.join(DATA_FOLDER, 'reddit.xml'))
baseurl             = base64.decodestring('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3Q4MDRteFV1') 
dp                  = xbmcgui.DialogProgress()
dialog              = xbmcgui.Dialog()
GET_VERSION         = xbmc.translatePath('special://home/addons/' + addon_id + '/addon.xml')
GET_REPO_VERSION    = xbmc.translatePath('special://home/addons/repository.echo/addon.xml')
PLEXUS_PATH         = xbmc.translatePath('special://home/addons/program.plexus')
cachePath           = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath            = os.path.join(xbmc.translatePath('special://home'), 'temp')
F4M_TESTER          = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.f4mTester'))
F4M_PROXY           = xbmc.translatePath(os.path.join('special://home/addons/script.video.F4mProxy'))
SPORTSDEVIL         = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.SportsDevil'))
REPO_INFO           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files/repository.txt'))
REPO_FOLDER         = xbmc.translatePath(os.path.join('special://home/addons/repository.echo'))
FILES_FOLDER        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files'))

def STARTER():

    if not os.path.exists(FILES_FOLDER):
        os.makedirs(FILES_FOLDER)
        
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        
    if not os.path.isfile(REDDIT_FILE):
        f = open(REDDIT_FILE,'w'); f.write('#START OF FILE#'); f.close()

def SOCCERSTREAMS_CHECK():

    try:
        supported=cache.get(open_url_ss,4,base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3JEQXJIMkpI'))
        
        file = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/lib/modules/soccerstreams.py'))

        if len(supported)>1:
            comparefile = file
            r = open(comparefile)
            compfile = r.read()       
            if compfile == supported:pass
            else:
                text_file = open(comparefile, "w")
                text_file.write(supported)
                text_file.close()
                kodi.notify(msg='SoccerStreams Scraper Updated.', duration=7500, sound=True)
    except:
        try:
            supported=cache.get(open_url_ss,4,base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3JEQXJIMkpI'))
            file = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/lib/modules/soccerstreams.py'))
            comparefile = file
            r = open(comparefile)
            compfile = r.read()       
            os.remove(file)
            text_file = open(comparefile, "w")
            text_file.write(supported)
            text_file.close()
            kodi.notify(msg='SoccerStreams Scraper Updated.', duration=7500, sound=True)
        except: pass

def RESOLVABLE_CHECK():

    try:
        supported=cache.get(open_url_ss,4,base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2VyY3cxSHAy'))
        
        file = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/lib/modules/resolvable.py'))

        if len(supported)>1:
            comparefile = file
            r = open(comparefile)
            compfile = r.read()       
            if compfile == supported:pass
            else:
                text_file = open(comparefile, "w")
                text_file.write(supported)
                text_file.close()
                kodi.notify(msg='Resolver Checker Updated.', duration=7500, sound=True)
    except:
        try:
            supported=cache.get(open_url_ss,4,base64.b64decode('aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2VyY3cxSHAy'))
            file = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/lib/modules/resolvable.py'))
            comparefile = file
            r = open(comparefile)
            compfile = r.read()       
            os.remove(file)
            text_file = open(comparefile, "w")
            text_file.write(supported)
            text_file.close()
            kodi.notify(msg='Resolver Checker Updated.', duration=7500, sound=True)
        except: pass

def CHECK_DB_ENABED(id):

    path = DB_FOLDER
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if 'Addons' in d]
        list = [name.replace('Addons','').replace('.db','') for name in files if ('Addons' in name) and (name.endswith('.db'))]
        list = [int(x) for x in list]; list.sort()
        db_file = xbmc.translatePath(os.path.join(DB_FOLDER, ('Addons%s.db' % (str(list[-1])))))

    import sqlite3
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT enabled FROM installed WHERE addonID = '%s'" % (id))
    
    for entry in cursor.fetchone():
        return entry
    
def ENABLE_DB_ADDON(id):

    try:
        path = DB_FOLDER
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if 'Addons' in d]
            list = [name.replace('Addons','').replace('.db','') for name in files if ('Addons' in name) and (name.endswith('.db'))]
            list = [int(x) for x in list]; list.sort()
            db_file = xbmc.translatePath(os.path.join(DB_FOLDER, ('Addons%s.db' % (str(list[-1])))))

        import sqlite3
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        enable = '1'
        q = """ UPDATE installed SET enabled= ? WHERE addonID = ? """
        cursor.execute(q, (str(enable), str(id)))
        conn.commit()

        dialog.ok(AddonTitle, id + ' has been enabled!', 'Thank you for using Sportie.')
        xbmc.executebuiltin("Container.Refresh")
        xbmc.executebuiltin("UpdateAddonRepos")
        xbmc.executebuiltin("UpdateLocalAddons")
    except:
        dialog.ok(AddonTitle, 'We were unable to enable ' + id +'. You can try to enable this manually in your Addons if you wish.')
        quit()
        
def GetMenu():

    addLink(kodi.giveColor(kodi.countGitHubIssues('https://github.com/Colossal1/plugin.video.sportie/issues'),'blue',True) + kodi.giveColor(' | Click To View Issues','white',True),'null',994,'https://imgur.com/kg2XOOc',fanarts,'')

    try:
        checkrtmp = plugintools.get_setting("check_rtmp")
        if checkrtmp == 'true':
            rtmp_check = CHECK_DB_ENABED('inputstream.rtmp')
            if rtmp_check == 0:
                addLink('[COLOR red][B]RTMP Input is Disabled. Click here to Enable.[/B][/COLOR]','inputstream.rtmp',996,'https://imgur.com/7Rllb9y',fanarts,'')   
            adaptive_check = CHECK_DB_ENABED('inputstream.adaptive')
            if adaptive_check == 0:
                addLink('[COLOR red][B]InputStream Adaptive is Disabled. Click here to Enable.[/B][/COLOR]','inputstream.adaptive',996,'https://imgur.com/7Rllb9y',fanarts,'')
    except: pass
        
    if os.path.isfile(TESTINGS_FILE):
        url2 = baseurl
        r = open(TESTINGS_FILE)
        testfile = r.read()
        testfile=testfile.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        match= re.compile('<item>(.+?)</item>').findall(testfile)
    else:
        SOCCERSTREAMS_CHECK()
        RESOLVABLE_CHECK()
        link=cache.get(open_url,4,baseurl)
        url2 = baseurl
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        match= re.compile('<item>(.+?)</item>').findall(link)
        
    for item in match:

        if "<notice>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<notice>(.+?)</notice>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addLink(name,url,995,iconimage,fanart,'')
        
        elif "<247hd>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<247hd>(.+?)</247hd>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,312,iconimage,fanart,'')

        elif "<reddit>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit>(.+?)</reddit>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',320,iconimage,fanart,'')
            
        elif "<reddit_link>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit_link>(.+?)</reddit_link>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,319,iconimage,fanart,'')

        elif "<redditevents>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<redditevents>(.+?)</redditevents>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,317,iconimage,fanart,'')

        elif "<reddit_suggested>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit_suggested>(.+?)</reddit_suggested>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,322,iconimage,fanart,'')

        elif "<goaltogoals>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<goaltogoals>(.+?)</goaltogoals>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,314,iconimage,fanart,'')

        elif "<hesgoal>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',205,iconimage,fanart,'')
            
        elif "<livescores>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',80,iconimage,fanart,'')

        elif "<livetv>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,'url',313,icon,fanarts,'')
            
        elif "<fixtureoverview>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',70,iconimage,fanart,'')

        elif "<predictions>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',40,iconimage,fanart,'')
            
        elif "<oddschecker>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',50,iconimage,fanart,'')
            
        elif "<formguide>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',60,iconimage,fanart,'')

        elif "<mamahd>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<mamahd>(.+?)</mamahd>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,310,iconimage,fanart,'')

        elif "<soccerstreams>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<soccerstreams>(.+?)</soccerstreams>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,307,iconimage,fanart,'')

        elif "<bigsports>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<bigsports>(.+?)</bigsports>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,301,iconimage,fanart,'')

        elif "<cricbox>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<cricbox>(.+?)</cricbox>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,302,iconimage,fanart,'')

        elif "<cricfree>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<cricfree>(.+?)</cricfree>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,303,iconimage,fanart,'')
            
        elif "<sports4u>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<sports4u>(.+?)</sports4u>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,304,iconimage,fanart,'')

        elif "<sports4ulive>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,"url",305,iconimage,fanart,'')

        elif '<fightclubsearch>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<fightclubsearch>(.+?)</fightclubsearch>').findall(item)[0]
            url = 'true|SPLIT|' + url
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            addDir(name,url,222,iconimage,fanarts)
            
        elif '<fightclubterms>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<fightclubterms>(.+?)</fightclubterms>').findall(item)[0]
            url = 'false|SPLIT|' + url + '|SPLIT|' + url2 + '|SPLIT|' + name
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            addDir(name,url,222,iconimage,fanarts)

        elif '<search>display</search>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,baseurl,100,icon,fanarts,'')
            
        elif '<arenavision>display</arenavision>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            if os.path.exists(PLEXUS_PATH): addDir(name,baseurl,95,iconimage,fanarts,'')
            else: addLink('[COLOR darkgray]' + name + ' - INSTALL PLEXUS TO USE.[/COLOR]',baseurl,999,iconimage,fanarts,'')
    
        elif '<vip>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,'none',24,icon,fanarts)

        elif '<divider>null</divider>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addLink(name,baseurl,999,icon,fanarts)

        elif '<m3ulists>display</m3ulists>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,baseurl,11,icon,fanarts)

        elif '<plexus>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            try:
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]   
            except: fanart = fanarts
            if os.path.exists(PLEXUS_PATH): addLink(name,url2+'NOTPLAY',7,icon,fanart)  
            else: addLink('[COLOR darkgray]' + name + ' - INSTALL PLEXUS TO USE.[/COLOR]',baseurl,999,iconimage,fanart,'')
            
        elif '<rutubeplaylist>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            try:
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]   
            except: fanart = fanarts
            addDir(name,url2,90,iconimage,fanart)

        elif '<folder>'in item:
            data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
            for name,url,iconimage,fanart in data:
                addDir(name,url,1,iconimage,fanart)

        elif '<m3u>'in item:
            data=re.compile('<title>(.+?)</title>.+?m3u>(.+?)</m3u>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
            for name,url,iconimage,fanart in data:
                addDir(name,url,10,iconimage,fanart)

        elif '<regex>' in item:
        
            hash = []
            
            regdata = re.compile('(<regex>.+?</regex>)', re.MULTILINE|re.DOTALL).findall(item)
            regdata = ''.join(regdata)
            reglist = re.compile('(<listrepeat>.+?</listrepeat>)', re.MULTILINE|re.DOTALL).findall(regdata)
            regdata = urllib.quote_plus(regdata)

            reghash = hashlib.md5()
            for i in regdata: reghash.update(str(i))
            reghash = str(reghash.hexdigest())
            
            try: name = re.findall('<title>(.+?)</title>', item)[0]
            except: name = '0'
            
            try: url = re.findall('<link>(.+?)</link>', item)[0]
            except: url = '0'
            
            try: image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
            except: image2 = icon

            try: fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
            except: fanart2 = fanarts

            hash.append({'regex': reghash, 'response': regdata})
            url += '|regex=%s' % regdata

            addLink(name,url,30,image2,fanart2)

        elif '<sportsdevil>' in item:
            links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
            if len(links)==1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                try:
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                except: iconimage = icon
                try:
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]            
                except: fanart = fanarts
                url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                try:
                    referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                except: referer = url
                check = referer
                suffix = "/"
                if not check.endswith(suffix):
                    refer = check + "/"
                else:
                    refer = check
                link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+str(name)+'%26url=' + url
                url = link + '%26referer=' +refer
                addLink(name,url,4,iconimage,fanart)   
            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                addLink(name,url2+'NOTPLAY',8,iconimage,fanart)

        else:
            links=re.compile('<link>(.+?)</link>').findall(item)
            if len(links)==1:
                data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                lcount=len(match)
                for name,url,iconimage,fanart in data:
                    addLink(name,url,2,iconimage,fanart)
            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                addLink(name,baseurl,3,iconimage,fanart)

    kodi_name = GET_KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif kodi_name == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')

def GetContent(name,url):

    hash = []
    url2 = url
    link=open_url(url)

    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:

        if "<hesgoal>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',205,iconimage,fanart,'')

        elif "<reddit>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit>(.+?)</reddit>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',320,iconimage,fanart,'')
            
        elif "<reddit_link>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit_link>(.+?)</reddit_link>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,319,iconimage,fanart,'')

        elif "<redditevents>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<redditevents>(.+?)</redditevents>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,317,iconimage,fanart,'')

        elif "<reddit_suggested>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<reddit_suggested>(.+?)</reddit_suggested>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,322,iconimage,fanart,'')
            
        elif "<goaltogoals>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<goaltogoals>(.+?)</goaltogoals>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,314,iconimage,fanart,'')

        elif "<livetv>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,'url',313,icon,fanarts,'')

        elif "<livescores>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',80,iconimage,fanart,'')
            
        elif "<fixtureoverview>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',70,iconimage,fanart,'')

        elif "<predictions>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',40,iconimage,fanart,'')
            
        elif "<oddschecker>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',50,iconimage,fanart,'')
            
        elif "<formguide>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,'url',60,iconimage,fanart,'')

        elif "<mamahd>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<mamahd>(.+?)</mamahd>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,310,iconimage,fanart,'')

        elif "<soccerstreams>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<soccerstreams>(.+?)</soccerstreams>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,307,iconimage,fanart,'')

        elif "<247hd>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<247hd>(.+?)</247hd>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,312,iconimage,fanart,'')

        elif "<bigsports>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<bigsports>(.+?)</bigsports>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,301,iconimage,fanart,'')

        elif "<cricbox>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<cricbox>(.+?)</cricbox>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,302,iconimage,fanart,'')

        elif "<cricfree>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<cricfree>(.+?)</cricfree>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,303,iconimage,fanart,'')
            
        elif "<sports4u>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<sports4u>(.+?)</sports4u>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,url,304,iconimage,fanart,'')

        elif "<sports4ulive>" in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
            addDir(name,"url",305,iconimage,fanart,'')

        elif '<folder>'in item:
            data=re.compile('<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
            for name,url,iconimage,fanart in data:
                addDir(name,url,1,iconimage,fanarts)

        elif '<m3u>'in item:
            data=re.compile('<title>(.+?)</title>.+?m3u>(.+?)</m3u>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
            for name,url,iconimage,fanart in data:
                addDir(name,url,10,iconimage,fanarts)

        elif '<rutube>'in item:
            data=re.compile('<title>(.+?)</title>.+?rutube>(.+?)</rutube>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
            for name,url,iconimage,fanart in data:
                url2 = 'https://rutube.ru/play/embed/'+url+'?wmode=opaque&fakeFullscreen=1'
                addDir(name,url2,2,iconimage,fanarts)

        elif '<m3ulists>display</m3ulists>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addDir(name,baseurl,11,icon,fanarts)

        elif '<fightclubsearch>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<fightclubsearch>(.+?)</fightclubsearch>').findall(item)[0]
            url = 'true|SPLIT|' + url
            addDir(name,url,222,icon,fanarts)
            
        elif '<fightclubterms>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            url=re.compile('<fightclubterms>(.+?)</fightclubterms>').findall(item)[0]
            url = 'false|SPLIT|' + url + '|SPLIT|' + url2 + '|SPLIT|' + name
            addDir(name,url,222,icon,fanarts)

        elif '<arenavision>display</arenavision>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            if os.path.exists(PLEXUS_PATH): addDir(name,baseurl,95,icon,fanarts,'')
            else: addLink('[COLOR darkgray]' + name + ' - INSTALL PLEXUS TO USE.[/COLOR]',baseurl,999,icon,fanarts,'')

        elif '<divider>null</divider>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            addLink(name,baseurl,999,icon,fanarts)

        elif '<plexus>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            try:
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]   
            except: fanart = fanarts
            if os.path.exists(PLEXUS_PATH): addLink(name,url2+'NOTPLAY',7,icon,fanarts) 
            else: addLink('[COLOR darkgray]' + name + ' - INSTALL PLEXUS TO USE.[/COLOR]',baseurl,999,iconimage,fanarts,'')
                
        elif '<rutubeplaylist>' in item:
            name=re.compile('<title>(.+?)</title>').findall(item)[0]
            iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            try:
                fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]   
            except: fanart = fanarts
            addDir(name,url2,90,iconimage,fanarts)

        elif '<search>' in item:
            links=re.compile('<search>(.+?)</search>').findall(item)
            if len(links)==1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url=re.compile('<search>(.+?)</search>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = name + "!" + url + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,20,iconimage,fanarts)

            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = url2 + "!" + name + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,22,iconimage,fanarts)

        elif '<regex>' in item:
        
            hash = []
            
            regdata = re.compile('(<regex>.+?</regex>)', re.MULTILINE|re.DOTALL).findall(item)
            regdata = ''.join(regdata)
            reglist = re.compile('(<listrepeat>.+?</listrepeat>)', re.MULTILINE|re.DOTALL).findall(regdata)
            regdata = urllib.quote_plus(regdata)

            reghash = hashlib.md5()
            for i in regdata: reghash.update(str(i))
            reghash = str(reghash.hexdigest())
            
            try: name = re.findall('<title>(.+?)</title>', item)[0]
            except: name = '0'
            
            try: url = re.findall('<link>(.+?)</link>', item)[0]
            except: url = '0'
            
            try: image2 = re.findall('<thumbnail>(.+?)</thumbnail>', item)[0]
            except: image2 = icon

            try: fanart2 = re.findall('<fanart>(.+?)</fanart>', item)[0]
            except: fanart2 = fanarts

            hash.append({'regex': reghash, 'response': regdata})
            url += '|regex=%s' % regdata

            addLink(name,url,30,image2,fanart2)

        elif '<sportsdevil>' in item:
            links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)
            if len(links)==1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                try:
                    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]            
                except: iconimage = icon
                try:
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]            
                except: fanart = fanarts
                url=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(item)[0]
                try:
                    referer=re.compile('<referer>(.+?)</referer>').findall(item)[0]
                except: referer = url
                check = referer
                suffix = "/"
                if not check.endswith(suffix):
                    refer = check + "/"
                else:
                    refer = check
                link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+str(name)+'%26url=' + url
                url = link + '%26referer=' +refer
                addLink(name,url,4,iconimage,fanart)   
            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                addLink(name,url2+'NOTPLAY',8,iconimage,fanart)

        else:
            links=re.compile('<link>(.+?)</link>').findall(item)
            if len(links)==1:
                data=re.compile('<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>').findall(item)
                lcount=len(match)
                for name,url,iconimage,fanart in data:
                    addLink(name,url,2,iconimage,fanart)
            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                try:
                    fanart=re.compile('<fanart>(.+?)</fanart>').findall(item)[0]
                except: fanart = fanarts
                addLink(name,url2,3,iconimage,fanart)  

    kodi_name = GET_KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif kodi_name == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')

def REDDIT_MAIN():

    xbmc.executebuiltin("ActivateWindow(busydialog)")

    addDir('Click for Sportie Recommended Reddits','url',322,icon,fanarts)
    addLink('Add A Reddit/Subreddit','url',321,icon,fanarts)
    addLink('-----------------------------------','url',999,icon,fanarts)
    addLink('User Added Reddits','url',999,iconimage,fanart)

    if os.path.exists(REDDIT_FILE):
        f = open(REDDIT_FILE,mode='r'); msg = f.read(); f.close()
        msg = msg.replace('\n','')
        if '<item>' in msg:
            match = re.compile('<item>(.+?)</item>').findall(msg)
            for item in match:
                name=re.compile('<name>(.+?)</name>').findall(item)[0]
                url=re.compile('<url>(.+?)</url>').findall(item)[0]
                cm=[]
                cm.append(('Remove from list','XBMC.RunPlugin(%s?mode=323&name=%s&url=%s)'% (sys.argv[0],name,url)))
                addDir('[COLOR blue]' + name.encode('utf-8') + '[/COLOR]',url.encode('utf-8'),319,iconimage,fanart,'',cm)
        else: addLink('No user added Reddits detected.','url',999,iconimage,fanart)
    xbmc.executebuiltin("Dialog.Close(busydialog)")

def REDDIT_ADD():

    xbmc.executebuiltin("ActivateWindow(busydialog)")
    if not os.path.isfile(REDDIT_FILE):
        f = open(REDDIT_FILE,'w'); f.write('#START OF FILE#'); f.close()

    string =''
    keyboard = xbmc.Keyboard(string, 'Enter Reddit URL/Name')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string)>1:
            if not 'http' in string.lower(): string = 'https://www.reddit.com/r/' + string
            r = open_url_m3u(string)
            if '<p id="noresults" class="error">' in r:
                dialog.ok(AddonTitle, 'An invalid URL has been entered.')
                xbmc.executebuiltin("Dialog.Close(busydialog)")
                quit()
            url = string
        else: 
            xbmc.executebuiltin("Dialog.Close(busydialog)")
            quit()
    else: 
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        quit()
    
    try:
        name = re.compile('<h1 class="hover redditname">.+?>(.+?)<\/a>').findall(r)[0]
        a=open(REDDIT_FILE).read()
        b=a.replace('#START OF FILE#', '#START OF FILE#\n<item>\n<name>'+str(name)+'</name>\n<url>'+str(url)+'</url>\n</item>\n')
        f= open(REDDIT_FILE, mode='w')
        f.write(str(b))
        f.close()
    except:
        dialog.ok(AddonTitle, 'Sorry, we were unable to add this Reddit.')
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        quit()
    dialog.ok(AddonTitle, name + ' has been added!')
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    xbmc.executebuiltin("Container.Refresh")

def REDDIT_SUGGESTED():

    r = open_url('https://pastebin.com/raw/4b2DegdY')
    
    r = re.compile('<link>(.+?)</link>').findall(r)

    for u in r:

        r = open_url_m3u(u)
            
        try:
            name = re.compile('<h1 class="hover redditname">.+?>(.+?)<\/a>').findall(r)[0]
            addDir(name.encode('utf-8'),u,319,icon,fanarts)
        except: pass
        
def REDDIT_GET(url):

    r = open_url_m3u(url)
    
    if not 'comments' in url:
    
        namelist = []; urllist = []; scorelist = []; commentlist = []; combinedlist = []
        try:
            sitename = re.compile('<h1 class="hover redditname">.+?>(.+?)<\/a>').findall(r)[0]
            addLink('[COLOR blue][B]Welcome to the ' + sitename.title() + ' Reddit![/B][/COLOR]','url',999,icon,fanart)
        except: pass
        
        r = dom_parser.parse_dom(r, 'div', {'class': re.compile('\sthing\sid')})

        if r:
            for i in r:
                title = re.compile('<a class="title may-blank.+?rel=".+?>(.+?)<').findall(i.content)[0]
                url = re.compile('href="([^"]+)').findall(i.content)
                url = [u for u in url if ('comments' in u) and ('reddit' in u)]
                try: score = re.compile('<div class="score unvoted" title=".+?">([0-9]+)</div>').findall(i.content)[0]
                except: score = '0'
                try: comments = re.compile('data-event-action="comments".+?>([0-9]+)\scomments<\/a>').findall(i.content)[0]
                except: comments = '0'

                if 'comments' in url[0]:
                    url = url[0]
                    if not 'reddit.com' in url: url = 'https://www.reddit.com' + url
                    namelist.append(title.encode('utf-8'))
                    urllist.append(url.encode('utf-8'))
                    scorelist.append(score.encode('utf-8'))
                    commentlist.append(comments.encode('utf-8'))
                    combinedlist = list(zip(scorelist,namelist,urllist,commentlist))

            #tup = sorted(combinedlist, key=lambda x: int(x[0]),reverse=True)
            for score,title,url,comments in combinedlist:
                title = title.replace('&amp;','&')
                addDir('[COLOR blue][B]' + score + '[/B][/COLOR] - [COLOR white]' + title + '[/COLOR] - ' + comments + ' Comments',url,319,icon,fanarts)
        else: addLink('No Sub Reddits Found','url',999,icon,fanart)

    else:
        
        checks = ['acestream','href']
        black = ['ads']
        s = 1

        r = dom_parser.parse_dom(r, 'div', {'class': re.compile('md')})
        ace = re.compile('([0-9a-z]+)').findall(str(r))
        e = [i for i in ace if len(i) == 40]
        u = [i[1] for i in r[1:] if ('<p>' in i[1]) and any(f for f in checks if f in i[1]) and not any(f for f in black if f in i[1])]
        r = re.findall('acestream:\/\/([0-9 a-z]+)[\s|<]', str(u)) + re.findall('<a href=\"http(.+?)\"', str(u))
        a = []
        a.extend(e)
        a.extend(r)

        combined  = []

        if a:
            countlist = []
            namelist  = []
            urllist   = []
            for i in a:
                if not i.endswith(('.jpg','.jpeg','.png','.gif')):
                    i = i.encode('utf-8')
                    if '://' in i: i = 'http' + i
                    if not 'reddit' in i:
                        if not 'http' in i:
                            if os.path.exists(PLEXUS_PATH): 
                                name = '[COLOR blue][B]Link ' + str(s) + '[/B][/COLOR] - Acestream: ' + i
                                namelist.append(name)
                                if not i in urllist: urllist.append('acestream://'+i)
                                countlist.append('0')
                                combined = list(zip(countlist,namelist,urllist))
                                s += 1
                        else: 
                            name = '[COLOR blue][B]Link ' + str(s) + '[/B][/COLOR] - ' + i
                            namelist.append(name)
                            if not i in urllist: urllist.append(i)
                            countlist.append('1')
                            combined = list(zip(countlist,namelist,urllist))
                            s += 1
            if s == 1: addLink('No Links Found','url',999,icon,fanart)
        else: addLink('No Links Found','url',999,icon,fanart)

        if combined:
            ace_got  = 0
            http_got = 0
            tup = sorted(combined, key=lambda x: int(x[0]))
            for count,name,url in tup:
                if count == '0': 
                    if ace_got == 0:
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        addLink('[COLOR blue][B]Acestream Links Below[/B][/COLOR]','url',999,icon,fanart)
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        ace_got = 1
                    addLink(name.encode('utf-8'),url,318,icon,fanart)
                else:
                    if http_got == 0:
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        addLink('[COLOR blue][B]HTTP Links Below[/B][/COLOR]','url',999,icon,fanart)
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        http_got = 1
                    addLink(name.encode('utf-8'),url,318,icon,fanart)
        
def REDDIT_REMOVE(name,url):

    try:
        name = name.replace('[COLOR blue]','').replace('[/COLOR]','')
        a=open(REDDIT_FILE).read()
        b=a.replace('<item>\n<name>'+str(name)+'</name>\n<url>'+str(url)+'</url>\n</item>','')
        f=open(REDDIT_FILE, mode='w')
        f.write(str(b))
        xbmc.executebuiltin("Container.Refresh")
    except:
        dialog.ok(AddonTitle,'There was an error removing the entry from the list.')
        quit()
        
def EVENT_REDDIT():

    r = open_url('https://pastebin.com/raw/6w0TPFBx')
    r = re.compile('<link>(.+?)</link>').findall(r)
    
    checks = ['acestream','href']
    black = ['ads']
    s = 1
    for u in r:
        r = open_url(u)
        checks = ['acestream','href']
        black = ['ads']
        s = 1

        r = dom_parser.parse_dom(r, 'div', {'class': re.compile('md')})
        ace = re.compile('([0-9a-z]+)').findall(str(r))
        e = [i for i in ace if len(i) == 40]
        u = [i[1] for i in r[1:] if ('<p>' in i[1]) and any(f for f in checks if f in i[1]) and not any(f for f in black if f in i[1])]
        r = re.findall('acestream:\/\/([0-9 a-z]+)[\s|<]', str(u)) + re.findall('<a href=\"http(.+?)\"', str(u))
        a = []
        a.extend(e)
        a.extend(r)

        combined  = []

        if a:
            countlist = []
            namelist  = []
            urllist   = []
            for i in a:
                if not i.endswith(('.jpg','.jpeg','.png','.gif')):
                    i = i.encode('utf-8')
                    if '://' in i: i = 'http' + i
                    if not 'reddit' in i:
                        if not 'http' in i:
                            if os.path.exists(PLEXUS_PATH): 
                                name = '[COLOR blue][B]Link ' + str(s) + '[/B][/COLOR] - Acestream: ' + i
                                namelist.append(name)
                                urllist.append('acestream://'+i)
                                countlist.append('0')
                                combined = list(zip(countlist,namelist,urllist))
                                s += 1
                        else: 
                            name = '[COLOR blue][B]Link ' + str(s) + '[/B][/COLOR] - ' + i
                            namelist.append(name)
                            urllist.append(i)
                            countlist.append('1')
                            combined = list(zip(countlist,namelist,urllist))
                            s += 1
            if s == 1: addLink('No Links Found','url',999,icon,fanart)
        else: addLink('No Links Found','url',999,icon,fanart)

        if combined:
            ace_got  = 0
            http_got = 0
            tup = sorted(combined, key=lambda x: int(x[0]),reverse=False)
            for count,name,url in tup:
                if count == '0': 
                    if ace_got == 0:
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        addLink('[COLOR blue][B]Acestream Links Below[/B][/COLOR]','url',999,icon,fanart)
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        ace_got = 1
                    addLink(name.encode('utf-8'),url,318,icon,fanart)
                else:
                    if http_got == 0:
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        addLink('[COLOR blue][B]HTTP Links Below[/B][/COLOR]','url',999,icon,fanart)
                        addLink('---------------------------------------------------------','url',999,icon,fanart)
                        http_got = 1
                    addLink(name.encode('utf-8'),url,318,icon,fanart)

def REDDIT_PLAYER(name,url,iconimage):

    dp.create(AddonTitle,"[COLOR blue]Opening link...[/COLOR]",'[COLOR yellow]Please wait...[/COLOR]','')   
    dp.update(0)
    import urlresolver
    import liveresolver
    if 'acestream' in url: url = "plugin://program.plexus/?url="+url+"&mode=1&name=acestream+"+name
    elif '.m3u8' in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage  
    elif '.ts'in url:
        url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+iconimage  
    elif urlresolver.HostedMediaFile(url).valid_url(): 
        url = urlresolver.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
        liz.setPath(url)
        dp.close()
        xbmc.Player ().play(url, liz, False)
    elif liveresolver.isValid(url)==True:
        url=liveresolver.resolve(url)
        liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
        liz.setPath(url)
        dp.close()
        xbmc.Player ().play(url, liz, False)
    else:
        url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+str(name)+'%26url=' + url + '%26referer=none'    
    liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
    liz.setPath(url)
    dp.close()
    xbmc.Player ().play(url, liz, False)

def LIVE_TV():

    namelist = []; urllist = []; combinedlist = []
    
    urls = ['aHR0cDovL3d3dy5pcHR2c2F0LmNvbS9wL2lwdHZzcG9ydC5odG1s']
    
    for url in urls:
        response = open_url_m3u(base64.b64decode(url))
        response = response.replace('#AAASTREAM:','#A:').replace('#EXTINF:','#A:').replace('</h4>','').replace('<h4>','')
        matches=re.compile('#A:-?[0-9]*(.*?),(.*?)(?:<br\s\/>)?\n(.*?)(?:<|\n)',re.I+re.M+re.U+re.S).findall(response)

        for params, display_name, url2 in matches:
            display_name = display_name.lstrip()
            namelist.append(display_name.title()); urllist.append(url2); combinedlist = list(zip(namelist,urllist))
            
    for name,url in sorted(combinedlist): addLink(name,url,2,icon,fanart)

def SCRAPE_GOALTOGOALS():

    r = open_url_m3u('https://goaltogoals.com')

    r = re.compile('<li id="menu-item.+? href="(.+?)">(.+?)<\/a><\/li>').findall(r)
    for i in r[1:][:-7]:
        addDir(i[1],i[0],315,icon,fanarts,'')

def SCRAPE_GOALTOGOALS_SECTIONS(url):

    u = open_url_m3u(url)

    if 'No posts to display' in u:
        addLink('No Games to Display','url',999,icon,fanarts,'')
    else:
        try: r = re.compile('<head>(.+?)<div class="page-nav td-pb-padding-side">',re.DOTALL).findall(u)[0]
        except: r = re.compile('<head>(.+?)</html>',re.DOTALL).findall(u)[0]
        
        r = re.compile('<div class="td-module-thumb"><a href="(.+?)" rel=.+?title="(.+?)"><img width="[0-9]+" height="[0-9]+" class="entry-thumb" src="(.+?)"',re.DOTALL).findall(r)
        
        if r:
            for i in r:
                try: name = i[1].split('&#')[0].encode('utf-8')
                except: name = i[1]
                addLink(name,i[0],316,i[2],fanarts,'')

        try: 
            r = re.compile('<link rel="next" href="(.+?)" />').findall(u)[0]
            addDir('Next Page -->',r,315,icon,fanarts,'')
        except: pass

def GET_GOALTOGOALS_LINKS(name,url,iconimage):

    xbmc.executebuiltin("ActivateWindow(busydialog)")

    streamurl=[]
    streamname=[]

    u=open_url_m3u(url)

    r = re.compile('<h4 class="vc_tta-panel-title">(.+?)</div>\n\t</div>',re.DOTALL).findall(u)
    if r:
        for i in r:
            title = re.compile('<span class="vc_tta-title-text">(.+?)</span>').findall(i)[0]
            
            #try:
            if 'data-config=' in i: url = re.compile('data-config="(.+?)"').findall(i)[0]
            else: url = re.compile('src="(.+?)"').findall(i)[0]
            if not 'http' in url: url = 'http:' + url
            streamurl.append(url)
            streamname.append(title)
            #except: pass
            
    if len(streamname) < 1:
        dialog.ok(AddonTitle, 'Nothing found for this game. Please try again later.')
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        quit()
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        r = open_url_m3u(streamurl[select])
        if '.json' in streamurl[select]:
            r = re.compile('f4m":"(.+?)"').findall(r)[0]
            r = open_url_m3u(r)
            b = re.compile('<baseURL>(.+?)</baseURL>').findall(r)[0]
            v = re.compile('<media url="(.+?)"').findall(r)[0]
            url = b + '/' + v
        elif 'weshare.me' in streamurl[select]:
            url = re.compile('<source src="(.+?)"').findall(r)[0]
        elif 'streamable.com' in streamurl[select]:
            r = re.compile('url": "(.+?)"',re.DOTALL).findall(r)
            e = [e for e in r if '.mp4' in e]
            if e: 
                if not 'http' in e[0]: url = 'http:' + e[0]
                else: url = e[0]
        else: url = streamurl[select]
        
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    if '.mp4' in url:
        liz = xbmcgui.ListItem(name,iconImage=iconimage, thumbnailImage=iconimage)
        liz.setPath(url)
        xbmc.Player ().play(url, liz, False)    
    else: PLAYLINK(name,url,iconimage)

def SCRAPE_247HD():

    link = cache.get(open_url,1,'http://www.genti.stream/')

    link = link.replace('\n', '').replace('\r','')
    link = link.replace('<tr>','</tr><tr>').replace('</tbody>','</tr></tbody>')
    match = re.compile ('<tr>(.+?)</tr>').findall(link)
    for items in match:
        if "href" in items:
            time = re.compile('<td>(.+?)</td>',re.DOTALL).findall(items)[0].strip()
            comp = re.compile('<td><strong>(.+?)</strong></td>',re.DOTALL).findall(items)[0].strip()
            teams = re.compile('<td>(.+?)</td>',re.DOTALL).findall(items)[2].strip()
            links = re.compile ('<td><a href="(.+?)">(.+?)<a/></td>').findall(items)
            for url,quality in links:
                addLink("[COLOR blue]" + comp + " | [/COLOR][COLOR white][B]" + teams.title() + " [/B][/COLOR][COLOR blue]| " + time + "[/COLOR]",url,4,icon,fanarts,'')

def SCRAPE_SPORTSMAMA_HOME():

    link = cache.get(open_url,1,'https://mamahd.tv/')

    addDir("[COLOR white][B]Live Channels[/B][/COLOR]",url,311,icon,fanarts,'')

    c = link.replace('\n', '').replace('\r','')
    r = dom_parser.parse_dom(c, 'tr', {'data-toggle': 'collapse'})
    r = [(dom_parser.parse_dom(i, 'span', {'class': 'date'}), \
          dom_parser.parse_dom(i, 'div', {'id': re.compile('time\d+')}), \
          dom_parser.parse_dom(i, 'td', {'class': 'home-league'}), \
          dom_parser.parse_dom(i, 'td', {'class': 'home-team'}), \
          dom_parser.parse_dom(i, 'td', {'class': 'home-away'}), \
          dom_parser.parse_dom(i, 'a', req='href')) \
          for i in r if i]
    r = [(i[0][0].content, re.sub('<.+?</.+?>', '', i[1][0].content).strip(), \
          i[2][0].content, re.sub('<.+?>', '', i[3][0].content).strip(), \
          re.sub('<.+?>', '', i[4][0].content).strip(), i[5][-1].attrs['href']) for i in r if i[4]]
      
    if r:
        for i in r:
            name = i[3] + ' vs ' + i[4]           
            addLink("[COLOR blue]" + i[0]  + "-" + i[1]  + "[/COLOR]- [COLOR white]" + name.encode('ascii', 'ignore') + "[/COLOR] - " + i[2],i[5],309,icon,fanarts,'')
    
def SCRAPE_SPORTSMAMA_CHANNELS():

    link = cache.get(open_url,1,'https://mamahd.tv/')

    c = link.replace('\n', '').replace('\r','')
    r = dom_parser.parse_dom(c, 'ul', {'class': 'dropdown-menu'})
    r = dom_parser.parse_dom(r[1].content, 'a', req=['href','title'])
    r = [(i.attrs['title'], i.attrs['href']) for i in r if i]
    if r:
        for i in r:
            addLink(i[0].title(),i[1],309,icon,fanarts,'')

def PLAY_SPORTSMAMA(name,url,iconimage):

    try:
        link = open_url(url)
        url = re.compile('href="([^"]+)">Watch').findall(link)[0]
        url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + url + '%26referer=no%26icon%3d' + icon
        PLAYSD(name,url,iconimage)
    except:
        dialog.ok(AddonTitle, "Sorry, we could not find any live links at the moment. Please try again later.")
        quit()
            
def SCRAPE_BIGSPORTS(url):

    addDir("[COLOR white][B]Live Channels[/B][/COLOR]",url,299,icon,fanarts,'')
    
    try:
        link = cache.get(open_url,1,'http://livetv.sc/')
        links = re.compile('Schedule -->(.+?)end grid',re.DOTALL).findall(link)[0]
        livegame = re.compile('class="menu-img.+?<td>[^\d]+([\d\/]+).+?time">[^\d]+([\d:]+).+?<td>.+?<td>[^\w]+([^<]+).+?href="([^"]+)">[^\w]+([^<]+)',re.DOTALL).findall(links)
        for date,time,comp,url,teams in livegame:
            comp = comp.strip()
            teams = teams.strip()
            addLink("[COLOR blue]%s | [/COLOR][COLOR white][B]%s [/B][/COLOR][COLOR blue]| %s - %s GMT +1[/COLOR]"%(comp,teams,date,time),url,300,icon,fanarts,'')
    except:
        dialog.ok(AddonTitle, "Sorry, we could not find any live links at the moment. Please try again later.")
        quit()
        
def SCRAPE_BIGSPORTS_CHANNELS(url):

    link = cache.get(open_url,1,'http://livetv.sc/')
    links = re.compile('sports-channels-inner(.+?)end grid',re.DOTALL).findall(link)[0]
    channels = re.compile('href="([^"]+)"\stitle="(?!Channels)([^"]+)"').findall(links)
    for url,name in channels:
        addLink(name,url,300,icon,fanarts,'')


def SCRAPE_BIGSPORTS_GET_LINKS(name,url,iconimage):

    try:
        link = open_url(url)
        url = re.compile('<iframe.+?src="([^"]+)"').findall(link)[0]
        link = open_url(url)
        link = re.compile('<iframe.+?src="([^"]+)"').findall(link)[0]
        url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + link + '%26referer=no%26icon%3d' + icon
        PLAYSD(name,url,iconimage)
    except:
        dialog.ok(AddonTitle, "Sorry, we could not find any live links at the moment. Please try again later.")
        quit()

def SCRAPE_CRICBOX(url):

    addDir("[COLOR white][B]Live Channels[/B][/COLOR]",url,298,icon,fanarts,'')
    try:
        base = 'http://cricbox.net/'
        link = cache.get(open_url,1,base)
        links=re.compile('<td><i\s.+?href="([^"]+)">.+?>([^<]+).+?px">([^&<]+).+?>([^<]+).+?dt">([\d:]+)',re.DOTALL).findall(link)
        for url,comp,day,starting,ending in links:
            url = base + url + '/'
            addLink("[COLOR blue]%s | [/COLOR][COLOR white]Starts %s %s GMT, ends %s[/COLOR]"%(comp,day,starting,ending),url,306,icon,fanarts,'')
    except:
        dialog.ok(AddonTitle, "Sorry, we could not find any live links at the moment. Please try again later.")
        quit()

def SCRAPE_CRICBOX_CHANNELS(url):

    link = cache.get(open_url,1,'http://cricbox.net/')
    channels = re.compile('class="has-sub".+?href="([^"]+).+?(?:icon|icon2)\s([^"]+)').findall(link)
    for url,name in channels:
        url += '/'
        addLink(name,url,306,icon,fanarts,'')
        
def PLAY_CRICBOX(name,url,iconimage):

    try:
        link = open_url(url)
        url = re.compile('<iframe.+?src="([^"]+)"').findall(link)[0]
        link = open_url(url)
        if 'cricbox.co' in link:
            url = re.compile('<a\shref="([^"]+)"').findall(link)[0]
            link = open_url(url)
            url = re.compile('<iframe.+?src="([^"]+)"').findall(link)[0]
        url = 'plugin://plugin.video.SportsDevil/?mode=1&item=catcher%3dstreams%26url=' + url + '%26referer=no%26icon%3d' + icon
        PLAYSD(name,url,iconimage)
    except:
        dialog.ok(AddonTitle, "Sorry, we could not find any live links at the moment. Please try again later.")
        quit()
        
def SCRAPE_ARENA_VISION():

    result = open_url('http://arenavision.in/iguide')
    match = re.compile('<tr><td class="auto-style3"(.+?)</tr>',re.DOTALL).findall(result)

    for item in match:
        try:
            pars = re.compile('style="width:.+?">(.+?)</td',re.DOTALL).findall(item)
            date=pars[0]
            time=pars[1]
            sport=pars[2].title()
            event=pars[3].title()
            game=pars[4].replace('<br/>',' ').title().replace('-','[COLOR yellow] vs [/COLOR]')
            channel=pars[5]
            url = event + '|SPLIT|' + channel
            addLink('[COLOR white][B]' + sport + ' |[/COLOR][COLOR yellow] ' + event + '[/COLOR][COLOR blue][B] | ' + game + '[/B][/COLOR][COLOR white] | ' + date + ' [COLOR orangered][B]' + time + '[/B][/COLOR]',url,97,icon,fanarts)
        except: pass
    kodi_name = GET_KODI_VERSION()

    if kodi_name == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif kodi_name == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')

def SCRAPE_ARENA_VISION_GET_CHANNELS(name,url,iconimage):
    
    name,url = url.split('|SPLIT|')
    links=[]
    multilink = False
    if '-' in url or '<br/>' in url:
        multilink = True

    if multilink:
        lines = url.split('<br/>')
        for line in lines:
            chn,lang = line.split(' ')
            if '-' in chn:
                chna,chnb = chn.split('-')
                links.append((chna,lang))
                links.append((chnb,lang))
            else:
                links.append((chn,lang))
        choices = []
        lno = 1
        for link in links:
            choices.append('[COLOR white]Link %s - %s Channel %s[/COLOR]'%(lno,link[1],link[0]))
            lno += 1
        
        choice = dialog.select("[COLOR red]Please select an stream[/COLOR]", choices)

        if choice >= 0:
            chn = links[choice][0]
            if len(chn)<2: chn = '0' + chn
            url = 'http://arenavision.in/' + chn
        else: quit()

    else:
        chn,lang = url.split(' ')
        if len(chn)<2: chn = '0' + chn
        url = 'http://arenavision.in/' + chn
    
    SCRAPE_ARENA_VISION_GET_LINK(name,url,iconimage)
    
def SCRAPE_ARENA_VISION_GET_LINK(name,url,iconimage):

    try:
        result = open_url(url)
        match = re.compile('this.loadPlayer(.+?),',re.DOTALL).findall(result)[0]
        url = match.replace('(','').replace(')','').replace('"','').replace(' ','')

        url2 = 'plugin://program.plexus/?url=acestream://' + str(url) + '&mode=1&name=acestream+' + str(name)

        PLAYLINK(name,url2,iconimage)
    except: quit()

def SCRAPE_HESGOAL():

    url = 'http://www.hesgoal.com/league/11/Football_News'
    today_raw = datetime.date.today()
    today_formated = datetime.datetime.strftime(today_raw,'%A %d %B %Y') 
    
    addLink('[COLOR mediumpurple][B]EVENTS FOR ' + str(today_formated).upper() + '[/B][/COLOR]',url,999,icon,fanarts,"")
    addLink('##############################################',url,999,icon,fanarts,"")

    result = open_url(url)
    match = re.compile('<div class="file browse_file">(.+?)<p class="played">',re.DOTALL).findall(result)
    fail = 0
    i = 0
    for item in match:
        try:
            title=re.compile('title="(.+?)"').findall(item)[0]    
            try:
                league=re.compile('<p>(.+?)</p>').findall(item)[0]    
            except: league = "Unknown"
            url=re.compile('<a href="(.+?)">').findall(item)[0] 
            iconimage=re.compile('<img src="(.+?)"').findall(item)[0]  
        except: fail = 1
        
        if fail == 0:
            if 'vs' in title:
                name = '[COLOR yellow][B]'+ title + ' - ' + '[/B][/COLOR][COLOR aqua]' + league + '[/COLOR]'
                i = i + 1
                addLink(name,url,206,iconimage,fanarts,'')
        fail = 0

    if i == 0:
        dialog.ok(AddonTitle,"[COLOR yellow]We could not find any live games at this time.[/COLOR]","[COLOR yellow]Please try again later.[/COLOR]")
        quit()

    Set_View()

def SCRAPE_HESGOAL_FIND_LINK(name,url,iconimage):

    result = open_url(url)
    new_url = re.compile('<iframe.+?src="(.+?)"').findall(result)[0]
    
    if not "http" in new_url:
        new_url = new_url.replace("//","")
        url = "http://" + new_url
    else:
        url = new_url
    
    ref_url = url

    get_link_result = open_url(url)
    try:
        new_url = re.compile("atob(.+?),").findall(get_link_result)[0]
        new_url = new_url.replace("('","").replace("')","")
        url = base64.b64decode(new_url)
    except: url = re.compile("source: '(.+?)'").findall(get_link_result)[0]
    url = url + '|User-Agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36&Referer=' + ref_url + '&Host=91.121.222.160:1935&X-Requested-With=ShockwaveFlash/24.0.0.186'
    PLAYLINK(name,url,iconimage)

def SCRAPE_UFC_GETLINK(url):

    result = open_url(url)
    match = re.compile('<div class="col-lg-3 col-md-4 col-sm-6 col-xs1-8 col-xs-12">(.+?)</div> </div>',re.DOTALL).findall(result)

def SCRAPE_RUTUBE_PLAYLISTS(name,url,iconimage):

    playlistname=[]
    playlisturl=[]
    combinedlists=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<rutubeplaylist>(.+?)</rutubeplaylist>').findall(urls)

    for sturl in links:
        sturl2=sturl
        if '(' in sturl:
            sturl=sturl.split('(')[0]
            caption=str(sturl2.split('(')[1].replace(')',''))
            playlistname.append(caption)
            playlisturl.append(sturl)
            combinedlists = list(zip(playlistname,playlisturl))

    tup = sorted(combinedlists)
   
    for marker,url in tup:
        result = open_url(url)
        match = re.compile('<article id="(.+?)</article>',re.DOTALL).findall(result)
        for item in match:
            title=re.compile('title="(.+?)"').findall(item)[0]    
            url=re.compile('<a class="preview-link" href="(.+?)"').findall(item)[0]  
            iconimage=re.compile('https://pic.rutube.ru(.+?)size').findall(item)[0]  
            iconimage = "https://pic.rutube.ru" + iconimage + "size=l"
            if marker.lower() == "all":
                title = title.replace('.',' ')
                addLink(title,url,2,iconimage,iconimage,'')
            elif marker.lower() in title.lower():
                title = title.replace('.',' ')
                addLink(title,url,2,iconimage,iconimage,'')

    try:
        match = re.compile('<a class="paginator-item active(.+?)</html>').findall(result)
        string = str(match)
        np=re.compile('href="(.+?)"').findall(string)[1]
        url = np + "|SPLIT|" + marker
        addDir("[COLOR mediumpurple][B]Next Page -->[/B][/COLOR]",url,91,icon,fanarts,'')
    except: pass

def SCRAPE_RUTUBE_PLAYLISTS_NP(name,url,iconimage):

    url,marker = url.split("|SPLIT|")

    result = open_url(url)
    match = re.compile('<article id="(.+?)</article>',re.DOTALL).findall(result)
    for item in match:
        title=re.compile('title="(.+?)"').findall(item)[0]    
        url=re.compile('<a class="preview-link" href="(.+?)"').findall(item)[0]  
        iconimage=re.compile('https://pic.rutube.ru(.+?)size').findall(item)[0]  
        iconimage = "https://pic.rutube.ru" + iconimage + "size=l"
        if marker.lower() == "all":
            title = title.replace('.',' ')
            addLink(title,url,2,iconimage,iconimage,'')
        elif marker.lower() in title.lower():
            title = title.replace('.',' ')
            addLink(title,url,2,iconimage,iconimage,'')

    try:
        match = re.compile('<a class="paginator-item active(.+?)</html>').findall(result)
        string = str(match)
        np=re.compile('href="(.+?)"').findall(string)[1]
        url = np + "|SPLIT|" + marker
        addDir("[COLOR mediumpurple][B]Next Page -->[/B][/COLOR]",url,91,icon,fanarts,'')
    except: pass

def GET_REGEX(name,url,iconimage):

    r, x = re.findall('(.+?)\|regex=(.+?)$', url)[0]
    r += urllib.unquote_plus(x)
    url = regex.resolve(r)

    PLAYLINK(name,url,iconimage)

def GENERATE_M3U8(url):

    if "iptvembed" in url:
        result = open_url(url)
        match = re.compile('#EXTM3U<br />(.+?)<div></div>',re.DOTALL).findall(result)
        for item in match:
            item = replace('<br />','\n')
            item = replace('</pre>','')
            url = item
   
    if "sourcetv" in url:
        result = open_url(url)
        match = re.compile('<pre class="alt2"(.+?)<br class="clearer" />',re.DOTALL).findall(result)
        for item in match:
            item = replace('<br />','\n')
            item = replace('</pre>','')
            url = item

    url = url.replace('#AAASTREAM:','#A:')
    url = url.replace('#EXTINF:','#A:')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
    li = []
    for params, display_name, url in matches:
        item_data = {"params": params, "display_name": display_name, "url": url}
        li.append(item_data)
    list = []
    for channel in li:
        item_data = {"display_name": channel["display_name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        list.append(item_data)

    found = 0
    for channel in list:
        found = 1
        name = GetEncodeString(channel["display_name"])
        url = GetEncodeString(channel["url"])
        url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
        if not ".m3u8" in url:
            addLink('[COLOR white]' + name + '[/COLOR]',url,2,icon,fanarts,'')
        else:
            addDir('[COLOR white]' + name + '[/COLOR]',url,10,icon,fanarts,'')

    if found == 0:
        addLink('[COLOR red]Sorry, No links found in this list.[/COLOR]',url,999,icon,fanarts,'')

def GET_SEARCH_TERMS(url):

    link=open_url(url)
    url2 = url
    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:
    
            links=re.compile('<search>(.+?)</search>').findall(item)
            if len(links)==1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]                        
                url=re.compile('<search>(.+?)</search>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = name + "!" + url + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,20,iconimage,iconimage) 

            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = url2 + "!" + name + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,22,iconimage,iconimage)

    xbmc.executebuiltin('Container.SetViewMode(500)')

def GETMULTI(name,url,iconimage):
    streamurl=[]
    streamname=[]
    streamicon=[]
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    links=re.compile('<link>(.+?)</link>').findall(urls)
    i=1
    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )
                i=i+1
    name='[COLOR red]'+name+'[/COLOR]'
    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        url = streamurl[select]
        print url

    url = streamurl[select]
    name = streamname[select]
    PLAYLINK(name,url,icon)
   
def GETMULTI_PLEXUS(name,url,iconimage):

    streamurl=[]
    streamname=[]
    streamicon=[]
    streamnumber=[]
    url = url.replace('NOTPLAY','')
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<plexus>(.+?)</plexus>').findall(urls)
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    
    base_start = "plugin://program.plexus/?url="
    base_end  =  "&mode=1&name=acestream+"
    i=0

    for sturl in links:
        i=i+1

        sturl2=sturl
        if '(' in sturl:
            sturl=sturl.split('(')[0]
            caption=str(sturl2.split('(')[1].replace(')',''))
            streamurl.append(sturl)
            streamname.append(caption)
            streamnumber.append('Stream ' + str(i))
        else:
            streamurl.append( sturl )
            streamname.append( 'Link '+str(i) )
            caption = name


    if i > 1:
        dialog = xbmcgui.Dialog()
        select = dialog.select(name,streamname)
        if select < 0:
            quit()
        else:
            number = streamurl[select]
            if not 'acestream://' in number:
                number = 'acestream://' + number
            url = base_start + number + base_end + streamname[select]
            name = streamname[select]
    else:   
        number = sturl
        if not 'acestream://' in number:
            number = 'acestream://' + number
        url = base_start + number + base_end + caption
        name = caption

    PLAYLINK(name,url,icon)
    
def GETMULTI_SD(name,url,iconimage):

    streamurl=[]
    streamname=[]
    streamicon=[]
    streamnumber=[]
    url = url.replace('NOTPLAY','')
    link=open_url(url)
    urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<sportsdevil>(.+?)</sportsdevil>').findall(urls)
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    
    sdbase = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title='+str(name)+'%26url='

    i=1

    for sturl in links:
                sturl2=sturl
                if '(' in sturl:
                        sturl=sturl.split('(')[0]
                        caption=str(sturl2.split('(')[1].replace(')',''))
                        streamurl.append(sturl)
                        streamname.append(caption)
                        streamnumber.append('Stream ' + str(i))
                else:
                        streamurl.append( sturl )
                        streamname.append( 'Link '+str(i) )

                i=i+1

    name='[COLOR red]'+name+'[/COLOR]'

    dialog = xbmcgui.Dialog()
    select = dialog.select(name,streamname)
    if select < 0:
        quit()
    else:
        check = streamname[select]
        suffix = "/"
        if not check.endswith(suffix):
              refer = check + "/"
        else:
              refer = check
        url = sdbase + streamurl[select] + "%26referer=" + refer

    name = streamname[select]
    PLAYLINK(name,url,icon)

def FIGHTCLUB_SEARCH(url):

    try:
        decide,url = url.split('|SPLIT|')
    except:  decide,url,url2,name = url.split('|SPLIT|')

    if decide == 'true':
        string =''
        keyboard = xbmc.Keyboard(string, 'Enter Search Term')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText()
            if len(string)>1:
                marker = string.lower()
            else: quit()

        namelist = []
        urllist  = []
        iconlist = []
        combinedlists = []

        dp.create(AddonTitle,"[COLOR white]We are searching for " + marker +".[/COLOR]",'','[COLOR yellow]Please wait...[/COLOR]')  
        dp.update(0)

        i = 1
        k = 0
        result = open_url(url)
        match = re.compile('<search>(.+?)</search>',re.DOTALL).findall(result)
        total = len(match)
        for item in match:
            progress = 100 * int(i)/int(total)
            dp.update(progress,'','[COLOR blue]Searching list ' + str(i) + ' of ' + str(total) + '[/COLOR]')
            result2 = open_url(item)
            match = re.compile('<article id="(.+?)</article>',re.DOTALL).findall(result2)
            for items in match:
                title=re.compile('title="(.+?)"').findall(items)[0]    
                url=re.compile('<a class="preview-link" href="(.+?)"').findall(items)[0]  
                iconimage=re.compile('https://pic.rutube.ru(.+?)size').findall(items)[0]  
                iconimage = "https://pic.rutube.ru" + iconimage + "size=l"
                title = title.replace('.',' ')
                if marker.lower() in title.lower():
                    k = k + 1
                    namelist.append(title)
                    urllist.append(url)
                    iconlist.append(iconimage)
                    combinedlists = list(zip(namelist,urllist,iconlist))

            i = i + 1

        tup = sorted(combinedlists)
        addLink('[B][COLOR dodgerblue]We found ' + str(k) + ' matches for ' + marker + '[/B][/COLOR]','url',999,icon,fanarts,'')
        addLink('#######################################################','url',999,icon,fanarts,'')
        for name,url,iconimage in tup:
            addLink('[COLOR white]' + name + '[/COLOR]',url,2,iconimage,iconimage,'')

    else:

        namelist = []
        urllist  = []
        iconlist = []
        combinedlists = []

        dp.create(AddonTitle,"[COLOR white]We are searching for " + name +".[/COLOR]",'','[COLOR yellow]Please wait...[/COLOR]')    
        dp.update(0)

        i = 1
        k = 0
        result = open_url(url2)
        urls=re.compile('<title>'+re.escape(name)+'</title>(.+?)</item>',re.DOTALL).findall(result)[0]
        links=re.compile('<term>(.+?)</term>').findall(urls)
        result2 = open_url(url)
        match2 = re.compile('<search>(.+?)</search>',re.DOTALL).findall(result2)
        total = len(match2)
        for item in match2:
            progress = 100 * int(i)/int(total)
            dp.update(progress,'','[COLOR blue]Searching list ' + str(i) + ' of ' + str(total) + '[/COLOR]')
            result2 = open_url(item)
            match = re.compile('<article id="(.+?)</article>',re.DOTALL).findall(result2)
            for items in match:
                title=re.compile('title="(.+?)"').findall(items)[0]   
                url=re.compile('<a class="preview-link" href="(.+?)"').findall(items)[0]  
                iconimage=re.compile('https://pic.rutube.ru(.+?)size').findall(items)[0]  
                iconimage = "https://pic.rutube.ru" + iconimage + "size=l"
                title = title.replace('.',' ')
                for marker in links:
                    if marker.lower() in title.lower():
                        k = k + 1
                        namelist.append(title)
                        urllist.append(url)
                        iconlist.append(iconimage)
                        combinedlists = list(zip(namelist,urllist,iconlist))
            i = i + 1

        tup = sorted(combinedlists)
        addLink('[B][COLOR dodgerblue]' + name + '[/B][/COLOR]','url',999,icon,fanarts,'')
        addLink('#######################################################','url',999,icon,fanarts,'')
        for name,url,iconimage in tup:
            addLink('[COLOR white]' + name + '[/COLOR]',url,2,iconimage,iconimage,'')

def GET_SEARCH_GAMES(url):
    
    today_raw = datetime.date.today()
    today_formated = datetime.datetime.strftime(today_raw,'%A %d %B %Y') 
    
    addLink('[COLOR dodgerblue]EVENTS FOR ' + str(today_formated).upper() + '[/COLOR]',url,20,icon,fanarts,"")
    addLink('##############################################',url,20,icon,fanarts,"")

    link=open_url(url)
    url2 = url
    match= re.compile('<item>(.+?)</item>').findall(link)
    for item in match:
    
            links=re.compile('<search>(.+?)</search>').findall(item)
            if len(links)==1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]                        
                url=re.compile('<search>(.+?)</search>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = name + "!" + url + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,20,iconimage,iconimage) 

            elif len(links)>1:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                url = url2 + "!" + name + "!" + iconimage
                name = '[COLOR white]' + name + '[/COLOR]'
                addDir(name,url,22,iconimage,iconimage)

def SEARCH_THROUGH_M3U_MULTI(name,url,iconimage):

    try:
        url,DISPLAY_NAME,iconimage = url.split('!')
    except: 
        dialog.ok(AddonTitle, "[COLOR blue]Sorry there was a problem processing your request.[/COLOR]","[COLOR blue]Sporie has plenty of content to choose from :-D[/COLOR]")
        quit()

    termlist=[]

    link=open_url(url)
    urls=re.compile('<title>'+re.escape(DISPLAY_NAME)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    iconimage=re.compile('<thumbnail>(.+?)</thumbnail>').findall(urls)[0]
    links=re.compile('<search>(.+?)</search>').findall(urls)
    for sturl in links:
        termlist.append( sturl )

    dp.create(AddonTitle,"[COLOR blue]We are just getting the channel links for you.[/COLOR]",'[COLOR yellow]Please wait...[/COLOR]','')    
    dp.update(0)

    z = 0

    namelist=[]
    urllist=[]
    countlist=[]
    combinedlists=[]

    dp.update(0)
    scraped = 0

    if scrape1 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MA=='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scrape2 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MTA='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scrape3 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MjA='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scraped == 0:
        dialog.ok(AddonTitle, "Error, no scrapers are enabled. Please enable some scrapers in the addon settings.")
        quit()

    tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=True)
    term_tup = sorted(termlist)

    a = 0
    
    dp.update(100)

    addLink('[COLOR dodgerblue][B]LINKS FOR ' + DISPLAY_NAME.upper() + '[/B][/COLOR]',url,999,iconimage,fanarts,'')
    addLink('================================================================',url,999,iconimage,fanarts,'')
    

    for term in term_tup:

        addLink('[COLOR orangered][B]' + term.upper() + ' LINKS[/B][/COLOR]',url,999,iconimage,fanarts,'')

        string = term.split(' ')

        for count,name,url in tup:

            forget = 0

            for find in string:
    
                if not find.lower() in name.lower():
                    forget = 1
            
            if forget == 0:
                a = a + 1
                if "hd" in name.lower():
                    addLink('[COLOR blue]LINK[/COLOR][COLOR blue] ' + str(a) + '[/COLOR] - [COLOR yellow][B]HD[/B][/COLOR]',url,2,iconimage,fanarts,'')
                else:
                    addLink('[COLOR blue]LINK[/COLOR][COLOR blue] ' + str(a) + '[/COLOR] - [COLOR white]SD[/COLOR]',url,2,iconimage,fanarts,'')
    
        if a == 0:
            addLink('[COLOR white]NO LINKS FOUND[/COLOR]',url,999,iconimage,fanarts,'')
        
        string = ""

    dp.close()

def SEARCH_THROUGH_M3U(name,url,iconimage):

    dp.create(AddonTitle,"[COLOR blue]We are just getting the channel links for you.[/COLOR]",'[COLOR yellow]Please wait...[/COLOR]','')    
    dp.update(0)

    z = 0
    try:
        DISPLAY_NAME,term,iconimage = url.split('!')
    except:
        try:
            term,iconimage = url.split('!')
            DISPLAY_NAME = term
        except: 
            dialog.ok(AddonTitle, "[COLOR blue]Sorry there was a problem processing your request.[/COLOR]","[COLOR blue]Sporie has plenty of content to choose from :-D[/COLOR]")
            quit()

    flag = 0

    if "all " in name.lower():
        term = term.replace('all ','').replace('ALL ','').replace('All ','')
        DISPLAY_NAME = DISPLAY_NAME.replace('all ','').replace('ALL ','').replace('All ','')
        flag=1

    namelist=[]
    urllist=[]
    countlist=[]
    combinedlists=[]

    dp.update(0)
    scraped = 0
    if scrape1 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MA=='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scrape2 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MTA='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scrape3 == "true":
        scraped = 1
        result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MjA='))
        match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
        for item in match:
            if z < 100:
                dp.update(z)
                z = z + 3
            item = replace('<br />','\n')
            url = item
            url = url.replace('#AAASTREAM:','#A:')
            url = url.replace('#EXTINF:','#A:')
            matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
            li = []
            for params, display_name, url in matches:
                item_data = {"params": params, "display_name": display_name, "url": url}
                li.append(item_data)
            lists = []
            for channel in li:
                item_data = {"display_name": channel["display_name"], "url": channel["url"]}
                matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
                for field, value in matches:
                    item_data[field.strip().lower().replace('-', '_')] = value.strip()
                lists.append(item_data)

            for channel in lists:
                name = GetEncodeString(channel["display_name"])
                url = GetEncodeString(channel["url"])
                url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
                namelist.append(name)               
                urllist.append(url)     
                if "hd" in name.lower():
                    countlist.append("1")
                else:
                    countlist.append("0")
                combinedlists = list(zip(countlist,namelist,urllist))

    if scraped == 0:
        dialog.ok(AddonTitle, "Error, no scrapers are enabled. Please enable some scrapers in the addon settings.")
        quit()

    tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=True)
    
    a = 0
    
    dp.update(100)

    addLink('[COLOR dodgerblue][B]LINKS FOR ' + DISPLAY_NAME.upper() + '[/B][/COLOR]',url,999,iconimage,fanarts,'')
    addLink('================================================================',url,999,iconimage,fanarts,'')
    string = term.split(' ')
    for count,name,url in tup:
        if flag == 1:
            new_name = name
            
        forget = 0

        for find in string:
    
            if not find.lower() in name.lower():
                forget = 1
            
        if forget == 0:
            a = a + 1
            if flag == 1:
                if "hd" in name.lower():
                    addLink('[COLOR blue] ' + str(new_name) + '[/COLOR] - [COLOR yellow][B]HD[/B][/COLOR]',url,2,iconimage,fanarts,'')
                else:
                    addLink('[COLOR blue] ' + str(new_name) + '[/COLOR] - [COLOR white]SD[/COLOR]',url,2,iconimage,fanarts,'')
            else:
                if "hd" in name.lower():
                    addLink('[COLOR blue]LINK[/COLOR][COLOR blue] ' + str(a) + '[/COLOR] - [COLOR yellow][B]HD[/B][/COLOR]',url,2,iconimage,fanarts,'')
                else:
                    addLink('[COLOR blue]LINK[/COLOR][COLOR blue] ' + str(a) + '[/COLOR] - [COLOR white]SD[/COLOR]',url,2,iconimage,fanarts,'')

    if a == 0:
        addLink('[COLOR white]NO LINKS FOUND[/COLOR]',url,999,iconimage,fanarts,'')

    dp.close()

def SEARCH_THROUGH_M3U_DIALOG(term):

    streamurl=[]
    streamname=[]

    result = open_url(base64.b64decode(b'aHR0cDovL2R2YnNhdC5ydS9zbWYvaW5kZXgucGhwP2FjdGlvbj1yZWNlbnQ7c3RhcnQ9MA=='))
    match = re.compile('#EXTM3U(.+?)</div>',re.DOTALL).findall(result)
    for item in match:
        item = replace('<br />','\n')
        url = item

        url = url.replace('#AAASTREAM:','#A:')
        url = url.replace('#EXTINF:','#A:')
        matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(url)
        li = []
        for params, display_name, url in matches:
            item_data = {"params": params, "display_name": display_name, "url": url}
            li.append(item_data)
        list = []
        for channel in li:
            item_data = {"display_name": channel["display_name"], "url": channel["url"]}
            matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
            for field, value in matches:
                item_data[field.strip().lower().replace('-', '_')] = value.strip()
            list.append(item_data)

        for channel in list:
            name = GetEncodeString(channel["display_name"])
            url = GetEncodeString(channel["url"])
            url = url.replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
            if term.lower() in name.lower():
                streamurl.append(url)
                streamname.append(name)

    dialog = xbmcgui.Dialog()
    select = dialog.select('[COLOR yellow]Search Term: [I]' + term + '[/I][/COLOR]',streamname)
    if select < 0:
        quit()

    url = streamurl[select]
    name = streamname[select]
    PLAYLINK(name,url,icon)

def READ_M3U(name,url,iconimage):

    response = open_url_m3u(url)
    response = response.replace('#AAASTREAM:','#A:')
    response = response.replace('#EXTINF:','#A:')
    matches=re.compile('^#A:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
    li = []
    for params, display_name, url in matches:
        item_data = {"params": params, "display_name": display_name, "url": url}
        li.append(item_data)
    lists = []
    for channel in li:
        item_data = {"display_name": channel["display_name"], "url": channel["url"]}
        matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
        for field, value in matches:
            item_data[field.strip().lower().replace('-', '_')] = value.strip()
        lists.append(item_data)
    
    if lists:
    
        term_check = plugintools.get_setting("sport_filter")
        term_check = term_check.replace(', ',',').replace(' ,',',')
        if (term_check == 'None') or (term_check == '') or (term_check == None):
            addLink('Click here to filter results by terms.','url',997,icon,fanarts)
            addLink('-----------------------------------------','url',997,icon,fanarts)
        else: 
            addLink('Click here to change filter terms.','url',997,icon,fanarts)
            addLink('List showing results containing: ' + term_check.title().replace(',',' & '),'url',997,icon,fanarts)
            addLink('-----------------------------------------','url',997,icon,fanarts)

        if ' ' in term_check: term_check = term_check.replace(' ','')
        namelist      = []
        urllist       = []
        combinedlists = []

        for channel in sorted(lists):
            name = GetEncodeString(channel["display_name"])
            name = M3U_CLEANER(name)
            name = name.lstrip()
            name = name.rstrip()
            url = GetEncodeString(channel["url"])
            url = url.replace('\\n','').replace('\n','').replace('\\r','').replace('\\t','').replace('\r','').replace('\t','').replace(' ','').replace('m3u8','m3u8')
            if (term_check == 'None') or (term_check == '') or (term_check == None):
                namelist.append(name)
                urllist.append(url)
                combinedlists = list(zip(namelist,urllist))
            else:
                if ',' in term_check:
                    terms = term_check.split(',')
                    for term in terms:
                        if (term.lower() in name.lower().replace(' ','')) and (url not in urllist):
                            namelist.append(name)
                            urllist.append(url)
                            combinedlists = list(zip(namelist,urllist))
                else:
                    if term_check.lower() in name.lower():
                        namelist.append(name)
                        urllist.append(url)
                        combinedlists = list(zip(namelist,urllist))

        tup = sorted(combinedlists)
        checking = len(tup)
        check = 1

        link_check = plugintools.get_setting("check_links")
    
        if link_check == 'true':
            try:
                limit = plugintools.get_setting("check_limit")
                if limit == '0': limit_num = 250
                elif limit == '1': limit_num = 500
                elif limit == '2': limit_num = 750
                elif limit == '3': limit_num = 1000
                elif limit == '4': limit_num = 99999999
                else: limit_num = 250
            except: limit_num = 250

        if (link_check == 'true') and (checking <= limit_num):
            dp.create(AddonTitle, "[COLOR white]We are checking link number....[/COLOR]","[COLOR white]Can be disabled or changed in settings.[/COLOR]","[COLOR blue][B]" + str(check) + " of " + str(checking) + "[/B][/COLOR] | [COLOR yellow][B]Please wait.....[/B][/COLOR]")
            dp.update(0)
            d = 0
            u = 0
            for name,url in tup:
                url = GET_RESPONSE(url)
                if (url == "None") or ('=' in name):
                    d = d + 1
                else: u = u + 1
                if check != checking:
                    check = check + 1
                progress = 100 * int(check)/int(checking)
                dp.update(progress,'','','[COLOR blue][B]Checking ' + str(check) + " of " + str(checking) + ' links[/B][/COLOR] | [COLOR lime][B]UP: ' + str(u) + '[/COLOR]   -   [COLOR red]DOWN: ' + str(d) + '[/B][/COLOR]')
                if (url != "None") and (not '=' in name):
                    addLink(name.title(),url,2,icon,fanarts,'')
                if dp.iscanceled():
                    dp.close()
                    break
            dp.close()
        else:
            for name,url in tup:
                if (url != "None") and (not '=' in name):
                    addLink(name.title(),url,2,icon,fanarts,'')

def M3U_CLEANER(string):

    string = string.lower()
    string = string.replace("ar:","")
    string = string.replace("uk:","")
    string = string.replace("fr:","")
    string = string.replace("hi:","")
    string = string.replace("de:","")
    string = string.replace("it:","")
    string = string.replace("es:","")
    string = string.replace("nl:","")
    string = string.replace("tr:","")
    string = string.replace("ex:","")
    string = string.replace("ar_","")
    string = string.replace("uk_","")
    string = string.replace("fr_","")
    string = string.replace("hi_","")
    string = string.replace("de_","")
    string = string.replace("it_","")
    string = string.replace("es_","")
    string = string.replace("nl_","")
    string = string.replace("tr_","")
    string = string.replace("ex_","")
    string = string.replace(":","")
    string = string.replace("_","")
    string = string.replace("-","")
    string = string.replace("*","")
    
    return string

def PREDICTIONS(name,url,iconimage):
    
    get_date = datetime.datetime.now()
    base = get_date.day

    today = base

    plus = datetime.date.today() + datetime.timedelta(days=0)
    plus_form = datetime.datetime.strftime(plus,'%A - %d %B %Y') 
    plus_url = 'http://www.predictz.com/predictions/'

    plus1 = datetime.date.today() + datetime.timedelta(days=1)
    plus1_form = datetime.datetime.strftime(plus1,'%A - %d %B %Y') 
    plus1_marker = datetime.datetime.strftime(plus1,'%d')
    plus1_url = 'http://www.predictz.com/predictions/tomorrow/'
    
    plus2 = datetime.date.today() + datetime.timedelta(days=2)
    plus2_form = datetime.datetime.strftime(plus2,'%A - %d %B %Y') 
    plus2_marker = datetime.datetime.strftime(plus2,'%y%m%d')
    plus2_url = 'http://www.predictz.com/predictions/20' + str(plus2_marker)

    plus3 = datetime.date.today() + datetime.timedelta(days=3)
    plus3_form = datetime.datetime.strftime(plus3,'%A - %d %B %Y') 
    plus3_marker = datetime.datetime.strftime(plus3,'%y%m%d')
    plus3_url = 'http://www.predictz.com/predictions/20' + str(plus3_marker)

    plus4 = datetime.date.today() + datetime.timedelta(days=4)
    plus4_form = datetime.datetime.strftime(plus4,'%A - %d %B %Y') 
    plus4_marker = datetime.datetime.strftime(plus4,'%y%m%d')
    plus4_url = 'http://www.predictz.com/predictions/20' + str(plus4_marker)

    #Start List of Dates
    addDir('Today' + ' - ' + str(plus_form),plus_url,41,icon,fanarts,'')
    addDir('Tomorrow' + ' - ' + str(plus1_form),plus1_url,41,icon,fanarts,'')
    addDir(str(plus2_form),plus2_url,41,icon,fanarts,'')
    addDir(str(plus3_form),plus3_url,41,icon,fanarts,'')
    addDir(str(plus4_form),plus4_url,41,icon,fanarts,'')

def GET_PREDICTIONS(name,url,iconimage):
    
    link=open_url(url)
    match= re.compile('<div class="scrolltable">(.+?)<div id="footerwrapper">').findall(link)
    string = str(match)
    match2= re.compile('<tr(.+?)</tr>').findall(string)
    for item in match2:
        try:
            league=re.compile('<a href="[^"]*">(.+?) Predictions</a>').findall(item)[0]
            addLink('#############################################','url',999,icon,fanarts,'')          
            addLink('[COLOR red][B]' + league + ' Predictions[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('#############################################','url',999,icon,fanarts,'')
        except: pass
        try:
            title=re.compile('title=".+?">(.+?)</a>').findall(item)[0]                      
            score=re.compile('<div class="score">(.+?)</div>').findall(item)[0]
            title = CLEAN_PREDICTIONS(title)
            score = CLEAN_PREDICTIONS(score)
            addLink('[COLOR orange][B]Prediction - [/COLOR][COLOR dodgerblue]' + score + ' [/B][/COLOR]| [COLOR mediumpurple]' + title + '[/COLOR]','url',999,icon,fanarts,'')
        except: pass

def ODDS(name,url,iconimage):
    
    get_date = datetime.datetime.now()
    base = get_date.day

    today = base

    plus = datetime.date.today() + datetime.timedelta(days=0)
    plus_form = datetime.datetime.strftime(plus,'%A - %d %B %Y') 
    plus_url = 'http://www.predictz.com/predictions/'

    plus1 = datetime.date.today() + datetime.timedelta(days=1)
    plus1_form = datetime.datetime.strftime(plus1,'%A - %d %B %Y') 
    plus1_marker = datetime.datetime.strftime(plus1,'%d')
    plus1_url = 'http://www.predictz.com/predictions/tomorrow/'
    
    plus2 = datetime.date.today() + datetime.timedelta(days=2)
    plus2_form = datetime.datetime.strftime(plus2,'%A - %d %B %Y') 
    plus2_marker = datetime.datetime.strftime(plus2,'%y%m%d')
    plus2_url = 'http://www.predictz.com/predictions/20' + str(plus2_marker)

    plus3 = datetime.date.today() + datetime.timedelta(days=3)
    plus3_form = datetime.datetime.strftime(plus3,'%A - %d %B %Y') 
    plus3_marker = datetime.datetime.strftime(plus3,'%y%m%d')
    plus3_url = 'http://www.predictz.com/predictions/20' + str(plus3_marker)

    plus4 = datetime.date.today() + datetime.timedelta(days=4)
    plus4_form = datetime.datetime.strftime(plus4,'%A - %d %B %Y') 
    plus4_marker = datetime.datetime.strftime(plus4,'%y%m%d')
    plus4_url = 'http://www.predictz.com/predictions/20' + str(plus4_marker)

    #Start List of Dates
    addDir('Today' + ' - ' + str(plus_form),plus_url,51,icon,fanarts,'')
    addDir('Tomorrow' + ' - ' + str(plus1_form),plus1_url,51,icon,fanarts,'')
    addDir(str(plus2_form),plus2_url,51,icon,fanarts,'')
    addDir(str(plus3_form),plus3_url,51,icon,fanarts,'')
    addDir(str(plus4_form),plus4_url,51,icon,fanarts,'')

def GET_ODDS(name,url,iconimage):
    
    link=open_url(url)
    match= re.compile('<div class="scrolltable">(.+?)<div id="footerwrapper">').findall(link)
    string = str(match)
    match2= re.compile('<tr(.+?)</tr>').findall(string)
    for item in match2:
        try:
            league=re.compile('<a href="[^"]*">(.+?) Predictions</a>').findall(item)[0]
            addLink('#############################################','url',999,icon,fanarts,'')          
            addLink('[COLOR red][B]' + league + '[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('#############################################','url',999,icon,fanarts,'')
        except: pass
        try:
            title=re.compile('title=".+?">(.+?)</a>').findall(item)[0]                      
            home_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[0]
            draw_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[1]
            away_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[2]
            title = CLEAN_PREDICTIONS(title)
            addLink('[COLOR mediumpurple][B]' + title + '[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]Home Win[/COLOR][COLOR dodgerblue] (' + home_odds + ')[/COLOR][COLOR orange]  -  Draw[/COLOR][COLOR dodgerblue] (' + draw_odds + ')[/COLOR][COLOR orange]  -  Away Win[/COLOR][COLOR dodgerblue] (' + away_odds + ')[/COLOR]','url',999,icon,fanarts,'')
        except: pass

def FORM(name,url,iconimage):
    
    get_date = datetime.datetime.now()
    base = get_date.day

    today = base

    plus = datetime.date.today() + datetime.timedelta(days=0)
    plus_form = datetime.datetime.strftime(plus,'%A - %d %B %Y') 
    plus_url = 'http://www.predictz.com/predictions/'

    plus1 = datetime.date.today() + datetime.timedelta(days=1)
    plus1_form = datetime.datetime.strftime(plus1,'%A - %d %B %Y') 
    plus1_marker = datetime.datetime.strftime(plus1,'%d')
    plus1_url = 'http://www.predictz.com/predictions/tomorrow/'
    
    plus2 = datetime.date.today() + datetime.timedelta(days=2)
    plus2_form = datetime.datetime.strftime(plus2,'%A - %d %B %Y') 
    plus2_marker = datetime.datetime.strftime(plus2,'%y%m%d')
    plus2_url = 'http://www.predictz.com/predictions/20' + str(plus2_marker)

    plus3 = datetime.date.today() + datetime.timedelta(days=3)
    plus3_form = datetime.datetime.strftime(plus3,'%A - %d %B %Y') 
    plus3_marker = datetime.datetime.strftime(plus3,'%y%m%d')
    plus3_url = 'http://www.predictz.com/predictions/20' + str(plus3_marker)

    plus4 = datetime.date.today() + datetime.timedelta(days=4)
    plus4_form = datetime.datetime.strftime(plus4,'%A - %d %B %Y') 
    plus4_marker = datetime.datetime.strftime(plus4,'%y%m%d')
    plus4_url = 'http://www.predictz.com/predictions/20' + str(plus4_marker)

    #Start List of Dates
    addDir('Today' + ' - ' + str(plus_form),plus_url,61,icon,fanarts,'')
    addDir('Tomorrow' + ' - ' + str(plus1_form),plus1_url,61,icon,fanarts,'')
    addDir(str(plus2_form),plus2_url,61,icon,fanarts,'')
    addDir(str(plus3_form),plus3_url,61,icon,fanarts,'')
    addDir(str(plus4_form),plus4_url,61,icon,fanarts,'')

def GET_FORM(name,url,iconimage):
    
    link=open_url(url)
    match= re.compile('<div class="scrolltable">(.+?)<div id="footerwrapper">').findall(link)
    string = str(match)
    match2= re.compile('<tr(.+?)</tr>').findall(string)
    for item in match2:
        try:
            league=re.compile('<a href="[^"]*">(.+?) Predictions</a>').findall(item)[0]
            addLink('#############################################','url',999,icon,fanarts,'')          
            addLink('[COLOR red][B]' + league + '[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('#############################################','url',999,icon,fanarts,'')
        except: pass
        try:
            title=re.compile('title=".+?">(.+?)</a>').findall(item)[0]      
            a,b = title.split(' v ')
            form_1=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[0]
            form_2=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[1]
            form_3=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[2]
            form_4=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[3]
            form_5=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[4]
            form_6=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[5]
            form_7=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[6]
            form_8=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[7]
            form_9=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[8]
            form_10=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[9]

            if form_1 == "W":
                form_1 = '[COLOR lime]W[/COLOR]'
            elif form_1 == "D":
                form_1 = '[COLOR yellow]D[/COLOR]'
            else: form_1 = '[COLOR red]L[/COLOR]'

            if form_2 == "W":
                form_2 = '[COLOR lime]W[/COLOR]'
            elif form_2 == "D":
                form_2 = '[COLOR yellow]D[/COLOR]'
            else: form_2 = '[COLOR red]L[/COLOR]'

            if form_3 == "W":
                form_3 = '[COLOR lime]W[/COLOR]'
            elif form_3 == "D":
                form_3 = '[COLOR yellow]D[/COLOR]'
            else: form_3 = '[COLOR red]L[/COLOR]'

            if form_4 == "W":
                form_4 = '[COLOR lime]W[/COLOR]'
            elif form_4 == "D":
                form_4 = '[COLOR yellow]D[/COLOR]'
            else: form_4 = '[COLOR red]L[/COLOR]'
            
            if form_5 == "W":
                form_5 = '[COLOR lime]W[/COLOR]'
            elif form_5 == "D":
                form_5 = '[COLOR yellow]D[/COLOR]'
            else: form_5 = '[COLOR red]L[/COLOR]'
            
            if form_6 == "W":
                form_6 = '[COLOR lime]W[/COLOR]'
            elif form_6 == "D":
                form_6 = '[COLOR yellow]D[/COLOR]'
            else: form_6 = '[COLOR red]L[/COLOR]'
            
            if form_7 == "W":
                form_7 = '[COLOR lime]W[/COLOR]'
            elif form_7 == "D":
                form_7 = '[COLOR yellow]D[/COLOR]'
            else: form_7 = '[COLOR red]L[/COLOR]'
            
            if form_8 == "W":
                form_8 = '[COLOR lime]W[/COLOR]'
            elif form_8 == "D":
                form_8 = '[COLOR yellow]D[/COLOR]'
            else: form_8 = '[COLOR red]L[/COLOR]'
            
            if form_9 == "W":
                form_9 = '[COLOR lime]W[/COLOR]'
            elif form_9 == "D":
                form_9 = '[COLOR yellow]D[/COLOR]'
            else: form_9 = '[COLOR red]L[/COLOR]'
            
            if form_10 == "W":
                form_10 = '[COLOR lime]W[/COLOR]'
            elif form_10 == "D":
                form_10 = '[COLOR yellow]D[/COLOR]'
            else: form_10 = '[COLOR red]L[/COLOR]'
                
            a = CLEAN_PREDICTIONS(a)
            b = CLEAN_PREDICTIONS(b)
            addLink('[COLOR mediumpurple][B]' + a + ' Form Guide[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[B]' + form_1 + '  ' + form_2 + '  ' + form_3 + '  ' + form_4 + '  ' + form_5 + '[/B]','url',999,icon,fanarts,'')
            addLink('[COLOR mediumpurple][B]' + b + ' Form Guide[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[B]' + form_6 + '  ' + form_7 + '  ' + form_8 + '  ' + form_9 + '  ' + form_10 + '[/B]','url',999,icon,fanarts,'')
        except: pass

def OVERVIEW(name,url,iconimage):
    
    get_date = datetime.datetime.now()
    base = get_date.day

    today = base

    plus = datetime.date.today() + datetime.timedelta(days=0)
    plus_form = datetime.datetime.strftime(plus,'%A - %d %B %Y') 
    plus_url = 'http://www.predictz.com/predictions/'

    plus1 = datetime.date.today() + datetime.timedelta(days=1)
    plus1_form = datetime.datetime.strftime(plus1,'%A - %d %B %Y') 
    plus1_marker = datetime.datetime.strftime(plus1,'%d')
    plus1_url = 'http://www.predictz.com/predictions/tomorrow/'
    
    plus2 = datetime.date.today() + datetime.timedelta(days=2)
    plus2_form = datetime.datetime.strftime(plus2,'%A - %d %B %Y') 
    plus2_marker = datetime.datetime.strftime(plus2,'%y%m%d')
    plus2_url = 'http://www.predictz.com/predictions/20' + str(plus2_marker)

    plus3 = datetime.date.today() + datetime.timedelta(days=3)
    plus3_form = datetime.datetime.strftime(plus3,'%A - %d %B %Y') 
    plus3_marker = datetime.datetime.strftime(plus3,'%y%m%d')
    plus3_url = 'http://www.predictz.com/predictions/20' + str(plus3_marker)

    plus4 = datetime.date.today() + datetime.timedelta(days=4)
    plus4_form = datetime.datetime.strftime(plus4,'%A - %d %B %Y') 
    plus4_marker = datetime.datetime.strftime(plus4,'%y%m%d')
    plus4_url = 'http://www.predictz.com/predictions/20' + str(plus4_marker)

    #Start List of Dates
    addDir('Today' + ' - ' + str(plus_form),plus_url,71,icon,fanarts,'')
    addDir('Tomorrow' + ' - ' + str(plus1_form),plus1_url,71,icon,fanarts,'')
    addDir(str(plus2_form),plus2_url,71,icon,fanarts,'')
    addDir(str(plus3_form),plus3_url,71,icon,fanarts,'')
    addDir(str(plus4_form),plus4_url,71,icon,fanarts,'')

def GET_OVERVIEW(name,url,iconimage):
    
    link=open_url(url)
    match= re.compile('<div class="scrolltable">(.+?)<div id="footerwrapper">').findall(link)
    string = str(match)
    match2= re.compile('<tr(.+?)</tr>').findall(string)
    for item in match2:
        try:
            league=re.compile('<a href="[^"]*">(.+?) Predictions</a>').findall(item)[0]
            addLink('#############################################','url',999,icon,fanarts,'')          
            addLink('[COLOR red][B]' + league + '[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('#############################################','url',999,icon,fanarts,'')
        except: pass
        try:
            title=re.compile('title=".+?">(.+?)</a>').findall(item)[0]      
            a,b = title.split(' v ')

            score=re.compile('<div class="score">(.+?)</div>').findall(item)[0]
            home_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[0]
            draw_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[1]
            away_odds=re.compile('title=".+?" rel="external nofollow">(.+?)</a>').findall(item)[2]
            form_1=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[0]
            form_2=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[1]
            form_3=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[2]
            form_4=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[3]
            form_5=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[4]
            form_6=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[5]
            form_7=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[6]
            form_8=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[7]
            form_9=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[8]
            form_10=re.compile('<div class="last5.+?">(.+?)</div>').findall(item)[9]

            if form_1 == "W":
                form_1 = '[COLOR lime]W[/COLOR]'
            elif form_1 == "D":
                form_1 = '[COLOR yellow]D[/COLOR]'
            else: form_1 = '[COLOR red]L[/COLOR]'

            if form_2 == "W":
                form_2 = '[COLOR lime]W[/COLOR]'
            elif form_2 == "D":
                form_2 = '[COLOR yellow]D[/COLOR]'
            else: form_2 = '[COLOR red]L[/COLOR]'

            if form_3 == "W":
                form_3 = '[COLOR lime]W[/COLOR]'
            elif form_3 == "D":
                form_3 = '[COLOR yellow]D[/COLOR]'
            else: form_3 = '[COLOR red]L[/COLOR]'

            if form_4 == "W":
                form_4 = '[COLOR lime]W[/COLOR]'
            elif form_4 == "D":
                form_4 = '[COLOR yellow]D[/COLOR]'
            else: form_4 = '[COLOR red]L[/COLOR]'
            
            if form_5 == "W":
                form_5 = '[COLOR lime]W[/COLOR]'
            elif form_5 == "D":
                form_5 = '[COLOR yellow]D[/COLOR]'
            else: form_5 = '[COLOR red]L[/COLOR]'
            
            if form_6 == "W":
                form_6 = '[COLOR lime]W[/COLOR]'
            elif form_6 == "D":
                form_6 = '[COLOR yellow]D[/COLOR]'
            else: form_6 = '[COLOR red]L[/COLOR]'
            
            if form_7 == "W":
                form_7 = '[COLOR lime]W[/COLOR]'
            elif form_7 == "D":
                form_7 = '[COLOR yellow]D[/COLOR]'
            else: form_7 = '[COLOR red]L[/COLOR]'
            
            if form_8 == "W":
                form_8 = '[COLOR lime]W[/COLOR]'
            elif form_8 == "D":
                form_8 = '[COLOR yellow]D[/COLOR]'
            else: form_8 = '[COLOR red]L[/COLOR]'
            
            if form_9 == "W":
                form_9 = '[COLOR lime]W[/COLOR]'
            elif form_9 == "D":
                form_9 = '[COLOR yellow]D[/COLOR]'
            else: form_9 = '[COLOR red]L[/COLOR]'
            
            if form_10 == "W":
                form_10 = '[COLOR lime]W[/COLOR]'
            elif form_10 == "D":
                form_10 = '[COLOR yellow]D[/COLOR]'
            else: form_10 = '[COLOR red]L[/COLOR]'
                
            a = CLEAN_PREDICTIONS(a)
            b = CLEAN_PREDICTIONS(b)
            title = CLEAN_PREDICTIONS(title)
            score = CLEAN_PREDICTIONS(score)
            addLink('[COLOR blue][B]' + title + '[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]Prediction - [/COLOR][COLOR dodgerblue][B]' + score + ' [/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]' + a + ' Form: - [/COLOR][B]' + form_1 + '  ' + form_2 + '  ' + form_3 + '  ' + form_4 + '  ' + form_5 + '[/B]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]' + b + ' Form - [/COLOR][B]' + form_6 + '  ' + form_7 + '  ' + form_8 + '  ' + form_9 + '  ' + form_10 + '[/B]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]' + a + ' Win[/COLOR][COLOR dodgerblue][B] (' + home_odds + ')[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]Draw[/COLOR][COLOR dodgerblue][B] (' + draw_odds + ')[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('[COLOR orange]' + b + ' Win[/COLOR][COLOR dodgerblue][B] (' + away_odds + ')[/B][/COLOR]','url',999,icon,fanarts,'')
            addLink('#############################################','url',999,icon,fanarts,'')

        except: pass

def GET_LIVE_SCORES(name,url,iconimage):
    
    team1list = []
    team2list = []
    scorelist = []
    minutelist = []
    markerlist = []
    combinedlists=[]

    link=open_url('http://www.livescores.com')
    match= re.compile('<div class="cal">(.+?)<div id="fb-root">').findall(link)
    string = str(match)
    match2= re.compile('<div class="min(.+?)data-esd="').findall(string)
    for item in match2:
        team1=re.compile('<div class="ply tright name">(.+?)</div>').findall(item)[0]
        team2=re.compile('<div class="ply name">(.+?)<').findall(item)[0]
        try:
            score=re.compile('class="scorelink">(.+?)</a>').findall(item)[0]
        except:
            score=re.compile('<div class="sco">(.+?)</div>').findall(item)[0]
        try:
            time=re.compile('"><img src=".+?" alt="live"/>(.+?)</div>').findall(item)[0]
        except: time=re.compile('">(.+?)</div>').findall(item)[0]
        time = time.replace('&#x27;',' Minute')
        
        if "minute" in time.lower():
            markerlist.append('3')
        elif "ht" in time.lower():
            markerlist.append('3')
        elif "ft" in time.lower():
            markerlist.append('2')
        else: markerlist.append('1')

        team1list.append(team1)         
        team2list.append(team2) 
        scorelist.append(score)
        minutelist.append(time)
        combinedlists = list(zip(markerlist,team1list,team2list,scorelist,minutelist))

    addLink('[COLOR dodgerblue][B]The scores will update every 10 seconds.[/B][/COLOR]','url',998,icon,fanarts,'')
    addLink('[COLOR darkgray]######################################[/COLOR]','url',999,icon,fanarts,'')

    tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=True)
    live = 0
    fulltime = 0
    later = 0
    for final_marker, team_1, team_2, score_, minute_ in tup:
        if final_marker == "3":
            if live == 0:
                addLink('[COLOR white][B]Live Now[/B][/COLOR]','url',999,icon,fanarts,'')
                live = 1
        elif final_marker == "2":
            if fulltime == 0:
                addLink('[COLOR white][B]Finished[/B][/COLOR]','url',999,icon,fanarts,'')
                fulltime = 1
        elif final_marker == "1":
            if later == 0:
                addLink('[COLOR white][B]Later Today[/B][/COLOR]','url',999,icon,fanarts,'')
                later = 1
        minute_ = minute_.replace("'","").replace(' Minute',"'")
        score_ = score_.replace(" ","")
        addLink('[COLOR red][B]' + minute_ + "[/B][/COLOR]- [COLOR blue]" + score_ + "[/COLOR] | [COLOR white]" + team_1 + "vs" + team_2 + '[/COLOR]','url',999,icon,fanarts,'')

def CLEAN(text):

    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />','\n')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&nbsp;',"")

    return text

def CLEAN_PREDICTIONS(text):

    text = str(text)
    text = text.replace('\\r','')
    text = text.replace('\\n','')
    text = text.replace('\\t','')
    text = text.replace('\\','')
    text = text.replace('<br />',' ')
    text = text.replace('<hr />','')
    text = text.replace('&#039;',"'")
    text = text.replace('&quot;','"')
    text = text.replace('&rsquo;',"'")
    text = text.replace('&amp;',"&")
    text = text.replace('&nbsp;',"")

    return text

def CLEAN_TERM(text):

    text = str(text)
    text = text.replace('ATR','at the races')
    text = text.replace('British Eurosport','eurosport')
    text = text.replace('Sky Sports','sky sports')
    text = text.replace('sky sport ','sky sports ')
    text = text.replace('skysports ','sky sports ')
    text = text.replace('skysport ','sky sports ')
    text = text.replace('RP Greyhound TV','greyhound')

    return text

def PLAYSD(name,url,iconimage):

    if not "SportsDevil" in url:
        link = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26title=Stream%26url=' + url
        url = link + '%26referer=' +url
    liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
    liz.setPath(url)
    xbmc.Player ().play(url, liz, False)

def PLAYLINK(name,url,iconimage):

    dp.create(AddonTitle,"[COLOR blue]Opening link...[/COLOR]",'[COLOR yellow]Please wait...[/COLOR]','')   
    dp.update(0)

    if "pl_type=user" in url:
        result = open_url(url)
        url = re.compile('<meta property="og:video:iframe" content="(.+?)">').findall(result)[0]

    if not "plugin" in url:
        try:
            if not'http'in url:url='http://'+url
        except: 
            dialog.ok(AddonTitle, "[COLOR blue]Sorry there was a problem playing this link.[/COLOR]","[COLOR blue]Sportie has plenty of content to choose from :-D[/COLOR]")
            quit()

    name = urllib.quote_plus(name)
    if not 'f4m'in url:
        if '.m3u8' in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=HLSRETRY&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon  
        elif '.ts'in url:
            url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name='+name+'&amp;url='+url+'&amp;iconImage='+icon  
    #else: url = url + '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    
    import urlresolver
    if urlresolver.HostedMediaFile(url).valid_url(): 
        stream_url = urlresolver.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
        liz.setPath(stream_url)
        dp.close()
        xbmc.Player ().play(stream_url, liz, False)
        quit()
    else:
        stream_url=url
        liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
        liz.setPath(stream_url)
        dp.close()
        xbmc.Player ().play(stream_url, liz, False)
        quit()

def TEXTBOXES(header=None,announce=None):
    class TextBox():
        WINDOW=10147
        CONTROL_LABEL=1
        CONTROL_TEXTBOX=5
        def __init__(self,*args,**kwargs):
            xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
            self.win=xbmcgui.Window(self.WINDOW) # get window
            xbmc.sleep(500) # give window time to initialize
            self.setControls()
        def setControls(self):
            if header == None: self.win.getControl(self.CONTROL_LABEL).setLabel(sys.args(0)) # set heading
            else: self.win.getControl(self.CONTROL_LABEL).setLabel(header) # set heading
            self.win.getControl(self.CONTROL_TEXTBOX).setText(str(announce))
            return
    announce = open_url_m3u(announce)
    announce = announce.encode('utf-8')
    TextBox()
    while xbmc.getCondVisibility('Window.IsVisible(10147)'):
        time.sleep(.5)

def TEXTBOXES_GIT(header=None,announce=None):
    class TextBox():
        WINDOW=10147
        CONTROL_LABEL=1
        CONTROL_TEXTBOX=5
        def __init__(self,*args,**kwargs):
            xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
            self.win=xbmcgui.Window(self.WINDOW) # get window
            xbmc.sleep(500) # give window time to initialize
            self.setControls()
        def setControls(self):
            if header == None: self.win.getControl(self.CONTROL_LABEL).setLabel(sys.args(0)) # set heading
            else: self.win.getControl(self.CONTROL_LABEL).setLabel(header) # set heading
            self.win.getControl(self.CONTROL_TEXTBOX).setText(str(announce))
            return
    announce = announce.encode('utf-8')
    TextBox()
    while xbmc.getCondVisibility('Window.IsVisible(10147)'):
        time.sleep(.5)
        
def GET_RESPONSE(url):

    http_interface = httplib2.Http(timeout=1.0)

    try:
        response, content = http_interface.request(url, method="HEAD")
        print ("Response status: %d - %s" % (response.status, response.reason))

        if response.status == 200:
            return url
        else: return "None"

    except:
        return "None"

def GET_KODI_VERSION():

    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
    version=float(xbmc_version[:4])
    if version >= 11.0 and version <= 11.9:
        codename = 'Eden'
    elif version >= 12.0 and version <= 12.9:
        codename = 'Frodo'
    elif version >= 13.0 and version <= 13.9:
        codename = 'Gotham'
    elif version >= 14.0 and version <= 14.9:
        codename = 'Helix'
    elif version >= 15.0 and version <= 15.9:
        codename = 'Isengard'
    elif version >= 16.0 and version <= 16.9:
        codename = 'Jarvis'
    elif version >= 17.0 and version <= 17.9:
        codename = 'Krypton'
    else: codename = "Decline"
    
    return codename

def Set_View():

    xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
    version=float(xbmc_version[:4])
    if version >= 11.0 and version <= 11.9:
        codename = 'Eden'
    elif version >= 12.0 and version <= 12.9:
        codename = 'Frodo'
    elif version >= 13.0 and version <= 13.9:
        codename = 'Gotham'
    elif version >= 14.0 and version <= 14.9:
        codename = 'Helix'
    elif version >= 15.0 and version <= 15.9:
        codename = 'Isengard'
    elif version >= 16.0 and version <= 16.9:
        codename = 'Jarvis'
    elif version >= 17.0 and version <= 17.9:
        codename = 'Krypton'
    else: codename = "Decline"
    
    if codename == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif codename == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else: xbmc.executebuiltin('Container.SetViewMode(50)')

def open_url(url,cookie=None):

    try:
        req = urllib2.Request(url)
        if not "referer" in url.lower():
            req.add_header('Referer', 'https://www.google.com/')
        if "echocoder" in url:
            req.add_header('User-Agent', base64.b64decode(b'VGhlV2l6YXJkSXNIZXJl'))
        elif not "user-agent" in url.lower():
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        if cookie != None:
            req.add_header('Cookie', 'cookiename=%s' % cookie)
        response = urllib2.urlopen(req, timeout = 15)
        link=response.read()
        link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
        response.close()
        return link
    except Exception as e:
        if ('tls' in str(e).lower()) or ('ssl' in str(e).lower()):
            kodi.notify(msg='Error connecting to the URL due to a TLS/SSL issue.', duration=5000, sound=True)
            quit()
        else:
            kodi.notify(msg='URL Error. Please try again.', duration=5000, sound=True)
            quit()

def open_url_ss(url):

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    response = urllib2.urlopen(req, timeout = 10)
    link=response.read()
    link=link.replace('\n','').replace('\t','')
    response.close()
    return link

def open_url_m3u(url):

    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        response = urllib2.urlopen(req, timeout = 10)
        link=response.read()
        response.close()
        return link
    except Exception as e:
        if ('tls' in str(e).lower()) or ('ssl' in str(e).lower()):
            kodi.notify(msg='Error connecting to the URL due to a TLS/SSL issue.', duration=5000, sound=True)
            quit()
        else:
            kodi.notify(msg='URL Error. Please try again.', duration=5000, sound=True)
            quit()

def GetEncodeString(str):
    try:
        import chardet
        str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
    except:
        try:
            str = str.encode("utf-8")
        except:
            pass
    return str

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]                    
        return param
    
def addDir(name,url,mode,iconimage,fanart,description='',cm=None):

    if cm == None: cm = []
    if not "http" in iconimage:
        iconimage = icon
    if not "http" in fanart:
        fanart = fanarts
    if 'imgur' in iconimage: iconimage += '.png'
    if 'imgur' in fanart: fanart += '.png'
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanart )
    liz.setProperty( "icon_Image", iconimage )
    liz.addContextMenuItems(items=cm, replaceItems=False)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name, url, mode, iconimage, fanart, description=''):

    if not "http" in iconimage:
        iconimage = icon
    if not "http" in fanart:
        fanart = fanarts
    if 'imgur' in iconimage: iconimage += '.png'
    if 'imgur' in fanart: fanart += '.png'
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanart )
    liz.setProperty( "icon_Image", iconimage )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def GITHUB_ISSUES():

    choice = dialog.yesno("[COLOR red]Please select an option[/COLOR]", "Would you like to view open issues or closed issues?",yeslabel='Closed',nolabel='Open')

    import githubissues
    if choice == 0: name = 'open'
    elif choice == 1: name = 'closed'
    else: quit()
    githubissues.run('Colossal1/plugin.video.sportie', '%s' % name)
    file = xbmc.translatePath(os.path.join(kodi.datafolder, '%s-issues-%s.csv' % (kodi.get_id(),name)))
    
    with open(file,mode='r')as f: txt = f.read()
    items = re.findall('<item>(.+?)</item>', txt, re.DOTALL)
    if (not items) or (len(items) < 1):
        msg_text = kodi.giveColor('No %s issues with Sportie at this time.' % name.title(),'blue',True)
    else:
        msg_text = kodi.giveColor('%s Issues with Sportie\n' % name.title(),'blue',True) + kodi.giveColor('Report Issues @ https://github.com/Colossal1/plugin.video.sportie/issues','white',True) + '\n---------------------------------\n\n'
        for item in items:
            try: id = re.findall('<id>([^<]+)', item)[0]
            except: id = 'Unknown'
            try: user = re.findall('<username>([^<]+)', item)[0]
            except: user = 'Unknown'
            try: label = re.findall('<label>([^<]+)', item)[0]
            except: label = 'Unknown'
            try: title = re.findall('<title>([^<]+)', item)[0]
            except: title = 'Unknown'
            try: body = re.findall('<body>([^<]+)', item)[0]
            except: body = 'Unknown'
            try: 
                created = re.findall('<created>([^<]+)', item)[0]
                date,time = created.split('T')
            except:
                date = 'Unknown'
                time = 'Unknwon'
            msg_text += '[B]ID: %s | Label: %s \nBy: %s on %s at %s[/B] \n\nTitle: %s \nMessage %s \n\n---------------------------------\n\n' \
                         % (id, \
                            kodi.githubLabel(label), \
                            user, \
                            date, \
                            time.replace('Z',''), \
                            title, \
                            body)
    TEXTBOXES_GIT('Sportie Issues', msg_text)

# Run Starter Def
STARTER()

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None; fanart=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanart=urllib.unquote_plus(params["fanart"])
except: pass
 
if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:GetContent(name,url)
elif mode==2:PLAYLINK(name,url,iconimage)
elif mode==3:GETMULTI(name,url,iconimage)
elif mode==4:PLAYSD(name,url,iconimage)
elif mode==7:GETMULTI_PLEXUS(name,url,iconimage)
elif mode==8:GETMULTI_SD(name,url,iconimage)
elif mode==10:READ_M3U(name,url,iconimage)
elif mode==22:SEARCH_THROUGH_M3U_MULTI(name,url,iconimage)
elif mode==30:GET_REGEX(name,url,iconimage)
elif mode==40:PREDICTIONS(name,url,iconimage)
elif mode==41:GET_PREDICTIONS(name,url,iconimage)
elif mode==50:ODDS(name,url,iconimage)
elif mode==51:GET_ODDS(name,url,iconimage)
elif mode==60:FORM(name,url,iconimage)
elif mode==61:GET_FORM(name,url,iconimage)
elif mode==70:OVERVIEW(name,url,iconimage)
elif mode==71:GET_OVERVIEW(name,url,iconimage)
elif mode==80:GET_LIVE_SCORES(name,url,iconimage)
elif mode==90:SCRAPE_RUTUBE_PLAYLISTS(name,url,iconimage)
elif mode==91:SCRAPE_RUTUBE_PLAYLISTS_NP(name,url,iconimage)
elif mode==95:SCRAPE_ARENA_VISION()
elif mode==96:SCRAPE_ARENA_VISION_GET_LINK(name,url,iconimage)
elif mode==97:SCRAPE_ARENA_VISION_GET_CHANNELS(name,url,iconimage)
elif mode==205:SCRAPE_HESGOAL()
elif mode==206:SCRAPE_HESGOAL_FIND_LINK(name,url,iconimage)
elif mode==221:SCRAPE_UFC_GETLINK(name,url,iconimage)
elif mode==222:FIGHTCLUB_SEARCH(url)
elif mode==298:SCRAPE_CRICBOX_CHANNELS(url)
elif mode==299:SCRAPE_BIGSPORTS_CHANNELS(url)
elif mode==300:SCRAPE_BIGSPORTS_GET_LINKS(name,url,iconimage)
elif mode==301:SCRAPE_BIGSPORTS(url)
elif mode==302:SCRAPE_CRICBOX(url)
elif mode==306:PLAY_CRICBOX(name,url,iconimage)
elif mode==307:soccerstreams.SCRAPE_SOCCERSTREAMS()
elif mode==308:soccerstreams.SCRAPE_SOCCERSTREAMS_GET_LINKS(name,url,iconimage)
elif mode==309:PLAY_SPORTSMAMA(name,url,iconimage)
elif mode==310:SCRAPE_SPORTSMAMA_HOME()
elif mode==311:SCRAPE_SPORTSMAMA_CHANNELS()
elif mode==312:SCRAPE_247HD()
elif mode==313:LIVE_TV()
elif mode==314:SCRAPE_GOALTOGOALS()
elif mode==315:SCRAPE_GOALTOGOALS_SECTIONS(url)
elif mode==316:GET_GOALTOGOALS_LINKS(name,url,iconimage)
elif mode==317:EVENT_REDDIT()
elif mode==318:REDDIT_PLAYER(name,url,iconimage)
elif mode==319:REDDIT_GET(url)
elif mode==320:REDDIT_MAIN()
elif mode==321:REDDIT_ADD()
elif mode==322:REDDIT_SUGGESTED()
elif mode==323:REDDIT_REMOVE(name,url)
elif mode==994:GITHUB_ISSUES()
elif mode==995:TEXTBOXES(name,url)
elif mode==996:ENABLE_DB_ADDON(url)
elif mode==997:
    xbmcaddon.Addon(id=addon_id).openSettings()
    xbmc.executebuiltin("Container.Refresh")
elif mode==998:xbmc.executebuiltin("Container.Refresh")

if mode < 1: 
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
else:
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)
if mode == 80:
    xbmc.sleep(10000)
    xbmc.executebuiltin('Container.Refresh')