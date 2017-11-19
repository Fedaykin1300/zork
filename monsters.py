# Scot Carpenter
# CIS 343 Fall 2017
#
# Monsters contains the implementation
# and inheritance of monster class

import random

class Monster:

	# Inititlizes name, hp, and attack dmd
	def __init__(self,nm,hitpoints,attack):
		self.name = nm
		self.hitpoints = hitpoints
		self.attack = attack

	# sets the house observer
	def add_observer(self,house):
		self.observer = house

	# prints the monster info
	def printInfo(self):
		print(self.name,end=" ")
		print("HP: ",end="")
		print(self.hitpoints,end=" ")
		print("DMG: ",end="")
		print(self.attack)

	# update observer when dies
	def dead(self):	
		self.observer.update(self)	

# Person Class
class Person(Monster):

	def __init__(self):
		super().__init__("Person",100,-1)

# Zombie Class
class Zombie(Monster):
	
	def __init__(self):
		super().__init__("Zombie",random.randrange(50,100),random.randrange(0,10))

# Vampire Class
class Vampire(Monster):

	def __init__(self):
		super().__init__("Vampire",random.randrange(100,200),random.randrange(10,20))

# Ghoul Class
class Ghoul(Monster):

	def __init__(self):
		super().__init__("Ghoul",random.randrange(40,80),random.randrange(15,30))

# Werewolf class
class Werewolf(Monster):

	def __init__(self):
		super().__init__("Werewolf",200,random.randrange(0,40))

# This function returns a random
# Monster that's not a person
def getRandomMonster():
	randnum = random.randrange(0,4)
	
	if randnum == 0:
		return Zombie()
	if randnum == 1:
		return Vampire()
	if randnum == 2:
		return Ghoul()
	if randnum == 3:
		return Werewolf()
