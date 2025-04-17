import pygame

pygame.init()
fps = 60
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_figure = 0
active_color = 'black'
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []

def draw_menu(color):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 130])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)
    
    brushes = [
        [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0],
        [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1],
        [pygame.draw.polygon(screen, 'black', [(140, 10), (140, 60), (190, 60)]), 3],
        [pygame.draw.polygon(screen, 'black', [(210, 60), (260, 60), (235, 10)]), 4],
        [pygame.draw.polygon(screen, 'black', [(280, 35), (300, 10), (320, 35), (300, 60)]), 5]
    ]
    
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)
    
    eraser = pygame.image.load("eraser-square-svgrepo-com.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.size = (25, 25)
    screen.blit(eraser, eraser_rect.topleft)
    
    color_rects = [
        pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25]),
        pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25]),
        pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25]),
        pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25]),
        pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25]),
        pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25]),
        pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    ]
    
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]
    
    return brushes, color_rects + [eraser_rect], rgb_list

def draw_painting(paints):
    for color, pos, figure in paints:
        if figure == 0:
            pygame.draw.circle(screen, color, pos, 20)
        elif figure == 1:
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20])
        elif figure == 2:
            pygame.draw.rect(screen, color, [pos[0] - 20, pos[1] - 20, 20, 40])
        elif figure == 3:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] - 20, pos[1] + 20), (pos[0] + 20, pos[1] + 20)])
        elif figure == 4:
            pygame.draw.polygon(screen, color, [(pos[0] - 20, pos[1] + 20), (pos[0] + 20, pos[1] + 20), (pos[0], pos[1] - 20)])
        elif figure == 5:
            pygame.draw.polygon(screen, color, [(pos[0], pos[1] - 20), (pos[0] + 20, pos[1]), (pos[0], pos[1] + 20), (pos[0] - 20, pos[1])])

run = True
while run:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    brushes, colors, rgbs = draw_menu(active_color)
    
    if left_click and mouse[1] > 85:
        painting.append((active_color, mouse, active_figure))
    
    draw_painting(painting)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, color_rect in enumerate(colors):
                if color_rect.collidepoint(event.pos):
                    active_color = rgbs[i]
            for brush in brushes:
                if brush[0].collidepoint(event.pos):
                    active_figure = brush[1]
    
    pygame.display.flip()

pygame.quit()
