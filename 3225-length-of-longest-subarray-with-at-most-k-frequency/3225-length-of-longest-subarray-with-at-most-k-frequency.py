class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        i = 0; j = 0; n= len(nums)

        ans = 0
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] <= k:
                ans = max(ans,i-j+1)

            while freq[nums[i]] > k:
                freq[nums[j]] -=  1
                j += 1
        return ans