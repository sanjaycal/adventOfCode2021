import sys


data = open(sys.argv[-1],"r").read().split(',')

a  = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in data:
    a[int(i)] +=1

data = a


def step(data):
    odata = data
    nos = data[0]
    data[0] = data[1]
    data[1] = data[2]
    data[2] = data[3]
    data[3] = data[4]
    data[4] = data[5]
    data[5] = data[6]
    data[6] = data[7]
    data[7] = data[8]
    data[6] += nos
    data[8] = nos
    return data


for i in range(256):
    print(i)
    data = step(data)

print(sum(data))