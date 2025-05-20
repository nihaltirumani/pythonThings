import pygame 
from sys import exit
import math

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Object following mouse")
clock = pygame.time.Clock()

speed = 10
angle = 0
velx = 0
vely = 0
dx = 0
dy = 0
box1 = pygame.Rect(400, 200, 40, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("white")

    mouse_pos = pygame.mouse.get_pos()
    dx = mouse_pos[0] - box1.centerx
    dy = mouse_pos[1] - box1.centery
    angle = math.atan2(dx, dy)
    velx = speed * math.sin(angle)
    vely = speed * math.cos(angle)
    box1.centerx += velx
    box1.centery += vely
    pygame.draw.rect(screen, "red", box1)

    pygame.display.update()
    clock.tick(60)