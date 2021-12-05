from os import environ, set_blocking
from posix import GRND_NONBLOCK
import sys


data = open(sys.argv[-1],"r").read().split('\n')
ogdata = data.copy()



def findMostCommonBit(dta, bitn):
    cnt = [0,0]
    for i in dta:
        cnt[int(i[bitn])] += 1
    return int(cnt[1]>=cnt[0])



for i in range(12):
    if len(data)!= 1:
        a = findMostCommonBit(data, i)
        k = len(data)
        cnt = 0
        for j in range(k):
            if int(data[j-cnt][i])==a:
                data.pop(j-cnt)
                cnt+=1
    
print(data)


for i in range(12):
    if len(ogdata)!=1:
        a = findMostCommonBit(ogdata, i)
        k = len(ogdata)
        cnt = 0
        for j in range(k):
            if int(ogdata[j-cnt][i])!=a:
                ogdata.pop(j-cnt)
                cnt+=1
    

print(ogdata)


ern = 0
grn = 0

n = 2**(12-1)



for i in range(12):
    ern += n*int(data[0][i])
    grn += n*int(ogdata[0][i])
    n = n/2


print(ern*grn)