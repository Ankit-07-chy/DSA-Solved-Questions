'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Code Here
        temp = head
        idx = 0
        while idx < p and temp:
            temp = temp.next
            idx += 1
        new_node = Node(x)
        if temp.next == None:
            temp.next = new_node
            new_node.prev = temp
        else:
            next_node = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = next_node
            next_node.prev = new_node
        return head
        
        