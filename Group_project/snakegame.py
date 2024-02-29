import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

# Define Grid Dimensions in terms of cells
grid_width_cells = 60  # Number of cells horizontally
grid_height_cells = 40  # Number of cells vertically

# Calculate Cell Size based on screen dimensions and grid dimensions
cell_size = width // grid_width_cells  # Assuming square cells for simplicity

# Now, your grid_size can be defined directly with grid dimensions
grid_size = (grid_width_cells, grid_height_cells)


# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

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
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food properties
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Game settings
speed = 15

# Score
score = 0

def gameOver():
    my_font = pygame.font.SysFont('times new roman', 90)
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
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10
        
        # Snake body mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()
        
        if not food_spawn:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True
    
        # Background
        screen.fill(black)
        
        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        # Draw food
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-10:
            gameOver()
        if snake_pos[1] < 0 or snake_pos[1] > height-10:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()
        
        pygame.display.flip()
        fps_controller.tick(speed)



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

def generate_hamiltonian_path(grid_width, grid_height):
    path = []
    for y in range(grid_height):
        # Move right on even rows, left on odd rows
        if y % 2 == 0:
            for x in range(1, grid_width):  # Assuming starting at 0,0
                path.append("RIGHT")
        else:
            for x in range(grid_width - 1, 0, -1):
                path.append("LEFT")
        # Move down at the end of each row if not at the last row
        if y < grid_height - 1:
            path.append("DOWN")
    return path

# Example usage:
grid_width = width // cell_size
grid_height = height // cell_size
hamiltonian_path = generate_hamiltonian_path(grid_width, grid_height)
# Now, in your game loop, follow the hamiltonian_path directions for the snake's movement


def run_hamiltonian_algorithm():
    global direction, snake_pos, snake_body, food_pos, food_spawn, score, cell_size, grid_size

    # Calculate grid dimensions based on screen size and cell size
    grid_width_cells = width // cell_size
    grid_height_cells = height // cell_size

    # Generate the Hamiltonian path
    hamiltonian_path = generate_hamiltonian_path(grid_width_cells, grid_height_cells)
    path_index = 0  # Start at the beginning of the Hamiltonian path

    while True:
        # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate the next move based on the Hamiltonian path
        direction, next_pos = calculate_next_move(snake_pos, direction, grid_size)

        # Directly update snake position based on the next position
        #snake_pos = list(next_pos)

        # Debug output
        print(f"Current Position: {snake_pos}, Next Position: {next_pos}, Direction: {direction}")

        # Follow the Hamiltonian path
        direction = hamiltonian_path[path_index]
        # Update the snake position based on the current direction
        if direction == 'RIGHT':
            snake_pos[0] += cell_size
        elif direction == 'LEFT':
            snake_pos[0] -= cell_size
        elif direction == 'DOWN':
            snake_pos[1] += cell_size

        # Update the snake's body and check for game over conditions
        snake_body.insert(0, list(snake_pos))
        if len(snake_body) > score + 1:
            snake_body.pop()

        # Check if the snake eats the food
        if snake_pos == food_pos:
            score += 1
            food_spawn = False

        if not food_spawn:
            # Generate new food position
            food_pos = [random.randrange(1, grid_width_cells) * cell_size, random.randrange(1, grid_height_cells) * cell_size]
            food_spawn = True

        # Drawing the game
        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

        # Game Over conditions adjusted for the snake's size
        if snake_pos[0] < 0 or snake_pos[0] >= width - cell_size or snake_pos[1] < 0 or snake_pos[1] >= height - cell_size:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()

        # Increment path_index to move to the next step in the path
        path_index = (path_index + 1) % len(hamiltonian_path)

        pygame.display.flip()
        fps_controller.tick(30)


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