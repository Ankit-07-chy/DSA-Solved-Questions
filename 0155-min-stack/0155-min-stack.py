class MinStack:

    def __init__(self):
        self.stack = [] # stack is list of list -- [[curr_ele,min_ele]]

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append([value,value])
        else:
            mini = self.stack[-1][-1]
            self.stack.append([value,min(value,mini)])
        

    def pop(self) -> None:
        top = self.stack.pop()
        # return top[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()