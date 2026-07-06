class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)

        # Previous Smaller or Equal
        psee = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                psee[i] = stack[-1]
            stack.append(i)

        # Next Smaller
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            ans = (ans + arr[i] * left * right) % mod

        return ans

# Brute force
'''
mod = 10**9 + 7
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            mini = inf
            for j in range(i,n):
                mini = min(mini,arr[j])
                ans += mini
                # ans = ans%mod

        return ans % mod'''