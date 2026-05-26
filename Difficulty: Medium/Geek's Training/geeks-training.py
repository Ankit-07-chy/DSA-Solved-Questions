class Solution:
    def maximumPoints(self, mat):
        # code here
        n = len(mat)
        dp = [[-1]*4 for i in range(n)]
        # choose each row element in manner so that will get maxi
        def fxn(day,idx,dp):
            if day == 0:
                maxi = 0
                for i in range(3):
                    if i != idx:
                        maxi = max(maxi,mat[0][i])
                return maxi
            
            if dp[day][idx] == -1:
                maxi = 0
                for i in range(3):
                    if i != idx:
                        curr= fxn(day-1,i,dp) + mat[day][i]
                        maxi = max(curr,maxi)
                dp[day][idx] = maxi
                
            return dp[day][idx]
                        
        return fxn(n-1,3,dp) #day,last_idx