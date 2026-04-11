class Solution:
    def minOperations(self, nums: list[int]) -> int:

        """
        Brute Force
        """
        count = 0
        def check_prime(number):
            if number < 2:
                return False
            for i in range(2,int(number**0.5)+1):
                if number % i == 0:
                    return False
            return True
            
        for idx,val in enumerate(nums):
            if idx % 2 == 0:
                # prime
                t = check_prime(val)
                while not t:
                    val += 1
                    count += 1
                    t = check_prime(val)
            else:
                # non-prime
                t = check_prime(val)
                while t:
                    val += 1
                    count += 1
                    t = check_prime(val)
        return count
            