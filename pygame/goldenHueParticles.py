"""
This project uses particle class and demonstrates the flexibility of classes
"""

import pygame
from sys import exit
from random import randint, choice

class Particle:
    def __init__(self):
        self.particles = []
        self.shiny_colors = [
        (255, 255, 204),  # Very Pale Yellow
        (255, 255, 153),  # Light Yellow
        (255, 223, 102),  # Golden Yellow
        (255, 204, 51),   # Bright Gold
        (255, 184, 28),   # Rich Golden
        (204, 153, 0),    # Deep Gold
        (255, 255, 128)   # Shiny Gold Highlight
        ]

    def emit(self):
        if self.particles:
            self.delete_particles() 
            for particle in self.particles:
                particle[3] += 0.1
                particle[1] += particle[3]
                #particle[3] *= 0.98
                particle[0] += particle[2]
                pygame.draw.circle(screen, particle[4], (particle[0], particle[1]), particle[5])

    def create_particles(self, xpos, ypos):
        x = xpos
        y = ypos
        speedx = randint(-10, 10)
        speedy = randint(-18, -5)
        color = choice(self.shiny_colors)
        radius = randint(8, 13)
        particle = [x, y, speedx, speedy, color, radius]
        self.particles.append(particle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] < 850]
        self.particles = particle_copy

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Golden Hues")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

text = font.render("Golden Hues", True, (255, 191, 0))
text_rect = text.get_rect(center = (400, 200))
particle1 = Particle()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((255, 255, 204))

    screen.blit(text, text_rect)

    particle1.create_particles(400, 820)

    particle1.emit()
    
    pygame.display.update()
    clock.tick(60)