import pygame

# Init pygame
pygame.init()


# Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World!")

# Main game loop
running = True

while running:  
    # Loop through a list of Event objects that have ocurred
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# End game
pygame.quit()