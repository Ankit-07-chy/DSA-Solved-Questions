class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        min_heap = []; n = len(nums)
        for i in range(k):
            heapq.heappush(min_heap,nums[i])
        for i in range(k,n):
            if nums[i]>min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,nums[i])
        return min_heap[0]
        
        '''
        # With Sorting
        nums.sort()
        return nums[-k]
        '''