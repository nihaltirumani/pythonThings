import pygame
from sys import exit

pygame.init()

# variables
WIDTH = 600
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

eraser = pygame.Rect(0, 0, 600, 600)
player = pygame.Rect(40, 500, 50, 50)
end = pygame.Rect(500, 30, 50, 50)
timer = 0

obs1 = pygame.Rect(125, 100, 100, 500)
obs2 = pygame.Rect(350, 0, 100, 500)

win_screen = font.render("YOU WON!", True, (0, 230, 77))
win_screen_rect = win_screen.get_rect(center = (300 ,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((242, 242, 242))

    pygame.draw.rect(screen, (242, 242, 242), eraser)

    mouse_pos = pygame.mouse.get_pos()

    if not player.colliderect(end):
        player.centerx = mouse_pos[0]
        player.centery = mouse_pos[1]
        
    # obstacle collisions
    if player.colliderect(obs1) or player.colliderect(obs2):
        pygame.quit()
        exit()

    # end and player
    pygame.draw.rect(screen, (140, 255, 26), end, 0, 5)
    pygame.draw.rect(screen, (26, 117, 255), player, 0, 5)

    # obstacles
    pygame.draw.rect(screen, (255, 92, 51), obs1)
    pygame.draw.rect(screen, (255, 51, 0), obs1, 10)
    pygame.draw.rect(screen, (255, 92, 51), obs2)
    pygame.draw.rect(screen, (255, 51, 0), obs2, 10)

    # winscreen collision
    if player.colliderect(end):
        timer += 1
        screen.blit(win_screen, win_screen_rect)

    # Winscreen duration
    if timer > 120:
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(FPS)