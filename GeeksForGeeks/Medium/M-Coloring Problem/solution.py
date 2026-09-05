class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        graph = [[] for _ in range(v)]
        for u,p in edges:
            graph[u].append(p)
            graph[p].append(u)
            
        color = [0]*v
        
        def isColor(node,c):
            for adjN in graph[node]:
                if color[adjN] == c:
                    return False
            return True
        
        def fxn(node):
            
            if node == v:
                return True
            
            for i in range(1,m+1):
                if isColor(node,i):
                    color[node] = i
                    if fxn(node+1):
                        return True
                    
                    color[node] = 0
            return False
        return fxn(0)
            