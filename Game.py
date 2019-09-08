#!/usr/bin/env python3


import numpy as np


class Game:

    def __init__(self, numPlayers=2, goal=4, N=8, M=2):

        self.players = [Player(i) for i in list(range(numPlayers))]
        self.board = Board(goal=goal, N=N, M=M)


class Player:

    def __init__(self, playerNum):
        playerDict = {0: "X", 1: "O", 2: "$", 3: "&"}

        self.playerNum = playerNum
        self.playerIcon = playerDict[
            playerNum] if playerNum in playerDict.keys() else playerNum


class Board:

    def __init__(self, goal=4, N=8, M=2):

        # M-Dimensional cube shape
        self.shape = (N,) * M

        # Initialize M-Dimensional matrix, column-major order
        self.MainBoard = np.zeros(self.shape, dtype=np.int8, order="F")

    def drop(loc, player):
        raise NotImplemented("Still working on this. <3")


def setup(CLI=True):

    if not CLI:
        return Game(numPlayers=2, goal=4, N=10, M=10)

    while True:
        try:
            players = int(input("How many players?\n"))
        except ValueError:
            print("Invalid input")
            continue
        if players <= 1:
            print("Invalid input")
            continue
        break

    while True:
        try:
            n = int(input("Input the size?\n"))
        except ValueError:
            print("Invalid input")
            continue
        if n <= 1:
            print("Invalid input")
            continue
        break

    while True:
        try:
            m = int(input("Input the number of dimensions?\n"))
        except ValueError:
            print("Invalid input")
            continue
        if m <= 1 or m > 32:
            print("Value must be between 1 and 33")
            continue
        break

    while True:
        try:
            goal = int(input("How many in a row to win?\n"))
        except ValueError:
            print("Invalid input")
            continue
        if goal <= 1 or goal > n:
            print("Value must be between 1 and N ({0})".format(n))
            continue
        break

    game = Game(numPlayers=players, goal=goal, N=n, M=m)

    return game

if __name__ == "__main__":

    game = setup()

    print(game.board.MainBoard)

    # class Square:
    #     def __init__(self):

    #         #Set text value (default ".", otherwise
    #         # contains the players ID
    #         self.contains = "."

    #         self.up = None
    #         self.right = None
    #         self.lDiag = None
    #         self.rDiag = None

    #     def __repr__(self):
    #         return self.contains

    #     def setVal(self, c):
    #         self.contains = c

    #     def isEmpty(self):
    #         return self.contains == "."

    # class Board:
    #     def __init__(self, size=4):
    #         self.board = [[Square() for _ in range(size)] for _ in range(size)]
    #         self.SIZE = size

    #     def printBoard(self):

    #         print(*[idx for idx in range(self.SIZE)], sep="\t")
    #         print()
    #         for row in self.board[::-1]:
    #             for item in row:
    #                 print(item, end="\t")
    #             print()

    #     #Get the location of the top empty space
    #     def getTop(self, idx):
    #         for idx, row in enumerate(self.board):
    #             if row[idx].isEmpty():
    #                 return idx

    #     def dropTile(self, idx, player="R"):
    #         #If column is full, return false
    #         if self.getTop(idx) == self.SIZE:
    #             return False
    #         else:
    #             self.board[self.getTop(idx)][idx].setVal(player)
    #             return True
