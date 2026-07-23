
# O(n^3) -> brute force

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        # maximum number we can get n; and min either 0 or 1
        def msb(num):
            #curr = 0
            idx = 0
            while num:
                num = num >> 1
                idx += 1
            return idx

                
        print(msb(n))
        if n < 3:
            return n
        else:
            return 2**(msb(n)) 
        

