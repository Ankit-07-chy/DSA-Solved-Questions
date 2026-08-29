# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        n = len(preorder)
        inorder_idx = {}
        for i,v in enumerate(inorder):
            inorder_idx[v] = i
        
        def buildTree(pl,pr,il,ir):
            if pl > pr or il > ir:
                return None
            root = TreeNode(preorder[pl])
            idx_in = inorder_idx[preorder[pl]]
            size = idx_in - il 
            root.left = buildTree(pl+1,pl+size,il,il+size-1)
            root.right = buildTree(pl+size+1,pr,il+size+1,ir)
            return root
        return buildTree(0,n-1,0,n-1)