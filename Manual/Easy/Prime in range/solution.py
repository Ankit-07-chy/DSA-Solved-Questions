class Solution:
    def primeRange(self, l, r):
        # code here
        
        prime = [1]*(r+1)
        prime[0] = prime[1] = 0
        for i in range(2,r+1):
            if prime[i] == 1:
                for j in range(i*i,r+1,i):
                    prime[j] = 0
        ans = []
        for i in range(l,r+1):
            if prime[i] == 1:
                ans.append(i)
        return ans