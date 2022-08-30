import pygame

# Init pygame
pygame.init()

# DS
W = 600
H = 300
ds = pygame.display.set_mode((W, H))
pygame.display.set_caption("Continuous Movement!")

# Set game values
VELOCITY = 20

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# load images
dragon_image = pygame.image.load("basic_tutorial_assets/dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (W//2, H//2)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Move the dragon continuosly
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY

    # fill display
    ds.fill((0, 0, 0))

    # Blit
    ds.blit(dragon_image, dragon_rect)

    # update display
    pygame.display.update()

    # Set fps
    clock.tick(FPS)

# end the game
pygame.quit()