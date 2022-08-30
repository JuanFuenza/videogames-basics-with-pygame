import pygame


# Init pygame
pygame.init()

# Display surface
WW = 600
WH = 300
ds = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("Blitting Images!")

# define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# see all available sistem fonts
fonts = pygame.font.get_fonts()

for font in fonts:
    print(font)

# define fonts
system_font = pygame.font.SysFont('calibri', 64)
custom_font = pygame.font.Font('basic_tutorial_assets/AttackGraffiti.ttf', 32)

# define text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WW//2, WH//2)

custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (WW//2, WH//2 + 100)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit (copy) the text surfaces to the display surface
    ds.blit(system_text, system_text_rect)
    ds.blit(custom_text, custom_text_rect)

    # update display
    pygame.display.update()

# endgame
pygame.quit()