from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = open(sys.argv[-1],"r").read().split('\n')


a = []

for i in data:
    b = []
    b.append(i.split(' ')[0])
    b.append([int(x) for x in i.split(',')[0].split('=')[1].split('..')])
    b.append([int(x) for x in i.split(',')[1].split('=')[1].split('..')])
    b.append([int(x) for x in i.split(',')[-1].split('=')[1].split('..')])
    a.append(b)

data = a

board = {}




def runStep(step,board):
    b = deepcopy(board)
    if step[1][0]<-50 or step[1][1]>50 or step[2][0]<-50 or step[2][1]>50 or step[2][0]<-50 or step[2][1]>50:
        return b
    for x in range(step[1][0],step[1][1]+1):
        for y in range(step[2][0],step[2][1]+1):
            for z in range(step[3][0],step[3][1]+1):
                try:
                    tmp = b[str(x)]
                except KeyError:
                    b[str(x)] = {}
                try:
                    tmp = b[str(x)][str(y)]
                except KeyError:
                    b[str(x)][str(y)] = {}
                try:
                    tmp = b[str(x)][str(y)][str(z)]
                except KeyError:
                    b[str(x)][str(y)][str(z)] = 0
                if step[0]=='on':
                    b[str(x)][str(y)][str(z)] = 1
                else:
                    b[str(x)][str(y)][str(z)] = 0
    return b





def getSum(board):
    s = 0
    for x in board.keys():
        for y in board[x].keys():
            for z in board[x][y].keys():
                s+=board[x][y][z]
    return s


c = 0
for i in data[:25]:
    print(c)
    c+=1
    board = runStep(i,board)

print(getSum(board))

