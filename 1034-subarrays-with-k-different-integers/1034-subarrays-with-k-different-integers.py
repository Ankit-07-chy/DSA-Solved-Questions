class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findSubarray(arr,k):
            left = 0; right = 0
            count = 0; freq = {}
            for right in range(len(arr)):
                freq[arr[right]] = freq.get(arr[right],0)+1

                while len(freq)>k:
                    freq[arr[left]] -= 1
                    if freq[arr[left]] == 0:
                        freq.pop(arr[left])
                    left += 1

                count += right-left+1

            return count

        return findSubarray(nums,k)-findSubarray(nums,k-1)