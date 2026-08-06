# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # just by watching the problem I can say it is related to level order traversal, 
        from collections import deque
        queue = deque([])

        queue.append([root,0])
        ans = 1
        while queue:
            size = len(queue)
            
            p1 = queue[0][1]; p2 = queue[-1][1]
            ans = max(ans,p2-p1+1)

            for i in range(0,size):
                t,i = queue.popleft()
                
                if t.left:
                    queue.append([t.left,2*i + 1])
                if t.right:
                    queue.append([t.right,2*i+2])

        return ans