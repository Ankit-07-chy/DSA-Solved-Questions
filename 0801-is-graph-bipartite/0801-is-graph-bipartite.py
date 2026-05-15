from collections import deque
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