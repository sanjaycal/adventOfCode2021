import sys


data = open(sys.argv[-1],"r").read().split('\n\n')

polymer = data[0]
fc = polymer[0]
lc = polymer[-1]
pchanges = data[1].split('\n')

c = {}

for i in pchanges:
    c[i.split(' -> ')[0]] = i.split(' -> ')[1]


pchanges = c

c = {}

for i in range(len(polymer)-1):
    if not polymer[i]+polymer[i+1] in c.keys():
        c[polymer[i]+polymer[i+1]] = 1
    else:
        c[polymer[i]+polymer[i+1]] += 1

polymer = c

def step(polymer, pchanges):
    np = {}
    for i in polymer.keys():
        v = polymer[i]
        ta = pchanges[i]
        k1 = i[0]+ta
        k2 = ta+i[1]
        if not k1 in np.keys():
            np[k1] = v
        else:
            np[k1] += v
        if not k2 in np.keys():
            np[k2] = v
        else:
            np[k2] += v
    return np


for i in range(40):
    polymer = step(polymer,pchanges)
    print(i)

print(polymer)

av = {}

c = 0

for i in polymer.keys():
    if not i[0] in av.keys():
        av[i[0]] = polymer[i]
    else:
        av[i[0]] += polymer[i]
    if not i[1] in av.keys():
        av[i[1]] = polymer[i]
    else:
        av[i[1]] += polymer[i]
    c+=1

av[fc]+=1
av[lc] +=1

for i in av.keys():
    av[i] = av[i]/2

print(av)

max = ['',0]

for i in av.keys():
    if av[i] > max[1]:
        max = [i,av[i]]

min = ['',10**99]

for i in av.keys():
    if av[i] < min[1]:
        min = [i,av[i]]

print(int((max[1]-min[1])))