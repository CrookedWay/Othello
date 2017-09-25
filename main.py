from Board import *
from Move import *

startBoard = Board("startBoard")
startBoard.initalizeBoard()
startBoard.printBoard()
nextMove = Move("NextMove")
nextMove.moveList(startBoard, '1')