
import pygame
import math

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# creating button rects
red = pygame.Rect(100, 20, 20, 20)
green = pygame.Rect(120, 20, 20, 20)
blue = pygame.Rect(100, 40, 20, 20)
black =  pygame.Rect(120, 40, 20, 20)
rectangle = pygame.Rect(200, 12.5, 50, 50)
circle = pygame.Rect(275, 12.5, 50, 50)
trirect = pygame.Rect(350, 12.5, 50, 50)
rhombrect = pygame.Rect(425, 12.5, 50, 50)

eraser = pygame.Rect(700, 12.5, 50, 50)

# creating polygons
triangle = ((375, 12.5), (350, 62.5), (400, 62.5))
rhombus = ((425, 37.5), (450, 12.5), (475, 37.5), (450, 62.5))

#loading in eraser image
eraseim = pygame.image.load("eraser.png")

def toolbar(screen):
    #draw toolbar
    global tools
    tools = pygame.draw.rect(screen, (128, 128, 128), (0, 0, screen.get_width(), 75))
    

    #draw colors
    pygame.draw.rect(screen, RED, red)
    pygame.draw.rect(screen, GREEN, green)
    pygame.draw.rect(screen, BLUE, blue)
    pygame.draw.rect(screen, BLACK, black)
    pygame.draw.rect(screen, BLACK, rectangle, 1)
    pygame.draw.circle(screen, BLACK, circle.center, circle.width / 2, 1)
    pygame.draw.polygon(screen, BLACK, triangle, 1)
    pygame.draw.polygon(screen, BLACK, rhombus, 1)

    screen.blit(eraseim, eraser)



#draw a circle all the way from point a to point b
def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        x = int(start[0] + progress * (end[0] - start[0]))
        y = int(start[1] + progress * (end[1] - start[1]))
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    active = False
    radius = 15
    x = -1
    y = -1
    color = BLACK
    mode = "norm"
    
    screen.fill((255, 255, 255))
    toolbar(screen)

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]


        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # fill shortcut
                if event.key == pygame.K_0:
                    radius = max(screen.get_height(), screen.get_width())
                # pencil shortcut
                if event.key == pygame.K_1:
                    radius = 1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: # up whell radius grows
                    radius = min(200, radius + 1)

                elif event.button == 5: # down whell radius shrinks
                    radius = max(1, radius - 1)

                if event.button == 1:
                    position = event.pos
                    if tools.collidepoint(position):
                        if blue.collidepoint(position):
                            color = BLUE
                        elif red.collidepoint(position):
                            color = RED
                        elif green.collidepoint(position):
                            color = GREEN
                        elif black.collidepoint(position):
                            color = BLACK
                        elif eraser.collidepoint(position):
                            color = WHITE
                            mode = "norm"
                        elif rectangle.collidepoint(position):
                            if mode != "rect":
                                mode = "rect"
                                print("to rect")
                            else:
                                mode = "norm"
                                print("from rect")
                        elif circle.collidepoint(position):
                            if mode != "circle":
                                mode = "circle"
                            else:
                                mode = "norm"
                        elif trirect.collidepoint(position):
                            if mode != "triangle":
                                mode = "triangle"
                            else:
                                mode = "norm"
                        elif rhombrect.collidepoint(position):
                            if mode != "rhombus":
                                mode = "rhombus"
                            else:
                                mode = "norm"
                    
                    else:
                        if mode != "norm":
                            x, y = event.pos
                    active = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    active = False
                    if not tools.collidepoint(event.pos):
                        if mode == "rect":
                            resx, resy = event.pos
                            if resx < x:
                                x, resx = resx, x
                            if resy < y:
                                y, resy = resy, y
                            width = resx - x
                            height = resy - y

                            #hold shift to make a square
                            if shift_held:
                                width, height = min(width, height), min(width, height)

                            to_draw = pygame.Rect(x, y, width, height)
                            pygame.draw.rect(screen, color, to_draw, radius)

                        elif mode == "circle":
                            resx, resy = event.pos
                            if resx < x:
                                x, resx = resx, x
                            if resy < y:
                                y, resy = resy, y
                            width = resx - x
                            height = resy - y
                            to_draw = pygame.Rect(x, y, width, height)
                            pygame.draw.circle(screen, color, to_draw.center, min(width, height) / 2, radius)

                        elif mode == "triangle":
                            resx, resy = event.pos
                            if shift_held:
                                if resx < x:
                                    x, resx = resx, x
                                side = min(resx - x, 2 / (3 ** 0.5) * abs(resy - y))
                                height = side * (3 ** 0.5) / 2
                                # invert if dragged upwards
                                if y < resy:
                                    to_draw = ((x + side / 2, y), (x, y + height), (x + side, y + height))
                                else:
                                    to_draw = ((x, resy), (x + side, resy), (x + side / 2, resy + height))

                            elif ctrl_held:
                                # draw from single point to side along the hypotenuse
                                to_draw = ((x, y), (x, resy), (resx, resy))
                            else:
                                if resx < x:
                                    x, resx = resx, x
                                # intentional that if you drag upwards you get an upside-down triangle
                                to_draw = ((resx, resy), (x, resy), ((x + resx) / 2, y))

                            if radius >= 5:
                                pygame.draw.polygon(screen, color, to_draw)
                            else:
                                pygame.draw.polygon(screen, color, to_draw, radius)

                        elif mode == "rhombus":
                            resx, resy = event.pos
                            if shift_held:
                                if resx < x:
                                    x, resx = resx, x
                                if resy < y:
                                    y, resy = resy, y
                                diagonal = min(abs(resx - x), abs(resy - y))
                                to_draw = ((x + diagonal / 2, y), (x + diagonal, y + diagonal / 2), (x + diagonal / 2, y + diagonal), (x, y + diagonal / 2))
                            # for symmetrical polygons with given coordinates there is no need to check which is less
                            else:
                                to_draw = (((x + resx) / 2, y), (resx, (y + resy) / 2), ((x + resx) / 2, resy), (x, (y + resy) / 2))
                            if radius >= 5:
                                pygame.draw.polygon(screen, color, to_draw)
                            else:
                                pygame.draw.polygon(screen, color, to_draw, radius)

            
            if event.type == pygame.MOUSEMOTION and not tools.collidepoint(event.pos):
                if mode == "norm":
                    # get mouse position
                    position = event.pos
                    #don't draw when mouse first enters screen
                    if active:
                        if (x, y) != (-1, -1):
                            drawLineBetween(screen, (x, y), position, radius, color)
                    x, y = position

        toolbar(screen)

        pygame.display.flip()
        
        clock.tick(60)

main()
