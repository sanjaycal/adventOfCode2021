import sys


data = open(sys.argv[-1],"r").read().split('\n')



a = []

for i in data:
    b = []
    for j in i:
        b.append(int(j))
    a.append(b)



data = a



def step(data):
    nf = 0
    flashed = []
    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y]+=1
    for i in range(10):
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y]>9 and not [x,y] in flashed:
                    nf+=1
                    if x!=0:
                        if y!=0:
                            data[x-1][y-1] += 1
                        data[x-1][y] += 1
                        if y!=len(data[x])-1:
                            data[x-1][y+1] += 1
                    if x!=len(data)-1:
                        if y!=0:
                            data[x+1][y-1] += 1
                        data[x+1][y] += 1
                        if y!=len(data[x])-1:
                            data[x+1][y+1] += 1
                    if y!=len(data[x])-1:
                        data[x][y+1] += 1
                    if y!=0:
                        data[x][y-1] += 1
                    
                    
                    
                    
                    data[x][y] = 0
                    flashed.append([x,y])
    for i in flashed:
        data[i[0]][i[1]] = 0
    return data,nf

f = 0

for i in range(100):
    data,nf = step(data)
    f+=nf

print(f)
