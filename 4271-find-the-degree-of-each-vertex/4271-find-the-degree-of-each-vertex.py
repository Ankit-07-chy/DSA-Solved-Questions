class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degree = [0]*n
        for i in range(n):
            curr_row = matrix[i]
            st = sum(curr_row)
            degree[i] = st
        return degree