class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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
                elif self.rank[px]<self.rank[py]:
                    self.parent[px] = py
                else:
                    self.parent[py] = px
                    self.rank[px] += 1

                
        n = len(isConnected)
        dsu = DisJointSet(n)
        count = 0
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    dsu.union(i,j)
        provinces = set()
        for i in range(n):
            provinces.add(dsu.find(i))
        return len(provinces)

'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n

        def bfs(start):
            row_to_start = isConnected[start]
            for j in range(n):
                if row_to_start[j] == 1 and not visited[j]:
                    visited[j] = True
                    bfs(j)

        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1
                visited[i] = True
                bfs(i)
        return count
        '''