from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = open(sys.argv[-1],"r").read().split('\n')


cubes = []

for i in data:
    a = []
    a.append(int(i.split(',')[0].split('=')[1].split('..')[0]))
    a.append(int(i.split(',')[0].split('=')[1].split('..')[1])+1)
    a.append(int(i.split(',')[1].split('=')[1].split('..')[0]))
    a.append(int(i.split(',')[1].split('=')[1].split('..')[1])+1)
    a.append(int(i.split(',')[2].split('=')[1].split('..')[0]))
    a.append(int(i.split(',')[2].split('=')[1].split('..')[1])+1)
    a.append(i.split(' ')[0])
    cubes.append(a)

def step(data,bounds):
    d = deepcopy(data)
    b = deepcopy(bounds)
    xs = b[0]
    xe = b[1]
    ys = b[2]
    ye = b[3]
    zs = b[4]
    ze = b[5]
    nc = []
    for i in range(len(d)):
        cb = d[i]
        if (xe > cb[0] and xs < cb[1]) and (ye > cb[2] and ys < cb[3]) and (ze > cb[4] and zs < cb[5]):
            if cb[0] < xs:
                nb = [cb[0],xs,cb[2],cb[3],cb[4],cb[5],cb[6]]
                cb[0] = xs
                nc.append(nb)
            if cb[1] > xe:
                nb = [xe,cb[1],cb[2],cb[3],cb[4],cb[5],cb[6]]
                cb[1] = xe
                nc.append(nb)
            if cb[2] < ys:
                nb = [cb[0],cb[1],cb[2],ys,cb[4],cb[5],cb[6]]
                cb[2] = ys
                nc.append(nb)        
            if cb[3] > ye:
                nb = [cb[0],cb[1],ye,cb[3],cb[4],cb[5],cb[6]]
                cb[3] = ye
                nc.append(nb) 
            if cb[4] < zs:
                nb = [cb[0],cb[1],cb[2],cb[3],cb[4],zs,cb[6]]
                cb[4] = zs
                nc.append(nb)        
            if cb[5] > ze:
                nb = [cb[0],cb[1],cb[2],cb[3],ze,cb[5],cb[6]]
                cb[5] = ze
                nc.append(nb)
        else:
            nc.append(cb)

    nc.append(cube)
    d = nc
    return d





d = []
for cube in cubes:
    d = step(d,cube)
    

s = 0
for i in range(len(d)): 
    cb = d[i]
    if cb[6]=='on': 
        s+=(cb[1]-cb[0])*(cb[3]-cb[2])*(cb[5]-cb[4])

print(s)