class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = {0:1}
        n = len(nums)
        curr_sum = 0
        count = 0 
        for i in range(0,n):
            curr_sum += nums[i]
            prev_sum = curr_sum - goal
            if prev_sum in prefixSum:
                count += prefixSum[prev_sum]
            if curr_sum in prefixSum:
                prefixSum[curr_sum]+=1
            elif curr_sum not in prefixSum:
                prefixSum[curr_sum] = 1

        return count