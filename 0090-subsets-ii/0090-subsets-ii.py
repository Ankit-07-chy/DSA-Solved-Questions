class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        
        def fxn(idx,stack):
            ans.append(stack[:])

            for j in range(idx,n):
                if nums[j] == nums[j-1] and j != idx:
                    continue
                stack.append(nums[j])
                fxn(j+1,stack)
                stack.pop()
        nums.sort()
        fxn(0,[])
        return ans