import random
import pygame

# Initiating Pygame and assigning the x and y
pygame.init()
x = 600
y = 600

def window():
    # Creating the pygame's window
    # Caption of the game
    # Editing the window and updates
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Hangperson")
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(200, 200, 140, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    # Creating a class for our Hangperson Character
    class hangperson():
        def __init__(self, image_path, size, position):
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)  # Assign to self.image, not self.size
            self.position = position

    # Assigning the class to character and creating it
    character = hangperson("images/sprite01.png", (200, 200), (200, 200))

    # The main loop of the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        # it will set background color of screen
        screen.fill((255, 255, 255))

        if active:
            color = color_active
        else:
            color = color_passive

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, input_rect.topleft)
        screen.blit(character.image, character.position)
        pygame.display.flip()

        # Print input text in the terminal
        print("Input text:", user_text)

def main():
    window()

if __name__ == "__main__":
    main()
