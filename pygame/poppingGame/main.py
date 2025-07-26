import pygame 
from sys import exit
from random import randint
import math

class Dart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dart = pygame.image.load('pygame/poppingGame/Assets/images/dart.png').convert_alpha()
        self.dart = pygame.transform.scale_by(self.dart, 0.75)
        self.dart_rect = self.dart.get_rect(center = (self.x, self.y))
        self.old_mouse = False
        self.angle = 0
        self.speed = 25
        self.velx = 0
        self.vely = 0
        self.throw = 0

    def update(self):
        self.pointing()
        self.respawn()
        self.shoot(mouse[0])
        self.movement()
        self.draw()

    def pointing(self):
        if dart_.throw < 1:
            dx = mouse_pos[0] - self.dart_rect.centerx
            dy = mouse_pos[1] - self.dart_rect.centery
            self.angle = -math.degrees(math.atan2(dy, dx))
        else:
            if self.angle < -89 :
                self.angle = -90
            else:
                self.angle -= 3
                if self.angle < 0:
                    self.angle %= 360
                elif self.angle > 0:
                    self.angle %= 360

    def draw(self):
        screen.blit(pygame.transform.rotate(self.dart, self.angle), pygame.transform.rotate(self.dart, self.angle).get_rect(center = self.dart_rect.center))

    def shoot(self, mouse):
        if self.old_mouse and not mouse and self.throw < 1:
            mx, my = pygame.mouse.get_pos()
            dx = mx - self.dart_rect.centerx
            dy = my - self.dart_rect.centery
            distance = math.hypot(dx, dy) or 1  # avoid division by 0
            self.velx = (dx / distance) * self.speed
            self.vely = (dy / distance) * self.speed

            self.throw += 1
        self.old_mouse = mouse

    def movement(self):
        self.dart_rect.centerx += self.velx
        self.dart_rect.centery += self.vely

        if self.throw > 0:
            self.vely += 1

    def respawn(self):
        if self.dart_rect.centery > WIDTH:
            self.throw = 0
            dx = mouse_pos[0] - dart_.dart_rect.centerx
            dy = mouse_pos[1] - dart_.dart_rect.centery
            self.angle = -math.degrees(math.atan2(dy, dx))
            self.velx = 0
            self.vely = 0
            self.dart_rect.centerx = self.x
            self.dart_rect.centery = self.y

class Balloon:
    def __init__(self, x, y, health):
        self.health = health
        self.health_ = health
        self.balloon = pygame.image.load(f"pygame/poppingGame/Assets/images/{types[self.health]}_balloon.png").convert_alpha()
        self.balloon = pygame.transform.scale_by(self.balloon, 0.4)
        self.balloon_rect = self.balloon.get_rect(center=(x, y))
        self.popped = False
        self.poptime = 0

    def update(self):
        self.draw()

    def draw(self):
        self.balloon = pygame.image.load(f"pygame/poppingGame/Assets/images/{types[self.health]}_balloon.png").convert_alpha()
        self.balloon = pygame.transform.scale_by(self.balloon, 0.4)
        screen.blit(self.balloon, self.balloon_rect)

def create_ballons():
    global grid, balloons
    grid = [randint(0,3) for i in range(SIDE ** 2)]
    balloons = [Balloon((x * 100) + 400, (y * 100) + 150, (grid[(y * SIDE) + x]) ) for x in range(SIDE) for y in range(SIDE)]

pygame.init()

WIDTH = 800
HEIGHT = 600
SIDE = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloons Popping game")
clock = pygame.time.Clock()
font1 = pygame.font.Font("pygame/poppingGame/Assets/font/LuckiestGuy-Regular.ttf", 50)
font2 = pygame.font.Font("pygame/poppingGame/Assets/font/LuckiestGuy-Regular.ttf", 150)
font3 = pygame.font.Font("pygame/poppingGame/Assets/font/LuckiestGuy-Regular.ttf", 160)

types = ["red", "blue", "green", "yellow", "pop"]
grid = []
balloons = []
balloons_empty = [None for i in range(SIDE ** 2)]
create_ballons()

points = 0
end_game_count = 0

dart_ = Dart(200, 300)

text1 = font1.render(f"Points: {points}", True, "green")
text1_rect = text1.get_rect(topleft = (10, 10))

text2 = font3.render(f"YOU WON!", True, "green")
text2_rect = text2.get_rect(center = (WIDTH / 2, HEIGHT / 2))

text3 = font2.render(f"YOU WON!", True, "green")
text3_rect = text3.get_rect(center = (WIDTH / 2, HEIGHT / 2))

pop = pygame.mixer.Sound("pygame/poppingGame/Assets/sounds/pop.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("skyblue")

    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    keys = pygame.key.get_pressed()

    if balloons == balloons_empty:
        end_game_count += 1

        if end_game_count >= 60:
            pygame.quit()
            exit()

    for bloon in balloons:
        if bloon != None:
            bloon.update()

    for bloon in balloons.copy():
        if bloon != None and dart_.dart_rect.colliderect(bloon.balloon_rect) and bloon.popped == False:
            bloon.popped = True
            bloon.poptime = 0
            bloon.health -= 1
            bloon.health_ = bloon.health
            points += 1
            pop.play()

            if bloon.health < 0 :
                balloons.insert(balloons.index(bloon), None)
                balloons.remove(bloon)

        if bloon != None and bloon.popped == True:
            bloon.poptime += 1
            if bloon.poptime >= 0  and bloon.poptime < 11:
                bloon.health = 4
            else:
                bloon.health = bloon.health_

        if dart_.throw == 0 and bloon != None:
            bloon.popped = False

    dart_.update()

    text1 = font1.render(f"Points: {points}", True, "black")
    text1_rect = text1.get_rect(topleft = (10, 10))
    screen.blit(text1, text1_rect)

    if balloons == balloons_empty: 
        text2 = font3.render(f"YOU WON!", True, "chartreuse4")
        text2_rect = text2.get_rect(center = (WIDTH / 2, HEIGHT / 2))
        screen.blit(text2, text2_rect)

        text2 = font2.render(f"YOU WON!", True, "chartreuse3")
        text2_rect = text2.get_rect(center = (WIDTH / 2, HEIGHT / 2))
        screen.blit(text2, text2_rect)

    pygame.display.update()
    clock.tick(60)