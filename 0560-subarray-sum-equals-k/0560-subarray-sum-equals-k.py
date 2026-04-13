class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        count = 0  
        n = len(nums); i = 0; curr_sum = 0
        while i < n:
            curr_sum += nums[i]
            if curr_sum - k in prefix_sum :
                count += prefix_sum[curr_sum-k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0) + 1
            i += 1
        return count