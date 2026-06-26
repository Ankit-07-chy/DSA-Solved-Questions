

'''
class Solution:
    def DSU(self, n, queries):
        
        class DisjointSet:
            def __init__(self, n):
                self.n = n
                self.rank = [0] * (n + 1)
                self.parent = list(range(n + 1))
                
            def find(self, x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):  # by rank
                px = self.find(x)
                py = self.find(y)

                if px == py:
                    return

                if self.rank[px] > self.rank[py]:
                    self.parent[py] = px

                elif self.rank[px] < self.rank[py]:
                    self.parent[px] = py

                else:
                    self.parent[px] = py   
                    self.rank[py] += 1
        
        dsu = DisjointSet(n)
        ans = []

        for query in queries:
            if query[0] == 2:
                ans.append(dsu.find(query[1]))
            else:
                dsu.union(query[1], query[2])

        return ans'''
        
class Solution:
    def DSU(self, n, queries):

        class DisjointSet:
            def __init__(self, n):
                self.parent = list(range(n + 1))

            def find(self, x):
                if self.parent[x] == x:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, z):
                px = self.find(x)
                pz = self.find(z)

                if px != pz:
                    self.parent[px] = pz   # always make z's root parent

        dsu = DisjointSet(n)

        ans = []

        for query in queries:
            if query[0] == 1:
                dsu.union(query[1], query[2])
            else:
                ans.append(dsu.find(query[1]))

        return ans