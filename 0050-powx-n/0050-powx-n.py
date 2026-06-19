class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fxn(base, exponent):
            result = 1.0
            while exponent > 0:
                if exponent % 2 == 1:  # If exponent is odd
                    result *= base
                base = base * base
                exponent = exponent // 2
            return result
        
        if n >= 0:
            return fxn(x, n)
        else:
            return 1.0 / fxn(x, -n)  # Use absolute value for negative exponent