import math
class Solution:
    def solve(self, bt):
        # code here
        bt.sort()
        prev_wait = 0
        total_wait = 0
        n = len(bt)
        for i in range(n):
            total_wait += prev_wait
            prev_wait += bt[i] 
            # print(prev_wait,total_wait)
        # print(total_wait+prev_wait)
        return (total_wait)//len(bt)