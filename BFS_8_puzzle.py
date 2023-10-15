from collections import deque

class PuzzleNode:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

def print_path(node):
    if node.parent is not None:
        print_path(node.parent)
        print(f"Move {node.action} ->\n")
        print_board(node.state)

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)).replace("0", " ") + "\n")
    print("\n")

def is_goal_state(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def get_neighbors(board):
    neighbors = []
    empty_row, empty_col = next((i, row.index(0)) for i, row in enumerate(board) if 0 in row)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dr, dc in moves:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_board = [row[:] for row in board]
            new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[empty_row][empty_col]
            neighbors.append(new_board)
    return neighbors

def bfs_8_puzzle(initial_state):
    start_node = PuzzleNode(initial_state, None, "Start")
    queue = deque([start_node])
    visited = set()

    while queue:
        node = queue.popleft()
        state = node.state
        visited.add(tuple(map(tuple, state)))

        if is_goal_state(state):
            print("Solution found!")
            print_path(node)
            return

        neighbors = get_neighbors(state)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in visited:
                new_node = PuzzleNode(neighbor, node, "Move")
                queue.append(new_node)

    print("No solution found.")

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
bfs_8_puzzle(initial_state)
