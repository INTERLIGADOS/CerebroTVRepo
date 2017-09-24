import re
import requests
from ..scraper import Scraper
import xbmc
from nanscrapers.modules import cfscrape

class Dizi720(Scraper):
    name = "dizi720p"
    domains = ['dizi720p.co/']
    sources = []

    def __init__(self):
        self.base_link = 'http://www.dizi720p.co/'
        self.scraper = cfscrape.create_scraper()

    def scrape_episode(self, title, show_year, year, season, episode, imdb, tvdb, debrid = False):
        try:
            start_url = self.base_link+title.replace(' ','-')+'-'+season+'-sezon-'+episode+'-bolum-izle.html'
            html = self.scraper.get(start_url).content
            block = re.compile('<ul class="dropdown-menu" role="menu">(.+?)</ul></div><div class="pull-right">',re.DOTALL).findall(html)
            for Block in block:
                print('12345')
            match = re.compile('<iframe src="(.+?)"').findall(html)
            for frame in match:
                if not '.html' in frame:
                    #print(frame)
                    if 'watchserieshd.xyz' in frame:
                        html2 = self.scraper.get(frame).content
                        match2 = re.compile('file: "(.+?)",.+?label":"(.+?)"',re.DOTALL).findall(html2)
                        for url,p in match2:
                            self.sources.append({'source': 'Watch Series', 'quality': 'p', 'scraper': self.name, 'url': url,'direct': False})
                    if '.ru' in frame:
                        if 'videoembed' in frame:
                            self.sources.append({'source': 'ok.ru', 'quality': 'SD', 'scraper': self.name, 'url': 'https:'+frame,'direct': False})
                    if 'streamango' in frame:
                        html4 = self.scraper.get(frame).content
                        match4 = re.compile('type:"video/mp4",src:"(.+?)"').findall(html4)
                        for link3 in match4:
                            link3 = 'https:'+link3
                            self.sources.append({'source': 'streamango' , 'quality': 'SD', 'scraper' : self.name, 'url' : link3, 'direct': False})
                match_multi = re.compile('<a href="(.+?)">(.+?)</a>').findall(str(Block))
                for page,name in match_multi:
                    if not 'http' in name:
                        if '.ru' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                if not '.html' in frame:
                                    if name.lower() in frame:
                                        self.sources.append({'source': 'ok.ru', 'quality': 'SD', 'scraper': self.name, 'url': 'https:'+frame,'direct': False})
                        elif 'Mango' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                html4 = self.scraper.get(frame).content
                                match4 = re.compile('type:"video/mp4",src:"(.+?)"').findall(html4)
                                for link3 in match4:
                                    link3 = 'https:'+link3
                                    self.sources.append({'source': 'streamango' , 'quality': 'SD', 'scraper' : self.name, 'url' : link3, 'direct': False})
                        elif 'Raptu' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                html4 = self.scraper.get(frame).content
                                match2 = re.compile('"sources"(.+?)"logo"').findall(html4)
                                for block in match2:
                                    match3 = re.compile('"https:(.+?)"').findall(str(block))
                                    for link3 in match3:
                                        link3 = 'https:'+link3.replace('\/\/','//').replace('\/','/')
                                        self.sources.append({'source': 'Raptu' , 'quality': 'SD', 'scraper' : self.name, 'url' : link3, 'direct': False})

                        elif 'Openload' in name:
                            pass
                        elif 'UpTo' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                if not '.html' in frame:
                                    if name.lower() in frame:
                                        self.sources.append({'source': 'uptovideo', 'quality': 'SD', 'scraper': self.name, 'url': frame,'direct': False})
                        elif 'TheVideo' in name:
                            pass
                        elif 'eStream' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                if not '.html' in frame:
                                    if name.lower() in frame:
                                        self.sources.append({'source': 'estream', 'quality': 'SD', 'scraper': self.name, 'url': frame,'direct': False})
                            match2 = re.compile('<IFRAME.+?SRC="(.+?)"').findall(html3)
                            for frame in match2:
                                if name.lower() in frame:
                                    Html = self.scraper.get(frame).content
                                    estr = re.compile('<source src="(.+?)"',re.DOTALL).findall(Html)
                                    for frame in estr:
                                        self.sources.append({'source': 'estream', 'quality': 'SD', 'scraper': self.name, 'url': frame,'direct': False})
                        elif 'Rapid' in name:
                            pass
                        elif 'ingilizce' in name:
                            pass
                        elif 'fragman' in name:
                            pass
                        elif 'Videomega' in name:
                            pass
                        elif 'VK' in name:
                            html3 = self.scraper.get(page).content
                            match = re.compile('<iframe.+?src="(.+?)"').findall(html3)
                            for frame in match:
                                if not '.html' in frame:
                                    if name.lower() in frame:
                                        self.sources.append({'source': 'vk', 'quality': 'SD', 'scraper': self.name, 'url': frame,'direct': False})
                            match2 = re.compile('<IFRAME.+?SRC="(.+?)"').findall(html3)
                            for frame in match2:
                                if name.lower() in frame:
                                    self.sources.append({'source': 'vk', 'quality': 'SD', 'scraper': self.name, 'url': frame,'direct': False})                            
                        else:
                            print( 'NO LIKEY: '+name)



            return self.sources
        except:
            pass
            return []


             

