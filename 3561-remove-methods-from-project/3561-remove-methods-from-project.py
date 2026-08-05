class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        queue = collections.deque([k])
        suspicious = bytearray(n)
        suspicious[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1

                if suspicious[v] == 0:
                    queue.append(v)
                    suspicious[v] = 1

        can_remove_all = True
        for i in range(n):
            if suspicious[i] == 1 and in_degree[i] > 0:
                can_remove_all = False
                break

        if not can_remove_all:
            return list(range(n))

        return [i for i in range(n) if suspicious[i] == 0]


'''from collections import deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # make graph
        adjList = [[] for i in range(n)]
        for a,b in invocations:
            adjList[a].append(b)
        # print(adjList)
        seen = set()
        seen.add(k)

        queue = deque([])
        queue.append(k)
        remove = False
        visited = [False]*n
        visited[k] = True
        while queue:
            temp = queue.popleft()
            for invoke_node in adjList[temp]:
                if invoke_node in seen:
                    remove = True
                
                seen.add(invoke_node)
                if visited[invoke_node]==False:
                    queue.append(invoke_node)
                    visited[invoke_node]=True
        result = []
        if remove :
            for i in range(n):
                if i not in seen:
                    result.append(i)
        else:
            for i in range(n):
                result.append(i)
        return result'''