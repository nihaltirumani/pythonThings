import pygame
from pygame.math import Vector3
import sys
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Voxel")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the voxel as a cube with 8 vertices
voxel_vertices = [
    Vector3(-1, -1, -1),
    Vector3(1, -1, -1),
    Vector3(1, 1, -1),
    Vector3(-1, 1, -1),
    Vector3(-1, -1, 1),
    Vector3(1, -1, 1),
    Vector3(1, 1, 1),
    Vector3(-1, 1, 1),
]

# Define the edges of the cube
voxel_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
    (0, 4), (1, 5), (2, 6), (3, 7),  # Connecting edges
]

# Rotation angles
angle_x = 0
angle_y = 0

# Camera position
camera_position = Vector3(0, 0, -5)

def rotate_vertex(vertex, angle_x, angle_y):
    """Rotate a vertex around the X and Y axes."""
    # Rotate around the X-axis
    cos_x = math.cos(angle_x)
    sin_x = math.sin(angle_x)
    y = vertex.y * cos_x - vertex.z * sin_x
    z = vertex.y * sin_x + vertex.z * cos_x
    vertex.y, vertex.z = y, z

    # Rotate around the Y-axis
    cos_y = math.cos(angle_y)
    sin_y = math.sin(angle_y)
    x = vertex.x * cos_y + vertex.z * sin_y
    z = -vertex.x * sin_y + vertex.z * cos_y
    vertex.x, vertex.z = x, z

def project_vertex(vertex):
    """Project a 3D vertex onto the 2D screen."""
    # Adjust vertex position relative to the camera
    relative_vertex = vertex - camera_position
    distance = 5  # Distance from the camera
    fov = 200  # Field of view
    factor = fov / (distance - relative_vertex.z)
    x = int(WIDTH / 2 + relative_vertex.x * factor)
    y = int(HEIGHT / 2 - relative_vertex.y * factor)
    return x, y

def draw_voxel():
    """Draw the voxel on the screen."""
    # Rotate and project vertices
    transformed_vertices = [v.copy() for v in voxel_vertices]
    for vertex in transformed_vertices:
        rotate_vertex(vertex, angle_x, angle_y)

    # Draw edges
    for edge in voxel_edges:
        start = project_vertex(transformed_vertices[edge[0]])
        end = project_vertex(transformed_vertices[edge[1]])
        pygame.draw.line(screen, BLUE, start, end, 2)

def main():
    global angle_x, angle_y, camera_position
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle key presses for rotation and camera movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle_y -= 0.05
        if keys[pygame.K_RIGHT]:
            angle_y += 0.05
        if keys[pygame.K_UP]:
            angle_x -= 0.05
        if keys[pygame.K_DOWN]:
            angle_x += 0.05
        if keys[pygame.K_w]:
            camera_position.z += 0.1
        if keys[pygame.K_s]:
            camera_position.z -= 0.1
        if keys[pygame.K_a]:
            camera_position.x -= 0.1
        if keys[pygame.K_d]:
            camera_position.x += 0.1

        # Clear the screen
        screen.fill(WHITE)

        # Draw the voxel
        draw_voxel()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()