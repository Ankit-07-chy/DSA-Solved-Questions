# optmization in this. 
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # instaed of diff array, do this using ordered map
        element_map = {}
        diff_map = {}
        size = max(nums)
        for num in nums:
            low = max(0,num-k)
            high = min(size,num+k)
            element_map[num] = element_map.get(num,0)+1
            diff_map[low] = diff_map.get(low,0)+1
            diff_map[high+1] = diff_map.get(high+1,0) - 1
        
        ans = 0
        # which making the cumulative sum do this as well
        cumulative_sum = 0

        # to ordered map
        for u in sorted(set(diff_map.keys()) | set(element_map.keys())):
            v = diff_map.get(u, 0)      # 0 if not a boundary
            cumulative_sum += v
            
            curr_freq = element_map.get(u, 0)
            can_go = cumulative_sum
            
            ans = max(ans, min(can_go - curr_freq, numOperations) + curr_freq)

        return ans

# this is expected to give TLE or MLE, as it gives
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # burte force that I have applied on 3346
        mapp = {}
        size = max(nums)
        diff = [0]*(size+2)
        for num in nums:
            mapp[num] = mapp.get(num,0) + 1
            lower = max(0,num-k)
            upper = min(size,num+k)
            diff[lower] += 1
            if upper + 1 < size:
                diff[upper+1] -= 1


        ans = 0
        for i in range(1,size+2):
            diff[i] += diff[i-1]

        for i in range(0,size+1):
            curr_freq = mapp.get(i,0)
            expect = diff[i]

            ans = max(ans,min(expect-curr_freq,numOperations) + curr_freq)
        return ans

        '''