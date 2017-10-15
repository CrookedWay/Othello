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
        for (initial_y, initial_x), element in np.ndenumerate(gameBoard.gameBoard):
            if element == self.color:
                x = initial_x
                y = initial_y
                for directional_y, directional_x in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0],
                                                     [-1, 1]]:
                    score = 0
                    while exit != True:
                        x += directional_x
                        y += directional_y
                        if self.isValid(y, x) == False:
                            x = initial_x
                            y = initial_y
                            break
                        if gameBoard.gameBoard[y][x] == self.enemyColor:
                            score+=1
                            continue
                        if gameBoard.gameBoard[y][x] == 0 and gameBoard.gameBoard[y - directional_y][
                                    x - directional_x] == 0:
                            x = initial_x
                            y = initial_y
                            break
                        if gameBoard.gameBoard[y][x] == 0 and gameBoard.gameBoard[y - directional_y][
                                    x - directional_x] == self.enemyColor and score > 0:
                            self.possibleMoves.append([x, y, directional_x, directional_y, score])

        for move in self.possibleMoves:
            x, y = move[0], move[1]
            if gameBoard.gameBoard[y][x] != 0:
                self.possibleMoves.remove(move)
        # for moves in self.possibleMoves:
        #     isIsland = True
        #     x, y = moves[0], moves[1]
        #     for directional_y, directional_x in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0],
        #                                          [-1, 1]]:
        #         if gameBoard.gameBoard[y - directional_y][x - directional_x] != 0:
        #             isIsland = False
        #             self.possibleMoves.remove(moves)
        #             break
        #     if isIsland == True:
        #         self.possibleMoves.remove(moves)
        # self.possibleMoves.sort(key=self.possibleMoves[5])
        return self.possibleMoves




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
