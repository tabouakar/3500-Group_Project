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
