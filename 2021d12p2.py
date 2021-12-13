import sys

data = open(sys.argv[-1],"r").read().split('\n')
sys.setrecursionlimit(30000)




nodes = {}
for line in data:
    a,b = line.strip().split('-')
    try:
        nodes[a].append(b)
    except KeyError:
        nodes[a] = [b]
    try:
        nodes[b].append(a)
    except KeyError:
        nodes[b] = [a]

def getp(nodes, start, end, cp=None, ud=False):
    if cp is None:
        cp = set()

    if start==end:
        return 1

    np = 0
    for a in nodes[start]:
        nud = ud
        if a.upper()!=a and a in cp:
            if ud or a in ['start','end']:
                continue
            else:
                nud = True

        np += getp(nodes, a, end, cp | {start}, nud)

    return np

print(getp(nodes, 'start', 'end'))