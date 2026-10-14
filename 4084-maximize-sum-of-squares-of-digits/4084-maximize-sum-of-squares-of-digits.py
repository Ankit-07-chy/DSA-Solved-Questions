class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        number = []
        while sum:
            if sum >= 9:
                number.append(9)
                sum = sum - 9
            else:
                number.append(sum)
                sum = 0
        if len(number) > num:
            return ''
        elif len(number) == num:
            return ''.join(str(c) for c in number)
        else:
            remaining = num - len(number)
            t = '0'*remaining
            t1 = ''.join(str(c) for c in number)
            return t1 + t
            

        '''
        left = 0
        right = 2000000
        ans = None

        def fxn(number):
            count_digits = 0
            sumi = 0
            for c in str(number):
                count_digits += 1
                sumi += int(c)
            if count_digits == num and sumi == sum:
                return True
            return False

        while left <= right:
            # print('HEre')
            mid = (left + right) // 2
            if fxn(mid) == True:
                left = mid + 1
                ans = mid 
            else:
                right = mid - 1
        if ans is not None:
            return str(ans)
        return ''
        '''