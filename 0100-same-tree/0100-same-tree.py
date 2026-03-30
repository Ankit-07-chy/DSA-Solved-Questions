# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            # Both nodes are None - they're equal
            if not p and not q:
                return True
            
            # One is None, the other isn't - they're different
            if not p or not q:
                return False
            
            # Values are different - they're different
            if p.val != q.val:
                return False
            
            # Recursively check left and right subtrees
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        return isSame(p, q)