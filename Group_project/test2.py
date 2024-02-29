import pygame
import time

# Initialize pygame
pygame.init()

# Grid size
width, height = 600, 600
rows, cols = 20, 20
grid_size = width // cols

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Set up display
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game with Hamiltonian Cycle")

# Hamiltonian path function
def create_hamiltonian_path():
    path = []
    for y in range(rows):
        for x in range(cols if y % 2 == 0 else -1, -1 if y % 2 == 0 else cols, -1 if y % 2 == 0 else 1):
            path.append((x, y))
    return path

# Snake class
class Snake:
    def __init__(self):
        self.positions = [(0, 0)] # Initial position of the snake
        self.path = create_hamiltonian_path()
        self.path_index = 0

    def move(self):
        self.path_index = (self.path_index + 1) % len(self.path)
        self.positions[0] = self.path[self.path_index]

    def draw(self, surface):
        for pos in self.positions:
            r = pygame.Rect((pos[0] * grid_size, pos[1] * grid_size), (grid_size, grid_size))
            pygame.draw.rect(surface, green, r)

def redraw_window(surface):
    global snake
    surface.fill(black)
    snake.draw(surface)
    pygame.display.update()

# Main loop
def main():
    global snake
    snake = Snake()
    clock = pygame.time.Clock()
    
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        redraw_window(win)

main()
