import pygame 
from sys import exit
from math import floor

class Slider:
    def __init__(self, xpos: int, ypos: int, vertical: bool, value: int):
        self.x = xpos
        self.y = ypos
        self.vertical = vertical
        self.value = value

        self.slider_button_width = 30
        self.slider_button_height = 10
        self.slider_button = pygame.Rect(self.x - (self.slider_button_width / 2 - 1), self.y - self.slider_button_height / 2, self.slider_button_width, self.slider_button_height)

    def draw(self, screen):
        pygame.draw.line(screen, "white", (self.x, ((self.y + self.value) + 10)), (self.x, (self.y - 10)), 40)
        pygame.draw.line(screen, "#4664fa", (self.x, (self.y + self.value)), (self.x, self.y), 20)
        pygame.draw.rect(screen, "#3858fc", self.slider_button)

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sliders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

slider = Slider(100, 100, True, 300)
"""
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

restrisction1_slider1 = restrisction1 + 7
restrisction2_slider1 = restrisction2 + 7"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((50, 50, 50))
    """
    #Slider button touching collisions
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if (mouse[0] and mouse_pos[0] < 65 and mouse_pos[0] > 35 and mouse_pos[1] < slider.y + 10 and mouse_pos[1] > slider.y - 10) or old_mouse_pressed:
        slider.y = mouse_pos[1] - 5
        old_mouse_pressed = mouse[0]

    if (mouse[0] and mouse_pos[0] < 135 and mouse_pos[0] > 100 and mouse_pos[1] < slider1.y + 25 and mouse_pos[1] > slider1.y - 25) or old_mouse_pressed1:
        slider1.y = mouse_pos[1] - 12.5
        old_mouse_pressed1 = mouse[0]

    # Adding restrictions to slider buttons
    if slider.y < restrisction1: slider.y = restrisction1
    elif slider.y > restrisction2: slider.y = restrisction2

    if slider1.centery < restrisction1_slider1: slider1.centery = restrisction1_slider1
    elif slider1.centery > restrisction2_slider1: slider1.centery = restrisction2_slider1

    # Uses line method to draw a slider except the slider button.
    pygame.draw.line(screen, "white", (50, 410), (50, 90), 40) # draws down to up (outer part)
    pygame.draw.line(screen, "#4664fa", (50, 400), (50, slider.centery), 20) # draws down to up (filled part)
    pygame.draw.rect(screen, "#3858fc", slider) # slider button

    # Uses rect method to draw a slider except the slider button which uses ellipse method to draw.
    pygame.draw.rect(screen, "white", (90, 80, 40, 340), border_radius = 20) # slider1 rect (outer part)
    filling_height = (100, slider1.centery, 20, 310 - (slider1.centery - restrisction1_slider1))
    pygame.draw.rect(screen, "#4664fa", filling_height, border_radius = 12) # slider1 rect (filled part)
    pygame.draw.ellipse(screen, "#3858fc", slider1) # slider1 button

    # Value of rectangle (line) slider
    value = 100 - floor((slider.centery - 100 ) / 3 )
    text = font.render(f"Value1: {value}", True, "white")
    text_rect = text.get_rect(topleft = (10, 10))
    screen.blit(text, text_rect)

    # Value of rounded (rect) slider
    value1 = 100 - (slider1.centery - 102) // 3
    text1 = font.render(f"Value2: {value1}", True, "white")
    text_rect1 = text.get_rect(topleft = (300, 10))
    screen.blit(text1, text_rect1)"""
    
    slider.draw(screen)

    pygame.display.update()
    clock.tick(60)