# recursion + memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1); m = len(word2)
        dp = [[None]*(m+1) for i in range(n+1)]

        def recursion(i,j):
            if i < 0:
                return j + 1
            elif j < 0:
                return i + 1
            
            elif word1[i] == word2[j]:
                if dp[i][j] == None:
                    dp[i][j] = recursion(i-1,j-1)
                return dp[i][j]
            else:
                if dp[i][j] == None:
                    insert = 1 + recursion(i,j-1)
                    delete = 1 + recursion(i-1,j)
                    replace = 1 + recursion(i-1,j-1)
                    dp[i][j] = min([insert,delete,replace])
                return dp[i][j]

        return recursion(n-1,m-1)



# Python inbuild Cache

'''
from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       
        n = len(word1); m = len(word2)

        @cache
        def recursion(i,j):
            # base case
            if i < 0:
                return j + 1
            elif j < 0:
                return i + 1

            elif word1[i] == word2[j]:
                return recursion(i-1,j-1)
            else:
                insert = 1 + recursion(i,j-1)
                delete = 1 + recursion(i-1,j)
                replace = 1 + recursion(i-1,j-1)
                return min([insert,delete,replace])

        return recursion(n-1,m-1)
        '''