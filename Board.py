from collections import defaultdict
from itertools import product


class Board:
    boardDict = {0: '-', 1: "W", 2: 'B'}

    def __init__(self, name):
        self.name = name
        self.gameBoard = defaultdict(defaultdict)

    def initalizeBoard(self):
        for x, y in product(range(8), range(8)):
            self.gameBoard[x][y] = 0
        self.gameBoard[3][3] = 2
        self.gameBoard[3][4] = 1
        self.gameBoard[4][3] = 1
        self.gameBoard[4][4] = 2

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
        print('   1  2  3  4  5  6  7  8')
        for x in range(8):
            nullStr = ''
            for y in range(8):
                gamePiece = self.gameBoard[x][y]
                nullStr += (" "+ str(gamePiece)+" ")
                if y == 7:
                    print(str(x+1) + " " + nullStr)

    def takeMove(self, x, y, color):
        x = x-1
        y = y-1
        if color == 'w':
            self.gameBoard[x][y] = 1
        else:
            self.gameBoard[x][y] = 2

    def countBlack(self):
        blackCounter = 0
        for x, y in product(range(8), range(8)):
            if self.gameBoard[x][y] == 2:
                blackCounter+=1
        return blackCounter

    def updateBoardSelf(self, moveList, color):
        boardDict = {'w': 1, 'b': 2}
        colorActual = boardDict[color]













