class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        n = len(nums)
        dp = [1]*n
        idxs = list(range(n))
        maxi = 1; idx = 0
        for i in range(1,n):
            for prev in range(0,i):
                if nums[i] % nums[prev] == 0 and dp[i] < 1 + dp[prev]:
                    dp[i] = 1 + dp[prev]
                    idxs[i] = prev 

                # if dp[prev] > maxi:
                #     maxi = dp[prev]
                #     idx = prev
            if dp[i] > maxi:
                maxi = dp[i]
                idx = i
        print(dp,idxs,idx)
        # now from idxs and idx try to find the subset
        subset = []
        while idxs[idx] != idx:
            subset.append(nums[idx])
            idx = idxs[idx]
        subset.append(nums[idx])
        return subset