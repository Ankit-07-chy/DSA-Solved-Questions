class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # o(n^2)
        
        ans = []
        seen = set()

        for i in range(0,len(nums)):
            hashMap = set()
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                if third in hashMap:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    seen.add(tuple(temp))
                hashMap.add(nums[j])
        return list(seen)