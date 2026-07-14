class Solution {

    public int find(int[] arr) {

        int low = 0;
        int high = 0;

        for (int x : arr) {
            high = Math.max(high, x);
        }

        int ans = high;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (check(arr, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }

    private boolean check(int[] arr, long x) {

        final long LIMIT = Long.MAX_VALUE / 4;

        for (int ele : arr) {

            if (x > LIMIT) {
                x = LIMIT;
            } else {
                x = 2L * x - ele;
            }

            if (x < 0) {
                return false;
            }
        }

        return true;
    }
}