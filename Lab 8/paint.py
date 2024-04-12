# press "d" chnage cursor position to create a rectangle
# press "f" chnage cursor position to create a circle
# Pressing r, g, or b keys will make the trail turn red, green, and blue respectively.
# Pressing the left mouse button will cause the trail to become thicker.
# Pressing the right mouse button will cause the trail to become thinner.

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []
    drawing_rectangle = False
    start_rect_pos = (0, 0)
    end_rect_pos = (0, 0)
    drawn_rect = None
    drawing_circle = False
    circle_center = (0, 0)
    circle_radius = 0

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    points = []
                elif event.key == pygame.K_d:
                    drawing_rectangle = True
                    start_rect_pos = pygame.mouse.get_pos()
                elif event.key == pygame.K_f:
                    drawing_circle = True
                    circle_center = pygame.mouse.get_pos()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    end_rect_pos = pygame.mouse.get_pos()
                    drawing_rectangle = False
                    circle_radius = pygame.math.Vector2(circle_center).distance_to(
                        pygame.math.Vector2(pygame.mouse.get_pos()))
                    drawing_circle = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                    radius = min(200, radius + 1)
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        screen.fill((0, 0, 0))

        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        if drawing_rectangle:
            end_rect_pos = pygame.mouse.get_pos()
            drawn_rect = pygame.Rect(start_rect_pos,
                                     (end_rect_pos[0] - start_rect_pos[0], end_rect_pos[1] - start_rect_pos[1]))
            pygame.draw.rect(screen, getColor(mode), drawn_rect)

        if drawing_circle:
            circle_radius = pygame.math.Vector2(circle_center).distance_to(pygame.math.Vector2(pygame.mouse.get_pos()))
            pygame.draw.circle(screen, getColor(mode), circle_center, int(circle_radius))

        pygame.display.flip()
        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def getColor(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)


main()
