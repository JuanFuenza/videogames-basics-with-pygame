import pygame

# Init game
pygame.init()

# display surface
WW = 600
WH = 300
ds = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("Adding Sounds!")

# load sound effects
sound_1 = pygame.mixer.Sound('basic_tutorial_assets/sound_1.wav')
sound_2 = pygame.mixer.Sound('basic_tutorial_assets/sound_2.wav')

# Play the sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)

# Change volume of a sound effect
sound_2.set_volume(.1)
sound_2.play()

# Load bg music
pygame.mixer.music.load('basic_tutorial_assets/music.wav')

# Play and stop the music
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# endgame
pygame.quit()