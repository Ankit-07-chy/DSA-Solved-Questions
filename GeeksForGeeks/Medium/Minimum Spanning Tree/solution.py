class Solution:
    def spanningTree(self, V, edges):
        
        # sort the edges based on wts in asc order
        edges.sort(key=lambda x:x[-1])
        class DisJointSet:
            def __init__(self,n):
                self.n = n
                self.parent = list(range(n+1))
                self.rank = [0]*(n+1)
            def find(self,x):
                if x == self.parent[x]:
                    return x 
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return 
                if self.rank[px]>self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px]<self.rank[py]:
                    self.parent[px] = py
                else:
                    self.parent[px] = py 
                    self.rank[py] += 1
        wts_sum = 0
        dsu = DisJointSet(V)
        for u,v,w in edges:
            if dsu.find(u) == dsu.find(v):
                continue
            wts_sum += w 
            dsu.union(u,v)
        return wts_sum




'''

# this is using Prim's algorithm
import heapq

class Solution:
    def spanningTree(self, V, edges):

        adjList = [[] for _ in range(V)]

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        visited = [0] * V
        min_heap = [(0, 0, -1)]

        edge_wt_sum = 0

        while min_heap:

            wt, node, parent = heapq.heappop(min_heap)

            if visited[node]:
                continue

            visited[node] = 1
            edge_wt_sum += wt

            for neig, edgeWt in adjList[node]:
                if not visited[neig]:
                    heapq.heappush(
                        min_heap,
                        (edgeWt, neig, node)
                    )

        return edge_wt_sum'''