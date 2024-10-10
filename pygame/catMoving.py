import pygame 
from sys import exit

def player_movement():
    global speed, player_surf, player_rect, facing_left

    if keys[pygame.K_w]:
        player_rect.y -= speed
    if keys[pygame.K_s]:
        player_rect.y += speed
    if keys[pygame.K_a]:
        player_rect.x -= speed
        
        if not facing_left:
            player_surf = pygame.transform.flip(player_surf, True, False)
            facing_left = True
    if keys[pygame.K_d]:
        player_rect.x += speed

        if facing_left:
            player_surf = pygame.transform.flip(player_surf, True, False)
            facing_left = False

def player_collisions():
    global player_rect
    if player_rect.x <= 0: player_rect.x = 0
    if player_rect.x >= 705: player_rect.x = 705
    if player_rect.y <= 0: player_rect.y = 0
    if player_rect.y >= 300: player_rect.y = 300

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Cat moving")

player_surf = pygame.image.load("pygame/cat.png").convert_alpha()
player_rect = player_surf.get_rect(center = (400 ,200))
speed = 4
facing_left = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((190, 190, 190))

    keys = pygame.key.get_pressed()

    player_movement()
    player_collisions()

    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)
        