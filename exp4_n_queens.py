"""
Experiment 4: Constraint Satisfaction Problem (N-Queens Problem)
Aim: Implement a solution for the N-Queens problem using Backtracking.
"""


def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


def is_safe(board, row, col, n):
    """Checks if placing a queen at board[row][col] is safe."""
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, n):
    """Solves the N-Queens CSP recursively using Backtracking."""
    if row == n:
        print_board(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # Backtrack
    return res


if __name__ == "__main__":
    N = 4
    board = [[0] * N for _ in range(N)]
    print(f"Solutions for {N}-Queens:\n")
    solve_n_queens(board, 0, N)
