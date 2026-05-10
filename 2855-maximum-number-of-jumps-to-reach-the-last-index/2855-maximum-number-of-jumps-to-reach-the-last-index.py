class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = [False]*n
        def solve(idx):
            if idx == n-1:
                return 0
            result = float('-inf')
            for j in range(idx+1,n):
                if abs(nums[idx]-nums[j]) <= target:
                    if memo[j] == False:
                        temp = 1+solve(j)
                        memo[j] = temp
                    else:
                        temp = memo[j]
                    result = max(temp,result)
            return result
        t = solve(0)
        if t != float('-inf'):
            return t
        return -1
        # return solve(0)
        
