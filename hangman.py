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

    def update(self, hangman_status, display_word, outcome, word=None):  # Accept word as an argument
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.hangman_images[hangman_status], (200, 100))
        word_label = self.font.render(display_word, 1, (0, 0, 0))
        self.screen.blit(word_label, (50, 500))

        if outcome == "lose" and word is not None:  # Check if word is provided and the outcome is "lose"
            word_text = self.font.render("The word was: " + word, 1, (255, 0, 0))
            self.screen.blit(word_text, (50, 550))

        pygame.display.update()

    def quit(self):
        pygame.quit()

def game_over_menu(display, outcome, word=None):  # Accept word as an argument
    menu_screen = True
    while menu_screen:
        display.screen.fill((255, 255, 255))
        if outcome == "win":
            text = display.font.render("Congratulations! You won!", True, (0, 0, 0))
        else:
            text = display.font.render("Sorry, you lost.", True, (0, 0, 0))
        display.screen.blit(text, (50, 200))

        if word is not None:  # Display the word if available
            word_text = display.font.render("The word was: " + word, True, (255, 0, 0))
            display.screen.blit(word_text, (50, 250))

        replay_button = pygame.Rect(100, 300, 200, 50)
        pygame.draw.rect(display.screen, (0, 255, 0), replay_button)
        replay_text = display.font.render("Replay", True, (0, 0, 0))
        display.screen.blit(replay_text, (150, 310))

        quit_button = pygame.Rect(500, 300, 200, 50)
        pygame.draw.rect(display.screen, (255, 0, 0), quit_button)
        quit_text = display.font.render("Quit", True, (0, 0, 0))
        display.screen.blit(quit_text, (570, 310))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 <= mouse_x <= 300 and 300 <= mouse_y <= 350:  # Replay button clicked
                    return True
                elif 500 <= mouse_x <= 700 and 300 <= mouse_y <= 350:  # Quit button clicked
                    return False

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
    outcome = ""

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

        display.update(game.hangman_status, game.get_display_word(), outcome, game.word)  # Pass the word
        if game.is_game_over() and outcome == "":
            if game.win:
                pygame.mixer.Sound.play(win_sound)
                outcome = "win"
            else:
                pygame.mixer.Sound.play(lose_sound)
                outcome = "lose"

        if outcome:
            replay = game_over_menu(display, outcome, game.word)  # Pass the word
            if not replay:
                running = False
            else:
                game.reset()
                outcome = ""

    display.quit()

if __name__ == "__main__":
    main()
