class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def findSum(arr,goal):
            if goal <0:
                return 0
            left = 0; right = 0
            count = 0
            curr_sum = 0
            for right in range(0,len(nums)):
                curr_sum += arr[right]
                while curr_sum > goal:
                    if left >= len(nums):
                        break
                    curr_sum -= arr[left]
                    left += 1

                if curr_sum <= goal:
                    count += right-left+1
            return count

        return findSum(nums,goal)-findSum(nums,goal-1)
'''
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

        return count'''