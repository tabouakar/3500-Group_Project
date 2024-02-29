def is_safe_move(x, y, grid, N):
    """Check if (x, y) is a valid move within the grid and not already part of the path."""
    return 0 <= x < N and 0 <= y < N and grid[x][y] == -1

def solve_hamiltonian_path_util(grid, x, y, move_x, move_y, pos, N):
    """Util function to find Hamiltonian path."""
    if pos == N**2:
        # All cells are covered
        return True
    
    for k in range(4):
        next_x = x + move_x[k]
        next_y = y + move_y[k]
        if is_safe_move(next_x, next_y, grid, N):
            grid[next_x][next_y] = pos
            if solve_hamiltonian_path_util(grid, next_x, next_y, move_x, move_y, pos+1, N):
                return True
            # Backtrack
            grid[next_x][next_y] = -1
    return False

def run_hamiltonian_algorithm():
    N = 10  # Size of the grid, adjust as needed
    grid = [[-1 for _ in range(N)] for _ in range(N)]

    # Possible movements for the snake
    move_x = [0, -1, 0, 1]
    move_y = [-1, 0, 1, 0]

    # Starting point
    grid[0][0] = 0

    if not solve_hamiltonian_path_util(grid, 0, 0, move_x, move_y, 1, N):
        print("Solution does not exist")
    else:
        # If a path is found, it can be displayed or used to move the snake
        print("A Hamiltonian path is found.")
        # Display or use the path
        for row in grid:
            print(row)

# You can test the function independently
# run_hamiltonian_algorithm()
