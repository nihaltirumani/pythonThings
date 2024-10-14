import pygame 
from sys import exit
from math import floor

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sliders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

value = 0
value1 = 0
old_mouse_pressed = False
old_mouse_pressed1 = False

width = 30
height = 10
slider = pygame.Rect(50 - (width / 2 - 1), 100 - height / 2, width, height)

width1 = 25
height1 = 25
slider1 = pygame.Rect(98, 90, width1, height1)

restrisction1 = 100 - height / 2
restrisction2 = 400 - height / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((220, 220, 220))

    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if (mouse[0] and mouse_pos[0] < 65 and mouse_pos[0] > 35 and mouse_pos[1] < slider.y + 10 and mouse_pos[1] > slider.y - 10) or old_mouse_pressed:
        slider.y = mouse_pos[1] - 5
        old_mouse_pressed = mouse[0]

    if (mouse[0] and mouse_pos[0] < 135 and mouse_pos[0] > 100 and mouse_pos[1] < slider1.y + 25 and mouse_pos[1] > slider1.y - 25) or old_mouse_pressed1:
        slider1.y = mouse_pos[1] - 12.5
        old_mouse_pressed1 = mouse[0]

    if slider.y < restrisction1: slider.y = restrisction1
    elif slider.y > restrisction2: slider.y = restrisction2

    if slider1.centery < restrisction1 + 7: slider1.centery = restrisction1 + 7
    elif slider1.centery > restrisction2 + 7: slider1.centery = restrisction2 + 7

    pygame.draw.line(screen, "white", (50, 410), (50, 90), 40) # draws down to up
    pygame.draw.line(screen, "#4664fa", (50, 400), (50, slider.centery), 20) # draws down to up
    pygame.draw.rect(screen, "#3858fc", slider)

    pygame.draw.rect(screen, "white", (90, 80, 40, 340), border_radius = 20)
    pygame.draw.rect(screen, "#4664fa", (100, slider1.y, 20, (3.2 * (100 - (slider1.centery - 102) // 3))), border_radius = 12)
    pygame.draw.ellipse(screen, "#3858fc", slider1)

    value = 100 - floor((slider.centery - 100 ) / 3 )
    text = font.render(f"Value: {value}", True, "black")
    text_rect = text.get_rect(topleft = (10, 10))
    screen.blit(text, text_rect)

    value1 = 100 - (slider1.centery - 102) // 3
    text1 = font.render(f"Value: {value1}", True, "black")
    text_rect1 = text.get_rect(topleft = (300, 10))
    screen.blit(text1, text_rect1)

    pygame.display.update()
    clock.tick(60)