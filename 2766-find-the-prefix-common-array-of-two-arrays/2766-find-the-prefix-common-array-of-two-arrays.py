class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        n = len(A)
        ans = [0]*n
        for i in range(1,n+1):
            freq[i] = 0
        count = 0
        idx = 0
        for u,v in list(zip(A,B)):
            freq[u] += 1
            if freq[u] > 1:
                count += 1
            freq[v] += 1
            if freq[v] > 1:
                count += 1
            ans[idx] = count
            idx += 1
        return ans
'''
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        n = len(A)
        ans = [0]*n
        def check(freq,idx):
            count = 0
            for u,v in freq.items():
                if len(v)>1:
                    temp = True
                    for e in v:
                        if e > idx:
                            temp = False
                    if temp:
                        count += 1
            return count

        for i in range(n):
            freq[A[i]] = [i]

        for i in range(n):
            element = B[i]
            freq[element].append(i)
            ans[i] = check(freq,i)
        return ans
        '''