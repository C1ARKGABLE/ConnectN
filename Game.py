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

    def isEmpty(self):
        return self.contains == '.'



class Board:
    def __init__(self, size=4):
        self.board = [[Square() for _ in range(size)] for _ in range(size)]
        self.SIZE = size

    def printBoard(self):
        
        print(*[idx for idx in range(self.SIZE)], sep="\t")
        print()
        for row in self.board[::-1]:
            for item in row:
                print(item, end="\t")
            print()
    
    #Get the location of the top empty space
    def getTop(self, idx):
        for idx, row in enumerate(self.board):
            if row[idx].isEmpty():
                return idx

    def dropTile(self, idx, player='R'):
        #If column is full, return false
        if self.getTop(idx) == self.SIZE:
            return False
        else:
            self.board[self.getTop(idx)][idx].setVal(player)
            return True
            
        

         


        



