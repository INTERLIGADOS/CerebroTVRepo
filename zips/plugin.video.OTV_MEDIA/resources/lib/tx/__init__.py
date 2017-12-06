from ..tw_util import __TW_VER__ as twisted_version
if twisted_version > (13, 0, 0):
    from twisted.web import client
    from twisted.internet import endpoints
if twisted_version >= (11, 1, 0):
    from . import client, endpoints
else:
    raise Exception('HTTP1.1 not supported')

Agent = client.Agent
ProxyAgent = client.ProxyAgent
ResponseDone = client.ResponseDone
ResponseFailed = client.ResponseFailed
HTTPConnectionPool = client.HTTPConnectionPool
TCP4ClientEndpoint = endpoints.TCP4ClientEndpoint
