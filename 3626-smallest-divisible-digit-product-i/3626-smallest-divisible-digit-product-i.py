class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def find_product(n):
            temp = 1
            while n :
                t = n% 10
                temp = temp * t
                n = n//10
            return temp

        n_prod = find_product(n)
        # print(n_prod)
        if n_prod == 0:
            return n
        else:
            if n_prod % t == 0:
                return n
            increment = t - (n_prod% t)

        # while increment:
        while True:
            if find_product(n)% t == 0:
                return n
            n = n+1