from collections import deque
# bfs method
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n

        def bfs(node,curr_color):
            color[node] = curr_color
            
            q = deque([])
            q.append([node,curr_color])
            while q:
                temp,c_color = q.popleft()
                next_color = 1 - c_color
                for neighbour in graph[temp]:
                    if color[neighbour] == c_color:
                        return False
                    elif color[neighbour] == -1:
                        color[neighbour] = next_color
                        q.append([neighbour,next_color])
            return True
                        

        for i in range(n):
            if color[i] == -1:
                curr_color = 0
                t = bfs(i,curr_color)
                if t == False:
                    return False
        return True
# dfs method
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        '''
        bipartite --> Dividing or Grouping into 2 parts
        '''
        
        '''
        DFS : 
        '''
        color = [-1]*n # -1 for no color, 1 for red, 0 for green
        def dfs(node,curr_color):
            color[node] = curr_color
            next_color = 1 - curr_color
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    t = dfs(neighbour,next_color)
                    if t == False:
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True
        for i in range(n):
            if color[i] == -1:
                curr_color = 0
                t = dfs(i,curr_color)
                if t == False:
                    return False
        return True

        """