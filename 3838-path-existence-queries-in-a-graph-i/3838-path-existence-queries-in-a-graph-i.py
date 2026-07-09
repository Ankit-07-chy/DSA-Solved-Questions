class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.rank = [0]*n

            def find(self,x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py :
                    return 
                if self.rank[px]>self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px]<self.rank[py]:
                    self.parent[px] = py
                else:
                    self.rank[px]+=1
                    self.parent[py] = px
        dsu = DSU(n)
        result = []

        # here is the actual use of the given thing that array is sorted
        for i in range(n-1):
            if nums[i+1]-nums[i]<=maxDiff:
                dsu.union(i+1,i)

        for query in queries:
            x = query[0]; y = query[1]
            if dsu.find(x) == dsu.find(y):
                result.append(True)
            else:
                result.append(False)
        return result

'''
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class DSU:
            def __init__(self,n):
                self.parent = list(range(n))
                self.rank = [0]*n

            def find(self,x):
                if x == self.parent[x]:
                    return x
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self,x,y):
                px = self.find(x)
                py = self.find(y)
                if px == py :
                    return 
                if self.rank[px]>self.rank[py]:
                    self.parent[py] = px
                elif self.rank[px]<self.rank[py]:
                    self.parent[px] = py
                else:
                    self.rank[px]+=1
                    self.parent[py] = px
        dsu = DSU(n)
        result = []

        i = 0
        # This loop can cause o(n^2)
        while i < n:
            j = i+1
            while j < n:
                if abs(nums[j]-nums[i]) <= maxDiff:
                    dsu.union(i,j)
                    j += 1
                else:
                    break
            i += 1

        for query in queries:
            x = query[0]; y = query[1]
            if dsu.find(x) == dsu.find(y):
                result.append(True)
            else:
                result.append(False)
        return result
'''