class Solution:
    def processStr(self, s: str, k: int) -> str:
        lenght = 0
        for char in s:
            if char == '*':
                if lenght > 0:
                    lenght -= 1
            elif char == '#':
                lenght *= 2
            elif char == '%':
                pass
            else:
                lenght += 1
        
        if k >= lenght:
            return '.'
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i] == '*':
                lenght += 1
            elif s[i] == '#':
                lenght /= 2
                if k >= lenght:
                    k = k-lenght
            elif s[i] == '%':
                k = lenght - k - 1
            else:
                lenght -= 1
            
            if lenght == k:
                return s[i]


# brute force
'''
class Solution:
    def processStr(self, s: str, k: int) -> str:
        result = []
        for char in s:
            if char == '*':
                if result:
                    result.pop()
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
            else:
                result.append(char)
        if len(result)> k:
            return result[k]
        return '.'
        '''