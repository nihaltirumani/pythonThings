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

        pygame.draw.rect(screen, self.color, (self.x - scrollx, self.y + scrolly, 40, 40))


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Scrolling Engine")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 80)

scrollx = 0
scrolly = 0

scroll_speed = 2

scrollyvelo = 0
scrollxvelo = 0

friction = 0.95

text1 = font.render("Welcome to Scrolling Engine", True, "tomato")
text1_rect = text1.get_rect(center = (400, 200))

moving_rect1 = Movingrect(-400, 400, 2, 0, 0, 0, 100, 400, "lightblue4")
moving_rect2 = Movingrect(-400, 400, 0, 2, -700, -400, 0, 0, "royalblue1")

moving_rects = [Movingrect(40 * i, 480 + (i * 40), 2, 0, 0, 0, 480 + (i * 40), 480 + (i * 40) + 300, "red") for i in range(20)]


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
            x = (40 * i - scrollx)
            y = (320 + (j * 40)) + scrolly
            pygame.draw.rect(screen, "chartreuse4", pygame.Rect(x, y, 40, 40))

    for moving_rect in moving_rects:
        moving_rect.draw(scrollx, scrolly)

    moving_rect1.draw(scrollx, scrolly)
    moving_rect2.draw(scrollx, scrolly)

    text1_rect.centerx = 400 - scrollx
    text1_rect.centery = 200 + scrolly

    screen.blit(text1, text1_rect)

    pygame.display.update()
    clock.tick(60)