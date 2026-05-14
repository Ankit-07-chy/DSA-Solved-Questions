class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq = {}
        for u,v in list(zip(s,t)):
            if u in freq:
                temp = (freq[u] == v)
                if temp == False:
                    return False
            else:
                freq[u] = v
        freq = {}
        for u,v in list(zip(t,s)):
            if u in freq:
                temp = (freq[u] == v)
                if temp == False:
                    return False
            else:
                freq[u] = v
        return True