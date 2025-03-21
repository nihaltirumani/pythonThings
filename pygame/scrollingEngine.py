import pygame
from sys import exit

class Movingrect:
    def __init__(self, xpos, ypos, spy, spx, p1x, p2x, p1y, p2y, color):
        self.x = xpos
        self.y = ypos
        self.point1x = p1x
        self.point2x = p2x
        self.point1y = p1y
        self.point2y = p2y
        self.speedy = spy
        self.setspeedy = spy
        self.speedx = spx
        self.setspeedx = spx
        self.color = color

    def draw(self, scrollx, scrolly):
        self.x += self.speedx
        self.y += self.speedy

        if self.x < self.point1x: self.speedx = self.setspeedx
        if self.x > self.point2x: self.speedx = -self.setspeedx
        if self.y < self.point1y: self.speedy = self.setspeedy
        if self.y > self.point2y: self.speedy = -self.setspeedy

        pygame.draw.rect(screen, self.color, (self.x - scrollx, self.y + scrolly, TILE_SIZE, TILE_SIZE))

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Scrolling Engine")
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None, 40)

TILE_SIZE = 40

scrollx = 0
scrolly = 0

scroll_speed = 2

scrollyvelo = 0
scrollxvelo = 0

friction = 0.95

text1 = font1.render("Welcome to Scrolling Engine", True, "tomato")
text1_rect = text1.get_rect(center = (400, 200))

text2 = font2.render(f"Scroll X: {scrollx}", True, "black")
text2_rect = text2.get_rect(center = (75, 20))

text3 = font2.render(f"Scroll Y: {scrolly}", True, "black")
text3_rect = text3.get_rect(center = (75, 50))

moving_rect1 = Movingrect(-400, 400, 2, 0, 0, 0, 100, 400, "lightblue4")
moving_rect2 = Movingrect(-400, 400, 0, 2, -700, -400, 0, 0, "royalblue1")

moving_rects1 = [Movingrect(TILE_SIZE * i, 480 + (i * TILE_SIZE), 2, 0, 0, 0, 480 + (i * TILE_SIZE), 480 + (i * TILE_SIZE) + 300, "red") for i in range(20)]
moving_rects2 =[Movingrect(TILE_SIZE * i, -500, 0, 4, (TILE_SIZE * i), (TILE_SIZE * (i + 15)), 0, 0, "khaki1") for i in range(5)]
moving_rects3 =[Movingrect((TILE_SIZE * (i + 15)), 60, 0, 4, (TILE_SIZE * i), (TILE_SIZE * (i + 15)), 0, 0, "khaki1") for i in range(5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("cyan1")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]: scrollyvelo += scroll_speed
    if keys[pygame.K_s]: scrollyvelo -= scroll_speed
    if keys[pygame.K_a]: scrollxvelo -= scroll_speed
    if keys[pygame.K_d]: scrollxvelo += scroll_speed

    scrollyvelo *= friction
    scrollxvelo *= friction

    scrollx += scrollxvelo
    scrolly += scrollyvelo

    for j in range(4):
        for i in range(20):
            x = (TILE_SIZE * i - scrollx)
            y = (320 + (j * TILE_SIZE)) + scrolly
            pygame.draw.rect(screen, "chartreuse4", pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

    for j in range(15):
        for i in range(20):
            x = (TILE_SIZE * i - scrollx)
            y = (-500 + (j * TILE_SIZE)) + scrolly
            pygame.draw.rect(screen, "cyan3", pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

    for moving_rect in moving_rects1: moving_rect.draw(scrollx, scrolly)
    for moving_rect in moving_rects2: moving_rect.draw(scrollx, scrolly)
    for moving_rect in moving_rects3: moving_rect.draw(scrollx, scrolly)

    moving_rect1.draw(scrollx, scrolly)
    moving_rect2.draw(scrollx, scrolly)

    text1_rect.centerx = 400 - scrollx
    text1_rect.centery = 200 + scrolly

    text2 = font2.render(f"Scroll X: {round(scrollx)}", True, "black")
    text3 = font2.render(f"Scroll Y: {round(scrolly)}", True, "black")

    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    pygame.display.update()
    clock.tick(60)