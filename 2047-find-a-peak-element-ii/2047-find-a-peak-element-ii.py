class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        rows = len(mat)
        cols = len(mat[0])

        low = 0
        high = cols - 1

        def check(col):
            row_idx = 0
            for i in range(rows):
                if mat[i][col] > mat[row_idx][col]:
                    row_idx = i
            return row_idx

        while low <= high:

            mid = (low + high) // 2

            row = check(mid)

            left = mat[row][mid - 1] if mid > 0 else -1
            right = mat[row][mid + 1] if mid < cols - 1 else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]

            elif left > mat[row][mid]:
                high = mid - 1

            else:
                low = mid + 1

        return [-1, -1]