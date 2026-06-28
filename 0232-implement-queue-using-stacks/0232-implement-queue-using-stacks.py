class MyQueue:

    def __init__(self):
        self.queue = []
        self.idx_init = 0
        self.idx_curr = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.idx_curr += 1

    def pop(self) -> int:
        self.idx_init += 1
        if self.idx_init - 1 < 0:
            return 
        return self.queue[self.idx_init - 1]

    def peek(self) -> int:
        if self.idx_init < 0:
            return 
        return self.queue[self.idx_init]
        

    def empty(self) -> bool:
        return self.idx_curr - self.idx_init == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()