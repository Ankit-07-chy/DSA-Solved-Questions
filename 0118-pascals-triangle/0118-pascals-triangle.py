class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        if numRows == 1:
            return ans
        for i in range(1,numRows):
            
            prev_row = ans[i-1]
            curr = [1]*(1 + len(prev_row))
            for j in range(1,len(prev_row)):
                curr[j] = prev_row[j] + prev_row[j-1]
            ans.append(curr)
        return ans