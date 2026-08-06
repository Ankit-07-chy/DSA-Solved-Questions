class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjList = [[] for i in range(n)]
        for a,b in connections:
            adjList[a].append(b)
            adjList[b].append(a)

        # tarjan's algo is for this
        bridge = []

        low_time = [inf]*n
        discovery_time = [0]*n
        time = 0

        visited =[False]*n

        def dfs(u,parent_u):
            nonlocal time
            visited[u] = True
            time += 1
            discovery_time[u] = time
            low_time[u] = time

            for neighbour in adjList[u]:
                if visited[neighbour]==False:
                    dfs(neighbour,u)
                    low_time[u] = min(low_time[u],low_time[neighbour])
                    if low_time[neighbour] > discovery_time[u]:
                        bridge.append([u,neighbour])
                    
                elif parent_u != neighbour:
                    low_time[u] = min(low_time[u],discovery_time[neighbour])

        for i in range(n):
            if visited[i] == False:
                dfs(i,-1)

        return bridge