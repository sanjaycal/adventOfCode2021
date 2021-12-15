from os import read
import sys
from queue import PriorityQueue

data = open(sys.argv[-1],"r").read().split('\n')

#data = ['1']



a = []
for i in data:
    b = []
    for j in i:
        b.append(int(j))
    a.append(b)


data = []
for i in range(len(a)):
    data.append([])
data = data.copy()

for k in range(5):
    for i in range(len(a)):
        data[i] = data[i]+a[i]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j]+=1
print("ready")
a = data.copy()
data = []
for k in range(5):
    for i in a:
        data.append(i.copy())
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j]+=1


a = data.copy()
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j] = a[i][j]%9
        if a[i][j] == 0:
            a[i][j] = 9

data = a.copy()

print("ready")

class Graph:
    def __init__(self, nv):
        self.v = nv
        self.edges = [[-1 for i in range(nv)] for j in range(nv)]
        self.visited = []
    def add_edge(self,u,v,weight):
        self.edges[u][v] = weight
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    c = 0
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)
        c+=1
        print(c)
        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


g = Graph(len(data)*len(data[0]))



for x in range(len(data)):
    for y in range(len(data[0])):
        n = []
        if x!=0:
            n.append([(x-1)*len(data)+y,data[x-1][y]])
        if x!=len(data)-1:
            n.append([(x+1)*len(data)+y,data[x+1][y]])
        if y!=0:
            n.append([(x)*len(data)+y-1,data[x][y-1]])
        if y!=len(data[0])-1:
            n.append([(x)*len(data)+y+1,data[x][y+1]])
        for edge in n:
            g.add_edge(x*len(data)+y,edge[0],edge[1])


D = dijkstra(g,0)
print(D[len(data)*len(data[0])-1])

