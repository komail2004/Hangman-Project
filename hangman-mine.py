#!/usr/bin/env python3

import random

# Function to get random line from text file.
def getText(fileName):
	with open(fileName, 'r') as file:
		lines = file.readlines()
		randomLine = random.choice(lines)

	return randomLine.replace('\n', '')

def printPrompt(word, rights):
	for i in word:
		if i in rights:
			print(i, end=' ')
		else:
			print("_", end=' ')

	print()

def main():
	word = getText('wordlist.txt')
	chars = list(word)
	num = len(word)
	lives = 6
	rights = []
	printPrompt(word, rights)

	while num > 0:
		guess = input("Guess a letter: ")
		if guess in chars:
			print("Right")
			chars.remove(guess)
			rights.append(guess)
			num = num - 1
			if num == 0:
				print("You guessed",word,"correctly!")
		else:
			print("Wrong")
			lives = lives - 1
			if lives == 0:
				print("You lost.")
				break

		printPrompt(word, rights)

main()
