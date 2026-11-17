








































































def ford_fulkerson(graph, source, sink):
    n = len(graph)
    flow = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        queue = [source]
        for u in queue:
            for v in range(n):
                if parent[v] == -1 and graph[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        if parent[sink] == -1:
            break
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        flow += path_flow
    return flow
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
print("Maximum Flow:", ford_fulkerson(graph, 0, 5))
