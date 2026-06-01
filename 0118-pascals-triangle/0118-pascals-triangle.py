class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*(i+1) for i in range(numRows)]

        for i in range(0,numRows):
            ans[i][0] = 1; ans[i][-1] = 1
            left = 1; right = len(ans[i])
            if i > 1:
                while left < right-1:
                    ans[i][left] = ans[i-1][left-1] + ans[i-1][left]
                    left += 1
        return ans