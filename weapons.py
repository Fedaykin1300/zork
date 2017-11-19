# Scot Carpenter
# CIS 343 Fall 2017
#
# Weapon Implementation
import random

class Weapon:
	
	# Default Constructor
	def __init__(self,name,attackMod,uses):
		self.name = name;
		self.attack_modifier = attackMod
		self.uses = uses

# HersheyKiss weapon
class HershyKisses(Weapon):

	def __init__(self):
		super().__init__("Kisses",1,100000)

# SourStraw weapon
class SourStraws(Weapon):

	def __init__(self):
		super().__init__("Sour",(random.random()*0.75) + 1,2)

# ChocolateBars weapon
class ChocolateBars(Weapon):

	def __init__(self):
		super().__init__("Bars",(random.random()*0.4)+2,4)

# NerdBomb weapon
class NerdBombs(Weapon):

	def __init__(self):
		super().__init__("Nerd",random.random()*1.5 + 3,1)

# returns random weapon
def getRandomWeapon():
	randnum = random.randrange(0,4)
	if randnum == 0:
		return HershyKisses()
	if randnum == 1:
		return SourStraws()
	if randnum == 2:
		return ChocolateBars()
	if randnum == 3:
		return NerdBombs()
