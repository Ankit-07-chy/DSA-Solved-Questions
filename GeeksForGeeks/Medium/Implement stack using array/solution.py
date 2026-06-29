class myStack:
    def __init__(self, n):
        self.array = [-1] * n
        self.top = -1
        self.size = n

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, x):
        if self.isFull():
            return False
        
        self.top += 1
        self.array[self.top] = x
        return True

    def pop(self):
        if self.isEmpty():
            return False
        
        self.array[self.top] = -1
        self.top -= 1
        return True

    def peek(self):
        if self.isEmpty():
            return -1
        
        return self.array[self.top]


    
        
        '''
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
        '''
