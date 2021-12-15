import sys
from queue import PriorityQueue

data = open(sys.argv[-1],"r").read().split('\n')


class node:
    def __init__(self,value,id):
        self.value = value
        self.id = id
    def setNeighbors(self,neighbors):
        self.neighbors = neighbors



a = []
c = 0
for i in data:
    b = []
    for j in i:
        b.append(node(int(j),c))
        c+=1
    a.append(b)



data = a

for x in range(len(data)):
    for y in range(len(data)):
        n = []
        if x!=0:
            n.append(data[x-1][y])
        if x!=len(data)-1:
            n.append(data[x+1][y])
        if y!=0:
            n.append(data[x][y-1])
        if y!=len(data[0])-1:
            n.append(data[x][y+1])
        data[x][y].setNeighbors(n)


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

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

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

for i in range(len(data)):
    for j in range(len(data[0])):
        for edge in data[i][j].neighbors:
            g.add_edge(data[i][j].id,edge.id,edge.value)


D = dijkstra(g,0)
print(D[c-1])

