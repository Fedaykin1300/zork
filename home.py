# Scot Carpenter
# CIS 343 Fall 2017
#
# Home contains random number of monsters
import monsters
import random

class Home:

	# create random number of random monsters
	def __init__(self):
		self.num_monsters = random.randrange(3,7)
		self.monsters = [monsters.getRandomMonster() for i in range(self.num_monsters)]
		for mon in self.monsters:
			mon.add_observer(self)

	# return number of monsters in house
	def getNum(self):
		return len(self.monsters)

	# monster calls update when it dies
	# this function removes it from list
	def update(self,mon):
		print("Monster Died")
		self.monsters.remove(mon)

	# returns list of monsters
	def getMonsters(self):
		return self.monsters
