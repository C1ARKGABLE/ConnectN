#!/usr/bin/env python3


import numpy as np


class Game:

    def __init__(self, numPlayers=2, goal=4, N=8, M=2):

        self.players = [Player(i) for i in list(range(numPlayers))]
        self.board = Board(goal=goal, N=N, M=M)
        self.won = False

    def checkWon(self, player):
        print("checking")

    def pickLocation(self, player):
        locations = []
        for i, N in enumerate(self.board.topShape):
            while True:
                try:
                    location = int(input("On axis {0}, where? ".format(i)))
                except (ValueError, TypeError):
                    print("Must be an integer")
                    continue
                if location >=N  or location < 0:
                    print("Must be between 0 and {0}".format(N))
                    continue
                locations.append(location)
                break

        self.board.drop(locations, player)

    def run(self):
        while not self.won:
            for player in self.players:
                self.pickLocation(player)
                self.board.draw()
                self.checkWon(player)


class Player:

    def __init__(self, playerNum):
        playerDict = {0: -1, 1: 1}

        self.playerNum = playerNum
        self.playerIcon = playerDict[
            playerNum] if playerNum in playerDict.keys() else playerNum


class Board:

    def __init__(self, goal=4, N=8, M=2):

        # M-Dimensional cube shape
        self.mainShape = (N,) * M

        self.topShape = (N,) * (M - 1)

        # Initialize M-Dimensional matrix
        self.mainBoard = np.zeros(
            self.mainShape, dtype=np.int8)
        # Initialize M-1 Dimensional matrix for keeping track of placed pieces
        self.topBoard = np.full(self.topShape, N - 1, dtype=int)

        #This makes my printBoard statement work better
        self.SIZE = N

    def drop(self, loc, player):
        check = int(self.topBoard[loc])
        print(check)
        if check != 0:
            loc.insert(0, check)
            print("Location -->{}<--".format(loc))
            np.put(self.mainBoard, loc, player.playerIcon)
            check -= 1
            print("Dropping!")
        else:
            print("Try again")
            raise OverflowError(
                "Haha, not memory overflow, just no free space here.")

        # raise NotImplemented("Still working on this. <3")

    def draw(self):
        '''
        Draws a pretty version of the board. Note that the board is flipped
        when printed to account for the fact that gravity is in fact a thing.
        '''
        #Indent by 1 tab length
        print("\t", end="")

        #Print the column numbers as a header
        print(*[x for x in range(self.SIZE)], sep="\t", end="\n")

        #Indent by 1 tab length
        print("\t", end="")

        #Print a row of dashes for separation
        print("-" * (self.SIZE * 7+2))

        for rowidx, row in enumerate(np.flipud(self.mainBoard)):
            print("{}|\t".format(rowidx), end="")
            for tile in row:
                print(tile, end="\t")
            print("\n |")
        # raise NotImplemented("Still working on this. <3")


def setup(CLI=True):

    if not CLI:
        return Game(numPlayers=2, goal=4, N=8, M=2)

    #Get number of players, must be 2 or more
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

    #Get size of board, must be 2 or more.
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

    #Get number of dimensions
    #Must be between 2 and 32
    while True:
        try:
            m = int(input("Input the number of dimensions?\n"))
        except ValueError:
            print("Invalid input")
            continue
        if m <= 1 or m > 32:
            #Double check me on this but I think that's right
            print("Value must be in the range 2<=x<=32")
            continue
        break


    while True:
        try:
            goal = int(input("How many in a row to win?\n"))
        except ValueError:
            print("Invalid input")
            continue
        #If number needed is greater than size of board, error. 
        #Number to goal must be 2 or more.
        if goal <= 1 or goal > n:
            print("Value must be between 1 and N ({0})".format(n))
            continue
        break

    game = Game(numPlayers=players, goal=goal, N=n, M=m)

    return game

if __name__ == "__main__":

    game = setup(CLI=False)

    game.board.draw()

    game.run()

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
