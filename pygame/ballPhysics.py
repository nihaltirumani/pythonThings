import pygame 
from sys import exit
import math

pygame.init()

class ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.color = "blue"
        self.velx = 0
        self.vely = 0

    def update(self):
        self.movement()
        self.collision()
        self.draw()

    def draw(self):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius + 5)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    def movement(self):
        self.vely += 1
        self.y += self.vely
        self.x += self.velx

    def collision(self):
        if self.y > (HEIGHT - self.radius):
            while self.y > (HEIGHT - self.radius) : self.y -= 1
            self.vely = 0

        if self.x > (WIDTH - self.radius):
            while self.x > (WIDTH - self.radius) : self.x -= 1
            self.velx = 0
        elif self.x < self.radius:
            while self.x < self.radius : self.x += 1
            self.velx = 0

    def fire(self, angle, speed):
        self.velx = speed * math.sin(angle)
        self.vely = speed * math.cos(angle)

WIDTH = 800
HEIGHT = 400
CENTERX = WIDTH / 2
CENTERY = HEIGHT / 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Physics")
clock = pygame.time.Clock()

ball1 = ball(CENTERX, CENTERY)
old_mouse = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("orange2")

    ball1.update()

    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    if old_mouse == 1 and mouse[0] == 0 :
        ball1.fire(math.atan2(mouse_pos[0] - ball1.x, mouse_pos[1] - ball1.y), 20)
    old_mouse = mouse[0]

    pygame.display.update()
    clock.tick(60)