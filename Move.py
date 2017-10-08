class Move:
    def __init__(self, name, color, enemyColor):
        self.possibleMoves = []
        self.color = color
        self.enemyColor = enemyColor


    def checkWest(self, gameBoard, x, y):
        for check in range(x, 0, -1):
            if gameBoard[check][y] == 0 and gameBoard[check+1][y] == self.enemyColor:
                print('West')
                self.possibleMoves.append([check, y])
            if gameBoard[check][y] == self.enemyColor:
                continue
            if gameBoard[check][y] == 0:
                break


    def checkEast(self, gameBoard, x, y):
        for check in range(x, 7):
            if gameBoard[check][y] == 0 and gameBoard[check-1][y] == self.enemyColor:
                print('East')
                self.possibleMoves.append([check, y])
            if gameBoard[check][y] == self.enemyColor:
                continue
            if gameBoard[check][y] == 0:
                break

    def checkNorth(self, gameBoard, x, y):
        for check in range(y, 0, -1):
            if gameBoard[x][check] == 0 and gameBoard[x][check+1] == self.enemyColor:
                print('North')
                self.possibleMoves.append([x, check])
            if gameBoard[x][check] == self.enemyColor:
                continue
            if gameBoard[x][check] == 0:
                break

    def checkSouth(self, gameBoard, x, y):
        for check in range(y, 7):
            if gameBoard[x][check] == 0 and gameBoard[x][check-1] == self.enemyColor:
                print('South')
                self.possibleMoves.append([x, check])
            if gameBoard[x][check] == self.enemyColor:
                continue
            if gameBoard[x][check] == 0:
                break

    def checkNE(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x-1, 7), range(y-1, 0, -1)):
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x-1][check_y+1] == self.enemyColor:
                print('NE')
                self.possibleMoves.append([check_x, check_y])
            if gameBoard[check_x][check_y] == self.enemyColor:
                continue
            if gameBoard[check_x][check_y] == 0:
                break

    def checkSE(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x-1, 7), range(y-1, 7)):
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x-1][check_y-1] == self.enemyColor:
                print('SE')
                self.possibleMoves.append([check_x, check_y])
            if gameBoard[check_x][check_y] == self.enemyColor:
                continue
            if gameBoard[check_x][check_y] == 0:
                break

    def checkSW(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x-1, 0, -1), range(y-1, 7)):
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x+1][check_y-1] == self.enemyColor:
                print('SW')
                self.possibleMoves.append([check_x, check_y])
            if gameBoard[check_x][check_y] == self.enemyColor:
                continue
            if gameBoard[check_x][check_y] == 0:
                break

    def checkNW(self, gameBoard, x, y):
        for check_x, check_y in zip(range(x-1, 0, -1), range(y-1, 0, -1)):
            if gameBoard[check_x][check_y] == 0 and gameBoard[check_x+1][check_y+1] == self.enemyColor:
                print('NW')
                self.possibleMoves.append([check_x, check_y])
            if gameBoard[check_x][check_y] == self.enemyColor:
                continue
            if gameBoard[check_x][check_y] == 0:
                break

    def moveList(self, gameBoard):
        gameDict = gameBoard.gameBoard
        for x in range(8):
            for y in range(8):
                if gameDict[x][y] == self.color:
                    self.checkWest(gameDict, x, y)
                    self.checkEast(gameDict, x, y)
                    self.checkNorth(gameDict, x, y)
                    self.checkSouth(gameDict, x, y)
                    # self.checkNE(gameDict, x, y)
                    # self.checkSE(gameDict, x, y)
                    # self.checkSW(gameDict, x, y)
                    self.checkNW(gameDict, x, y)
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


# class Move:
#     def __init__(self, name, color, enemyColor):
#         self.possibleMoves = []
#         self.color = color
#         self.enemyColor = enemyColor
#
#     def checkWest(self, gameBoard, x, y):
#         for check in range(x, 0, -1):
#             if gameBoard[check][y] != 0:
#                 continue
#             if gameBoard[check][y] == 0 and gameBoard[check + 1][y] == self.enemyColor:
#                 self.possibleMoves.append([check, y])
#
#     def checkEast(self, gameBoard, x, y):
#         for check in range(x, 8):
#             if gameBoard[check][y] != 0:
#                 continue
#             if gameBoard[check][y] == 0 and gameBoard[check - 1][y] == self.enemyColor:
#                 self.possibleMoves.append([check, y])
#
#     def checkNorth(self, gameBoard, x, y):
#         for check in range(y, 0, -1):
#             if gameBoard[x][check] != 0:
#                 continue
#             if gameBoard[x][check] == 0 and gameBoard[x][check + 1] == self.enemyColor:
#                 self.possibleMoves.append([x, check])
#
#     def checkSouth(self, gameBoard, x, y):
#         for check in range(y, 8):
#             if gameBoard[x][check] != 0:
#                 continue
#             if gameBoard[x][check] == 0 and gameBoard[x][check - 1] == self.enemyColor:
#                 self.possibleMoves.append([x, check])
#
#     def checkNE(self, gameBoard, x, y):
#         for check_x, check_y in zip(range(x, 8), range(y, 0, -1)):
#             if gameBoard[check_x][check_y] != 0:
#                 continue
#             if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y + 1] == self.enemyColor:
#                 self.possibleMoves.append([check_x, check_y])
#
#     def checkSE(self, gameBoard, x, y):
#         for check_x, check_y in zip(range(x, 8), range(y, 8)):
#             if gameBoard[check_x][check_y] != 0:
#                 continue
#             if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y - 1] == self.enemyColor:
#                 self.possibleMoves.append([check_x, check_y])
#
#     def checkSW(self, gameBoard, x, y):
#         for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
#             if gameBoard[check_x][check_y] != 0:
#                 continue
#             if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y - 1] == self.enemyColor:
#                 self.possibleMoves.append([check_x, check_y])
#
#     def checkNW(self, gameBoard, x, y):
#         for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
#             if gameBoard[check_x][check_y] != 0:
#                 continue
#             if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y + 1] == self.enemyColor:
#                 self.possibleMoves.append([check_x, check_y])

    # def checkWest(self, gameBoard, x, y):
    #     for check in range(x, 0, -1):
    #         if gameBoard[y][check] != 0:
    #             continue
    #         if gameBoard[y][check] == 0 and gameBoard[y][check+1] == self.enemyColor:
    #             self.possibleMoves.append([y, check])
    #
    # def checkEast(self, gameBoard, x, y):
    #     for check in range(x, 8):
    #         if gameBoard[y][check-1] != 0:
    #             continue
    #         if gameBoard[y][check] == 0 and gameBoard[y][check-1] == self.enemyColor:
    #             self.possibleMoves.append([y, check])
    #
    # def checkNorth(self, gameBoard, x, y):
    #     for check in range(y, 0, -1):
    #         if gameBoard[check][x] != 0:
    #             continue
    #         if gameBoard[check][x] == 0 and gameBoard[check + 1][x] == self.enemyColor:
    #             self.possibleMoves.append([check, x])
    #
    # def checkSouth(self, gameBoard, x, y):
    #     for check in range(y, 8):
    #         if gameBoard[check][x] != 0:
    #             continue
    #         if gameBoard[check][x] == 0 and gameBoard[check-1][x] == self.enemyColor:
    #             self.possibleMoves.append([check, x])
    #
    # def checkNE(self, gameBoard, x, y):
    #     for check_y, check_x in zip(range(x, 8), range(y, 0, -1)):
    #         if gameBoard[check_y][check_x] != 0:
    #             continue
    #         if gameBoard[check_y][check_x] == 0 and gameBoard[check_y - 1][check_x + 1] == self.enemyColor:
    #             self.possibleMoves.append([check_y, check_x])
    #
    # def checkSE(self, gameBoard, x, y):
    #     for check_y, check_x in zip(range(x, 8), range(y, 8)):
    #         if gameBoard[check_y][check_x] != 0:
    #             continue
    #         if gameBoard[check_y][check_x] == 0 and gameBoard[check_y - 1][check_x - 1] == self.enemyColor:
    #             self.possibleMoves.append([check_y, check_x])
    #
    # def checkSW(self, gameBoard, x, y):
    #     for check_y, check_x in zip(range(x, 0, -1), range(y, 8)):
    #         if gameBoard[check_y][check_x] != 0:
    #             continue
    #         if gameBoard[check_y][check_x] == 0 and gameBoard[check_y + 1][check_x - 1] == self.enemyColor:
    #             self.possibleMoves.append([check_y, check_x])
    #
    # def checkNW(self, gameBoard, x, y):
    #     for check_y, check_x in zip(range(x, 0, -1), range(y, 0, -1)):
    #         if gameBoard[check_y][check_x] != 0:
    #             continue
    #         if gameBoard[check_y][check_x] == 0 and gameBoard[check_y + 1][check_x + 1] == self.enemyColor:
    #             self.possibleMoves.append([check_y, check_x])