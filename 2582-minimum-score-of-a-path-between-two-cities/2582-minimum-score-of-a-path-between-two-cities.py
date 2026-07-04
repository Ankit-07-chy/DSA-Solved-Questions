class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.n = n
                self.rank = [0]*(n+1)
                self.parent= list(range(n+1))
            def find(self,x):
                if x == self.parent[x]:
                    return x 
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py:
                    return 
                if self.rank[px]>self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px]<self.rank[py]:
                    self.parent[px] = py
                else:
                    self.parent[px] = py
                    self.rank[py] += 1
        dsu = DSU(n)
        roads.sort(key=lambda x:x[-1])
        for a,b,dist in roads:
            dsu.union(a,b)
        
        if dsu.find(1) != dsu.find(n):
            return 
        ans = inf
        for a,b,dist in roads:
            p_a = dsu.find(a)
            p_b = dsu.find(b)
            p_1 = dsu.find(1)
            p_n = dsu.find(n)
            if p_1 == p_a or p_1 == p_b or p_n == p_a or p_n == p_b:
                ans = min(ans,dist)
        return ans