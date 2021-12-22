from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = [int(x) for x in open(sys.argv[-1],"r").read().split('\n')]
print(data)

c = 0


d = {str([data[0],0,data[1],0,False]):1}



p = []

for i in range(3):
    for j in range(3):
        for k in range(3):
            p.append(i+1+j+1+k+1)



w = [0,0]


while True:
    c+=1
    od = deepcopy(d)
    d = {}
    for i in od.keys():
        for pr in p:
            ind = ast.literal_eval(i)
            ind[0]+=pr
            ind[0]=(ind[0]-1)%10+1
            ind[1]+=ind[0]
            if ind[1]>=21:
                w[0]+=od[i]
            else:
                if not(str(ind) in d.keys()):
                    d[str(ind)] = 0
                d[str(ind)] +=od[i]
    od = deepcopy(d)
    d = {}
    for i in od.keys():
        for pr in p:
            ind = ast.literal_eval(i)
            oi1 = ind[3]
            ind[2]+=pr
            ind[2]=(ind[2]-1)%10+1
            ind[3]+=ind[2]
            if ind[3]>=21:
                w[1]+=od[i]
            else:
                if not(str(ind) in d.keys()):
                    d[str(ind)] = 0
                d[str(ind)] +=od[i]
    print(c)
    if len(d.keys())==0:
        break

print(w)
