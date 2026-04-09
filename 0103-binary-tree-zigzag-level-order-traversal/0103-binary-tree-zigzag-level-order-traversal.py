# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result = []
        q = deque([])
        q.append(root)
        p = 0
        while q:
            size = len(q)
            temp = []
            for i in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                temp.append(curr.val)
            if p%2 == 0:
                result.append(temp[:])
            else:
                result.append(temp[::-1][:])
            p += 1
        return result
