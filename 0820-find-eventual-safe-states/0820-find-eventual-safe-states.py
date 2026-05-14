from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        reverse the graph nodes, do topo and return that
        """
        n = len(graph)
        graph1 = [[]for i in range(n)]
        for i in range(n):
            for node in graph[i]:
                graph1[node].append(i)
        # print(graph)
        # print(graph1)
        topo = []
        indegree = [0]*n
        for i in range(n):
            for node in graph1[i]:
                indegree[node] += 1
        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        def toposort(topo,q,graph1,n):
            while q:
                temp = q.popleft()
                topo.append(temp)
                for node in graph1[temp]:
                    indegree[node] -=1
                    if indegree[node] == 0:
                        q.append(node)
        
        toposort(topo,q,graph1,n)
        return sorted(topo)
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [None]*n
        visited = [0]*n
        recursion_stack = [0]*n

        def checkCycle(node):
            
            if safe[node] is not None:
                return safe[node]
            visited[node] = 1
            recursion_stack[node] = 1
            for neighbour in graph[node]:
                if recursion_stack[neighbour] == 1 :
                    safe[node] = False
                    #recursion_stack[node] = 0
                    return False # cycle detecte not safe
                if visited[neighbour] == 0:
                    t = checkCycle(neighbour)
                    if not t:
                        safe[node] = False
                        # recursion_stack[node] = 0
                        return False
            safe[node] = True
            recursion_stack[node] = 0
            return True


        for i in range(n):
            if safe[i] == None:
                checkCycle(i)
        return [x for x in range(n) if safe[x]]
        '''
# this solution is working but give TLE, for that I have to memoize that
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # terminal node -> no outgoing edges;
        # safe node -> if every path from that node terminating to terminal node
        safe = [True]*n # sorted manner

        def checkCycle(node,visited,recursion_stack):
            # from dfs detect cycle
            visited[node] = 1
            recursion_stack[node] = 1
            for neighbour in graph[node]:
                if visited[neighbour] == 1 and recursion_stack[neighbour] == 1:
                    return True
                if visited[neighbour] ==0:
                    t = checkCycle(neighbour,visited,recursion_stack)
                    if t:
                        return True
            recursion_stack[node] = 0
            return False

        # answer contains all terminal node + the nodes whose paths 
        for i in range(n):
            visited = [0]*n
            recursion_stack = [0]*n
            # find every possible path, and if any one found to be terminate at non terminal then assign false to then
            t = checkCycle(i,visited,recursion_stack) # return true, if cycle(means not terminates at terminal) else return False
            if t:
                safe[i] = False
        
        return [x for x,v in enumerate(safe) if v == True]

        """