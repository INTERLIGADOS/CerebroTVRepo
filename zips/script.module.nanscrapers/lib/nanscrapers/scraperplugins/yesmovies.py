import re
import requests
import xbmc
from ..scraper import Scraper

class Yesmovies(Scraper):
    domains = ['yesmovies.to']
    name = "yesmovies"
    sources = []

    def __init__(self):
        self.base_link = 'https://yesmovies.to'
        self.search_link = '/search/'


    def scrape_episode(self, title, show_year, year, season, episode, imdb, tvdb, debrid = False):
        try:
            start_url = self.base_link+self.search_link+title.replace(' ','+')+'.html'
            html = requests.get(start_url).content
            match = re.compile('<div class="ml-item">.+?<a href="(.+?)".+?title="(.+?)"',re.DOTALL).findall(html)
            for url,name in match:
                if title.lower().replace(' ','') in name.lower().replace(' ',''):
                    if title.lower()[0] == name.lower()[0]:
                        if 'Season '+season in name:
                            html2 = requests.get(url).content
                            match2 = re.findall('favorite\((.+?),',html2)[0]
                            get_ep = requests.get('https://yesmovies.to/ajax/v4_movie_episodes/'+match2).content
                            print 'https://yesmovies.to/ajax/v4_movie_episodes/'+match2
                            block = re.compile('<ul id=.+?"episodes-sv-6(.+?)"(.+?)ul>',re.DOTALL).findall(get_ep)
                            for c,u in block:
                                if '9' in c:
                                    pass
                                else:
                                    m = re.compile('<li class=.+?"ep-item .+?".+?data-server=.+?"(.+?)" data-id=.+?"(.+?)".+?title=.+?"(.+?)">',re.DOTALL).findall(str(u))
                                    for s,i,t in m:
                                        ep = re.findall('Episode (.+?):',str(t))[0]
                                        if len(episode) == 1:
                                            episode = '0'+episode
                                        if episode == ep:
                                            self.get_ep_source(i.replace('\\',''),match2)                        
                            block = re.compile('<ul id=.+?"episodes-sv-7(.+?)"(.+?)ul>',re.DOTALL).findall(get_ep)
                            for c,u in block:
                                if '9' in c:
                                    pass
                                else:
                                    m = re.compile('<li class=.+?"ep-item .+?".+?data-server=.+?"(.+?)" data-id=.+?"(.+?)".+?title=.+?"(.+?)">',re.DOTALL).findall(str(u))
                                    for s,i,t in m:
                                        ep = re.findall('Episode (.+?):',str(t))[0]
                                        if len(episode) == 1:
                                            episode = '0'+episode
                                        if episode == ep:
                                            self.get_ep_source(i.replace('\\',''),match2)                        
            return self.sources
                                        
        except:
            pass
            return []                           

    def scrape_movie(self, title, year, imdb, debrid = False):
        try:
            start_url = self.base_link+self.search_link+title.replace(' ','+')+'.html'
            html = requests.get(start_url).content
            match = re.compile('<div class="ml-item">.+?<a href="(.+?)".+?title="(.+?)"',re.DOTALL).findall(html)
            for url,name in match:
                if title.lower().replace(' ','').replace(':','') in name.lower().replace(' ','').replace(':',''):
                    if title.lower()[0] == name.lower()[0]:
                        if '(' in name:
                            if year in name:
                                self.get_movie_source(url)
                        elif name.replace(' ','').lower()[-1]==title.replace(' ','').lower()[-1]:
                            print url
                            self.get_movie_source(url)
                        elif name.lower().replace(' ','') == title.replace(' ','').lower():
                            self.get_movie_source(url)
                        else:
                            pass
                        
                        
            return self.sources
        except:
            pass
            return[]

    def get_ep_source(self,m,match):
        try:
            url = 'https://yesmovies.to/ajax/movie_token?eid='+m+'&mid='+match
            html3 = requests.get(url).content
            x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
            fin_url = 'https://yesmovies.to/ajax/movie_sources/'+m+'?x='+x+'&y='+y
            h = requests.get(fin_url).content
            source = re.findall('"sources":\[(.+?)\]',h)
            single = re.findall('{(.+?)}',str(source))
            for s in single:
                playlink = re.findall('"file":"(.+?)"',str(s))
                try:
                    qual = re.findall('"label":"(.+?)"',str(s))[0]
                except:
                    qual = 'SD'
                for p in playlink:
                    p = p.replace('\\','')
                    if 'lemon' in p:
                        p = p+'|User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0&Host=streaming.lemonstream.me:1443&Referer=https://yesmovies.to'
                    if 'http' in p:
                        self.sources.append({'source': 'Gvideo', 'quality': qual, 'scraper': self.name, 'url': p,'direct': True})
        except:
            pass

    def get_movie_source(self,link):
        try:
            qual = 'SD'
            html = requests.get(link).content
            match = re.findall('favorite\((.+?),',html)[0]
            second_url = 'https://yesmovies.to/ajax/v4_movie_episodes/'+match
            html2 = requests.get(second_url).content
            match2 = re.compile('data-id=.+?"(.+?)\"').findall(html2)
            for m in match2:
                print m
                m = m.replace('\\','')
                if len(m)==6 or len(m)==7:
                    url = 'https://yesmovies.to/ajax/movie_token?eid='+m+'&mid='+match
                    html3 = requests.get(url).content
                    x,y = re.findall("_x='(.+?)', _y='(.+?)'",html3)[0]
                    fin_url = 'https://yesmovies.to/ajax/movie_sources/'+m+'?x='+x+'&y='+y
                    print fin_url
                    print 'https://yesmovies.to/ajax/movie_sources/1049195?x=93f5a3754170b19c615e9815ddcfa538&y=777190237a834b35d1611ddf9f978df2'
                    h = requests.get(fin_url).content
                    source = re.findall('"sources":\[(.+?)\]',h)
                    single = re.findall('{(.+?)}',str(source))
                    for s in single:
                        playlink = re.findall('"file":"(.+?)"',str(s))
                        q = re.compile('"label":"(.+?)"').findall(str(s))
                        for h in q:
                            qual = h
                        for p in playlink:
                            p = p.replace('\\','')
                            if 'lemon' in p:
                                p = p+'|User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0&Host=streaming.lemonstream.me:1443&Referer=https://yesmovies.to'
                            if 'http' in p:
                                self.sources.append({'source': 'Gvideo', 'quality': qual, 'scraper': self.name, 'url': p,'direct': True})
        except:
            pass

#Yesmovies().scrape_movie('baywatch','2017','')
#Yesmovies().scrape_episode('game of thrones', '', '', '7', '7', '', '')
