from collections import defaultdict
from itertools import product


class Move:

    def __init__(self, name):
        self.name = name
        self.possibleMoves = list

    def checkLeft(self, gameBoard, x, y, color):
        for x in range(x, 0, -1):
            if gameBoard[x][y] != 0:
                continue
            if gameBoard[x][y] == 0 and gameBoard[x-1][y] != color:
                print("left" + str(x+1) + str(y+1))
                return x + 1, y + 1

    def checkRight(self, gameBoard,  x, y, color):
        previousMoveColor = 0
        for x in range(x, 8):
            if gameBoard[x][y] != 0:
                continue
            if gameBoard[x][y] == 0 and previousMoveColor != color:
                print("right" + str(x+1) + str(y+1))
                return x + 1, y + 1

    def checkUp(self, gameBoard, x, y, color):
        previousMoveColor = 0
        for y in range(y, 0, -1):
            if gameBoard[x][y] != 0:
                previousMoveColor = gameBoard[x][y]
            if gameBoard[x][y] == 0 and previousMoveColor != color:
                print("up" + str(x+1) + str(y+1) )
                return x+1, y+1


    def checkDown(self, gameBoard, x, y, color):
        previousMoveColor = 0
        for y in range(y, 8):
            if gameBoard[x][y] != 0:
                previousMoveColor = gameBoard[x][y]
            if gameBoard[x][y] == 0 and previousMoveColor != color:
                print("down" + str(x+1) + str(y+1))
                return x + 1, y + 1

    def moveList(self, gameBoard, color):
        gameDict = gameBoard.gameBoard
        interiorMoves = []
        for x in range(8):
            for y in range(8):
                if gameDict[x][y] != 0:
                    interiorMoves.append(self.checkLeft(gameDict, x, y, color))
                    interiorMoves.append(self.checkRight(gameDict, x, y, color))
                    interiorMoves.append(self.checkUp(gameDict, x, y, color))
                    interiorMoves.append(self.checkDown(gameDict, x, y, color))
        for x in range(8): print(interiorMoves[x])