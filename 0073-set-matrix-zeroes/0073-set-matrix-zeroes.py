# Optimal Approach
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero rows based on markers
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Zero columns based on markers
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
# Better Approach
'''
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
                matrix[r][e] = 0'''