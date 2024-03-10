import pygame
import pygame.font

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36)

text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))

x, y = 100, 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(text_surface, (x, y))
    pygame.display.flip()

pygame.quit()
