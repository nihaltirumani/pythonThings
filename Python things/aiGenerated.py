import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avoider Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Set up game states
GAME_STATE_START = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2

# Set up the player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 2 * player_size
player_speed = 5

# Set up obstacles
obstacle_size = 50
obstacle_x = random.randint(0, screen_width - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 3

# Set up slow obstacle
slow_obstacle_size = 100
slow_obstacle_x = random.randint(0, screen_width - slow_obstacle_size)
slow_obstacle_y = -slow_obstacle_size
slow_obstacle_speed = 1

# Set up small obstacle
small_obstacle_size = 25
small_obstacle_x = random.randint(0, screen_width - small_obstacle_size)
small_obstacle_y = -small_obstacle_size
small_obstacle_speed = 8

# Set up power-up
power_up_size = 30
power_up_x = random.randint(0, screen_width - power_up_size)
power_up_y = -power_up_size
power_up_speed = 4
power_up_type = None
power_up_active = False

# Set up score and lives
score = 0
player_lives = 3
best_score = 0

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up buttons
button_width = 100
button_height = 50
button_x = screen_width // 2 - button_width // 2
button_y = screen_height // 2 + 50

# Set up game clock
clock = pygame.time.Clock()

# Set up game state
game_state = GAME_STATE_START

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == GAME_STATE_START:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    game_state = GAME_STATE_PLAYING

            elif game_state == GAME_STATE_GAME_OVER:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    # Reset game variables
                    obstacle_x = random.randint(0, screen_width - obstacle_size)
                    obstacle_y = -obstacle_size
                    slow_obstacle_x = random.randint(0, screen_width - slow_obstacle_size)
                    slow_obstacle_y = -slow_obstacle_size
                    small_obstacle_x = random.randint(0, screen_width - small_obstacle_size)
                    small_obstacle_y = -small_obstacle_size
                    power_up_x = random.randint(0, screen_width - power_up_size)
                    power_up_y = -power_up_size
                    power_up_active = False
                    score = 0
                    player_lives = 3
                    game_state = GAME_STATE_PLAYING

    if game_state == GAME_STATE_START:
        # Start screen
        window.fill(WHITE)
        start_text = font.render("Click Play to Start", True, BLACK)
        start_button = pygame.draw.rect(window, GREEN, (button_x, button_y, button_width, button_height))
        start_button_text = font.render("Play", True, BLACK)
        window.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, screen_height // 2 - 50))
        window.blit(start_button_text, (button_x + button_width // 2 - start_button_text.get_width() // 2,
                                         button_y + button_height // 2 - start_button_text.get_height() // 2))
        pygame.display.update()

    elif game_state == GAME_STATE_PLAYING:
        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # Move the obstacles
        obstacle_y += obstacle_speed
        slow_obstacle_y += slow_obstacle_speed
        small_obstacle_y += small_obstacle_speed
        power_up_y += power_up_speed

        # Check for obstacle reaching the end
        if obstacle_y > screen_height:
            obstacle_x = random.randint(0, screen_width - obstacle_size)
            obstacle_y = -obstacle_size

        # Check for slow obstacle reaching the end
        if slow_obstacle_y > screen_height:
            slow_obstacle_x = random.randint(0, screen_width - slow_obstacle_size)
            slow_obstacle_y = -slow_obstacle_size

        # Check for small obstacle reaching the end
        if small_obstacle_y > screen_height:
            small_obstacle_x = random.randint(0, screen_width - small_obstacle_size)
            small_obstacle_y = -small_obstacle_size

        # Check for power-up reaching the end
        if power_up_y > screen_height:
            if random.random() < 0.15:  # 15% chance for life power-up
                power_up_type = "life"
                power_up_x = random.randint(0, screen_width - power_up_size)
                power_up_y = -power_up_size
                power_up_active = True
            elif random.random() < 0.5:  # 50% chance for score power-up
                power_up_type = "score"
                power_up_x = random.randint(0, screen_width - power_up_size)
                power_up_y = -power_up_size
                power_up_active = True

        # Check for collision with obstacles
        if player_x < obstacle_x + obstacle_size and player_x + player_size > obstacle_x and \
                player_y < obstacle_y + obstacle_size and player_y + player_size > obstacle_y:
            player_lives -= 1
            if player_lives <= 0:
                game_state = GAME_STATE_GAME_OVER
                if score > best_score:
                    best_score = score
            else:
                obstacle_x = random.randint(0, screen_width - obstacle_size)
                obstacle_y = -obstacle_size
                score += 1

        # Check for collision with slow obstacles
        if player_x < slow_obstacle_x + slow_obstacle_size and player_x + player_size > slow_obstacle_x and \
                player_y < slow_obstacle_y + slow_obstacle_size and player_y + player_size > slow_obstacle_y:
            player_lives -= 2
            if player_lives <= 0:
                game_state = GAME_STATE_GAME_OVER
                if score > best_score:
                    best_score = score
            else:
                slow_obstacle_x = random.randint(0, screen_width - slow_obstacle_size)
                slow_obstacle_y = -slow_obstacle_size

        # Check for collision with small obstacles
        if player_x < small_obstacle_x + small_obstacle_size and player_x + player_size > small_obstacle_x and \
                player_y < small_obstacle_y + small_obstacle_size and player_y + player_size > small_obstacle_y:
            player_lives -= 1
            if player_lives <= 0:
                game_state = GAME_STATE_GAME_OVER
                if score > best_score:
                    best_score = score
            else:
                small_obstacle_x = random.randint(0, screen_width - small_obstacle_size)
                small_obstacle_y = -small_obstacle_size

        # Check for collision with power-ups
        if player_x < power_up_x + power_up_size and player_x + player_size > power_up_x and \
                player_y < power_up_y + power_up_size and player_y + player_size > power_up_y:
            if power_up_type == "life":
                player_lives += 1
            elif power_up_type == "score":
                score += 1
            power_up_x = random.randint(0, screen_width - power_up_size)
            power_up_y = -power_up_size
            power_up_active = False

        # Fill the background
        window.fill(WHITE)

        # Draw the player
        pygame.draw.rect(window, BLACK, (player_x, player_y, player_size, player_size))

        # Draw the obstacles
        pygame.draw.rect(window, RED, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
        pygame.draw.rect(window, BLUE, (slow_obstacle_x, slow_obstacle_y, slow_obstacle_size, slow_obstacle_size))
        pygame.draw.rect(window, YELLOW, (small_obstacle_x, small_obstacle_y, small_obstacle_size, small_obstacle_size))

        # Draw the power-up
        if power_up_active:
            if power_up_type == "life":
                pygame.draw.rect(window, GREEN, (power_up_x, power_up_y, power_up_size, power_up_size))
            elif power_up_type == "score":
                pygame.draw.rect(window, ORANGE, (power_up_x, power_up_y, power_up_size, power_up_size))

        # Draw the score and lives
        score_text = font.render("Score: " + str(score), True, BLACK)
        lives_text = font.render("Lives: " + str(player_lives), True, BLACK)
        best_score_text = font.render("Best Score: " + str(best_score), True, BLACK)
        window.blit(score_text, (10, 10))
        window.blit(lives_text, (10, 50))
        window.blit(best_score_text, (10, 90))

        # Update the display
        pygame.display.update()

    elif game_state == GAME_STATE_GAME_OVER:
        # Game over screen
        window.fill(WHITE)
        game_over_text = font.render("Game Over", True, BLACK)
        score_text = font.render("Final Score: " + str(score), True, BLACK)
        best_score_text = font.render("Best Score: " + str(best_score), True, BLACK)
        restart_button = pygame.draw.rect(window, RED, (button_x, button_y, button_width, button_height))
        restart_button_text = font.render("Restart", True, BLACK)
        window.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
        window.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2))
        window.blit(best_score_text, (screen_width // 2 - best_score_text.get_width() // 2, screen_height // 2 + 50))
        window.blit(restart_button_text, (button_x + button_width // 2 - restart_button_text.get_width() // 2,
                                           button_y + button_height // 2 - restart_button_text.get_height() // 2))
        pygame.display.update()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
