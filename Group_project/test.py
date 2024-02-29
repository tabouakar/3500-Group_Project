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

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Font for text
font = pygame.font.Font(None, 36)

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
            food_pos = [random.randrange(1, (width//cell_size)) * cell_size, random.randrange(1, (height//cell_size)) * cell_size]
        food_spawn = True
    
        # Background
        screen.fill(black)
        
        # Draw snake
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        
        # Draw food
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
        
        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-cell_size:
            gameOver()
        if snake_pos[1] < 0 or snake_pos[1] > height-cell_size:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()
        
        # Display score
        score_text = font.render('Score: ' + str(score), True, white)
        screen.blit(score_text, [0, 0])
        
        # Refresh game screen
        pygame.display.flip()
        
        # Refresh rate
        fps_controller.tick(speed)

if __name__ == '__main__':
    play_game()
