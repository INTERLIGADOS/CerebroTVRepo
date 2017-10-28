# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
inprogress_db = control.setting('inprogress_db')

sysaddon = sys.argv[0]

syshandle = int(sys.argv[1])

artPath = control.artPath()

addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

	

class navigator:
    def root(self):
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Action', 'actionNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Adventure', 'adventureNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Animation', 'animationNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Comedy', 'comedyNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Crime', 'crimeNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Drama', 'dramaNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Family', 'familyNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fantasy', 'fantasyNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Horror', 'horrorNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mystery', 'mysteryNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Romance', 'romanceNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sci-Fi', 'scifiNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Thriller', 'thrillerNavigator', 'decepticons.png', 'decepticons.png')
#        self.addDirectoryItem('War', 'warNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Western', 'westernNavigator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem(32008, 'toolNavigator', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32010, 'movieSearch', 'decepticons.png', 'decepticons.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	
    def action(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('300', 'movies2&url=tmdb300', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Avengers', 'movies2&url=tmdbavengers', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Batman', 'movies2&url=tmdbbatman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Best Of The Best', 'movies2&url=tmdbbob', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bloodsport', 'movies2&url=tmdbblood', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Bourne', 'movies2&url=tmdbbourne', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Die Hard', 'movies2&url=tmdbdie', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Hot Shots', 'movies2&url=tmdbhot', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Ip Man', 'movies2&url=tmdbipman', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Iron Fists', 'movies2&url=tmdbironfists', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jackass', 'movies2&url=tmdbjackass', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kick-Ass', 'movies2&url=tmdbkick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kickboxer', 'movies2&url=tmdbkickboxer', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Matrix', 'movies2&url=tmdbmatrix', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Never Back Down', 'movies2&url=tmdbnever', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Olympus Has Fallen', 'movies2&url=tmdbolympus', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Smokey and The Bandit', 'movies2&url=tmdbsmokey', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Taken', 'movies2&url=tmdbtaken', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Terminator', 'movies2&url=tmdbterminator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Under Siege', 'movies2&url=tmdbunder', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'decepticons.png', 'decepticons.png')


        self.endDirectory()

    def adventure(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Austin Powers', 'movies2&url=tmdbaustin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Batman', 'movies2&url=tmdbbatman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Conan', 'movies2&url=tmdbconan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Crocodile Dundee', 'movies2&url=tmdbcroc', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Harold and Kumar', 'movies2&url=tmdbharold', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Hobbit', 'movies2&url=tmdbhobbit', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lady and The Tramp', 'movies2&url=tmdblady', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Planet of The Apes', 'movies2&url=tmdbplanet', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def animation(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Charlottes Web', 'movies2&url=tmdbcharlottes', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lady and The Tramp', 'movies2&url=tmdblady', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'decepticons.png', 'decepticons.png')	
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Reef', 'movies2&url=tmdbreef', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Thomas & Friends', 'movies2&url=tmdbthomas', 'decepticons.png', 'decepticons.png')
		
        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Wallace & Gromit', 'movies2&url=tmdbwallace', 'decepticons.png', 'decepticons.png')
		
		
		
		
		

        self.endDirectory()
		
    def comedy(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('A Haunted House', 'movies2&url=tmdbhaunted', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ace Ventura', 'movies2&url=tmdbace', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Adams Family', 'movies2&url=tmdbadams', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('American Pie', 'movies2&url=tmdbampie', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Anchorman', 'movies2&url=tmdbanchor', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Austin Powers', 'movies2&url=tmdbaustin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Neighbors', 'movies2&url=tmdbbn', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Barbershop', 'movies2&url=tmdbbarber', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'movies2&url=tmdbbestexotic', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bridget Jones', 'movies2&url=tmdbbridget', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('City Slickers', 'movies2&url=tmdbcity', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Clerks', 'movies2&url=tmdbclerks', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Crocodile Dundee', 'movies2&url=tmdbcroc', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Daddy Daycare', 'movies2&url=tmdbdaddy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Diary of A Wimpy Kid', 'movies2&url=tmdbdiary', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Dumb and Dumber', 'movies2&url=tmdbdumb', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Friday', 'movies2&url=tmdbfriday', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Grown Ups', 'movies2&url=tmdbgrown', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Hangover', 'movies2&url=tmdbhangover', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Harold and Kumar', 'movies2&url=tmdbharold', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Home Alone', 'movies2&url=tmdbhome', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Horrible Bosses', 'movies2&url=tmdbhorrible', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hot Shots', 'movies2&url=tmdbhot', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Hot Tub Time Machine', 'movies2&url=tmdbhotub', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Inbetweeners', 'movies2&url=tmdbinbetweeners', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Jackass', 'movies2&url=tmdbjackass', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kick-Ass', 'movies2&url=tmdbkick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Legally Blonde', 'movies2&url=tmdblegally', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Major League', 'movies2&url=tmdbmajor', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Meet The Parents', 'movies2&url=tmdbmeet', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Naked Gun', 'movies2&url=tmdbnaked', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Pitch Perfect', 'movies2&url=tmdbpitch', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Police Academy', 'movies2&url=tmdbpolice', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Problem Child', 'movies2&url=tmdbproblem', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Scary Movie', 'movies2&url=tmdbscary', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Smokey and The Bandit', 'movies2&url=tmdbsmokey', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Ted', 'movies2&url=tmdbted', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Teen Wolf', 'movies2&url=tmdbteen', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Tremors', 'movies2&url=tmdbtremors', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Waynes World', 'movies2&url=tmdbwayne', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Whole Nine Yards', 'movies2&url=tmdbwholenine', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Zoolander', 'movies2&url=tmdbzoo', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def crime(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Godfather', 'movies2&url=tmdbgodfather', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Green Street Hooligans', 'movies2&url=tmdbgreen', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Horrible Bosses', 'movies2&url=tmdbhorrible', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Naked Gun', 'movies2&url=tmdbnaked', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Oceans', 'movies2&url=tmdboceans', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Once Were Warriors', 'movies2&url=tmdbonce', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'movies2&url=tmdbrise', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sin City', 'movies2&url=tmdbsin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Step Up', 'movies2&url=tmdbstepup', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Whole Nine Yards', 'movies2&url=tmdbwholenine', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def drama(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Barbershop', 'movies2&url=tmdbbarber', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Before', 'movies2&url=tmdbbefore', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'movies2&url=tmdbbestexotic', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Best Of The Best', 'movies2&url=tmdbbob', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bloodsport', 'movies2&url=tmdbblood', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dirty Dancing', 'movies2&url=tmdbdirtyd', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dolphin Tale', 'movies2&url=tmdbdolphin', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Friday', 'movies2&url=tmdbfriday', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Godfather', 'movies2&url=tmdbgodfather', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Green Street Hooligans', 'movies2&url=tmdbgreen', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ip Man', 'movies2&url=tmdbipman', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Never Back Down', 'movies2&url=tmdbnever', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Nymphomaniac', 'movies2&url=tmdbnymph', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Once Were Warriors', 'movies2&url=tmdbonce', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'movies2&url=tmdbrise', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rocky', 'movies2&url=tmdbrocky', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Step Up', 'movies2&url=tmdbstepup', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'decepticons.png', 'decepticons.png')


        self.endDirectory()

    def family(self, lite=False):
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Charlottes Web', 'movies2&url=tmdbcharlottes', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Daddy Daycare', 'movies2&url=tmdbdaddy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Diary of A Wimpy Kid', 'movies2&url=tmdbdiary', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Dolphin Tale', 'movies2&url=tmdbdolphin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Flintstones', 'movies2&url=tmdbflintstones', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Home Alone', 'movies2&url=tmdbhome', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'decepticons.png', 'decepticons.png')	

        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Problem Child', 'movies2&url=tmdbproblem', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Reef', 'movies2&url=tmdbreef', 'decepticons.png', 'decepticons.png')
	
        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'decepticons.png', 'decepticons.png')
	
        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Thomas & Friends', 'movies2&url=tmdbthomas', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'decepticons.png', 'decepticons.png')
		
	
        self.endDirectory()
		
    def fantasy(self, lite=False):
        self.addDirectoryItem('300', 'movies2&url=tmdb300', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('A Haunted House', 'movies2&url=tmdbhaunted', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Adams Family', 'movies2&url=tmdbadams', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Conan', 'movies2&url=tmdbconan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'dolittle.jpg', 'decepticons.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Flintstones', 'movies2&url=tmdbflintstones', 'decepticons.png', 'decepticons.png')		

        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Hobbit', 'movies2&url=tmdbhobbit', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'decepticons.png', 'decepticons.png')	

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ted', 'movies2&url=tmdbted', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Teen Wolf', 'movies2&url=tmdbteen', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'decepticons.png', 'decepticons.png')

        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def horror(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('A Nightmare on Elm Street', 'movies2&url=tmdbelmst', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Alien', 'movies2&url=tmdbalien', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Childs Play', 'movies2&url=tmdbchilds', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Evil Dead', 'movies2&url=tmdbevil', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Exorcist', 'movies2&url=tmdbexorcist', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Final Destination', 'movies2&url=tmdbfinal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Halloween', 'movies2&url=tmdbhalloween', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hellraiser', 'movies2&url=tmdbhell', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Hills Have Eyes', 'movies2&url=tmdbhills', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hostel', 'movies2&url=tmdbhostel', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Human Centipede', 'movies2&url=tmdbhuman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Omen', 'movies2&url=tmdbomen', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Ring', 'movies2&url=tmdbring', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Scream', 'movies2&url=tmdbscream', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Texas Chainsaw Massacre', 'movies2&url=tmdbtexas', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Tremors', 'movies2&url=tmdbtremors', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('VHS', 'movies2&url=tmdbvhs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Wrong Turn', 'movies2&url=tmdbwrong', 'decepticons.png', 'decepticons.png')		


        self.endDirectory()
		
    def mystery(self, lite=False):
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Ring', 'movies2&url=tmdbring', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Scream', 'movies2&url=tmdbscream', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def romance(self, lite=False):
        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Before', 'movies2&url=tmdbbefore', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bridget Jones', 'movies2&url=tmdbbridget', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Dirty Dancing', 'movies2&url=tmdbdirtyd', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Legally Blonde', 'movies2&url=tmdblegally', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Meet The Parents', 'movies2&url=tmdbmeet', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Think Like a Man', 'movies2&url=tmdbthink', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def scifi(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Alien', 'movies2&url=tmdbalien', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Avengers', 'movies2&url=tmdbavengers', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Butterfly Effect', 'movies2&url=tmdbbutterfly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cocoon', 'movies2&url=tmdbcocoon', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hot Tub Time Machine', 'movies2&url=tmdbhotub', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Matrix', 'movies2&url=tmdbmatrix', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Planet of The Apes', 'movies2&url=tmdbplanet', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Terminator', 'movies2&url=tmdbterminator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'decepticons.png', 'decepticons.png')		


        self.endDirectory()
		
    def thriller(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Bourne', 'movies2&url=tmdbbourne', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('The Butterfly Effect', 'movies2&url=tmdbbutterfly', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Childs Play', 'movies2&url=tmdbchilds', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'crank.jpg', 'decepticons.png')
        self.addDirectoryItem('Die Hard', 'movies2&url=tmdbdie', 'die.jpg', 'decepticons.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Halloween', 'movies2&url=tmdbhalloween', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hellraiser', 'movies2&url=tmdbhell', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Hills Have Eyes', 'movies2&url=tmdbhills', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kickboxer', 'movies2&url=tmdbkickboxer', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Oceans', 'movies2&url=tmdboceans', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Olympus Has Fallen', 'movies2&url=tmdbolympus', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sin City', 'movies2&url=tmdbsin', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Taken', 'movies2&url=tmdbtaken', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Under Siege', 'movies2&url=tmdbunder', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'decepticons.png', 'decepticons.png')		
        self.addDirectoryItem('VHS', 'movies2&url=tmdbvhs', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'decepticons.png', 'decepticons.png')		
        

        self.endDirectory()



    def Clts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]More To Come[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('canada loves tv shows', 'tvshows&url=tmdbClts', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Canada loves movies', 'movies2&url=tmdbClm', 'decepticons.png', 'decepticons.png')


        self.endDirectory()

    def Urt(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Users requests tv ', 'tvshows&url=tmdbUrt', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Users requests movies', 'movies2&url=tmdbUrm', 'decepticons.png', 'decepticons.png')



        self.endDirectory()


    def Tts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Toddler tv shows', 'tvshows&url=tmdbTts', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Toddler movies', 'movies2&url=tmdbTm', 'decepticons.png', 'decepticons.png')



        self.endDirectory()

    def Kzt(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kids zone tv', 'tvshows&url=tmdbKzt', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Kids Zone Movies', 'movies2&url=tmdbKzm', 'decepticons.png', 'decepticons.png')



        self.endDirectory()

    def Bftv(self, lite=False):
        self.addDirectoryItem('bone crushers fav tv shows', 'tvshows&url=tmdbBft', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('bone crushers fav', 'movies2&url=tmdbbcfm', 'decepticons.png', 'decepticons.png')



        self.endDirectory()
		
    def Docstv(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('documentary tv', 'tvshows&url=tmdbDocstv', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('documentary movies', 'movies2&url=tmdbDocs', 'decepticons.png', 'decepticons.png')



        self.endDirectory()
		
    def at(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('anime tv', 'tvshows&url=tmdbat', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Anime movies', 'movies2&url=tmdbam', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def Tl(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Tv legends', 'tvshows&url=tmdbTl', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Movie legends ', 'movies2&url=tmdbMl', 'decepticons.png', 'decepticons.png')



        self.endDirectory()
		
    def Sfts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sci fi tv shows', 'tvshowstvshows&url=tmdbSfts', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Sci fi movies', 'movies2&url=tmdbSfim', 'decepticons.png', 'decepticons.png')


        self.endDirectory()

    def Paratv(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem(' paranormal tv', 'tvshows&url=tmdbParamtv', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('paranormal Movies', 'movies2&url=tmdbParam', 'decepticons.png', 'decepticons.png')



        self.endDirectory()

    def Kfuleg(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jet Li', 'movies2&url=tmdbjli', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Chuck Norris', 'movies2&url=tmdbchuck', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jackie Chan', 'movies2&url=tmdbchan', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Jean Claude Van Damme', 'movies2&url=tmdbtmdbdam', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Steven Seagal', 'movies2&url=tmdbsegal', 'decepticons.png', 'decepticons.png')


        self.endDirectory()


		
    def Br(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('B rated', 'movies2&url=tmdbBr', 'decepticons.png', 'decepticons.png')


        self.endDirectory()
		
    def Mh(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Morbid minded movies', 'movies2&url=tmdbMh', 'decepticons.png', 'decepticons.png')



        self.endDirectory()
		

    def ldmov(self, lite=False):
        self.addDirectoryItem('LockDown movies', 'movies2&url=tmdbldmov', 'lock.png', 'decepticons.png')
        self.addDirectoryItem('LockDown Tv Shows', 'tvshows&url=tmdbldtv', 'lock.png', 'decepticons.png')

        self.endDirectory()

    def Enforcermo(self, lite=False):
        self.addDirectoryItem('Enforcer movies', 'movies2&url=tmdbenmov', 'ENFORCER.png', 'decepticons.png')
        self.addDirectoryItem('Enforcer Tv Shows', 'tvshows&url=tmdbentv', 'ENFORCER.png', 'decepticons.png')

        self.endDirectory()

    def warhammermo(self, lite=False):
        self.addDirectoryItem('Warhammer movies', 'movies2&url=tmdbwarm', 'WAR.png', 'decepticons.png')
        self.addDirectoryItem('Warhammer Tv Shows', 'tvshows&url=tmdbwartv', 'WAR.png', 'decepticons.png')

        self.endDirectory()


    def katsmo(self, lite=False):
        self.addDirectoryItem('Kastastrophy movies', 'movies2&url=tmdbkatsmov', 'kat.png', 'decepticons.png')
        self.addDirectoryItem('Kastastrophy Tv Shows', 'tvshows&url=tmdbkatstv', 'kat.png', 'decepticons.png')

        self.endDirectory()

    def stalkermo(self, lite=False):
        self.addDirectoryItem('Stalkers movies', 'movies2&url=tmdbstalkermov', 'stalker.png', 'decepticons.png')
        self.addDirectoryItem('Stalkers Tv Shows', 'tvshows&url=tmdbstalkertv', 'stalker.png', 'decepticons.png')

        self.endDirectory()
    def Swm(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Hockey movies', 'movies2&url=tmdbSwm', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Baseball movies', 'movies2&url=tmdbBaseball', 'decepticons.png', 'decepticons.png')  
        self.addDirectoryItem('Soccer movies', 'movies2&url=tmdbSoccer', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Football movies', 'movies2&url=tmdbFootball', 'decepticons.png', 'decepticons.png')
        self.addDirectoryItem('Basketball movies', 'movies2&url=tmdbBasketball', 'decepticons.png', 'decepticons.png')
        self.endDirectory()

    def western(self, lite=False):
        self.addDirectoryItem('The Man With No Name', 'movies2&url=tmdbnoman', 'decepticons.png', 'decepticons.png')		


        self.endDirectory()



        
        
		
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'urlresolversettings', 'decepticons.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=4.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=6.0', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Views', 'viewsNavigator', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Providers', 'clearSources', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Cache', 'clearCache', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'decepticons.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Progress Database', 'clearProgress', 'decepticons.png', 'DefaultAddonProgram.png')

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'decepticons.png', 'decepticons.png', isAction=False)
        self.endDirectory()



    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import cache
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.directory(syshandle, cacheToDisc=True)


