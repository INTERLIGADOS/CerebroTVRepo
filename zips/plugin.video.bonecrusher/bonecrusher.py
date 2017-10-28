# -*- coding: utf-8 -*-
import urlparse , sys
import xbmc , os , zipfile , ntpath , xbmcgui , xbmcaddon , xbmcplugin
import time
oo000 = xbmcgui . Dialog ( )
ii = dict ( urlparse . parse_qsl ( sys . argv [ 2 ] . replace ( '?' , '' ) ) )
if 51 - 51: IiI1i11I
Iii1I1 = ii . get ( 'action' )
if 73 - 73: II1I1iiiiii * ooo0OO / o0OO00 / oo
i1iII1IiiIiI1 = ii . get ( 'name' )
if 40 - 40: ooOoO0O00 * IIiIiII11i
o0oOOo0O0Ooo = ii . get ( 'title' )
if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11i / Ii1I
IiiIII111iI = ii . get ( 'year' )
if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
Oo = ii . get ( 'imdb' )
if 27 - 27: o00 * o00 - IiI1i11I - ooOoO0O00 % II - ooo0OO
iiI1iIiI = ii . get ( 'tvdb' )
if 91 - 91: i1 . IiI1i11I / Ii1I % O00oOoOoO0o0O / i1 - IiI1i11I
II1Iiii1111i = ii . get ( 'tmdb' )
if 25 - 25: O0oo0OO0
oo00000o0 = ii . get ( 'season' )
if 34 - 34: I1i1iI1i % ooOoO0O00 % ooo0OO % I1i1iI1i * Oo0ooO0oo0oO / ii1IiI1i
Iiii = ii . get ( 'episode' )
if 87 - 87: Ii1I / o00 + II - o00 . o00 / ooOoO0O00
iiIIIIi1i1 = ii . get ( 'tvshowtitle' )
if 54 - 54: iii1I1I % II1I1iiiiii + IIiIiII11i - Oo0ooO0oo0oO / O00oOoOoO0o0O
iIiiI1 = ii . get ( 'premiered' )
if 68 - 68: IIiIiII11i - IiI1i11I - i1 / iii1I1I - i1 + oo
IiiIII111ii = ii . get ( 'url' )
if 3 - 3: Oo0ooO0oo0oO + II1I1iiiiii
I1Ii = ii . get ( 'image' )
if 66 - 66: O0oo0OO0
oo0Ooo0 = ii . get ( 'meta' )
if 46 - 46: o00 % o00 - Ii1I * OOooOOo % Oo0ooO0oo0oO
OOooO0OOoo = ii . get ( 'select' )
if 29 - 29: OOooOOo / ooo0OO
IiIIIiI1I1 = ii . get ( 'query' )
if 86 - 86: IiI1i11I + O0oo0OO0 + o00 * O00oOoOoO0o0O + OOooOOo
oOoO = ii . get ( 'source' )
if 68 - 68: ii1IiI1i . Ii1I . IiI1i11I
IIiI = ii . get ( 'content' )
if 22 - 22: o0 % O0oo0OO0
if 84 - 84: IiI1i11I . OOooOOo
if Iii1I1 == None :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . root ( )
 if 100 - 100: O0oo0OO0 - O0oo0OO0 - II
if Iii1I1 == 'docs2navNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . root ( )
 if 20 - 20: o0OO00
if Iii1I1 == 'bioNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . bio ( )
 if 13 - 13: oo - O0oo0OO0 % Ii1I / ooo0OO % Oo0ooO0oo0oO
if Iii1I1 == 'natutredocsNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . natutredocs ( )
 if 97 - 97: IiI1i11I
if Iii1I1 == 'thebibleNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . bible ( )
 if 32 - 32: o0 * II1I1iiiiii % Ii1I % O0oo0OO0 . I1i1iI1i
if Iii1I1 == 'ConspiraciesNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . Conspiracies ( )
 if 61 - 61: o00
if Iii1I1 == 'mentalNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . mental ( )
 if 79 - 79: o0 + IIiIiII11i - Oo0ooO0oo0oO
if Iii1I1 == 'killersNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . killers ( )
 if 83 - 83: o00
if Iii1I1 == 'ufoNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . ufo ( )
 if 64 - 64: i1 % o00 % Oo0ooO0oo0oO / ii1IiI1i - i1
if Iii1I1 == 'mythsNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . myths ( )
 if 74 - 74: Oo0ooO0oo0oO * II1I1iiiiii
if Iii1I1 == 'addictionNavigator' :
 from resources . lib . indexers import docs2nav
 docs2nav . navigator ( ) . addiction ( )
 if 89 - 89: Ii1I + o0
if Iii1I1 == 'kids2Navigator' :
 from resources . lib . indexers import kidsnav
 kidsnav . navigator ( ) . root ( )
 if 3 - 3: oo / IIiIiII11i % O00oOoOoO0o0O * IiI1i11I / II1I1iiiiii * O00oOoOoO0o0O
if Iii1I1 == 'toddlerNavigator' :
 from resources . lib . indexers import kidsnav
 kidsnav . navigator ( ) . toddler ( )
 if 49 - 49: Ii1I % O0oo0OO0 + oo . IIiIiII11i % I11i
if Iii1I1 == 'KidsNavigator' :
 from resources . lib . indexers import kidsnav
 kidsnav . navigator ( ) . Kids ( )
 if 48 - 48: O00oOoOoO0o0O + O00oOoOoO0o0O / ooOoO0O00 / ooo0OO
if Iii1I1 == 'TeenNavigator' :
 from resources . lib . indexers import kidsnav
 kidsnav . navigator ( ) . Teen ( )
 if 20 - 20: OOooOOo
 if 77 - 77: ii1IiI1i / O00oOoOoO0o0O
if Iii1I1 == 'NatureNavigator' :
 from resources . lib . indexers import kidsnav
 kidsnav . navigator ( ) . Nature ( )
 if 98 - 98: ooo0OO / oo / IiI1i11I / OOooOOo
if Iii1I1 == 'classicsNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . root ( )
 if 28 - 28: iii1I1I - I1i1iI1i . I1i1iI1i + ii1IiI1i - o0OO00 + II1I1iiiiii
if Iii1I1 == 'actionNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . action ( )
 if 95 - 95: i1 % Ii1I . II1I1iiiiii
if Iii1I1 == 'adventureNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . adventure ( )
 if 15 - 15: o00 / O0oo0OO0 . O0oo0OO0 - oo
if Iii1I1 == 'animationNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . animation ( )
 if 53 - 53: I1i1iI1i + IIiIiII11i * Ii1I
if Iii1I1 == 'comedyNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . comedy ( )
 if 61 - 61: oo * iii1I1I / o0OO00 . IiI1i11I . ii1IiI1i
if Iii1I1 == 'crimeNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . crime ( )
 if 60 - 60: O00oOoOoO0o0O / O00oOoOoO0o0O
if Iii1I1 == 'dramaNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . drama ( )
 if 46 - 46: O0oo0OO0 * iii1I1I - i1 * Ii1I - II
if Iii1I1 == 'familyNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . family ( )
 if 83 - 83: o0OO00
if Iii1I1 == 'fantasyNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . fantasy ( )
 if 31 - 31: ooOoO0O00 - iii1I1I . II % ii1IiI1i - II1I1iiiiii
if Iii1I1 == 'horrorNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . horror ( )
 if 4 - 4: ooOoO0O00 / o00 . Oo0ooO0oo0oO
if Iii1I1 == 'mysteryNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . mystery ( )
 if 58 - 58: iii1I1I * IiI1i11I / ii1IiI1i % II - I11i / Ii1I
if Iii1I1 == 'romanceNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . romance ( )
 if 50 - 50: IIiIiII11i
if Iii1I1 == 'scifiNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . scifi ( )
 if 34 - 34: IIiIiII11i * ooOoO0O00 % Oo0ooO0oo0oO * ii1IiI1i - IIiIiII11i
if Iii1I1 == 'thrillerNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . thriller ( )
 if 33 - 33: OOooOOo + iii1I1I * i1 - o0 / Ii1I % O0oo0OO0
if Iii1I1 == 'warNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . war ( )
 if 21 - 21: i1 * ooo0OO % Ii1I * oo
if Iii1I1 == 'westernNavigator' :
 from resources . lib . indexers import classicnav
 classicnav . navigator ( ) . western ( )
 if 16 - 16: II1I1iiiiii - II * ooo0OO + Oo0ooO0oo0oO
 if 50 - 50: ooOoO0O00 - o00 * I11i / II + OOooOOo
 if 88 - 88: O0oo0OO0 / II + Oo0ooO0oo0oO - ooOoO0O00 / o00 - ii1IiI1i
if Iii1I1 == 'boxsetsNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . root ( )
 if 15 - 15: I11i + ii1IiI1i - o0OO00 / iii1I1I
elif Iii1I1 == 'actionNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . action ( )
 if 58 - 58: IiI1i11I % O00oOoOoO0o0O
elif Iii1I1 == 'actionliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . action ( lite = True )
 if 71 - 71: iii1I1I + o00 % IiI1i11I + I11i - I1i1iI1i
elif Iii1I1 == 'adventureNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . adventure ( )
 if 88 - 88: ii1IiI1i - i1 % iii1I1I
elif Iii1I1 == 'adventureliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . adventure ( lite = True )
 if 16 - 16: IIiIiII11i * Ii1I % I1i1iI1i
elif Iii1I1 == 'animationNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . animation ( )
 if 86 - 86: IIiIiII11i + O0oo0OO0 % IiI1i11I * Ii1I . o00 * O00oOoOoO0o0O
elif Iii1I1 == 'animationliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . animation ( lite = True )
 if 44 - 44: Ii1I
elif Iii1I1 == 'comedyNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . comedy ( )
 if 88 - 88: II % O0oo0OO0 . ooOoO0O00
elif Iii1I1 == 'comedyliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . comedy ( lite = True )
 if 38 - 38: OOooOOo
elif Iii1I1 == 'crimeNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . crime ( )
 if 57 - 57: II1I1iiiiii / Ii1I * II / ii1IiI1i . ooOoO0O00
elif Iii1I1 == 'crimeliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . crime ( lite = True )
 if 26 - 26: Oo0ooO0oo0oO
elif Iii1I1 == 'dramaNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . drama ( )
 if 91 - 91: i1 . I11i + i1 - Oo0ooO0oo0oO / o0OO00
elif Iii1I1 == 'dramaliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . drama ( lite = True )
 if 39 - 39: I11i / o00 - ooOoO0O00
elif Iii1I1 == 'familyNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . family ( )
 if 98 - 98: I11i / O00oOoOoO0o0O % Ii1I . ii1IiI1i
elif Iii1I1 == 'familyliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . family ( lite = True )
 if 91 - 91: Ii1I % o0
elif Iii1I1 == 'fantasyNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . fantasy ( )
 if 64 - 64: O00oOoOoO0o0O % Oo0ooO0oo0oO - II - Ii1I
elif Iii1I1 == 'fantasyliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . fantasy ( lite = True )
 if 31 - 31: O00oOoOoO0o0O - ooOoO0O00 . O00oOoOoO0o0O
elif Iii1I1 == 'horrorNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . horror ( )
 if 18 - 18: OOooOOo
elif Iii1I1 == 'horrorliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . horror ( lite = True )
 if 98 - 98: Oo0ooO0oo0oO * Oo0ooO0oo0oO / Oo0ooO0oo0oO + O00oOoOoO0o0O
elif Iii1I1 == 'mysteryNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . mystery ( )
 if 34 - 34: o00
elif Iii1I1 == 'mysteryliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . mystery ( lite = True )
 if 15 - 15: O00oOoOoO0o0O * o00 * o0 % IiI1i11I % ii1IiI1i - iii1I1I
elif Iii1I1 == 'romanceNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . romance ( )
 if 68 - 68: II % oo . I1i1iI1i . I11i
elif Iii1I1 == 'romanceliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . romance ( lite = True )
 if 92 - 92: Oo0ooO0oo0oO . II
elif Iii1I1 == 'scifiNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . scifi ( )
 if 31 - 31: II . ii1IiI1i / II1I1iiiiii
elif Iii1I1 == 'scifiliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . scifi ( lite = True )
 if 89 - 89: ii1IiI1i
elif Iii1I1 == 'thrillerNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . thriller ( )
 if 68 - 68: i1 * o0OO00 % II1I1iiiiii + i1 + o00
elif Iii1I1 == 'thrillerliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . thriller ( lite = True )
 if 4 - 4: o00 + II1I1iiiiii * iii1I1I
elif Iii1I1 == 'westernNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . western ( )
 if 55 - 55: o0 + ooo0OO / ii1IiI1i * Ii1I - IiI1i11I - O0oo0OO0
elif Iii1I1 == 'westernliteNavigator' :
 from resources . lib . indexers import bxsets
 bxsets . navigator ( ) . western ( lite = True )
 if 25 - 25: I11i
elif Iii1I1 == 'teamNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . root ( )
 if 7 - 7: oo / IIiIiII11i * II . I1i1iI1i . ooo0OO
elif Iii1I1 == 'ldmovNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . ldmov ( )
 if 13 - 13: iii1I1I / IiI1i11I
elif Iii1I1 == 'EnforcermoNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . Enforcermo ( )
 if 2 - 2: IIiIiII11i / II1I1iiiiii / OOooOOo % ii1IiI1i % O0oo0OO0
elif Iii1I1 == 'warhammermoNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . warhammermo ( )
 if 52 - 52: OOooOOo
elif Iii1I1 == 'katsmoNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . katsmo ( )
 if 95 - 95: O0oo0OO0
elif Iii1I1 == 'stalkermoNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . stalkermo ( )
 if 87 - 87: o00 + ii1IiI1i . iii1I1I + ii1IiI1i
elif Iii1I1 == 'oddsNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . root ( )
 if 91 - 91: II1I1iiiiii
elif Iii1I1 == 'KfulegNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Kfuleg ( )
 if 61 - 61: ooOoO0O00
elif Iii1I1 == 'qocNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . qoc ( )
 if 64 - 64: o00 / ii1IiI1i - II1I1iiiiii - O00oOoOoO0o0O
elif Iii1I1 == 'giftsNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . gifts ( )
 if 86 - 86: O00oOoOoO0o0O % ii1IiI1i / IIiIiII11i / ii1IiI1i
elif Iii1I1 == 'amNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . at ( )
 if 42 - 42: i1
elif Iii1I1 == 'MlNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Tl ( )
 if 67 - 67: II . Oo0ooO0oo0oO . II1I1iiiiii
elif Iii1I1 == 'restNavigator' :
 from resources . lib . indexers import wishes
 wishes . navigator ( ) . rest ( )
 if 10 - 10: I11i % I11i - ooo0OO / iii1I1I + O0oo0OO0
elif Iii1I1 == 'SwmNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Swm ( )
 if 87 - 87: Ii1I * I11i + iii1I1I / ooo0OO / Oo0ooO0oo0oO
elif Iii1I1 == 'ClmNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Clts ( )
 if 37 - 37: Oo0ooO0oo0oO - o00 * Ii1I % IiI1i11I - II
elif Iii1I1 == 'metalNavigator' :
 from resources . lib . indexers import metal
 metal . navigator ( ) . root ( )
 if 83 - 83: O00oOoOoO0o0O / IIiIiII11i
elif Iii1I1 == 'unexplainedNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . unexplained ( )
 if 34 - 34: I1i1iI1i
elif Iii1I1 == 'metal2Navigator' :
 from resources . lib . indexers import metal
 metal . navigator ( ) . metal ( )
 if 57 - 57: Ii1I . O00oOoOoO0o0O . oo
elif Iii1I1 == 'classicNavigator' :
 from resources . lib . indexers import metal
 metal . navigator ( ) . classic ( )
 if 42 - 42: O00oOoOoO0o0O + I11i % II1I1iiiiii
elif Iii1I1 == 'psyNavigator' :
 from resources . lib . indexers import metal
 metal . navigator ( ) . psy ( )
 if 6 - 6: Ii1I
elif Iii1I1 == 'grungeNavigator' :
 from resources . lib . indexers import metal
 metal . navigator ( ) . grunge ( )
 if 68 - 68: ii1IiI1i - i1
elif Iii1I1 == 'UrmNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Urt ( )
 if 28 - 28: i1 . iii1I1I / iii1I1I + o0 . I11i
elif Iii1I1 == 'TmNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Tts ( )
 if 1 - 1: ooo0OO / ooOoO0O00
elif Iii1I1 == 'KzmNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Kzt ( )
 if 33 - 33: O00oOoOoO0o0O
elif Iii1I1 == 'BftvNavigator' :
 from resources . lib . indexers import teamnav
 teamnav . navigator ( ) . Bftv ( )
 if 18 - 18: OOooOOo % Oo0ooO0oo0oO * II1I1iiiiii
elif Iii1I1 == 'KrestsNavigator' :
 from resources . lib . indexers import wishes
 wishes . navigator ( ) . root ( )
 if 87 - 87: IiI1i11I
elif Iii1I1 == 'KrestswNavigator' :
 from resources . lib . indexers import wishes
 wishes . navigator ( ) . krests ( )
 if 93 - 93: I11i - i1 % IiI1i11I . Oo0ooO0oo0oO / Oo0ooO0oo0oO - II
elif Iii1I1 == 'SfimNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Sfts ( )
 if 9 - 9: I11i / o0 - IIiIiII11i / o0OO00 / ooo0OO - OOooOOo
elif Iii1I1 == 'ParamNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Paratv ( )
 if 91 - 91: Oo0ooO0oo0oO % oo % ooo0OO
elif Iii1I1 == 'DocsNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Docstv ( )
 if 20 - 20: iii1I1I % O0oo0OO0 / O0oo0OO0 + O0oo0OO0
elif Iii1I1 == 'BrNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Br ( )
 if 45 - 45: Ii1I - I1i1iI1i - o0OO00 - i1 . ooOoO0O00 / II1I1iiiiii
elif Iii1I1 == 'kocNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . koc ( )
 if 51 - 51: II1I1iiiiii + Oo0ooO0oo0oO
elif Iii1I1 == 'MhNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . Mh ( )
 if 8 - 8: Ii1I * ii1IiI1i - O0oo0OO0 - i1 * iii1I1I % IIiIiII11i
elif Iii1I1 == 'darktvNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . darktv ( )
 if 48 - 48: II1I1iiiiii
elif Iii1I1 == 'firestickNavigator' :
 from resources . lib . indexers import oddsnends
 oddsnends . navigator ( ) . firestick ( )
 if 11 - 11: O00oOoOoO0o0O + o0OO00 - i1 / OOooOOo + o0 . ooOoO0O00
elif Iii1I1 == 'movieNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . movies ( )
 if 41 - 41: O0oo0OO0 - II1I1iiiiii - II1I1iiiiii
elif Iii1I1 == 'ShowChangelog' :
 from resources . lib . modules import changelog
 changelog . get ( )
 if 68 - 68: iii1I1I % II
elif Iii1I1 == 'movieliteNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . movies ( lite = True )
 if 88 - 88: ooo0OO - o00 + iii1I1I
elif Iii1I1 == 'pairNavigator' :
 from resources . lib . modules import control
 control . openSettings ( id = 'script.triangulum.pair' )
 if 40 - 40: IIiIiII11i * O0oo0OO0 + iii1I1I % Oo0ooO0oo0oO
 if 74 - 74: Ii1I - o0 + o0OO00 + II / ii1IiI1i
elif Iii1I1 == 'mymovieNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mymovies ( )
 if 23 - 23: II1I1iiiiii
elif Iii1I1 == 'mymovieliteNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mymovies ( lite = True )
 if 85 - 85: O0oo0OO0
elif Iii1I1 == 'tvNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . tvshows ( )
 if 84 - 84: IIiIiII11i . ooo0OO % o0OO00 + O0oo0OO0 % o0OO00 % i1
elif Iii1I1 == 'tvliteNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . tvshows ( lite = True )
 if 42 - 42: i1 / O00oOoOoO0o0O / OOooOOo + Oo0ooO0oo0oO / ii1IiI1i
elif Iii1I1 == 'mytvNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mytvshows ( )
 if 84 - 84: o00 * ooOoO0O00 + o0
elif Iii1I1 == 'mytvliteNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mytvshows ( lite = True )
 if 53 - 53: Oo0ooO0oo0oO % ooOoO0O00 . I1i1iI1i - ooo0OO - I1i1iI1i * ooOoO0O00
elif Iii1I1 == 'downloadNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . downloads ( )
 if 77 - 77: ooo0OO * i1
elif Iii1I1 == 'toolNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . tools ( )
 if 95 - 95: IIiIiII11i + IiI1i11I
elif Iii1I1 == 'searchNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . search ( )
 if 6 - 6: o00 / IiI1i11I + Oo0ooO0oo0oO * Ii1I
elif Iii1I1 == 'viewsNavigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . views ( )
 if 80 - 80: ooOoO0O00
elif Iii1I1 == 'clearCache' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . clearCache ( )
 if 83 - 83: O00oOoOoO0o0O . IiI1i11I + ooOoO0O00 . OOooOOo * O00oOoOoO0o0O
elif Iii1I1 == 'movies' :
 from resources . lib . indexers import movies
 movies . movies ( ) . get ( IiiIII111ii )
 if 53 - 53: ooOoO0O00
elif Iii1I1 == 'similar_movies' :
 from resources . lib . indexers import movies
 movies . movies ( ) . similar_movies ( Oo )
 if 31 - 31: i1
elif Iii1I1 == 'get_similar_movies' :
 from resources . lib . indexers import movies
 movies . movies ( ) . get_similar_movies ( Oo )
 if 80 - 80: II . IiI1i11I - OOooOOo
elif Iii1I1 == 'movies2' :
 from resources . lib . indexers import movies2
 movies2 . movies ( ) . get ( IiiIII111ii )
 if 25 - 25: i1
elif Iii1I1 == 'movies' :
 from resources . lib . indexers import movies
 movies . movies ( ) . get ( IiiIII111ii )
 if 62 - 62: iii1I1I + II1I1iiiiii
elif Iii1I1 == 'moviePage' :
 from resources . lib . indexers import movies
 movies . movies ( ) . get ( IiiIII111ii )
 if 98 - 98: OOooOOo
elif Iii1I1 == 'movieWidget' :
 from resources . lib . indexers import movies
 movies . movies ( ) . widget ( )
 if 51 - 51: o0 - Ii1I + ooOoO0O00 * O0oo0OO0 . O00oOoOoO0o0O + Ii1I
elif Iii1I1 == 'movieSearch' :
 from resources . lib . indexers import movies
 movies . movies ( ) . search ( IiIIIiI1I1 )
 if 78 - 78: IiI1i11I / Oo0ooO0oo0oO - O0oo0OO0 / iii1I1I + Ii1I
elif Iii1I1 == 'moviePerson' :
 from resources . lib . indexers import movies
 movies . movies ( ) . person ( IiIIIiI1I1 )
 if 82 - 82: O0oo0OO0
elif Iii1I1 == 'movieGenres' :
 from resources . lib . indexers import movies
 movies . movies ( ) . genres ( )
 if 46 - 46: o0OO00 . IiI1i11I
elif Iii1I1 == 'movieLanguages' :
 from resources . lib . indexers import movies
 movies . movies ( ) . languages ( )
 if 94 - 94: OOooOOo * O0oo0OO0 / o0 / O0oo0OO0
elif Iii1I1 == 'movieCertificates' :
 from resources . lib . indexers import movies
 movies . movies ( ) . certifications ( )
 if 87 - 87: o0 . I1i1iI1i
elif Iii1I1 == 'movieYears' :
 from resources . lib . indexers import movies
 movies . movies ( ) . years ( )
 if 75 - 75: o00 + ii1IiI1i + OOooOOo * O00oOoOoO0o0O % Ii1I . Oo0ooO0oo0oO
elif Iii1I1 == 'moviePersons' :
 from resources . lib . indexers import movies
 movies . movies ( ) . persons ( )
 if 55 - 55: iii1I1I . IIiIiII11i
elif Iii1I1 == 'movieUserlists' :
 from resources . lib . indexers import movies
 movies . movies ( ) . userlists ( )
 if 61 - 61: o0 % I1i1iI1i . o0
elif Iii1I1 == 'channels' :
 from resources . lib . indexers import channels
 channels . channels ( ) . get ( )
 if 100 - 100: II * II1I1iiiiii
elif Iii1I1 == 'tvshows' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . get ( IiiIII111ii )
 if 64 - 64: iii1I1I % ooo0OO * Ii1I
elif Iii1I1 == 'similar_shows' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . similar_shows ( Oo )
 if 79 - 79: II1I1iiiiii
elif Iii1I1 == 'get_similar_shows' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . get_similar_shows ( Oo )
 if 78 - 78: I11i + iii1I1I - II
elif Iii1I1 == 'tvshowPage' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . get ( IiiIII111ii )
 if 38 - 38: OOooOOo - Ii1I + ooo0OO / ii1IiI1i % o0
elif Iii1I1 == 'tvSearch' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . search ( )
 if 57 - 57: i1 / o00
elif Iii1I1 == 'tvPerson' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . person ( )
 if 29 - 29: ooo0OO + ii1IiI1i * i1 * iii1I1I . IIiIiII11i * IIiIiII11i
elif Iii1I1 == 'tvGenres' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . genres ( )
 if 7 - 7: I1i1iI1i * II % O0oo0OO0 - OOooOOo
elif Iii1I1 == 'tvNetworks' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . networks ( )
 if 13 - 13: O0oo0OO0 . IiI1i11I
elif Iii1I1 == 'tvCertificates' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . certifications ( )
 if 56 - 56: I11i % II1I1iiiiii - IIiIiII11i
elif Iii1I1 == 'tvPersons' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . persons ( IiiIII111ii )
 if 100 - 100: O0oo0OO0 - II1I1iiiiii % Ii1I * iii1I1I + IIiIiII11i
elif Iii1I1 == 'tvUserlists' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . userlists ( )
 if 88 - 88: o0OO00 - i1 * II1I1iiiiii * o0OO00 . o0OO00
elif Iii1I1 == 'seasons' :
 from resources . lib . indexers import episodes
 episodes . seasons ( ) . get ( iiIIIIi1i1 , IiiIII111iI , Oo , iiI1iIiI )
 if 33 - 33: II + Oo0ooO0oo0oO * Ii1I / ooo0OO - IIiIiII11i
elif Iii1I1 == 'episodes' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . get ( iiIIIIi1i1 , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii )
 if 54 - 54: II / iii1I1I . Ii1I % Oo0ooO0oo0oO
elif Iii1I1 == 'calendar' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . calendar ( IiiIII111ii )
 if 57 - 57: IiI1i11I . I11i - O0oo0OO0 - Ii1I + ii1IiI1i
elif Iii1I1 == 'tvWidget' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . widget ( )
 if 63 - 63: ii1IiI1i * Oo0ooO0oo0oO
elif Iii1I1 == 'calendars' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . calendars ( )
 if 69 - 69: II1I1iiiiii . i1
elif Iii1I1 == 'episodeUserlists' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . userlists ( )
 if 49 - 49: IIiIiII11i - O00oOoOoO0o0O
elif Iii1I1 == 'refresh' :
 from resources . lib . modules import control
 control . refresh ( )
 if 74 - 74: ooo0OO * I11i + ii1IiI1i / oo / ooOoO0O00 . o0
elif Iii1I1 == 'queueItem' :
 from resources . lib . modules import control
 control . queueItem ( )
 if 62 - 62: o0OO00 * IIiIiII11i
elif Iii1I1 == 'openSettings' :
 from resources . lib . modules import control
 control . openSettings ( IiIIIiI1I1 )
 if 58 - 58: ii1IiI1i % OOooOOo
elif Iii1I1 == 'artwork' :
 from resources . lib . modules import control
 control . artwork ( )
 if 50 - 50: II . OOooOOo
elif Iii1I1 == 'addView' :
 from resources . lib . modules import views
 views . addView ( IIiI )
 if 97 - 97: II1I1iiiiii + ii1IiI1i
elif Iii1I1 == 'moviePlaycount' :
 from resources . lib . modules import playcount
 playcount . movies ( Oo , IiIIIiI1I1 )
 if 89 - 89: OOooOOo + i1 * O00oOoOoO0o0O * O0oo0OO0
elif Iii1I1 == 'episodePlaycount' :
 from resources . lib . modules import playcount
 playcount . episodes ( Oo , iiI1iIiI , oo00000o0 , Iiii , IiIIIiI1I1 )
 if 37 - 37: o0OO00 - II1I1iiiiii - OOooOOo
elif Iii1I1 == 'tvPlaycount' :
 from resources . lib . modules import playcount
 playcount . tvshows ( i1iII1IiiIiI1 , Oo , iiI1iIiI , oo00000o0 , IiIIIiI1I1 )
 if 77 - 77: iii1I1I * ooo0OO
elif Iii1I1 == 'tvPlaycountShow' :
 from resources . lib . modules import playcount
 playcount . marktvshows ( i1iII1IiiIiI1 , Oo , iiI1iIiI , IiIIIiI1I1 )
 if 98 - 98: IIiIiII11i % O0oo0OO0 * o0OO00
elif Iii1I1 == 'trailer' :
 from resources . lib . modules import trailer
 trailer . trailer ( ) . play ( i1iII1IiiIiI1 , IiiIII111ii )
 if 51 - 51: ooo0OO . ii1IiI1i / Ii1I + OOooOOo
elif Iii1I1 == 'traktManager' :
 from resources . lib . modules import trakt
 trakt . manager ( i1iII1IiiIiI1 , Oo , iiI1iIiI , IIiI )
 if 33 - 33: o00 . ooOoO0O00 % Oo0ooO0oo0oO + OOooOOo
elif Iii1I1 == 'authTrakt' :
 from resources . lib . modules import trakt
 trakt . authTrakt ( )
 if 71 - 71: o0 % iii1I1I
elif Iii1I1 == 'rdAuthorize' :
 from resources . lib . modules import debrid
 debrid . rdAuthorize ( )
 if 98 - 98: O00oOoOoO0o0O % IiI1i11I % o00 + O0oo0OO0
elif Iii1I1 == 'download' :
 import json
 from resources . lib . sources import sources
 from resources . lib . modules import downloader
 try : downloader . download ( i1iII1IiiIiI1 , I1Ii , sources ( ) . sourcesResolve ( json . loads ( oOoO ) [ 0 ] , True ) )
 except : pass
 if 78 - 78: I11i % Ii1I / Oo0ooO0oo0oO - ooo0OO
elif Iii1I1 == 'play' :
 from resources . lib . modules import control
 OOooO0OOoo = control . setting ( 'hosts.mode' )
 if OOooO0OOoo == '3' and 'plugin' in control . infoLabel ( 'Container.PluginName' ) :
  from resources . lib . sources import sources
  sources ( ) . play_dialog ( o0oOOo0O0Ooo , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii , iiIIIIi1i1 , iIiiI1 , oo0Ooo0 , OOooO0OOoo )
 elif OOooO0OOoo == '4' and 'plugin' in control . infoLabel ( 'Container.PluginName' ) :
  from resources . lib . sources import sources
  sources ( ) . play_dialog_list ( o0oOOo0O0Ooo , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii , iiIIIIi1i1 , iIiiI1 , oo0Ooo0 , OOooO0OOoo )
 else :
  from resources . lib . sources import sources
  sources ( ) . play ( o0oOOo0O0Ooo , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii , iiIIIIi1i1 , iIiiI1 , oo0Ooo0 , OOooO0OOoo )
  if 69 - 69: II
elif Iii1I1 == 'play_alter' :
 from resources . lib . sources import sources
 sources ( ) . play_alter ( o0oOOo0O0Ooo , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii , iiIIIIi1i1 , iIiiI1 , oo0Ooo0 )
 if 11 - 11: IIiIiII11i
elif Iii1I1 == 'play_library' :
 from resources . lib . sources import sources
 sources ( ) . play_library ( o0oOOo0O0Ooo , IiiIII111iI , Oo , iiI1iIiI , oo00000o0 , Iiii , iiIIIIi1i1 , iIiiI1 , oo0Ooo0 , OOooO0OOoo )
 if 16 - 16: O0oo0OO0 + I1i1iI1i * II1I1iiiiii % oo . IIiIiII11i
elif Iii1I1 == 'addItem' :
 from resources . lib . sources import sources
 sources ( ) . addItem ( o0oOOo0O0Ooo )
 if 67 - 67: o0OO00 / IIiIiII11i * O0oo0OO0 + O00oOoOoO0o0O
elif Iii1I1 == 'movieFavourites' :
 from resources . lib . indexers import movies
 movies . movies ( ) . favourites ( )
 if 65 - 65: o0OO00 - I11i / o00 / ooOoO0O00 / oo
elif Iii1I1 == 'movieProgress' :
 from resources . lib . indexers import movies
 movies . movies ( ) . in_progress ( )
 if 71 - 71: II + O0oo0OO0
elif Iii1I1 == 'showsProgress' :
 from resources . lib . indexers import episodes
 episodes . episodes ( ) . in_progress ( )
 if 28 - 28: iii1I1I
elif Iii1I1 == 'deleteProgress' :
 from resources . lib . modules import favourites
 favourites . deleteProgress ( oo0Ooo0 , IIiI )
 if 38 - 38: o00 % ooOoO0O00 % O00oOoOoO0o0O / i1 + ii1IiI1i / oo
elif Iii1I1 == 'tvFavourites' :
 from resources . lib . indexers import tvshows
 tvshows . tvshows ( ) . favourites ( )
 if 54 - 54: ooo0OO % I11i - iii1I1I / Ii1I - i1 . O00oOoOoO0o0O
elif Iii1I1 == 'addFavourite' :
 from resources . lib . modules import favourites
 favourites . addFavourite ( oo0Ooo0 , IIiI )
 if 11 - 11: I11i . i1 * I1i1iI1i * o0OO00 + o00
elif Iii1I1 == 'deleteFavourite' :
 from resources . lib . modules import favourites
 favourites . deleteFavourite ( oo0Ooo0 , IIiI )
elif Iii1I1 == 'playItem' :
 from resources . lib . sources import sources
 sources ( ) . playItem ( o0oOOo0O0Ooo , oOoO )
 if 33 - 33: II1I1iiiiii * OOooOOo - II % II
elif Iii1I1 == 'alterSources' :
 from resources . lib . sources import sources
 sources ( ) . alterSources ( IiiIII111ii , oo0Ooo0 )
 if 18 - 18: II / o0 * II + II * IiI1i11I * I11i
elif Iii1I1 == 'clearSources' :
 from resources . lib . sources import sources
 sources ( ) . clearSources ( )
 if 11 - 11: o00 / ii1IiI1i - I1i1iI1i * o0OO00 + o0OO00 . ii1IiI1i
elif Iii1I1 == 'clearProgress' :
 from resources . lib . modules import control
 import os , xbmc , xbmcaddon , xbmcgui
 oo000 = xbmcgui . Dialog ( )
 i1I1i111Ii = xbmcaddon . Addon ( ) . getAddonInfo
 ooo = xbmc . translatePath ( i1I1i111Ii ( 'profile' ) ) . decode ( 'utf-8' )
 i1i1iI1iiiI = os . path . join ( ooo , 'favourites.db' )
 Ooo0oOooo0 = os . path . join ( ooo , 'progress.db' )
 oOOOoo00 = control . yesnoDialog ( control . lang ( 32056 ) . encode ( 'utf-8' ) , '' , '' )
 if oOOOoo00 :
  try :
   os . remove ( Ooo0oOooo0 )
   oo000 . ok ( 'Clear Progress' , 'Clear Progress Complete' , '' , '' )
  except :
   oo000 . ok ( 'Clear Progress' , 'There was an error Deleting the Database' , '' , '' )
   if 9 - 9: II1I1iiiiii % II1I1iiiiii - OOooOOo
   if 51 - 51: IIiIiII11i . ooo0OO - I11i / II1I1iiiiii
elif Iii1I1 == 'urlresolversettings' :
 import urlresolver
 urlresolver . display_settings ( )
 if 52 - 52: OOooOOo + II1I1iiiiii + Oo0ooO0oo0oO + o0 % Oo0ooO0oo0oO
elif Iii1I1 == 'movieToLibrary' :
 from resources . lib . sources import sources
 sources ( ) . movieToLibrary ( o0oOOo0O0Ooo , IiiIII111iI , Oo , oo0Ooo0 )
 if 75 - 75: IIiIiII11i . o00 . II1I1iiiiii * II
elif Iii1I1 == 'backupwatchlist' :
 import xbmc , os , zipfile , ntpath , xbmcgui
 from resources . lib . modules import control
 oo000 = xbmcgui . Dialog ( )
 i11II1I11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.chaostheroy' , '' ) )
 if os . path . exists ( os . path . join ( i11II1I11I1 , 'favourites.db' ) ) :
  OOoOO0ooo = control . setting ( 'remote_path' )
  if not OOoOO0ooo == '' :
   II1iIi11 = xbmc . translatePath ( os . path . join ( 'special://' , 'home/userdata/addon_data/' ) )
   I11iiii = len ( i11II1I11I1 )
   O0 = xbmc . translatePath ( os . path . join ( OOoOO0ooo , 'chaos theroy_watchlist.zip' ) )
   i1iI = zipfile . ZipFile ( O0 , 'w' , zipfile . ZIP_DEFLATED )
   IiI1iiiIii = os . path . join ( i11II1I11I1 , 'favourites.db' )
   i1iI . write ( IiI1iiiIii , IiI1iiiIii [ I11iiii : ] )
   oo000 . ok ( 'Backup Watchlist' , 'Backup complete' , '' , '' )
  else :
   oo000 . ok ( 'Backup Watchlist' , 'No backup location found: Please setup your Backup location in the addon settings' , '' , '' )
   xbmc . executebuiltin ( 'RunPlugin(%s?action=openSettings&query=5.0)' % sys . argv [ 0 ] )
   if 7 - 7: II * i1 - o00 + iii1I1I * IIiIiII11i % i1
elif Iii1I1 == 'restorewatchlist' :
 import xbmc , os , zipfile , ntpath , xbmcgui
 from resources . lib . modules import control
 oo000 = xbmcgui . Dialog ( )
 i11II1I11I1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.chaostheroy' , '' ) )
 if os . path . exists ( i11II1I11I1 ) :
  iI1i111I1Ii = control . setting ( 'remote_restore_path' )
  if not iI1i111I1Ii == '' :
   with zipfile . ZipFile ( iI1i111I1Ii , "r" ) as i11i1ii1I :
    i11i1ii1I . extractall ( i11II1I11I1 )
    oo000 . ok ( 'Restore Watchlist' , 'Restore complete' , '' , '' )
  else :
   oo000 . ok ( 'Restore Watchlist' , 'No item found: Please select your zipfile location in the addon settings' , '' , '' )
   xbmc . executebuiltin ( 'RunPlugin(%s?action=openSettings&query=5.0)' % sys . argv [ 0 ] )
   if 88 - 88: O00oOoOoO0o0O % I11i
elif Iii1I1 == 'movielist' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mymovies ( )
 if 48 - 48: o00 / II . ooo0OO * ii1IiI1i * Ii1I / oo
elif Iii1I1 == 'tvlist' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . mytv ( )
 if 92 - 92: o0 % o0 - OOooOOo / ii1IiI1i
elif Iii1I1 == 'lists_navigator' :
 from resources . lib . indexers import navigator
 navigator . navigator ( ) . lists_navigator ( )
 if 10 - 10: Oo0ooO0oo0oO + o0 * I11i + ooo0OO / II / I11i
 if 42 - 42: IIiIiII11i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3

