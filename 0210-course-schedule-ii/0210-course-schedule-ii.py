from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # in this I have to give topological sort order

        '''
        I am doing this using Khan's Algo 1st
        '''
        n = numCourses
        graph = [[] for i in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
        indegree = [0]*n
        for i in range(n):
            for node in graph[i]:
                indegree[node]+=1
        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        visited = [0]*n
        topo = []

        def bfs(node):
            visited[node] = 1
            while q:
                temp = q.popleft()
                topo.append(temp)
                for t in graph[temp]:
                    indegree[t]-=1
                    if indegree[t] == 0:
                        q.append(t)
        for i in range(n):
            if visited[i] == 0:
                bfs(i)
        return topo if len(topo) == n else []