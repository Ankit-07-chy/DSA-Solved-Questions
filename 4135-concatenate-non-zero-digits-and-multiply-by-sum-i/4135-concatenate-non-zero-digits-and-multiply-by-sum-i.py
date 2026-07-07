class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = list(str(n))
        new_num = []
        for i in num:
            if i != '0':
                new_num.append(i)
        sumi = sum(int(i) for i in new_num)
        new_num = ''.join(new_num)
        if not new_num:
            return 0
        new_num = int(new_num)
        return new_num*sumi