#!/usr/bin/env python3

import pygame																														   
import random																														   

# Function to get random line from text file.																						   
def get_word(filename):																												 
	with open(filename, 'r') as file:																								   
		lines = file.readlines()																										
		return random.choice(lines).strip().lower()																					 

# Pygame initializations																												
pygame.init()																														   
screen = pygame.display.set_mode((800, 600))																							
font = pygame.font.Font(None, 36)																									   

# Load hangman images																												   
hangman_images = [pygame.image.load('hangman' + str(i) + '.png') for i in range(0, 7)]												  

def main():
	filename = "wordlist.txt"
	word = get_word(filename)
	guessed_letters = []

	hangman_status = 0
	running = True
	win = False

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				letter = pygame.key.name(event.key)
				if len(letter) == 1 and letter.isalpha():
					if letter not in guessed_letters:
						guessed_letters.append(letter)
						if letter not in word:
							hangman_status += 1
						elif set(word) <= set(guessed_letters):
							win = True
							running = False

		screen.fill((255, 255, 255))
		screen.blit(hangman_images[hangman_status], (200, 100))

		word_label = font.render(' '.join([letter if letter in guessed_letters 
										   else '_' for letter in word]), 1, (0, 0, 0))
		screen.blit(word_label, (50, 500))

		pygame.display.update()
		if hangman_status == 6:
			running = False

	if win:
		print("Congratulations! You won!")
	else:
		print(f"Sorry, you lost. The word was: {word}")

	pygame.quit()

if __name__ == "__main__":
	main()

