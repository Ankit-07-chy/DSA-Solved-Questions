class Solution:
    def myAtoi(self, s: str) -> int:
        
        ans = 0
        sign = 1
        idx = 0
        n = len(s)

        while idx < n and s[idx] == ' ':
            idx += 1
        # whitespace done

        if idx < n and (s[idx] == '+' or s[idx] == '-'):
            if s[idx] == '-':
                sign = -1
            idx += 1
        # signed 

        while idx < n and '0'<=s[idx]<='9':
            ans = ans*10 + int(s[idx])
            idx += 1
        # conversion
        ans = sign*ans

        if sign is -1:
            if ans >= -1*(2**31):
                return ans
            else:
                return -(2**31)
        if ans >= 2**31 -1:
            return 2**31 -1 
        return ans