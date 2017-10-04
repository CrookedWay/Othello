import asyncio
import argparse

from Board import *
from Move import *

trace = False

gameOver = False

alphaNumeric = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

myTurn = False
myColor = None
opponentColor = None


startBoard = Board("startBoard")
startBoard.initalizeBoard()

#Game Begins.
colorChoice = input()
if colorChoice == "I W":
    myColor = "w"
    opponentColor = "b"
    print("R W")
if colorChoice == "I B":
    myColor = "b"
    opponentColor = "w"
    print("R B")

while gameOver != True:
    if myTurn == False:
        currentAction = input()
        if len(currentAction) == 1 and currentAction[0] != "n":
                print("Pass")
        elif currentAction[0] == "n":
            gameOver = True
        else:
            column = int(alphaNumeric[currentAction[2]])
            row = int(currentAction[4])
            startBoard.takeMove(column, row, opponentColor)
        if trace == True:
            startBoard.prettyPrintBoard()
    if myTurn == True:
# nextMove = Move("NextMove")
# nextMove.moveList(startBoard, '1')



