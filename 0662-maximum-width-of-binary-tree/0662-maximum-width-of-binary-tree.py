# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        queue = deque([])

        ans = 0
        queue.append([root,0])
        while queue:
            ans = max(ans,queue[-1][-1]-queue[0][-1]+1)
            i = 0
            for i in range(0,len(queue)):
                node,idx = queue.popleft()
                if node.left:
                    queue.append([node.left,2*idx+1])
                if node.right:
                    queue.append([node.right,2*idx+2])
        return ans
                