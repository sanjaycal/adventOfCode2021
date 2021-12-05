import sys

data = open(sys.argv[-1],"r").read().split('\n')

points = []

for i in data:
    a = i.split(' -> ')
    b = []
    for j in a:
        c = j.split(",")
        d = []
        for k in c:
            d.append(int(k))
        b.append(d)
    points.append(b)

minx = 999999
miny = 999999
maxx = 0
maxy = 0

for point in points:
    if point[0][0] < minx:
        minx = point[0][0]
    if point[1][0] < minx:
        minx = point[1][0]
    if point[0][0] > maxx:
        maxx = point[0][0]
    if point[1][0] > maxx:
        maxx = point[1][0]
    if point[0][1] < miny:
        miny = point[0][1]
    if point[1][1] < miny:
        miny = point[1][1]
    if point[0][1] > maxy:
        maxy = point[0][1]
    if point[1][1] > maxy:
        maxy = point[1][1]


mask = []

for i in range(minx,maxx+99):
    a = []
    for j in range(miny, maxy+99):
        a.append(0)
    mask.append(a)

for point in points:
    if point[0][0] == point[1][0]:
        for i in range(min([point[0][1],point[1][1]]),max([point[0][1],point[1][1]])+1):
            mask[point[0][0]][i] +=1
    elif point[0][1] == point[1][1]:
        for i in range(min([point[0][0],point[1][0]]),max([point[0][0],point[1][0]])+1):
            mask[i][point[0][1]] +=1
    else:
        for i in range(max([point[0][1],point[1][1]])-min([point[0][1],point[1][1]])+1):
            xdir = int((point[0][0]-point[1][0])/(((point[0][0]-point[1][0])**2)**0.5))*-1
            ydir = int((point[0][1]-point[1][1])/(((point[0][1]-point[1][1])**2)**0.5))*-1
            mask[i*xdir+point[0][0]][i*ydir+point[0][1]] +=1
                
count = 0

for i in mask:
    for j in i:
        if j>1:
            count+=1

print(mask)
print(count)