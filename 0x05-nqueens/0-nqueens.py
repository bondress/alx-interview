#!/usr/bin/python3
"""This pyton program solves the Nqueens problem.
"""


import sys


def print_board(board):
    """Prints the chessboard
    Args:
        board - list of list with length sys.argv[1]
    """
    new_list = []
    for n, row in enumerate(board):
        value = []
        for o, colmn in enumerate(row):
            if colmn == 1:
                value.append(n)
                value.append(o)
        new_list.append(value)

    print(new_list)


def isSafe(board, row, col, number):
    """Checks if moves are safe
    Args:
        board - list of list with length sys.argv[1]
        row - row to check if is safe doing a movement in this position
        col - col to check if is safe doing a movement in this position
        number: size of the board
    Return: True of False
    """

    for n in range(col):
        if board[row][n] == 1:
            return False

    for n, o in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[n][o] == 1:
            return False

    for n, o in zip(range(row, number, 1), range(col, -1, -1)):
        if board[n][o] == 1:
            return False

    return True


def solveNQUtil(board, col, number):
    """Find the possibilities
    Args:
        board - Board to resolve
        col - Number of col
        number - size of the board
    Returns:
        All the possibilities to solve the problem
    """

    if (col == number):
        print_board(board)
        return True
    res = False
    for i in range(number):

        if (isSafe(board, n, colmn, number)):

            board[n][colmn] = 1

            res = solveNQUtil(board, colmn + 1, number) or res

            board[n][colmn] = 0

    return res


def solve(number):
    """ Find all possibilities if exists
    Args:
        number - size of the board
    """
    board = [[0 for i in range(number)]for i in range(number)]

    if not solveNQUtil(board, 0, number):
        return False

    return True


def validate(args):
    """Validate the input data to verify if the answer size is possible
    Args:
        args - sys.argv
    """
    if (len(args) == 2):
        try:
            number = int(args[1])
        except Exception:
            print("N must be a number")
            exit(1)
        if number < 4:
            print("N must be at least 4")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Main method to execute the application
    """

    number = validate(sys.argv)
    solve(number)
