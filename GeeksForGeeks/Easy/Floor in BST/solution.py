'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        ans = -1
        temp = root
        while temp:
            if temp.data == k:
                return k 
            elif temp.data > k:
            
                temp = temp.left
            else:
                # temp.data < k 
                ans = temp.data
                temp = temp.right
                
        return ans