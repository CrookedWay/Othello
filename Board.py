from collections import defaultdict
from itertools import product


class Board:
    boardDict = {0: '-', 1: "W", 2: 'B'}

    def __init__(self):
        # self.name = name
        self.gameBoard = defaultdict(defaultdict)

    def __getitem__(self, row, column):
        return self.gameBoard[row][column]

    def __setitem__(self, row, column, value):
        self.gameBoard[row][column] = value

    def initalizeBoard(self):
        for x, y in product(range(8), range(8)):
            self.gameBoard[x][y] = 0
        self.gameBoard[3][3] = 1
        self.gameBoard[3][4] = 2
        self.gameBoard[4][3] = 2
        self.gameBoard[4][4] = 1

    def prettyPrintBoard(self):
        print('   a  b  c  d  e  f  g  h')
        nullDict = {0:'-', 1:"W", 2:'B'}
        for x in range(8):
            nullStr = ''
            for y in range(8):
                gamePiece = self.gameBoard[x][y]
                nullStr += (" "+ str((nullDict[gamePiece]))+" ")
                if y == 7:
                    print(str(x+1) + " " + nullStr)

    def uglyPrintBoard(self):
        print('   0  1  2  3  4  5  6  7')
        for x in range(8):
            nullStr = ''
            for y in range(8):
                gamePiece = self.gameBoard[x][y]
                nullStr += (" "+ str(gamePiece)+" ")
                if y == 7:
                    print(str(x) + " " + nullStr)

    def takeMove(self, x, y, number):
        alphaNumeric = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        x = alphaNumeric[x]-1
        y = int(y)-1
        self.gameBoard[y][x] = number

    def playMove(self, x_actual, y_actual, number):
        x = int(x_actual)
        y = int(y_actual)
        self.gameBoard[y][x] = number

    def broadcastMove(self, x, y, color):
        revAlphaNumeric = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
        print(str(color).upper() + " " + (revAlphaNumeric[x])+ " " +str(y))


    def countBlack(self):
        blackCounter = 0
        for x, y in product(range(8), range(8)):
            if self.gameBoard[x][y] == 2:
                blackCounter+=1
        return blackCounter














