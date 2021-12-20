from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = open(sys.argv[-1],"r").read().split('\n\n')


converter = data[0]

image = data[1].split('\n')


nte = 2


def convert(img):
    global nte
    a = []
    image = deepcopy(img)
    for i in image:
        b = []
        for j in i:
            if j==".":
                b.append('0')
            else:
                b.append('1')
        a.append(b)
    return a

def expand(img,ov):
    global nte
    tbr = []

    for i in range(len(img[0])+2*nte):
        tbr.append(ov)
    a = []

    for i in range(nte):
        a.append(tbr)

    for i in img:
        b = []
        for jjj in range(nte):
            b.append(ov)
        for j in i:
            if j=="0" or j=='.':
                b.append('0')
            else:
                b.append('1')
        for i in range(nte):
            b.append(ov)
        a.append(b)
    for i in range(nte):
        a.append(tbr)
    return a



def enhance1(img,converter,x,y):
    v = img[x-1][y-1] + img[x-1][y] + img[x-1][y+1] + img[x][y-1] + img[x][y] + img[x][y+1] + img[x+1][y-1] + img[x+1][y] + img[x+1][y+1]
    iv = int(v,2)
    return converter[iv]


def enhance(img,converter,c):
    nimg = []
    oimg = expand(deepcopy(img),str(c%2))
    for x in range(len(oimg)-nte):
        a = []
        for y in range(len(oimg)-nte):
            a.append(enhance1(oimg,converter,x+1,y+1))
        nimg.append(a)
    return nimg



a = image

for i in range(2):
    if converter[0] == '.':
        a = enhance(a,converter,0)
    elif converter[0] == '#':
        a = enhance(a,converter,i)


a = convert(a)

s = 0

for i in a:
    for j in i:
        s+=int(j)

print(s)