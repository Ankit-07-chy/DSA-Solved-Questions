# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # mirrored should have together, and in incresing order of level
        freq = {}
        def traversal(temp,mirror,level):
            if temp == None:
                return
            if mirror in freq:
                freq[mirror].append([level,temp.val])
            else:
                freq[mirror] = [[level,temp.val]]
            traversal(temp.left,mirror-1,level+1)
            traversal(temp.right,mirror+1,level+1)
        t = root
        traversal(t,0,0)
        freq = dict(sorted(freq.items()))
        result = []
        for u,v in freq.items():
            t1 = []
            v.sort(key=lambda x: (x[0], x[1]))
            for tp in v:
                t1.append(tp[-1])
            result.append(t1) # Here We have to Sort this based on tp[0]
        return result