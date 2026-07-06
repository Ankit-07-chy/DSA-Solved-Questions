from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_dec_queue = deque([])
        n = len(nums)
        ans = []
        for i in range(0,k-1):
            while monotonic_dec_queue and nums[monotonic_dec_queue[-1]] < nums[i]:
                monotonic_dec_queue.pop()
            monotonic_dec_queue.append(i)

        # k lenght window has been puted to my queue, now slidie this and check whether length is in range or not
        for i in range(k-1,n):
            while monotonic_dec_queue and i - monotonic_dec_queue[0] + 1 > k:
                monotonic_dec_queue.popleft()
            while monotonic_dec_queue and nums[monotonic_dec_queue[-1]] < nums[i]:
                monotonic_dec_queue.pop()
            monotonic_dec_queue.append(i)
            ans.append(nums[monotonic_dec_queue[0]])
        return ans