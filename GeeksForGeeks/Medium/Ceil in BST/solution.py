'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        ans = 10**9
        temp = root
        while temp:
            if x == temp.data :
                return x 
            elif x > temp.data:
                
                temp = temp.right 
            else:
                # x < temp.val
                ans = min(ans,temp.data)
                temp = temp.left
        return ans if ans != 10**9 else -1