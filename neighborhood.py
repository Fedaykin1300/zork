# Scot Carpenter
# CIS 343 Fall 2017
#
# Neighborhood holds all the houses
import home

class Neighborhood:

	# initializes the 4x4 house grid
	def __init__(self):
		self.width = 4
		self.height = 4
		self.houses = [[home.Home() for i in range(self.height)] for j in range(self.width)]

	# prints the neighborhood with the number
	# of monsters in each house
	def printBoard(self):
		print("_______________________")
		print("    Neighborhood")
		print("\n")
		for i in range(self.height):
			print("\t",end="")
			for j in range(self.width):
				print(self.houses[j][i].getNum(),end="")
			print()
		print("_______________________")
		print("\n")
		print("Number Monsters Left:",self.numberEnemy())
		print("\n")

	# returns the number of monsters left alive
	def numberEnemy(self):
		sum = 0
		for i in range(self.height):
			for j in range(self.width):
				sum = sum + self.houses[j][i].getNum()
		return sum

	# returns width of neighborhood
	def getWidth(self):
		return self.width

	# returns height of neighborhood
	def getHeight(self):
		return self.height

	# returns list of monsters at location
	def getMonsters(self,x,y):
		return self.houses[x][y].getMonsters()
