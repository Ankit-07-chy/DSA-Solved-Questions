# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}; parent_ = set(); child_ = set()
        for d in descriptions:
            parent = d[0]; child = d[1]; isLeft = d[2]
            if parent in hashmap:
                parent_node = hashmap[parent]
            else:
                parent_node = TreeNode(parent,None,None)
            
            if child in hashmap:
                child_node = hashmap[child]
            else:
                child_node = TreeNode(child,None,None)
            
            if isLeft == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            hashmap[parent] = parent_node
            hashmap[child]= child_node
            parent_.add(parent_node)
            child_.add(child_node)

        # Tree creation was occur successfully now which one will be root?
        root = (parent_ - child_).pop()
        return root