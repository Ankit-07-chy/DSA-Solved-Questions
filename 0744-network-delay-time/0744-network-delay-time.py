import heapq
import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        inf = math.inf
        # graph using adjList
        # n = len(times)
        adjList = [[] for i in range(n+1)]
        for u,v,w in times:
            adjList[u].append([v,w])
        
        # return the minimum time to takes all the n nodes to receive the signal
        src_node = k
        # dijkastra apply as it is given weight
        min_heap = []
        distance =[inf]*(n+1)
        heapq.heappush(min_heap,[0,src_node])
        distance[src_node] = 0

        while min_heap:
            dist, node = heapq.heappop(min_heap)
            for neighbour,wt in adjList[node]:
                if dist + wt < distance[neighbour]:
                    distance[neighbour] = dist+wt
                    heapq.heappush(min_heap,[distance[neighbour],neighbour])

        ans = max(distance[1:])
        return -1 if ans == inf else ans