import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball with Gravity")

# Ball properties
ball_radius = 20
ball_pos = [WIDTH // 2, HEIGHT // 4]  # Starting position of the ball
ball_velocity_y = 0  # Initial vertical velocity
gravity = 0.5  # Gravity constant
bounce_factor = -0.7  # Controls energy loss on each bounce

# Clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Apply gravity to the ball's velocity
    ball_velocity_y += gravity
    # Update the ball's vertical position
    ball_pos[1] += ball_velocity_y

    # Check for collision with the ground
    if ball_pos[1] + ball_radius >= HEIGHT:
        ball_pos[1] = HEIGHT - ball_radius  # Keep the ball on the ground
        ball_velocity_y *= bounce_factor  # Reverse velocity and apply bounce factor

    # Fill the background with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
 