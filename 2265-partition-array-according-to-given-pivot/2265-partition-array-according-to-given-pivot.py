class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [pivot]*n
        low = 0; high = n-1
        for i in nums:
            if i < pivot:
                result[low] = i
                low += 1
            elif i > pivot:
                result[high] = i
                high -= 1
        # reverse the array after the last pivot + 1 idx to n-1
        last_idx = -1
        for i in range(n-1,-1,-1):
            if result[i] == pivot:
                last_idx = i
                break
        high = n-1
        last_idx += 1
        while last_idx <= high:
            result[last_idx],result[high]= result[high],result[last_idx]
            last_idx += 1
            high -= 1
        return result

# T.C. - O(n), S.C. - O(n)
'''
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # 
        #     Every element less than pivot appears before and every element greater than pivot
        #     every element equal to pivot appears in b/w
        #     relative order should be maintain
        # 
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
        return arr_left[:] + arr_bw[:] + arr_right[:]'''