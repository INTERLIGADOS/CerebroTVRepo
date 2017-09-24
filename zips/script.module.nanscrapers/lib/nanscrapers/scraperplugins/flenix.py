import re
import requests
import xbmc
import urllib
from ..scraper import Scraper

requests.packages.urllib3.disable_warnings()

s = requests.session()
User_Agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

class flenix(Scraper):
    domains = ['https://flenix.net']
    name = "Flenix"
    sources = []

    def __init__(self):
        self.base_link = 'https://flenix.net/'
        self.sources = []

    def scrape_movie(self, title, year, imdb, debrid=False):
        try:
            search_id = urllib.quote_plus(title.lower())
            movie_url = '%s/index.php?do=search&story=%s' %(self.base_link,search_id.replace(' ','+'))
            headers = {'User_Agent':User_Agent}
            link = requests.get(movie_url,headers=headers,verify=False,timeout=5).content
            results = re.compile('class="leftInfo".+?href="(.+?)">(.+?)</a></div>.+?Year:</li>.+?<li>(.+?)</li>',re.DOTALL).findall(link)
            for url,link_title,date in results:
                if title.lower() in link_title.lower():
                    if date in year:
                        ID = url.split('movies/')[1].split('-')[0]
                        headers = {'User-Agent': User_Agent}
                        page = requests.get(url,headers=headers,allow_redirects=False,timeout=5)
                        COOKIE = page.headers['Set-Cookie']
                        #print 'my cookie'+COOKIE

                        headers = {'Origin':'flenix.net', 'Referer':url,'Cookie':COOKIE,
                                   'X-Requested-With':'XMLHttpRequest', 'User_Agent':User_Agent}

                        req_url = 'https://flenix.net/?do=player_ajax&id=%s&xfn=player2' %ID
                        
                        end_url = requests.post(req_url, headers=headers).content
                        link = end_url
                        self.sources.append({'source': 'DirectLink','quality': '720P','scraper': self.name,'url': link,'direct': True})
            return self.sources
        except Exception, argument:
            return self.sources


