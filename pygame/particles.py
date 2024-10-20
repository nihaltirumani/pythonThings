import pygame
from sys import exit
from random import randint

def draw_partcles(particle_list):
    if particle_list:
        for particle in particle_list:
            particle[2] += 1
            particle[1] += particle[2]
            #particle[3] *= 0.98
            particle[0] += particle[3]

            pygame.draw.circle(screen, particle[4], (particle[0], particle[1]), particle[5])

            particle_list = [particle for particle in particle_list if particle[1] < 789]

        return particle_list
    else: return []

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Particles")
clock = pygame.time.Clock()

particles = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.fill((240, 240, 240))

    if pygame.mouse.get_pressed()[0]:
        for i in range(1):
            particles.append([event.pos[0], event.pos[1], randint(-18, -5), randint(-10, 10), (randint(0, 255), randint(0, 255), randint(0, 255)), randint(8, 13)])

    particles = draw_partcles(particles)
    
    pygame.display.update()
    clock.tick(60)