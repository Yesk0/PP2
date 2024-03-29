import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("deon")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

player = pygame.image.load("images/icon.png")

run = True
while run:

    screen.blit(player, (10, 40))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
