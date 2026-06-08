class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
            Every element less than pivot appears before and every element greater than pivot
            every element equal to pivot appears in b/w
            relative order should be maintain
        '''
        arr_left = []
        arr_right = []
        arr_bw = []
        for u in nums:
            if u == pivot:
                arr_bw.append(u)
            if u < pivot:
                arr_left.append(u)
            if u > pivot:
                arr_right.append(u)
        return arr_left[:] + arr_bw[:] + arr_right[:]