'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        # children sum property : 
        
        def childProperty(root):
            if root == None:
                return True
            if root.left == None and root.right == None:
                return True
            left_val = 0 if root.left == None else root.left.data
            right_val = 0 if root.right == None else root.right.data
            if root.data != left_val + right_val:
                return False 
            find_left = childProperty(root.left)
            find_right = childProperty(root.right)
            
            return find_left and find_right
        return childProperty(root)