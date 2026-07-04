class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = height[0]; rightMax = height[-1]
        ans = 0
        l = 0; r = n-1
        while l < r:
            
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                ans += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax,height[r])
                ans += rightMax - height[r]
                
        return ans


'''class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        monotonic_stack_left = [0]
        for i in range(1,n):
            monotonic_stack_left.append(max(height[i-1],monotonic_stack_left[-1]))
        # print(monotonic_stack_left)
        monotonic_stack_right = [0]*(n)
        for i in range(n-2,-1,-1):
            monotonic_stack_right[i] = max(height[i+1],monotonic_stack_right[i+1])
        # print(monotonic_stack_right)

        ans = 0
        l = list(zip(height,monotonic_stack_left,monotonic_stack_right))
        for i in range(1,n-1):
            u,v,z = l[i]
            temp = min(v,z) - u
            if temp > 0:
                ans += temp
        return ans'''