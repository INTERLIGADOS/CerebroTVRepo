import xbmc, xbmcaddon, xbmcgui, os, json, requests ,gzip, time, shutil, re, urllib

def SetPVRSetting(PVRFolder):
	try:
		os.makedirs(os.path.join(PVRFolder))
	except:	pass
	
	PVRSetting = {	"epgPath": os.path.join(PVRFolder,"custom.xml"),
					"epgPathType":"0",
					"logoBaseUrl":"https://github.com/Apollo2000/Repo/raw/master/TVLogos/",
					"logoPathType":"1",
					"m3uPath": os.path.join(PVRFolder,"apollo.m3u"),
					"m3uPathType":"0"}
	settingFile = xbmc.translatePath(os.path.join(PVRFolder, 'settings.xml'))
	xml = []
	xml.append("<settings>\n")
	for k, v in PVRSetting.iteritems():
		xml.append('\t<setting id="{0}" value="{1}" />\n'.format(k, v))
	xml.append("</settings>\n")
	outF = open(settingFile, 'wb')
	outF.write("".join(xml))
	outF.close()

def GetPVRAddon():
	PVRAddon = None
	if xbmc.getCondVisibility("System.HasAddon(pvr.iptvsimple)"):
		try:
			PVRAddon = xbmcaddon.Addon("pvr.iptvsimple")
		except:	pass
	return PVRAddon

def GetFile(url,file):
	try:
		os.remove(file)
	except:	pass
	response = requests.get(url, stream=True)
	with open(file, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response

def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def CheckAddonUpdate():
	try:
		folder = xbmc.translatePath(os.path.join('special://home','addons','repository.apollo'))
		if not os.path.isdir(folder):
			os.makedirs(folder)
			xml_file = xbmc.translatePath(os.path.join('special://home','addons','repository.apollo','addon.xml'))
			icon_file = xbmc.translatePath(os.path.join('special://home','addons','repository.apollo','icon.png'))
			urllib.urlretrieve ("https://raw.githubusercontent.com/Apollo2000/Repo/master/repository.apollo/addon.xml", xml_file)
			urllib.urlretrieve ("https://raw.githubusercontent.com/Apollo2000/Repo/master/repository.apollo/icon.png", icon_file)
	except: pass
	
	ApolloAddon = xbmcaddon.Addon("program.apollo")

	if ApolloAddon.getSetting('apollo.first')=="false":
		if ApolloAddon.getSetting('apollo.email')== "":
			i = xbmcgui.Dialog().yesno("Apollo Group","Are you a member ?")
			if i == 1:
				email = xbmcgui.Dialog().input('Enter Member Email', type=xbmcgui.INPUT_ALPHANUM)
				ApolloAddon.setSetting('apollo.email', str(email))
				password = xbmcgui.Dialog().input('Enter Member Password', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
				ApolloAddon.setSetting('apollo.password', str(password))
			else:
				xbmcgui.Dialog().ok('Apollo Group',"Free users have limit access. Get membership at FB @ApolloGroupTV")
		xbmc.sleep(10)

		i = xbmcgui.Dialog().yesno("Apollo Group","Use Apollo TV Guide ?")
		if i == 0:
			ApolloAddon.setSetting('apollo.pvr', "false")
		else:
			ApolloAddon.setSetting('apollo.pvr', "true")
		ApolloAddon.setSetting('apollo.first', "true")
			
	LocalVersion = ApolloAddon.getAddonInfo('version')
	response = requests.get("https://raw.githubusercontent.com/Apollo2000/Repo/master/program.apollo/addon.xml")
	match = re.search (r'version="(\d\.\d\.\d)"', response.text,re.M|re.I)
	if not match:
		return
	RemoteVersion = match.groups()[0]

	STRversion = str(LocalVersion)+"/"+str(RemoteVersion)
	if not ApolloAddon.getSetting('apollo.version')==str(STRversion):
		ApolloAddon.setSetting('apollo.version', str(STRversion))

	if versiontuple(RemoteVersion) > versiontuple(LocalVersion):
		xbmc.executebuiltin('Notification(Apollo Group,"Please wait, Updating Addon to {0}.", 5000,{1})'.format(RemoteVersion,os.path.join(xbmcaddon.Addon("program.apollo").getAddonInfo('path') ,"icon.png")))
		xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
		sys.exit(1)

CheckAddonUpdate()
if xbmcaddon.Addon("program.apollo").getSetting('apollo.pvr')=="false":
	sys.exit(1)

PVRFolder = xbmc.translatePath(os.path.join('special://profile', 'addon_data', 'pvr.iptvsimple'))
PVRAddon = GetPVRAddon()
if not os.path.exists(PVRFolder) or PVRAddon is None:
	SetPVRSetting(PVRFolder)
elif not PVRAddon.getSetting("m3uPath") == os.path.join(PVRFolder,"apollo.m3u"):
	SetPVRSetting(PVRFolder)

GuideFile = xbmc.translatePath(os.path.join(PVRFolder, 'custom.xml'))
M3UFile = xbmc.translatePath(os.path.join(PVRFolder, 'apollo.m3u'))
ApolloAddon = xbmcaddon.Addon("program.apollo")
if not os.path.exists(GuideFile) or not os.path.exists(M3UFile) or (os.stat(GuideFile).st_mtime < (time.time() - 24*60*60)):
	xbmc.executebuiltin('Notification(Apollo Group,"Please wait, loading TV Guide.", 5000,{0})'.format(os.path.join(xbmcaddon.Addon("program.apollo").getAddonInfo('path') ,"icon.png")))
	xmltvGzFile = xbmc.translatePath(os.path.join(PVRFolder, 'guide.xml.gz'))
	try:
		os.remove(xmltvGzFile)
	except:	pass
	GetFile("http://static.apollogroup.tv/guide.xml.gz", xmltvGzFile)
	inF = gzip.open(xmltvGzFile, 'rb')
	outF = open(GuideFile, 'wb')
	outF.write(inF.read())
	inF.close()
	outF.close()
	
	GetFile("http://static.apollogroup.tv/apollo.m3u",M3UFile)

	xbmc.sleep(5)
	xbmc.executebuiltin('StopPVRManager')
	xbmc.executebuiltin('StartPVRManager')

try:
	if not json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.GetAddonDetails","params":{"addonid":"pvr.iptvsimple", "properties": ["enabled"]},"id":1}'))['result']['addon']['enabled']:
		xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}')
		xbmc.sleep(5)
		print "**** Apollo IPTV Simple: Enable"
except:	pass

try:
	if not json.loads(xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.GetSettingValue", "params":{"setting":"pvrmanager.enabled"},"id":1}'))['result']['value']:
		xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}')
		xbmc.sleep(2)
		xbmc.executebuiltin('StopPVRManager')
		xbmc.executebuiltin('StartPVRManager')
		print "**** Apollo PVR Manager: Enable"
		xbmc.Dialog().ok("Apollo Group","Please restart kodi for TV Guide to start")
except:	pass

xbmc.executebuiltin("AlarmClock('ApolloPVR',RunScript(plugin://program.apollo/pvr.py),3600,silent)")