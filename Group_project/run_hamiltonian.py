#needs work, kinda broken


    #Main Function to run Hamiltonian Algorithm (automated mode)
def run_hamiltonian_algorithm():
    global direction, change_to, snake_pos, snake_body, food_pos, food_spawn, score


#if each cell of your grid is 10 pixels by 10 pixels, and your screen size is 600x400, then:
    cell_size = 10  # size of each grid cell in pixels
    grid_width = width // cell_size  # Number of cells horizontally
    grid_height = height // cell_size  # Number of cells vertically
    grid_size = (grid_width, grid_height)  # Define your grid size

    while True:
        # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        direction, next_pos = calculate_next_move(snake_pos, direction, grid_size)

        # Update snake position and body
        if direction == 'UP':
            snake_pos[1] -= cell_size
        elif direction == 'DOWN':
            snake_pos[1] += cell_size
        elif direction == 'LEFT':
            snake_pos[0] -= cell_size
        elif direction == 'RIGHT':
            snake_pos[0] += cell_size

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

        # Drawing the game
        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

        # Game Over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-cell_size or snake_pos[1] < 0 or snake_pos[1] > height-cell_size:
            gameOver()
        for block in snake_body[1:]:
            if snake_pos == block:
                gameOver()

        pygame.display.flip()
        fps_controller.tick(speed)
