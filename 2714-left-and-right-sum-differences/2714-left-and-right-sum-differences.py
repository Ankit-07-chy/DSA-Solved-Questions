class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0]*n
        rightSum = [0]*n
        curr = 0
        for i in range(n):
            leftSum[i] = curr
            curr += nums[i]
        curr = 0
        for i in range(n-1,-1,-1):
            rightSum[i] = curr
            curr += nums[i]
        ans = [0]*n
        for i in range(n):
            ans[i] = abs(leftSum[i]-rightSum[i])
        return ans