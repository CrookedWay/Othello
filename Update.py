#TODO: Worried about hitting edges and updating with current logic



def takeUpdate(gameBoard, color, x_input, y):
    alphaNumeric = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    x = alphaNumeric[x_input]
    updateWest(gameBoard, color, x, y)
    # updateEast(gameBoard, color, x, y)
    # updateNorth(gameBoard, color, x, y)
    # updateSouth(gameBoard, color, x, y)
    # updateNE(gameBoard, color, x, y)
    # updateSE(gameBoard, color, x, y)
    # updateSW(gameBoard, color, x, y)
    # updateNW(gameBoard, color, x, y)

def selfUpdate(gameBoard, color, x, y):
    updateWest(gameBoard, color, x, y)
    # updateEast(gameBoard, color, x, y)
    # updateNorth(gameBoard, color, x, y)
    # updateSouth(gameBoard, color, x, y)
    # updateNE(gameBoard, color, x, y)
    # updateSE(gameBoard, color, x, y)
    # updateSW(gameBoard, color, x, y)
    # updateNW(gameBoard, color, x, y)


#
# def updateWest(gameBoard, color, actual_x, actual_y):
#     print("Color" + str(color))
#     x = int(actual_x)
#     y = int(actual_y)
#     for check in range(x, 0, -1):
#         print("Loop Variables: X: "+str(check)+" Y: "+str(y))
#         print("-")
#         print("Current Contents: "+str(gameBoard.gameBoard[check][y]) + " Previous Contents: "+ str(gameBoard.gameBoard[check+1][y]))
#         print("\n")
#         if gameBoard.gameBoard[check][y] == 0 and gameBoard.gameBoard[check+1][y] == color:
#             print("INSIDE")
#             for z in range(check+1, x):
#                 gameBoard.gameBoard[z][y] = color
#             break

def updateWest(gameBoard, myNum, actual_x, actual_y):
    x = int(actual_x)
    y = int(actual_y)
    for check in range(x, 0, -1):
        print("Loop Variables: X: " + str(check) + " Y: " + str(y))
        print("-")
        print("Current Contents: "+str(gameBoard.gameBoard[check][y]) + " Previous Contents: "+ str(gameBoard.gameBoard[check+1][y]))
        print("\n")
        if gameBoard.gameBoard[y][check] == myNum:
            for z in range(check, x):
                gameBoard.gameBoard[z][y] = myNum




def updateEast(gameBoard, color, actual_x, actual_y):
    x = int(actual_x) - 1
    y = int(actual_y) - 1
    for check in range(x, 8):
        if gameBoard.gameBoard[check][y] == 0 and gameBoard.gameBoard[check-1][y] == color:
            print("INSIDE")
            for z in range(x, check-1):
                gameBoard.gameBoard[z][y] = color


def updateNorth(gameBoard, color, actual_x, actual_y):
    x = int(actual_x) - 1
    y = int(actual_y) - 1
    for check in range(y, 0, -1):
        if gameBoard.gameBoard[x][y] == 0 and gameBoard.gameBoard[x][check+1] == color:
            print("INSIDE")
            for z in range(y, check+1, -1):
                gameBoard.gameBoard[x][z] = color


def updateSouth(gameBoard, color, actual_x, actual_y):
    x = int(actual_x) - 1
    y = int(actual_y) - 1
    for check in range(y, 8):
        if gameBoard.gameBoard[x][y] == 0 and gameBoard.gameBoard[x][check-1] == color:
            print("INSIDE")
            for z in range(y, check-1):
                gameBoard.gameBoard[x][z] = color


# def updateNE(self, gameBoard, color, x, y):
#     for check_x, check_y in zip(range(x, 8), range(y, 0, -1)):
#         if gameBoard[check_x][check_y] != 0:
#             continue
#         if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y + 1] == self.enemyColor:
#             self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NE'])
#
#
# def updateSE(self, gameBoard, color, x, y):
#     for check_x, check_y in zip(range(x, 8), range(y, 8)):
#         if gameBoard[check_x][check_y] != 0:
#             continue
#         if gameBoard[check_x][check_y] == 0 and gameBoard[check_x - 1][check_y - 1] == self.enemyColor:
#             self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SE'])
#
#
# def updateSW(self, gameBoard, color, x, y):
#     for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
#         if gameBoard[check_x][check_y] != 0:
#             continue
#         if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y - 1] == self.enemyColor:
#             self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'SW'])
#
#
# def updateNW(self, gameBoard, color, x, y):
#     for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
#         if gameBoard[check_x][check_y] != 0:
#             continue
#         if gameBoard[check_x][check_y] == 0 and gameBoard[check_x + 1][check_y + 1] == self.enemyColor:
#             self.possibleMoves.append([x, y, check_x + 1, check_y + 1, 'NW'])

# def updateWest(gameBoard, color, actual_x, actual_y):
#     print(color)
#     x = int(actual_x)
#     y = int(actual_y)
#     for check in range(0, x):
#         print("Loop Variables: X: " + str(check) + " Y: " + str(y))
#         print("-")
#         print("Current Contents: "+str(gameBoard.gameBoard[check][y]) + " Previous Contents: "+ str(gameBoard.gameBoard[check+1][y]))
#         print("\n")
#         if gameBoard.gameBoard[check][y] == 0:
#             break
#         if gameBoard.gameBoard[check][y] != color:
#             gameBoard.gameBoard[check][y] = color
