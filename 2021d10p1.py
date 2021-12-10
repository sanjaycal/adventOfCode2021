import sys


data = open(sys.argv[-1],"r").read().split('\n')

pl = ""

sc = 0

for line in data:
    ec = []
    closers = [")",']','}','>']
    openers = ["(",'[','{','<']
    for i in range(len(line)):
        if line[i] in openers:
            ec.append(closers[openers.index(line[i])])
        elif line[i] == ec[-1]:
            ec.pop(-1)
        else:
            if line!=pl:
                if line[i]==")":
                    sc+=3
                if line[i]=="]":
                    sc+=57
                if line[i]=="}":
                    sc+=1197
                if line[i]==">":
                    sc+=25137
                pl = line

print(sc)
