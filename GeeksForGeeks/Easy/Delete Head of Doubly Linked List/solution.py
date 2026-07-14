def deleteHead(head):
    #code here
    
    temp = head
    head = head.next
    if head :
        head.prev = None
    return head