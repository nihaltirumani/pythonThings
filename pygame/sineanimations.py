import pygame
from sys import exit
from math import sin

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

rectx = width / 2
recty = height / 2
rect1 = pygame.Rect(rectx, recty, 40, 40)
range = 10

cat_surf = pygame.image.load("pygame/cat.png").convert_alpha()
cat_rect = cat_surf.get_rect(center = (150, 150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((0, 0, 0))

    rect1.y = (range * sin(pygame.time.get_ticks() * 0.0025)) + recty
    pygame.draw.rect(screen, (255, 255, 255), rect1)
    screen.blit(cat_surf, cat_rect)

    pygame.display.update()
    clock.tick(60)