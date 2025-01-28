import pygame
from sys import exit
from math import floor

class Slider:
    def __init__(self, xpos: int, ypos: int, value: int, y_limits: tuple):
        self.x = xpos
        self.y = ypos
        self.value = value
        self.y_limits = y_limits  # Restriction for slider movement
        self.old_mouse_pressed = False

        self.slider_button_width = 30
        self.slider_button_height = 10
        self.slider_button = pygame.Rect(
            self.x - (self.slider_button_width / 2),
            self.y - self.slider_button_height / 2,
            self.slider_button_width,
            self.slider_button_height
        )

    def detect(self, mx, my, mouse_pressed):
        mouse_pressed = mouse_pressed[0]  # Left mouse button
        if (mouse_pressed and self.x - 15 < mx < self.x + 15 and self.y - 10 < my < self.y + 10) or self.old_mouse_pressed:
            self.y = max(self.y_limits[0], min(my - self.slider_button_height / 2, self.y_limits[1]))  # Clamp y position
            self.old_mouse_pressed = mouse_pressed  # Update press state

    def draw(self, screen):
        # Update slider button's rectangle position
        self.slider_button.y = self.y

        # Draw the slider background and filled portion
        pygame.draw.line(screen, "white", (self.x, self.y_limits[1] + 10), (self.x, self.y_limits[0] - 10), 40)
        pygame.draw.line(screen, "#4664fa", (self.x, self.y_limits[1]), (self.x, self.y), 20)
        pygame.draw.rect(screen, "#3858fc", self.slider_button)

pygame.init()

# Set up the screen and clock
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sliders")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Create a slider object with vertical limits (100, 400)
slider = Slider(100, 100, 300, (100, 400))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((50, 50, 50))

    # Get mouse state
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Update and draw the slider
    slider.detect(mouse_pos[0], mouse_pos[1], mouse)  # Correct mouse position input
    slider.draw(screen)

    pygame.display.update()
    clock.tick(60)