class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums); subArrayCount = 0


        def check(number,x):
            number = str(number)
            if int(number[0]) == x and int(number[-1]) == x:
                return True
            return False
        
        for i in range(0,n):
            sumi = 0
            for j in range(i,n):
                sumi += nums[j]
                t = check(sumi,x)
                if t:
                    subArrayCount += 1
                
        return subArrayCount
            