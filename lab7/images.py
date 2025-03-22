import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
clock = pygame.time.Clock()
bg_image = pygame.image.load('clock.png')
sec_image = pygame.image.load('sec_hand.png')
min_image = pygame.image.load('min_hand.png')

rect = bg_image.get_rect(center=(405, 320)) 
running=True 
while running:
    screen.blit(bg_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    time = datetime.now().time()
    sec_angle = -time.second * 6
    nsec_img = pygame.transform.rotate(sec_image, sec_angle)
    sec_rect = nsec_img.get_rect(center=rect.center)
    screen.blit(nsec_img, sec_rect.topleft)

    min_angle = -time.minute * 6
    nmin_img = pygame.transform.rotate(min_image, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)
    pygame.display.flip()
    clock.tick(60) 
