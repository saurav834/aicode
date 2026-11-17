"""
Experiment 7: Game Playing Algorithm (Minimax / Tic-Tac-Toe)
Aim: Implement the Minimax algorithm for an optimal Tic-Tac-Toe AI agent.
"""

import math

board = [' ' for _ in range(9)]


def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    print()


def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(b[i] == player for i in cond) for cond in win_conditions)


def is_full(b):
    return ' ' not in b


def minimax(b, depth, is_maximizing):
    """Minimax recursive algorithm for optimal decision making."""
    if check_winner(b, 'O'):
        return 10 - depth
    if check_winner(b, 'X'):
        return depth - 10
    if is_full(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score


def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


if __name__ == "__main__":
    # Demonstration: AI ('O') responding to Human ('X') at position 0
    board[0] = 'X'
    ai_choice = best_move()
    board[ai_choice] = 'O'
    print(f"Human placed X at 0. AI optimal move for O is at index {ai_choice}:\n")
    print_board()
