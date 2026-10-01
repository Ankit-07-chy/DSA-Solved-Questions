class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # it is mentioned consecutive maximum length
        nums = set(nums)
        nums = list(nums)
        # initally it came to my mind is, first sort it, then choose a idx prev, and idx curr and also a maxi varible when ever condition dissatisfied break it
        nums.sort()
        # print(nums)
        prev_idx = 0
        max_len = 0
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                max_len = max(max_len,i-1-prev_idx+1)
                prev_idx = i
        max_len = max(max_len,i-prev_idx+1)
        return max_len
1,2,3,4,100,200
0,1,2,3,4,5,6,7,8