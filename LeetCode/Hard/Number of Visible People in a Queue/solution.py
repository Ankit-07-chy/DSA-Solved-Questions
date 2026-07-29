class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0]*n
        stack = []

        for i in range(0,n):
            while stack and heights[stack[-1]]<=heights[i]:
                result[stack[-1]] += 1
                stack.pop()
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        return result
# Brute Force
'''
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0]*n 
        for i in range(0,n):

            count = 0
            prev_height = -1
            curr_height = heights[i]

            for j in range(i+1,n):
                if heights[j]>curr_height:
                    count += 1
                    break
                if heights[j]<curr_height:
                    if heights[j]>prev_height:
                        count += 1
                        prev_height = heights[j]
                if heights[j] == curr_height:
                    if heights[j] > prev_height:
                        count += 1
                        prev_height = heights[j]

            result[i] = count

        return result
'''