#!/usr/bin/env python3
import random

# Function to get random line from text file.
def getText(fileName):
	with open(fileName, 'r') as file:
		lines = file.readlines()
		randomLine = random.choice(lines)
	return randomLine.replace('\n', '')
# Print the prompt. Fills in guesses provided by rights list.
def printPrompt(word, rights):
	for i in word:
		if i in rights:
			print(i, end=' ')
		else:
			print("_", end=' ')
	print()

def main():
	fileName = "wordlist.txt"
	word = getText(fileName)
	word = getText(fileName).lower()
	max_guesses = 6
	rights = []

	print("Welcome to Hangman!")
	
	while max_guesses > 0:
		printPrompt(word, rights)
		
		guess = input("Enter a letter: ").lower()
		
		if len(guess) != 1 or not guess.isalpha():
			print("Please enter a valid single letter.")
			continue
		
		if guess in rights:
			print("You already guessed that letter.")
			continue
		
		rights.append(guess)
		
		if guess not in word:
			max_guesses -= 1
			print(f"Wrong! You have {max_guesses} guesses left.")
		
		if all(letter in rights for letter in word):
			printPrompt(word, rights)
			print("Congratulations! You won!")
			break
		
	if max_guesses == 0:
		print(f"Sorry, you lost. The word was: {word}")
if __name__ == "__main__":
	main()
