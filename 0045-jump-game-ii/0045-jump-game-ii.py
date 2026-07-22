class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        if len(nums) == 1:
            return 0
        r = 1; l  = 0

        while r < (len(nums)):
            farthest = 0
            for idx in range(l,r):
                farthest = max(farthest,idx+nums[idx])
            l = r
            jump += 1
            r = farthest+1

        return jump
        