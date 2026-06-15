class Solution {
    public List<Integer> maxMeetings(int[] s, int[] f) {
        // code here
        
        int n = s.length;
        int[][] meetings = new int[n][3];
        
        for(int i =0; i < n; i++){
            meetings[i][0] = s[i];
            meetings[i][1] = f[i];
            meetings[i][2] = i+1;
        }
        
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[1], b[1]));

        List<Integer> ans = new ArrayList<>();

        int freeTime = -1;

        for (int i = 0; i < n; i++) {
            if (meetings[i][0] > freeTime) {
                ans.add(meetings[i][2]);
                freeTime = meetings[i][1];
            }
        }

        Collections.sort(ans);
        return ans;
        
    }
}
