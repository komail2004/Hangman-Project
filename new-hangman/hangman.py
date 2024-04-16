import pygame
import random

class HangmanGame:
    def __init__(self, filename):
        self.word = self.get_word(filename)
        self.guessed_letters = []
        self.hangman_status = 0
        self.win = False

    def get_word(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            return random.choice(lines).strip().lower()

    def guess(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.word:
                self.hangman_status += 1
            elif set(self.word) <= set(self.guessed_letters):
                self.win = True

    def is_game_over(self):
        return self.hangman_status == 6 or self.win

    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

class HangmanDisplay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.hangman_images = [pygame.image.load(f'hangman{i}.png') for i in range(7)]

    def update(self, hangman_status, display_word):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.hangman_images[hangman_status], (200, 100))
        word_label = self.font.render(display_word, 1, (0, 0, 0))
        self.screen.blit(word_label, (50, 500))
        pygame.display.update()

    def quit(self):
        pygame.quit()

def main():
    filename = "wordlist.txt"
    game = HangmanGame(filename)
    display = HangmanDisplay()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                letter = pygame.key.name(event.key)
                if len(letter) == 1 and letter.isalpha():
                    game.guess(letter)

        display.update(game.hangman_status, game.get_display_word())

        if game.is_game_over():
            running = False

    display.quit()

    if game.win:
        print("Congratulations! You won!")
    else:
        print(f"Sorry, you lost. The word was: {game.word}")

if __name__ == "__main__":
    main()
