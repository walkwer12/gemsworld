









































































INF = float('inf')
n = 3
graph = []

print("Enter the weight matrix (use 0 for no edge between different nodes):")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Replace "no edge" (0 between different nodes) with infinity
for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == 0:
            graph[i][j] = INF

# Floyd-Warshall
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print("\nShortest Distance Matrix:")
for row in graph:
    print(*row)
