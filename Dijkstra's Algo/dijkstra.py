import heapq

def dijkstra(src,edges):
    pq = []
    V = len(edges)
    distances = [float('inf')]*V
    distances[src] = 0
    heapq.heappush(pq, (0,src))

    while pq:
        d, u = heapq.heappop(pq)
        if d > distances[u]:
            continue
        for v, w in edges[u]:
            if distances[u]+w < distances[v]:
                distances[v] = distances[u]+w
                heapq.heappush(pq, (distances[v], v))
    return distances


adj_list = [[(1,4), (2,8)], [(0,4),(4,6)],[(0,8),(3,2)],[(2,2),(4,10)],[(1,6),(3,10)]]
start = 0

print(dijkstra(start,adj_list))