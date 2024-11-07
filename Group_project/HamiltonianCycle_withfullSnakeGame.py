










'''Readme file contains instructions'''









import pygame
import sys
import random
import time
import os
import subprocess 


# Initialize pygame
pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption('SNAKE 3500 Group 2')

#controls where window appears on the screen
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (750,300)

# Screen dimensions
# Calculate Cell Size based on screen dimensions and grid dimensions
cell_size = 100  # Fixed size for each grid cell

# Define Grid Dimensions in terms of cells
grid_width_cells = 7 # Number of cells horizontally
grid_height_cells = 6  # Number of cells vertically

width = cell_size * grid_width_cells  # Screen width
height = cell_size * grid_height_cells  # Screen height
screen = pygame.display.set_mode((width, height))


# grid_size can be defined directly with grid dimensions
grid_size = (grid_width_cells, grid_height_cells)


# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
purple = pygame.Color(152, 17, 247)

#globals
paths_searched = 0          #passed to gameover function
search_duration = 0         #passed to gameover
hamiltonian_path = None     #passed to gameover

# The draw_background function is used to draw onto the window the checkered background of the game.
def draw_background():
    # Draw vertical lines
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, white, (x, 0), (x, height))
    # Draw horizontal lines
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, white, (0, y), (width, y))


def draw_grid_overlay():
    # Set the color for the grid lines (semi-transparent white for overlay)
    grid_line_color = (255, 255, 255, 128)  # RGBA, 128 for semi-transparency

    # Ensure the use of a Surface that supports alpha channel (transparency)
    s = pygame.Surface((width, height), pygame.SRCALPHA)  # per-pixel alpha

    # Draw vertical grid lines
    for x in range(0, width, cell_size):
        pygame.draw.line(s, grid_line_color, (x, 0), (x, height), 1)  # 1 pixel wide lines

    # Draw horizontal grid lines
    for y in range(0, height, cell_size):
        pygame.draw.line(s, grid_line_color, (0, y), (width, y), 1)

    # Blit this surface onto the main screen
    screen.blit(s, (0,0))

# Font for text
font = pygame.font.Font(None, 36)

# Button text
play_game_text = font.render('Play Game', True, black, green)
play_game_rect = play_game_text.get_rect()
play_game_rect.center = (width // 2, height // 3)

run_algo_text = font.render('Run Hamiltonian Algorithm', True, black, red)
run_algo_rect = run_algo_text.get_rect()
run_algo_rect.center = (width // 2, 2 * height // 3)

# FPS controller
fps_controller = pygame.time.Clock()

# Snake properties
# Assuming we want to start the snake in the middle of the grid
start_x = grid_width_cells // 2
start_y = grid_height_cells // 2
snake_pos = [start_x * cell_size, start_y * cell_size]
# Initial snake body (3 segments, including the head)
snake_body = [
    [snake_pos[0], snake_pos[1]],  # Head
    [snake_pos[0] - cell_size, snake_pos[1]],  # Body segment 1
    [snake_pos[0] - 2 * cell_size, snake_pos[1]]  # Body segment 2
]


direction = 'RIGHT'
change_to = direction

# Food properties
food_pos = [random.randrange(1, grid_width_cells) * cell_size, random.randrange(1, grid_height_cells) * cell_size]
food_spawn = True

# Game settings
speed = 50

# Score
score = 0

def gameOver():
    global paths_searched, search_duration, hamiltonian_path  # Access the global counter
    print(f"Hamiltonian path found after {paths_searched} paths searched.")
    print(f"Path found in {search_duration:.2f} seconds")

    if hamiltonian_path:
        print(f"Hamiltonian path: {hamiltonian_path}")
    else:
        print("No Hamiltonian path was found.")


    my_font = pygame.font.SysFont('times new roman', 50)
    GO_surface = my_font.render('Your Score is: ' + str(score), True, red)
    GO_rect = GO_surface.get_rect()
    GO_rect.midtop = (width/2, height/4)
    screen.fill(black)
    screen.blit(GO_surface, GO_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Main loop (play_game function for manual play mode)
def play_game():
    global direction, change_to, snake_pos, snake_body, food_pos, food_spawn, score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = 'RIGHT'
        
        # Validate direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Move snake
        if direction == 'UP':
            snake_pos[1] -= cell_size
        if direction == 'DOWN':
            snake_pos[1] += cell_size
        if direction == 'LEFT':
            snake_pos[0] -= cell_size
        if direction == 'RIGHT':
            snake_pos[0] += cell_size
        
        # Snake body mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()
        
        if not food_spawn:
            food_pos = [random.randrange(1, grid_width_cells) * cell_size, random.randrange(1, grid_height_cells) * cell_size]
        food_spawn = True
    
        # Background
        screen.fill(black)
        draw_background()



        
        # Draw snake
        for pos in snake_body:
            if pos == snake_body[0]:  # Check if the segment is the head
                pygame.draw.rect(screen, purple, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
            else:  # For the rest of the body
                pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        
        # # Draw food
        # # Calculate the center of the cell by adding half the tile_size to the x and y positions
        # center_x = food_pos[0] * cell_size + cell_size // 2
        # center_y = food_pos[1] * cell_size + cell_size // 2
        
        # # Define the radius of the fruit circle, typically half the tile_size works well
        # radius = cell_size // 2
        
        # # Draw the circle on the screen
        # pygame.draw.circle(screen, red, (center_x, center_y), radius)
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width- cell_size:
            gameOver()
        if snake_pos[1] < 0 or snake_pos[1] > height-cell_size:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()
        
        pygame.display.flip()
        fps_controller.tick(speed)





def visualize_search(grid_size, path):
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Highlight the current path
    for pos in path:
        highlight_rect = pygame.Rect(pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 255, 0), highlight_rect)  # Green for current path
    
    # Draw the grid on top
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)  # White grid lines
    
    pygame.display.flip()  # Update the display



def get_adjacent_cells(grid_size, pos):
    """Generate positions adjacent to the given one within the grid boundaries."""
    x, y = pos
    grid_width, grid_height = grid_size
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
    return [(x + dx, y + dy) for dx, dy in directions if 0 <= x + dx < grid_width and 0 <= y + dy < grid_height]

def find_hamiltonian_cycle(grid_size, path, pos, start):
    global paths_searched, search_duration, hamiltonian_path
    start_time = time.time()

    visualize_search(grid_size, path) # showing current path being searched
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(10000)
    print(f"Number of Paths Searched: {paths_searched}")
    """Attempt to find a Hamiltonian cycle in the grid starting from 'start'."""
    #print(f"Checking path: {path}")  # Debug print statement to show the current path

    # Check if the path is a Hamiltonian cycle
    if len(path) == grid_size[0] * grid_size[1]:
        # Check if the last position is adjacent to the starting position
        if pos in get_adjacent_cells(grid_size, start):
            hamiltonian_path = path
            return path
        else:
            return None

    for next_pos in get_adjacent_cells(grid_size, pos):
        if next_pos not in path:
            paths_searched += 1
            path.append(next_pos)
            result = find_hamiltonian_cycle(grid_size, path, next_pos, start)
            if result:
                search_duration = time.time() - start_time
                return result
            path.pop()  # Backtrack

    search_duration = time.time() - start_time
    return None  # No Hamiltonian cycle found






    # This function calculates the next move based on the current position, current direction, and the grid size.
    # It returns the new direction and the next position of the snake.
def calculate_next_move(current_position, direction, grid_size):
    x, y = current_position
    grid_width, grid_height = grid_size

    # Implementing the specific Hamiltonian path logic
    if direction == 'RIGHT' and x < grid_width - 1 and (y > 0 and y < grid_height - 1):
        if y == 1 or y == grid_height - 2 or (x + 1) % 2 == 1:
            next_direction = 'RIGHT'
        else:
            next_direction = 'UP' if y > 1 else 'DOWN'
    elif x == 0:
        next_direction = 'DOWN' if y < grid_height - 1 else 'RIGHT'
    elif x == grid_width - 1:
        if y == 0:
            next_direction = 'LEFT'
        else:
            next_direction = 'UP'
    else:
        next_direction = 'DOWN' if (x % 2 == 0) else 'UP'

    # Calculating next position based on the next direction
    if next_direction == 'UP':
        next_position = (x, y - 1)
    elif next_direction == 'DOWN':
        next_position = (x, y + 1)
    elif next_direction == 'LEFT':
        next_position = (x - 1, y)
    elif next_direction == 'RIGHT':
        next_position = (x + 1, y)
    else:
        next_position = current_position  # Fallback to current position

    return next_direction, next_position




def run_hamiltonian_algorithm():
    global snake_pos, snake_body, food_pos, food_spawn, score, hamiltonian_path, direction



    # Before starting the game, find a Hamiltonian cycle
    #start_pos = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))  # Starting position in grid coordinates, not pixels
    start_pos =(0,2)
    hamiltonian_path = find_hamiltonian_cycle(grid_size, [start_pos], start_pos, start_pos)
    if not hamiltonian_path:
        print("Failed to find a Hamiltonian cycle")
        sys.exit(1)  # Exit if no cycle found, or handle more gracefully




    path_index = 0  # Keep track of where we are in the Hamiltonian path

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        print(f"Current Position: {snake_pos}, Direction: {direction}, Score: {score}")
        # Move along the Hamiltonian path
        grid_pos = hamiltonian_path[path_index]  # Current position in grid coordinates
        snake_pos = [grid_pos[0] * cell_size, grid_pos[1] * cell_size]  # Convert to pixel coordinates

        # Update the path index, wrapping around if necessary
        path_index = (path_index + 1) % len(hamiltonian_path)
        # Game logic 
        # Snake body mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()
        
        if not food_spawn:
            food_pos = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, (height // cell_size)) * cell_size]
            food_spawn = True

        # Background
        screen.fill(black)
        draw_background()
        
        # Draw snake
        for pos in snake_body:
            if pos == snake_body[0]:  # Check if the segment is the head
                pygame.draw.rect(screen, purple, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
            else:  # For the rest of the body
                pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        
        # # Draw food
        # # Calculate the center of the cell by adding half the tile_size to the x and y positions
        # center_x = food_pos[0] * cell_size + cell_size // 2
        # center_y = food_pos[1] * cell_size + cell_size // 2
        
        # # Define the radius of the fruit circle, typically half the tile_size works well
        # radius = cell_size // 2
        
        # # Draw the circle on the screen
        # pygame.draw.circle(screen, red, (center_x, center_y), radius)

        # # Draw food (working)
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
        # pygame.draw.rect(screen, red, pygame.Rect(food_pos[0] * cell_size, food_pos[1] * cell_size, cell_size, cell_size), border_radius=cell_size//2)
        # Assuming food_pos contains the grid coordinates of the fruit
        # center_x = food_pos[0] * cell_size + cell_size // 2
        # center_y = food_pos[1] * cell_size + cell_size // 2
        # radius = cell_size // 2  # This ensures the circle fits within the cell

        # # Draw the circle on the screen
        # pygame.draw.circle(screen, red, (center_x, center_y), radius)
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] + cell_size > width:
            gameOver()
        if snake_pos[1] < 0 or snake_pos[1] + cell_size > height:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()

        # # Draw buttons, didnt actually implement this feature, can be uncommented and used, some functionality still needs to be added
        # for button in buttons:
        #     button.draw(screen)

        draw_grid_overlay()  # Draw the grid lines on top
        pygame.display.flip()  # Update the display
        fps_controller.tick(speed)



#Button functionality to adjust speed (fast forward mechanic). This logic needs to adjust the flip() / render time where it only renders 
## every Nth frame, where N increases with the speed multiplier. For example, at 10x speed, it renders every 10th frame (this should make things move much faster)
class Button:
    def __init__(self, text, x, y, width, height, command):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(text, True, black)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, white, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def click(self, event_pos):
        if self.rect.collidepoint(event_pos):
            self.command()

def set_speed_multiplier(multiplier):
    global speed_multiplier, render_every_n_frames
    speed_multiplier = multiplier
    render_every_n_frames = multiplier
    print(f"Speed set to {speed_multiplier}x")


# Initialize buttons
buttons = [
    Button("1x", 50, 10, 80, 40, lambda: set_speed_multiplier(1)),
    Button("10x", 150, 10, 80, 40, lambda: set_speed_multiplier(10)),
    Button("100x", 250, 10, 80, 40, lambda: set_speed_multiplier(100)),
    Button("1000x", 350, 10, 80, 40, lambda: set_speed_multiplier(1000)),
]




# Main menu function
def main_menu():
    while True:
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_game_rect.collidepoint(event.pos):
                    play_game()
                elif run_algo_rect.collidepoint(event.pos):
                    run_hamiltonian_algorithm()
        screen.blit(play_game_text, play_game_rect)
        screen.blit(run_algo_text, run_algo_rect)
        pygame.display.flip()




# Start with the main menu
if __name__ == "__main__":
    main_menu()