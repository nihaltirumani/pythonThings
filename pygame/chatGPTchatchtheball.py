import pygame
import sys
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Ball")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_width, player_height = 50, 50
player_x = width - player_width // 2
player_y = height - player_height - 20
player_speed = 10

ball_radius = 20
num_balls = 5
balls = [{"x": random.randint(ball_radius, width - ball_radius), "y": 0, "delay": random.randint(0, 300)} for _ in range(num_balls)]
ball_speed = 5

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    for ball in balls:
        if ball["delay"] > 0:
            ball["delay"] -= 1
        else:
            ball["y"] += ball_speed
            if ball["y"] > height:
                ball["y"] = 0
                ball["x"] = random.randint(ball_radius, width - ball_radius)
                ball["delay"] = random.randint(0, 300)

            if (
                player_x < ball["x"] < player_x + player_width
                and player_y < ball["y"] < player_y + player_height
            ):
                score += 1
                ball["y"] = 0
                ball["x"] = random.randint(ball_radius, width - ball_radius)
                ball["delay"] = random.randint(0, 300)

    screen.fill(white)
    pygame.draw.rect(screen, black, [player_x, player_y, player_width, player_height])
    
    for ball in balls:
        pygame.draw.circle(screen, red, (ball["x"], int(ball["y"])), ball_radius)

    # Display score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)
