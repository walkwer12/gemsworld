














































































#first establish edges

edges = [
    (0, 1, 5), 
    (0, 2, 4), 
    (0, 3, 7),
    (1, 3, 20),
    (2, 3, 6)
]

#sort edges based on weight
edges.sort(key=lambda x: x[2])

parent = [0, 1, 2, 3]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

cost = 0

print("Edges in MST: ")

for u, v, w in edges:
    a, b = find(u), find(v)
    if a != b:
        parent[a] = b
        print(f"{u} - {v} : {w}")
        cost += w

print("Minimum cost: ", cost)

