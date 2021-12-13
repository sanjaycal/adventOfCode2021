import sys


data = open(sys.argv[-1],"r").read().split('\n\n')

points = data[0].split('\n')
folds = data[1].split('\n')

p = []

for i in points:
    a = []
    b = i.split(',')
    for j in b:
        a.append(int(j))
    p.append(a)

points = p





def convertToGrid(points):
    grid = []
    for x in range(40):
        a = []
        for y in range(6):
            a.append(' ')
        grid.append(a)
    for point in points:
        grid[point[0]][point[1]] = '#'
    return grid


def fold(points, axis, value):
    np  = []
    if axis=="x":
        for point in points:
            np.append([value - abs(point[0]-value),point[1]])
    if axis=="y":
        for point in points:
            np.append([point[0],value - abs(point[1]-value)])
    return np


for i in range(len(folds)):
    points = fold(points, folds[i][11], int(folds[i].split('=')[-1]))
    print([folds[i][11],int(folds[i].split('=')[-1])])

print(points)
grid = convertToGrid(points)
c = 0
for i in range(len(grid[0])):
    s = ""
    for j in range(len(grid)):
        s+=grid[j][i]
    print(s)
