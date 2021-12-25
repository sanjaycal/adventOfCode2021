from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = [list(x) for x in open(sys.argv[-1],"r").read().split('\n')]




def stepe(data):
    d = deepcopy(data)
    nd = []
    for i in range(len(d)):
        a = []
        for j in range(len(d[0])):
            a.append('.')
        nd.append(a)
    for x in range(len(d)):
        for y in range(len(d[0])):
            if d[x][y] == ">":
                tc = y+1
                if y==len(d[0])-1:
                    tc = 0
                if d[x][tc] == ".":
                    nd[x][tc] = ">"
                else:
                    nd[x][y] = '>'
            if d[x][y]=='v':
                nd[x][y] = 'v'
    return nd
    

def steps(data):
    d = deepcopy(data)
    nd = []
    for i in range(len(d)):
        a = []
        for j in range(len(d[0])):
            a.append('.')
        nd.append(a)
    for x in range(len(d)):
        for y in range(len(d[0])):
            if d[x][y] == "v":
                tc = x+1
                if x==len(d)-1:
                    tc = 0
                if d[tc][y] == ".":
                    nd[tc][y] = "v"
                else:
                    nd[x][y] = 'v'
            if d[x][y]=='>':
                nd[x][y] = '>'
    return nd


def step(data):
    d = deepcopy(data)
    d = stepe(d)
    d = steps(d)
    return d


def p(data):
    d = deepcopy(data)
    for i in d:
        s = ""
        for j in i:
            s+=j
        print(s)


for i in range(1000000):
    od = deepcopy(data)
    data = step(data)
    p(data)
    print("\n")
    if od==data:
        print(i+1)
        break