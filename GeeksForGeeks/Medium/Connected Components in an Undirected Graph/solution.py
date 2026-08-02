from collections import deque
class Solution:
    def getComponents(self, V, edges):
        # code here
        
        # bfs would be one way I am currently thinking
        adjList = [[] for i in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            
        # using BFS I am doing at this moment 
        # q = deque([])
        
        def bfs(node,arr):
            q = deque([])
            q.append(node)
            
            while q:
                temp = q.popleft()
                for neighbour in adjList[temp]:
                    if visited[neighbour] == False:
                        arr.append(neighbour)
                        visited[neighbour] = True
                        q.append(neighbour)
        
        result = []
        visited = [False]*(V)
        for i in range(V):
            if visited[i] == False:
                visited[i] = True
                arr = [i]
                bfs(i,arr)
                result.append(arr)
                
        return result
                
                
    
        
        
        
        '''
class Solution:
    def getComponents(self, V, edges):
        # code here
        # Make Graph form V and edges
        lists = [[] for i in range(V)]
        for u,v in edges:
            # u,v = edges[i]
            lists[u].append(v)
            lists[v].append(u)
            
        
        result = []
        def traversal(node,arr):
            connected =  lists[node]
            for u in connected:
                if visited[u] == False:
                    visited[u] = True
                    arr.append(u)
                    traversal(u,arr)
            
        visited = [False]*V
        for i in range(V):
            if visited[i] == False:
                visited[i] = True
                temp = [i]
                traversal(i,temp)
                result.append(temp)
        return result
                    
        
        '''