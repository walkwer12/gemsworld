


































































def bellman_ford(V, edges, src):

    INF = float('inf')
    d = [INF] * V #set all distances to infinity

    d[src] = 0

    for _ in range(V-1):
        for u, v, w in edges:
            if d[u] != INF:
                d[v] = min(d[v], d[u] + w)

    #now checking for negative weight cycle

    for u, v, w in edges:
        if d[u] != INF and d[u] + w < d[v]:
            print("Negative weight cycle exists")
            return

    print("No negative weight cycles")
    print("Distances: ", d)

edges = [
    (0, 1, 5),
    (0, 2, 10),
    (0, 3, 8),
    (1, 3, 4),
    (2, 3, 1)
]

bellman_ford(5, edges, 0)