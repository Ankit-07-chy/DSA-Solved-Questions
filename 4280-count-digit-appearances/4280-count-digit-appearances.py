class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        def check(num,digit):
            temp = 0
            while num:
                rem = num % 10
                num = num//10
                if rem == digit:
                    temp += 1
            return temp
        for u in nums:
            count += check(u,digit)
        return count