from itertools import product

import numpy as np


class Move:
    trace = True

    def __init__(self, color, enemyColor):
        self.possibleMoves = []
        self.color = color
        self.enemyColor = enemyColor


    def moveList(self, gameBoard):
        for (x, y), element in np.ndenumerate(gameBoard.gameBoard):
            if element == 0:
                # Check South
                for check_x in range(x, 8):
                    if gameBoard.gameBoard[y, check_x] == 0 and check_x != x:
                        break
                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
                        continue
                    if gameBoard.gameBoard[y, check_x] == self.color:
                        self.possibleMoves.append([y, x, "South"])
                        break
                # Check North
                for check_x in range(x, 0, -1):
                    if gameBoard.gameBoard[y, check_x] == 0 and check_x != x:
                        break
                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
                        continue
                    if gameBoard.gameBoard[y, check_x] == self.color:
                        self.possibleMoves.append([y, x, "North"])
                        break
                # Check East
                for check_y in range(y, 8):
                    if gameBoard.gameBoard[check_y, x] == 0 and check_y != y:
                        break
                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
                        continue
                    if gameBoard.gameBoard[y, check_x] == self.color:
                        self.possibleMoves.append([y, x, "East"])
                        break
                # Check West
                for check_y in range(y, 0, -1):
                    if gameBoard.gameBoard[check_y, x] == 0 and check_y != y:
                        break
                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
                        continue
                    if gameBoard.gameBoard[y, check_x] == self.color:
                        self.possibleMoves.append([check_y, x, "East"])
                # Check NE
                for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
                    if gameBoard.gameBoard[check_y, check_x] == 0 and check_y != y:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
                        continue
                    if gameBoard.gameBoard[check_y, check_x] == self.color:
                        self.possibleMoves.append([check_y, x, "East"])
                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y - 1, check_x + 1] == 0:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y - 1, check_x + 1] == self.enemyColor:
                        self.possibleMoves.append([check_y, check_x, "NE"])
                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
                        continue
                # Check NW
                for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x + 1] == 0:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x + 1] == self.enemyColor:
                        self.possibleMoves.append([check_y, check_x, "NW"])
                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
                        continue
                # Check SE
                for check_x, check_y in zip(range(x, 8), range(x, 0, -1)):
                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x - 1] == 0:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x - 1] == self.enemyColor:
                        self.possibleMoves.append([check_y, check_x, "SE"])
                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
                        continue
                # Check SE
                for check_x, check_y in zip(range(x, 8), range(x, 0, -1)):
                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x - 1] == 0:
                        break
                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
                                check_y + 1, check_x - 1] == self.enemyColor:
                        self.possibleMoves.append([check_y, check_x, "SE"])
                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
                        continue
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


 # for check_x in range(x, 8):
 #                    if gameBoard.gameBoard[y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[y, check_x] == 0 and gameBoard.gameBoard[y, check_x - 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[y, check_x] == 0 and gameBoard.gameBoard[y, check_x - 1] == self.enemyColor:
 #                        self.possibleMoves.append([y, check_x, "South"])
 #                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
 #                        continue
 #                # Check North
 #                for check_x in range(x, 0, -1):
 #                    if gameBoard.gameBoard[y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[y, check_x] == 0 and gameBoard.gameBoard[y, check_x + 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[y, check_x] == 0 and gameBoard.gameBoard[y, check_x + 1] == self.enemyColor:
 #                        self.possibleMoves.append([y, check_x, "North"])
 #                    if gameBoard.gameBoard[y, check_x] == self.enemyColor:
 #                        continue
 #                # Check East
 #                for check_y in range(y, 8):
 #                    if gameBoard.gameBoard[check_y, x] == self.color and check_y != y:
 #                        break
 #                    if gameBoard.gameBoard[check_y, x] == 0 and gameBoard.gameBoard[check_y - 1, x] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, x] == 0 and gameBoard.gameBoard[check_y - 1, x] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, x, "East"])
 #                    if gameBoard.gameBoard[check_y, x] == self.enemyColor:
 #                        continue
 #                # Check West
 #                for check_y in range(y, 0, -1):
 #                    if gameBoard.gameBoard[check_y, x] == self.color and check_y != y:
 #                        break
 #                    if gameBoard.gameBoard[check_y, x] == 0 and gameBoard.gameBoard[check_y + 1, x] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, x] == 0 and gameBoard.gameBoard[check_y + 1, x] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, x, "West"])
 #                    if gameBoard.gameBoard[check_y, x] == self.enemyColor:
 #                        continue
 #                # Check NE
 #                for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
 #                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y - 1, check_x + 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y - 1, check_x + 1] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, check_x, "NE"])
 #                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
 #                        continue
 #                # Check NW
 #                for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
 #                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x + 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x + 1] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, check_x, "NW"])
 #                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
 #                        continue
 #                # Check SE
 #                for check_x, check_y in zip(range(x, 8), range(x, 0, -1)):
 #                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x - 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x - 1] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, check_x, "SE"])
 #                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
 #                        continue
 #                # Check SE
 #                for check_x, check_y in zip(range(x, 8), range(x, 0, -1)):
 #                    if gameBoard.gameBoard[check_y, check_x] == self.color and check_x != x:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x - 1] == 0:
 #                        break
 #                    if gameBoard.gameBoard[check_y, check_x] == 0 and gameBoard.gameBoard[
 #                                check_y + 1, check_x - 1] == self.enemyColor:
 #                        self.possibleMoves.append([check_y, check_x, "SE"])
 #                    if gameBoard.gameBoard[check_y, check_x] == self.enemyColor:
 #                        continue
