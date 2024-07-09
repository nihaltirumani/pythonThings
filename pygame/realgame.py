import pygame

pygame.init()

width, height = 900, 700 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RPG GAME")
clock = pygame.time.Clock()
running = True

player_pos = pygame.Rect(width /  2, height / 2, 100, 100)
player_speed = 10

black = (0,0,0)
white = (255, 255, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    pygame.draw.rect(screen, white, player_pos)

    keys = pygame.key.get_pressed ()

    if keys[pygame.K_w]:
        player_pos.y -= player_speed
    if keys[pygame.K_s]:
        player_pos.y += player_speed
    if keys[pygame.K_a]:
        player_pos.x -= player_speed
    if keys[pygame.K_d]:
        player_pos.x += player_speed

    pygame.display.flip()
    clock.tick(60)