class Solution:
    def isPalindromic(self, s: str) -> bool:
        # return bin(int(ord(s[0])))
        p = ''
        for c in s:
            temp = f'{ord(c):08b}'
            p += temp 
        return p == p[::-1]