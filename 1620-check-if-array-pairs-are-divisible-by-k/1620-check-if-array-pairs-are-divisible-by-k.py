class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # I have picked wrong question and got increment in that direction

        freq = {}
        for n in arr:
            freq[n%k] = freq.get(n%k,0) + 1

        for i in range(0,k):
            if i in freq:
                if i == 0:
                    if freq[0] % 2 != 0:
                        return False

                elif i*2 == k:
                    if freq[i] % 2 != 0:
                        return False
                else:
                    if k-i not in freq:
                        return False
                    if freq[i] != freq[k-i]:
                        return False
        return True
'''
from functools import cache
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        total_sum = sum(arr)
        n = len(arr)

        @cache
        def recursion(idx,curr_sum,curr_len):
            if idx >= n and curr_sum % k == 0 and (total_sum-curr_sum) % k == 0 and curr_len == n//2:
                return True
            elif idx >= n :
                return False

            else:
                # now we have pick and not pick, then return or of both
                pick = recursion(idx+1,curr_sum +arr[idx],curr_len+1)
                not_pick = recursion(idx+1,curr_sum,curr_len)

                return pick or not_pick

        return recursion(0,0,0)'''