class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod

        dif = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue
            dif[:] = [1] * len(dif)
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % mod
                R = ((r - l) // k + 1) * k + l
                dif[R] = dif[R] * pow(v, mod - 2, mod) % mod

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        res = 0
        for x in nums:
            res ^= x
        return res

'''
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        Optimal for : 3653. XOR After Range Multiplication Queries I
        https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/?envType=daily-question&envId=2026-04-08
        """ 
        q = len(queries) # len of quereis
        mod = 10**9 + 7
        curr = 0
        n = len(nums)
        for i in range(q):
            li,ri,ki,vi = map(int,queries[i])
            # my logic is directly find how many time I need to multiply with vi
            # and simply take vi^mult_times % mod
            # then multimpy each element of nums and take % mod and return result the both mod mult to mod
            
            '''