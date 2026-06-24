
import math
class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        # inf = math.inf
        dist = [10**8]*V
        
        dist[src] = 0
        for i in range(V-1):
            for u,v,w in edges:
                if dist[u] != 10**8 and dist[u]+w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Check for negative cycle
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[u] + w < dist[v]:
                return [-1]

        return dist