import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 102)

# Player settings
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]
player_speed = 5
max_health = 100
player_health = max_health

# Enemy settings
enemy_size = 50
enemy_pos = [100, 100]
enemy_speed = 3
damage_per_second = 20

# Coin settings
coin_size = 25
coins = []
coin_spawn_time = random.uniform(2.00, 4.00)
coin_last_spawn = time.time()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Create the screen object
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game clock
clock = pygame.time.Clock()
frame_rate = 30
damage_per_frame = damage_per_second / frame_rate

# Main game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed
    if keys[pygame.K_a] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed

    # Enemy movement towards player
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed

    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

    # Check for collision with enemy
    if (abs(player_pos[0] - enemy_pos[0]) < player_size) and (abs(player_pos[1] - enemy_pos[1]) < player_size):
        player_health -= damage_per_frame

    if player_health <= 0:
        game_over = True

    # Spawn new coins after interval
    if time.time() - coin_last_spawn > coin_spawn_time:
        new_coin_pos = [random.randint(0, screen_width - coin_size), random.randint(0, screen_height - coin_size)]
        coins.append(new_coin_pos)
        coin_last_spawn = time.time()
        coin_spawn_time = random.uniform(2.00, 4.00)

    # Check for collision with coins
    for coin in coins[:]:
        if (abs(player_pos[0] - coin[0]) < player_size) and (abs(player_pos[1] - coin[1]) < player_size):
            coins.remove(coin)
            score += 1

    # Fill the screen with black
    screen.fill(black)

    # Draw the player and enemy
    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Draw the coins
    for coin in coins:
        pygame.draw.rect(screen, yellow, (coin[0], coin[1], coin_size, coin_size))

    # Display the score
    score_text = font.render(f"Coins: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # Display the health
    health_text = font.render(f"Health: {int(player_health)}", True, white)
    screen.blit(health_text, (screen_width - 150, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(frame_rate)

# End of game
pygame.quit()
sys.exit()