class Solution:
    def check(self, nums: List[int]) -> bool:
        change = 0
        n = len(nums)
        if n <= 2:
            return True # n : 1, always sorted, n : 2 either sorted or rotated

        # n > 2 : 3,4,5,
        for i in range(0,n):
            if nums[i] > nums[(i+1)%n]:
                change += 1
        
        print(change)
        return change < 2