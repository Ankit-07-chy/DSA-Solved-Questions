class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix); cols = len(matrix[0])

        i = 0; j = cols - 1

        while True:
            if i >= rows or i < 0 or j < 0 or j >= cols:
                return False
            elif matrix[i][j] == target:
                return True
            elif matrix[i][j]<target:
                i+=1
            elif matrix[i][j]>target:
                j -= 1