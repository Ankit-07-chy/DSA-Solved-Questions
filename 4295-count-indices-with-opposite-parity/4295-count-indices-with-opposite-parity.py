class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        score = [0]*n
        for i in range(n):
            curr = nums[i]
            count = 0
            for j in range(i+1,n):
                if curr % 2 != nums[j]%2:
                    count += 1
            score[i]=count
        
        return score