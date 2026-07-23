class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        # count = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
                # count += 1
            if char == ')':
                # count -= 1
                low -= 1
                high -=1 
            if char == '*':
                low -= 1
                high += 1

            
            if low < 0:
                low  = 0
            if high < 0:
                return False
        if low<=0<=high:
            return True
        return False