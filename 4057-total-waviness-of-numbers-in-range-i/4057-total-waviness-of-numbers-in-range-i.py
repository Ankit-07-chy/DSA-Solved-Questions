class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # waviness -> total peaks and valleys
        def find(n):
            temp = n
            temp = list(str(n))
            curr = 0
            for i in range(1,len(temp)-1):
                if temp[i-1]<temp[i]>temp[i+1] or temp[i-1]>temp[i]<temp[i+1]:
                    curr += 1
            return curr
        count = 0
        for num in range(num1,num2+1):
            count += find(num)
        return count