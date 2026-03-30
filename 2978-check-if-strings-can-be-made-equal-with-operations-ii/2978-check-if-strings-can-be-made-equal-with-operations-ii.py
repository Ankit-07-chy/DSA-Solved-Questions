class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        odd = [0]*26
        even = [0]*26
        for i in range(n):
            if i % 2 ==0:
                even[ord(s1[i])-97] += 1
                even[ord(s2[i])-97] -= 1
            else:
                odd[ord(s1[i])-97] += 1
                odd[ord(s2[i])-97] -= 1
        for u,v in zip(odd,even):
            if u != 0 or v!=0:
                return False 
        return True
