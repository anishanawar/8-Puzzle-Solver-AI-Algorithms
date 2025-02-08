import copy
import time
import heapq

# define the goal state for the 8-puzzle
GOAL_STATE = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]

# node class to store the state, depth, heuristic cost, and children nodes
class Node:
    def __init__(self, puzzle, depth=0, hcost=0):
        self.puzzle = puzzle  # current state of the puzzle
        self.depth = depth    # depth of the node (g(n))
        self.hcost = hcost    # heuristic cost (h(n))
        self.parent = None    # parent node
        self.children = []    # children nodes generated from this node

    def __lt__(self, other):
        """Override less than to compare nodes by f(n) = g(n) + h(n)"""
        return (self.depth + self.hcost) < (other.depth + other.hcost)

# general search function that implements the search algorithm
def general_search(problem, queueing_function):
    # initialize the search process
    nodes = []
    heapq.heappush(nodes, Node(problem['initial_state'], 0, problem['heuristic'](problem['initial_state'])))

    visited = set()  # set to track visited states
    expanded_nodes_count = 0  # counter for nodes expanded
    max_queue_size = 0  # variable to track the maximum queue size

    while nodes:
        node = heapq.heappop(nodes)
        expanded_nodes_count += 1

        # track the max queue size
        max_queue_size = max(max_queue_size, len(nodes))

        # if the node's state is the goal state, return the solution
        if goal_test(node.puzzle):
            return solution(node, expanded_nodes_count, max_queue_size)

        # add the node's state to visited set
        visited.add(tuple(map(tuple, node.puzzle)))

        # children nodes and add them to the queue
        for child in expand(node):
            if tuple(map(tuple, child.puzzle)) not in visited:
                child.parent = node
                heapq.heappush(nodes, child)

    return "Failure"  # Return failure if no solution found

# goal test function to check if the current puzzle state matches the goal state
def goal_test(puzzle):
    return puzzle == GOAL_STATE

# expands the current node by generating all possible moves
def expand(node):
    r, c = find_blank(node.puzzle)
    children = []

    # define the four possible moves (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc

        if 0 <= new_r < 3 and 0 <= new_c < 3:  # check within bounds
            # copy of the puzzle and swap the blank space
            new_puzzle = copy.deepcopy(node.puzzle)
            new_puzzle[r][c], new_puzzle[new_r][new_c] = new_puzzle[new_r][new_c], new_puzzle[r][c]

            # a new node for the child state
            child = Node(new_puzzle, node.depth + 1)
            children.append(child)

    return children

# find the position of the blank space (represented by '0')
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                return i, j
    return -1, -1

# misplaced tile heuristic
def misplaced(puzzle):
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != GOAL_STATE[i][j] and puzzle[i][j] != '0':
                count += 1
    return count

# manhattan distance
def manhattan(puzzle):
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != '0':
                goal_r, goal_c = divmod(int(puzzle[i][j]) - 1, 3)
                count += abs(i - goal_r) + abs(j - goal_c)
    return count

# the solution path from the goal node to the start node
def solution(node, expanded_nodes_count, max_queue_size):
    path = []
    while node:
        path.insert(0, node.puzzle)  # insert at the beginning of the path
        node = node.parent

    return {
        'solution_path': path,
        'expanded_nodes_count': expanded_nodes_count,
        'depth_of_goal': len(path) - 1,
        'max_queue_size': max_queue_size
    }

# main function to execute the program
def main():
    print('Welcome to my 8-Puzzle Solver.')
    print('Select your option:')
    print('1. Use the default puzzle')
    print('2. Create your own puzzle')
    inputnum = int(input('Enter your choice (1 or 2): '))

    # Setting up puzzle if user uses a custom puzzle
    if inputnum == 1:
        puzzle = [['1', '2', '3'], ['4', '0', '6'], ['7', '5', '8']]
    elif inputnum == 2:
        print('Enter your puzzle, use a zero to represent the blank \n')

        # Getting the first row
        row1 = input('Enter the first row, use spaces between numbers: ')

        # Getting the second row
        row2 = input('Enter the second row, use spaces between numbers: ')

        # Getting the third row
        row3 = input('Enter the third row, use spaces between numbers: ')

        print('\n')

        # Combining input into a puzzle
        row1 = row1.split(' ')
        row2 = row2.split(' ')
        row3 = row3.split(' ')

        puzzle = [row1, row2, row3]

    print('Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic.')
    algo_choice = int(input('Enter your choice: '))

    # problem definition
    problem = {
        'initial_state': puzzle,
        'goal_state': GOAL_STATE,
    }

    # select heuristic based on user input
    if algo_choice == 1:
        problem['heuristic'] = lambda puzzle: 0  # uniform Cost Search has h(n) = 0
    elif algo_choice == 2:
        problem['heuristic'] = misplaced  # misplaced tile heuristic
    elif algo_choice == 3:
        problem['heuristic'] = manhattan  # manhattan Distance heuristic
    else:
        print('Invalid choice')
        return

    # run the general search with the selected queueing function
    print("Running the algorithm...")
    result = general_search(problem, queueing_function=None)

    if result == "Failure":
        print("No solution found.")
    else:
        print("\nSolution found!")
        print(f"Number of nodes expanded: {result['expanded_nodes_count']}")
        print(f"Depth of goal node: {result['depth_of_goal']}")
        print(f"Maximum queue size: {result['max_queue_size']}")
        print("Solution path:")
        for state in result['solution_path']:
            for row in state:
                print(' '.join(row))
            print()

if __name__ == "__main__":
    main()