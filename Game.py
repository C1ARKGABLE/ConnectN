#!/usr/bin/env python3

class Square:
    def __init__(self):

        #Set text value (default '.', otherwise 
        # contains the players ID
        self.contains = '.'
        
        self.up = None
        self.right = None
        self.lDiag = None
        self.rDiag = None
    def __repr__(self):
        return self.contains
    def setVal(self, c):
        self.contains = c



class Board:
    def __init__(self, size=4):
        self.board = [[Square() for _ in range(size)] for _ in range(size)]
        self.SIZE = size

    def printBoard(self):
        print(*[idx+1 for idx in range(self.SIZE)], sep="\t")
        for col in self.board:
            for item in col:
                print(item, end="\t")
            print()




