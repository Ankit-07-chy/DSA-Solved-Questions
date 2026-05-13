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