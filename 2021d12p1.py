import sys


data = open(sys.argv[-1],"r").read().split('\n')
sys.setrecursionlimit(3000000)

class node:
    def __init__(self,name):
        self.cn = []
        self.name = name
    def addcn(self,node):
        self.cn.append(node)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

nodes ={}

for path in data:
    a = path.split("-")
    if not(a[0] in nodes):
        nodes[a[0]] = node(a[0])
    if not(a[1] in nodes):
        nodes[a[1]] = node(a[1])
    nodes[a[0]].addcn(nodes[a[1]])
    nodes[a[1]].addcn(nodes[a[0]])

pp = 0

def getp(node,ai):
    global pp
    a = node.cn.copy()
    c = 0
    for i in range(len(a)):
        if a[i-c] in ai and a[i-c].name.upper() != a[i-c].name and a[i-c].name != 'end':
            a.pop(i-c)
            c+=1
    aj = ai.copy()
    aj.append(node)
    
    ap = {}
    for j in range(len(a)):
        i = a[j]
        if i.name == "end":
            ap[i.name] = "end"
            pp+=1
        else:
            b = getp(i,aj)
            if b!={}:
                ap[i.name] = b
    return ap




a = getp(nodes["start"],[])


print(pp)
