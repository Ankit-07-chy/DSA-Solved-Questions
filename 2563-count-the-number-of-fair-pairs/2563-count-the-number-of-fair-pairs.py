class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        def lowerBound(nums,number,low,high):
            #low = 0
            #high = len(nums)
            while low < high:
                mid = (low+high)//2
                if nums[mid] < number:
                    low = mid + 1
                else:
                    high = mid 
            return low 
        
        def upperBound(nums,number,low,high):
            #low = 0
            #high = len(nums)
            while low < high:
                mid = (low+high)//2
                if nums[mid] <= number:
                    low = mid + 1
                else:
                    high = mid 
            return low 

        for i in range(0,n):
            lower_range = lower - nums[i]
            upper_range = upper - nums[i]

            lower_idx = lowerBound(nums,lower_range,i+1,n)
            upper_idx = upperBound(nums,upper_range,i+1,n)

            count += (upper_idx-lower_idx)

        return count