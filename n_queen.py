def solve_n_queens(n):
    def solve_n_queens_util(row, ld, rd):
        if row == n:
            solutions.append(["".join(" Q " if i == col else " . " for i in range(n)) for col in board])
            return

        for col in range(n):
            if (col not in board) and (row + col not in ld) and (row - col not in rd):
                board.append(col)
                ld.add(row + col)
                rd.add(row - col)
                solve_n_queens_util(row + 1, ld, rd)
                board.pop()
                ld.remove(row + col)
                rd.remove(row - col)

    solutions = []
    board = []
    ld = set()
    rd = set()
    solve_n_queens_util(0, ld, rd)
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

# Example usage:
n = 4  # Change this to the desired board size
solutions = solve_n_queens(n)
print_solutions(solutions)
