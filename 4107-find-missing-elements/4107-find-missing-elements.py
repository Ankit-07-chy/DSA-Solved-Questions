class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)
        size = largest - smallest + 1
        arr = [0] * size

        for num in nums:
            idx = num - smallest
            arr[idx] += 1

        result = []
        for idx, val in enumerate(arr):
            if val == 0:
                result.append(idx + smallest)
        return result
