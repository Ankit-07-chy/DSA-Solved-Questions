class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        # Helper function to check if the first k queries can make nums a zero array
        def check(k: int) -> bool:
            diff = [0] * (n + 1)
            # Apply the first k queries using the difference array technique
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val
            
            # Compute prefix sums and check against nums
            curr_sum = 0
            for i in range(n):
                curr_sum += diff[i]
                if nums[i] > curr_sum:
                    return False
            return True

        # Binary search for the minimum k
        left, right = 0, m
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            # If 0 queries are enough (i.e., nums is already all zeros)
            if mid == 0:
                if all(x == 0 for x in nums):
                    return 0
                left = mid + 1
                continue
                
            if check(mid):
                ans = mid
                right = mid - 1  # Try to find a smaller valid k
            else:
                left = mid + 1   # Need more queries
                
        return ans if check(ans) else -1