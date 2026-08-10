from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D Dp Problem it is , lets do recursion first then will memoize it
        n1 = len(text1); n2 = len(text2)
        
        @cache
        def recursion(i,j):
            if i >= n1 or j >= n2:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + recursion(i+1,j+1)
            else:
                t1 = recursion(i+1,j)
                t2 = recursion(i,j+1)
                return max(t1,t2)
                
        return recursion(0,0)