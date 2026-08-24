"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def paths(self, root):
        # code here
        result = []
        
        def preorder(node,stack):
            if node == None:
                return 
            stack.append(node.data)
            if node.left == None and node.right == None:
                result.append(stack.copy())
            else:
                preorder(node.left,stack)
                preorder(node.right,stack)
            stack.pop()
        preorder(root,[])
        return result
        