import pygame

# Init pygame
pygame.init()

# Display surface
WIN_WIDTH = 600
WIN_HEIGHT = 600
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Drawing Objets")

# Define colors as rgb tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# BG 
display_surface.fill(BLUE)

# Draw various shapes on our display
# Line(Surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)

# Circle(surface, color, center, radius, thickness...0 for fill)
pygame.draw.circle(display_surface, WHITE, (WIN_HEIGHT // 2, WIN_WIDTH // 2), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WIN_HEIGHT // 2, WIN_WIDTH // 2), 195, 0)

# Rectangle(surface, color, (top-left x, top-left-y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

# Endgame
pygame.quit()