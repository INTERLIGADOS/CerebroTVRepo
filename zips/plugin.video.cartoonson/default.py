# -*- coding: utf-8 -*-
import urllib2, urllib, xbmcgui, xbmcplugin, xbmc, re, sys, os, dandy,xbmcaddon
import urlresolver
from addon.common.addon import Addon
import requests
s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.cartoonson'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
ADDON      = xbmcaddon.Addon()
ADDON_PATH = ADDON.getAddonInfo('path')
ICON = ADDON.getAddonInfo('icon')
FANART = ADDON.getAddonInfo('fanart')
PATH = 'cartoonson'
VERSION = ADDON.getAddonInfo('version')
BASEURL = 'http://www.cartoonson.com/'
BASEURL2= 'http://www.cartoonson.com'
ART = ADDON_PATH + "/resources/icons/"

def Main_menu():
    addDir('[B][COLOR white]All Content[/COLOR][/B]',BASEURL,1,ART + 'allcont.jpg',FANART,'')
    addDir('[B][COLOR white]By Studio[/COLOR][/B]',BASEURL,5,ART + 'studio.jpg',FANART,'')
    addDir('[B][COLOR white]Characters[/COLOR][/B]',BASEURL,6,ART + 'char.jpg',FANART,'')
    addDir('[B][COLOR white]Series[/COLOR][/B]',BASEURL,7,ART + 'series.jpg',FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def studios(url):
    OPEN = Open_Url(url)
    Regex = re.compile('id="menu-group-id-2"(.+?)</ul>',re.DOTALL).findall(OPEN)[0]
    Regex = Regex.replace('\r','').replace('\n','').replace('\t','')
    Regex2 = re.compile('href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,BASEURL2 + url,1,iconimage,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def charac(url):
    OPEN = Open_Url(url)
    Regex = re.compile('id="menu-group-id-3"(.+?)</ul>',re.DOTALL).findall(OPEN)[0]
    Regex = Regex.replace('\r','').replace('\n','').replace('\t','')
    Regex2 = re.compile('href="(.+?)">(.+?)</a>',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,BASEURL2 + url,1,ICON,FANART,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def toons_only():
        addDir('[B][COLOR white]Archer (TV series) Full Episodes - Season 2[/COLOR][/B]',BASEURL + 'cartoons/view/id/archer-full-episodes/season/2',2,BASEURL + '_resources/Cartoons/season/61/image/555x418/Archer_Season_2_Episodes.jpg',BASEURL + '_resources/Cartoons/season/61/image/555x418/Archer_Season_2_Episodes.jpg','')
        addDir('[B][COLOR white]Archer (TV series) Full Episodes - Season 1[/COLOR][/B]',BASEURL + 'cartoons/view/id/archer-full-episodes/season/1',2,BASEURL + '_resources/Cartoons/season/60/image/555x418/Archer_Season_1_Episodes.jpg',BASEURL + '_resources/Cartoons/season/60/image/555x418/Archer_Season_1_Episodes.jpg','')
        addDir('[B][COLOR white]One-Punch Man (TV Series) Dub Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/one-punch-man-full-episodes',2,BASEURL + '_resources/Cartoons/show/88/image/555x418/One-Punch-Man.jpg',BASEURL + '_resources/Cartoons/show/88/image/555x418/One-Punch-Man.jpg','')
        addDir('[B][COLOR white]Frisky Dingo (TV Series 2006-2008) Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/frisky-dingo-full-episodes',2,BASEURL + '_resources/Cartoons/show/87/image/555x418/frisky-dingo.jpg',BASEURL + '_resources/Cartoons/show/87/image/555x418/frisky-dingo.jpg','')
        addDir('[B][COLOR white]Sailor Moon R (1993–1994) Season 2 Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/sailor-moon-r-season-2',2,BASEURL + '_resources/Cartoons/show/86/image/555x418/sailor-moon-season-2.jpg',BASEURL + '_resources/Cartoons/show/86/image/555x418/sailor-moon-season-2.jpg','')
        addDir('[B][COLOR white]Sailor Moon (1992–1993) Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/sailor-moon-season-1',2,BASEURL + '_resources/Cartoons/show/85/image/555x418/sailor-moon-season-1.jpg',BASEURL + '_resources/Cartoons/show/85/image/555x418/sailor-moon-season-1.jpg','')
        addDir('[B][COLOR white]Aquaman (1968 TV Series)[/COLOR][/B]',BASEURL + 'cartoons/view/id/aquaman-1968-episodes',2,BASEURL + '_resources/Cartoons/show/84/image/555x418/Aquaman.jpg',BASEURL + '_resources/Cartoons/show/84/image/555x418/Aquaman.jpg','')
        addDir('[B][COLOR white]The Buzz on Maggie (2005-2006) Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-buzz-on-maggie',2,BASEURL + '_resources/Cartoons/show/83/image/555x418/maggie-the-fly.jpg',BASEURL + '_resources/Cartoons/show/83/image/555x418/maggie-the-fly.jpg','')
        addDir('[B][COLOR white]The Oblongs (TV Series 2001-2002) Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-oblongs-full-episodes',2,BASEURL + '_resources/Cartoons/show/82/image/555x418/the-obolongs1.jpg',BASEURL + '_resources/Cartoons/show/82/image/555x418/the-obolongs1.jpg','')
        addDir('[B][COLOR white]The Porky Pig Show (1964-1967)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-porky-pig-full-episodes',2,BASEURL + '_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg',BASEURL + '_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg','')
        addDir('[B][COLOR white]The Ripping Friends (2001-2002)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-ripping-friends-episodes',2,BASEURL + '_resources/Cartoons/show/79/image/555x418/ripping-friends.jpg',BASEURL + '_resources/Cartoons/show/79/image/555x418/ripping-friends.jpg','')
        addDir('[B][COLOR white]The Legend of Korra Season 4[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-legend-of-korra-book-4',2,BASEURL + '_resources/Cartoons/show/78/image/555x418/legend-of-korra-book-4.jpg',BASEURL + '_resources/Cartoons/show/78/image/555x418/legend-of-korra-book-4.jpg','')
        addDir('[B][COLOR white]The Legend of Korra Season 3[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-legend-of-korra-book-3',2,BASEURL + '_resources/Cartoons/show/77/image/555x418/legend-of-korra-book-3.jpg',BASEURL + '_resources/Cartoons/show/77/image/555x418/legend-of-korra-book-3.jpg','')
        addDir('[B][COLOR white]The Legend of Korra Season 2[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-legend-of-korra-book-2',2,BASEURL + '_resources/Cartoons/show/76/image/555x418/legend-of-korra-book-2.jpg',BASEURL + '_resources/Cartoons/show/76/image/555x418/legend-of-korra-book-2.jpg','')
        addDir('[B][COLOR white]The Legend of Korra Season 1[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-legend-of-korra-book-1',2,BASEURL + '_resources/Cartoons/show/75/image/555x418/legend-of-korra-book-1.jpg',BASEURL + '_resources/Cartoons/show/75/image/555x418/legend-of-korra-book-1.jpg','')
        addDir('[B][COLOR white]SWAT Kats: The Radical Squadron Full Episodes[/COLOR][/B]',BASEURL + 'cartoons/view/id/swat-kats-the-radical-squadron',2,BASEURL + '_resources/Cartoons/show/74/image/555x418/swat-kats.jpg',BASEURL + '_resources/Cartoons/show/74/image/555x418/swat-kats.jpg','')
        addDir('[B][COLOR white]Cybersix (TV Series 1999-2000)[/COLOR][/B]',BASEURL + 'cartoons/view/id/cybersix-full-episodes',2,BASEURL + '_resources/Cartoons/show/73/image/555x418/cybersix.jpg',BASEURL + '_resources/Cartoons/show/73/image/555x418/cybersix.jpg','')
        addDir('[B][COLOR white]Road Rovers (TV Series 1996-1997)[/COLOR][/B]',BASEURL + 'cartoons/view/id/road-rovers-full-episodes',2,BASEURL + '_resources/Cartoons/show/72/image/555x418/road-rovers-by-seriojainc.jpg',BASEURL + '_resources/Cartoons/show/72/image/555x418/road-rovers-by-seriojainc.jpg','')
        addDir('[B][COLOR white]Scooby\'s Laff-A Lympics (TV Series 1977–1979)[/COLOR][/B]',BASEURL + 'cartoons/view/id/scoobys-laff-a-lympics-full-episodes',2,BASEURL + '_resources/Cartoons/show/71/image/555x418/laff-a-lympics1.jpg',BASEURL + '_resources/Cartoons/show/71/image/555x418/laff-a-lympics1.jpg','')
        addDir('[B][COLOR white]DC Super Friends (2015 TV Series)[/COLOR][/B]',BASEURL + 'cartoons/view/id/dc-super-friends-full-episodes',2,BASEURL + '_resources/Cartoons/show/70/image/555x418/dc-superfriends.jpg',BASEURL + '_resources/Cartoons/show/70/image/555x418/dc-superfriends.jpg','')
        addDir('[B][COLOR white]Young Justice (2010 TV Series)[/COLOR][/B]',BASEURL + 'cartoons/view/id/young-justice-full-episodes',2,BASEURL + '_resources/Cartoons/show/69/image/555x418/Young_Justice.jpg',BASEURL + '_resources/Cartoons/show/69/image/555x418/Young_Justice.jpg','')
        addDir('[B][COLOR white]Green Lantern: The Animated Series[/COLOR][/B]',BASEURL + 'cartoons/view/id/green-lantern-the-animated-series-full-episodes',2,BASEURL + '_resources/Cartoons/show/68/image/555x418/green-latern.jpg',BASEURL + '_resources/Cartoons/show/68/image/555x418/green-latern.jpg','')
        addDir('[B][COLOR white]Denver, the Last Dinosaur (TV Series 1988-1990)[/COLOR][/B]',BASEURL + 'cartoons/view/id/denver-the-last-dinosaur-episodes',2,BASEURL + '_resources/Cartoons/show/67/image/555x418/Denver_the_Last_Dinosaur.jpg',BASEURL + '_resources/Cartoons/show/67/image/555x418/Denver_the_Last_Dinosaur.jpg','')
        addDir('[B][COLOR white]Iron Man (TV Series 1994-1996)[/COLOR][/B]',BASEURL + 'cartoons/view/id/iron-man-tv-series-1994-1996',2,BASEURL + '_resources/Cartoons/show/66/image/555x418/Iron-Man-animated-series.jpg',BASEURL + '_resources/Cartoons/show/66/image/555x418/Iron-Man-animated-series.jpg','')
        addDir('[B][COLOR white]Aeon Flux (TV Series 1991-1995)[/COLOR][/B]',BASEURL + 'cartoons/view/id/aeon-flux-full-episodes',2,BASEURL + '_resources/Cartoons/show/65/image/555x418/aeon-flux.jpg',BASEURL + '_resources/Cartoons/show/65/image/555x418/aeon-flux.jpg','')
        addDir('[B][COLOR white]Ed, Edd n Eddy (TV Series 1999-2009)[/COLOR][/B]',BASEURL + 'cartoons/view/id/ed-edd-n-eddy-full-episodes',2,BASEURL + '_resources/Cartoons/show/64/image/555x418/ed-edd-n-eddy.jpg',BASEURL + '_resources/Cartoons/show/64/image/555x418/ed-edd-n-eddy.jpg','')
        addDir('[B][COLOR white]Generator Rex (TV Series 2010-2013)[/COLOR][/B]',BASEURL + 'cartoons/view/id/generator-rex-tv-series-2010-2013',2,BASEURL + '_resources/Cartoons/show/63/image/555x418/generator-rex.jpg',BASEURL + '_resources/Cartoons/show/63/image/555x418/generator-rex.jpg','')
        addDir('[B][COLOR white]Race to the Edge[/COLOR][/B]',BASEURL + 'cartoons/view/id/fosters-home-for-imaginary-friends-episodes',2,BASEURL + '_resources/Cartoons/show/62/image/555x418/Fosters-Home-for-Imaginary-Friends.jpg',BASEURL + '_resources/Cartoons/show/62/image/555x418/Fosters-Home-for-Imaginary-Friends.jpg','')
        addDir('[B][COLOR white]Race to the Edge[/COLOR][/B]',BASEURL + 'cartoons/view/id/race-to-the-edge',2,BASEURL + '_resources/Cartoons/show/61/image/555x418/dragons_race_edge.jpg',BASEURL + '_resources/Cartoons/show/61/image/555x418/dragons_race_edge.jpg','')
        addDir('[B][COLOR white]Dragons Defenders of Berk[/COLOR][/B]',BASEURL + 'cartoons/view/id/dragons-defenders-of-berk',2,BASEURL + '_resources/Cartoons/show/60/image/555x418/Defenders_of_berk_1.jpg',BASEURL + '_resources/Cartoons/show/60/image/555x418/Defenders_of_berk_1.jpg','')
        addDir('[B][COLOR white]Dragons Riders of Berk[/COLOR][/B]',BASEURL + 'cartoons/view/id/dragon-riders-of-berk',2,BASEURL + '_resources/Cartoons/show/59/image/555x418/dragons-riders-of-berk.jpg',BASEURL + '_resources/Cartoons/show/59/image/555x418/dragons-riders-of-berk.jpg','')
        addDir('[B][COLOR white]Invader ZIM[/COLOR][/B]',BASEURL + 'cartoons/view/id/invader-zim-tv-series-2001-2004',2,BASEURL + '_resources/Cartoons/show/58/image/555x418/invader-zim-featured.jpg',BASEURL + '_resources/Cartoons/show/58/image/555x418/invader-zim-featured.jpg','')
        addDir('[B][COLOR white]The New Batman Adventures[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-new-batman-adventures-tv-series',2,BASEURL + '_resources/Cartoons/show/57/image/555x418/The-New-Batman-Adventures.jpg',BASEURL + '_resources/Cartoons/show/57/image/555x418/The-New-Batman-Adventures.jpg','')
        addDir('[B][COLOR white]The Best of Mr. Peabody & Sherman[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-best-of-mr-peabody-and-sherman',2,BASEURL + '_resources/Cartoons/show/54/image/555x418/The_Mr._Peabody__Sherman_Show_1959-1962.jpg',BASEURL + '_resources/Cartoons/show/54/image/555x418/The_Mr._Peabody__Sherman_Show_1959-1962.jpg','')
        addDir('[B][COLOR white]The Addams Family (1992)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-addams-family-1992-tv-series',2,BASEURL + '_resources/Cartoons/show/53/image/555x418/the-addams-family-1992.jpg',BASEURL + '_resources/Cartoons/show/53/image/555x418/the-addams-family-1992.jpg','')
        addDir('[B][COLOR white]The Avengers: Earths Mightiest Heroes[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-avengers-earth-s-mightiest-heroes',2,BASEURL + '_resources/Cartoons/show/52/image/555x418/avenger_earths_mightiest_heroes.jpg',BASEURL + '_resources/Cartoons/show/52/image/555x418/avenger_earths_mightiest_heroes.jpg','')
        addDir('[B][COLOR white]Baby Looney Tunes (2001-2006)[/COLOR][/B]',BASEURL + 'cartoons/view/id/baby-looney-tunes-tv-series',2,BASEURL + '_resources/Cartoons/show/51/image/555x418/baby-looney-toons.jpg',BASEURL + '_resources/Cartoons/show/51/image/555x418/baby-looney-toons.jpg','')
        addDir('[B][COLOR white]The Cleveland Show (2009–2013)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-cleveland-show-2009-2013-tv-series',2,BASEURL + '_resources/Cartoons/show/22/image/555x418/The_Cleveland_Show_.jpg',BASEURL + '_resources/Cartoons/show/22/image/555x418/The_Cleveland_Show_.jpg','')
        addDir('[B][COLOR white]Tom and Jerry[/COLOR][/B]',BASEURL + 'cartoons/view/id/tom-and-jerry-classic-collection',2,BASEURL + '_resources/Cartoons/show/12/image/555x418/Tom-and-Jerry-classic.jpg',BASEURL + '_resources/Cartoons/show/12/image/555x418/Tom-and-Jerry-classic.jpg','')
        addDir('[B][COLOR white]Avatar: The Last Airbender[/COLOR][/B]',BASEURL + 'cartoons/view/id/avatar-the-last-airbender',2,BASEURL + '_resources/Cartoons/show/8/image/555x418/avatar-the-last-airbender-episodes.jpg',BASEURL + '_resources/Cartoons/show/8/image/555x418/avatar-the-last-airbender-episodes.jpg','')
        addDir('[B][COLOR white]Ben 10: Omniverse[/COLOR][/B]',BASEURL + 'cartoons/view/id/ben-10-omniverse',2,BASEURL + '_resources/Cartoons/show/9/image/555x418/Ben-10-Omniverse2.jpg',BASEURL + '_resources/Cartoons/show/9/image/555x418/Ben-10-Omniverse2.jpg','')
        addDir('[B][COLOR white]Courage the Cowardly Dog[/COLOR][/B]',BASEURL + 'cartoons/view/id/courage-the-cowardly-dog',2,BASEURL + '_resources/Cartoons/show/7/image/555x418/courage-the-cowardly-dog-show.jpg',BASEURL + '_resources/Cartoons/show/7/image/555x418/courage-the-cowardly-dog-show.jpg','')
        addDir('[B][COLOR white]The Flintstones[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-flintstones-tv-series',2,BASEURL + '_resources/Cartoons/show/14/image/555x418/The-Flintstone-TV-series.jpg',BASEURL + '_resources/Cartoons/show/14/image/555x418/The-Flintstone-TV-series.jpg','')
        addDir('[B][COLOR white]The Bugs Bunny Show[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-bugs-bunny-show',2,BASEURL + '_resources/Cartoons/show/13/image/555x418/bugs-bunny-show.jpg',BASEURL + '_resources/Cartoons/show/13/image/555x418/bugs-bunny-show.jpg','')
        addDir('[B][COLOR white]Family Guy[/COLOR][/B]',BASEURL + 'cartoons/view/id/family-guy-tv-series',2,BASEURL + '_resources/Cartoons/show/18/image/555x418/family-guy.jpg',BASEURL + '_resources/Cartoons/show/18/image/555x418/family-guy.jpg','')
        addDir('[B][COLOR white]The Legend of Korra[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-legend-of-korra',2,BASEURL + '_resources/Cartoons/show/27/image/555x418/the-legend-of-korra.jpg',BASEURL + '_resources/Cartoons/show/27/image/555x418/the-legend-of-korra.jpg','')
        addDir('[B][COLOR white]As Told by Ginger (TV Series)[/COLOR][/B]',BASEURL + 'cartoons/view/id/as-told-by-ginger-tv-series',2,BASEURL + '_resources/Cartoons/show/48/image/555x418/As_Told_By_Ginger.jpg',BASEURL + '_resources/Cartoons/show/48/image/555x418/As_Told_By_Ginger.jpg','')       
        addDir('[B][COLOR white]Yo Yogi! (TV Series 1991-1992)[/COLOR][/B]',BASEURL + 'cartoons/view/id/yo-yogi-tv-series-1991-1992',2,BASEURL + '_resources/Cartoons/show/47/image/555x418/Yo_Yogi_.jpg',BASEURL + '_resources/Cartoons/show/47/image/555x418/Yo_Yogi_.jpg','') 		
        addDir('[B][COLOR white]Over the Garden Wall (TV Miniseries)[/COLOR][/B]',BASEURL + 'cartoons/view/id/over-the-garden-wall-tv-miniseries',2,BASEURL + '_resources/Cartoons/show/46/image/555x418/Over_the_Garden_Wall_.jpg',BASEURL + '_resources/Cartoons/show/46/image/555x418/Over_the_Garden_Wall_.jpg','')
        addDir('[B][COLOR white]Mr. Bean - The Animated Series[/COLOR][/B]',BASEURL + 'cartoons/view/id/mr-bean-the-animated-series',2,BASEURL + '_resources/Cartoons/show/44/image/555x418/Mr.-Bean1.jpg',BASEURL + '_resources/Cartoons/show/44/image/555x418/Mr.-Bean1.jpg','') 		
        addDir('[B][COLOR white]Scooby-Doo, Where Are You! (1969-1978)[/COLOR][/B]',BASEURL + 'cartoons/view/id/scooby-doo-where-are-you-1969-1978',2,BASEURL + '_resources/Cartoons/show/43/image/555x418/scooby-doo-where-are-you.jpg',BASEURL + '_resources/Cartoons/show/43/image/555x418/scooby-doo-where-are-you.jpg','')
        addDir('[B][COLOR white]The Jetsons (1962-1963)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-jetsons-tv-series-1962-1963',2,BASEURL + '_resources/Cartoons/show/35/image/555x418/jetsons.jpg',BASEURL + '_resources/Cartoons/show/35/image/555x418/jetsons.jpg','')
        addDir('[B][COLOR white]The Smurfs (1981–1989)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-smurfs-tv-series-1981-1989',2,BASEURL + '_resources/Cartoons/show/19/image/555x418/The_Smurfs_1981.jpg',BASEURL + '_resources/Cartoons/show/19/image/555x418/The_Smurfs_1981.jpg','')
        addDir('[B][COLOR white]Tom & Jerry Kids Show (1990-1994)[/COLOR][/B]',BASEURL + 'cartoons/view/id/tom-and-jerry-kids-show-1990-1994',2,BASEURL + '_resources/Cartoons/show/6/image/555x418/tom__Jerry_kids_show_.jpg',BASEURL + '_resources/Cartoons/show/6/image/555x418/tom__Jerry_kids_show_.jpg','')
        addDir('[B][COLOR white]Tom and Jerry Tales[/COLOR][/B]',BASEURL + 'cartoons/view/id/tom-and-jerry-tales',2,BASEURL + '_resources/Cartoons/show/2/image/555x418/Tom-And-Jerry-Tales-all-volumes.jpg',BASEURL + '_resources/Cartoons/show/2/image/555x418/Tom-And-Jerry-Tales-all-volumes.jpg','')
        addDir('[B][COLOR white]Gargoyles (1994-1996)[/COLOR][/B]',BASEURL + 'cartoons/view/id/gargoyles-1994-1996-tv-series',2,BASEURL + '_resources/Cartoons/show/31/image/555x418/disney-s-gargoyles.jpg',BASEURL + '_resources/Cartoons/show/31/image/555x418/disney-s-gargoyles.jpg','')
        addDir('[B][COLOR white]Gravity Falls[/COLOR][/B]',BASEURL + 'cartoons/view/id/gravity-falls-tv-series',2,BASEURL + '_resources/Cartoons/show/20/image/555x418/gravity-falls.jpg',BASEURL + '_resources/Cartoons/show/20/image/555x418/gravity-falls.jpg','')
        addDir('[B][COLOR white]Bunnicula[/COLOR][/B]',BASEURL + 'cartoons/view/id/bunnicula-tv-series',2,BASEURL + '_resources/Cartoons/show/40/image/555x418/Bunnicula_Title.jpg',BASEURL + '_resources/Cartoons/show/40/image/555x418/Bunnicula_Title.jpg','')
        addDir('[B][COLOR white]Wile E. Coyote and The Road Runner[/COLOR][/B]',BASEURL + 'cartoons/view/id/wile-e-coyote-and-the-road-runner',2,BASEURL + '_resources/Cartoons/show/39/image/555x418/Wile_E._Coyote_and_The_Road_Runner.jpg',BASEURL + '_resources/Cartoons/show/39/image/555x418/Wile_E._Coyote_and_The_Road_Runner.jpg','')
        addDir('[B][COLOR white]We Bare Bears[/COLOR][/B]',BASEURL + 'cartoons/view/id/we-bare-bears-tv-series',2,BASEURL + '_resources/Cartoons/show/42/image/555x418/we-bare-bears.jpg',BASEURL + '_resources/Cartoons/show/42/image/555x418/we-bare-bears.jpg','')
        addDir('[B][COLOR white]Class of 3000[/COLOR][/B]',BASEURL + 'cartoons/view/id/class-of-3000-tv-series-2006',2,BASEURL + '_resources/Cartoons/show/36/image/555x418/Class-of-3000-Cartoon-Animation.jpg',BASEURL + '_resources/Cartoons/show/36/image/555x418/Class-of-3000-Cartoon-Animation.jpg','')
        addDir('[B][COLOR white]Adventure Time[/COLOR][/B]',BASEURL + 'cartoons/view/id/adventure-time-tv-series',2,BASEURL + '_resources/Cartoons/show/32/image/555x418/adventure-time.jpg',BASEURL + '_resources/Cartoons/show/32/image/555x418/adventure-time.jpg','')
        addDir('[B][COLOR white]The Marvelous Misadventures of Flapjack[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-marvelous-misadventures-of-flapjack',2,BASEURL + '_resources/Cartoons/show/30/image/555x418/the_marvelous_misadventures_of_flapjack.jpg',BASEURL + '_resources/Cartoons/show/30/image/555x418/the_marvelous_misadventures_of_flapjack.jpg','')
        addDir('[B][COLOR white]The Boondocks (2005)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-boondocks-tv-series-2005',2,BASEURL + '_resources/Cartoons/show/23/image/555x418/the-boondocks.jpg',BASEURL + '_resources/Cartoons/show/23/image/555x418/the-boondocks.jpg','')
        addDir('[B][COLOR white]The Land Before Time Movies[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-land-before-time-movies',2,BASEURL + '_resources/Cartoons/show/11/image/555x418/the-land-before-time-movies.jpg',BASEURL + '_resources/Cartoons/show/11/image/555x418/the-land-before-time-movies.jpg','')
        addDir('[B][COLOR white]Danny Phantom (2004-2007)[/COLOR][/B]',BASEURL + 'cartoons/view/id/danny-phantom-tv-series-2004-2007',2,BASEURL + '_resources/Cartoons/show/38/image/555x418/danny-phantom.jpg',BASEURL + '_resources/Cartoons/show/38/image/555x418/danny-phantom.jpg','')
        addDir('[B][COLOR white]Sonic X (2003-2004)[/COLOR][/B]',BASEURL + 'cartoons/view/id/sonic-x-tv-series-2003-2004',2,BASEURL + '_resources/Cartoons/show/37/image/555x418/Sonic.X..jpg',BASEURL + '_resources/Cartoons/show/37/image/555x418/Sonic.X..jpg','')
        addDir('[B][COLOR white]Bruno the Kid (1996-1997)[/COLOR][/B]',BASEURL + 'cartoons/view/id/bruno-the-kid-tv-series-1996-1997',2,BASEURL + '_resources/Cartoons/show/34/image/555x418/bruno-the-kid.jpg',BASEURL + '_resources/Cartoons/show/34/image/555x418/bruno-the-kid.jpg','')
        addDir('[B][COLOR white]C Bear and Jamal (1996-1997)[/COLOR][/B]',BASEURL + 'cartoons/view/id/c-bear-and-jamal-tv-series-1996-1997',2,BASEURL + '_resources/Cartoons/show/33/image/555x418/C-Bear-and-Jamal_-1.jpg',BASEURL + '_resources/Cartoons/show/33/image/555x418/C-Bear-and-Jamal_-1.jpg','')
        addDir('[B][COLOR white]Justice League Unlimited (2004-2006)[/COLOR][/B]',BASEURL + 'cartoons/view/id/justice-league-unlimited-2004-2006',2,BASEURL + '_resources/Cartoons/show/29/image/555x418/justice-league-unlimited-1.jpg',BASEURL + '_resources/Cartoons/show/29/image/555x418/justice-league-unlimited-1.jpg','')
        addDir('[B][COLOR white]Justice League (2001-2004)[/COLOR][/B]',BASEURL + 'cartoons/view/id/justice-league-tv-series-2001-2004',2,BASEURL + '_resources/Cartoons/show/28/image/555x418/Justice_League_TV_Series_20012004.jpg',BASEURL + '_resources/Cartoons/show/28/image/555x418/Justice_League_TV_Series_20012004.jpg','')
        addDir('[B][COLOR white]Steven Universe[/COLOR][/B]',BASEURL + 'cartoons/view/id/steven-universe-tv-series',2,BASEURL + '_resources/Cartoons/show/26/image/555x418/Steven_Universe-all_characters.jpg',BASEURL + '_resources/Cartoons/show/26/image/555x418/Steven_Universe-all_characters.jpg','')
        addDir('[B][COLOR white]Rick and Morty[/COLOR][/B]',BASEURL + 'cartoons/view/id/rick-and-morty-tv-series',2,BASEURL + '_resources/Cartoons/show/25/image/555x418/rick-and-morty.jpg',BASEURL + '_resources/Cartoons/show/25/image/555x418/rick-and-morty.jpg','')
        addDir('[B][COLOR white]Maggie and the Ferocious Beast[/COLOR][/B]',BASEURL + 'cartoons/view/id/maggie-and-the-ferocious-beast-tv-series',2,BASEURL + '_resources/Cartoons/show/24/image/555x418/Maggie_and_the_Ferocious_Beast1.jpg',BASEURL + '_resources/Cartoons/show/24/image/555x418/Maggie_and_the_Ferocious_Beast1.jpg','')
        addDir('[B][COLOR white]Archer[/COLOR][/B]',BASEURL + 'cartoons/view/id/archer-tv-series',2,BASEURL + '_resources/Cartoons/show/21/image/555x418/archer-18817.jpg',BASEURL + '_resources/Cartoons/show/21/image/555x418/archer-18817.jpg','')
        addDir('[B][COLOR white]Black Panther (Mini-Series)[/COLOR][/B]',BASEURL + 'cartoons/view/id/black-panther-tv-mini-series',2,BASEURL + '_resources/Cartoons/show/17/image/555x418/Black-Panther_1.jpg',BASEURL + '_resources/Cartoons/show/17/image/555x418/Black-Panther_1.jpg','')
        addDir('[B][COLOR white]Saikano (2002)[/COLOR][/B]',BASEURL + 'cartoons/view/id/saikano-2002-dub-series',2,BASEURL + '_resources/Cartoons/show/49/image/555x418/saikano.jpg',BASEURL + '_resources/Cartoons/show/49/image/555x418/saikano.jpg','')
        addDir('[B][COLOR white]No Game No Life[/COLOR][/B]',BASEURL + 'cartoons/view/id/no-game-no-life-the-series',2,BASEURL + '_resources/Cartoons/show/56/image/555x418/no-game-no-life1.jpg',BASEURL + '_resources/Cartoons/show/56/image/555x418/no-game-no-life1.jpg','')
        setView('movies', 'movie-view')
    
def page_content(url):
    OPEN = Open_Url(url)
    Regex = re.compile('class="image-overlay">.+?src="(.+?)".+?href="(.+?)" title="(.+?)">',re.DOTALL).findall(OPEN)
    for icon,url,name in Regex:
            icon = icon.replace('/336x280','')
            name = name.replace('Watch ','').replace('&#039;','\'').replace('&amp;','&').replace(' Film','')
            if 'Series' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Season ' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Full Episodes' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif ' Episodes' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Peabody' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Trailer' in name:
                url = url.replace('view','watch')
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,150,icon,icon,'')
            elif 'Mightiest' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Miniseries' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Where Are You' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Wile E' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Flapjack' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Justice League Unlimeted' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Bunny Show' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Collection' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Before Time' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Animated Movies' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Omniverse' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Airbender' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Cowardly' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Kids Show' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Cinderella Films' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Volumes' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Booba' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Dragons' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'to the Edge' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            elif 'Friends Episodes' in name:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,icon,icon,'')
            else:
                url = url.replace('view','watch')
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,icon,icon,'')
    np = re.compile('href="(.+?)">(.+?)</a>',re.DOTALL).findall(OPEN)
    for url,name in np:
            if '&raquo;' in name:
                    addDir('[B][COLOR red]Next Page>>>[/COLOR][/B]',url,1,ART + 'nextpage.jpg',FANART,'')
    setView('movies', 'movie-view')
    
def shows_Menu(url):
    OPEN = Open_Url(url)
    if '<h3><span>Seasons</span></h3>' in OPEN:
        holderpage = re.compile('<h3 class="text-center".+?href="(.+?)">(.+?)</a></h3>',re.DOTALL).findall(OPEN)
        for url,name in holderpage:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,iconimage,iconimage,'')
    else:
        Regex = re.compile('data-parent=.+?href=".+?".+?href="(.+?)".+?<p>(.+?)</p>',re.DOTALL).findall(OPEN)
        for url,name, in Regex:
                url = url.replace('watch-preview','watch')
                name = name.replace('Watch ','').replace('- Cartoon for kids','').replace('online in HD','').replace('full movie','').replace('in awesome quality on any device.','').replace('in high quality','').replace('online ','').replace(' on all devices','').replace(' for free','')
                if 'Booba' in name:
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,150,iconimage,iconimage,'')
                else:
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,iconimage,iconimage,'')
    xbmc.executebuiltin('Container.SetViewMode(50)') 

    

	########################################

def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link

def addDir(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==100 or mode==150:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
		

def resolve(name,url,iconimage,description):
    OPEN = Open_Url(url)
    try:
        url = re.compile('<source.+?src="(.+?)">',re.DOTALL).findall(OPEN)[0]
        if 'bit.ly' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location']
        elif 'blogspot' in url:
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        else:
            url=urlresolver.resolve(url)
    except:
        url = re.compile('<iframe.+?src="(.+?)">',re.DOTALL).findall(OPEN)[0]
        if 'bit.ly' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location']
        elif 'blogspot' in url:
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        else:
            url=urlresolver.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def setView(content, viewType):
    ''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '504'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '503'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '515'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '508'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '501'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '51'
        elif addon.get_setting(viewType) == 'Low List':
            VT = '724'
        elif addon.get_setting(viewType) == 'List':
            VT = '50'
        elif addon.get_setting(viewType) == 'Default Menu View':
            VT = addon.get_setting('default-view1')
        elif addon.get_setting(viewType) == 'Default TV Shows View':
            VT = addon.get_setting('default-view2')
        elif addon.get_setting(viewType) == 'Default Episodes View':
            VT = addon.get_setting('default-view3')
        elif addon.get_setting(viewType) == 'Default Movies View':
            VT = addon.get_setting('default-view4')
        elif addon.get_setting(viewType) == 'Default Docs View':
            VT = addon.get_setting('default-view5')
        elif addon.get_setting(viewType) == 'Default Cartoons View':
            VT = addon.get_setting('default-view6')
        elif addon.get_setting(viewType) == 'Default Anime View':
            VT = addon.get_setting('default-view7')

        print viewType
        print VT
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )

def yt_resolve(url):
    OPEN = Open_Url(url)
    url = re.compile('<iframe.+?src="(.+?)"',re.DOTALL).findall(OPEN)[0]
    url = url[:-6]
    url = url.replace('https://www.youtube.com/embed/','plugin://plugin.video.youtube/play/?video_id=')
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
    
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
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#########################################################
	
if mode == None: Main_menu()
elif mode == 1 : page_content(url)
elif mode == 2 : shows_Menu(url)
elif mode == 5 : studios(url)
elif mode == 6 : charac(url)
elif mode == 7 : toons_only()
elif mode == 100 : resolve(name,url,iconimage,description)
elif mode == 150 : yt_resolve(url)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
