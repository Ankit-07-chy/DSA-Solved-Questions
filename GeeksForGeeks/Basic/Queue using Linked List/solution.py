# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class
class myQueue:

    def __init__(self):
        self.capacity = 0
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, x):
        new_node = Node(x)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.capacity += 1

    def dequeue(self):
        if self.front is None:
            return -1

        num = self.front.data
        self.front = self.front.next
        self.capacity -= 1

        # If queue becomes empty, update rear also
        if self.front is None:
            self.rear = None

        return num

    def getFront(self):
        if self.front is None:
            return -1
        return self.front.data

    def size(self):
        return self.capacity






