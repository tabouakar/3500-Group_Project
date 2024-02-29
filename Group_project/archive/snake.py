import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))

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


    # Run Hamiltonian Algorithm function (automated mode)
def run_hamiltonian_algorithm():
                                                            # Placeholder for future implementation
    print("Hamiltonian Algorithm Placeholder")
    play_game()                                             # Call playgame as placeholder


# Main menu function
def main_menu():
    play_game_text = font.render('Play Game', True, black, green)
    play_game_rect = play_game_text.get_rect()
    play_game_rect.center = (width // 2, height // 3)

    run_algo_text = font.render('Run Hamiltonian Algorithm', True, black, red)
    run_algo_rect = run_algo_text.get_rect()
    run_algo_rect.center = (width // 2, 2 * height // 3)

    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_game_rect.collidepoint(event.pos):
                    menu_running = False
                    play_game()
                elif run_algo_rect.collidepoint(event.pos):
                    menu_running = False
                    run_hamiltonian_algorithm()

        screen.fill(white)
        screen.blit(play_game_text, play_game_rect)
        screen.blit(run_algo_text, run_algo_rect)
        pygame.display.flip()





# Start with the main menu
if __name__ == "__main__":
    main_menu()