







































































edges = [
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 2),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 5)
]

V = 4

selected = [False] * V
selected[0] = True

cost = 0

print("Edges in MST: ")

for i in range(V-1):
    minimum = float('inf')

    for u, v, w in edges:
        if selected[u] and not selected[v]:
            if w < minimum:
                minimum = w
                a, b = u, v

#because it is an undirected graph. If it was a directed graph then this would not come. 
        elif selected[v] and not selected[u]:
            if w < minimum:
                minimum = w
                a, b = v, u

    print(f"{a} - {b}: {minimum}")

    cost += minimum
    selected[b] = True

print("Minimum Cost: ", cost)
