class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        int[][] dp = new int[n + 1][n + 1];

        // i from n-1 to 0 and j from i+1 to n-1
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {

                // find total Sum
                int totalSum = 0;
                for (int k = i; k <= j; k++) {
                    totalSum += stoneValue[k];
                }

                // now recursion wala part
                int maxi = -1000000000;
                int currSum = 0;
                
                for (int k = i; k < j; k++) {
                    currSum += stoneValue[k];

                    int remSum = totalSum - currSum;
                    int s1 = 0, s2 = 0, s3 = 0;
                    
                    if (remSum > currSum) {
                        s1 = currSum + dp[i][k];
                    } else if (remSum < currSum) {
                        s2 = remSum + dp[k + 1][j];
                    } else {
                        s3 = currSum + Math.max(dp[i][k], dp[k + 1][j]);
                    }
                    
                    maxi = Math.max(maxi, Math.max(s1, Math.max(s2, s3)));
                }
                
                dp[i][j] = maxi;
            }
        }
        return dp[0][n - 1];
    }
}