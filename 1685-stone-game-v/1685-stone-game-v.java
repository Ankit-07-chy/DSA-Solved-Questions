import java.util.Arrays;

class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        
        // Prefix sums for O(1) range sum queries
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + stoneValue[i];
        }
        
        int[][] dp = new int[n][n];
        
        // Tabulation loop by subarray length
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                int maxi = 0;
                
                for (int k = i; k < j; k++) {
                    // Sum of left part: stoneValue[i...k]
                    int leftSum = pref[k + 1] - pref[i];
                    // Sum of right part: stoneValue[k+1...j]
                    int rightSum = pref[j + 1] - pref[k + 1];
                    
                    int s1 = 0, s2 = 0, s3 = 0;
                    if (leftSum < rightSum) {
                        s1 = leftSum + dp[i][k];
                        maxi = Math.max(maxi, s1);
                    } else if (leftSum > rightSum) {
                        s2 = rightSum + dp[k + 1][j];
                        maxi = Math.max(maxi, s2);
                    } else {
                        s3 = leftSum + Math.max(dp[i][k], dp[k + 1][j]);
                        maxi = Math.max(maxi, s3);
                    }
                }
                
                dp[i][j] = maxi;
            }
        }
        
        return dp[0][n - 1];
    }
}