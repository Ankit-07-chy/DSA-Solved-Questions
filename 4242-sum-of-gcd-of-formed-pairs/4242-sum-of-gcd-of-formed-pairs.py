class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        import math
        max_array = [-1]*n
        prefixGcd = [-1]*n 
        max_array[0] = nums[0]; prefixGcd[0] = nums[0]

        for i in range(1,n):
            max_array[i] = max(nums[i],max_array[i-1])
            prefixGcd[i] = math.gcd(max_array[i],nums[i])

        prefixGcd.sort()
        sumi = 0
        i = 0; j = n-1
        while i<j:
            temp = math.gcd(prefixGcd[i],prefixGcd[j])
            sumi += temp
            i += 1
            j -= 1
        
        return sumi