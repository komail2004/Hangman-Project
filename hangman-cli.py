#!/usr/bin/env python3

import random
import pygame
import time

#Initiating Pygame and assigning the x and y
pygame.init()
x= 600	
y= 800

def window():
	#Creating the pygame's window
	#Caption of the game
	#Editing the window and updates
	screen = pygame.display.set_mode((x,y))
	pygame.display.set_caption("Hangperson")
	screen.fill(("white"))

	#Creating a class for our Hangpersong Characater
	class hangperson():
		def __init__(self, image_path, size, position):
			self.image = pygame.image.load(image_path).convert_alpha()
			self.image = pygame.transform.scale(self.image, size)  # Assign to self.image, not self.size
			self.position = position

	#Assigning the class to character and creating it
	character = hangperson("images/person.png", (200,200),(200, 200))
	#The main loop of the game
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		screen.blit(character.image,character.position)
		pygame.display.flip()
# Function to get random line from text file.
# def getText(fileName):
# 	with open(fileName, 'r') as file:
# 		lines = file.readlines()
# 		randomLine = random.choice(lines)

# 	return randomLine.replace('\n', '')

# # Print the prompt. Fills in guesses provided by rights list.
# def printPrompt(word, rights):
# 	for i in word:
# 		if i in rights:
# 			print(i, end=' ')
# 		else:
# 			print("_", end=' ')

# 	print()

def main():
	window()
# 	fileName = "wordlist.txt"
# 	word = getText(fileName).lower()
# 	max_guesses = 6
# 	rights = []
	
# 	print("Welcome to Hangman!")
	
# 	while max_guesses > 0:
# 		printPrompt(word, rights)
		
# 		guess = input("Enter a letter: ").lower()
		
# 		if len(guess) != 1 or not guess.isalpha():
# 			print("Please enter a valid single letter.")
# 			continue
		
# 		if guess in rights:
# 			print("You already guessed that letter.")
# 			continue
		
# 		rights.append(guess)
		
# 		if guess not in word:
# 			max_guesses -= 1
# 			print(f"Wrong! You have {max_guesses} guesses left.")
		
# 		if all(letter in rights for letter in word):
# 			printPrompt(word, rights)
# 			print("Congratulations! You won!")
# 			break
		
# 	if max_guesses == 0:
# 		print(f"Sorry, you lost. The word was: {word}")

if __name__ == "__main__":
	main()
