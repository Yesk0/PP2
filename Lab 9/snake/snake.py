import pygame
from pygame.math import Vector2
import datetime
import random 

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)] # head, and body of the snake
        self.eated = False # checker for snake eating
        self.isDead = False # check snake death

    def drawingSnake(self): # draw the snake
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0 ,128 ,0), body_rect)

    def snakeMoving(self): # move the snake
        if self.eated == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]
            self.eated = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]

class Fruit:
    def __init__(self):
        self.randomize() # spawn fruit
    
    def drawingFruit(self): # draw fruit
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size) 
        self.food = pygame.image.load(f'food{self.randomFood}.png').convert_alpha() # random fruit
        self.food = pygame.transform.scale(self.food, (35, 35))
        screen.blit(self.food, fruit_rect)

    def randomize(self): # randomize fruit position and type
        self.x = random.randint(0, cell_number - 2) 
        self.y = random.randint(0, cell_number - 2) 
        self.pos = Vector2(self.x, self.y)
        self.randomFood = random.randint(1, 3)

class Game:
    def __init__(self):
        self.snake = Snake() 
        self.fruit = Fruit() 
        self.level = 1 
        self.snake_speed = 5 
        self.score = 0 

    def update(self): # update game state
        self.snake.snakeMoving()
        self.checkCollision()

    def drawElements(self): # draw snake, fruit, score
        self.snake.drawingSnake()
        self.fruit.drawingFruit()
        self.scoreDrawing()
    
    def checkCollision(self): # check collision with fruit
        if(self.fruit.pos == self.snake.body[0]):
            self.snake.eated = True
            if(self.fruit.randomFood == 1):
                self.score += 1
            if(self.fruit.randomFood == 2):
                self.score += 2
            if(self.fruit.randomFood == 3):
                self.score += 3
            self.fruit.randomize()
            self.levelAdding()

    def gameOver(self): # check collision with borders and itself
        if self.snake.body[0].x >= 19 or self.snake.body[0].x <= 0 or self.snake.body[0].y >= 19 or self.snake.body[0].y <= 0:
            return True
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True
        return False
    
    def levelAdding(self): # increase level
        if self.score % 3 == 0:
            self.level += 1
            self.snake_speed += 1
    
    def scoreDrawing(self): # draw score and level
        score_text = "Score: " + str(self.score)
        score_surface = font.render(score_text, True, (56, 74, 12))
        score_rect = score_surface.get_rect(center = (cell_size * cell_number - 120, 40))
        screen.blit(score_surface, score_rect)

        level_text = "Level: " + str(self.level)
        level_surface = font.render(level_text, True, (56, 74, 12))
        level_rect = level_surface.get_rect(center = (cell_size * cell_number - 120, 70))
        screen.blit(level_surface, level_rect)

pygame.init()
clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
direction = Vector2(1, 0) 
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) 
done = False

font = pygame.font.Font('font.ttf', 25) 

nowSeconds = int((datetime.datetime.now()).strftime("%S"))

game = Game() 
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if direction.x != -1:
                direction = Vector2(1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if direction.x != 1:
                direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if direction.y != 1:
                direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if direction.y != -1:
                direction = Vector2(0, 1)

    if(game.gameOver() == True):
        done = True
    
    time = datetime.datetime.now()
    seconds = int(time.strftime("%S"))
    if abs(seconds - nowSeconds) > 3:
        game.fruit.randomize()
        nowSeconds = seconds
    screen.fill((175, 215, 70))
    game.drawElements()
    game.update()
    pygame.display.flip()
    clock.tick(game.snake_speed)
pygame.quit()