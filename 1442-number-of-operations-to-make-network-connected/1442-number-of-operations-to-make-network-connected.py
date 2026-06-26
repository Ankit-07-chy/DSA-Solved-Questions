class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class DisJointSet:
            def __init__(self,n):
                self.n = n
                self.parent = list(range(n+1))
                self.rank = [0]*(n+1)
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
                elif self.rank[py]>self.rank[px]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px] += 1
        dsu = DisJointSet(n)
        temp = set()
        for u,v in connections:
            dsu.union(u,v)
        for i in range(n):
            temp.add(dsu.find(i))
        total_wires = len(connections)
        if total_wires >= n-1:
            return len(temp)-1
        return -1