class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_idx = 0; neg_idx = 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] >=0:
                ans[pos_idx]= nums[i]
                pos_idx += 2
            else:
                ans[neg_idx]= nums[i]
                neg_idx += 2
        return ans


'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        ans = []
        ans.append(pos[0]); ans.append(neg[0])
        for i in range(1,len(neg)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
'''