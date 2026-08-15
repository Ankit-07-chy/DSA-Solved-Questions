class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix); cols = len(matrix[0])

        def find_max_square_area(heights):
            nonlocal ans
            # first find next_smaller element and previous smaller eelemnt
            n = len(heights)
            nse = [-1]*n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    nse[i] = stack[-1]
                stack.append(i)
            
            pse = [-1]*n 
            stack = []
            for i in range(0,n,1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                stack.append(i)
            
            curr = 0
            for i in range(n):
                left = pse[i]
                right = n if nse[i] == -1 else nse[i]
                width = right - left - 1
                curr = min(heights[i],width)**2 
                ans = max(ans,curr)


        ans = 0
        heights = [0]*cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            find_max_square_area(heights)

        return ans
                