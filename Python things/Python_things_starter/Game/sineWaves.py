import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sine Wave Animation")

# Sine wave parameters
amplitude = 100
frequency = 0.01

# Set up clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the sine wave
    for x in range(width):
        y = int(amplitude * math.sin(frequency * x + pygame.time.get_ticks() * 0.005) + height / 2)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 2)
    for x in range(width):
        y = int(amplitude * math.sin(frequency * x + pygame.time.get_ticks() * 0.005) + (height+50) / 2)
        pygame.draw.circle(screen, (0, 255, 255), (x, y), 2)
    for x in range(width):
        y = int(amplitude * math.sin(frequency * x + pygame.time.get_ticks() * 0.005) + (height-50) / 2)
        pygame.draw.circle(screen, (0, 255, 255), (x, y), 2)


    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # Adjust this value for desired frames per second
