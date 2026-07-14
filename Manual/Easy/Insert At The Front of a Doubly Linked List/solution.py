from typing import Optional


class Node:
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

def insertAtFront(head: Optional[Node], k: int) -> Node:
    # Write your code here.
    if not head:
        return Node(k)
    new_node = Node(k)
    new_node.next = head 
    head.prev = new_node
    head = head.prev 
    return head