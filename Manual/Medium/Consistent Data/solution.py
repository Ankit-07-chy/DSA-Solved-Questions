import sys

class Solution:
    def Consistent(self, N: int) -> int:
        # Write your logic here
        MOD = 10**9 + 7
        # first i have to make the sequence
        seq = [0]*N
        for i in range(1,N):
            seq[i] = 1-seq[i-1]
        
        # now wrote recursion in sense of pick & not pick, and fxn(idx,prev_idx)
        def fxn(idx,prev_idx):
            # Base Case
            if idx == N:
                # if prev_idx == -1:
                #     return 0
                return 1 
            pick = 0
            if prev_idx == -1 or seq[prev_idx] != seq[idx]:
                pick = fxn(idx+1,idx)
            not_pick = fxn(idx+1,prev_idx)
            return (pick+not_pick) % MOD 
        return ((fxn(0, -1) - 1 + MOD) % MOD)


def main():
    line = sys.stdin.readline()
    if line:
        N = int(line.strip())
        sol = Solution()
        print(sol.Consistent(N))

if __name__ == "__main__":
    main()