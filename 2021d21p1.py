from os import SCHED_BATCH
import sys
import math
import ast
from copy import deepcopy

data = [int(x) for x in open(sys.argv[-1],"r").read().split('\n')]
print(data)

c = 0

s = [0,0]

while True:
    for i in range(3):
        data[0] += (c+1)%100
        data[0] = (data[0]-1)%10+1
        c+=1
    s[0]+=data[0]
    if s[0]>=1000:
        break
    for i in range(3):
        data[1] += (c+1)%100
        data[1] = (data[1]-1)%10+1
        c+=1
    s[1]+=data[1]
    if s[1]>=1000:
        break

print(c)
print(s)
print(c*min(s))