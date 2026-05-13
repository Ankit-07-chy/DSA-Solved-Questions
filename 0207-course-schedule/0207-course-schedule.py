from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using Khan's algo
        '''
        indegree, queue, put in queue whose indegree is zero, deque form queue, and then decrease indegree due to this, if indegree goes to be zero then push it to topo --> for cycle check if len(topo) == V -> no cycle else cycle
        '''
        n = numCourses
        graph = [[]for i in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
        
        indegree = [0]*n
        visited = [0]*n
        for i in range(n):
            for node in graph[i]:
                indegree[node] += 1
        q = deque([])
        for u,v in enumerate(indegree):
            if v == 0:
                q.append(u)
        topo = []
        def bfs(node):
            visited[node] = 1
            while q:
                temp = q.popleft()
                topo.append(temp)
                for p in graph[temp]:
                    indegree[p] -= 1
                    if indegree[p] == 0:
                        q.append(p)
        for i in range(n):
            if visited[i] == 0:
                bfs(i)  
        if len(topo) == n:
            return True
        else:
            return False    


"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        lists = [[] for i in range(n)]
        for u,v in prerequisites:
            lists[v].append(u)
        
        visited = [0]*n
        recursion_stack = [0]*n

        def dfs(node,visited,recursion_stack,lists):
            visited[node] = 1
            recursion_stack[node] = 1
            for neighbour in lists[node]:
                if visited[neighbour] == 1 and recursion_stack[neighbour] == 1:
                    return True
                if visited[neighbour] == 0:
                    if dfs(neighbour,visited,recursion_stack,lists):
                        return True
            recursion_stack[node] = 0
            return False


        for i in range(n):
            if visited[i] == 0:
                t = dfs(i,visited,recursion_stack,lists) # to detect cycle, if cycle detected means not able to complete the courses
                if t :
                    return False
        return True
        """