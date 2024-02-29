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

# Then, in your run_hamiltonian_algorithm function, you should update the snake's position based on the output of calculate_next_move.
# Ensure to remove or adjust the snake's food interaction as it may not align with the Hamiltonian cycle logic.
















#old
def calculate_next_move(current_position, direction, grid_size):
    # This function calculates the next move based on the current position, current direction, and the grid size.
    # It returns the new direction and the next position of the snake.
    x, y = current_position
    grid_width, grid_height = grid_size

    if direction == 'DOWN' and y == grid_height - 2:
        next_direction = 'RIGHT'
    elif direction == 'UP' and y == 1:
        next_direction = 'RIGHT'
    elif direction == 'RIGHT' and x == grid_width - 1:
        next_direction = 'UP' if y > 0 else 'DOWN'
    else:
        next_direction = direction

    if next_direction == 'DOWN':
        next_position = (x, y + 1)
    elif next_direction == 'UP':
        next_position = (x, y - 1)
    elif next_direction == 'RIGHT':
        next_position = (x + 1, y)
    else:
        next_position = (x, y)  # Default case, should not happen

    return next_direction, next_position
