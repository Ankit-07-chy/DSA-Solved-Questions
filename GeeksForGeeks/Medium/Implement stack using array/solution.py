
        
class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.array = []
        self.size = n
        self.idx_curr = 0
        self.idx_init = 0

    def isEmpty(self):
        # Check if stack is empty
        return self.idx_curr - self.idx_init == 0

    def isFull(self):
        # Check if stack is full
        return self.idx_curr - self.idx_init == self.size

    def push(self, x):
        # Insert x at the top of the stack
        if not self.isFull():
            self.array.append(x)
            self.idx_curr += 1
            return True
        return False

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return False
        
        self.idx_curr -= 1
        self.array.pop()
        return True

    def peek(self):
        # Returns the top element of the stack without removing it
        if self.isEmpty():
            return -1
        
        return self.array[-1]