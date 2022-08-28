import pygame

#init pygame
pygame.init()

# display
WIN_W = 600
WIN_H = 300
dis_sur = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Blitting Images!")

# load images... returns a surface object with the image dragon on it.
# We can then get the rect of the surface and use the rect to position the image.
dragon_left_image = pygame.image.load("basic_tutorial_assets/dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("basic_tutorial_assets/dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WIN_W, 0)

# init game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit(copy) a surface object at the given coordinates to our display
    dis_sur.blit(dragon_left_image, dragon_left_rect)
    dis_sur.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(dis_sur, (255, 255, 255), (0, 75), (WIN_W, 75), 4)

    # Update screen
    pygame.display.update()


pygame.quit()