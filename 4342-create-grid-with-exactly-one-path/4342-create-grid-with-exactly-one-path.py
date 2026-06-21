class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']*n for i in range(m)]
       
        for i in range(n):
            grid[0][i] = '.'
        
        for j in range(m):
            grid[j][-1] = '.'

        return [''.join(row) for row in grid]
        