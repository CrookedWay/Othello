from collections import defaultdict
from itertools import product


class Move:
    def __init__(self, name, color, enemyColor):
        boardDict = {'w': 1, 'b': 2}
        self.possibleMoves = []
        self.color = boardDict[color]
        self.enemyColor = boardDict[enemyColor]

    def checkWest(self, gameBoard, x, y):
        for check in range(x, 0, -1):
            if gameBoard[check][y] != 0:
                continue
            if gameBoard[check][y] == 0 and gameBoard[check + 1][y] == self.enemyColor:
                self.possibleMoves.append([x, y, check + 1, y + 1, 'W'])

    def checkEast(self, gameBoard, x, y):
        for check in range(x, 8):
            if gameBoard[check][y] != 0:
                continue
            if gameBoard[check][y] == 0 and gameBoard[check - 1][y] == self.enemyColor:
                self.possibleMoves.append([x,y,check + 1, y + 1, 'E'])

    def checkNorth(self, gameBoard, x, y):
        for check in range(y, 0, -1):
            if gameBoard[x][check] != 0:
                continue
            if gameBoard[x][check] == 0 and gameBoard[x][check + 1] == self.enemyColor:
                self.possibleMoves.append([x, y, x + 1, check + 1, 'N'])

    def checkSouth(self, gameBoard, x, y):
        for check in range(y, 8):
            if gameBoard[x][check] != 0:
                continue
            if gameBoard[x][check] == 0 and gameBoard[x][check - 1] == self.enemyColor:
                self.possibleMoves.append([x, y, x + 1, check + 1, 'S'])

    def checkNE(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x, 8), range(y, 0, -1)):
            if gameBoard[check_x][check_y] != 0:
                continue
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y + 1] == self.enemyColor:
                self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NE'])

    def checkSE(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x, 8), range(y, 8)):
            if gameBoard[check_x][check_y] != 0:
                continue
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y - 1] == self.enemyColor:
                self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SE'])

    def checkSW(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
            if gameBoard[check_x][check_y] != 0:
                continue
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y - 1] == self.enemyColor:
                self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SW'])

    def checkNW(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
            if gameBoard[check_x][check_y] != 0:
                continue
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y + 1] == self.enemyColor:
                self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NW'])

    def moveList(self, gameBoard):
        gameDict = gameBoard.gameBoard
        for x in range(8):
            for y in range(8):
                if gameDict[x][y] == self.color:
                    self.checkWest(gameDict, x, y)
                    self.checkEast(gameDict, x, y)
                    self.checkNorth(gameDict, x, y)
                    self.checkSouth(gameDict, x, y)
                    self.checkNE(gameDict, x, y)
                    self.checkSE(gameDict, x, y)
                    self.checkSW(gameDict, x, y)
                    self.checkNW(gameDict, x, y)
        return self.possibleMoves


