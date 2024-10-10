import pygame
from sys import exit
import math

def sety(ypos):
    plank_rect.y = ypos
    wood_rect.y = ypos
    dirt_rect.y = ypos
    grass_rect.y = ypos

def setx(xpos):
    plank_rect.x = xpos + 0
    wood_rect.x = xpos + 80
    dirt_rect.x = xpos + 160
    grass_rect.x = xpos + 240

def draw():
    screen.blit(plank, plank_rect)
    screen.blit(wood, wood_rect)
    screen.blit(dirt, dirt_rect)
    screen.blit(grass, grass_rect)

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Blocks")
clock = pygame.time.Clock()
pixel_font = pygame.font.Font("pygame/blocks/PixelifySans-VariableFont_wght.ttf", 50)
modern_font = pygame.font.Font("pygame/blocks/modernfont.ttc", 60)

plank = pygame.image.load("pygame/blocks/plank.png").convert_alpha()
plank_rect = plank.get_rect(center = (0, 0))
plank = pygame.transform.scale_by(plank, 10)

wood = pygame.image.load("pygame/blocks/wood.png").convert_alpha()
wood_rect = wood.get_rect(center = (80, 0))
wood = pygame.transform.scale_by(wood, 10.0)

dirt = pygame.image.load("pygame/blocks/dirt.png").convert_alpha()
dirt_rect = dirt.get_rect(center = (160, 0))
dirt = pygame.transform.scale_by(dirt, 10)

grass = pygame.image.load("pygame/blocks/grass.png").convert_alpha()
grass_rect = grass.get_rect(center = (240, 0))
grass = pygame.transform.scale_by(grass, 10)

text1 = pixel_font.render("Minecraft-Styled Blocks!", False, (0, 0, 35))
text1_rect = text1.get_rect(center = (400, 400))

text2 = modern_font.render("Wow!", True, (0, 0, 35))
text2_rect = text2.get_rect(center = (200, 150))
text2 = pygame.transform.rotate(text2, 45)

text3 = modern_font.render("Cool!", True, (0, 0, 35))
text3_rect = text3.get_rect(center = (500,  600))
text3 = pygame.transform.rotozoom(text3, 15, 1.5)

img1 = pygame.image.load("pygame/blocks/staricon.png").convert_alpha()
img1_rect = img1.get_rect(center = (163, 650))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((242, 242, 242))
   
    for i in range(3):
        setx(i * 320)
        for i in range(10):
            sety(i * 80)
            draw()

    text1_rect.y = 15 * math.sin(pygame.time.get_ticks() * 0.0025) + 400
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    screen.blit(img1, img1_rect)
    
    pygame.display.update()
    clock.tick(60)
