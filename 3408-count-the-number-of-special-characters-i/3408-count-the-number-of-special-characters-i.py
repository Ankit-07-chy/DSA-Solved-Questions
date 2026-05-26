class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charU = [0]*26
        charL = [0]*26
        for _ in word:
            temp = ord(_)
            if 97<=temp<=122:
                charL[temp-97] += 1
            else:
                charU[temp-65] += 1
        count = 0
        for u,v in list(zip(charU,charL)):
            if u> 0 and v > 0:
                count += 1
        return count
