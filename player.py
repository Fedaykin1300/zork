# Scot Carpenter
# CIS 343 Fall 2017
#
# Player contains location and weapons
import weapons
import random

class Player:

	# Default Constructor
	# sets location and weapons
	def __init__(self):
		self.x = 0
		self.y = 0
		self.hp = random.random() * 25 + 100
		self.attack_value = random.random() * 10 + 10
		self.weapons = [weapons.getRandomWeapon() for i in range(10)] 

	# move player up
	def moveUp(self):
		self.y = self.y - 1
	
	# move player down
	def moveDown(self):
		self.y = self.y + 1

	# move player left
	def moveLeft(self):
		self.x = self.x - 1

	# move player rgiht
	def moveRight(self):
		self.x = self.x + 1

	# returns x coordinate
	def getX(self):
		return self.x

	# returns y coordinate
	def getY(self):
		return self.y

	# returns list of weapons
	def getWeapons(self):
		return self.weapons

	# player fights monsters
	def fight(self,monsters=[]):
		# print info
		print("__________")
		print("Fighting Monsters")
		for mon in monsters:
			mon.printInfo()
		
		for mon in monsters:
			mon.dead()

		print("\n\n")
		print("__________")
