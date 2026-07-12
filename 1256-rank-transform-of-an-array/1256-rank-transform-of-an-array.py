class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(set(arr))
        arr_ = {}
        for i,e in enumerate( new_arr):
            if e not in arr_:
                arr_[e] = i 
        result = []
        for a in arr:
            result.append(arr_[a]+1)
        return result
'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        new_arr = sorted(set(arr))
        print(new_arr)
        for num in arr:
            for i in range(len(new_arr)):
                if num == new_arr[i]:
                    result.append(i+1)
                    break 
        return result
        '''