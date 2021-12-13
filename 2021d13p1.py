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

grid = []
for x in range(100):
    a = []
    for y in range(100):
        a.append(0)
    grid.append(a)



def convertToGrid(points):
    grid = []
    for x in range(2000):
        a = []
        for y in range(2000):
            a.append(0)
        grid.append(a)
    for point in points:
        grid[point[0]][point[1]] = 1
    return grid


def fold(points, axis, value):
    np  = []
    if axis=="x":
        for point in points:
            np.append([abs(point[0]-value),point[1]])
    if axis=="y":
        for point in points:
            np.append([point[0],abs(point[1]-value)])
    return np



for i in folds:
    points = fold(points, folds[i][11], int(folds[i].split('=')[-1]))


s = 0

for i in grid:
    s += sum(i)
print(s)


