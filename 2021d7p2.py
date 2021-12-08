import sys


data = open(sys.argv[-1],"r").read().split(',')

a  = []

for i in data:
    a.append(int(i))


data = a

print(data)


def sm(n):
    s = 0
    for i in range(n):
        s+=i
    return s+n
def calculateFuelCost(data,n):
    c = 0
    for i in data:
        c += sm(abs(i-n))
    return c


minv = 999999999999



print(max(data))
for i in range(max(data)-300):
    print(i)
    if calculateFuelCost(data,i)<minv:
        minv = calculateFuelCost(data,i)

print(minv)