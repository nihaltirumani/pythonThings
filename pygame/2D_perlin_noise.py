import noise as n
import random
import pygame 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("2D Perlin noise")
clock = pygame.time.Clock()

r = random.random() * 1000
scale = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("red")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        scale += 0.1
    elif keys[pygame.K_DOWN]:
        scale -= 0.1

    for y in range(0, 300):
        for x in range(0, 300):
            # grey_scale = 255 if ((n.pnoise2((x/scale + r) + (pygame.time.get_ticks() / 800), (y/scale + r)  + (pygame.time.get_ticks() / 800)) + 1) / 2 ) < 0.5 else 0
            grey_scale = ((n.pnoise2((x/scale + r) + (pygame.time.get_ticks() / 800), (y/scale + r)  + (pygame.time.get_ticks() / 800)) + 1) / 2 ) * 255
            screen.set_at((x, y), (grey_scale, grey_scale, grey_scale))
    pygame.display.update()
    clock.tick(60)