class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total
# This Gives TLE
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        '''
        Brute Force : 
            Generate all Substring -> n^2
            check char if all different present then True -> n
            count increase -> 1

            Space Complexity : 

        '''
        n = len(s)
        ans = 0
        for i in range(n):
            arr = [0]*3
            for j in range(i,n):
                if s[j] == 'a':
                    arr[0] += 1
                elif s[j] == 'b':
                    arr[1] += 1
                else:
                    arr[2] += 1

                if arr[0]>0 and arr[1]>0 and arr[2]>0:
                    ans += 1
        return ans
        """