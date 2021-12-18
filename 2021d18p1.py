import sys
import math
import ast
data = [ast.literal_eval(x) for x in open(sys.argv[-1],"r").read().split('\n')]






def depth(l):
    if isinstance(l, list):
        return 1 + max(depth(item) for item in l)
    else:
        return 0


def getNestLen(num, n, p,q):
    np = p.copy()
    if n==q:
        return str(np)
    pp = ""
    if type(num[0])==list:
        a = getNestLen(num[0],n+1,np+[0],q)
        if len(a)>=11:
            return a
    if type(num[1])==list:
        a = getNestLen(num[1],n+1,np+[1],q)
        if len(a)>=11:
            return a
    return pp

def explode(n):
    nc = n.copy()
    kk = depth(nc)
    if kk<5:
        return nc
    hh = getNestLen(n,0,[],kk-1).replace('[','').replace(']','').replace(' ','').split(",")
    if hh==['']:
        return nc
    b = [int(x) for x in hh]
    nib = ''
    for i in b:
        nib+=str(i)
    nib = int(nib,2)
    nm1 = bin(nib-1)[2:]
    np1 = bin(nib+1)[2:]
    while len(nm1)<kk-1:
        nm1 = '0' +nm1
    while len(np1)<kk-1:
        np1 = '0'+np1
    if b != None:
        a  = n.copy()
        for i in b:
            a = a[i]
        nc[int(b[0])][int(b[1])][int(b[2])][int(b[3])] = 0
        if nib-1>=0:
            if type(nc[int(nm1[0])]) == list:
                if type(nc[int(nm1[0])][int(nm1[1])]) == list:
                    if type(nc[int(nm1[0])][int(nm1[1])][int(nm1[2])]) == list:
                        if type(nc[int(nm1[0])][int(nm1[1])][int(nm1[2])][int(nm1[3])]) == list:
                            if type(nc[int(nm1[0])][int(nm1[1])][int(nm1[2])][int(nm1[3])][int(nm1[4])]) == list:
                                nc[int(nm1[0])][int(nm1[1])][int(nm1[2])][int(nm1[3])][int(nm1[4])][1] += a[0]
                            else:
                                nc[int(nm1[0])][int(nm1[1])][int(nm1[2])][int(nm1[3])][int(nm1[4])] += a[0]
                        else:
                            nc[int(nm1[0])][int(nm1[1])][int(nm1[2])][int(nm1[3])] += a[0]
                    else:
                        nc[int(nm1[0])][int(nm1[1])][int(nm1[2])] += a[0]
                else:
                    nc[int(nm1[0])][int(nm1[1])] += a[0]
            else:
                nc[int(nm1[0])] += a[0]
        if nib+1<16:
            if type(nc[int(np1[0])]) == list:
                if type(nc[int(np1[0])][int(np1[1])]) == list:
                    if type(nc[int(np1[0])][int(np1[1])][int(np1[2])]) == list:
                        if (type(nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])]) == list):
                            try:
                                if type(nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])][int(np1[4])]) == list:
                                    nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])][int(np1[4])][1] += a[1]
                                else:
                                    nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])][int(np1[4])] += a[1]
                            except:
                                nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])][0] += a[1]
                        else:
                            nc[int(np1[0])][int(np1[1])][int(np1[2])][int(np1[3])] += a[1]
                    else:
                        nc[int(np1[0])][int(np1[1])][int(np1[2])] += a[1]
                else:
                    nc[int(np1[0])][int(np1[1])] += a[1]
            else:
                nc[int(np1[0])] += a[1]
    return nc

def split(n):
    try:
        nc = n.copy()
        a = split(nc[0])
        if a != nc[0]:
            return [a,nc[1]]
        else:
            return [nc[0],split(nc[1])]
    except AttributeError:
        if n>=10:
            return [math.floor(n/2.0),math.ceil(n/2.0)]
        else:
            return n

def reduce(n):
    c = 0
    while c==0:
        a = n.copy()
        for i in range(10):
            n = explode(n)
        if a == n:
            n = split(n)
        if a == n:
            c+=1
    return n

def add(a,b):
    c = [a,b]
    for i in range(30):
        c = reduce(c)
    print(c)
    return c


def magnitude(n):
    if type(n)==int:
        return n
    return magnitude(n[0])*3 + magnitude(n[1])*2





ov = data[0]

for i in range(len(data)-1):
    ov = add(ov,data[i+1])


print(magnitude(ov))
