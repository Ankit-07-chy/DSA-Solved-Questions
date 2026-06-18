class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = [0]*n

        def solve(stack,visited):
            if len(stack) == len(nums):
                result.append(stack[:])
                return
            
            for i in range(0,n):
                if visited[i] == 0:
                    stack.append(nums[i])
                    visited[i] = 1
                    solve(stack,visited)
                    visited[i] = 0
                    stack.pop()
        solve([],visited)
        return result