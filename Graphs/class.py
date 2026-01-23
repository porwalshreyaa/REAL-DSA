class MatGraph:
    def __init__(self, nodes, edges):
        self.graph = [[0 for i in nodes]for i in nodes]
        for (u,v) in edges:
            self.graph[u][v]=1
            self.graph[v][u]=1 # in case of undirected graphs
    def print_graph(self):
        for i in self.graph:
            print(i)

nodes=["ram", "jay", "prasad", "shyam", "madhur"]
edges=[(1,4), (0,3), (2,1),(4,3)]

graph = MatGraph(nodes, edges)
graph.print_graph()