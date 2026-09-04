class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # n queen -> n X n
        
        ans = []

        grid = [['.']*n for i in range(n)]

        def isSafe(row,col):
            i,j = row,col-1
            while i >=0 and j >= 0:
                if grid[i][j] == 'Q':
                    return False
                j -= 1
            
            i, j = row-1,col-1
            while i >= 0 and j >= 0:
                if grid[i][j] == 'Q':
                    return False
                i-=1;j -= 1
            i,j = row+1,col-1
            while n > i >= 0 and j>=0:
                if grid[i][j] == 'Q':
                    return False
                i += 1; j -= 1
            return True

        def fxn(col):
            if col == n:
                ans.append([''.join(row) for row in grid])
                return 
            
            for row in range(n):
                if isSafe(row,col):
                    grid[row][col] = 'Q'
                    fxn(col+1)
                    grid[row][col] = '.'
              
        fxn(0)

        return ans