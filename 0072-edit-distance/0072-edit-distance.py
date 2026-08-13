from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        9 + 9 - 5 -5
        '''
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