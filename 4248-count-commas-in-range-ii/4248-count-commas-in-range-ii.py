class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        lent = len(str(n))
        for i in range(4,lent+1):
            commas = (i-1)//3
            start = 10**(i-1)
            end = min(10**i-1,n)
            temp = end-start +1
            if temp > 0:
                count += temp*commas
        return count