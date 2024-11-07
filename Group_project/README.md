
# Snake Game with Hamiltonian Cycle Solver

This project implements a classic Snake game with an additional mode that autonomously solves the game by following a Hamiltonian cycle. The game can be run in two modes: Manual Play or Automated Mode using a Hamiltonian cycle to cover the entire grid without crashing.

## Overview
- **Manual Play**: The player controls the snake using the keyboard and tries to avoid crashing while consuming fruit.
- **Automated Mode**: The program finds a Hamiltonian cycle for the grid size, passes the path to the movement logic, and allows the snake to follow this cycle to complete the game automatically.

## Requirements
- **Python 3.x**
- **Pygame library** for the game interface

To install Pygame, run:
```bash
pip install pygame
```

## Important Notes

### Grid Size Limitations
- Recommended grid size is a maximum of 8x6 due to computational intensity. Larger grids may cause significant CPU load.
- Supported grid configurations:
  - Even x Even (e.g., 6x6)
  - Even x Odd (e.g., 8x7)
- **Odd x Odd configurations are not supported** due to limitations in the Hamiltonian cycle computation. (doesnt exist)

### Adjustable Settings
- **Snake Speed**: Adjust on **Line 41** to change the snake's speed.
- **Grid Size**: Set the grid height and width on **Lines 44 and 45**.

- **Manual Play Speed**: Recommended speed setting of `10` on **Line 132** for easier manual control.

### Visualization
The Hamiltonian cycle search includes a visualization that can impact performance. To disable, comment out the `visualize_search` function call.

## Code Structure
- **Game Initialization and Settings**: Adjustable settings for grid size and speed.
- **Backtracking Algorithm**:
  - `get_adjacent_cells` (Line 269): Finds adjacent cells as part of the Hamiltonian path search.
  - `find_hamiltonian` (Line 276): Core logic for finding the Hamiltonian cycle.
- **Game Logic**: Includes snake and fruit logic, game-over conditions, and main gameplay loop.
- **Menu System**: Allows the user to select between Manual Play and Automated Mode.

## Usage

### Run the Game
```bash
python HamiltonianCycle_withfullSnakeGame.py
```

### Select Mode
- **Manual Play**: Control the snake using arrow keys to avoid the walls and collect fruit.
- **Automated Mode**: The snake follows a precomputed Hamiltonian cycle to complete the game autonomously.

### Additional Recommendations
For the best experience in Manual Play:
- Set `speed = 10` on **Line 132** to allow more time for manual input.
- Increase the grid size to provide more movement space.

---

Enjoy the game and feel free to tweak settings for a custom experience!
