import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
obj = pygame.Rect(400, 300, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), obj)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        obj.y -= 5
    if keys[pygame.K_s]:
        obj.y += 5
    if keys[pygame.K_a]:
        obj.x -= 5
    if keys[pygame.K_d]:
        obj.x += 5


    pygame.display.flip()
    clock.tick(60)
