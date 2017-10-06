def update(gameBoard, color, x_input, y):
    alphaNumeric = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    x = alphaNumeric[x_input]
    updateWest(gameBoard, color, x, y)
    updateEast(gameBoard, color, x, y)
    updateNorth(gameBoard, color, x, y)
    updateSouth(gameBoard, color, x, y)
    updateNE(gameBoard, color, x, y)
    updateSE(gameBoard, color, x, y)
    updateSW(gameBoard, color, x, y)
    updateNW(gameBoard, color, x, y)



def updateWest(self, gameBoard, x, y):
    for check in range(x, 0, -1):
        if gameBoard[check][y] != 0:
            continue
        if gameBoard[check][y] == 0 and gameBoard[check + 1][y] == self.enemyColor:
            self.possibleMoves.append([x, y, check + 1, y + 1, 'W'])


def updateEast(self, gameBoard, x, y):
    for check in range(x, 8):
        if gameBoard[check][y] != 0:
            continue
        if gameBoard[check][y] == 0 and gameBoard[check - 1][y] == self.enemyColor:
            self.possibleMoves.append([x, y, check + 1, y + 1, 'E'])


def updateNorth(self, gameBoard, x, y):
    for check in range(y, 0, -1):
        if gameBoard[x][check] != 0:
            continue
        if gameBoard[x][check] == 0 and gameBoard[x][check + 1] == self.enemyColor:
            self.possibleMoves.append([x, y, x + 1, check + 1, 'N'])


def updateSouth(self, gameBoard, x, y):
    for check in range(y, 8):
        if gameBoard[x][check] != 0:
            continue
        if gameBoard[x][check] == 0 and gameBoard[x][check - 1] == self.enemyColor:
            self.possibleMoves.append([x, y, x + 1, check + 1, 'S'])


def updateNE(self, gameBoard, x, y):
    for check_x, check_y in zip(range(x, 8), range(y, 0, -1)):
        if gameBoard[check_x][check_y] != 0:
            continue
        if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y + 1] == self.enemyColor:
            self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NE'])


def updateSE(self, gameBoard, x, y):
    for check_x, check_y in zip(range(x, 8), range(y, 8)):
        if gameBoard[check_x][check_y] != 0:
            continue
        if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y - 1] == self.enemyColor:
            self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SE'])


def updateSW(self, gameBoard, x, y):
    for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
        if gameBoard[check_x][check_y] != 0:
            continue
        if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y - 1] == self.enemyColor:
            self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SW'])


def updateNW(self, gameBoard, x, y):
    for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
        if gameBoard[check_x][check_y] != 0:
            continue
        if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y + 1] == self.enemyColor:
            self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NW'])