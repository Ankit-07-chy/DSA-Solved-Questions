class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        iKnow = [0]*n
        knowMe = [0]*n
        for i in range(n):
            for j in range(n):
                if i != j and mat[i][j] == 1:
                    iKnow[i] += 1
                    knowMe[j] += 1
        for i in range(n):
            if iKnow[i] == 0 and knowMe[i] == n-1:
                return i
        return -1