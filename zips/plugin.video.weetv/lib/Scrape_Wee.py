import xbmc,xbmcgui,xbmcplugin,sys,xbmcaddon
import weescrapers
import process
import re
import os
import datetime
import time
from lib.weeresolver import weeresolver

#import urlresolver

dp =  xbmcgui.DialogProgress()
ADDON = xbmcaddon.Addon(id='plugin.video.weetv')
Hosts = []
hd_list = ['s']
mid_list = ['s']
sd_list = ['s']
fin_list = []
unsorted_list = []
scraper_list =[]
if ADDON.getSetting('vidzi')=='true':Hosts.append('vidzi')
if ADDON.getSetting('thevideo')=='true':Hosts.append('thevideo')
if ADDON.getSetting('gvid')=='true':Hosts.append('gvideo')
if ADDON.getSetting('direct')=='true':Hosts.append('direct')
if ADDON.getSetting('low_return')=='None':
    low_qual = '0'
else:
    low_qual = int(ADDON.getSetting('low_return'))
if ADDON.getSetting('high_return')=='None':
    high_qual = '1080'
else:
    high_qual = int(ADDON.getSetting('high_return'))

def sort_qual(link):
    qual_return = str(link["quality"]).lower().replace('0p','0').replace(' ','')
    if qual_return=='sd': qual_check = '240';qual_letter='i';name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
    elif qual_return=='240': qual_check = '240';qual_letter='i'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
    elif qual_return=='cam': qual_check = '120';qual_letter='j'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
    elif qual_return=='360': qual_check = '360';qual_letter='h'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";sd_list.append('1')
    elif qual_return=='480': qual_check = '480';qual_letter='g'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
    elif qual_return=='560': qual_check = '560';qual_letter='f'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
    elif qual_return=='720': qual_check = '720';qual_letter='e'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";mid_list.append('1')
    elif qual_return=='hd': qual_check = '1080';qual_letter='d'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
    elif qual_return=='dvd': qual_check = '1080';qual_letter='c'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
    elif qual_return=='bluray': qual_check = '1080';qual_letter='b'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
    elif qual_return=='1080': qual_check = '1080';qual_letter='a'; name = link["source"] + " - " + link["scraper"] + " (" + link["quality"] + ")";hd_list.append('1')
    else: qual_check='240';qual_letter='i';name = str(link["source"]) + " - " + str(link["scraper"]) + " (" + str(link["quality"]) + ")";sd_list.append('1')
    unsorted_list.append({'name':name,'quality':qual_check,'letter':qual_letter,'link':link})
    
def return_links(populator):
    weescraper_no = []
    weescraper_folder = xbmc.translatePath('special://home/addons/script.module.weescrapers/lib/weescrapers/scraperplugins/')
    for Root,Dir,Files in os.walk(weescraper_folder):
        for File in Files:
            if File.endswith('.py'):
                if not '__' in File:
                    weescraper_no.append('1')
    result = 0
    #xbmc.log('Weescrape number',xbmc.LOGNOTICE)
 
    for scraper_links in populator():
        scraper_list.append('a')
        if scraper_links != None:
            for link in scraper_links:
                if dp.iscanceled():
                    dp.close()              
                    #return
                    #break
                    continue
                    #pass
                    xbmc.log('cancel scrape1',xbmc.LOGNOTICE)
                fin_list.extend('a')
                dp.update(100/int(len(weescraper_no))*int(len(scraper_list)),'Looking for links, be patient',"Links found: ""HD-"+str(int(len(hd_list)-1))+ " | MD-"+str(int(len(mid_list)-1))+ " | SD-"+str(int(len(sd_list)-1))+'','Scrapers left to run: '+str(int(len(weescraper_no))-int(len(scraper_list)))+' of '+str(len(weescraper_no)))  
 
                #xbmc.log('Response: %s' % weescraper_no ,  xbmc.LOGNOTICE)               
                if dp.iscanceled():
                    dp.close()
                    xbmc.log('cancel scrape222',xbmc.LOGNOTICE)
                    break               
                    #return
                    #pass
                    #continue
                sort_qual(link)
    if len(unsorted_list)>=2:
        sorted_list = sorted(unsorted_list, key = lambda unsorted_link: unsorted_link['letter'])
    else:
        sorted_list = unsorted_list
    if ADDON.getSetting('autoplay')=='true':
        if xbmc.Player().isPlaying()==True:
            xbmc.Player().stop()
            time.sleep(3)
        dp.close()
        count = 0
        if len(sorted_list)==1:
            try:
                for item in sorted_list:
                    qual_check = item['quality']
                    name = item['name']
                    if int(high_qual)>=int(qual_check)>=int(low_qual):
                        playlink = item['link']
                        playlink = playlink['url']
                        xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
                        time.sleep(3)
            except:
                time.sleep(3)
                pass
        else:
            while count<len(sorted_list) and xbmc.Player().isPlaying()!=True:
                count+=1
                try:
                    item = sorted_list[int(count)]
                    playlink = item['link']
                    playlink = playlink['url']
                    qual_check = item['quality']
                    name = item['name']
                    if int(high_qual)>=int(qual_check)>=int(low_qual):
                        if '.mp4' in playlink or '.mkv' in playlink or 'm3u8' in playlink or '=m22' in playlink or '=m18' in playlink or '=m37' in playlink:
                            if not 'openload' in playlink:
                                if not 'embed' in playlink:
                                    if not '.html' in playlink:
                                        try:
                                            xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
                                            time.sleep(3)
                                        except:
                                            time.sleep(3)
                                            #pass
                                            break
                                            
                        else:
                            if not 'openload' in playlink:
                                try:
                                    resolved_link = weeresolver(name,url,return_link=True)
                                    #resolved_link = urlresolver(name,url,return_link=True)
                                except:
                                    resolved_link = 'None'
                                if resolved_link != 'None':
                                    try:
                                        xbmc.Player().play(playlink, xbmcgui.ListItem(item['name']))
                                        time.sleep(3)
                                    except:
                                        time.sleep(3)
                                        #pass
                                        break
                                        
                except:
                    #pass
                    break
                    
    else:
        for item in sorted_list:
            qual_check = item['quality']
            name = item['name']
            link = item['link']
            if int(high_qual)>=int(qual_check)>=int(low_qual):
                process.PLAY(' '+name,str(link['url']),20,'','','','')
            else:
                for host in Hosts:
                    if int(qual_check)<=int(high_qual):
                        if str(host) in str(link["source"].lower().replace(' ','')):
                            process.PLAY(name,str(link['url']),20,'','','','')
                    else:
                        pass
                        #break

def scrape_episode(name,show_year,year,season,episode,imdb):

    process.watched_shows(name,show_year,year,season,episode,imdb)

    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    show_year = show_year.replace('(','').replace(')','').replace(' ','')
    year = re.sub("[^0123456789\.]","",year)
    show_year = re.sub("[^0123456789\.]","",show_year)
    from weescrapers import scrape_episode
    progress = []
    item = []
    dp.create('Searching TV........')
    try:
        populator = scrape_episode(name, show_year, year, season, episode,imdb,'', timeout=20000)
    except:
        return
    return_links(populator)

def scrape_movie(name,year,imdb):

    exclude_scrapers = 'Alluc'

    dp.create('Searching movies.....')
    year = year.replace('(','').replace(')','').replace(' ','').replace('I','')
    year = re.sub("[^0123456789\.]","",year)
    xbmc.log('clean_year:'+year,xbmc.LOGNOTICE)
    xbmc.log('IMDB:'+imdb,xbmc.LOGNOTICE)
    from weescrapers import scrape_movie
    try:
        populator = scrape_movie(name, year, imdb, exclude=exclude_scrapers, timeout=2000)
    except:
        return
    return_links(populator)
 
