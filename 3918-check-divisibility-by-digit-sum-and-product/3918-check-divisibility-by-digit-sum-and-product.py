class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        temp = str(temp)
        sumi = 0
        prod = 1
        for s in temp:
            sumi += int(s)
            prod *= int(s)
        if n % (sumi+prod) == 0:
            return True
        return False