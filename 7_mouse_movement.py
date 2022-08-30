import pygame

# Init pygame
pygame.init()

# Display surface
W = 600
H = 300
ds = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mouse movement!")

# Load images
dragon_image = pygame.image.load("basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Move base on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y

        # Drag the object when the mouse button is clicked
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y


    # fill display
    ds.fill((0, 0, 0))

    # Blit assets
    ds.blit(dragon_image, dragon_rect)

    # update display
    pygame.display.update()

# end the game
pygame.quit()