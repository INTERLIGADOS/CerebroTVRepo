# -*- coding: UTF-8 -*-
#/*  ==== Author :: _beastMaster [ SweetWork Copyright (C) 2017 ] ==============
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# *  ===========================================================================
# *  
# */
import sys

from resources.lib.common import control

from resources.lib.common.utils import XbmcUtil

################################################################################
#  Constant Definitions
################################################################################

log = XbmcUtil.getLogger()

ADDON_ID = "plugin.video.mobdina"

################################################################################
#  Class Definitions ('Enum' analogs)
################################################################################

class Assets:

    THUMBNAIL  = "https://i.imgur.com/Xgwlhrq.png"
    FANART     = "https://i.imgur.com/85YjsJw.jpg"

class Param:
    """  Parameter labels for plugin querystring 
    """
    ACTION     = "action"
    QUERY      = "query"
    URL        = "url"

class Action:
    """  Parameter arguments for plugin querystring 
    """
    MAINMENU   = None
    BROWSE     = "index"                                                        
    SEARCH     = "search"                                                        # NOT IMPLEMENTED
    PLAY       = "play"                                                        
    SETTINGS   = "settings"                                                      # TESTING
    CLEARCACHE = "clearCache"                                                    # TESTING

class Error:

    UNKNOWN_ACTION   = 100
    MISSING_PARAM    = 200
    INVALID_XML      = 300
    HTTP_REQUEST     = 400
    # ILLEGAL_ARGUMENT = 500
    NO_RESULTS       = 600

    @staticmethod
    def text(errCode):
        try:
            return {
                Error.UNKNOWN_ACTION: "unknown argument",
                Error.MISSING_PARAM: "missing argument",
                Error.INVALID_XML: "malformed/unreadable xml",
                Error.HTTP_REQUEST: "couldn't connect to server",
                # Error.ILLEGAL_ARGUMENT: "illegal mobdro-api call",
                Error.NO_RESULTS: "no valid items found",
            }[int(errCode)]
        except: return "SwampError: {}".format(errCode)

    
################################################################################
#  Function Definitions
################################################################################


def swampError(tag, errCode, message="", fatal=True):
    log("{_tag}/ {_err}: {_msg}".format(
            _tag=tag, 
            _err=Error.text(errCode), 
            _msg=message
        ), level=XbmcUtil.LOGERROR
    )
    if fatal: sys.exit(errCode)
    return errCode
