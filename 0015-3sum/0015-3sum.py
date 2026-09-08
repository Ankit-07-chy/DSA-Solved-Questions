# optimal one
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(0,n):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i+1; k = n-1
            while j<k:
                sumi = nums[i] + nums[j] + nums[k]
                if sumi > 0:
                    k -= 1
                elif sumi < 0:
                    j += 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1; k -= 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                    while k >= 0 and nums[k] == nums[k+1]:
                        k -= 1
        return ans



'''
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
'''