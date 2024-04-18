import pygame
import random
import os
import simpleaudio as sa

class HangmanGame:
    def __init__(self, filename):
        self.filename = filename
        self.word = self.get_word()
        self.guessed_letters = []
        self.hangman_status = 0
        self.win = False

    def get_word(self):
        with open(self.filename, 'r') as file:
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

    def reset(self):
        self.word = self.get_word()
        self.guessed_letters = []
        self.hangman_status = 0
        self.win = False

    def get_display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

class HangmanDisplay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.hangman_images = [pygame.image.load(f'images/hangman{i}.png') for i in range(7)]

    def update(self, hangman_status, display_word):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.hangman_images[hangman_status], (200, 100))
        word_label = self.font.render(display_word, 1, (0, 0, 0))
        self.screen.blit(word_label, (50, 500))
        pygame.display.update()

    def play_sound(self, sound):
        sound.play()

    def quit(self):
        pygame.quit()

def main():
    filename = "wordlist.txt"
    game = HangmanGame(filename)
    display = HangmanDisplay()
    pygame.mixer.init()
    correct_sound = pygame.mixer.Sound(os.path.join('sound', 'correct_guess.wav'))
    incorrect_sound = pygame.mixer.Sound(os.path.join('sound', 'wrong_guess.wav'))
    win_sound = pygame.mixer.Sound(os.path.join('sound', 'winning_sound.wav'))
    lose_sound = pygame.mixer.Sound(os.path.join('sound', 'losing_sound.wav'))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                letter = pygame.key.name(event.key)
                if len(letter) == 1 and letter.isalpha():
                    if letter in game.word:
                        pygame.mixer.Sound.play(correct_sound)
                    else:
                        pygame.mixer.Sound.play(incorrect_sound)
                    game.guess(letter)

        display.update(game.hangman_status, game.get_display_word())

        if game.is_game_over():
            if game.win:
                pygame.mixer.Sound.play(win_sound)
            else:
                pygame.mixer.Sound.play(lose_sound)
            pygame.time.delay(2000)  # Delay for 2 seconds
            game.reset()

    display.quit()

if __name__ == "__main__":
    main()
