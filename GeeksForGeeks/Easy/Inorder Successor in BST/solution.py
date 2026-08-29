'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrderSuccessor(self, root, k):
        # code here
        suc = None
        def inorder(node,k):
            nonlocal suc
            if node == None:
                return 
            if node.data > k.data:
                suc = node.data
                inorder(node.left,k)
            else:
                inorder(node.right,k)
        inorder(root,k)
        return suc if suc else -1