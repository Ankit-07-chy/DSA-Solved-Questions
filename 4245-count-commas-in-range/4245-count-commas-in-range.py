class Solution:
    def countCommas(self, n: int) -> int:
        # if n >= 1000:
        count = 0
        for i in range(1000,n+1):
            t = str(i)
            count += ((len(t)-1)//3)
        return count
                