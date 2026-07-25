class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(str(n)) #--> o(1)
        # print(n)

        n.sort() # -> o(1)
        return int(n[-1])*int(n[-2])
