from Board import *
from Move import *
from Flip import *

trace = True

gameOver = False

alphaNumeric = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

myTurn = False

global myColor
global myNum
global opponentColor
global opponentNum

gameBoard = Board("gameBoard")
gameBoard.initalizeBoard()

#Game Begins.
colorChoice = input()
if colorChoice == "I W":
    myColor = "W"
    opponentColor = "B"
    myNum = 1
    opponentNum = 2
    print("R W")
    myTurn = False

if colorChoice == "I B":
    myColor = "B"
    opponentColor = "W"
    myNum = 2
    opponentNum = 1
    print("R B")
    myTurn = True

while gameOver != True:
    if myTurn == False:
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
        myTurn = True
    if myTurn == True:
        nextMove = Move("NextMove", myNum, opponentNum)
        moveList = nextMove.moveList(gameBoard)
        #Forgive me.
        for move in range(len(moveList)):
            if gameBoard.gameBoard[moveList[move][1]][moveList[move][0]] == 0:
                gameBoard.playMove(moveList[move][0], moveList[move][1], myNum)
                gameBoard.broadcastMove(moveList[move][0], moveList[move][1], myColor)
                selfFlip(gameBoard, myNum, moveList[move][0], moveList[move][1])
                break
        nextMove.emptyMoves()
        myTurn=False





