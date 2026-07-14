import math
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1

        ans = max(bloomDay)
        low = 0; high = max(bloomDay)

        def check(bloomDay,day,m,k):
            
            curr = 0; count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=day:
                    count += 1
                else:
                    curr += (count //k)
                    count = 0
            curr += count // k   
            
            return m <= curr
                    

        while low <= high:
            
            mid = (low+high)//2
            # print('low mid high ',low,mid,high)
            t = check(bloomDay,mid,m,k)
            if t == True:
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans

        