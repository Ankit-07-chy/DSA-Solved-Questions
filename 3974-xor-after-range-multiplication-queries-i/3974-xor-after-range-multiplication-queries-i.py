class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        q = len(queries) # return len of queries
        n = len(nums)
        for i in range(q):
            li,ri,ki,vi = map(int,queries[i])
            idx = li
            while idx <= ri and idx < n:
                nums[idx] = (nums[idx]*vi) % (10**9 + 7)
                idx += ki
        ans = 0
        for t in nums:
            ans = ans^t
        return ans^0