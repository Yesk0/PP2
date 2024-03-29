import pygame
from pygame import mixer

pygame.init()
mixer.init()
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((424, 780), pygame.RESIZABLE)
background_image = pygame.image.load("song2.png")
background_image = pygame.transform.scale(background_image, (424, 780))

running = True
i = 0
music = ['basta.mp3', 'bum.mp3', 'inna.mp3']
play = ['song2.png', 'song4.png', 'song6.png']
pause = ['song1.png', 'song3.png', 'song5.png']

def start(i):
    mixer.music.load(music[i])
    mixer.music.set_volume(0.3)
    mixer.music.play()

start(i)
space = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if space == False:
                mixer.music.pause()
                space = True
                background_image = pygame.image.load(pause[i])
                background_image = pygame.transform.scale(background_image, (424, 780))
            else:
                mixer.music.unpause()
                space = False
                background_image = pygame.image.load(play[i])
                background_image = pygame.transform.scale(background_image, (424, 780))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if i == 2:
                i = 0
                start(i)
                background_image = pygame.image.load(play[i])
                background_image = pygame.transform.scale(background_image, (424, 780))
            else:
                i += 1
                start(i)
                background_image = pygame.image.load(play[i])
                background_image = pygame.transform.scale(background_image, (424, 780))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if i == 0:
                i = 2
                start(i)
                background_image = pygame.image.load(play[i])
                background_image = pygame.transform.scale(background_image, (424, 780))
            else:
                i -= 1
                start(i)
                background_image = pygame.image.load(play[i])
                background_image = pygame.transform.scale(background_image, (424, 780))

    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()