import math
from functools import lru_cache
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def recursion( idx, first, second):
            if idx == len(nums):
                return 1 if first != 0 and first == second else 0
            skip = recursion(idx+1,first,second)
            tak1 = recursion(idx+1,math.gcd(first,nums[idx]),second)
            tak2 = recursion(idx+1,first,math.gcd(nums[idx],second))
            return (skip + tak1 + tak2) % MOD
            

        return recursion(0,0,0)