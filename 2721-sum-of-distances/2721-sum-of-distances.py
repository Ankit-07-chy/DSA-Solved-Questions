class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        res = [0] * n
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return res

"""
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        freq = {} # number , [indexing]
        for idx, val in enumerate(nums):
            if val in freq:
                freq[val].append(idx)
            else:
                freq[val]=[idx]
        def find(array,value):
            curr = 0
            for u in array:
                curr += abs(u-value)
            return curr

        n = len(nums)
        arr = [0]*n
        for u,v in freq.items():
            if len(v)>1:
                for value in v:
                    arr[value] = find(v,value)
        return arr

        """
