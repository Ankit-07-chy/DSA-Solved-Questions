class Solution:
    def articulationPoints(self, V: int, edges: list[list[int]]) -> list[int]:
        # code here
        
        # graph make
        adjList = [[] for i in range(V)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        result = set()
        low_time = [0]*V
        discovery_time = [0]*V
        time = 0
        visited = [False]*V
        
        def dfs(u,parent):
            nonlocal time
            time += 1
            children = 0
            visited[u] = True
            discovery_time[u] = time
            low_time[u] = time
            
            for v in adjList[u]:
                if visited[v] == False:
                    dfs(v,u)
                    children += 1
                    low_time[u] = min(low_time[u],low_time[v])
                    
                    if parent != -1 and low_time[v] >= discovery_time[u]:
                        
                        result.add(u)
                elif visited[v] == True:
                    low_time[u] = min(low_time[u],discovery_time[v])
            if parent == -1 and children>1:
                result.add(u)
        for i in range(V):
            if visited[i] == False:
                dfs(i,-1)
                
        return list(result) if result else [-1]
        