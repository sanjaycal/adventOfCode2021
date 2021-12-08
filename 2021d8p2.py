import sys


data = open(sys.argv[-1],"r").read().split('\n')

a = []

for i in data:
    a.append(i.split("|"))


data = a

c = 0
n = 0
for i in data:
    for j in i[1].split(" "):
        if len(j) == 2:
            n = 1
        if len(j) == 4:
            n = 4
        if len(j) == 3:
            n = 7
        if len(j) == 7:
            n = 8
        c+=n
            


print(c)