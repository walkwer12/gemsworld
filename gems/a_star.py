




































































import heapq
def astar(s,goal):
    q=[(h[s],0,s,[s])]
    while q:
        f,c,n,p=heapq.heappop(q)
        if n==goal: return p,c
        for x,w in g.get(n,[]): heapq.heappush(q,(c+w+h[x],c+w,x,p+[x]))
g={'A':[('B',2),('E',3)],
   'B':[('C',1),('G',9)],
   'E':[('D',6)],
   'D':[('G',1)]}
h={'A':11,'B':6,'C':99,'D':1,'E':7,'G':0}
p,c=astar('A','G')
print("Shortest path:",p)
print("Total cost:",c)
