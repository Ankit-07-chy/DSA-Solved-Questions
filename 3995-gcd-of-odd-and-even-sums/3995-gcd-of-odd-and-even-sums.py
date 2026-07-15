class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_n_sum = n*(n+1)
        n_ = 2*n
        odd_n_sum = int((n_*(n_+1))/2 - even_n_sum)

        #print(even_n_sum,odd_n_sum)
        import math
        return math.gcd(odd_n_sum,even_n_sum)