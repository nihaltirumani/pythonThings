import pygame

def bouncing_rect():
    global speed_x, speed_y
    moving_rect.x += speed_x
    moving_rect.y += speed_y

    # collision with screen borders
    if moving_rect.right >= screen_width or moving_rect.left <= 0:
        speed_x *= -1
    if moving_rect.bottom >= screen_heigth  or moving_rect.top <= 0:
        speed_y *= -1

    # collision with other_rect
    if moving_rect.colliderect(other_rect):
        if other_rect.top - moving_rect.bottom:
            speed_y *= -1

    pygame.draw.rect(screen, (255, 255, 255), moving_rect)
    pygame.draw.rect(screen, (255, 0, 0), other_rect)




pygame.init()

clock = pygame.time.Clock()
screen_heigth = 800
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_heigth))
running = True

moving_rect = pygame.Rect(350, 350, 100, 100)
speed_x, speed_y = 5, 4

other_rect = pygame.Rect(300, 600, 200, 100)
other_speed = 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    bouncing_rect()

    pygame.display.flip()
    clock.tick(60)