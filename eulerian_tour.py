# Finds Eulerian Tour
from collections import defaultdict

def get_degrees(graph):
    degrees = {}
    for (x,y) in graph:
        if x not in degrees: degrees[x] = 0
        if y not in degrees: degrees[y] = 0
        degrees[x]=degrees[x]+1 
        degrees[y]=degrees[y]+1
    print(degrees)
    return degrees
    
def get_adj(graph):
    adj = defaultdict(list)
    for x in graph:
        adj[x[0]].append(x[1])
        adj[x[1]].append(x[0])
    return adj
    
def unused_edges(graph):
    edges =[]
    for x in graph:
        edges.append(x)
    return edges
    
def min_nodes(adj,degrees):
    min = 1000
    node = adj[0]
    for x in adj:
        if degrees[x] < min: 
            min = degrees[x]
            node = x
    return node
    
def find_eulerian_tour(graph):
    # your code here
    tour = []
    degrees = get_degrees(graph)
    adj = get_adj(graph)
    unused = unused_edges(graph)

    tour.append(graph[0][0])
    
    while len(adj[tour[0]]) > 0:
        x = min_nodes(adj[tour[len(tour)-1]],degrees)
        print("{} to {}".format(tour[len(tour)-1], x))
        tour.append(x)
        print("Adding {}".format(x))
        adj[tour[len(tour)-2]].remove(x)
        adj[x].remove(tour[len(tour)-2])
        adj_list(adj)
        print(tour)
    return tour
    
def adj_list(adj):
    for v in adj:
        print("{}: {}".format(v,adj[v]))
    
def test():
    input = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    print (find_eulerian_tour(input))
test()

