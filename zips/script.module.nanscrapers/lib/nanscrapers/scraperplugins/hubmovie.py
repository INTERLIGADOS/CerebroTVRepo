import re
import requests
import xbmc
import urllib
from ..scraper import Scraper
from ..common import clean_title,clean_search

User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4'


class hubmovie(Scraper):
    domains = ['http://hubmovie.cc']
    name = "Hubmovie"
    sources = []

    def __init__(self):
        self.base_link = 'http://hubmovie.cc'
        self.sources = []

    def scrape_movie(self, title, year, imdb, debrid=False):
        try:
            search_id = clean_search(title.lower())
            start_url = '%s/pages/search/%s' %(self.base_link,search_id.replace(' ','%20'))
            #print 'SEARCH url > '+start_url
            headers = {'User_Agent':User_Agent}
            html = requests.get(start_url,headers=headers,timeout=5).content
            page = html.split('<div id="movies_cont">')[1]
            Regex = re.compile('href="(.+?)".+?<h1>(.+?)</h1>.+?class="poster_tag">(.+?)</li>',re.DOTALL).findall(page)
            for item_url,name,date in Regex:
                if clean_title(title).lower() == clean_title(name).lower():
                    if year in date:
                        movie_link = item_url.replace('.',self.base_link)
                        self.get_source(movie_link)
                
            return self.sources
        except Exception, argument:
            return self.sources

    def scrape_episode(self,title, show_year, year, season, episode, imdb, tvdb, debrid = False):
        try:
            search_id = clean_search(title.lower())
            start_url = '%s/pages/search/%s' %(self.base_link,search_id.replace(' ','%20'))
            #print 'SEARCH url > '+start_url
            headers = {'User_Agent':User_Agent}
            html = requests.get(start_url,headers=headers,timeout=5).content
            page = html.split('<div id="movies_cont">')[1]
            Regex = re.compile('href="(.+?)".+?<h1>(.+?)</h1>',re.DOTALL).findall(page)
            for item_url,name in Regex:
                if clean_title(title).lower() == clean_title(name).lower():
                    movie_link = item_url.replace('.',self.base_link)
                    movie_link = movie_link + '/season-%s-episode-%s' %(season,episode)
                    self.get_source(movie_link)
                
            return self.sources
        except Exception, argument:
            return self.sources

    def get_source(self,movie_link):
        try:
            #print ':::::::::::::::::::::::'+movie_link
            html = requests.get(movie_link).content
            sources = re.compile('<div class="link_go".+?href="(.+?)"',re.DOTALL).findall(html)
            for link in sources:
                if 'openload' in link:
                    headers = {'User_Agent':User_Agent}
                    get_res=requests.get(link,headers=headers,timeout=5).content
                    rez = re.compile('description" content="(.+?)"',re.DOTALL).findall(get_res)[0]
                    if '1080p' in rez:
                        qual = '1080p'
                    elif '720p' in rez:
                        qual='720p'
                    else:
                        qual='DVD'
                else: qual = 'DVD'
                host = link.split('//')[1].replace('www.','')
                host = host.split('/')[0].split('.')[0].title()
                self.sources.append({'source': host,'quality': qual,'scraper': self.name,'url': link,'direct': False})
        except:
            pass
