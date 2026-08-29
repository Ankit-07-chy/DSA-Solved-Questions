# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node,ll,lr):
            if node == None:
                return True
            left = inorder(node.left,ll,min(lr,node.val))
            
            if node.val <= ll or node.val >= lr:
                return False
            right = inorder(node.right,max(ll,node.val),lr)

            return left and right
        return inorder(root,-inf,+inf)