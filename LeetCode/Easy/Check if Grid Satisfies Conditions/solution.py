class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid); cols = len(grid[0])
        # if only one row or only one cols
        if cols == 1:
            for row in range(rows-1):
                if grid[row][0] != grid[row+1][0]:
                    return False
        if rows == 1:
            for col in range(cols-1):
                if grid[0][col]==grid[0][col+1]:
                    return False
        for i in range(rows-1):
            for col in range(0,cols-1):
                if grid[i][col] != grid[i+1][col] or grid[i][col] == grid[i][col+1]:
                    return False

        # check the last row and last cols

        # for last col
        for row in range(rows-1):
            if grid[row][-1] != grid[row+1][-1]:
                return False
        # for last row
        for col in range(cols-1):
            if grid[-1][col] == grid[-1][col+1]:
                return False

        return True