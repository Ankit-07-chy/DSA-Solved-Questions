import math
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.LOG = math.ceil(math.log2(n))+1
        self.parent = [[-1]*self.LOG for i in range(n)]
        for node,val in enumerate(parent): # for column 1 it has done by this only
            self.parent[node][0] = val
        
        for col in range(1,self.LOG):
            for node in range(0,n):
                mid = self.parent[node][col-1]
                if mid != -1:
                    self.parent[node][col] = self.parent[self.parent[node][col-1]][col-1]
        

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.LOG):
            if k & (1<<j):
                node = self.parent[node][j]
                if node == -1:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)