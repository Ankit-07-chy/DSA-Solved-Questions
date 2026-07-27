def pow(a,b):
    if b == 1:
        return a
    if b == 0:
        return 1
    half = pow(a,b//2)
    if b%2 == 0:
        return (half*half)%((10**9)+7)
    else :
        return (a*half*half)%((10**9)+7)

class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = int(n/2)
        if n == 1:
            return 5
        if n%2 ==0 :
            return (4*pow(5,(p-1))*5*pow(4,(p-1)))%((10**9)+7)
        else : 
            return (5*(pow(4,p)*pow(5,p)))%((10**9)+7)
        