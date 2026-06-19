#User function Template for python3

from typing import List

import math
class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
                         
        # Make graph complete
        lists= [[] for i in range(V)]
        for u,v,w in edges:
            lists[u].append([v,w])
        
        inf = math.inf
        
        # topo sort
        # for topo sort using DFS for now
        def dfs(node):
            visited[node] = 1
            for neighbour in lists[node]:
                if visited[neighbour[0]] == 0:
                    dfs(neighbour[0])
            stack.append(node)
        
        stack = []; visited = [0]*V
        for i in range(V):
            if visited[i] == 0:
                dfs(i)
                
        # topological sorting done
        
        # step 2 . take the node out of stack & relaxed the edges.
        distance = [inf]*V
        distance[0] = 0
        while stack:
            node = stack.pop()
            for neighbour in lists[node]:
                if distance[node] + neighbour[-1] < distance[neighbour[0]]:
                    distance[neighbour[0]] = distance[node] + neighbour[-1]
        
        return [-1 if d == inf else d for d in distance]
        
        return distance
        
