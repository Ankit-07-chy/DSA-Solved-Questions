class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        

        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        heights = [0]*cols

        def check_max_area(arr):
            nonlocal ans
            n = len(arr)

            nse = [-1]*n
            stack = []
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]
                stack.append(i)

            pse = [-1]*n
            stack = []
            for i in range(0,n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    pse[i] = stack[-1]
                stack.append(i)

            for i in range(n):
                right = n if nse[i] == -1 else nse[i]
                left = pse[i]
                ans = max(ans,arr[i]*(right-left-1))


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            check_max_area(heights)

        return ans

            
