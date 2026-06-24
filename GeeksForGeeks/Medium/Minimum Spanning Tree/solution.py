import heapq

class Solution:
    def spanningTree(self, V, edges):

        adjList = [[] for _ in range(V)]

        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        visited = [0] * V
        min_heap = [(0, 0, -1)]

        edge_wt_sum = 0

        while min_heap:

            wt, node, parent = heapq.heappop(min_heap)

            if visited[node]:
                continue

            visited[node] = 1
            edge_wt_sum += wt

            for neig, edgeWt in adjList[node]:
                if not visited[neig]:
                    heapq.heappush(
                        min_heap,
                        (edgeWt, neig, node)
                    )

        return edge_wt_sum