from collections import deque
import math 

class Solution:
    def shortestPath(self, V, edges, src):
        # code here
        
        def bfs(queue, distance, visited):
            while queue:
                temp = queue.popleft()
                curr_dist = temp[-1]
                curr_node = temp[0]
                for node in lists[curr_node]:
                    if visited[node] == 0:
                        queue.append([node,curr_dist+1])
                        distance[node] = min(distance[node],curr_dist+1)
                        visited[node] = 1
        
        # adjacency list graph make Complete
        lists = [[] for i in range(V)]
        for u,v in edges:
            lists[u].append(v)
            lists[v].append(u)
        
        # Using BFS traverse and make it
        inf = math.inf
        distance = [inf]*(V)
        queue = deque([])
        queue.append([src,0])
        distance[src] = 0
        visited = [0]*(V)
        visited[src] = 1
        
        bfs(queue, distance, visited)
        return [-1 if d == inf else d for d in distance]
        
        
