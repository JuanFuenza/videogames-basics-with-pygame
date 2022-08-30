import pygame

# Init pygame
pygame.init()

# Create display surface
WW = 600
WH = 300
ds = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("Discrete Movement!")

# Set game values
VELOCITY = 30

# Load in images
dragon_image = pygame.image.load("basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WW//2
dragon_rect.bottom = WH

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    # fill the display surface to cover old images
    ds.fill((0, 0, 0))

    # Blit (copy) assets to the screen
    ds.blit(dragon_image, dragon_rect)

    # Update display
    pygame.display.update()

# end the game
pygame.quit()