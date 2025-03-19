import pygame
import noise

# Constants
GRID_SIZE = 50  # Number of rows and columns
BOX_SIZE = 10   # Size of each box in pixels
SCALE = 10.0    # Controls how smooth the Perlin noise is

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * BOX_SIZE, GRID_SIZE * BOX_SIZE))
pygame.display.set_caption("Perlin Noise Grid")

# Generate Perlin noise grid (binary 0 or 1)
perlin_noise = [[noise.pnoise2(x / SCALE, y / SCALE) for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# Convert Perlin noise to binary (0 or 255)
binary_noise = [[255 if perlin_noise[y][x] > 0 else 0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    
    # Draw the Perlin noise grid
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = (binary_noise[y][x], binary_noise[y][x], binary_noise[y][x])  # Convert to RGB
            pygame.draw.rect(screen, color, (x * BOX_SIZE, y * BOX_SIZE, BOX_SIZE, BOX_SIZE))

    pygame.display.flip()  # Update display
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
