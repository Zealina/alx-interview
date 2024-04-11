#!/usr/bin/env python3
"""Solve the nqueens problem"""
import sys
from typing import List


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

if not sys.argv[1].isdigit():
    print('N must be a number')
    sys.exit(1)

arg = int(sys.argv[1])

if arg < 4:
    print('N must be at least 4')
    sys.exit(1)


def is_safe(board: List[List[int]], row: int, col: int, n: int) -> bool:
    """Ensure a position is safe"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board: List[List[int]],
                   col: int, n: int, solutions: List) -> None:
    """Recursive call to backtrack"""
    if col >= n:
        solution = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[i][col] = 0


def to_index(solution: List[List[int]]) -> List[List[int]]:
    """Convert solution format"""
    s_index = []
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if solution[i][j] == 1:
                s_index.append([i, j])
    return s_index


def n_queens(n: int) -> None:
    """main function to call recursive"""
    board = [[0] * n for _ in range(n)]
    solutions: List = []
    solve_n_queens(board, 0, n, solutions)
    for i in solutions:
        print(to_index(i))


n_queens(arg)
