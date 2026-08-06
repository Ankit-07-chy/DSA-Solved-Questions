class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.rank = [0]*n

            def union(self,x,y):
                # here x is idx and y is also idx
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
            def find(self,x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        dsu = DSU(n)
        for i in range(n):
            for j in range(0,n):
                if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) :
                    dsu.union(i,j)
        s = set()
        # this will give how different groups formen
        for i in range(n):
            s.add(dsu.find(i))
        return n - len(s)