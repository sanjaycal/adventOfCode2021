import sys


data = open(sys.argv[-1],"r").read().split('\n\n')

polymer = data[0]

pchanges = data[1].split('\n')

c = {}

for i in pchanges:
    c[i.split(' -> ')[0]] = i.split(' -> ')[1]


pchanges = c

def step(polymer, pchanges):
    na = ""
    for i in range(len(polymer)-1):
        na += pchanges[polymer[i]+polymer[i+1]]
    np = ""
    for i in range(len(polymer)-1):
        np += polymer[i]
        np += na[i]
    np += polymer[-1]
    return np


for i in range(10):
    polymer = step(polymer,pchanges)
    print(i)

av = {}

for i in polymer:
    if not i in av.keys():
        av[i] = 1
    else:
        av[i] +=1

max = ['',0]

for i in av.keys():
    if av[i] > max[1]:
        max = [i,av[i]]

min = ['',10**99]

for i in av.keys():
    if av[i] < min[1]:
        min = [i,av[i]]

print(max[1]-min[1])