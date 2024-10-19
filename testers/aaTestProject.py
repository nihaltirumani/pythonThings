import pygame 
from sys import exit

class Laser():
    def __init__(self, color1, color2, color3, pos1, pos2, size):
        self.color1 = color1  # Outer color
        self.color2 = color2  # Middle color
        self.color3 = color3  # Inner color
        self.pos1 = pos1  # Start position
        self.pos2 = pos2  # End position
        self.size = size  # Base size multiplier

    def draw(self):
        # Draw three lines with decreasing thickness to create a layered laser effect
        pygame.draw.line(trans_surf, self.color1, self.pos1, self.pos2, int(self.size * 20))
        pygame.draw.line(trans_surf, self.color2, self.pos1, self.pos2, int(self.size * 12))
        pygame.draw.line(trans_surf, self.color3, self.pos1, self.pos2, int(self.size * 4))

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Lasers")
clock = pygame.time.Clock()

# Transparent surface for drawing lasers
trans_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

# Laser colors: outer, middle, and inner colors (red to white gradient for a glowing effect)
laser1 = Laser((255, 0, 0, 122), (255, 100, 100, 255), (255, 255, 255, 255), (0, 0), (600, 600), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((230, 230, 230))

    # Reset the transparent surface to clear old drawings
    trans_surf.fill((0, 0, 0, 0))  # Fully transparent background

    # Draw the laser directly using the class method
    laser1.draw()

    # Blit the transparent surface onto the main screen
    screen.blit(trans_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)
