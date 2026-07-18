class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = 0; high = 0
        prev = -1
        n = len(nums)
        zeros = 0; ans = 0

        while high < n:
            if nums[high]==0:
                zeros += 1

            while zeros > k:
                if nums[low]==0:
                    zeros -= 1
                low += 1
            
            ans = max(ans,high-low+1)

            high += 1

        return ans