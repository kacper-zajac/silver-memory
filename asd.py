import os
import sys

board = []

for x in range(0, 8):
    board.append(["O"] * 8)

board[7][0] = "x"
board[5][0] = "x"
board[6][1] = "x"
board[7][2] = "x"
board[5][2] = "x"
board[6][3] = "x"
board[7][4] = "x"
board[5][4] = "x"
board[6][5] = "x"
board[7][6] = "x"
board[5][6] = "x"
board[6][7] = "x"

# setting up team y
board[1][0] = "y"
board[0][1] = "y"
board[2][1] = "y"
board[1][2] = "y"
board[0][3] = "y"
board[2][3] = "y"
board[1][4] = "y"
board[0][5] = "y"
board[2][5] = "y"
board[1][6] = "y"
board[0][7] = "y"
board[2][7] = "y"


def print_board(board):
    for a in board:
        print(" | ".join(a))

print_board(board)