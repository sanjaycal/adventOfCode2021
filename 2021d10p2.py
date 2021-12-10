import sys


data = open(sys.argv[-1],"r").read().split('\n')

pl = ""

def calculateScore(e):
    sc = 0
    sta = {")":1,"]":2,"}":3,">":4}
    for i in range(len(e)):
        sc = sc*5
        sc += sta[e[0-i-1]]
    return sc


sc = 0
gsc = []
for line in data:
    ec = []
    closers = [")",']','}','>']
    bl = False
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
            bl = True
    if not bl and len(ec)!=0:
        gsc.append(calculateScore(ec))
    
        

print(sorted(gsc)[int(len(gsc)/2)])
