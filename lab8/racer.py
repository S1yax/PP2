import random
import time
import pygame
import sys
import os
from pygame.locals import *

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
car1 = pygame.image.load("top-view-car.png")
car1 = pygame.transform.scale (car1,(40,60))
car2= pygame.image.load("car-icon.png")
car2 = pygame.transform.scale(car2,(40,60))
coin=pygame.image.load("gold-coin-icon.png")
coin=pygame.transform.scale(coin,(40,40))
car2.set_colorkey((238,243,250))
# Создание окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
background = pygame.image.load("road.png")
background=pygame.transform.scale(background,(800,800))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car1
        while True:
            self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
            if abs(self.rect.centerx - P1.rect.centerx) > 50:
                break

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car2
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)
    
    def collect_coin(self, coins):
        return bool(pygame.sprite.spritecollide(self, coins, True))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image =coin
        while True:
            self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
            if abs(self.rect.centerx - P1.rect.centerx) > 50 and abs(self.rect.centerx - E1.rect.centerx) > 50:
                break
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.blit(background, (-200, -20))
    scores = font_small.render(str(SCORE), True, RED)
    coin_scores = font_small.render(str(COIN_SCORE), True, RED)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (375, 10))
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    if P1.collect_coin(coins):
        COIN_SCORE += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)                                       
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
