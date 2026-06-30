# Structure of linked list Node
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:

    def __init__(self):
        # Initialize your data members
        self.top = None
        self.capacity = 0
        

    def isEmpty(self):
        # Check if the stack is empty
        return self.top == None
        

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.capacity += 1

    def pop(self):
        # Removes an element from the top of the stack
        self.capacity -=1 
        if self.isEmpty():
            return 
        val = self.top.data
        self.top = self.top.next


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1 
        return self.top.data


    def size(self):
        # Returns the current size of the stack
        return self.capacity