import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        # Create adjacency list
        adj = [[] for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))

        # Min heap: (stops, node, cost)
        q = []
        heapq.heappush(q, (0, src, 0))

        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = heapq.heappop(q)

            # If stops exceed k, skip
            if stops > k:
                continue

            for adjNode, edgeCost in adj[node]:

                if cost + edgeCost < dist[adjNode] and stops <= k:
                    dist[adjNode] = cost + edgeCost

                    heapq.heappush(
                        q,
                        (stops + 1, adjNode, cost + edgeCost)
                    )

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]