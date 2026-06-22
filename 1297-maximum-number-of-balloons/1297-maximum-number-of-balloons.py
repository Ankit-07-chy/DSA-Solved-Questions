class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for c in 'balloon':
            d[c] = 0
        for char in text:
            if char in d:
                d[char] += 1
        ans = 0
        while True:
            for char in 'balloon':
                if d[char]>0:
                    d[char] -= 1
                else:
                    return ans
            ans += 1
