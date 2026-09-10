# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        ans = 0
        def traverse(node):
            nonlocal ans 
            if node == None:
                return 0,0
            left_sum,left_count = traverse(node.left)
            right_sum,right_count = traverse(node.right)
            avg = (left_sum+right_sum+node.val) // (left_count+right_count + 1)
            if avg == node.val:
                ans += 1
            return (left_sum+right_sum+node.val) , (left_count+right_count + 1)
        traverse(root)
        return ans