#!/usr/bin/env python3
import sys
import numpy as np

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

    def isEmpty(self):
        return self.contains == '.'



class Board:
    def __init__(self, size=8):
        self.SIZE = size
        self.board = np.zeros((self.SIZE, self.SIZE), dtype=int)

    #Flip board upside down for printing so we aren't like breaking gravity
    #Plz dont touch this it works perfectly
    def printBoard(self):

        #Indent by 1 tab length
        print("\t", end="")

        #Print the column numbers as a header
        print(*[x for x in range(self.SIZE)], sep="\t", end="\n")

        #Indent by 1 tab length
        print("\t", end="")

        #Print a row of dashes for separation
        print("-" * (self.SIZE * 7+2))

        for rowidx, row in enumerate(np.flipud(self.board)):
            print("{}|\t".format(rowidx), end="")
            for tile in row:
                print(tile, end="\t")
            print("\n |")

    #Get the location of the top empty space
    def getTop(self, idx):
        
        #Get column as a numpy array
        col = self.board.T[idx]
        r =  np.nonzero(col)[0]-1 if np.any(col) else 0
        print("getTop Value: -->{}<--".format(r))
        return r

    def dropTile(self, idx, player='1'):
        #If column is full, return false
        if np.all(self.board.T[idx]):
            return False

        else:
            self.board[self.getTop(idx)+1, idx] = player
            return True
            
        

         


        



