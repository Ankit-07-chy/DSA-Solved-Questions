"""
Structure of doubly linked list node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        
        temp = head
        
        while temp:
            _temp = temp.prev
            temp_ = temp.next
            
            curr_ = temp.next
            
            temp.next = _temp
            temp.prev = temp_
            
            if curr_:
                temp = curr_
            else:
                return temp
        # return temp.next
            
            