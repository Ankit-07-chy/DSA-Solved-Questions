class Solution {

    boolean palindrome(String s, int l, int r) {
        while (l <= r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }

    public int palPartition(String s) {

        int n = s.length();

        int[] dp = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {

            int t = 100000000;

            for (int j = i; j < n; j++) {

                if (palindrome(s, i, j)) {
                    t = Math.min(t, 1 + dp[j + 1]);
                }
            }

            dp[i] = t;
        }

        return dp[0] - 1;
    }
}
/*
class Solution:
    def palPartition(self, s):
        # code here
        n = len(s)
        dp = [0]*(n+1)
        
        def palindrome(s):
            i = 0; j = len(s)-1
            while i <=j:
                if s[i] != s[j]:
                    return False
                i += 1; j -= 1
            return True
        
        for i in range(n-1,-1,-1):
            t = 10**8 
            for j in range(i,n):
                # string = s[i:j+1]
                if palindrome(s[i:j+1]):
                    t = min(t,1+dp[j+1])
            dp[i] = t
        # print(dp)
        return dp[0] - 1
*/