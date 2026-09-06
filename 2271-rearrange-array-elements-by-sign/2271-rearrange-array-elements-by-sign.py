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