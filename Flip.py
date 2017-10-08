def inverse(myNum):
    if myNum == 1:
        return 2
    if myNum == 2:
        return 1

def takeFlip(gameBoard, color, x_input, y_input):
    alphaNumeric = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    x = alphaNumeric[x_input]
    y = int(y_input)-1
    flipWest(gameBoard, color, x, y)
    flipEast(gameBoard, color, x, y)
    flipNorth(gameBoard, color, x, y)
    flipSouth(gameBoard, color, x, y)
    flipNE(gameBoard, color, x, y)
    flipSE(gameBoard, color, x, y)
    flipSW(gameBoard, color, x, y)
    flipNW(gameBoard, color, x, y)

def selfFlip(gameBoard, color, x, y):
    flipWest(gameBoard, color, x, y)
    flipEast(gameBoard, color, x, y)
    flipNorth(gameBoard, color, x, y)
    flipSouth(gameBoard, color, x, y)
    flipNE(gameBoard, color, x, y)
    flipSE(gameBoard, color, x, y)
    flipSW(gameBoard, color, x, y)
    flipNW(gameBoard, color, x, y)

def flipWest(gameBoard, myNum, x, y):
    flipList = []
    anchor = False
    for check in range(x, 0, -1):
        if gameBoard.gameBoard[y][check] == 0 and check != x:
            break
        if gameBoard.gameBoard[y][check] != myNum:
            flipList.append([y, check])
            continue
        if gameBoard.gameBoard[y][check] == myNum and check != x:
            flipList.append([y, check])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipEast(gameBoard, myNum, x, y):
    flipList = []
    anchor = False
    for check in range(x, 8):
        if gameBoard.gameBoard[y][check] == 0 and check != x:
            break
        if gameBoard.gameBoard[y][check] != myNum:
            flipList.append([y, check])
            continue
        if gameBoard.gameBoard[y][check] == myNum and check != x:
            flipList.append([y, check])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum


def flipNorth(gameBoard, myNum, x, y):
    flipList = []
    anchor = False
    for check in range(y, 0, -1):
        if gameBoard.gameBoard[check][x] == 0 and check != y:
            break
        if gameBoard.gameBoard[check][x] != myNum:
            flipList.append([check, x])
            continue
        if gameBoard.gameBoard[check][x] == myNum and check != y:
            flipList.append([check, x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipSouth(gameBoard, myNum, x, y):
    flipList = []
    anchor = False
    for check in range(y, 8):
        if gameBoard.gameBoard[check][x] == 0 and check != y:
            break
        if gameBoard.gameBoard[check][x] != myNum:
            flipList.append([check, x])
            continue
        if gameBoard.gameBoard[check][x] == myNum and check !=y:
            flipList.append([check, x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipNE(gameBoard, myNum, x, y):
    flipList =[]
    anchor = False
    for check_x, check_y in zip(range(x, 8), range(y, 0, -1)):
        if gameBoard.gameBoard[check_y][check_x] == 0 and check_x != x:
            break
        if gameBoard.gameBoard[check_y][check_x] != myNum:
            flipList.append([check_y, check_x])
            continue
        if gameBoard.gameBoard[check_y][check_x] == myNum and check_x != x:
            flipList.append([check_y, check_x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipSE(gameBoard, myNum, x, y):
    flipList = []
    anchor = None
    for check_x, check_y in zip(range(x, 8), range(y, 8)):
        if gameBoard.gameBoard[check_y][check_x] == 0 and check_x != x:
            break
        if gameBoard.gameBoard[check_y][check_x] != myNum:
            flipList.append([check_y, check_x])
            continue
        if gameBoard.gameBoard[check_y][check_x] == myNum and check_x != x:
            flipList.append([check_y, check_x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipSW(gameBoard, myNum, x, y):
    flipList = []
    anchor = False
    for check_x, check_y in zip(range(x, 0, -1), range(y, 8)):
        if gameBoard.gameBoard[check_y][check_x] == 0 and check_x != x:
            break
        if gameBoard.gameBoard[check_y][check_x] != myNum:
            flipList.append([check_y, check_x])
            continue
        if gameBoard.gameBoard[check_y][check_x] == myNum and check_x != x:
            flipList.append([check_y, check_x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum

def flipNW(gameBoard, myNum, x, y):
    flipList = []
    anchor = None
    for check_x, check_y in zip(range(x, 0, -1), range(y, 0, -1)):
        if gameBoard.gameBoard[check_y][check_x] == 0 and check_x != x:
            break
        if gameBoard.gameBoard[check_y][check_x] != myNum:
            flipList.append([check_y, check_x])
            continue
        if gameBoard.gameBoard[check_y][check_x] == myNum and check_x != x:
            flipList.append([check_y, check_x])
            anchor = True
            break
    if anchor == True and len(flipList)>=2:
        for z in range(len(flipList)):
            row, column = flipList[z]
            gameBoard.gameBoard[row][column] = myNum


