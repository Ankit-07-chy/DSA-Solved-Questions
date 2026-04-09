# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Do levelordertraversal and in that if something is coming at that level at last put only that
        result = [-200]*100

        def level_order(root):
            if root == None:
                return 
            q = deque([])
            q.append((root,0))
            while q:
                curr,lev = q.popleft()
                if curr.left:
                    q.append((curr.left,lev+1))
                if curr.right:
                    q.append((curr.right,lev+1))
                result[lev] = curr.val
        level_order(root)
        r = []
        for u in result:
            if u != -200:
                r.append(u)
        return r
                    
            
