# Implementation

# Simple One
# Using Adjacency List

nodes = ['a', 'b', 'c', 'd']
edges = [('a', 'b'), ('a', 'd'),('d', 'b'), ('c', 'd')]

# Output:
# [[1, 3], [0, 3], [3], [0, 1, 2]]

"""
so, we are mapping nodes to their indexes here
a -> 0
b -> 1
c -> 2
d -> 3
"""
def graph_list(nodes:list, edges:list)->list:
    # Graph
    nodemap = {} # mapping nodes: names as keys and indexes as values

    n=len(nodes)
    for i in range(n):
        nodemap[nodes[i]]=i

    graph = [[] for i in range(n)]


    for e in edges:
        u = nodemap[e[0]]
        v = nodemap[e[1]]
        graph[u].append(v)
        graph[v].append(u)

    return(graph) 

print(graph_list(nodes, edges))


# -----------------------------------------------------------------------------------------------

# weighted

# nodes = ['a', 'b', 'c', 'd']
# edges = [('a', 'b', 2), ('a', 'd', 4),('d', 'b', 1), ('c', 'd', 3)]

# [[(1,2), (3,4)], [(0,2),(3, 1)], [(3, 3)], [(0, 4), (1, 1), (2, 3)]]

def graph_list_weighted(nodes:list, edges:list)->list:
    # Graph
    nodemap = {} # mapping nodes: names as keys and indexes as values

    n=len(nodes)
    for i in range(n):
        nodemap[nodes[i]]=i

    graph = [[] for i in range(n)]


    for e in edges:
        u = nodemap[e[0]]
        v = nodemap[e[1]]
        weight = e[2]
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    return graph

# print(graph_list_weighted(nodes, edges))

# -------------------------------------------------------------------------------------------------------------

# Use case: Social Networks

# nodes = ['Shreya', 'Harshita', 'Medhavi', 'Gunisha', 'Kavyashree', 'Hitesh Sir', 'Ankush Sir']

# edges = [('Shreya', 'Harshita'), ('Shreya', 'Medhavi'), ('Shreya', 'Gunisha'), ('Shreya', 'Kavyashree'), ('Shreya', 'Hitesh Sir'), ('Hitesh Sir', 'Ankush Sir'), ('Ankush Sir', 'Kavyashree'), ('Medhavi', 'Gunisha'), ('Medhavi', 'Harshita')]

# Output:
# [[1, 2, 3, 4, 5], [0, 2], [0, 3, 1], [0, 2], [0, 6], [0, 6], [5, 4]]

# print(graph_list(nodes, edges)) 

# -------------------------------------------------------------------------------------------------------------


# Using Adjacency Matrix

# nodes = ['a', 'b', 'c', 'd']
# edges = [('a', 'b'), ('a', 'd'),('d', 'b'), ('c', 'd')]

"""
mapping part would be common
"""

def graph_matrix(nodes:list,edges:list)->list:
    nodemap = {} # mapping nodes: names as keys and indexes as values

    n=len(nodes)
    for i in range(n):
        nodemap[nodes[i]]=i

    graph = [[0 for i in range(n)] for i in range(n)]

    for e in edges:
        u = nodemap[e[0]]
        v = nodemap[e[1]]
        graph[u][v] = 1
        graph[v][u] = 1
    
    return graph

print(graph_matrix(nodes, edges))

# [[0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 0]]

# ------------------------------------------------------------------------------------------------

# weighted

# nodes = ['a', 'b', 'c', 'd']
# edges = [('a', 'b', 2), ('a', 'd', 4),('d', 'b', 1), ('c', 'd', 3)]

# # [[0, 2, 0, 4], [2, 0, 0, 1], [0, 0, 0, 3], [4, 1, 3, 0]]

def graph_matrix_weighted(nodes:list,edges:list)->list:
    nodemap = {} # mapping nodes: names as keys and indexes as values

    n=len(nodes)
    for i in range(n):
        nodemap[nodes[i]]=i

    graph = [[0 for i in range(n)] for i in range(n)]

    for e in edges:
        u = nodemap[e[0]]
        v = nodemap[e[1]]
        graph[u][v] = e[2]
        graph[v][u] = e[2]
    
    return graph



# print(graph_matrix_weighted(nodes, edges))