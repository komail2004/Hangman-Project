import pygame

# Initiating Pygame and assigning the x and y
pygame.init()
x = 600
y = 600

def window():
    global active, user_text
    # Creating the pygame's window
    # Caption of the game
    # Editing the window and updates
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Hangperson")

    # Creating a class for our text input area
    class TextInput():
        def __init__(self, rect, font, color_active, color_passive):
            self.rect = pygame.Rect(rect)
            self.font = pygame.font.Font(font, 32)
            self.color_active = pygame.color.Color(color_active)
            self.color_passive = pygame.color.Color(color_passive)
            self.active = False
            self.text = ''

    # Initialize the text input area
    text_input = TextInput((200, 200, 140, 32), None, 'lightskyblue3', 'chartreuse4')

    # Creating a class for our Hangperson 
    class Hangperson():
        def __init__(self, image_path, size, position):
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)  # Assign to self.image, not self.size
            self.position = position

    # Assigning the class to character and creating it
    character = Hangperson("images/sprite01.png", (200, 200), (200, 200))

    # The main loop of the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_input.rect.collidepoint(event.pos):
                    text_input.active = not text_input.active
                else:
                    text_input.active = False
            if event.type == pygame.KEYDOWN:
                if text_input.active:
                    if event.key == pygame.K_BACKSPACE:
                        text_input.text = text_input.text[:-1]
                    else:
                        text_input.text += event.unicode

        # Set background color
        screen.fill((255, 255, 255))

        # Determine color of text input area
        color = text_input.color_active if text_input.active else text_input.color_passive

        # Draw the text input area
        pygame.draw.rect(screen, color, text_input.rect, 2)

        # Render and display the text
        text_surface = text_input.font.render(text_input.text, True, (0, 0, 0))
        screen.blit(text_surface, (text_input.rect.x + 5, text_input.rect.y + 5))

        # Display the hangperson character
        screen.blit(character.image, character.position)

        pygame.display.flip()

def main():
    window()

if __name__ == "__main__":
    main()
