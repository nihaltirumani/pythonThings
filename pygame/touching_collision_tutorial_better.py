import pygame
import random

pygame.init()

width = 1260
height = 760
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
player_pos = pygame.Rect(width /  2, height / 2, 100, 100)
player_speed = 10
running = True
obstacles = []
for _ in range(16):
    box1 = pygame.Rect(random.randint(0, width), random.randint(0, height), 50, 50)
    obstacles.append(box1)

pygame.mouse.set_visible(False)

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)

    col = green

    for obstacle in obstacles:
        if player_pos.colliderect(obstacle):
            col = red

    for obstacle in obstacles:
        pygame.draw.rect(screen, white, obstacle)

    mouse_pos = pygame.mouse.get_pos()
    player_pos.center = mouse_pos
    player_pos.x += 1
    player_pos.y += 1

    pygame.draw.rect(screen, col, player_pos)

    keys = pygame.key.get_pressed ()
    """
    if keys[pygame.K_w]:
        player_pos.y -= player_speed
    if keys[pygame.K_s]:
        player_pos.y += player_speed
    if keys[pygame.K_a]:
        player_pos.x -= player_speed
    if keys[pygame.K_d]:
        player_pos.x += player_speed
    """
    pygame.display.flip()
    clock.tick(60)