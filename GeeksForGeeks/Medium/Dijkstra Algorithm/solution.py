import math
import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        adjList = [[] for i in range(V)]
        for u, v, w in edges:
            adjList[u].append((v, w))  # Tuple instead of list
            adjList[v].append((u, w))  # Tuple instead of list
            
        distance = [math.inf] * V
        heap = []
        
        distance[src] = 0
        heapq.heappush(heap, (0, src))  # Tuple instead of list
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            if dist > distance[node]:
                continue
            
            for neighbour_node, wts in adjList[node]:
                if dist + wts < distance[neighbour_node]:
                    distance[neighbour_node] = dist + wts
                    heapq.heappush(heap, (distance[neighbour_node], neighbour_node))
        
        return distance