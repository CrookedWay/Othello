from itertools import product

import numpy as np

class Board:

    def __init__(self):
        # self.name = name
        self.gameBoard = np.zeros((8,8), dtype=np.int)
        self.gameBoard[3, 3] = 1
        self.gameBoard[3, 4] = 2
        self.gameBoard[4, 3] = 2
        self.gameBoard[4, 4] = 1


    def boardPrint(self, aesthetic):
        if aesthetic == True:
            nullDict = {0:'-', 1:"W", 2:'B'}
            for x in range(8):
                if x == 0:
                    print('\ta\tb\tc\td\te\tf\tg\th')
                    print(str(x+1), end="")
                else:
                    print("\r")
                    print(str(x+1), end="")
                for y in range(8):
                    print("\t"+str(nullDict[self.gameBoard[x][y]])+" ", end="")
            print("\n")
        if aesthetic == False:
            for x in range(8):
                if x == 0:
                    print('\t0\t1\t2\t3\t4\t5\t6\t7')
                    print(str(x), end="")
                else:
                    print("\r")
                    print(str(x), end="")
                for y in range(8):
                    print("\t" + str(self.gameBoard[x][y]) + " ", end="")
            print("\n")


    def takeMove(self, x, y, number):
        alphaNumeric = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        x = alphaNumeric[x]
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
        whiteCounter = 0
        for x, y in product(range(8), range(8)):
            if self.gameBoard[x][y] == 1:
                whiteCounter+=1
            if self.gameBoard[x][y] == 2:
                blackCounter+=1
        return blackCounter

