
# optimized one
class Solution:
    def celebrity(self, mat):
        n = len(mat)

        for i in range(n):
            mat[i][i] = 0
            
        up = 0
        bottom = n-1
        
        while up < bottom:
            if mat[up][bottom] == 1:
                up += 1
            elif mat[bottom][up] == 1:
                bottom -= 1
            else:
                up += 1
                bottom -=1 
        
        iKnow = 0
        knowMe = 0
        for i in range(n):
            if mat[up][i] == 1:
                iKnow += 1
            if mat[i][up] == 1:
                knowMe += 1
        if iKnow == 0 and knowMe == n - 1:
            return up
        return -1
            

# brute force

'''
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
        return -1'''
