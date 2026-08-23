class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum = 0; right_sum = 0
        leftQ = 0; rightQ = 0
        n = len(num)
        for i in range(0,n//2):
            if num[i] == '?':
                leftQ += 1
            else:
                left_sum += int(num[i])
        for i in range(n//2,n):
            if num[i] == '?':
                rightQ += 1
            else:
                right_sum += int(num[i])
        if (leftQ + rightQ) % 2== 1:
            return True
        else:
            if 2*left_sum + 9*leftQ != 2*right_sum + 9*rightQ:
                return True
        return False