class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxi = max(nums); mini = min(nums)
        ans = -1
        for i in range(1,mini+1):
            if maxi % i == 0 and mini % i == 0:
                ans = max(ans,i)
        return ans
