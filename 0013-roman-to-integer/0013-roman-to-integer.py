class Solution:
    def romanToInt(self, s: str) -> int:
        freq = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        n = len(s)
        for i in range(len(s)-1):
            curr = s[i]
            next = s[i+1]
            curr = freq[curr]
            next = freq[next]
            if curr > next:
                total += curr
            elif curr == next:
                total += curr
            else:
                total -= curr
        return total + freq[s[n-1]]
            