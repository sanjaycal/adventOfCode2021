import sys

data = open(sys.argv[-1],"r").read().split('\n')


hp = 0

vp = 0
aim = 0

for i in data:
    if i[0]=="f":
        hp+=int(i[-1])
        vp += aim*int(i[-1])
    elif i[0] == "d":
        aim +=int(i[-1])
    elif i[0]=="u":
        aim -=int(i[-1])
    print(i)
    print(aim)
    print(hp)
    print(vp)



print(hp*vp)
