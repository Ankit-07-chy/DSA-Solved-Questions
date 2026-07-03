import math
inf = math.inf
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        '''
        DAG 
            n node, edges(u_i,v_i,cost_i)

        '''
        left = inf; right = 0
        # Binary search + Dijkastra approach
        n = len(online)
        adjList = [[] for i in range(n)]
        for u,v,cost in edges:
            if online[u] == False or online[v] == False:
                continue
            adjList[u].append([v,cost])
            left = min(left,cost)
            right = max(right,cost)

        # graph make completed


        # check fxn using dijkstra's algo
        def check(mid,k,n,adjList):
            import heapq
            distance = [inf]*n
            distance[0] = 0

            min_heap = []
            heapq.heappush(min_heap,[0,0])

            while min_heap:
                dist,node = heapq.heappop(min_heap)

                

                if dist > k:
                    return False
                if node == n-1:
                    return True

                if distance[node] < dist:
                    continue

                for neigh,wt in adjList[node]:
                    if wt < mid:
                        continue
                    if dist + wt < distance[neigh]:
                        distance[neigh] = dist+wt
                        heapq.heappush(min_heap,[distance[neigh],neigh])
            return False


        # Do binary search on cost
        ans = -1
        # if left == inf or right == 0:
        #     return -1
        while left <= right:
            mid = (left+right) // 2

            if check(mid,k,n,adjList):
                ans = mid
                left = mid + 1
            else:
                right = mid-1

        return ans