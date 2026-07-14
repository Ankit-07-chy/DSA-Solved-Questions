class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    if head is None:
        return None
    temp = head 
    if temp.next == None:
        return None
    while temp.next != None:
        temp = temp.next 
    temp = temp.prev 
    temp.next = None 
    

    return head 

