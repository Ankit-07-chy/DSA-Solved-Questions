from functools import cmp_to_key
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        # challenge that we can rearrange the order of segments
        nums = list(zip(nums1,nums0))
        seg = [u[0]*'1' + u[1]*'0' for u in nums]
        def cmp(a,b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            else:
                return 0
        seg.sort(key=cmp_to_key(cmp))
        mod = 10**9 + 7
        final_ = ''.join(seg)
        return int(final_,2)%mod
        '''
         nums = sorted(zip(nums1, nums0), key=lambda x: (-x[0], x[1]))
        mod = 10**9 + 7
        final_ = ''
        for u in nums:
            t1 = u[0]*'1'
            t2 = u[1]*'0'
            temp = t1+t2
            final_ = final_ + temp
        return int(final_,2)%mod
        '''
       
        """
        n = len(nums1)
        mod = 10**9 + 7
        dummy = [None]*n
        
        def count_1(string_):
            count_ = 0
            for s in string_:
                if s == '1':
                    count_ += 1
            return count_
            
        for i in range(n):
            temp1 = '1'*nums1[i]
            temp0 = '0'*nums0[i]
            dummy[i] = temp1 + temp0
        # visit = [False]*n
        
        final_str = ''
        freq = {}
        for idx,u in enumerate(dummy):
            tp = count_1(u)
            freq[idx] = tp
        # now sort dict based on val not on the key basis
        freq = dict(sorted(freq.items(),key=lambda item:item[1]))

        for key,val in freq.items():
            idx = key
            # my_val = dummy[idx]
            final_str = dummy[idx] + final_str
        return int(final_str,2) % mod
        """
        