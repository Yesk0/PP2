#Imports
import pygame, sys
from pygame.locals import *
import random, time

from pygame.sprite import Group

#Initialzing 
pygame.init()
pygame.mixer.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
EXP = 0
LVL = 1

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


# loading music
pygame.mixer.music.load("care_game/background.wav")
# loading in images
background = pygame.image.load("care_game/AnimatedStreet.png")
coinsmall = pygame.image.load("care_game/coin.png")
coinmed = pygame.image.load("care_game/Coinm.png")
coinlarge = pygame.image.load("care_game/Coinl.png")

coinmed = pygame.transform.scale(coinmed, (60, 60))
coinlarge = pygame.transform.scale(coinlarge, (60, 60))

# creating a weighted distribution of coins
coin_choice = [coinsmall, coinsmall, coinsmall, coinmed, coinmed, coinlarge]


#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.get_type()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-200, 0))
    # choosing which coin to spawn
    def get_type(self):
        # choose which coin to spawn
        id = random.randint(0, 5)
        # set value and image
        if id < 3:
            self.worth = 1
        elif id < 5:
            self.worth = 2
        else:
            self.worth = 4
        self.image = coin_choice[id]
        # randomise the distance till dissapearance
        self.wait = random.randint(600, 1000)
    def move(self):
        self.rect.move_ip(0, (SPEED + 2 * self.worth) / 2)
        #wait a little before respawning
        if (self.rect.bottom > self.wait):
            self.get_type()
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-200, 0))

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("care_game/Enemy.png")
        # save width and height of object (from image)
        self.rect = self.image.get_rect()
        # center at random x coordiate within bounds
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        # if enemy reached bottom of screen increment score and reset enemy to top with a new random position
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        # same as enemy, with fixed initial center
        self.image = pygame.image.load("care_game/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        # move within bounds
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
bonuses = pygame.sprite.Group()
bonuses.add(C1)
bonuses.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)

# start  music
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              # speed increases first by 1, then slightly less until starts increasing by 1/4
              SPEED += 4 / min(max(4, LVL), 16)
              LVL += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #blit background and car score
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    #blit coin score and an icon for it
    coin_score = font_small.render(str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(coin_score, (370,10))
    DISPLAYSURF.blit(coinsmall, (300, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #when collecting coin upgrade score and move it out of sight for respawning
    if pygame.sprite.spritecollideany(P1, bonuses):
        collected = pygame.sprite.spritecollide(P1, bonuses, False)
        for item in collected:
            COIN_SCORE += item.worth
            item.rect.center = (200, 650)
            # give 1 exp per coin
            EXP += 1
            # at 5 exp level up, remove 5 exp
            # (easily improvable to give n levels in case we somehow get over 10 EXP)
            if EXP >= 5:
                pygame.event.post(pygame.event.Event(INC_SPEED))
                EXP %= 5


    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          pygame.mixer.Sound('care_game/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)