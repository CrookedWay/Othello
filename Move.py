from itertools import product

import numpy as np


class Move:
    trace = True

    def __init__(self, color, enemyColor):
        self.possibleMoves = []
        self.color = color
        self.enemyColor = enemyColor

    def moveList(self, gameBoard):
        exit = False
        zeroIndex = 0
        for (initial_y, initial_x), element in np.ndenumerate(gameBoard.gameBoard):
            if element == self.color:
                x = initial_x
                y = initial_y
                for directional_y, directional_x in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0],
                                                     [-1, 1]]:
                    while exit != True:
                        x += directional_x
                        y += directional_y
                        if self.isValid(y, x) == False:
                            x = initial_x
                            y = initial_y
                            break
                        if gameBoard.gameBoard[y][x] == self.enemyColor:
                            continue
                        if gameBoard.gameBoard[y][x] == 0 and gameBoard.gameBoard[y - directional_y][
                                    x - directional_x] == 0:
                            x = initial_x
                            y = initial_y
                            break
                        if gameBoard.gameBoard[y][x] == 0 and gameBoard.gameBoard[y - directional_y][
                                    x - directional_x] == self.enemyColor:
                            self.possibleMoves.append([x, y, directional_x, directional_y])
        return self.possibleMoves

    def hook(self, gameBoard):
        for moves in self.moveList():
            isIsland = True
            x, y = moves[0], moves[1]
            for directional_y, directional_x in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0],
                                                 [-1, 1]]:
                if gameBoard.gameBoard[y - directional_y][x - directional_x] != 0:
                    isIsland = False
                    del self.moveList[moves]
                    break

    def printMoves(self):
        for x in self.possibleMoves:
            print(x)

    def inverse(myNum):
        if myNum == 1:
            return 2
        if myNum == 2:
            return 1

    def emptyMoves(self):
        del self.possibleMoves[:]

    def isValid(self, x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return False
