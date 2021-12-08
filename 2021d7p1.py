import sys


data = open(sys.argv[-1],"r").read().split(',')

a  = []

for i in data:
    a.append(int(i))


data = a

print(data)

print(sum(a)/len(a))

def calculateFuelCost(data,n):
    c = 0
    for i in data:
        c += abs(i-n)
    return c


minv = 999999



for i in range(max(data)):
    if calculateFuelCost(data,i)<minv:
        minv = calculateFuelCost(data,i)

print(minv)