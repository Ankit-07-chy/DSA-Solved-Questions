class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        def solve(idx):
            if idx == n:
                ans.append(nums[:])
                return
            used = set()

            for i in range(idx,n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[idx],nums[i] = nums[i],nums[idx]
                solve(idx+1)
                nums[idx],nums[i] = nums[i],nums[idx]
        solve(0)
        return ans