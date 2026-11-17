














































































#define graph
graph = {
    'A' : {'B' : 4, 'C': 2},
    'B' : {'A' : 4, 'C' : 1, 'D' : 5},
    'C' : {'A': 1, 'B' : 1, 'D' : 8},
    'D' : {'B': 5, 'C' : 8}
}

#set all initial dist to infinity
dist = {n : float('inf') for n in graph}
visited = [] #create list for visited vertx

dist['A'] = 0 #set initial vertex to 0

for i in graph:
    #checks to see if vertex has been visited
    u = min((n for n in graph if n not in visited), key=lambda n:dist[n])

#n for n in graph if n not in visited - Go through all vertices and select only those that have not been visited.
#key=lambda n: dist[n] - compare the vertices using their distances.

    visited.append(u)

    for v, w in graph[u].items():
        dist[v] = min(dist[v], dist[u] + w) # main formula

print(dist)
    

