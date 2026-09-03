class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        ans = 0
        curr_sign = '+'
        if i < n and s[i] == '+':
            curr_sign = '+'
            i += 1
        elif i < n and s[i] == '-':
            curr_sign = '-'
            i += 1
       
        while i < n :
            if s[i] in '0123456789':
                ans = 10*ans + int(s[i])
                i += 1
            else:
                break 
            if curr_sign == '+' and ans > 2**31 - 1:
                return 2**31 - 1
            elif curr_sign == '-' and -ans < -2**31:
                return - 2**31
        
        if curr_sign == '-':
            return -ans 
        return ans