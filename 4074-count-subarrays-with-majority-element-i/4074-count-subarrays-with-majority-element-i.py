class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        '''
        Super Brute Force
        Brute Force : 
            Generate all the subarray  --> O(2^n)
            Then in each subarray check whether target is greater then 1/2 of size ()
            If yes increase count by 1

            Avg T.C. n*2^n, S.C. n*2^n
        '''

        '''

        '''
        count = 0
        n = len(nums)

        for i in range(n):
            targetCount = 0
            for j in range(i,n):
                if nums[j] == target:
                    targetCount += 1
                length = j-i +1
                if targetCount*2 > length:
                    count += 1
        return count