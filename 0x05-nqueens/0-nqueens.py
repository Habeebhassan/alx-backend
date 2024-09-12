#!/usr/bin/env python3
"""N Queens Puzzle Solver.

This program solves the N Queens puzzle by 
placing N non-attacking queens
on an N×N chessboard. It takes an integer N as 
input and prints all possible
solutions to the puzzle.

Usage:
    ./nqueens N
"""

import sys


def print_usage_and_exit(message):
    """Prints an error message and exits the program.

    Args:
        message (str): The message to be printed before exiting.
    """
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    """Checks if a queen can be placed on board 
    at (row, col) without conflicts.

    Args:
        board (list): The current state of the board, 
        where board[i] = column
                      index of the queen placed in the ith row.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it's safe to place the queen, 
        False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """Recursive function to solve the N Queens problem.

    Args:
        N (int): The size of the chessboard.
        row (int): The current row being checked.
        board (list): The current state of the board.
        solutions (list): A list to store all possible solutions.
    """
    if row == N:
        # Found a solution; add it to the list
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(N, row + 1, board, solutions)
                # No need to explicitly backtrack as we overwrite board[row]


def nqueens(N):
    """Main function to solve the N Queens problem.

    Args:
        N (int): The size of the chessboard.
    """
    solutions = []
    board = [-1] * N  # Initialize the board where board[row] = col
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)


def main():
    """Main entry point of the program."""
    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    # Ensure N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    # Ensure N is at least 4
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    nqueens(N)


if __name__ == "__main__":
    main()
