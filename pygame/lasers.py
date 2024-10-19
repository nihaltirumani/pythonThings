import pygame 
from sys import exit

def draw_laser(
    color1: tuple,
    color2: tuple,
    color3: tuple,
    pos1: tuple,
    pos2: tuple,
    size: float,
    ):

    pygame.draw.line(trans_surf, color1, pos1, pos2, size * 20)
    pygame.draw.line(trans_surf, color2, pos1, pos2, size * 12)
    pygame.draw.line(trans_surf, color3, pos1, pos2, size * 4)

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lasers")
clock = pygame.time.Clock()

trans_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
laser1_pos1 = (50, 50)
laser1_pos2 = (550, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((230, 230, 230))

    draw_laser((255, 0, 0, 25), (255, 0, 0, 64), (255, 0, 0, 127), (50, 50), (550, 50), 1)
    draw_laser((255, 0, 0, 25), (255, 0, 0, 64), (255, 0, 0, 127), (40, 60), (40, 550), 1)
    draw_laser((255, 0, 0, 25), (255, 0, 0, 64), (255, 0, 0, 127), (50, 560), (550, 560), 1)
    draw_laser((255, 0, 0, 25), (255, 0, 0, 64), (255, 0, 0, 127), (560, 550), (560, 60), 1)

    draw_laser((0, 255, 0, 25), (0, 255, 0, 64), (0, 255, 0, 127), (300, 300), (50, 70), 1)
    draw_laser((0, 255, 0, 25), (0, 255, 0, 64), (0, 255, 0, 127), (300, 300), (550, 70), 1)
    draw_laser((0, 255, 0, 25), (0, 255, 0, 64), (0, 255, 0, 127), (300, 300), (50, 540), 1)
    draw_laser((0, 255, 0, 25), (0, 255, 0, 64), (0, 255, 0, 127), (300, 300), (550, 540), 1)

    screen.blit(trans_surf, (0, 0))

    pygame.draw.rect(screen, "black", pygame.Rect(285, 285, 30, 30))

    pygame.display.update()
    clock.tick(60)