#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m,url = ''):
    from resources.lib.modules import cache,client,workers
    import re,urllib,xbmc,xbmcgui
    def kboard():
        w = xbmcgui.Window(10000) ; p = 'plugin.video.phstreams.regex.search'
        t = xbmc.getInfoLabel('listitem.label')
        if t == '': return w.getProperty(p)
        k = xbmc.Keyboard('', t) ; k.doModal()
        q = k.getText() if k.isConfirmed() else None
        if (q == None or q == ''): return
        w.setProperty(p, q) ; return q
    class page:
        def run(self, r):
            threads = [] ; self.r = [] ; r = [(r.index(i)+1, i) for i in r]
            for i in r: threads.append(workers.Thread(self.request, i))
            [i.start() for i in threads] ; [i.join() for i in threads]
            return ''.join([str(i[1]) for i in sorted(self.r, key=lambda x: x[0])])
        def request(self, i):
            self.r += [(i[0], client.request(i[1]))]
    q = kboard()
    if q == None: return
    url = 'http://moviego.net/search-movies/%s/page-' % urllib.quote_plus(q)
    u = []
    for i in range(1, 3): u += [url + str(i) + '.html']
    u = cache.get(page().run, 24, u)
    e = re.findall('(?s)ml-item">.+?f="([^"]*).+?<i>([^<]*).+?se:\s([^<]*).+?">.+?c="([^"]*)', u)
    return e