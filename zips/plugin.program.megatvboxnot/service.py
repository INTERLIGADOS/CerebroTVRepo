import xbmc,string,logging,array
import common as Common #from common import * #import common
## ################################################## ##
## ################################################## ##
# temp fix to stop twitter search error
import xbmcaddon
import xbmc

## Start of program
TypeOfMessage="t"; (NewImage,NewMessage)=Common.FetchNews(); 
Common.CheckNews(TypeOfMessage,NewImage,NewMessage,True); 
## ################################################## ##
## ################################################## ##
