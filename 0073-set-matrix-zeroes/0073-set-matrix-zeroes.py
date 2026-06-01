class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set(); col = set()
        n = len(matrix); m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i); col.add(j)
        
        for e in row:
            for c in range(m):
                matrix[e][c] = 0
        for e in col:
            for r in range(n):
                matrix[r][e] = 0