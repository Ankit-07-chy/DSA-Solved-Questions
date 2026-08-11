class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # as I am at index i so for that I need to find -> the index of element which are at previous and smaller than this i element idx, and also I need to find element which are nxt to it and smaller than its idx

        # first for nxt smaller element
        n = len(heights)
        nse = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        # for pse 
        pse = [-1]*n
        stack = []
        for i in range(0,n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        print(nse,pse)

        ans = 0
        for i in range(0,n):
            right = n if nse[i] == -1 else nse[i]
            ans = max(ans,(right-pse[i]-1)*heights[i])
        return ans