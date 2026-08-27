class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_height_left = [0]*n
        
        for i in range(1,n):
            max_height_left[i]=(max(height[i-1],max_height_left[i-1]))
        print(max_height_left)
        max_height_right = [0]*n
        for i in range(n-2,-1,-1):
            max_height_right[i] =(max(height[i+1],max_height_right[i+1]))
        print(max_height_right)

        ans = 0
        for i in range(1,n-1):
            curr = min(max_height_left[i],max_height_right[i]) - height[i]
            if curr > 0:
                ans += curr 
        return ans