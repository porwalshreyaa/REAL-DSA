adj_list = [[[1,4], [2,8]], [[0,4], [4,6], [2,3]], [[0,8], [3,2], [1,3]], [[2,2], [4,10]], [[1,6], [3,10]]]

# Very Basic - Brute Force
def dijkstra(src, graph):
    result = []
    V = len(graph)
    for v in range(V):
        result.append(float('inf'))
    for v in range(V):
        if v == src:
            result[v]=0
        for [edge, cost] in graph[v]:
            if cost + result[v]<result[edge]:
                result[edge]=cost+result[v]
    return result

print(dijkstra(0,adj_list))

