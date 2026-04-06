class ListNode:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index<0:
            return -1
        else:
            temp = self.head
            i =0
            while i<index :
                temp = temp.next
                i += 1
            return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val,self.head)
        self.head = new_node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val,None)
        temp = self.head
        if not temp:
            self.head = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        new_node = ListNode(val,None)
        current = self.head
        
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)