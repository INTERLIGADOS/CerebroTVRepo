import time
import base64
import md5

################################################################################
#  Constant Definitions
################################################################################

TOKEN_KEY = "65rSwUzRad"
USER_AGENT = "Mozilla%2F5.0%20%28Linux%3B%20Android%205.1.1%3B%20Nexus%205%20Build%2FLMY48B%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F43.0.2357.65%20Mobile%20Safari%2F537.36"
LINK_WRAPPER = "http://{0}/p2p/{1}?st={2}&e={3}|User-Agent={4}&referer={5}"
MIRROR_LIST = [
    "185.102.219.72",
    "185.102.219.67",
    "185.102.218.56",
    "185.102.219.139",
    "185.59.221.157",
]

################################################################################
#  Function Definitions
################################################################################


def linkifyMobdro(mopidy, mirror_index=0):
    url = str(mopidy).replace("mpd://", "")
    time_stamp = str(int(time.time()) + 14400)
    to_hash = "{0}{1}/hls/{2}".format(TOKEN_KEY, time_stamp, url)
    token_hash = base64.b64encode(md5.new(to_hash).digest()).replace("+", "-").replace("/", "_").replace("=", "")
    mirror = MIRROR_LIST[mirror_index]
    result = LINK_WRAPPER.format(mirror, url, token_hash, time_stamp, USER_AGENT, "mobdro.me")

    return result
