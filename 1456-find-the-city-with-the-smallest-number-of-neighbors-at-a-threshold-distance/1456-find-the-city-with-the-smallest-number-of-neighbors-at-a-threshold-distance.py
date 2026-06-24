class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cost = [[10**8]*n for i in range(n)]

        for i in range(n):
            cost[i][i] = 0
        for u, v, w in edges:
            cost[u][v] = w
            cost[v][u] = w
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if cost[i][via] != 10**8 and cost[via][j] != 10**8 and cost[i][j] > cost[i][via] + cost[via][j]:
                        cost[i][j] = cost[i][via]+cost[via][j]
        
        city = [[] for _ in range(n)]
        for i_c in range(n):
            for j_c in range(n):
                if i_c != j_c and cost[i_c][j_c]<=distanceThreshold:
                    city[i_c].append(j_c)
        lenght = float("inf")
        ans = -1

        for idx, cit in enumerate(city):
            if len(cit) <= lenght:
                lenght = len(cit)
                ans = idx
        return ans