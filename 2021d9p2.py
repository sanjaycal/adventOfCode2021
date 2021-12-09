from os import remove
import sys


data = open(sys.argv[-1],"r").read().split('\n')


def getAdj(data,x,y):
    if len(data)-1!=x!=0 and len(data[0])-1!=y!=0:
        adj = [[data[x-1][y],data[x+1][y],data[x][y-1],data[x][y+1]],[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]]
    elif x==0 and len(data[0])-1!=y!=0:
        adj = [[data[x+1][y],data[x][y-1],data[x][y+1]],[[x+1,y],[x,y-1],[x,y+1]]]
    elif x==len(data)-1 and len(data[0])-1!=y!=0:
        adj = [[data[x-1][y],data[x][y-1],data[x][y+1]],[[x-1,y],[x,y-1],[x,y+1]]]
    elif y==0 and len(data)-1!=x!=0:
        adj = [[data[x-1][y],data[x+1][y],data[x][y+1]],[[x-1,y],[x+1,y],[x,y+1]]]
    elif y==len(data[0])-1 and len(data)-1!=x!=0:
        adj = [[data[x-1][y],data[x+1][y],data[x][y-1]],[[x-1,y],[x+1,y],[x,y-1]]]
    elif y==0 and x==0:
        adj = [[data[x+1][y],data[x][y+1]],[[x+1,y],[x,y+1]]]
    elif y==0 and x==len(data)-1:
        adj = [[data[x-1][y],data[x][y+1]],[[x-1,y],[x,y+1]]]
    elif y==len(data[0])-1 and x==0:
        adj = [[data[x+1][y],data[x][y-1]],[[x+1,y],[x,y-1]]]
    elif y==len(data[0])-1 and x==len(data)-1:
        adj = [[data[x-1][y],data[x][y-1]],[[x-1,y],[x,y-1]]]
    return adj

lps = 0

def isLower(pn,ps):
    c = 0
    for i in ps[0]:
        if int(i)<int(pn):
            c+=1
    if c==0:
        return True
    return False

def getBasin(data,x,y,pia):
    d = getAdj(data,x,y)
    p = data[x][y]
    c = 0
    if int(p)!=9:
        for i in range(len(d[0])):
            if d[1][i-c] in pia:
                d[1].pop(i-c)
                d[0].pop(i-c)
                c+=1
        if isLower(p,d):
            pia.append([x,y])
            for i in d[1]:
                pia = getBasin(data,i[0],i[1],pia)
    return pia

a = []

for x in range(len(data)):
    for y in range(len(data[0])):
        b = getBasin(data,x,y,[])
        if len(b) !=0:
            c = []
            for i in b:
                if not(i in c):
                    c.append(i)
            a.append(len(c))

print(sorted(a)[-1]*sorted(a)[-2]*sorted(a)[-3])
            

    