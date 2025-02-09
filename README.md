# 8-Puzzle Solver

## Overview
This project is an interactive command-line 8-puzzle solver that allows users to either use a default puzzle or create their own. The program implements the A* search algorithm with different heuristic options to find the optimal solution.

## Features
- Allows users to input a custom puzzle or use a default one.
- Implements three search algorithms:
  - **Uniform Cost Search (UCS)**
  - **Misplaced Tile Heuristic**
  - **Manhattan Distance Heuristic**
- Tracks performance metrics such as:
  - Number of nodes expanded
  - Solution depth (number of moves to reach the goal)
  - Maximum queue size during execution
- Displays the solution path from the initial state to the goal state.

## Getting Started
### Prerequisites
Ensure you have Python installed on your system. This program requires **Python 3.x**.

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/8-puzzle-solver.git
   cd 8-puzzle-solver
   ```
2. Run the program:
   ```sh
   main.py
   ```

## Usage
When you run the program, you will be prompted to choose between using a default puzzle or entering your own:
```
Welcome to my 8-Puzzle Solver.
Select your option:
1. Use the default puzzle
2. Create your own puzzle
Enter your choice (1 or 2):
```
If you select **2**, you will enter your puzzle manually by providing three rows with numbers separated by spaces. Use `0` to represent the blank tile.
```
Enter the first row: 1 2 3
Enter the second row: 4 0 6
Enter the third row: 7 5 8
```
Next, select the search algorithm:
```
Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.
Enter your choice:
```
The program will then find the solution and output the solution path along with statistics:
```
Solution found!
Number of nodes expanded: 56272
Depth of goal node: 20
Maximum queue size: 29289
Solution path:
1 2 3
4 5 6
7 8 0
```

## Algorithm Details
The solver uses the **A* search algorithm** with different heuristic functions:
- **Uniform Cost Search (UCS)**: Uses a heuristic function `h(n) = 0`, effectively treating all moves equally.
- **Misplaced Tile Heuristic**: Counts the number of misplaced tiles compared to the goal state.
- **Manhattan Distance Heuristic**: Computes the sum of the vertical and horizontal distances each tile is from its correct position.

## Code Structure
- **`Node` Class**: Represents a state in the search tree.
- **`general_search` Function**: Implements the A* algorithm using a priority queue.
- **`expand` Function**: Generates all valid child states.
- **`misplaced` and `manhattan` Functions**: Compute heuristic costs.
- **`solution` Function**: Reconstructs the solution path from the goal node.
- **`main` Function**: Handles user input and executes the chosen search algorithm.

## Example Output
```
Welcome to my 8-Puzzle Solver.
Select your option:
1. Use the default puzzle
2. Create your own puzzle
Enter your choice (1 or 2): 2

Enter your puzzle, use a zero to represent the blank

Enter the first row: 7 1 2
Enter the second row: 4 8 5
Enter the third row: 6 3 0

Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) the Manhattan Distance Heuristic.
3

Running the algorithm...

Solution found!
Number of nodes expanded: 56272
Depth of goal node: 20
Maximum queue size: 29289
Solution path:
1 2 3
4 5 6
7 8 0


