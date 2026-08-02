class Solution:
    def dfs(self, adj):
        # code here
        
        
        nodes = len(adj)
        visited = [0]*nodes
        
        ans = [0]
        visited[0] = 1
        
        def dfs_recursion(node):
            for neighbour in adj[node]:
                if visited[neighbour] == 0:
                    visited[neighbour] = 1
                    ans.append(neighbour)
                    dfs_recursion(neighbour)
        dfs_recursion(0)
        for i in range(nodes):
            if visited[i] == 0:
                visited[i] = 1
                ans.append(i)
                dfs_recursion(i)
        return ans