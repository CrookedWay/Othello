from Board import *
from Move import *
from Flip import *

trace = True
gameOver = False
myTurn = False

myColor = None
myNum = None
opponentColor = None
opponentNum = None

gameBoard = Board()
gameBoard.initalizeBoard()
if trace:
    gameBoard.prettyPrintBoard()

#Game Begins.
colorChoice = input()
if colorChoice == "I W":
    myColor = "W"
    opponentColor = "B"
    myNum = 1
    opponentNum = 2
    print("R W")
    myTurn = False
else:
    myColor = "B"
    opponentColor = "W"
    myNum = 2
    opponentNum = 1
    print("R B")
    myTurn = True

while not gameOver:
    if not myTurn:
        currentAction = input()
        if len(currentAction) == 1 and currentAction[0] != "n":
                print("Pass")
        elif currentAction[0] == "n":
            gameOver = True
        else:
            column = currentAction[2]
            row = currentAction[4]
            gameBoard.takeMove(column, row, opponentNum)
            takeFlip(gameBoard, opponentNum, column, row)
            if trace:
                gameBoard.prettyPrintBoard()
        myTurn = True
    if myTurn:
        nextMove = Move(myNum, opponentNum)
        moveList = nextMove.moveList(gameBoard)
        if trace:
            nextMove.printMoves()
        #Forgive me.
        for move in range(len(moveList)):
            if gameBoard.gameBoard[moveList[move][1]][moveList[move][0]] == 0:
                gameBoard.playMove(moveList[move][0], moveList[move][1], myNum)
                gameBoard.broadcastMove(moveList[move][0], moveList[move][1], myColor)
                selfFlip(gameBoard, myNum, moveList[move][0], moveList[move][1])
                if trace:
                    gameBoard.prettyPrintBoard()
                break
        nextMove.emptyMoves()
        myTurn=False





