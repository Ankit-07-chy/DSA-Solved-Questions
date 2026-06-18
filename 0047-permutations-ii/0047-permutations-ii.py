class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        visited = [0]*n
        nums.sort()

        def solve(stack,visited):
            if len(stack) == len(nums):
                result.append(stack[:])
                return 
            for i in range(0,n):
                if visited[i] == 1:
                    continue
                
                if visited[i-1] == 0 and nums[i] == nums[i-1] and i>0:
                    continue
                visited[i] = 1
                stack.append(nums[i])
                solve(stack,visited)
                visited[i] = 0
                stack.pop()
        solve([],visited)
        return result