import sys


data = open(sys.argv[-1],"r").read().split(',')

a  = []

for i in data:
    a.append(int(i))


data = a


def step(data):
    for i in range(len(data)):
        data[i] = data[i]-1
    for i in range(len(data)):
        if data[i]==-1:
            data[i]=6
            data.append(8)
    return data


for i in range(80):
    print(i)
    data = step(data)

print(len(data))