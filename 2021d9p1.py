import sys


data = open(sys.argv[-1],"r").read().split('\n')


def getAdj(data,x,y):
    if len(data)-1!=x!=0 and len(data[0])-1!=y!=0:
        adj = [data[x-1][y],data[x+1][y],data[x][y-1],data[x][y+1]]
    elif x==0 and len(data[0])-1!=y!=0:
        adj = [data[x+1][y],data[x][y-1],data[x][y+1]]
    elif x==len(data)-1 and len(data[0])-1!=y!=0:
        adj = [data[x-1][y],data[x][y-1],data[x][y+1]]
    elif y==0 and len(data)-1!=x!=0:
        adj = [data[x-1][y],data[x+1][y],data[x][y+1]]
    elif y==len(data[0])-1 and len(data)-1!=x!=0:
        adj = [data[x-1][y],data[x+1][y],data[x][y-1]]
    elif y==0 and x==0:
        adj = [data[x+1][y],data[x][y+1]]
    elif y==0 and x==len(data)-1:
        adj = [data[x-1][y],data[x][y+1]]
    elif y==len(data[0])-1 and x==0:
        adj = [data[x+1][y],data[x][y-1]]
    elif y==len(data[0])-1 and x==len(data)-1:
        adj = [data[x-1][y],data[x][y-1]]
    return adj

lps = 0

for x in range(len(data)):
    for y in range(len(data[0])):
        print([x,y])
        d = getAdj(data,x,y)
        p = data[x][y]
        c = 0
        for i in d:
            if int(i)>int(p):
                c+=1
        if c==len(d):
            lps+=int(p)+1

print(lps)
    