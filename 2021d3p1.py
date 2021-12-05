from os import environ, set_blocking
from posix import GRND_NONBLOCK
import sys


data = open(sys.argv[-1],"r").read().split('\n')


b1 = [0,0]
b2 = [0,0]
b3 = [0,0]
b4 = [0,0]
b5 = [0,0]

b = []

for i in range(len(data[1])):
    b.append([0,0])

for i in data:
    a = i
    for j in range(len(i)):
        b[j][int(i[j])]+=1


gr = []
er = []


for i in b:
    if i[0]>i[1]:
        gr.append(0)
        er.append(1)
    else:
        gr.append(1)
        er.append(0)

ern = 0
grn = 0

n = 2**(len(data[1])-1)


for i in range(len(data[1])):
    ern += n*er[i]
    grn += n*gr[i]
    n = n/2

print(er)
print(gr)

print(ern)
print(grn)

print(ern*grn)