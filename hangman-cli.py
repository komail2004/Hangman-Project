#!/usr/bin/env python3

import random
import pygame

x= 600	
y= 800

def window():
	#Creating the pygame's window
	#Caption of the game
	#Editing the window and updates
	screen = pygame.display.set_mode((x,y))

	pygame.display.set_caption("Hangperson")
	screen.fill("blue")
	pygame.display.flip()

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

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
