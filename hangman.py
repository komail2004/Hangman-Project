import pygame
import math
import random
import time

# Function to get random line from a inputted text file.
# Input should be the path to a file. Output will be a random line from that file as a string.
def getText(fileName):
	with open(fileName, 'r') as file:
		lines = file.readlines()
		randomLine = random.choice(lines)

	return randomLine.replace('\n', '')

#Coordinates
x=800
y=600
# hangma = 
# Classes
class player:
	def __init__(self, image, x,y):
		# self.image = hangman
		self.x = x
		self.y = y


# Create graphical window for game.
def hangMan():
	#Define window.
	# Add the player (class).
	# Add the promp.
	# Display guess correction - Words guessed turn green.
	# Update the player's x and y with correct or incorrect guesses.
	#If statements, if player answers wins and otherwiese the hangman dies.


def main():
	pass

if __name__ == "__main__":
	main()
