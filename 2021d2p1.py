import sys

data = open(sys.argv[-1],"r").read().split('\n')


hp = 0

vp = 0
aim = 0

for i in data:
    if i[0]=="f":
        hp+=int(i[-1])
    elif i[0] == "d":
        vp += int(i[-1])
    elif i[0]=="u":
        vp-=int(i[-1])
    print(i)



print(hp*vp)
