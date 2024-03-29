import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))




running = True
blue = (0, 0, 200)
fps = 60
x = 300
y = 300
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 20: y -= 20
    if pressed[pygame.K_DOWN] and y < 580: y += 20
    if pressed[pygame.K_LEFT] and x > 20 : x -= 20
    if pressed[pygame.K_RIGHT] and x < 580: x += 20

    pygame.draw.circle(screen, blue, (x, y), 25)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(fps)
    


