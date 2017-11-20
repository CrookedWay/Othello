import time
from threading import Thread
import numpy as np
from Board import *
from Move import *
from Flip import *

"""
Largest Known number of moves is 24. Average game length is 16 according to this review, which sounds right to me.

#http://casualgamerevolution.com/blog/2015/01/the-closet-report-othello

We want to give a small amount of time at the beginning and even more in the middle of the game.

I'm going to multiply an iterable of it by a normalized distribution. We'll see how that works out.

#We're talking wall clock time.
"""

class GameTree(list):
    def __init__(self, initialBoard, scoreCard):
        super().__init__()
        self.initialBoard = initialBoard
        self.children = []


    class Node(object):
        def __init__(self, data):
            self.data = data
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

def alpha(initialBoard, scoreCard, moves):
    alphaSum = []
    for element in moves:
        alphaSum.append([element, initialBoard[element]*scoreCard[element]])
    alphaSum.sort(key=lambda x: x[2])
    for x in alphaSum:
        newGameBoard = (alphaSum[x][0][0], alphaSum[x][0][1], myNum)
        moveList = .moveList(gameBoard)

def timer():



def alphaBeta(move, gameBoard):
