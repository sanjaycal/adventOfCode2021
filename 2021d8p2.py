import sys


data = open(sys.argv[-1],"r").read().split('\n')

a = []

for i in data:
    a.append(i.split("|"))


data = a

c = ""
n = 0


def getpos(config):
    data = config.split(" ")
    out = ["","","","","","","","","",""]
    for i in data:
        if len(i)==2:
            out[1] = i
        if len(i) == 4:
            out[4] = i
        if len(i) == 3:
            out[7] = i
        if len(i) == 7:
            out[8] = i
    for i in data:
        if len(i)==5:
            if out[1][0] in i and out[1][1] in i:
                out[3] = i
    for i in data:
        if len(i) == 6:
            c = 0
            for j in out[3]:
                if j in i:
                    c+=1
            if c==5:
                out[9] = i
            else:
                if out[1][0] in i and out[1][1] in i:
                    out[0] = i
    for i in data:
        if len(i)==6 and i!=out[0] and i!= out[9]:
            out[6] = i
    for i in data:
        c = 0
        if len(i) == 5:
            for j in i:
                if j in out[6]:
                    c+=1
            if c==5:
                out[5] = i
            elif i!=out[3]:
                out[2] = i
    return out
        

ot = 0

for i in data:
    cfg = getpos(i[0])
    print(cfg)
    for j in i[1].split(" "):
        if j!="":
            pp = 0
            ccl = [0,0,0,0,0,0,0,0,0,0]
            for k in j:
                for l in range(len(cfg)):
                    if k in cfg[l]:
                        ccl[l]+=1
            for i in range(len(ccl)):
                if ccl[i]== max(ccl) and len(cfg[i])==len(j):
                    n = i
            print(n)
            c+=str(n)
    ot += int(c)
    c = ""
            


print(ot)