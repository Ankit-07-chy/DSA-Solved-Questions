from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix arrays (1-indexed for easier queries)
        pref_sum = [0] * (n + 1)   # sum of digits
        pref_val = [0] * (n + 1)   # integer of concatenated non-zero digits % MOD
        pref_len = [0] * (n + 1)   # count of non-zero digits
        pow10 = [1] * (n + 1)      # powers of 10 modulo MOD

        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i in range(1, n + 1):
            digit = int(s[i - 1])
            
            pref_sum[i] = pref_sum[i - 1] + digit
            pref_len[i] = pref_len[i - 1] + (1 if digit != 0 else 0)

            if digit == 0:
                pref_val[i] = pref_val[i - 1]
            else:
                pref_val[i] = (pref_val[i - 1] * 10 + digit) % MOD

        ans = []
        for l, r in queries:
            # Convert 0-based inclusive to 1-based for prefix arrays
            l += 1
            r += 1

            # sum of digits in substring s[l:r]
            sum_x = pref_sum[r] - pref_sum[l - 1]

            # length of the non-zero concatenated part in substring
            len_x = pref_len[r] - pref_len[l - 1]

            # Extract X (mod MOD) using formula:
            # X = (val_r - val_left * 10^(len_x)) % MOD
            val_r = pref_val[r]
            val_left = pref_val[l - 1]
            x_mod = (val_r - (val_left * pow10[len_x]) % MOD + MOD) % MOD

            # Final result modulo MOD
            ans.append((x_mod * (sum_x % MOD)) % MOD)

        return ans



# o(n**2)



'''MOD = 10**9 + 7
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum = [0]*n
        concateDigits = [None]*n

        def findSum(string,idx):
            if idx == 0:
                return int(s[0]) % MOD
            previous_sum = preSum[idx-1] + int(string)
            return previous_sum % MOD

        def findConcate(string,idx):
            if idx == 0:
                return s[0]

            previous_concate = concateDigits[idx-1]
            if string == '0':
                return previous_concate
            else:
                return previous_concate + string

        for idx,string in enumerate(s):
            preSum[idx] = findSum(string,idx)  # sum upto idx index
            concateDigits[idx] = findConcate(string,idx) # this will return concated digits upto index idx

        def check_concate(right,left):
            while len(left)!=len(right):
                left += '0'
            return (int(right)-int(left))%MOD

        query_len = len(queries)
        result = [-1]*query_len
        for idx,query in enumerate(queries):
            left = query[0]-1; right = query[1]
            if left < 0:
                result[idx] = (int(concateDigits[right])*preSum[right]) % MOD
            else:
                result[idx] = ((preSum[right]-preSum[left])*check_concate(concateDigits[right],concateDigits[left]))%MOD
            
        return result'''