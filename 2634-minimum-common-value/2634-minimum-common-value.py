class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pt1 = 0; pt2 = 0; n1 = len(nums1); n2 = len(nums2)
        common = float('inf')
        while pt1<n1 and pt2<n2:
            temp1 = nums1[pt1]; temp2 = nums2[pt2]
            if temp1 == temp2:
                common = min(common,temp1)
                pt1 += 1
                pt2 += 1
            elif temp1 > temp2:
                pt2 += 1
            else:
                pt1 += 1
        if common == float('inf'):
            return -1
        return common