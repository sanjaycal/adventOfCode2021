import sys

data = open(sys.argv[-1],"r").read().split(',')

y = data[-1].split('y=')[-1].split('..')

y = [int(y[0]),int(y[1])]

x = data[0].split('x=')[-1].split('..')

x = [int(a) for a in x]


def step(x,y,dx,dy):
    x += dx
    y+=dy
    if dx>0:
        dx-=1
    elif dx<0:
        dx+=1
    dy-=1
    return x,y,dx,dy

def isInRegion(dx,dy,rx,ry):
    iv = [dx,dy]
    p = [0,0]
    my = 0
    for i in range(500):
        a,b,dx,dy = step(p[0],p[1],dx,dy)
        p = [a,b]
        if b>my:
            my = b
        if rx[0] <= p[0] <= rx[1] and ry[0]<=p[1]<=ry[1]:
            return my,iv
    return "FAIL","FAIL"

h = 0



for dx in range(300):
    print(dx)
    for dy in range(-100,300):
        a,b = isInRegion(dx,dy,x,y)
        if a!= "FAIL":
            h +=1

print(h)


