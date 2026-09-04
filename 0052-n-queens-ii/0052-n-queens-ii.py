class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [['.']*n for _ in range(n)]
        ans = 0

        def isSafe(row,col):
            i,j = row-1,col-1
            while i >= 0 and j>= 0:
                if grid[i][j] == 'Q':
                    return False
                i -= 1; j -= 1
            i,j = row,col-1
            while j>= 0:
                if grid[i][j] == 'Q':
                    return False
                j -= 1
            i,j = row+1,col-1
            while i < n and j >=0:
                if grid[i][j] == 'Q':
                    return False
                i +=1;j -=1
            return True

        def fxn(col):
            nonlocal ans
            if col == n:
                ans += 1
                return 1
            for r in range(0,n):
                if isSafe(r,col):
                    grid[r][col] = 'Q'
                    fxn(col+1)
                    grid[r][col] = '.'
        fxn(0)
        return ans