class myQueue:
    def __init__(self, n):
        self.size = n
        self.array = []
        self.curr_idx = 0
        self.init_idx = 0

    def isEmpty(self):
        return self.curr_idx == self.init_idx

    def isFull(self):
        return self.curr_idx - self.init_idx == self.size

    def enqueue(self, x):
        if self.isFull():
            return False
        
        self.array.append(x)
        self.curr_idx += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        
        x = self.array[self.init_idx]
        self.init_idx += 1
        return x

    def getFront(self):
        if self.isEmpty():
            return -1
        
        return self.array[self.init_idx]

    def getRear(self):
        if self.isEmpty():
            return -1
        
        return self.array[self.curr_idx - 1]