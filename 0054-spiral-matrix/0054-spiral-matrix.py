class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0; top = 0
        right = len(matrix[0])-1; bottom = len(matrix)-1
        rows = len(matrix); cols = len(matrix[0])

        result = []

        while top <= bottom and left <= right:

            # while len(result) != rows*cols:
            # top operation means left to right
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1

            # right op means top to bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1

            #  bottom operation means right to left
            if top <= bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # left means bottom to top
            if left <= right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1

        return result