class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0]*26
        for _ in s:
            t1 = ord(_) - 97
            chars[t1] += 1
        # print(chars)
        for _ in t:
            t1 = ord(_) - 97
            chars[t1] -= 1
        # print(chars)
        for u in chars:
            if u != 0:
                return False
        return True