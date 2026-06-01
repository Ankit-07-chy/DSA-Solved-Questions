# Recursion with memo
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def find(row,col):
            if row == n-1:
                return triangle[row][col]
            
            down = find(row+1,col)
            diag = find(row+1,col+1)
            return triangle[row][col] + min(down,diag)
            
        return find(0,0)
        

# Recursion WIth TLE
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        def find(triangle,idx,row):
            if row == rows-1:
                return triangle[row][idx]
                
            down = find(triangle,idx,row+1)
            diag = find(triangle,idx+1,row+1)
            return triangle[row][idx] + min(down,diag)
            
        return find(triangle,0,0)'''
            