'''
Structure of a Binary Search Tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        # code here
        suc = None
        
        def successor(node,k):
            nonlocal suc
            if node == None:
                return None
            if node.data > k:
                suc = node
                successor(node.left,key)
            else:
                successor(node.right,key)
        successor(root,key)
        
        pre = None
        def predecessor(node,k):
            nonlocal pre
            if node == None:
                return None
            if node.data < k:
                pre = node
                predecessor(node.right,k)
            else:
                predecessor(node.left,k)
                
        predecessor(root,key)
        return [pre,suc]