'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        
        # first I will find left nodes, then leaf nodes and then right nodes -> o(3n + ln(n)n)
        left = []
        def leftPart(node):
            if node == None :
                return 
            if node.left == None and node.right == None:
                return 
            left.append(node.data)
            if node.left:
                leftPart(node.left)
            else:
                leftPart(node.right)
        if root.left:
            leftPart(root)
        elif root.left == None and root.right != None:
            left.append(root.data)
        
        leaf = []
        def leafPart(node):
            if node == None:
                return 
            if node.left == None and node.right == None:
                leaf.append(node.data)
                return 
            if node:
                leafPart(node.left)
                leafPart(node.right)
        leafPart(root)
        
        right = []
        def rightPart(node):
            if node == None:
                return 
            if node.left == None and node.right == None:
                return
            right.append(node.data)
            if node.right:
                rightPart(node.right)
            else:
                rightPart(node.left)
        if root.right:
            rightPart(root.right)
            
        # print(left,leaf,right)
        return left + leaf + right[::-1]
            
            