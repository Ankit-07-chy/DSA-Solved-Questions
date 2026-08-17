class Solution:
    def longestBitonicSequence(self, n, nums):
        # code here
        dp1 = [1]*n
        dp2 = [1]*n 
        
        for i in range(0,n):
            for prev in range(0,i):
                if nums[i] > nums[prev] and dp1[i] < 1 + dp1[prev]:
                    dp1[i] = 1 + dp1[prev]
        
        for i in range(n-1,-1,-1):
            for prev in range(n-1,i,-1):
                if nums[i]>nums[prev] and dp2[i] < 1 + dp2[prev]:
                    dp2[i] = 1 + dp2[prev]
        
        count_1_1 = 0; count_1_2 = 0
        maxi = 0
        for i in range(n):
            if dp1[i] == 1:
                count_1_1 += 1
            if dp2[i] == 1:
                count_1_2 += 1
            
            if dp1[i] == 1 or dp2[i] == 1:
                continue
            maxi = max(maxi,dp1[i]+dp2[i] - 1)
        
        if count_1_1 == n or count_1_2 == n:
            return 0
        return maxi