#!/usr/bin/env
# Scot Carpenter
# CIS 343 Fall 2017
#
# Game holds the player and neighborhood
# Gets input and produces output
import neighborhood
import player

class Game:

	# Game constructor
	def __init__(self):
		self.neighborhood = neighborhood.Neighborhood()
		self.player = player.Player()
		self.gameOver = False

	# is the game finished?
	def isWon(self):
		return self.gameOver

	# prints the board info
	def printBoard(self):
		self.neighborhood.printBoard()

	# gets input from user
	def getDirection(self):

		# print board
		self.printBoard()
		print("Player Location:" + str(self.player.getX()) + "," + str(self.player.getY()))
		print("\n")

		# Get input direction
		print("Input Direction (up/down/left/right)  or exit")
		direction = input("Input Direction:")

		# clear screen
		print("\033c")

		# move up
		if direction == "up":
			if(self.player.getY() <= 0):
				return
			self.player.moveUp()
			self.player.fight(self.neighborhood.getMonsters(self.player.getX(),self.player.getY()))

		# move down
		elif direction == "down":
			if(self.player.getY() >= self.neighborhood.getHeight()-1):
				return
			self.player.moveDown()
			self.player.fight(self.neighborhood.getMonsters(self.player.getX(),self.player.getY()))

		# move left
		elif direction == "left":
			if(self.player.getX() <= 0):
				return
			self.player.moveLeft()
			self.player.fight(self.neighborhood.getMonsters(self.player.getX(),self.player.getY()))

		# move right
		elif direction == "right":
			if(self.player.getX() >= self.neighborhood.getWidth()-1):
				return;
			self.player.moveRight()
			self.player.fight(self.neighborhood.getMonsters(self.player.getX(),self.player.getY()))

		# exit
		elif direction == "exit":
			self.gameOver = True

		# other input
		else:
			print("Input Error")

# main entry point
def main():
	
	# clear screen
	print("\033c")
	
	# instantiate game
	game = Game()

	# while game isnt finished keep playing
	while (not game.isWon()):
		game.getDirection()


main()
