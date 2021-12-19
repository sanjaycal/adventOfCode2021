from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = open(sys.argv[-1],"r").read().split('\n')


a = []

c = -1

for i in data:
    if i!='':
        if i[0:2]=='--':
            c+=1
            a.append([])
        else:
            a[c].append([int(x) for x in i.split(',')])

data = a


def normalize(scanner,n):
    sc = deepcopy(scanner)
    tn = sc[n]
    nsc = []
    for i in sc:
        a = [0,0,0]
        a[0] = i[0]-tn[0]
        a[1] = i[1]-tn[1]
        a[2] = i[2]-tn[2]
        nsc.append(a)
    return nsc

def checkOverlaps(scannerA, scannerB):
    c = 0
    for i in range(len(scannerA)):
        if scannerA[i] in scannerB:
            c+=1
    if c>=12:
        return True
    return False

def checkIfOverlap(scannerA,scannerB):
    for a in range(len(scannerA)):
        for b in range(len(scannerB)-11):
            na = normalize(deepcopy(scannerA),a)
            nb = normalize(deepcopy(scannerB),b)
            if checkOverlaps(na,nb):
                sbp = [scannerA[a][0]-scannerB[b][0],scannerA[a][1]-scannerB[b][1],scannerA[a][2]-scannerB[b][2]]
                return sbp

def rotate(scanner, rot):
    ns = deepcopy(scanner)
    np = []
    for i in ns:
        b = [0,0,0]
        u = rot[0]
        if u > 0:
            b[abs(u)-1] = i[0]
        if u<0:
            b[abs(u)-1] = -i[0]
            
        u = rot[1]
        if u > 0:
            b[abs(u)-1] = i[1]
        if u<0:
            b[abs(u)-1] = -i[1]

        u = rot[2]
        if u > 0:
            b[abs(u)-1] = i[2]
        if u<0:
            b[abs(u)-1] = -i[2]
        np.append(b)
    return(np)


allLegalRotations = [[1,2,3],
                     [1,-3,2],
                     [1,-2,-3],
                     [1,3,-2],
                     [-1,-2,3],
                     [-1,3,2],
                     [-1,2,-3],
                     [-1,-3,-2],
                     [2,1,-3],
                     [2,-3,-1],
                     [2,-1,3],
                     [2,3,1],
                     [-2,1,3],
                     [-2,3,-1],
                     [-2,-1,-3],
                     [-2,-3,1],
                     [3,1,2],
                     [3,2,-1],
                     [3,-1,-2],
                     [3,-2,1],
                     [-3,1,-2],
                     [-3,-2,-1],
                     [-3,-1,2],
                     [-3,2,1]]


rps = [[[1,2,3],[0,0,0],data[0],data[0]]]

ps = [0]


td = {}

while len(rps)!=len(data):
    for p in range(len(data)-1):
        print(p)
        if not p+1 in ps:
            for i in allLegalRotations:
                r2 = rotate(data[p+1],i)
                for j in rps:
                    try:
                        tmp = td[str(p+1)]
                    except KeyError:
                        td[str(p+1)] = []
                    if not ([i,j] in td[str(p+1)]):
                        td[str(p+1)].append([i,j])
                        a = checkIfOverlap(j[-1],r2)
                        if a != None:
                            b = [a[0],a[1],a[2]]
                            print(p)
                            r3 = []
                            for k in r2:
                                r3.append([k[0]+b[0],k[1]+b[1],k[2]+b[2]])
                            if not [i,b,r3] in rps:
                                rps.append([i,b,r3])
                                ps.append(p+1)
                            break



ls = [x[1] for x in rps]


def manhattanDistance(a,b):
    s = abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])
    return s

mmd = 0

for i in ls:
    for j in ls:
        if i!=j:
            a = manhattanDistance(i,j)
            if a>mmd:
                mmd = a

print(mmd)

print([x[0:2] for x in rps])
